# 用户故事清单

需求基线 1.0，共 24 条故事。每条指定实际 GitHub 负责人，关联需求、用例和证据，并给出 Given/When/Then。

本表由 [requirements.json](requirements.json) 生成；更新后执行 `python3 scripts/course_requirements.py render`。故事描述课程目标，实现进度以关联 Issue 和验收记录为准。

| 故事 / Issue | 类别 | 需求 | 用例 | 优先级 | 负责人 |
| --- | --- | --- | --- | --- | --- |
| [US-01 #6](https://github.com/lilong555/agentcloud-course/issues/6) 为不同任务创建独立工位 | functional | FR-06 | UC-01 | P0 | @lilong555 |
| [US-02 #7](https://github.com/lilong555/agentcloud-course/issues/7) 从工位列表继续已有任务 | functional | FR-06 | UC-02 | P0 | @lilong555 |
| [US-03 #8](https://github.com/lilong555/agentcloud-course/issues/8) 向工位提交任务并查看助手结果 | functional | FR-07 | UC-03 | P0 | @lilong555 |
| [US-04 #9](https://github.com/lilong555/agentcloud-course/issues/9) 查看工具执行输出和失败原因 | functional | FR-07 | UC-04 | P0 | @lilong555 |
| [US-05 #10](https://github.com/lilong555/agentcloud-course/issues/10) 浏览工作区并读取已有文件 | functional | FR-08 | UC-05 | P0 | @lilong555 |
| [US-06 #11](https://github.com/lilong555/agentcloud-course/issues/11) 保存文件并保留写入回执 | functional | FR-08 | UC-06 | P0 | @lilong555 |
| [US-07 #12](https://github.com/lilong555/agentcloud-course/issues/12) 等待期间自动存档并让出执行槽位 | functional | FR-02 | UC-07 | P0 | @lilong555 |
| [US-08 #13](https://github.com/lilong555/agentcloud-course/issues/13) 唤醒后继续原文件和执行现场 | functional | FR-08 | UC-08 | P0 | @lilong555 |
| [US-09 #14](https://github.com/lilong555/agentcloud-course/issues/14) 资源繁忙时查看容量等待状态 | functional | FR-03 | UC-09 | P0 | @lilong555 |
| [US-10 #15](https://github.com/lilong555/agentcloud-course/issues/15) 看懂工作、存档和唤醒进度 | functional | FR-05 | UC-10 | P0 | @lilong555 |
| [US-11 #16](https://github.com/lilong555/agentcloud-course/issues/16) 刷新后查回原任务结果 | functional | FR-07 | UC-11 | P0 | @lilong555 |
| [US-12 #17](https://github.com/lilong555/agentcloud-course/issues/17) 重复提交同一操作时复用原回执 | functional | FR-07、NFR-01 | UC-12 | P0 | @lilong555 |
| [US-13 #18](https://github.com/lilong555/agentcloud-course/issues/18) 对结果未知的操作执行只读核对 | functional | FR-07、NFR-01 | UC-13 | P0 | @lilong555 |
| [US-14 #19](https://github.com/lilong555/agentcloud-course/issues/19) 查看工位数量与实际资源用量 | functional | FR-05 | UC-14 | P0 | @lilong555 |
| [US-15 #20](https://github.com/lilong555/agentcloud-course/issues/20) 查看有基线和价格来源的费用估算 | functional | FR-09 | UC-15 | P1 | @lilong555 |
| [US-16 #21](https://github.com/lilong555/agentcloud-course/issues/21) 用同一负载对照 TTL 与智能调度 | functional | FR-04 | UC-16 | P0 | @lilong555 |
| [US-17 #22](https://github.com/lilong555/agentcloud-course/issues/22) 让多个有状态工位共享有限槽位 | functional | FR-01 | UC-17 | P0 | @lilong555 |
| [US-18 #23](https://github.com/lilong555/agentcloud-course/issues/23) 验证恢复与重复操作的一致性 | reliability | NFR-01 | UC-08、UC-12、UC-13 | P0 | @lilong555 |
| [US-19 #24](https://github.com/lilong555/agentcloud-course/issues/24) 同时评价资源消耗与交互等待 | measurement | NFR-02 | UC-14、UC-16、UC-17 | P0 | @lilong555 |
| [US-20 #25](https://github.com/lilong555/agentcloud-course/issues/25) 按冻结配置复现演示与实验 | reproducibility | NFR-03 | UC-16、UC-17 | P0 | @lilong555 |
| [US-21 #26](https://github.com/lilong555/agentcloud-course/issues/26) 让个人用户独立完成主要流程 | usability | NFR-04 | UC-01、UC-03、UC-05、UC-08、UC-10 | P0 | @lilong555 |
| [US-22 #27](https://github.com/lilong555/agentcloud-course/issues/27) 及时查询工位与更新状态 | performance | NFR-05 | UC-02、UC-10、UC-11 | P0 | @lilong555 |
| [US-23 #28](https://github.com/lilong555/agentcloud-course/issues/28) 保护个人工位与凭据 | security | NFR-06 | UC-01、UC-02、UC-03、UC-05、UC-06、UC-11、UC-14 | P0 | @lilong555 |
| [US-24 #29](https://github.com/lilong555/agentcloud-course/issues/29) 服务重启后找回已确认结果并展示故障 | availability | NFR-07 | UC-10、UC-11、UC-13 | P0 | @lilong555 |

## US-01 为不同任务创建独立工位

作为同时做课程代码和数据分析的学生，我想为每个任务创建独立云端工位，以便各任务保留各自的文件与进度。

关联：[US-01 #6](https://github.com/lilong555/agentcloud-course/issues/6)；FR-06；UC-01。负责人：@lilong555。

实现基础：会话创建 API 已有；任务名称与 Web 创建入口待实现。

证据：[EV-01](EVIDENCE.md)、[EV-02](EVIDENCE.md)。

验收场景 1：

- Given：已配置有效身份且会话配额充足。
- When：依次创建课程代码、数据分析、实验图表三个工位。
- Then：返回三个不同会话身份，列表可分别进入，向一个工位写入的标记文件只属于该工作区。

验收场景 2：

- Given：一个创建请求已提交。
- When：重复提交相同会话身份和输入或收到配额错误。
- Then：按服务端原身份查询结果或显示配额原因，工作台保留原任务输入。

## US-02 从工位列表继续已有任务

作为在多个项目间切换的个人开发者，我想查看自己的工位并打开原任务，以便切换或刷新后仍能找到工作现场。

关联：[US-02 #7](https://github.com/lilong555/agentcloud-course/issues/7)；FR-06；UC-02。负责人：@lilong555。

实现基础：会话列表与详情 API 已有；工位卡片待实现。

证据：[EV-01](EVIDENCE.md)、[EV-02](EVIDENCE.md)。

验收场景 1：

- Given：当前身份已有三个工位。
- When：刷新列表并打开其中任一工位。
- Then：显示该会话的身份和已确认状态，刷新前后会话身份一致，列表仅含当前租户工位。

## US-03 向工位提交任务并查看助手结果

作为使用 AI 处理代码或数据的个人用户，我想在工位中提交指令并查看进度和结果，以便在一个工作区内完成任务。

关联：[US-03 #8](https://github.com/lilong555/agentcloud-course/issues/8)；FR-07；UC-03。负责人：@lilong555。

实现基础：模型请求与结果认领 API 已有；对话与执行流程待接入。

证据：[EV-01](EVIDENCE.md)、[EV-02](EVIDENCE.md)。

验收场景 1：

- Given：工位可用且受控模型返回一个固定结果。
- When：提交一条任务并等待完成。
- Then：生成稳定 logical_request_id，依次显示已提交和结果，记录结果认领，完成一次模型请求至结果展示闭环。

## US-04 查看工具执行输出和失败原因

作为用助手调试代码的个人开发者，我想看到工具输出、退出码及执行状态，以便判断任务是否完成并定位失败步骤。

关联：[US-04 #9](https://github.com/lilong555/agentcloud-course/issues/9)；FR-07；UC-04。负责人：@lilong555。

实现基础：文件和 shell 工具、回执已有；工具结果界面待实现。

证据：[EV-02](EVIDENCE.md)、[EV-03](EVIDENCE.md)。

验收场景 1：

- Given：工位已获得执行资源且工具 gate 为 OPEN。
- When：执行一个成功工具和一个受控失败工具。
- Then：各自保存独立 tool_op_id，界面对应展示 stdout、stderr、退出码或结构化错误，结果与持久回执一致。

## US-05 浏览工作区并读取已有文件

作为整理课程实验的学生，我想从文件列表打开助手生成的文件，以便直接检查任务产物。

关联：[US-05 #10](https://github.com/lilong555/agentcloud-course/issues/10)；FR-08；UC-05。负责人：@lilong555。

实现基础：file_read 已有；受限目录列表接口与文件浏览待实现。

证据：[EV-01](EVIDENCE.md)、[EV-02](EVIDENCE.md)、[EV-03](EVIDENCE.md)。

验收场景 1：

- Given：工作区内有内容已知的 UTF-8 文件和一个空文件。
- When：打开目录列表并分别读取两个文件及一个缺失路径。
- Then：显示正确相对路径和原内容，空文件显示为空，缺失路径显示 FILE_NOT_FOUND，文件访问遵守工作区路径约束。

## US-06 保存文件并保留写入回执

作为维护实验脚本的研究生，我想在当前工位保存修改后的文件，以便下一步工具执行使用确认过的内容。

关联：[US-06 #11](https://github.com/lilong555/agentcloud-course/issues/11)；FR-08；UC-06。负责人：@lilong555。

实现基础：file_write 与回执已有；编辑保存界面待实现。

证据：[EV-02](EVIDENCE.md)、[EV-03](EVIDENCE.md)。

验收场景 1：

- Given：当前工位处于可写状态且文件大小在 1 MiB 上限内。
- When：用唯一 tool_op_id 保存含随机标记的文本并读回。
- Then：提交成功回执，读回内容与原文本及摘要一致，失败时展示服务端错误并保留待保存文本。

## US-07 等待期间自动存档并让出执行槽位

作为关注云端用量的个人用户，我想让工位在合适的等待阶段自动休眠，以便减少等待期间的执行资源占用。

关联：[US-07 #12](https://github.com/lilong555/agentcloud-course/issues/12)；FR-02；UC-07。负责人：@lilong555。

实现基础：安全点、调度决策与挂起已有；产品状态展示待接入。

证据：[EV-01](EVIDENCE.md)、[EV-04](EVIDENCE.md)、[EV-05](EVIDENCE.md)。

验收场景 1：

- Given：已配置调度策略并准备短等待、长等待和样本不足轨迹。
- When：模型请求或显式闲置窗口触发决策。
- Then：记录等待、切换成本、容量观测和 KEEP 或 SUSPEND；挂起先完成安全点与持久快照，再释放槽位，样本不足的 v2 采用固定两秒期限并遵守安全约束。

## US-08 唤醒后继续原文件和执行现场

作为上课后回来继续项目的学生，我想唤醒休眠工位后继续原任务，以便保留已有文件、依赖和可恢复状态。

关联：[US-08 #13](https://github.com/lilong555/agentcloud-course/issues/13)；FR-08；UC-08。负责人：@lilong555。

实现基础：MEMORY 恢复与身份校验已有；继续任务入口待接入。

证据：[EV-01](EVIDENCE.md)、[EV-03](EVIDENCE.md)、[EV-06](EVIDENCE.md)。

验收场景 1：

- Given：已保存随机标记文件并在真实 MEMORY 环境记录进程 nonce 和堆标记。
- When：挂起工位后登记返回需求并完成恢复。
- Then：文件内容和摘要相同，进程标记连续，epoch 按协议推进，界面展示实际恢复耗时及 fidelity；VOLUMES 演示按文件恢复标识。

## US-09 资源繁忙时查看容量等待状态

作为在共享环境继续任务的学生，我想知道工位是否正在等待执行资源，以便能区分容量排队与任务失败。

关联：[US-09 #14](https://github.com/lilong555/agentcloud-course/issues/14)；FR-03；UC-09。负责人：@lilong555。

实现基础：恢复容量回执已有；首次准入与恢复等待统一展示待接入。

证据：[EV-02](EVIDENCE.md)、[EV-05](EVIDENCE.md)。

验收场景 1：

- Given：四个热槽位已占用且另一个工位发起恢复。
- When：服务返回 WAITING_CAPACITY 及重试时间。
- Then：显示容量等待和已等待时间，按服务端时间沿用原操作身份继续，权威状态确认前保留原 epoch 和 manifest；首次准入等待单独记录。

## US-10 看懂工作、存档和唤醒进度

作为同时管理多个助手的个人用户，我想用文字状态识别每个任务的进度，以便知道当前应该等待、继续还是处理异常。

关联：[US-10 #15](https://github.com/lilong555/agentcloud-course/issues/15)；FR-05；UC-10。负责人：@lilong555。

实现基础：会话状态、生命周期回执与事件已有；组合展示待实现。

证据：[EV-01](EVIDENCE.md)、[EV-02](EVIDENCE.md)。

验收场景 1：

- Given：存在工作、模型等待、存档、休眠、唤醒、容量等待和待核对轨迹。
- When：状态接口或事件确认这些变化。
- Then：卡片和详情显示一致的文字状态、时间及来源，生命周期、模型等待和容量状态分别保留，事件缺口后重新读取权威状态。

## US-11 刷新后查回原任务结果

作为网络恢复后继续工作的个人用户，我想按原任务身份查看进度和结果，以便刷新页面后继续追踪同一任务。

关联：[US-11 #16](https://github.com/lilong555/agentcloud-course/issues/16)；FR-07；UC-11。负责人：@lilong555。

实现基础：持久模型请求和回执查询已有；页面恢复上下文待实现。

证据：[EV-01](EVIDENCE.md)、[EV-02](EVIDENCE.md)。

验收场景 1：

- Given：一个任务已登记或完成并保存逻辑请求身份。
- When：刷新页面后用原身份查询。
- Then：显示原任务状态、结果或待核对提示，查询本身保持原物理请求计数，已完成结果与刷新前一致。

## US-12 重复提交同一操作时复用原回执

作为遇到响应延迟的个人开发者，我想重复点击时沿用同一操作身份，以便能够确认原操作结果并维持副作用一致性。

关联：[US-12 #17](https://github.com/lilong555/agentcloud-course/issues/17)；FR-07、NFR-01；UC-12。负责人：@lilong555。

实现基础：工具 ID 输入绑定与持久回执已有；客户端身份复用待接入。

证据：[EV-02](EVIDENCE.md)、[EV-03](EVIDENCE.md)。

验收场景 1：

- Given：工具操作已有终态回执。
- When：使用同 tool_op_id 和相同输入重放 20 次。
- Then：返回相同持久结果，受控工具实际执行次数保持一次。

验收场景 2：

- Given：同一个操作 ID 已绑定原输入。
- When：使用该 ID 提交不同输入。
- Then：返回身份或输入冲突并保留原回执与工作区内容。

## US-13 对结果未知的操作执行只读核对

作为处理异常任务的个人开发者，我想查看待核对操作及允许的后续动作，以便根据实际结果决定如何继续。

关联：[US-13 #18](https://github.com/lilong555/agentcloud-course/issues/18)；FR-07、NFR-01；UC-13。负责人：@lilong555。

实现基础：OUTCOME_UNKNOWN、恢复提示与只读检查已有；产品处理页待实现。

证据：[EV-02](EVIDENCE.md)、[EV-03](EVIDENCE.md)。

验收场景 1：

- Given：模拟工具已产生副作用但终态回执丢失。
- When：协调器标记 OUTCOME_UNKNOWN。
- Then：保留原操作身份，显示 RECOVERY_REQUIRED 和允许的只读检查；写入、自动重放与新安全点保持关闭，核对后按人工确认的流程处理。

## US-14 查看工位数量与实际资源用量

作为关注使用开销的个人用户，我想分别看到工位总数、热槽位和资源积分，以便理解多个工位怎样共享执行资源。

关联：[US-14 #19](https://github.com/lilong555/agentcloud-course/issues/19)；FR-05；UC-14。负责人：@lilong555。

实现基础：原始指标与资源分析已有；租户范围的看板聚合待实现。

证据：[EV-01](EVIDENCE.md)、[EV-07](EVIDENCE.md)。

验收场景 1：

- Given：有固定运行身份、测量窗口和后端资源记录。
- When：打开用量看板。
- Then：会话数、休眠数与实际槽位可逐项核对，GB·s、恢复耗时和采样覆盖率附单位与来源，缺测显示待采集；租户页面仅展示授权范围。

## US-15 查看有基线和价格来源的费用估算

作为有月度云端预算的学生，我想按实际用量和单价估算费用，以便根据资源开销选择使用方式。

关联：[US-15 #20](https://github.com/lilong555/agentcloud-course/issues/20)；FR-09；UC-15。负责人：@lilong555。

实现基础：成本指标口径已有；价格参数与分项费用估算待实现。

证据：[EV-01](EVIDENCE.md)、[EV-07](EVIDENCE.md)。

验收场景 1：

- Given：同配置同负载的基线积分为 100 GB·s、当前为 80 GB·s，其他成本项有采集状态。
- When：计算资源节省和费用。
- Then：资源节省显示 20%，计算资源、模型调用、存储和 I/O 按明确单价分项列出，缺测保留待采集，完整总额在成本项齐备后提供。

## US-16 用同一负载对照 TTL 与智能调度

作为讲解项目的课程演示者，我想展示固定 TTL 与 v2 的配对结果，以便解释调度对资源和等待的实际影响。

关联：[US-16 #21](https://github.com/lilong555/agentcloud-course/issues/21)；FR-04；UC-16。负责人：@lilong555。

实现基础：受控 Runner 与配对分析已有；演示入口待接入。

证据：[EV-05](EVIDENCE.md)、[EV-08](EVIDENCE.md)。

验收场景 1：

- Given：固定机器、源码、负载、窗口和至少三个种子对。
- When：在独立演示环境运行或读取 TTL 与 v2 对照。
- Then：显示每个运行身份、计划和完成请求数、资源与 TTFT P95 的配对差及区间，同时保留失败、缺测与清理结果。

## US-17 让多个有状态工位共享有限槽位

作为使用校园共享环境的学生，我想在有限服务器资源上保留更多任务工位，以便让等待中的任务按需让出执行资源。

关联：[US-17 #22](https://github.com/lilong555/agentcloud-course/issues/22)；FR-01；UC-17。负责人：@lilong555。

实现基础：64 Agent / 4 gVisor 槽位历史验证已有；课程复现实验待执行。

证据：[EV-06](EVIDENCE.md)、[EV-08](EVIDENCE.md)。

验收场景 1：

- Given：真实 MEMORY 环境配置四个热槽位、六轮任务和冻结负载。
- When：按课程预算运行 N 个有状态会话并执行至清理结束。
- Then：记录 N/4 复用倍率，实测热槽位峰值至多四个，完成分母和状态校验齐全；N=64 时记为 16×，实际运行配置单独保存。

## US-18 验证恢复与重复操作的一致性

作为依赖任务现场的个人用户，我想恢复后的文件和已确认操作保持一致，以便继续工作时有可核验的结果。

关联：[US-18 #23](https://github.com/lilong555/agentcloud-course/issues/23)；NFR-01；UC-08、UC-12、UC-13。负责人：@lilong555。

实现基础：身份、快照、回执与相关回归已有；课程验收记录待补齐。

证据：[EV-02](EVIDENCE.md)、[EV-03](EVIDENCE.md)、[EV-06](EVIDENCE.md)。

验收场景 1：

- Given：真实 MEMORY 工位和十组唯一文件、进程标记及受控工具计数器。
- When：完成十次挂起恢复并对已完成操作分别重放 20 次。
- Then：十次文件摘要和进程标记全部一致，已完成操作各执行一次；未知结果独立记录并进入核对。

## US-19 同时评价资源消耗与交互等待

作为核验项目效果的课程评审者，我想使用同口径的资源与延迟数据，以便判断策略的收益和代价。

关联：[US-19 #24](https://github.com/lilong555/agentcloud-course/issues/24)；NFR-02；UC-14、UC-16、UC-17。负责人：@lilong555。

实现基础：配对分析和覆盖率门槛已有；课程结果按新运行归档。

证据：[EV-05](EVIDENCE.md)、[EV-07](EVIDENCE.md)、[EV-08](EVIDENCE.md)。

验收场景 1：

- Given：至少三个完整种子对及全部计划请求分母。
- When：生成资源和交互评价报告。
- Then：逐种子报告 GB·s 与 TTFT P95 差及 95% 区间，资源覆盖率达到 90% 才参与联合判定，失败与缺测继续保留在分母和状态中。

## US-20 按冻结配置复现演示与实验

作为复查交付的测试成员，我想获得源码、配置、种子、命令和清理记录，以便按同一协议复现结果。

关联：[US-20 #25](https://github.com/lilong555/agentcloud-course/issues/25)；NFR-03；UC-16、UC-17。负责人：@lilong555。

实现基础：锁定依赖、CI 与实验脚本已有；课程材料与运行对应保存。

证据：[EV-05](EVIDENCE.md)、[EV-09](EVIDENCE.md)。

验收场景 1：

- Given：一份冻结的交付记录。
- When：另一位成员按命令运行基础演示并检查一个实验归档。
- Then：make check 和 make demo 有实际结果，源码、依赖、运行身份、种子、原始数据和清理记录七类字段全部可定位。

## US-21 让个人用户独立完成主要流程

作为首次使用的高校学生，我想理解界面并完成建工位、发任务和继续工作，以便顺利完成自己的任务。

关联：[US-21 #26](https://github.com/lilong555/agentcloud-course/issues/26)；NFR-04；UC-01、UC-03、UC-05、UC-08、UC-10。负责人：@lilong555。

实现基础：试用协议已规划；工作台与真实用户试用待完成。

证据：[EV-01](EVIDENCE.md)、[EV-10](EVIDENCE.md)。

验收场景 1：

- Given：可运行工作台和至少五位目标用户。
- When：参与者按相同任务独立建工位、发任务、恢复并找回文件。
- Then：目标至少四位独立完成，报告实际人数、耗时与求助点；在 390×844 和 1440×900 视口正文至少 14 px，关键操作可见且页面无横向溢出。

## US-22 及时查询工位与更新状态

作为等待任务进度的个人用户，我想及时打开列表和看到已确认的变化，以便掌握工位进展。

关联：[US-22 #27](https://github.com/lilong555/agentcloud-course/issues/27)；NFR-05；UC-02、UC-10、UC-11。负责人：@lilong555。

实现基础：状态查询 API 已有；负载目标及前端刷新待验收。

证据：[EV-02](EVIDENCE.md)、[EV-10](EVIDENCE.md)。

验收场景 1：

- Given：4 vCPU、16 GiB、同机测试且 RTT 至多 50 ms，已有 20 个会话和 20 个查询客户端。
- When：均匀执行 1000 次已授权列表或状态 GET，并观测 20 次已确认状态变化。
- Then：成功查询比例至少 99%，响应 P95 至多 2 秒，20 次变化均在确认后 5 秒内呈现；报告实际硬件、分母和采样，模型生成与恢复耗时单列。

## US-23 保护个人工位与凭据

作为把代码与数据保存在云端的个人用户，我想工位和文件按身份隔离，以便自己的数据只向授权身份提供。

关联：[US-23 #28](https://github.com/lilong555/agentcloud-course/issues/28)；NFR-06；UC-01、UC-02、UC-03、UC-05、UC-06、UC-11、UC-14。负责人：@lilong555。

实现基础：Bearer 租户绑定和路径约束已有；Web 凭据处理待实现并验收。

证据：[EV-02](EVIDENCE.md)、[EV-03](EVIDENCE.md)、[EV-11](EVIDENCE.md)。

验收场景 1：

- Given：两个租户各有独立工位和不同文件标记。
- When：对列表、详情、请求、文件及用量执行 20 次跨租户或无效凭据访问，并执行路径逃逸用例。
- Then：20 次全部被拒绝且响应包含零条他人记录，逃逸访问全部被拒绝；浏览器构建产物和日志中检索测试服务凭据命中数为零。

## US-24 服务重启后找回已确认结果并展示故障

作为经历短暂服务中断的个人用户，我想恢复服务后查回已确认结果并知道待处理异常，以便继续原任务并判断下一步操作。

关联：[US-24 #29](https://github.com/lilong555/agentcloud-course/issues/29)；NFR-07；UC-10、UC-11、UC-13。负责人：@lilong555。

实现基础：持久日志、readiness 和未知结果语义已有；重启时限及产品故障提示待验收。

证据：[EV-02](EVIDENCE.md)、[EV-03](EVIDENCE.md)、[EV-11](EVIDENCE.md)。

验收场景 1：

- Given：持久存储健康、20 条已确认回执及稳定运行的后端依赖。
- When：重启协调器进程并分别注入日志不可写和未知结果故障。
- Then：正常重启目标为 30 秒内 ready，20 条回执内容一致；日志不可写时 readyz 返回 503，页面在 5 秒内提示查询故障，未知结果保留原身份并进入核对。
