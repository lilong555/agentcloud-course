#!/usr/bin/env python3
"""Render and validate the course requirement baseline using the story catalog."""

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "docs/course"
CATALOG = COURSE / "requirements.json"


def load_catalog():
    return json.loads(CATALOG.read_text(encoding="utf-8"))


def issue_body(story, repository):
    base = f"https://github.com/{repository}/blob/docs/lesson03-srs-v1/docs/course"
    lines = [
        f"作为：{story['role']}。",
        f"我想：{story['want']}。",
        f"以便：{story['benefit']}。",
        "",
        f"故事：{story['id']}；需求：{'、'.join(story['requirement_ids'])}；"
        f"用例：{'、'.join(story['use_cases'])}；优先级：{story['priority']}。",
        "",
        f"负责人：@{story['assignee']}。",
        f"现有基础与课程交付：{story['implementation']}。",
        "",
        "## 验收条件",
    ]
    for index, acceptance in enumerate(story["acceptance"], 1):
        lines.extend([
            "",
            f"场景 {index}",
            f"- Given：{acceptance['given']}。",
            f"- When：{acceptance['when']}。",
            f"- Then：{acceptance['then']}。",
        ])
    lines.extend([
        "",
        "## 调研与技术依据",
        "",
        " · ".join(
            f"[{evidence}]({base}/EVIDENCE.md)" for evidence in story["evidence"]
        ),
        "",
        "EV-01 为用户需求假设；访谈、问卷与试用结论随真实采集补充。"
        "本条记录需求与验收，完成状态以实际实现和验证为准。",
        "",
        f"[SRS]({base}/SRS.md) · [用例]({base}/USE_CASES.md) · "
        f"[追溯矩阵]({base}/TRACEABILITY.md) · [变更通道]({base}/CHANGE_CONTROL.md)",
    ])
    return "\n".join(lines) + "\n"


def story_link(story, repository):
    number = story.get("issue_number")
    if number:
        return f"[{story['id']} #{number}](https://github.com/{repository}/issues/{number})"
    return story["id"]


def story_anchor(story):
    return re.sub(r"[^\w\- ]", "", f"{story['id']} {story['title']}".lower()).replace(" ", "-")


