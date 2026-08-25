from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path('个人通识知识系统_v2_A2/30 世界文学')
WORKS = ROOT / '40 作品'
AUDIT = ROOT / '_audit' / 'entity_dedup'
SCAN_AUDIT = ROOT / '_audit' / 'entity_dedup_scan'
MARKER = AUDIT / 'APPLY_ENTITY_DEDUP_V2'
REPORT = AUDIT / 'ENTITY_DEDUP_V2.md'
GUARD = SCAN_AUDIT / 'NEGATIVE_MATCH_GUARD_V1.csv'

MERGES = [
    dict(canonical='社会毒瘤.md', duplicate='Noli Me Tangere.md', cid='WL-WORK-3171', did='WL-WORK-T3-NOLI-ME-TANGERE', title_original='Noli Me Tangere', aliases=['Noli Me Tangere','不许犯我'], year='1887', axis_t=['T3 19世纪现代文学体系'], note='José Rizal 的 Noli Me Tangere；英文/原题实体与中文实体合并。'),
    dict(canonical='伊本·白图泰游记.md', duplicate='Rihla.md', cid='WL-WORK-T1-RIHLA', did='WL-WORK-1368', title_original='Rihla', aliases=['Rihla','伊本白图泰游记','Rihla / 伊本·白图泰游记'], year='', axis_t=['T1 中古多中心文学世界'], note='Ibn Battuta 的 Rihla；T1 网络属性与 QT14 旅行文学属性合并。'),
    dict(canonical='卡皮斯特拉诺的诅咒.md', duplicate='佐罗的诅咒.md', cid='WL-WORK-2470', did='WL-WORK-2448', title_original='The Curse of Capistrano', aliases=['The Curse of Capistrano','佐罗的诅咒','The Mark of Zorro'], year='1919', axis_t=['T4 全球现代主义时代'], note='Johnston McCulley 的 The Curse of Capistrano；不同中文译名与骑士/剑客专题属性合并。'),
    dict(canonical='白鲸.md', duplicate='莫比·迪克.md', cid='WL-WORK-T3-MOBY-DICK', did='WL-WORK-2844', title_original='Moby-Dick', aliases=['Moby-Dick','莫比·迪克'], year='1851', axis_t=['T3 19世纪现代文学体系'], note='Herman Melville 的 Moby-Dick；T3 锚点与 CANON-129 Core 实体合并。'),
    dict(canonical='阿尔戈船英雄纪.md', duplicate='阿尔戈英雄纪.md', cid='WL-WORK-0865', did='WL-WORK-1515', title_original='Argonautica', aliases=['Argonautica','阿尔戈英雄纪'], year='', axis_t=[], note='Apollonius of Rhodes 的 Argonautica；冒险与神话专题入口合并。'),
    dict(canonical='开往巴基斯坦的列车.md', duplicate='开往巴基斯坦的火车.md', cid='WL-WORK-T5-TRAIN-PAKISTAN', did='WL-WORK-1098', title_original='Train to Pakistan', aliases=['Train to Pakistan','开往巴基斯坦的火车'], year='1956', axis_t=['T5 二战后多极文学'], note='Khushwant Singh 的 Train to Pakistan；列车/火车异译与 T5/历史专题属性合并。'),
    dict(canonical='法昆多.md', duplicate='Facundo.md', cid='WL-WORK-1765', did='WL-WORK-2223', title_original='Facundo', aliases=['Facundo'], year='1845', axis_t=['T3 19世纪现代文学体系'], note='Domingo Faustino Sarmiento 的 Facundo；作者简称差异导致的重复实体合并。'),
]

NEGATIVE = [
    ('Estoire del Saint Graal.md','Queste del Saint Graal.md','圣杯循环中的不同文本'),
    ('人世间.md','人世间（普拉姆迪亚）.md','不同作者：梁晓声 vs Pramoedya Ananta Toer'),
    ('历史.md','历史（莫兰特）.md','不同作者/不同作品：Herodotus vs Elsa Morante'),
    ('失乐园.md','失乐园（弥尔顿）.md','不同作者/不同作品：Junichi Watanabe vs John Milton'),
    ('凯瑟琳·安·波特短篇小说集.md','琼·斯塔福德短篇小说集.md','不同作者的短篇小说集'),
]

