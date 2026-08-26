from pathlib import Path
import re

ROOT = Path('个人通识知识系统_v2_A2/30 世界文学')
WORKS = ROOT / '40 作品'
AUD = ROOT / '_audit' / 'r_axis_acceptance' / 'R8_R9_BIBLIOGRAPHIC_CLEANUP_V1.md'

AUTHOR_MAP = {
    '夕雾花园': '陈团英（Tan Twan Eng）',
    '彩虹战士': 'Andrea Hirata',
    '美丽是一种伤': 'Eka Kurniawan',
    '天使在我桌上': 'Janet Frame',
    '如果我们梦想太久': 'Goh Poh Seng',
    '曼谷苏醒': 'Pitchaya Sudbanthad',
    '雨之赐': '陈团英（Tan Twan Eng）',
    '西蒂·努尔巴雅': 'Marah Rusli',
    '沙丽娜': 'A. Samad Said',
    '传奇漫录': '阮屿（Nguyễn Dữ）',
    '胡春香诗选': '胡春香（Hồ Xuân Hương）',
    '博尔哈·达科斯塔诗选': 'Borja da Costa',
    '尤今小说选': '尤今',
    '王润华诗选': '王润华',
    '费尔南多·西尔万诗选': 'Fernando Sylvan',
    '哈姆扎·凡苏里诗选': 'Hamzah Fansuri',
    '卡彭塔利亚湾': 'Alexis Wright',
    '我的地方': 'Sally Morgan',
    '曾经是勇士': 'Alan Duff',
    '花园聚会': 'Katherine Mansfield',
    '荆棘鸟': 'Colleen McCullough',
    '鲸骑士': 'Witi Ihimaera',
    '詹姆斯·K·巴克斯特诗选': 'James K. Baxter',
    '霍内·图法雷诗选': 'Hone Tuwhare',
    'Déwé Gorodé诗选': 'Déwé Gorodé',
    '乌哲鲁诗选': 'Oodgeroo Noonuccal',
    '兔子证明栅栏': 'Doris Pilkington Garimara',
    '幽灵鸟': 'Lisa Fuller',
    '普纳穆，普纳穆': 'Witi Ihimaera',
    '雪河来客': 'Banjo Paterson',
    '我们曾经是海洋': 'Epeli Hauʻofa',
    '无糖': 'Jack Davis',
    '鳄鱼': 'Vincent Eri',
    '阿卜杜拉游记': 'Abdullah bin Abdul Kadir',
    '三界经': '立泰王（Lithai）',
    '阿周那婚礼': 'Mpu Kanwa',
}

ANON_MAP = {
    '坤昌坤平': '佚名（口传与宫廷整理传统）',
    '杭图亚传': '佚名',
    '拉玛衍那卡卡温': '佚名',
    '阿米尔·哈姆扎传': '佚名',
    '南国山河': '佚名（传统归李常杰）',
    '琉璃宫史': '缅甸皇家历史委员会（编纂）',
    '马来纪年': '佚名（后世编纂传统）',
}

TITLE_ORIGINAL = {
    '夕雾花园': 'The Garden of Evening Mists',
    '彩虹战士': 'Laskar Pelangi',
    '美丽是一种伤': 'Cantik Itu Luka',
    '天使在我桌上': 'An Angel at My Table',
    '如果我们梦想太久': 'If We Dream Too Long',
    '曼谷苏醒': 'Bangkok Wakes to Rain',
    '雨之赐': 'The Gift of Rain',
    '西蒂·努尔巴雅': 'Sitti Nurbaya',
    '沙丽娜': 'Salina',
    '卡彭塔利亚湾': 'Carpentaria',
    '曾经是勇士': 'Once Were Warriors',
    '花园聚会': 'The Garden Party',
    '荆棘鸟': 'The Thorn Birds',
    '鲸骑士': 'The Whale Rider',
    '兔子证明栅栏': 'Follow the Rabbit-Proof Fence',
    '幽灵鸟': 'Ghost Bird',
    '普纳穆，普纳穆': 'Pounamu, Pounamu',
    '我们曾经是海洋': 'We Are the Ocean',
    '无糖': 'No Sugar',
    '鳄鱼': 'The Crocodile',
    '坤昌坤平': 'Khun Chang Khun Phaen',
}

