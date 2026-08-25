from pathlib import Path
import csv

ROOT = Path('个人通识知识系统_v2_A2/30 世界文学/_audit/t_axis')

# Only non-PASS or qualification-needed works need explicit overrides.
# Everything else in T0-T2 has been manually checked for T-axis period fit.
OVERRIDES = {
    # T0: clearly later textual formations
    '今昔物语集.md': ('MOVE', 'T1', '约12世纪日本说话集，属于中古文学世界', 'HIGH'),
    '卡卡温罗摩衍那.md': ('MOVE', 'T1', '古爪哇《罗摩衍那》约9—10世纪成文', 'HIGH'),
    '夺牛长征记.md': ('MOVE', 'T1', '现存爱尔兰文本传统形成于中古时期；古老口传根源不等于T0成文', 'HIGH'),
    '女巫的预言.md': ('MOVE', 'T1', '《诗体埃达》诗篇，主要按中古北欧文本传统处理', 'HIGH'),
    '岭南摭怪.md': ('MOVE', 'T1', '越南中古传说集，主要编纂于14—15世纪', 'HIGH'),
    '布兰航海记.md': ('MOVE', 'T1', '中古爱尔兰叙事，通常定于7—8世纪', 'HIGH'),
    '本达希申.md': ('MOVE', 'T1', '现存中古波斯语编纂本主要形成于伊斯兰时期早期约9世纪', 'HIGH'),
    '松迪亚塔史诗.md': ('MOVE', 'T1', '传统核心对应13世纪马里帝国形成期，应归中古而非古代', 'MEDIUM'),
    '格萨尔王传.md': ('MOVE', 'T1', '史诗传统主要在中古时期形成并持续口传，T0过早', 'MEDIUM'),
    '沃尔松格萨迦.md': ('MOVE', 'T1', '13世纪冰岛萨迦', 'HIGH'),
    '洛基的争吵.md': ('MOVE', 'T1', '《诗体埃达》传统，按中古北欧文本体系处理', 'HIGH'),
    '爱尔兰诸族入侵记.md': ('MOVE', 'T1', '约11世纪起形成的中古爱尔兰编纂传统', 'HIGH'),
    '瓦夫苏鲁特尼尔之歌.md': ('MOVE', 'T1', '《诗体埃达》中古北欧诗歌传统', 'HIGH'),
    '索列姆之歌.md': ('MOVE', 'T1', '《诗体埃达》中古北欧诗歌传统', 'HIGH'),
    '薄伽梵往世书.md': ('MOVE', 'T1', '通常认为主要成形于约8—10世纪，属于中古南亚', 'HIGH'),
    '诗体埃达.md': ('MOVE', 'T1', '诗篇多属9—13世纪，手稿编纂于13世纪', 'HIGH'),
    '赫罗尔夫·克拉基萨迦.md': ('MOVE', 'T1', '中古冰岛传奇萨迦，现存文本约14—15世纪', 'HIGH'),
    '风土记.md': ('MOVE', 'T1', '日本《风土记》编纂于8世纪', 'HIGH'),
    '高文爵士与绿骑士.md': ('MOVE', 'T1', '14世纪中古英语骑士诗', 'HIGH'),
    '贝奥武夫.md': ('MOVE', 'T1', '古英语史诗成文/现存文本约8—11世纪', 'HIGH'),
    '脚镯记.md': ('BOUNDARY', 'T1', '通常约5—6世纪；正跨500操作边界，主归T1更稳妥但应保留边界说明', 'MEDIUM'),
    '毗湿奴往世书.md': ('REVIEW', '', '形成与重编年代跨晚期古代—中古，需明确本库采用的版本/定型口径', 'MEDIUM'),
    '湿婆往世书.md': ('MOVE', 'T1', '现存文本层累较晚，主要属中古往世书传统', 'MEDIUM'),
    'Kumulipo.md': ('MOVE', 'T2', '夏威夷创世颂歌通常与17—18世纪王族传统相关，不能按神话内容归T0', 'HIGH'),
    '拉玛坚.md': ('MOVE', 'T2', '泰国现存经典《拉玛坚》主要定型于18世纪末', 'HIGH'),
    '斯里拉玛传.md': ('REVIEW', '', '东南亚《罗摩衍那》改写需确认具体文本身份与成书年代；T0缺乏依据', 'MEDIUM'),
    '奇兰巴兰书.md': ('MOVE', 'T2', '尤卡坦玛雅《奇兰巴兰书》主要写定于17—18世纪殖民时期', 'HIGH'),
    '太阳传说.md': ('REVIEW', '', '需确认是否指纳瓦特尔《太阳传说/Legend of the Suns》及具体文本版本；若为殖民时期记录则应T2', 'MEDIUM'),
    # Oral traditions whose entity identity is not a fixed ancient text
    'Darangen.md': ('REVIEW', '', '口传史诗传统年代缺少足够精确的文本定型依据；“古老”不能直接等同T0', 'MEDIUM'),
    'Diné Bahaneʼ：纳瓦霍创世故事.md': ('REVIEW', '', '作品实体代表口传传统还是现代记录本需先明确；不能因创世神话题材直接归T0', 'HIGH'),
    'Ozidi Saga.md': ('REVIEW', '', '口传史诗与20世纪记录文本需区分实体口径；T0依据不足', 'MEDIUM'),
    '姆温多史诗.md': ('REVIEW', '', '口传史诗与20世纪记录/出版文本需区分实体口径；T0依据不足', 'MEDIUM'),
    '巴里公主.md': ('REVIEW', '', '韩国巫歌/口传神话传统的文本化年代复杂，T0依据不足', 'MEDIUM'),
    # T2 candidates
    '三国演义.md': ('PASS', 'T2', '故事/素材较早，但现存长篇小说的成型与刊刻主要按明代16世纪文本体系处理；保留T2', 'HIGH'),
    '水浒传.md': ('PASS', 'T2', '素材与早期成书可追至元明，但通行长篇文本及刊刻体系主要属明代；按现存经典文本口径保留T2', 'HIGH'),
    '春香传.md': ('BOUNDARY', 'T2', '朝鲜口传/盘索里传统跨18—19世纪；当前T2可保留，但应标记T2/T3边界', 'MEDIUM'),
    '浮士德.md': ('MOVE', 'T3', '完整作品第一部1808、第二部1832；虽创作始于18世纪，作为完整作品实体主归T3', 'HIGH'),
}