def render_documents(data):
    repository = data["repository"]
    stories = data["stories"]
    story_lines = [
        "# 用户故事清单", "",
        f"需求基线 {data['version']}，共 {len(stories)} 条故事。"
        "每条指定实际 GitHub 负责人，关联需求、用例和证据，并给出 Given/When/Then。",
        "",
        "本表由 [requirements.json](requirements.json) 生成；更新后执行 "
        "`python3 scripts/course_requirements.py render`。故事描述课程目标，"
        "实现进度以关联 Issue 和验收记录为准。",
        "",
        "| 故事 / Issue | 类别 | 需求 | 用例 | 优先级 | 负责人 |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for story in stories:
        story_lines.append(
            f"| {story_link(story, repository)} {story['title']} | {story['category']} | "
            f"{'、'.join(story['requirement_ids'])} | {'、'.join(story['use_cases'])} | "
            f"{story['priority']} | @{story['assignee']} |"
        )
    for story in stories:
        story_lines.extend([
            "", f"## {story['id']} {story['title']}", "",
            f"作为{story['role']}，我想{story['want']}，以便{story['benefit']}。", "",
            f"关联：{story_link(story, repository)}；"
            f"{'、'.join(story['requirement_ids'])}；{'、'.join(story['use_cases'])}。"
            f"负责人：@{story['assignee']}。", "",
            f"实现基础：{story['implementation']}。", "",
            "证据：" + "、".join(
                f"[{evidence}](EVIDENCE.md)" for evidence in story["evidence"]
            ) + "。",
        ])
        for index, acceptance in enumerate(story["acceptance"], 1):
            story_lines.extend([
                "", f"验收场景 {index}：", "",
                f"- Given：{acceptance['given']}。",
                f"- When：{acceptance['when']}。",
                f"- Then：{acceptance['then']}。",
            ])
    trace_lines = [
        "# 需求追溯矩阵", "",
        "需求 ID 与用例编号构成初版追溯关系，故事 Issue、证据和验收记录补充完整链条。"
        "功能实现状态在故事 Issue 维护，SRS 验收目标与历史实验分别引用。", "",
        "| 需求 ID | 用例编号 | 用户故事 / Issue | 证据 | 验收定位 |",
        "| --- | --- | --- | --- | --- |",
    ]
    for requirement in data["requirements"]:
        matched = [s for s in stories if requirement["id"] in s["requirement_ids"]]
        use_cases = sorted({u for s in matched for u in s["use_cases"]})
        evidence = sorted({e for s in matched for e in s["evidence"]})
        trace_lines.append(
            f"| {requirement['id']} {requirement['title']} | {'、'.join(use_cases)} | "
            f"{'、'.join(story_link(s, repository) for s in matched)} | "
            f"{'、'.join(evidence)} | [SRS](SRS.md)、"
            f"[故事验收](USER_STORIES.md#{story_anchor(matched[0])}) |"
        )
    trace_lines.extend([
        "", "## 反向追溯", "",
        "| 用例编号 | 对应需求 | 对应故事 |", "| --- | --- | --- |",
    ])
    for use_case in sorted({u for s in stories for u in s["use_cases"]}):
        matched = [s for s in stories if use_case in s["use_cases"]]
        requirements = sorted({r for s in matched for r in s["requirement_ids"]})
        trace_lines.append(
            f"| {use_case} | {'、'.join(requirements)} | "
            f"{'、'.join(s['id'] for s in matched)} |"
        )
    return {
        COURSE / "USER_STORIES.md": "\n".join(story_lines) + "\n",
        COURSE / "TRACEABILITY.md": "\n".join(trace_lines) + "\n",
    }


def validate(data, published=False):
    stories = data["stories"]
    assert len(stories) >= 20, "至少需要 20 条故事"
    assert len({s["id"] for s in stories}) == len(stories), "故事编号重复"
    categories = {s["category"] for s in stories}
    assert {"performance", "security", "availability"} <= categories
    requirements = {r["id"] for r in data["requirements"]}
    assert len(requirements) == len(data["requirements"]), "需求编号重复"
    use_case_doc = (COURSE / "USE_CASES.md").read_text(encoding="utf-8")
    use_cases = set(re.findall(r"^## (UC-\d+) ", use_case_doc, re.M))
    evidence_doc = (COURSE / "EVIDENCE.md").read_text(encoding="utf-8")
    evidence = set(re.findall(r"\| (EV-\d+) \|", evidence_doc))
    referenced_requirements, referenced_use_cases = set(), set()
    for story in stories:
        assert story["assignee"] and story["acceptance"], story["id"]
        assert set(story["requirement_ids"]) <= requirements, story["id"]
        assert set(story["use_cases"]) <= use_cases, story["id"]
        assert story["evidence"] and set(story["evidence"]) <= evidence, story["id"]
        for acceptance in story["acceptance"]:
            assert all(acceptance.get(k) for k in ("given", "when", "then")), story["id"]
        if published:
            assert isinstance(story.get("issue_number"), int), story["id"]
        referenced_requirements.update(story["requirement_ids"])
        referenced_use_cases.update(story["use_cases"])
    assert referenced_requirements == requirements, "存在未覆盖需求"
    assert referenced_use_cases == use_cases, "存在未覆盖用例"
    srs = (COURSE / "SRS.md").read_text(encoding="utf-8")
    assert all(identifier in srs for identifier in requirements)
    diagram = (COURSE / "diagrams/use-cases.puml").read_text(encoding="utf-8")
    assert all(identifier in diagram for identifier in use_cases)
    if published:
        numbers = [s["issue_number"] for s in stories]
        assert len(set(numbers)) == len(numbers), "Issue 关联重复"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("render", "check"))
    parser.add_argument("--published", action="store_true", help="Require actual issue numbers")
    args = parser.parse_args()
    data = load_catalog()
    validate(data, published=args.published)
    for path, expected in render_documents(data).items():
        if args.command == "render":
            path.write_text(expected, encoding="utf-8")
        else:
            assert path.read_text(encoding="utf-8") == expected, f"请重新生成 {path.name}"
    use_cases = {u for story in data['stories'] for u in story['use_cases']}
    print(f"PASS: {len(data['stories'])} stories, {len(data['requirements'])} requirements, {len(use_cases)} use cases")


if __name__ == "__main__":
    main()