LIST_KEYS = {'aliases','literary_traditions','axis_t','axis_r','axis_m','axis_g','axis_q','awards','topics','topic_links','martial_systems'}

def split_doc(text: str):
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n?(.*)$', text, re.S)
    if not m:
        raise ValueError('missing frontmatter')
    return m.group(1), m.group(2)

def parse_blocks(fm: str):
    lines = fm.splitlines()
    blocks = []
    cur = None
    for line in lines:
        m = re.match(r'^([A-Za-z0-9_]+):(?:\s*(.*))?$', line)
        if m:
            if cur: blocks.append(cur)
            cur = [m.group(1), [line]]
        elif cur:
            cur[1].append(line)
    if cur: blocks.append(cur)
    return {k:v for k,v in blocks}

def block_values(lines):
    first = lines[0]
    if re.search(r':\s*\[\s*\]\s*$', first): return []
    out=[]
    for x in lines[1:]:
        m=re.match(r'^\s*-\s*(.*?)\s*$',x)
        if m: out.append(m.group(1).strip().strip("'\""))
    return out

def list_block(key, vals):
    if not vals: return [f'{key}: []']
    return [f'{key}:'] + [f'- {v}' for v in vals]

def scalar_value(lines):
    raw=lines[0].split(':',1)[1].strip()
    return '' if raw.lower() in {'','null','none','~'} else raw.strip("'\"")

def merge_group(g):
    cp, dp = WORKS/g['canonical'], WORKS/g['duplicate']
    if not cp.exists() or not dp.exists(): raise SystemExit(f'missing pair: {cp} / {dp}')
    ctext=cp.read_text(encoding='utf-8-sig'); dtext=dp.read_text(encoding='utf-8-sig')
    cfm,cbody=split_doc(ctext); dfm,_=split_doc(dtext)
    cb,db=parse_blocks(cfm),parse_blocks(dfm)
    if scalar_value(cb['id']) != g['cid'] or scalar_value(db['id']) != g['did']:
        raise SystemExit(f'id mismatch for {g["canonical"]}')

    # Copy missing metadata blocks from duplicate; union simple list-like blocks.
    for key,dlines in db.items():
        if key in {'id','type','title'}: continue
        if key not in cb:
            cb[key]=dlines
            continue
        cvals,dvals=block_values(cb[key]),block_values(dlines)
        looks_list = key in LIST_KEYS or key.endswith('_refs') or key.endswith('_axes') or key.endswith('_mechanism')
        if looks_list and (cvals or dvals or '[]' in cb[key][0] or '[]' in dlines[0]):
            vals=[]
            for v in cvals+dvals:
                if v not in vals: vals.append(v)
            cb[key]=list_block(key,vals)
        elif not scalar_value(cb[key]) and scalar_value(dlines):
            cb[key]=dlines

    # Governed identity/chronology overrides and alias union.
    cb['title_original']=[f"title_original: {g['title_original']}"]
    av=[]
    if 'aliases' in cb: av += block_values(cb['aliases'])
    if 'aliases' in db: av += block_values(db['aliases'])
    av += g['aliases'] + [Path(g['duplicate']).stem]
    aliases=[]
    for v in av:
        if v and v not in aliases: aliases.append(v)
    cb['aliases']=list_block('aliases', aliases)
    cb['axis_t']=list_block('axis_t', g['axis_t'])
    if g['year']:
        cb['year']=[f"year: {g['year']}"]
    cb['verification_status']=['verification_status: 人工核验']
    if g['year']:
        cb['bibliography_status']=['bibliography_status: verified']
    cb['review_note']=["review_note: '实体去重 V2：" + g['note'].replace("'",'') + "'"]

    # Keep canonical key order, then append newly inherited keys.
    c_order=[k for k,_ in parse_blocks(cfm).items()]
    keys=[]
    for k in c_order + list(db.keys()) + ['title_original','aliases','year','verification_status','bibliography_status','review_note']:
        if k in cb and k not in keys: keys.append(k)
    fm='\n'.join(line for k in keys for line in cb[k])
    governance = f"\n\n## 实体治理\n\n> Dedup V2：已将 `{g['duplicate']}`（{g['did']}）合并到本 canonical Work（{g['cid']}）。异译名/原题保留在 aliases；重复 Work 不再维护。\n"
    cp.write_text('---\n'+fm+'\n---\n'+cbody.rstrip()+governance, encoding='utf-8', newline='\n')
    return cp,dp

