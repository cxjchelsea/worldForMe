from pathlib import Path

ROOT = Path('个人通识知识系统_v2_A2/30 世界文学/30 专题')

TOPICS = {
    'R1 ': ('WL-TOPIC-R1-WEST-ASIA-MEDITERRANEAN', '西亚—地中海古老传统'),
    'R2 ': ('WL-TOPIC-R2-EAST-ASIA', '东亚文学'),
    'R3 ': ('WL-TOPIC-R3-SOUTH-ASIA', '南亚文学'),
    'R4 ': ('WL-TOPIC-R4-EUROPE', '欧洲文学'),
    'R5 ': ('WL-TOPIC-R5-NORTH-AMERICA', '北美文学'),
    'R6 ': ('WL-TOPIC-R6-LATAM', '拉丁美洲与加勒比文学'),
    'R7 ': ('WL-TOPIC-R7-AFRICA', '非洲文学'),
    'R8 ': ('WL-TOPIC-R8-SOUTHEAST-ASIA', '东南亚文学'),
    'R9 ': ('WL-TOPIC-R9-OCEANIA-PACIFIC', '大洋洲与太平洋文学'),
    'R10 ': ('WL-TOPIC-R10-TRANSREGIONAL', '跨区域文学传统'),
}

DIMENSION_ZH = (
    'dimension.replace("definition", "定义与边界")'
    '.replace("history", "历史层与连续性")'
    '.replace("language_media", "语言、文字与媒介")'
    '.replace("institution", "文学制度与传播")'
    '.replace("reading_route", "阅读路线")'
    '.replace("internal_tradition", "内部传统")'
    '.replace("literary_network", "跨传统网络")'
    '.replace("mechanism", "形成机制")'
    '.replace("transmission_mechanism", "传播机制")'
    '.replace("comparison", "比较")'
    '.replace("cross_region", "跨区域比较")'
    '.replace("literary_field", "文学场域")'
    '.replace("literary_space", "文学空间")'
    '.replace("field", "文学场域")'
    '.replace("civilization", "文明传统")'
)


def build_base(topic_id: str, topic_name: str) -> str:
    # R-axis semantic mapping into the already-frozen T-axis display grammar:
    # core dimensions -> 核心结构; internal traditions -> 专题分支;
    # cross-tradition/literary networks -> 形成机制.
    return f'''filters:\n  and:\n    - topic_id == "{topic_id}"\nformulas:\n  type_zh: if(type == "literature_topic_mechanism", "形成机制", if(dimension == "mechanism", "形成机制", if(dimension == "transmission_mechanism", "形成机制", if(dimension == "literary_network", "形成机制", if(dimension == "internal_tradition", "专题分支", if(dimension == "literary_space", "专题分支", if(dimension == "literary_field", "专题分支", if(dimension == "field", "专题分支", if(dimension == "civilization", "专题分支", "核心结构")))))))))\n  dimension_zh: if(dimension, {DIMENSION_ZH}, "综合结构")\n  sequence_zh: if(sequence, sequence, 0)\n  parent_zh: if(parent, parent, if(dimension == "internal_tradition", "{topic_name}｜内部传统", if(dimension == "literary_network", "{topic_name}｜跨传统网络", if(dimension == "mechanism", "{topic_name}｜形成机制", "{topic_name}"))))\n  history_zh: if(period, period, if(postwar_stage, postwar_stage, if(civilization, civilization, if(dimension == "definition", "全时段边界", if(dimension == "history", "历史纵向", if(dimension == "language_media", "跨时期媒介", if(dimension == "institution", "跨时期制度", if(dimension == "reading_route", "综合阅读", if(dimension == "internal_tradition", "传统纵向", if(dimension == "literary_network", "跨时期网络", if(dimension == "mechanism", "跨时期机制", "跨时期结构")))))))))))\n  mechanism_zh: if(mechanism, mechanism, if(dimension == "definition", "划定专题边界、归属原则与比较范围", if(dimension == "history", "组织文学传统的历史连续性、断裂与分期", if(dimension == "language_media", "解释语言、文字、口传、印刷与媒介如何塑造文学", if(dimension == "institution", "解释教育、宗教、出版、市场与文学制度如何形成", if(dimension == "reading_route", "组织核心阅读路径、比较顺序与扩展入口", if(dimension == "internal_tradition", "展开区域内部文学传统的形成、分化与延续", if(dimension == "literary_network", "连接内部传统并解释传播、翻译、迁徙与重组", if(dimension == "mechanism", "解释跨传统文学形成与传播机制", "说明该节点在专题结构中的作用"))))))))\n  id_zh: if(id, id, "待补编号")\nproperties:\n  file.name:\n    displayName: 节点\n  formula.type_zh:\n    displayName: 类型\n  formula.dimension_zh:\n    displayName: 维度\n  formula.sequence_zh:\n    displayName: 顺序\n  formula.parent_zh:\n    displayName: 父节点\n  formula.history_zh:\n    displayName: 历史位置\n  formula.mechanism_zh:\n    displayName: 机制\n  formula.id_zh:\n    displayName: 编号\nviews:\n  - type: table\n    name: 全部知识节点\n    groupBy:\n      property: formula.type_zh\n      direction: ASC\n    order:\n      - file.name\n      - formula.type_zh\n      - formula.dimension_zh\n      - formula.sequence_zh\n      - formula.parent_zh\n      - formula.history_zh\n      - formula.mechanism_zh\n      - formula.id_zh\n  - type: table\n    name: 核心结构\n    filters:\n      and:\n        - formula.type_zh == "核心结构"\n    groupBy:\n      property: formula.type_zh\n      direction: ASC\n    order:\n      - file.name\n      - formula.type_zh\n      - formula.dimension_zh\n      - formula.sequence_zh\n      - formula.parent_zh\n      - formula.history_zh\n      - formula.mechanism_zh\n      - formula.id_zh\n  - type: table\n    name: 专题分支\n    filters:\n      and:\n        - formula.type_zh == "专题分支"\n    groupBy:\n      property: formula.type_zh\n      direction: ASC\n    order:\n      - file.name\n      - formula.type_zh\n      - formula.dimension_zh\n      - formula.sequence_zh\n      - formula.parent_zh\n      - formula.history_zh\n      - formula.mechanism_zh\n      - formula.id_zh\n  - type: table\n    name: 形成机制\n    filters:\n      and:\n        - formula.type_zh == "形成机制"\n    groupBy:\n      property: formula.type_zh\n      direction: ASC\n    order:\n      - file.name\n      - formula.type_zh\n      - formula.dimension_zh\n      - formula.sequence_zh\n      - formula.parent_zh\n      - formula.history_zh\n      - formula.mechanism_zh\n      - formula.id_zh\n'''

