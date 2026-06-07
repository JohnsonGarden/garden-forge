#!/usr/bin/env python3
"""Initialize a reusable AI novel-writing harness."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def slug_default(title: str) -> str:
    cleaned = re.sub(r"[\\/:*?\"<>|]+", "", title).strip()
    return cleaned or "小说工程"


def render(text: str, data: dict[str, str]) -> str:
    for key, value in data.items():
        text = text.replace("{{" + key + "}}", value)
        text = text.replace("{" + key + "}", value)
    return text.strip() + "\n"


def write(path: Path, text: str, data: dict[str, str], force: bool) -> None:
    if path.exists() and not force:
        raise FileExistsError(f"{path} already exists; pass --force to overwrite")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render(text, data), encoding="utf-8")


def templates() -> dict[str, str]:
    return {
        "docguide.md": """
# {{PROJECT_TITLE}} 工程目录指引

本文档是给大模型快速理解工程目录的入口地图。它只说明"文件在哪里、负责什么"，不承载具体创作规则；正式协作规则以 `AGENTS.md` 为准。

## 根目录

- `docguide.md`：工程目录指引，也就是当前文件。
- `AGENTS.md`：所有AI协作主体的主要工作规则入口。
- `CLAUDE.md`：Claude类助手兼容入口，指向 `AGENTS.md`。

## 核心目录

| 目录 | 用途 |
|---|---|
| `SPEC/Me2AI/` | 作者稳定意图、大纲、风格、设定、核心角色 |
| `SPEC/AI2AI/` | AI维护的流程、状态、会议索引、审查、任务和工具 |
| `SPEC/AI2AI/会议纪要/` | 按章节归档章前启动会与章后复盘会 |
| `SPEC/AI2AI/创作工具/` | 耐看特质、去AI味、术语边界、风险控制等工具 |
| `agents/` | 常驻智能体角色卡 |
| `novel/` | 正文 |
| `briefs/` | 每章RunBrief |
| `scene_cards/` | 每章场景卡 |
| `reviews/` | 审查报告、评分表、主编裁决 |
| `handoffs/` | 重要智能体交接记录 |
| `publish_feedback/` | 平台数据、读者反馈、弃读点原始材料 |
| `style_examples/` | 正向样本、反例样本、角色口吻样本 |

## 阅读顺序

1. 先读 `AGENTS.md`。
2. 再读 `SPEC/Me2AI/` 下全部稳定SPEC。
3. 根据任务读取 `SPEC/AI2AI/` 的流程、状态和创作工具。
4. 正式章节写作或审查时读取 `agents/` 下全部常驻角色卡。

## 禁止

- 不要把会议纪要堆进本文件。
""",
        "AGENTS.md": """
# {{PROJECT_TITLE}} 小说工程协作入口

本工程是小说创作工程，不是代码工程。所有正式写作、重写、优化、审查，必须遵守双层SPEC与多智能体协作机制。

## 核心目标

- 作品形态：{{FORM}}
- 目标篇幅：{{TARGET_LENGTH}}
- 硬上限：{{HARD_CAP}}
- 发布平台/阅读场景：{{PLATFORM}}
- 核心立意：{{CORE_INTENT}}
- 读者承诺：{{READER_PROMISE}}

## 目录

- `SPEC/Me2AI/`：作者稳定意图。
- `SPEC/AI2AI/`：AI维护的动态状态、流程、审查、会议索引、任务和工具。
- `SPEC/AI2AI/会议纪要/`：按章节归档章前启动会与章后复盘会。
- `agents/`：常驻智能体角色卡。
- `novel/`：正文。
- `briefs/`：章节RunBrief。
- `scene_cards/`：章节场景卡。
- `reviews/`：审查报告与评分。
- `handoffs/`：智能体交接。
- `publish_feedback/`：平台反馈入口。
- `style_examples/`：正反风格样本。

根目录 `docguide.md` 是给大模型查看工程目录的指引，必须保留在根目录。跨agent操作规则统一使用根目录 `AGENTS.md`；`CLAUDE.md` 只做兼容指引。

## 正式章节门禁

上下文加载 -> 章前启动会 -> RunBrief -> 场景卡 -> 初稿 -> 创作工具检查 -> 多智能体审查 -> 章节评分 -> 主编裁决 -> 二稿 -> 终审 -> 章后复盘 -> task清零 -> 状态更新。