YEAR_MAP = {
    '夕雾花园': 2012,
    '彩虹战士': 2005,
    '美丽是一种伤': 2002,
    '天使在我桌上': 1984,
    '如果我们梦想太久': 1972,
    '曼谷苏醒': 2019,
    '雨之赐': 2007,
    '西蒂·努尔巴雅': 1922,
    '沙丽娜': 1961,
    '卡彭塔利亚湾': 2006,
    '我的地方': 1987,
    '曾经是勇士': 1990,
    '花园聚会': 1922,
    '荆棘鸟': 1977,
    '鲸骑士': 1987,
    '兔子证明栅栏': 1996,
    '幽灵鸟': 2019,
    '普纳穆，普纳穆': 1972,
    '雪河来客': 1890,
    '我们曾经是海洋': 2008,
    '无糖': 1985,
    '鳄鱼': 1970,
}


def split(text):
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n?(.*)$', text, re.S)
    return (m.group(1), m.group(2)) if m else ('', text)

def scalar(front, key):
    m = re.search(rf'(?m)^{re.escape(key)}:\s*["\']?(.*?)["\']?\s*$', front)
    return m.group(1).strip(' "\'') if m else ''

def list_field(front, key):
    lines = front.splitlines(); out = []
    for i, line in enumerate(lines):
        if re.match(rf'^{re.escape(key)}:\s*\[\]\s*$', line): return []
        if re.match(rf'^{re.escape(key)}:\s*$', line):
            for n in lines[i+1:]:
                mm = re.match(r'^\s*-\s*["\']?(.*?)["\']?\s*$', n)
                if mm:
                    out.append(mm.group(1)); continue
                if n.strip() and not n.startswith((' ', '\t')): break
            return out
    return []

def q(v):
    return '"' + str(v).replace('\\', '\\\\').replace('"', '\\"') + '"'

def set_scalar(front, key, val):
    line = f'{key}: {q(val)}'
    if re.search(rf'(?m)^{re.escape(key)}:', front):
        return re.sub(rf'(?m)^{re.escape(key)}:.*$', line, front, 1)
    return front.rstrip() + '\n' + line

def render(front, body):
    return '---\n' + front.strip() + '\n---\n' + body.lstrip('\n')

# Identify unresolved missing-author R8/R9 structural records.
missing = []
for p in sorted(WORKS.glob('*.md')):
    text = p.read_text(encoding='utf-8'); front, body = split(text)
    if scalar(front, 'type') != 'work': continue
    if scalar(front, 'author'): continue
    axes = list_field(front, 'axis_r')
    if 'R8 东南亚文学' not in axes and 'R9 大洋洲与太平洋' not in axes: continue
    missing.append((p, front, body))

repaired = []
anonymized = []
quarantined = []

for p, front, body in missing:
    title = scalar(front, 'title') or p.stem
    if title in AUTHOR_MAP:
        front = set_scalar(front, 'author', AUTHOR_MAP[title])
        front = set_scalar(front, 'author_source', 'r8_r9_bibliographic_cleanup_v1_curated')
        if title in TITLE_ORIGINAL and not scalar(front, 'title_original'):
            front = set_scalar(front, 'title_original', TITLE_ORIGINAL[title])
        if title in YEAR_MAP and not scalar(front, 'year').strip():
            front = set_scalar(front, 'year', YEAR_MAP[title])
        front = set_scalar(front, 'bibliography_status', 'curated_bibliographic_anchor_v1')
        front = set_scalar(front, 'verification_status', '书目清理V1：作者已核定，其他字段按现有证据保留')
        p.write_text(render(front, body), encoding='utf-8')
        repaired.append(title)
    elif title in ANON_MAP:
        front = set_scalar(front, 'author', ANON_MAP[title])
        front = set_scalar(front, 'author_source', 'r8_r9_bibliographic_cleanup_v1_traditional_authorship')
        if title in TITLE_ORIGINAL and not scalar(front, 'title_original'):
            front = set_scalar(front, 'title_original', TITLE_ORIGINAL[title])
        front = set_scalar(front, 'bibliography_status', 'traditional_or_compiled_authorship_v1')
        front = set_scalar(front, 'verification_status', '书目清理V1：传统/编纂作者身份已规范')
        p.write_text(render(front, body), encoding='utf-8')
        anonymized.append(title)
    else:
        # Preserve evidence but remove from canonical Work layer until bibliographically verified.
        front = set_scalar(front, 'type', 'work_candidate')
        front = set_scalar(front, 'candidate_status', 'quarantined_pending_bibliographic_verification')
        front = set_scalar(front, 'bibliography_status', 'quarantined_structural_placeholder_v1')
        front = set_scalar(front, 'verification_status', '书目清理V1：退出canonical Work，待真实作品/作者核验')
        p.write_text(render(front, body), encoding='utf-8')
        quarantined.append(title)