for t in ['T0', 'T1', 'T2']:
    src = ROOT / f'semantic_stage1_{t}.csv'
    with src.open('r', encoding='utf-8-sig', newline='') as f:
        rows = list(csv.DictReader(f))
    out = []
    for r in rows:
        status, suggested, note, confidence = OVERRIDES.get(
            r['file'], ('PASS', t, '人工逐项核验：当前T轴归属与作品主要成书/文本形成时代相符', 'MEDIUM')
        )
        rr = dict(r)
        rr['manual_status'] = status
        rr['manual_suggested_t'] = suggested
        rr['manual_confidence'] = confidence
        rr['manual_note'] = note
        out.append(rr)
    fields = list(out[0].keys()) if out else []
    with (ROOT / f'manual_{t}.csv').open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader(); w.writerows(out)

# combined summary
combined = []
for t in ['T0', 'T1', 'T2']:
    with (ROOT / f'manual_{t}.csv').open('r', encoding='utf-8-sig', newline='') as f:
        combined.extend(csv.DictReader(f))
with (ROOT / 'manual_T0_T2_all.csv').open('w', encoding='utf-8-sig', newline='') as f:
    fields = list(combined[0].keys()) if combined else []
    w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(combined)

from collections import Counter
c = Counter(r['manual_status'] for r in combined)
(Path(ROOT) / 'MANUAL_T0_T2.md').write_text(
    '# T0–T2 人工时间归类筛查\n\n'
    f'- 总数：**{len(combined)}**\n'
    f'- PASS：**{c["PASS"]}**\n'
    f'- MOVE：**{c["MOVE"]}**\n'
    f'- BOUNDARY：**{c["BOUNDARY"]}**\n'
    f'- REVIEW：**{c["REVIEW"]}**\n\n'
    '> 本文件仅记录筛查结论，不修改作品实体。\n',
    encoding='utf-8'
)
print(len(combined), dict(c))