没有章前启动会，不得生成最终RunBrief。没有RunBrief和场景卡，不得写正文。没有章后复盘与必要task清零，不得进入下一章。

## 常驻智能体

主编、架构师、执行主笔作家、人设与对白专员、去AI写作风格审查专员、模拟读者、平台留存与数据分析师、连续性与档案官。

## 写作规则占位

- 对话标点规则：请在此填写。
- 禁用或慎用句式：请在此填写。
- 视角规则：请在此填写。
- 平台章节长度：请在此填写。
""",
        "CLAUDE.md": """
# Claude入口说明

本工程统一协作约束以 `AGENTS.md` 为准。进入工程后，先读取 `AGENTS.md`，再按其中要求读取 Me2AI、AI2AI、创作工具和角色卡。

不得绕过上下文加载摘要、章前启动会、RunBrief、场景卡、创作工具检查、章节评分表、章后复盘会和task闭环直接写正文。
""",
        "SPEC/Me2AI/人类作者创作初衷.md": """
# 人类作者创作初衷

## 核心立意

{{CORE_INTENT}}

## 初始创意母本

{{INITIAL_IDEA}}

## 读者承诺

{{READER_PROMISE}}

## 发布平台/阅读场景

{{PLATFORM}}

## 不可改变

{{TABOO_CHANGES}}

## 可调整

- 请填写可压缩、可替换、可重排的内容。
""",
        "SPEC/Me2AI/outline.md": """
# 全书大纲

## 形态与篇幅

- 作品形态：{{FORM}}
- 目标篇幅：{{TARGET_LENGTH}}
- 硬上限：{{HARD_CAP}}
- 发布平台/阅读场景：{{PLATFORM}}

## 初始创意转化原则

- 创意母本：{{INITIAL_IDEA}}
- 改写时优先保留：{{TABOO_CHANGES}}
- 大纲可以压缩支线、合并人物、重排事件，但不得削弱核心立意：{{CORE_INTENT}}

## 四幕结构占位

| 幕 | 功能 | 预计章节/字数 | 核心任务 |
|---|---|---|---|
| 第一幕 | 建立主角、冲突、读者承诺 | 待定 | 待填 |
| 第二幕 | 扩大局势与爽点模式 | 待定 | 待填 |
| 第三幕 | 中段升级与关键兑现 | 待定 | 待填 |
| 第四幕 | 终局收束与主题兑现 | 待定 | 待填 |
""",
        "SPEC/Me2AI/写作风格.md": """
# 写作风格

## 基调

- 请填写：轻松/热血/悬疑/克制/群像/爽文等。

## 章节要求

- 开头必须有抓手。
- 每章必须有冲突、情绪点、记忆点、章末钩子。
- 设定必须通过冲突、行动、对白呈现。

## 禁止

- 禁止无功能设定说明。
- 禁止角色声音趋同。
- 禁止为金句牺牲人物真实。
""",
        "SPEC/Me2AI/故事整体设定.md": """
# 故事整体设定

## 世界规则

- 待填。

## 核心矛盾

- 待填。

## 信息揭露原则

- 按需揭露。
- 优先服务章节冲突和读者理解。
- 禁止把世界观当展示柜。
""",
        "SPEC/Me2AI/核心角色.md": """
# 核心角色

## 主角/主角团

| 角色 | 核心欲望 | 底线 | 弧线 | 声音特征 |
|---|---|---|---|---|
| 待填 | 待填 | 待填 | 待填 | 待填 |

## 关系优先级

- 请填写本书最重要的关系资产。
""",
        "SPEC/AI2AI/多智能体协作机制.md": """
# 多智能体协作机制

## 最高原则

1. 作者明确指令优先。
2. 立意与篇幅目标优先。
3. 读者体验前置。
4. 主编裁决，多agent不堆意见。
5. 写作与审查分离。
6. 每章必须会议闭环和task闭环。

## 标准章节流程

上下文加载 -> 章前全员启动会 -> RunBrief -> 场景卡 -> 初稿 -> 创作工具检查 -> 多agent审查 -> 章节评分 -> 主编裁决 -> 二稿 -> 主编终审 -> 章后复盘 -> task清零 -> 更新AI2AI状态。