# Downgrade R8/R9 work-support completion claims until coverage is revalidated.
for folder, fname, code in [
    ('R8 东南亚文学', '00 东南亚文学.md', 'R8'),
    ('R9 大洋洲与太平洋文学', '00 大洋洲与太平洋文学.md', 'R9'),
]:
    hp = ROOT / '30 专题' / folder / fname
    text = hp.read_text(encoding='utf-8')
    text = text.replace(f'`{code}_WORK_SUPPORT = COMPLETE`', f'`{code}_WORK_SUPPORT = REQUIRES_BIBLIOGRAPHIC_REVALIDATION`')
    text = text.replace(f'`{code}_TOPIC_MAP_V1 = COMPLETE_USABLE`', f'`{code}_TOPIC_MAP_V1 = STRUCTURE_COMPLETE_WORK_SUPPORT_REVALIDATING`')
    hp.write_text(text, encoding='utf-8')

# Post-cleanup counts.
def active_count(axis_label):
    n = 0
    for p in WORKS.glob('*.md'):
        f, _ = split(p.read_text(encoding='utf-8'))
        if scalar(f, 'type') == 'work' and axis_label in list_field(f, 'axis_r'):
            n += 1
    return n

def active_missing_authors():
    rows = []
    for p in WORKS.glob('*.md'):
        f, _ = split(p.read_text(encoding='utf-8'))
        if scalar(f, 'type') != 'work' or scalar(f, 'author'): continue
        axes = list_field(f, 'axis_r')
        if any(x.startswith('R') for x in axes):
            rows.append(p.stem)
    return rows

remaining = active_missing_authors()
lines = [
    '# R8/R9 Bibliographic Cleanup V1', '',
    f'- Missing-author R8/R9 records reviewed: **{len(missing)}**',
    f'- Curated real works repaired: **{len(repaired)}**',
    f'- Traditional/compiled authorship normalized: **{len(anonymized)}**',
    f'- Unverified structural placeholders quarantined as `work_candidate`: **{len(quarantined)}**',
    f'- Active R8 Works after cleanup: **{active_count("R8 东南亚文学")}**',
    f'- Active R9 Works after cleanup: **{active_count("R9 大洋洲与太平洋")}**',
    f'- Active R-axis Works still missing author: **{len(remaining)}**', '',
    '## Governance', '',
    '- No unresolved R8/R9 missing-author record is allowed to remain an active canonical `type: work`.',
    '- Quarantined records are preserved for audit; they are not deleted.',
    '- R8/R9 `WORK_SUPPORT = COMPLETE` is withdrawn pending structural revalidation against verified works.',
    '- Bibliographic cleanup does not invent authors for ambiguous titles or regional anthology placeholders.', '',
    '## Repaired real works',
]
for x in repaired:
    lines.append(f'- {x}')
lines += ['', '## Traditional/compiled authorship']
for x in anonymized:
    lines.append(f'- {x}')
lines += ['', '## Quarantined candidates']
for x in quarantined:
    lines.append(f'- {x}')
if remaining:
    lines += ['', '## Remaining active R-axis author gaps'] + [f'- {x}' for x in remaining]
lines += ['', '`R8_R9_BIBLIOGRAPHIC_CLEANUP_V1 = PASS_WITH_QUARANTINE_AND_REVALIDATION_REQUIRED`', '']
AUD.parent.mkdir(parents=True, exist_ok=True)
AUD.write_text('\n'.join(lines), encoding='utf-8')
print(f'repaired={len(repaired)} anon={len(anonymized)} quarantined={len(quarantined)} remaining={len(remaining)}')
