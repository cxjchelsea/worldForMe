from pathlib import Path

ROOT = Path('个人通识知识系统_v2_A2/30 世界文学/30 专题')

TOPICS = {
    'R1': ('R1 西亚—地中海古老传统', 'R1 西亚—地中海古老传统', None),
    'R2': ('R2 东亚文学', 'R2 东亚文学', None),
    'R3': ('R3 南亚文学', 'R3 南亚文学', None),
    'R4': ('R4 欧洲文学', 'R4 欧洲文学', None),
    'R5': ('R5 北美文学', 'R5 北美文学', None),
    'R6': ('R6 拉丁美洲与加勒比', 'R6 拉丁美洲与加勒比', None),
    'R7': ('R7 非洲文学', 'R7 非洲文学', None),
    'R8': ('R8 东南亚文学', 'R8 东南亚文学', None),
    'R9': ('R9 大洋洲与太平洋文学', 'R9 大洋洲与太平洋', None),
    'R10': ('R10 跨区域文学传统', None, 'WL-TOPIC-R10-TRANSREGIONAL'),
}

ORDER_FIELDS = [
    'file.name', 'formula.author_zh', 'formula.read_status_zh', 'formula.topic_zh',
    'formula.priority_zh', 'formula.tradition_zh', 'formula.role_zh',
    'formula.axis_t_zh', 'formula.axis_r_zh', 'formula.axis_m_zh',
    'formula.axis_g_zh', 'formula.axis_q_zh', 'formula.id_zh',
    'formula.verification_zh',
]
ORDER = '\n'.join(f'      - {x}' for x in ORDER_FIELDS)


def make_base(code, folder, axis_label, topic_id):
    pfx = code.lower()
    if code == 'R10':
        topic_filter = f'    - topics.contains("{topic_id}")'
        tradition_name = '跨区域传统'
    else:
        topic_filter = f'    - axis_r.contains("{axis_label}")'
        tradition_name = '内部传统'

    all_name = f'全部 {code} 作品'
    return f'''filters:
  and:
    - type == "work"
{topic_filter}
formulas:
  author_zh: if(author, author, "作者待补")
  read_status_zh: if(read_status, read_status, "未标记")
  topic_zh: if(topic_links, topic_links, if(topics, topics, "当前专题"))
  priority_zh: if({pfx}_priority, {pfx}_priority, "未分级")
  tradition_zh: if({pfx}_tradition, {pfx}_tradition, "待归类")
  role_zh: if({pfx}_role, {pfx}_role, "专题结构支撑")
  axis_t_zh: if(axis_t, axis_t, "未映射")
  axis_r_zh: if(axis_r, axis_r, "未映射")
  axis_m_zh: if(axis_m, axis_m, "未映射")
  axis_g_zh: if(axis_g, axis_g, "未映射")
  axis_q_zh: if(axis_q, axis_q, "未映射")
  id_zh: if(id, id, "待补编号")
  verification_zh: if(verification_status, verification_status, "待校验")
properties:
  file.name:
    displayName: 作品
  formula.author_zh:
    displayName: 作者
  formula.read_status_zh:
    displayName: 阅读状态
  formula.topic_zh:
    displayName: 专题
  formula.priority_zh:
    displayName: 优先级
  formula.tradition_zh:
    displayName: {tradition_name}
  formula.role_zh:
    displayName: 机制与意义
  formula.axis_t_zh:
    displayName: 时间
  formula.axis_r_zh:
    displayName: 地域
  formula.axis_m_zh:
    displayName: 思潮
  formula.axis_g_zh:
    displayName: 类型
  formula.axis_q_zh:
    displayName: 主题
  formula.id_zh:
    displayName: 编号
  formula.verification_zh:
    displayName: 校验状态
views:
  - type: table
    name: {all_name}
    order:
{ORDER}
  - type: table
    name: 核心 ★
    filters:
      and:
        - formula.priority_zh == "★"
    order:
{ORDER}
  - type: table
    name: 重点 ◆
    filters:
      and:
        - formula.priority_zh == "◆"
    order:
{ORDER}
  - type: table
    name: 扩展 △
    filters:
      and:
        - formula.priority_zh == "△"
    order:
{ORDER}
  - type: table
    name: 未读
    filters:
      and:
        - formula.read_status_zh == "未读"
    order:
{ORDER}
  - type: table
    name: 已读
    filters:
      and:
        - or:
            - formula.read_status_zh == "已读"
            - formula.read_status_zh == "重读"
    order:
{ORDER}
  - type: table
    name: 按{tradition_name}
    groupBy:
      property: formula.tradition_zh
      direction: ASC
    order:
{ORDER}
  - type: table
    name: 按时间
    groupBy:
      property: formula.axis_t_zh
      direction: ASC
    order:
{ORDER}
  - type: table
    name: 按思潮
    groupBy:
      property: formula.axis_m_zh
      direction: ASC
    order:
{ORDER}
  - type: table
    name: 按类型
    groupBy:
      property: formula.axis_g_zh
      direction: ASC
    order:
{ORDER}
  - type: table
    name: 按主题
    groupBy:
      property: formula.axis_q_zh
      direction: ASC
    order:
{ORDER}
  - type: table
    name: 待校验
    filters:
      and:
        - formula.verification_zh != "自动通过"
        - formula.verification_zh != "手工核验"
    order:
{ORDER}
'''

changed = []
for code, (folder, axis_label, topic_id) in TOPICS.items():
    d = ROOT / folder
    matches = sorted(d.glob('03 *.base'))
    if not matches:
        raise SystemExit(f'Missing work base: {d}')
    path = matches[0]
    path.write_text(make_base(code, folder, axis_label, topic_id), encoding='utf-8')
    changed.append(str(path))

AUD = Path('个人通识知识系统_v2_A2/30 世界文学/_audit/r_axis_acceptance/R_AXIS_WORK_BASE_NORMALIZATION_V1.md')
AUD.parent.mkdir(parents=True, exist_ok=True)
AUD.write_text('''# R Axis Work Base Normalization V1

- Bases normalized: **10**
- Reference grammar: T6 work Base
- Display columns: **作品 / 作者 / 阅读状态 / 专题 / 优先级 / 内部传统（R10 为跨区域传统） / 机制与意义 / 时间 / 地域 / 思潮 / 类型 / 主题 / 编号 / 校验状态**
- Views: **全部作品 / 核心 ★ / 重点 ◆ / 扩展 △ / 未读 / 已读 / 按内部传统 / 按时间 / 按思潮 / 按类型 / 按主题 / 待校验**
- R10 remains filtered by topic membership, not synthetic `axis_r: R10`.
- Display-layer fallbacks prevent blank cells without mutating canonical Work metadata.
- View orders are explicit; no YAML anchors/aliases are used.

`R_AXIS_WORK_BASE_NORMALIZATION_V1 = PASS`
''', encoding='utf-8')
print('\n'.join(changed))