def active_files():
    for p in ROOT.rglob('*'):
        if not p.is_file() or p.suffix.lower() not in {'.md','.canvas','.base','.csv','.json','.yaml','.yml'}: continue
        rel=p.relative_to(ROOT)
        if '_source' in rel.parts or '_audit' in rel.parts or p.parent==WORKS: continue
        yield p

def rewrite_refs(g):
    changed=0; oldstem=Path(g['duplicate']).stem; newstem=Path(g['canonical']).stem
    pat=re.compile(r'(\[\[(?:[^\]\n]*?/)? )')
    for p in active_files():
        try: text=p.read_text(encoding='utf-8-sig')
        except UnicodeDecodeError: continue
        new=text.replace(g['did'],g['cid'])
        # Rewrite only wikilink targets, never ordinary prose/title mentions.
        new=re.sub(r'(\[\[(?:[^\]\n]*?/)?)(?P<t>'+re.escape(oldstem)+r')(?=(?:\||#|\]\]))', lambda m:m.group(1)+newstem, new)
        if new!=text:
            p.write_text(new,encoding='utf-8',newline='\n'); changed+=1
    return changed

def main():
    if not MARKER.exists(): raise SystemExit('Dedup V2 authorization marker missing')
    AUDIT.mkdir(parents=True,exist_ok=True); SCAN_AUDIT.mkdir(parents=True,exist_ok=True)
    before=len(list(WORKS.glob('*.md'))); rows=[]
    for g in MERGES:
        cp,dp=merge_group(g)
        rewritten=rewrite_refs(g)
        dp.unlink()
        rows.append((g['duplicate'],g['canonical'],g['did'],g['cid'],rewritten))
    after=len(list(WORKS.glob('*.md')))
    if before-after != len(MERGES): raise SystemExit(f'expected {len(MERGES)} Work removals, got {before-after}')
    for g in MERGES:
        if (WORKS/g['duplicate']).exists() or not (WORKS/g['canonical']).exists(): raise SystemExit('post-merge file verification failed')

    with GUARD.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.writer(f); w.writerow(['file_a','file_b','decision','reason'])
        for a,b,r in NEGATIVE: w.writerow([a,b,'DO_NOT_MERGE',r])

    md=['# Canonical Work Entity Dedup V2','',f'- Confirmed duplicate groups merged: **{len(MERGES)}**',f'- Duplicate Work files removed: **{len(MERGES)}**',f'- Work population before: **{before}**',f'- Work population after: **{after}**',f'- Negative-match guards: **{len(NEGATIVE)}**','','## Merges','','| Removed duplicate | Canonical Work | ID redirect | Active files rewritten |','|---|---|---|---:|']
    for d,c,did,cid,n in rows: md.append(f'| `{d}` | `{c}` | `{did}` → `{cid}` | {n} |')
    md += ['', '## Negative-match guard', '']
    for a,b,r in NEGATIVE: md.append(f'- `{a}` ↔ `{b}` — {r}')
    md += ['', '`CANONICAL_WORK_ENTITY_DEDUP_V2 = APPLIED_AND_VERIFIED`','']
    REPORT.write_text('\n'.join(md),encoding='utf-8',newline='\n')
    MARKER.unlink()

if __name__=='__main__': main()
