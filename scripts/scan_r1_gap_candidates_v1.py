from pathlib import Path
import re

ROOT=Path('个人通识知识系统_v2_A2/30 世界文学/40 作品')
AUDIT=Path('个人通识知识系统_v2_A2/30 世界文学/_audit/r_axis_r1')
OUT=AUDIT/'R1_GAP_CANDIDATE_SCAN_V1.md'

CANDIDATES={
'乌尔哀歌':['Lament for Ur','Lamentation over the Destruction of Ur'],
'巴比伦神义论':['Babylonian Theodicy'],
'普塔霍特普教谕':['Instruction of Ptahhotep','Maxims of Ptahhotep'],
'能言善辩的农夫':['The Eloquent Peasant'],
'萨福诗歌':['Sappho'],
'利西翠妲':['Lysistrata'],
'历史（希罗多德）':['Histories','The Histories'],
'阿尔戈船英雄纪':['Argonautica','阿尔戈英雄纪'],
'歌集（贺拉斯）':['Odes','Carmina'],
'孪生兄弟':['Menaechmi','The Brothers Menaechmus'],
'讽刺诗（尤维纳利斯）':['Satires','The Satires'],
'编年史（塔西佗）':['Annals','The Annals'],
'论演说家':['De Oratore','On the Orator'],
'金驴记':['The Golden Ass','Metamorphoses (Apuleius)'],
'米示拿':['Mishnah','Mishna'],
'犹大·哈列维诗歌':['Judah Halevi poems','Poems of Judah Halevi'],
'古兰经':['Quran','Qur’an','Koran'],
'一腿跨过一腿':['Leg over Leg','Al-Saq ala al-Saq'],
'哈菲兹诗集':['Divan of Hafez','Divan-e Hafez'],
'传说（尼玛·尤希吉）':['Afsaneh','The Myth'],
'苏乌尚':['Savushun','Suvashun'],
'尤努斯·埃姆雷诗集':['Yunus Emre Divan','Divan of Yunus Emre'],
'卡拉贾奥兰诗歌':['Karacaoğlan','Karacaoglan'],
'觉醒':['İntibah','Intibah'],
'禁忌之恋':['Aşk-ı Memnu','Ask-i Memnu'],
'巴基诗集':['Bâkî Divanı','Baki Divan','Divan of Baki'],
}

def norm(s):
    return re.sub(r'[^0-9a-z\u4e00-\u9fff]+','',s.lower())

def fields(text):
    m=re.match(r'^---\s*\n(.*?)\n---',text,re.S)
    if not m:return []
    fm=m.group(1)
    vals=[]
    for key in ('title','title_original','author','author_original'):
        x=re.search(rf'(?m)^{key}:\s*["\']?(.*?)["\']?\s*$',fm)
        if x: vals.append(x.group(1).strip())
    am=re.search(r'(?ms)^aliases:\s*\n((?:\s*-.*\n?)*)',fm)
    if am:
        vals += [re.sub(r'^\s*-\s*','',x).strip().strip('"\'') for x in am.group(1).splitlines() if x.strip().startswith('-')]
    return vals

index=[]
for p in ROOT.glob('*.md'):
    if p.name.startswith('00 '): continue
    try: text=p.read_text(encoding='utf-8-sig')
    except UnicodeDecodeError: continue
    vals=[p.stem]+fields(text)
    index.append((p,vals,{norm(v) for v in vals if v}))

lines=['# R1 Gap Candidate Scan V1','',f'- Candidate anchors: **{len(CANDIDATES)}**','', '| Candidate | Result | Existing file | Matched value |','|---|---|---|---|']
found=0
for title,alts in CANDIDATES.items():
    keys=[title]+alts
    hits=[]
    for p,vals,nvals in index:
        for k in keys:
            nk=norm(k)
            if nk and nk in nvals:
                mv=next((v for v in vals if norm(v)==nk),'')
                hits.append((p.name,mv)); break
    if hits:
        found+=1
        rendered='; '.join(f'{fn} / {mv}' for fn,mv in hits[:5])
        lines.append(f'| {title} | REUSE_REVIEW | {rendered} | exact normalized identity |')
    else:
        lines.append(f'| {title} | NEW_CANDIDATE | — | — |')
lines += ['',f'- Reuse candidates: **{found}**',f'- New candidates: **{len(CANDIDATES)-found}**','','`R1_GAP_CANDIDATE_SCAN_V1 = COMPLETE_READ_ONLY`','']
OUT.write_text('\n'.join(lines),encoding='utf-8')
print(f'candidates={len(CANDIDATES)} reuse={found} new={len(CANDIDATES)-found}')