## 常驻智能体

见 `agents/` 目录。正式章节写作必须读取全部常驻角色卡。
""",
        "SPEC/AI2AI/上下文加载规则.md": """
# 上下文加载规则

## 正式章节新写必须读取

- `AGENTS.md`
- `SPEC/Me2AI/` 全部文件
- `SPEC/AI2AI/` 核心机制文件与动态状态文件
- `SPEC/AI2AI/创作工具/` 相关工具
- `agents/` 全部常驻角色卡
- 上一章正文，如有

## 输出模板

```markdown
## 本轮上下文加载摘要
- 任务类型：
- 已读取Me2AI：
- 已读取AI2AI：
- 已读取创作工具：
- 已读取角色卡：
- 缺失文件：
- 是否允许进入下一步：
```
""",
        "SPEC/AI2AI/RunBrief模板.md": """
# RunBrief模板

```markdown
# 第X章 RunBrief

## 章前启动会输入
- 启动会纪要路径：
- 会前阻塞项是否清零：

## 本章定位
- 所属幕：
- 本章功能：
- 读者期待：

## 必须完成
1.

## 禁止事项
1.

## 核心冲突
- 表层冲突：
- 深层冲突：
- 如何升级：
- 如何阶段性解决：

## 角色分工
-

## 爽点/笑点/情绪点
-

## 伏笔
- 需回收：
- 可新增：
- 预计回收：

## 章末钩子
-

## 创作工具重点
- 耐看特质：
- 去AI味：
- 术语边界：
- 风险红线：

## 场景卡要求
- 场景数量建议：
- 必须包含：
- 禁止出现：

## 主编批准意见
- 是否批准：
```
""",
        "SPEC/AI2AI/场景卡工作流.md": """
# 场景卡工作流

RunBrief批准后、正文初稿前，必须建立场景卡。单章建议3-6张场景卡。

每张场景卡必须回答：功能、冲突、主推角色、信息投放、爽点/情绪点、角色推进、伏笔、结尾推进、可删内容、禁止写法。
""",
        "SPEC/AI2AI/章节审查工作流.md": """
# 章节审查工作流

初稿完成后，依次或并行执行：创作工具检查、架构师审查、人设与对白审查、去AI审查、模拟读者反馈、平台留存分析、章节评分、主编裁决。

主编必须形成唯一修改清单，执行主笔只按主编裁决改二稿。
""",
        "SPEC/AI2AI/章节评分表.md": """
# 章节评分表

| 维度 | 权重 | 通过标准 |
|---|---:|---|
| 开头抓力 | 15% | 前300字有抓手 |
| 第一爽点 | 15% | 爽点不拖延 |
| 核心关系/角色魅力 | 15% | 读者更喜欢角色 |
| 结构功能 | 15% | 服务全书目标 |
| 章末点击 | 15% | 想读下一章 |
| 去AI味 | 10% | 无明显模板腔 |
| 角色稳定 | 10% | 行为符合人设 |
| 篇幅控制 | 5% | 不膨胀 |

硬门槛：章末点击低于项目阈值、无爽点、无结构功能、触发风险红线时不得定稿。
""",
        "SPEC/AI2AI/会议机制与任务闭环.md": """
# 会议机制与任务闭环

每章必须有章前启动会和章后复盘会。

章前会输出：本章目标、禁止事项、角色高光、留存策略、伏笔承接、场景卡重点、创作工具重点、是否允许生成RunBrief。纪要单独归档到 `SPEC/AI2AI/会议纪要/`。

章后会输出：是否达成RunBrief、评分结果、工具检查结果、遇到的问题、解决方式、协作经验、新增task、是否允许进入下一章。纪要单独归档到 `SPEC/AI2AI/会议纪要/`，task同步写入 `SPEC/AI2AI/会议纪要与任务看板.md`。
""",
        "SPEC/AI2AI/会议纪要与任务看板.md": """
# 会议纪要与任务看板

本文件只保留章节门禁、task状态和会议索引。完整会议纪要不得写入本文件，统一归档到 `SPEC/AI2AI/会议纪要/`。

## 当前章节门禁

