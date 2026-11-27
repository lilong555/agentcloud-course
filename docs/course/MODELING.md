# 分析模型草稿

下次课的分析对象为“个人工位如何保存现场并继续任务”。本稿依据 [SRS](SRS.md) 和 [UC-08](USE_CASES.md#uc-08-唤醒工位)，描述待评审的领域关系、状态与交互。Workstation 表示工作台展示对象，Session、Manifest、请求和回执字段参考[当前控制器类型](../../internal/control/types.go)。

## 类图草稿

```mermaid
classDiagram
    class Tenant {
        tenantID
    }
    class Workstation {
        displayName
        workspaceID
        sessionID
    }
    class Session {
        state
        gate
        epoch
        actorUID
    }
    class ModelRequest {
        logicalRequestID
        status
        claimedEpoch
    }
    class ToolReceipt {
        toolOpID
        payloadHash
        status
        result
    }
    class LifecycleReceipt {
        operationID
        action
        status
        retryAfter
    }
    class Manifest {
        snapshotUUID
        fidelity
        receiptWatermark
        retainedTagUID
    }
    class SchedulingDecision {
        policy
        observedWaiting
        switchingCost
        action
    }
    Tenant "1" --> "0..*" Workstation : 拥有
    Workstation "1" --> "1" Session : 关联
    Session "1" --> "0..*" ModelRequest : 登记
    Session "1" --> "0..*" ToolReceipt : 保存
    Session "1" --> "0..*" LifecycleReceipt : 记录
    Session "1" --> "0..1" Manifest : 引用当前恢复点
    Session "1" --> "0..*" SchedulingDecision : 产生
    LifecycleReceipt "0..*" --> "0..1" Manifest : 关联
```

领域不变量：一个 workspace 对应一个持久会话；操作 ID 绑定输入；每条请求和回执属于确定租户及会话；恢复基于已提交 manifest 与身份围栏。工位显示名称是课程待补的产品元数据。

## 状态图草稿

```mermaid
stateDiagram-v2
    [*] --> CREATING : 创建工位
    CREATING --> RUNNING : 环境准备并持久确认
    CREATING --> RECOVERY_REQUIRED : 创建结果未知
    RUNNING --> QUIESCING : 决定存档并关闭新工具准入
    QUIESCING --> CHECKPOINTED : 工具排空且快照已提交
    QUIESCING --> SUSPENDED : 存档挂起已确认
    QUIESCING --> RUNNING : 排空超时后取消屏障已确认
    CHECKPOINTED --> SUSPENDED : 复用安全点挂起
    CHECKPOINTED --> RESUMING : 恢复准备
    SUSPENDED --> RESUMING : 容量可用后执行恢复
    RESUMING --> RUNNING : 身份校验通过并推进 epoch
    RESUMING --> SUSPENDED : 权威确认容量拒绝且原身份保持
    RUNNING --> RECOVERY_REQUIRED : 工具结果未知
    QUIESCING --> RECOVERY_REQUIRED : 取消或快照结果未知
    RESUMING --> RECOVERY_REQUIRED : 恢复结果未知
    CHECKPOINTED --> RECOVERY_REQUIRED : 持久状态需核对
```

这是会话生命周期的分析草稿，图中每条箭头表示一个条件明确的流程。SUSPENDING 等实现中间态可在详细设计继续展开。RECOVERY_REQUIRED 的后续处置依赖核对结果，当前用例保存材料并提示人工处理。

工作台采用三个正交维度组合文字状态：生命周期、模型请求状态、容量等待。模型等待可以发生在 RUNNING 或 SUSPENDED；恢复容量回执可以是 WAITING_CAPACITY，确认容量拒绝后会话保持 SUSPENDED。首次准入队列由运行入口单独计量。页面据三者展示“工作中”“等待模型”“已休眠”“唤醒中”“等待容量”或“需要核对”。

## 顺序图草稿

```mermaid
sequenceDiagram
    actor U as 个人用户
    participant W as Web工作台
    participant C as 协调器
    participant J as 持久日志
    participant S as 沙箱与快照服务
    U->>W: 继续休眠工位（UC-08）
    W->>C: 原会话身份与返回需求
    C->>J: 持久登记需求及操作身份
    C->>S: 查询容量并尝试恢复
    alt 权威确认容量不足且原快照身份保持
        S-->>C: 容量拒绝及原 SUSPENDED 身份
        C->>J: WAITING_CAPACITY 和 Retry-After
        C-->>W: 等待容量
        W-->>U: 已等待时间与状态
        W->>C: 按约定时间查询或复用原操作
        C->>S: 继续恢复
    end
    alt 恢复明确成功
        S-->>C: 恢复身份、fidelity 和水位
        C->>J: 校验并提交新 epoch、RUNNING / OPEN
        C-->>W: 确认运行及恢复耗时
        W->>C: 读取原标记文件
        C->>S: file_read（新 epoch）
        S-->>C: 内容和工具结果
        C->>J: 保存工具回执
        C-->>W: 文件内容和持久结果
        W-->>U: 原文件与继续任务入口
    else 恢复或身份结果未知
        C->>J: 保留原身份和 RECOVERY_REQUIRED
        C-->>W: 核对提示与允许的后续动作
        W-->>U: 查看异常详情（UC-13）
    end
```

评审重点：领域对象与需求一致；图中的每条事件有明确来源；容量等待和未知结果均有备选流；Web 状态来自已确认记录。后续设计继续细化接口、并发和恢复围栏，图与需求变更同步进入 PR。
