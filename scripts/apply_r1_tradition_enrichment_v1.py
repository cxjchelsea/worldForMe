from pathlib import Path
import re, csv

ROOT=Path('个人通识知识系统_v2_A2/30 世界文学/40 作品')
AUDIT=Path('个人通识知识系统_v2_A2/30 世界文学/_audit/r_axis_r1')
SRC=AUDIT/'r1_works_v1.csv'
REPORT=AUDIT/'R1_TRADITION_ENRICHMENT_V1.md'
MARKER=AUDIT/'APPLY_R1_TRADITION_ENRICHMENT_V1'

MAP={
'两河文学传统': {'伊南娜下降冥界','伊南娜与杜穆兹','吉尔伽美什史诗','埃努玛·埃利什','埃拉史诗','恩基与宁玛赫','恩基与宁胡尔萨格','阿特拉哈西斯史诗'},
'古埃及文学传统': {'埃及亡灵书','棺椁铭文','船难水手的故事','荷鲁斯与塞特之争','辛努赫传','金字塔铭文'},
'黎凡特—迦南与乌加里特文学传统': {'凯雷特史诗','巴力神话组诗','阿卡特史诗'},
'古希腊文学传统': {'伊利亚特','会饮篇','俄狄浦斯王','奥德赛','安提戈涅','工作与时日','希波吕托斯','理想国','神谱','美狄亚','荷马颂歌','酒神的伴侣','酒神的女信徒'},
'罗马与拉丁文学传统': {'变形记','埃涅阿斯纪','女英雄书简','岁时记','爱的艺术','爱经'},
'希伯来—犹太文学传统': {'以诺一书','但以理书','出埃及记','创世记','库萨里','往事','约伯记'},
'阿拉伯文学传统': {'Beirut Blues','一千零一夜','伊本·白图泰游记','卡里来和笛木乃','哈里里玛卡梅集','太阳下的人们','宫间街','开罗三部曲','思宫街','悬诗','悲观主义者塞义德的奇异事件','我们街区的孩子们','海法归来','烈日下的人们','甘露街','盐城','重返海法','队列'},
'波斯—伊朗文学传统': {'Safarnama / 旅行记','列王纪','扎哈克','本达希申','果园','玛斯纳维','盲枭','莱拉和马吉农','蔷薇园','阿维斯塔','鲁拜集','鲁斯塔姆与苏赫拉布','鸟的会议'},
'土耳其—奥斯曼文学传统': {'我的名字叫红','旅行书','时间调校研究所','杰夫代特先生和他的儿子们','瘦子麦麦德'},
}
TITLE_TO_TRAD={t:k for k,v in MAP.items() for t in v}
SKIP={'移居北方的时节'}

def fm_span(text):
    return re.match(r'^---\s*\n(.*?)\n---(?:\s*\n|$)',text,re.S)

def scalar(fm,key):
    m=re.search(rf'(?m)^{re.escape(key)}:\s*(.*?)\s*$',fm)
    if not m:return ''
    v=m.group(1).strip().strip('"\'')
    return '' if v.lower() in {'null','none','~'} else v

def set_scalar(fm,key,value):
    pat=rf'(?m)^{re.escape(key)}:\s*.*$'
    if re.search(pat,fm):return re.sub(pat,f'{key}: {value}',fm,count=1)
    return fm+f'\n{key}: {value}'

def main():
    if not MARKER.exists(): raise SystemExit('authorization marker missing')
    rows=list(csv.DictReader(SRC.open(encoding='utf-8-sig')))
    applied=[]; skipped=[]; blocked=[]
    for r in rows:
        title=r['title']; fn=r['file']
        if title in SKIP: skipped.append((title,'R1/R7 boundary review')); continue
        trad=TITLE_TO_TRAD.get(title)
        if not trad: blocked.append((title,'no reviewed tradition mapping')); continue
        p=ROOT/fn
        if not p.exists(): blocked.append((title,'file missing')); continue
        text=p.read_text(encoding='utf-8-sig'); m=fm_span(text)
        if not m: blocked.append((title,'frontmatter missing')); continue
        fm=m.group(1)
        if 'R1 西亚—地中海古老传统' not in fm:
            skipped.append((title,'no longer R1')); continue
        existing=scalar(fm,'r1_tradition')
        if existing and existing!=trad: blocked.append((title,f'conflict existing={existing}')); continue
        if existing==trad: skipped.append((title,'already enriched')); continue
        fm=set_scalar(fm,'r1_tradition',trad)
        p.write_text(text[:m.start(1)]+fm+text[m.end(1):],encoding='utf-8')
        applied.append((title,trad))
    lines=['# R1 Tradition Enrichment V1','',f'- Input historical R1 rows: **{len(rows)}**',f'- Applied: **{len(applied)}**',f'- Skipped: **{len(skipped)}**',f'- Blocked: **{len(blocked)}**','','- Mutated field: `r1_tradition` only.','- Global `axis_r` was not changed by this writer.','', '## Applied','']
    for t,tr in applied: lines.append(f'- {t} → {tr}')
    lines += ['','## Skipped','']
    for t,w in skipped: lines.append(f'- {t}: {w}')
    if blocked:
        lines += ['','## Blocked','']
        for t,w in blocked: lines.append(f'- {t}: {w}')
    lines += ['','`R1_TRADITION_ENRICHMENT_V1 = APPLIED_WITH_REVIEW_GATES`','']
    REPORT.write_text('\n'.join(lines),encoding='utf-8')
    MARKER.unlink()
    print(f'APPLIED={len(applied)} SKIPPED={len(skipped)} BLOCKED={len(blocked)}')
if __name__=='__main__': main()
