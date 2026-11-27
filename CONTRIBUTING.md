# 课程协作规范

需求、调研、实现和缺陷通过 Issue 追踪。每个任务写清用户场景、交付物、负责人和验收条件，并关联[需求编号](docs/course/PROJECT.md)。

需求基线见 [SRS](docs/course/SRS.md)，故事与用例对应见[追溯矩阵](docs/course/TRACEABILITY.md)。新故事使用“用户故事”模板，需求变更使用“需求变更”模板；影响分析、同步范围和发布约定见[需求变更流程](docs/course/CHANGE_CONTROL.md)。

## 开发与评审

```bash
git switch main
git pull --ff-only
git switch -c feat/scheduler-diagnostics
# 完成对应任务并验证
git add <相关文件>
git commit -m "feat: 增加调度诊断字段"
git push -u origin feat/scheduler-diagnostics
```

分支可使用 `feat/`、`fix/`、`docs/`、`test/` 前缀。PR 关联 Issue，说明交付行为、验收结果和 AI 辅助范围；保持一次 PR 聚焦一个可评审任务。

`main` 通过 PR 接收贡献，要求 Course CI 通过、至少 1 位成员批准以及评审讨论解决。新的提交使旧审批失效；强制推送和分支删除受保护。

## 运行与验证

首次准备环境：

```bash
make bootstrap
python3 scripts/upstream.py --fetch substrate
```

提交代码前执行适合该任务的验证。基础检查入口为 `make check`，端到端演示入口为 `make demo`；PR 的 Course CI 执行这两项并上传验证记录。PostgreSQL 相关用例在 CI 的数据库服务上执行。

纯文档提交核对来源、链接、命令和需求编号。测试结果按实际执行范围记录，涉及真实沙箱、模型或 GPU 的结论附对应环境和原始结果。

## AI 使用与来源

AI 使用记录包括工具名称、辅助任务、采用的内容和核验方法，汇总见 [AI 使用记录](docs/course/AI_USAGE.md)。访谈与问卷保存真实采集记录，引用资料附来源。

复用源码保留许可证和署名。课程功能使用本仓库 Issue、PR 和验收记录追踪，已有实现与实验的来源见 [README](README.md#来源与许可)。