| 项目 | 状态 | 说明 |
|---|---|---|
| 当前章节 | 未开始 |  |
| 章前启动会 | 未召开 |  |
| RunBrief | 未生成 |  |
| 场景卡 | 未生成 |  |
| 初稿 | 未开始 |  |
| 创作工具检查 | 未生成 |  |
| 章节评分 | 未生成 |  |
| 章后复盘 | 未召开 |  |
| 是否允许进入下一章 | 否 |  |

## 当前未完成task

| task编号 | 关联章节 | task | 负责人agent | 优先级 | 完成标准 | 状态 |
|---|---|---|---|---|---|---|
| INIT-001 | 工程初始化 | 完成第1章章前启动会 | 主编 | P0 | 形成纪要并允许生成RunBrief | 待办 |

## 会议纪要索引

会议纪要不写入本文件正文，统一存放在 `SPEC/AI2AI/会议纪要/`，本区只保留索引。

| 章节 | 章前启动会 | 章后复盘会 |
|---|---|---|
| 第1章 | `会议纪要/第001章-章前启动会.md` | `会议纪要/第001章-章后复盘会.md` |
""",
        "SPEC/AI2AI/会议纪要/README.md": """
# 会议纪要目录

本目录按章节归档会议纪要，避免把所有会议内容堆进一个AI2AI文件。

命名建议：

- `第001章-章前启动会.md`
- `第001章-章后复盘会.md`

`SPEC/AI2AI/会议纪要与任务看板.md` 只记录会议索引、章节门禁和task状态，不承载完整会议内容。
""",
        "SPEC/AI2AI/会议纪要/第X章章前启动会模板.md": """
# 第X章 章前启动会

## 会议结论

-

## 各agent关键意见

| agent | 关键意见 |
|---|---|

## RunBrief输入

- 本章定位：
- 必须完成：
- 禁止事项：
- 角色高光：
- 留存策略：
- 伏笔承接：
- 场景卡重点：
- 创作工具重点：
- 章末钩子方向：

## 会前阻塞项

| 阻塞项 | 负责人 | 解决标准 |
|---|---|---|

## 是否允许生成RunBrief

- 判断：
- 理由：
""",
        "SPEC/AI2AI/会议纪要/第X章章后复盘会模板.md": """
# 第X章 章后复盘会

## 本章最终判断

- 是否达到RunBrief：
- 是否完成场景卡目标：
- 创作工具检查结果：
- 章节评分表结果：
- 是否达到留存目标：
- 是否服务全书篇幅目标：

## 本章遇到的问题

| 问题 | 发现者 | 解决方式 | 是否沉淀为规则 |
|---|---|---|---|

## 各agent复盘

| agent | 复盘结论 |
|---|---|

## 新增task

| task编号 | task | 负责人agent | 优先级 | 完成标准 | 状态 |
|---|---|---|---|---|---|

## 需更新文件

-

## 是否允许进入下一章

- 判断：
- 前置条件：
""",
        "SPEC/AI2AI/主编决策日志.md": """
# 主编决策日志

| 编号 | 日期 | 决策 | 适用范围 | 理由 | 状态 |
|---|---|---|---|---|---|
| DEC-001 | 初始化 | 建立双层SPEC与多智能体harness | 全书 | 保持协作一致性 | 生效 |
""",
        "SPEC/AI2AI/临时专家智能体机制.md": """
# 临时专家智能体机制

常驻八个智能体之外，可按风险召集临时专家，如情感关系、战斗场面、商业爽点、标题章名、世界观压缩、首三章急救、线索公平性等。

临时专家只给专项意见，必须经主编裁决后才能进入修改清单。
""",
        "SPEC/AI2AI/章节目录以及写作状态.md": """
# 章节目录以及写作状态

| 章号 | 章名 | 所属阶段 | 预计字数 | 实际字数 | 状态 | RunBrief | 场景卡 | 审查 | 复盘 | task清零 |
|---|---|---|---:|---:|---|---|---|---|---|---|
| 第1章 | 待定 | 第一阶段 | 待定 | 0 | 未开始 | 未生成 | 未生成 | 未审 | 未召开 | 否 |
""",
        "SPEC/AI2AI/中长线伏笔设计和进展.md": """
# 中长线伏笔设计和进展

| 编号 | 伏笔 | 类型 | 首次投放 | 当前状态 | 预计回收 | 风险 |
|---|---|---|---|---|---|---|
| F-001 | 待定 | 待定 | 待定 | 计划中 | 待定 | 待定 |
""",
        "SPEC/AI2AI/各角色线设计和进展.md": """
