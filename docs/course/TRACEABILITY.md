# 需求追溯矩阵

需求 ID 与用例编号构成初版追溯关系，故事 Issue、证据和验收记录补充完整链条。功能实现状态在故事 Issue 维护，SRS 验收目标与历史实验分别引用。

| 需求 ID | 用例编号 | 用户故事 / Issue | 证据 | 验收定位 |
| --- | --- | --- | --- | --- |
| FR-01 共享执行槽位 | UC-17 | [US-17 #22](https://github.com/lilong555/agentcloud-course/issues/22) | EV-06、EV-08 | [SRS](SRS.md)、[故事验收](USER_STORIES.md#us-17-让多个有状态工位共享有限槽位) |
| FR-02 按等待与成本智能休眠 | UC-07 | [US-07 #12](https://github.com/lilong555/agentcloud-course/issues/12) | EV-01、EV-04、EV-05 | [SRS](SRS.md)、[故事验收](USER_STORIES.md#us-07-等待期间自动存档并让出执行槽位) |
| FR-03 管理容量与恢复排队 | UC-09 | [US-09 #14](https://github.com/lilong555/agentcloud-course/issues/14) | EV-02、EV-05 | [SRS](SRS.md)、[故事验收](USER_STORIES.md#us-09-资源繁忙时查看容量等待状态) |
| FR-04 对照调度策略 | UC-16 | [US-16 #21](https://github.com/lilong555/agentcloud-course/issues/21) | EV-05、EV-08 | [SRS](SRS.md)、[故事验收](USER_STORIES.md#us-16-用同一负载对照-ttl-与智能调度) |
| FR-05 呈现状态与资源用量 | UC-10、UC-14 | [US-10 #15](https://github.com/lilong555/agentcloud-course/issues/15)、[US-14 #19](https://github.com/lilong555/agentcloud-course/issues/19) | EV-01、EV-02、EV-07 | [SRS](SRS.md)、[故事验收](USER_STORIES.md#us-10-看懂工作存档和唤醒进度) |
| FR-06 创建和管理个人工位 | UC-01、UC-02 | [US-01 #6](https://github.com/lilong555/agentcloud-course/issues/6)、[US-02 #7](https://github.com/lilong555/agentcloud-course/issues/7) | EV-01、EV-02 | [SRS](SRS.md)、[故事验收](USER_STORIES.md#us-01-为不同任务创建独立工位) |
| FR-07 发起任务并查询持久结果 | UC-03、UC-04、UC-11、UC-12、UC-13 | [US-03 #8](https://github.com/lilong555/agentcloud-course/issues/8)、[US-04 #9](https://github.com/lilong555/agentcloud-course/issues/9)、[US-11 #16](https://github.com/lilong555/agentcloud-course/issues/16)、[US-12 #17](https://github.com/lilong555/agentcloud-course/issues/17)、[US-13 #18](https://github.com/lilong555/agentcloud-course/issues/18) | EV-01、EV-02、EV-03 | [SRS](SRS.md)、[故事验收](USER_STORIES.md#us-03-向工位提交任务并查看助手结果) |
| FR-08 操作文件并恢复工作现场 | UC-05、UC-06、UC-08 | [US-05 #10](https://github.com/lilong555/agentcloud-course/issues/10)、[US-06 #11](https://github.com/lilong555/agentcloud-course/issues/11)、[US-08 #13](https://github.com/lilong555/agentcloud-course/issues/13) | EV-01、EV-02、EV-03、EV-06 | [SRS](SRS.md)、[故事验收](USER_STORIES.md#us-05-浏览工作区并读取已有文件) |
| FR-09 估算资源节省与使用费用 | UC-15 | [US-15 #20](https://github.com/lilong555/agentcloud-course/issues/20) | EV-01、EV-07 | [SRS](SRS.md)、[故事验收](USER_STORIES.md#us-15-查看有基线和价格来源的费用估算) |
| NFR-01 状态与副作用一致性 | UC-08、UC-12、UC-13 | [US-12 #17](https://github.com/lilong555/agentcloud-course/issues/17)、[US-13 #18](https://github.com/lilong555/agentcloud-course/issues/18)、[US-18 #23](https://github.com/lilong555/agentcloud-course/issues/23) | EV-02、EV-03、EV-06 | [SRS](SRS.md)、[故事验收](USER_STORIES.md#us-12-重复提交同一操作时复用原回执) |
| NFR-02 资源与交互联合评价 | UC-14、UC-16、UC-17 | [US-19 #24](https://github.com/lilong555/agentcloud-course/issues/24) | EV-05、EV-07、EV-08 | [SRS](SRS.md)、[故事验收](USER_STORIES.md#us-19-同时评价资源消耗与交互等待) |
| NFR-03 交付与实验可复现 | UC-16、UC-17 | [US-20 #25](https://github.com/lilong555/agentcloud-course/issues/25) | EV-05、EV-09 | [SRS](SRS.md)、[故事验收](USER_STORIES.md#us-20-按冻结配置复现演示与实验) |
| NFR-04 主要流程易用性 | UC-01、UC-03、UC-05、UC-08、UC-10 | [US-21 #26](https://github.com/lilong555/agentcloud-course/issues/26) | EV-01、EV-10 | [SRS](SRS.md)、[故事验收](USER_STORIES.md#us-21-让个人用户独立完成主要流程) |
| NFR-05 查询性能与状态新鲜度 | UC-02、UC-10、UC-11 | [US-22 #27](https://github.com/lilong555/agentcloud-course/issues/27) | EV-02、EV-10 | [SRS](SRS.md)、[故事验收](USER_STORIES.md#us-22-及时查询工位与更新状态) |
| NFR-06 身份认证与租户隔离 | UC-01、UC-02、UC-03、UC-05、UC-06、UC-11、UC-14 | [US-23 #28](https://github.com/lilong555/agentcloud-course/issues/28) | EV-02、EV-03、EV-11 | [SRS](SRS.md)、[故事验收](USER_STORIES.md#us-23-保护个人工位与凭据) |
| NFR-07 重启恢复与故障可见性 | UC-10、UC-11、UC-13 | [US-24 #29](https://github.com/lilong555/agentcloud-course/issues/29) | EV-02、EV-03、EV-11 | [SRS](SRS.md)、[故事验收](USER_STORIES.md#us-24-服务重启后找回已确认结果并展示故障) |

## 反向追溯

| 用例编号 | 对应需求 | 对应故事 |
| --- | --- | --- |
| UC-01 | FR-06、NFR-04、NFR-06 | US-01、US-21、US-23 |
| UC-02 | FR-06、NFR-05、NFR-06 | US-02、US-22、US-23 |
| UC-03 | FR-07、NFR-04、NFR-06 | US-03、US-21、US-23 |
| UC-04 | FR-07 | US-04 |
| UC-05 | FR-08、NFR-04、NFR-06 | US-05、US-21、US-23 |
| UC-06 | FR-08、NFR-06 | US-06、US-23 |
| UC-07 | FR-02 | US-07 |
| UC-08 | FR-08、NFR-01、NFR-04 | US-08、US-18、US-21 |
| UC-09 | FR-03 | US-09 |
| UC-10 | FR-05、NFR-04、NFR-05、NFR-07 | US-10、US-21、US-22、US-24 |
| UC-11 | FR-07、NFR-05、NFR-06、NFR-07 | US-11、US-22、US-23、US-24 |
| UC-12 | FR-07、NFR-01 | US-12、US-18 |
| UC-13 | FR-07、NFR-01、NFR-07 | US-13、US-18、US-24 |
| UC-14 | FR-05、NFR-02、NFR-06 | US-14、US-19、US-23 |
| UC-15 | FR-09 | US-15 |
| UC-16 | FR-04、NFR-02、NFR-03 | US-16、US-19、US-20 |
| UC-17 | FR-01、NFR-02、NFR-03 | US-17、US-19、US-20 |
