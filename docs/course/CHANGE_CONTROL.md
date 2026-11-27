# 需求变更流程

需求从 Issue 提出，经影响分析和 PR 评审进入 SRS 基线。`requirements.json` 保存故事身份、验收、负责人、来源和 Issue；SRS、用例与追溯矩阵共同描述需求合同。

1. 使用仓库的“需求变更”模板创建 Issue，填写用户场景、当前需求 ID、目标行为、依据与 Given/When/Then。
2. 指定负责人，分析对用例、状态、接口、数据、测试、工期和资源预算的影响；新增需求分配后续稳定编号。
3. 在独立分支同步 SRS、故事目录、用例、追溯矩阵与验收目标。更新原故事时保留其身份及关联 Issue；删除需求保留历史和理由。
4. 提交关联变更 Issue 的 PR，填写需求影响、验证结果及 AI 辅助范围。由另一位成员核对可测试性、完整性与一致性，执行仓库检查。
5. PR 合并后更新需求版本和发布记录，归档可定位的源码、检查与验收材料。

## 验证入口

```bash
python3 scripts/course_requirements.py render
python3 scripts/course_requirements.py check
git diff --check
```

`render` 从故事目录生成[故事清单](USER_STORIES.md)与[追溯矩阵](TRACEABILITY.md)。`check` 检查故事数量、负责人、验收、证据、需求及用例引用和生成材料一致性。代码行为变化按范围运行测试，Course CI 执行既有基础检查和演示。

## 版本与发布

`v1.0` 对应首个 SRS 需求基线。产品实现状态由故事 Issue 和验收记录维护，需求变更与实现进度分别记录。后续补充和语义变化按评审结果发布新的需求版本，Release 指向明确提交，并保留变更 Issue、PR 与验证入口。

发布记录见 [SRS 变更记录](SRS_CHANGELOG.md)，评审依据见[评审记录](REVIEW.md)。