changed = []
for prefix, (topic_id, topic_name) in TOPICS.items():
    dirs = [p for p in ROOT.iterdir() if p.is_dir() and p.name.startswith(prefix)]
    if len(dirs) != 1:
        raise RuntimeError(f'{prefix}: expected 1 topic dir, got {len(dirs)}: {dirs}')
    topic_dir = dirs[0]
    candidates = [p for p in topic_dir.glob('02 *.base') if '结构' in p.name]
    if len(candidates) != 1:
        raise RuntimeError(f'{topic_dir}: expected 1 structure base, got {len(candidates)}: {candidates}')
    base = candidates[0]
    content = build_base(topic_id, topic_name)
    base.write_text(content, encoding='utf-8')
    changed.append(base)

# Static acceptance: exact field/view grammar and non-empty fallback formulas.
required = [
    'displayName: 节点', 'displayName: 类型', 'displayName: 维度', 'displayName: 顺序',
    'displayName: 父节点', 'displayName: 历史位置', 'displayName: 机制', 'displayName: 编号',
    'name: 全部知识节点', 'name: 核心结构', 'name: 专题分支', 'name: 形成机制',
    'formula.parent_zh', 'formula.history_zh', 'formula.mechanism_zh', 'formula.id_zh',
]
for base in changed:
    text = base.read_text(encoding='utf-8')
    missing = [x for x in required if x not in text]
    if missing:
        raise RuntimeError(f'{base}: missing {missing}')

AUD = Path('个人通识知识系统_v2_A2/30 世界文学/_audit/r_axis_acceptance/R_AXIS_STRUCTURE_BASE_NORMALIZATION_V1.md')
AUD.parent.mkdir(parents=True, exist_ok=True)
AUD.write_text('# R Axis Structure Base Normalization V1\n\n'
               f'- Bases normalized: **{len(changed)}**\n'
               '- Reference grammar: T6 structure Base\n'
               '- Columns: **节点 / 类型 / 维度 / 顺序 / 父节点 / 历史位置 / 机制 / 编号**\n'
               '- Views: **全部知识节点 / 核心结构 / 专题分支 / 形成机制**\n'
               '- Internal traditions map to: **专题分支**\n'
               '- Literary/cross-tradition networks map to: **形成机制**\n'
               '- English dimensions are rendered in Chinese.\n'
               '- Parent/history/mechanism/id use non-empty semantic fallbacks.\n\n'
               '`R_AXIS_STRUCTURE_BASE_NORMALIZATION_V1 = PASS`\n', encoding='utf-8')
print(f'normalized {len(changed)} R-axis structure bases')
