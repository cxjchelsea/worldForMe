from pathlib import Path
import re, json

ROOT = Path('个人通识知识系统_v2_A2/30 世界文学')
TOPROOT = ROOT/'30 专题'
NODEROOT = ROOT/'20 节点'/'R 地域'
WORKS = ROOT/'40 作品'
AUD = ROOT/'_audit'/'r_axis_acceptance'
AUD.mkdir(parents=True, exist_ok=True)

spec = {
'R1': ('R1 西亚—地中海古老传统', '00 西亚—地中海古老传统.md'),
'R2': ('R2 东亚文学', '00 东亚文学.md'),
'R3': ('R3 南亚文学', '00 南亚文学.md'),
'R4': ('R4 欧洲文学', '00 欧洲文学.md'),
'R5': ('R5 北美文学', '00 北美文学.md'),
'R6': ('R6 拉丁美洲与加勒比', '00 拉丁美洲文学.md'),
'R7': ('R7 非洲文学', '00 非洲文学.md'),
'R8': ('R8 东南亚文学', '00 东南亚文学.md'),
'R9': ('R9 大洋洲与太平洋文学', '00 大洋洲与太平洋文学.md'),
'R10': ('R10 跨区域文学传统', '00 跨区域文学传统.md'),
}

required_dirs = ['10 核心结构','11 内部传统','12 跨传统网络']
issues=[]; rows=[]

for code,(dirname,home) in spec.items():
    d=TOPROOT/dirname
    status=[]
    if not d.exists():
        issues.append((code,'MISSING_TOPIC_DIR',str(d))); rows.append((code,'FAIL','topic dir missing')); continue
    hp=d/home
    if not hp.exists(): issues.append((code,'MISSING_HOME',str(hp)))
    files=list(d.iterdir()) if d.exists() else []
    has_canvas=any(p.suffix=='.canvas' for p in files)
    bases=[p for p in files if p.suffix=='.base']
    if not has_canvas: issues.append((code,'MISSING_CANVAS',str(d)))
    if len(bases)<2: issues.append((code,'BASE_COUNT_LT_2',str(d)))
    for rd in required_dirs:
        p=d/rd
        if not p.exists(): issues.append((code,'MISSING_STD_DIR',str(p)))
        elif not any(p.iterdir()): issues.append((code,'EMPTY_STD_DIR',str(p)))
    if hp.exists():
        t=hp.read_text(encoding='utf-8')
        if 'TOPIC_MAP_V1 = COMPLETE_USABLE' not in t: issues.append((code,'HOME_STATUS_NOT_COMPLETE',str(hp)))
        if '文学结构' not in t or '作品' not in t: issues.append((code,'HOME_NAV_INCOMPLETE',str(hp)))
    node_candidates=list(NODEROOT.glob(f'{code} *.md')) if code!='R10' else list(NODEROOT.glob('R10 跨区域文学传统.md'))
    if not node_candidates: issues.append((code,'MISSING_NODE',''))
    else:
        nt=node_candidates[0].read_text(encoding='utf-8')
        if 'topic_map: null' in nt: issues.append((code,'NODE_TOPIC_MAP_NULL',str(node_candidates[0])))
    rows.append((code,'PASS' if not any(x[0]==code for x in issues) else 'FAIL',dirname))

# R10 governance
r10node=NODEROOT/'R10 跨区域文学传统.md'
r102node=NODEROOT/'R10.2 非洲离散文学.md'
if r10node.exists():
    t=r10node.read_text(encoding='utf-8')
    if not re.search(r'(?m)^anchorable:\s*false\s*$',t): issues.append(('R10','R10_MUST_BE_NONANCHORABLE',str(r10node)))
if not r102node.exists(): issues.append(('R10.2','MISSING_R10_2_NODE',''))
else:
    t=r102node.read_text(encoding='utf-8')
    if not re.search(r'(?m)^anchorable:\s*true\s*$',t): issues.append(('R10.2','R10_2_MUST_BE_ANCHORABLE',str(r102node)))

# Work-coordinate governance
illegal_r10=[]; illegal_r77=[]
for p in WORKS.glob('*.md'):
    txt=p.read_text(encoding='utf-8', errors='ignore')
    if re.search(r'(?m)^\s*-\s*R10 跨区域文学传统\s*$',txt): illegal_r10.append(p.name)
    if 'R7.7' in txt: illegal_r77.append(p.name)
if illegal_r10: issues.append(('WORKS','ILLEGAL_AXIS_R10',','.join(illegal_r10[:20])))
if illegal_r77: issues.append(('WORKS','ILLEGAL_R7_7',','.join(illegal_r77[:20])))

# duplicate structural filenames/ids in topic notes
ids={}; dupids=[]
for dname,_ in spec.values():
    d=TOPROOT/dname
    if not d.exists(): continue
    for p in d.rglob('*.md'):
        txt=p.read_text(encoding='utf-8', errors='ignore')
        m=re.search(r'(?m)^id:\s*["\']?([^"\'\n]+)',txt)
        if m:
            i=m.group(1).strip()
            if i in ids and ids[i]!=str(p): dupids.append((i,ids[i],str(p)))
            ids[i]=str(p)
if dupids: issues.append(('TOPICS','DUPLICATE_TOPIC_IDS',str(dupids[:10])))

# summary
lines=['# R Axis Acceptance Audit V1','',f'- Topic maps checked: **{len(spec)}**',f'- Issues: **{len(issues)}**',f'- Illegal `axis_r: R10`: **{len(illegal_r10)}**',f'- Illegal `R7.7`: **{len(illegal_r77)}**','', '## Per topic']
for r in rows: lines.append(f'- {r[0]}: **{r[1]}** — {r[2]}')
lines += ['', '## Issues']
if issues:
    for a,b,c in issues: lines.append(f'- `{a}` — `{b}` — {c}')
else: lines.append('- None')
lines += ['', '## Acceptance', '`R_AXIS_ACCEPTANCE_V1 = PASS`' if not issues else '`R_AXIS_ACCEPTANCE_V1 = FAIL`']
(AUD/'R_AXIS_ACCEPTANCE_V1.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
(AUD/'r_axis_acceptance_v1.json').write_text(json.dumps({'issues':issues,'rows':rows,'illegal_r10':illegal_r10,'illegal_r77':illegal_r77},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'issues':len(issues),'illegal_r10':len(illegal_r10),'illegal_r77':len(illegal_r77)},ensure_ascii=False))
if issues: raise SystemExit(2)