# 各角色线设计和进展

| 角色 | 核心功能 | 起点 | 阶段目标 | 终局方向 | 当前风险 |
|---|---|---|---|---|---|
| 待填 | 待填 | 待填 | 待填 | 待填 | 待填 |
""",
        "SPEC/AI2AI/发布反馈记录.md": """
# 发布反馈记录

| 日期 | 平台 | 范围 | 核心问题 | 证据 | 主编判断 | 关联task |
|---|---|---|---|---|---|---|
""",
        "SPEC/AI2AI/风险验收记录与风险处置记录.md": """
# 风险验收记录与风险处置记录

| 编号 | 风险 | 类型 | 关联范围 | 优先级 | 处置状态 | 验收标准 |
|---|---|---|---|---|---|---|
| R-001 | 新工程未完成首章启动会 | 流程 | 第1章 | P0 | 待处理 | 章前启动会纪要完成 |
""",
        "SPEC/AI2AI/创作工具/README.md": """
# 创作工具目录说明

本目录存放章节质量控制工具。正式章节写作和审查时按需调用：耐看特质、去AI味、术语边界、风险控制、旧经验沉淀。
""",
        "SPEC/AI2AI/创作工具/耐看小说特质.md": """
# 耐看小说特质

四步验收：语言与节奏、情节与悬念、人物与弧光、主题与回旋。

每章检查：开头抓力、爽点兑现、喜剧/情绪、冲突强度、信息缺口、章末钩子、人物记忆点、关系变化、主题落地。
""",
        "SPEC/AI2AI/创作工具/去AI味儿.md": """
# 去AI味儿

重点查：忽然、然后、瞬间、竟然、居然、显然、真的、突然、顿了顿、沉默了一瞬、愣了一下、深吸一口气。

严格审查重复金句和"不是XXX，是XXX"句式。能用动作表达的，不用旁白解释。
""",
        "SPEC/AI2AI/创作工具/英文与现代术语使用规范.md": """
# 英文与现代术语使用规范

除非必要，不要使用英文。除非角色身份允许，不要使用现代术语。原住民不主动说现代词；需要出现时必须有翻译层。
""",
        "SPEC/AI2AI/创作工具/风险控制表.md": """
# 风险控制表

红线：开篇模板化、为搞笑降智、无因果硬转折、设定冲突、过度说教、长篇水章、金手指强行解题、核心关系被挤压、新增无法回收支线。
""",
        "SPEC/AI2AI/创作工具/旧工程审查经验沉淀.md": """
# 旧工程审查经验沉淀

可沉淀经验写在这里。默认提醒：对话直入优于环境铺陈；设定通过冲突呈现；悬念不要当场说透；情感优先落在动作上；系统提示后必须把戏还给人物。
""",
        "SPEC/AI2AI/模板/智能体交接模板.md": """
# 智能体交接模板

```markdown
# 第X章 智能体交接
- 发起agent：
- 接收agent：
- 背景：
- 需要处理：
- 输入材料：
- 完成标准：
- 禁止事项：
- 主编备注：
```
""",
    }


AGENT_TEMPLATE = """# {name}

## 身份

你是《{{PROJECT_TITLE}}》小说工程的{name}。

## 职责

{duties}

## 禁止

- 禁止绕过主编裁决。
- 禁止空泛评价，必须给可执行意见。
- 禁止削弱核心立意：{{CORE_INTENT}}

## 输出

