# 第 03 课交付

AgentCloud 个人 AI 云端工作台。课程主题：学生讲解项目需求（二）、SRS 定稿。对应第 11 周，交付日期为 2026-11-27。

## 检查入口

| 教师检查项 | 交付物 | 核验方式 |
| --- | --- | --- |
| 故事 Issue 至少 20 条，含性能、安全、可用性 | [24 条用户故事](USER_STORIES.md)及 [story 标签](https://github.com/lilong555/agentcloud-course/issues?q=is%3Aissue+label%3Astory) | 每条含用户故事、Given/When/Then、负责人、证据及需求和用例编号 |
| 主次参与者、动宾用例与系统边框 | [用例图与 17 个场景](USE_CASES.md) | 图中含个人用户、演示与测试、推理、沙箱；每个用例有主流程和备选流 |
| 功能、量化质量与约束三块 SRS | [SRS v1.0](SRS.md) | 九项功能、七项非功能需求、运行与许可等约束 |
| 需求与用例追溯 | [初版追溯矩阵](TRACEABILITY.md) | 16 项需求和 17 个用例双向追溯，关联故事 Issue 与证据 |
| 需求变更通过 Issue 和 PR | [变更流程](CHANGE_CONTROL.md)及[变更模板](../../.github/ISSUE_TEMPLATE/requirement_change.yml) | 填写影响分析并同步 SRS、故事、用例、矩阵和验收 |
| SRS v1.0 发布与变更记录 | [Release v1.0](https://github.com/lilong555/agentcloud-course/releases/tag/v1.0)、[SRS 变更记录](SRS_CHANGELOG.md) | 需求基线发布指向明确提交，关联检查和评审记录 |
| 下次课分析建模草稿 | [类图、状态图和顺序图](MODELING.md) | 围绕 UC-08 / UC-13 检查领域关系、容量等待和未知结果 |
| 课堂八分钟讲解 | [讲解稿](LESSON03_BRIEFING.md) | 前三分钟用例、后三分钟场景与质量、最后两分钟提问 |

PDF 附件：[SRS v1.0](deliverables/AgentCloud-SRS-v1.0.pdf)。需求基线的文档核验和评审来源见[评审记录](REVIEW.md)。产品功能与试用进度由故事 Issue 记录。

## 当课角色与认领

目前实际维护账号为 @lilong555，本课故事的需求基线与后续认领由该账号统一负责，GitHub Assignees 已按实际账号设置。成员组队后按[角色分工](TEAM.md)调整具体实现负责人。用户访谈、问卷和试用继续按实际采集登记，技术资料与用户假设在[证据索引](EVIDENCE.md)注明。

## 课后衔接

需求基线作为分析建模输入。后续通过变更 Issue 登记新发现，PR 中同步文字需求与图；实现按故事验收推进。下次课讲解重点为工位、会话、请求、回执和快照的关系，以及继续任务时的容量与异常处理。