```markdown
## {name}报告

### 判断

-

### P0必须处理

1.

### 给主编的建议

-
```
"""


def agent_templates() -> dict[str, str]:
    duties = {
        "主编": "方向、取舍、会议、RunBrief批准、场景卡批准、最终裁决、定稿门禁。",
        "架构师": "结构、篇幅、因果链、伏笔、主线收束，防止工程膨胀。",
        "执行主笔作家": "按主编批准的RunBrief和场景卡写初稿与二稿，不自行宣布定稿。",
        "人设与对白专员": "角色稳定、声音辨识度、核心关系、对白是否推进冲突。",
        "去AI写作风格审查专员": "去AI味、套路句、解释性废话、术语边界、重复句式。",
        "模拟读者": "开头吸引力、弃读点、爽点、角色喜爱度、章末点击意愿。",
        "平台留存与数据分析师": "标题、开头、章末、平台反馈、传播点与留存风险。",
        "连续性与档案官": "AI2AI状态、伏笔、角色线、风险、会议纪要目录、任务看板、task闭环。",
    }
    return {f"agents/{name}.md": AGENT_TEMPLATE.format(name=name, duties=duty) for name, duty in duties.items()}


def readmes() -> dict[str, str]:
    return {
        "agents/README.md": "# agents\n\n本目录存放常驻智能体角色卡。正式章节写作、整章重写、定稿审查时必须读取全部常驻角色卡。\n",
        "novel/README.md": "# novel\n\n本目录存放正文。每章一个Markdown文件。\n",
        "briefs/README.md": "# briefs\n\n本目录存放每章RunBrief。\n",
        "scene_cards/README.md": "# scene_cards\n\n本目录存放章节场景卡。\n",
        "reviews/README.md": "# reviews\n\n本目录存放审查报告、评分表和主编裁决。\n",
        "handoffs/README.md": "# handoffs\n\n本目录存放重要智能体交接记录。\n",
        "publish_feedback/README.md": "# publish_feedback\n\n本目录存放平台数据、评论、弃读点等原始反馈。\n",
        "style_examples/README.md": "# style_examples\n\n本目录存放正向样本、反例样本和角色口吻样本。\n",
        "style_examples/样本文本索引.md": "# 样本文本索引\n\n| 编号 | 类型 | 来源 | 可学习点 | 禁止照搬点 |\n|---|---|---|---|---|\n",
        "scene_cards/第X章场景卡模板.md": "# 第X章场景卡\n\n| 场景 | 功能 | 主推角色 | 冲突 | 爽点/情绪点 | 结尾推进 |\n|---|---|---|---|---|---|\n",
        "publish_feedback/发布反馈录入模板.md": "# 发布反馈录入模板\n\n- 日期：\n- 平台：\n- 范围：\n- 数据：\n- 评论摘录：\n- 弃读点判断：\n",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialize an AI novel-writing harness.")
    parser.add_argument("--root", required=True, help="Parent directory where the harness folder will be created")
    parser.add_argument("--name", help="Harness directory name")
    parser.add_argument("--title", required=True, help="Novel/project title")
    parser.add_argument("--form", default="小说", help="Project form, e.g. 短篇/长篇/系列")
    parser.add_argument("--target-length", default="待定", help="Target length")
    parser.add_argument("--hard-cap", default="待定", help="Hard cap")
    parser.add_argument("--initial-idea", default="待填写", help="Initial fiction idea or rewrite seed")
    parser.add_argument("--core-intent", default="待填写", help="Core theme/intent")
    parser.add_argument("--reader-promise", default="待填写", help="Primary reader promise")
    parser.add_argument("--platform", default="待定", help="Publication platform or reading context")
    parser.add_argument("--taboo-changes", default="待填写", help="Things that must not be changed")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    parser.add_argument("--dry-run", action="store_true", help="Print target path without writing")
    args = parser.parse_args()

    name = args.name or slug_default(args.title)
    target = Path(args.root).expanduser().resolve() / name
    data = {
        "PROJECT_TITLE": args.title,
        "FORM": args.form,
        "TARGET_LENGTH": args.target_length,
        "HARD_CAP": args.hard_cap,
        "INITIAL_IDEA": args.initial_idea,
        "CORE_INTENT": args.core_intent,
        "READER_PROMISE": args.reader_promise,
        "PLATFORM": args.platform,
        "TABOO_CHANGES": args.taboo_changes,
    }

    all_templates = {}
    all_templates.update(templates())
    all_templates.update(agent_templates())
    all_templates.update(readmes())

    if args.dry_run:
        print(target)
        for rel in sorted(all_templates):
            print(target / rel)
        return 0

    if target.exists() and any(target.iterdir()) and not args.force:
        raise SystemExit(f"Target exists and is not empty: {target}. Use --force to overwrite files.")

    for rel, content in all_templates.items():
        write(target / rel, content, data, args.force)

    print(f"Initialized novel harness at: {target}")
    print("Next: open AGENTS.md, fill SPEC/Me2AI, then run the chapter-1 kickoff meeting.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
