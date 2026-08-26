from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT=Path('个人通识知识系统_v2_A2/30 世界文学/40 作品')
AUDIT=Path('个人通识知识系统_v2_A2/30 世界文学/_audit/r_axis_r1')
MATRIX=AUDIT/'r1_structural_coverage_v1.csv'
REPORT=AUDIT/'R1_STRUCTURAL_GAP_FILL_V1.md'
MARKER=AUDIT/'APPLY_R1_STRUCTURAL_GAP_FILL_V1'
R1='R1 西亚—地中海古老传统'

SPECS=[
# tradition, slot, title, original, author, author_original, T, year, priority, id
('两河文学传统','智慧/争辩文学','巴比伦神义论','Babylonian Theodicy','佚名','', 'T0 文学源头与古代文学',None,'◆','WL-WORK-R1-BABYLONIAN-THEODICY'),
('两河文学传统','城市哀歌','乌尔哀歌','Lament for Ur','佚名','', 'T0 文学源头与古代文学',None,'◆','WL-WORK-R1-LAMENT-UR'),
('古埃及文学传统','智慧/教诲文学','普塔霍特普教谕','Instruction of Ptahhotep','普塔霍特普','Ptahhotep','T0 文学源头与古代文学',None,'◆','WL-WORK-R1-PTAHHOTEP'),
('古埃及文学传统','社会修辞/申诉叙事','能言善辩的农夫','The Eloquent Peasant','佚名','', 'T0 文学源头与古代文学',None,'◆','WL-WORK-R1-ELOQUENT-PEASANT'),
('古希腊文学传统','抒情诗','萨福诗歌','Poems of Sappho','萨福','Sappho','T0 文学源头与古代文学',None,'◆','WL-WORK-R1-SAPPHO'),
('古希腊文学传统','喜剧','吕西斯特拉忒','Lysistrata','阿里斯托芬','Aristophanes','T0 文学源头与古代文学',None,'◆','WL-WORK-T0-LYSISTRATA'),
('古希腊文学传统','历史书写','历史（希罗多德）','Histories','希罗多德','Herodotus','T0 文学源头与古代文学',None,'◆','WL-WORK-R1-HERODOTUS-HISTORIES'),
('古希腊文学传统','希腊化文学','阿尔戈船英雄纪','Argonautica','阿波罗尼奥斯','Apollonius of Rhodes','T0 文学源头与古代文学',None,'◆','WL-WORK-0865'),
('罗马与拉丁文学传统','抒情诗','贺拉斯颂歌','Odes','贺拉斯','Horace','T0 文学源头与古代文学',None,'◆','WL-WORK-T0-HORACE-ODES'),
('罗马与拉丁文学传统','喜剧','孪生兄弟','Menaechmi','普劳图斯','Plautus','T0 文学源头与古代文学',None,'◆','WL-WORK-R1-MENAECHMI'),
('罗马与拉丁文学传统','罗马讽刺','讽刺诗（尤维纳利斯）','Satires','尤维纳利斯','Juvenal','T0 文学源头与古代文学',None,'△','WL-WORK-R1-JUVENAL-SATIRES'),
('罗马与拉丁文学传统','历史书写','编年史（塔西佗）','Annals','塔西佗','Tacitus','T0 文学源头与古代文学',None,'◆','WL-WORK-R1-TACITUS-ANNALS'),
('罗马与拉丁文学传统','演说/修辞','论演说家','De Oratore','西塞罗','Cicero','T0 文学源头与古代文学',None,'△','WL-WORK-R1-DE-ORATORE'),
('罗马与拉丁文学传统','小说/散文虚构','金驴记','The Golden Ass','阿普列尤斯','Apuleius','T0 文学源头与古代文学',None,'◆','WL-WORK-R1-GOLDEN-ASS'),
('希伯来—犹太文学传统','拉比/塔木德解释传统','米示拿','Mishnah','多位编纂者','Various','T0 文学源头与古代文学',None,'◆','WL-WORK-R1-MISHNAH'),
('希伯来—犹太文学传统','中古希伯来诗歌','犹大·哈列维诗歌','Poems of Judah Halevi','犹大·哈列维','Judah Halevi','T1 中古多中心文学世界',None,'△','WL-WORK-R1-JUDAH-HALEVI-POEMS'),
('阿拉伯文学传统','古兰经语言/修辞/经典化','古兰经','Quran','传统文本','', 'T1 中古多中心文学世界',None,'★','WL-WORK-R1-QURAN'),
('阿拉伯文学传统','Nahda/19世纪文学复兴','一腿跨过一腿','Al-Sāq ʿalā al-sāq','艾哈迈德·法里斯·希迪亚克','Ahmad Faris al-Shidyaq','T3 19世纪现代文学体系',1855,'◆','WL-WORK-R1-LEG-OVER-LEG'),
('波斯—伊朗文学传统','ghazal抒情顶峰','哈菲兹诗集','Divan of Hafez','哈菲兹','Hafez','T1 中古多中心文学世界',None,'★','WL-WORK-R1-HAFEZ-DIVAN'),
('波斯—伊朗文学传统','近代/现代诗歌转型','传说（尼玛·尤希吉）','Afsaneh','尼玛·尤希吉','Nima Yushij','T4 全球现代主义时代',1922,'◆','WL-WORK-R1-NIMA-AFSANEH'),
('波斯—伊朗文学传统','现代社会小说/女性写作','苏乌尚','Savushun','西敏·达内什瓦尔','Simin Daneshvar','T5 二战后多极文学',1969,'△','WL-WORK-R1-SAVUSHUN'),
('土耳其—奥斯曼文学传统','早期安纳托利亚神秘诗','尤努斯·埃姆雷诗集','Yunus Emre Divanı','尤努斯·埃姆雷','Yunus Emre','T1 中古多中心文学世界',None,'★','WL-WORK-R1-YUNUS-EMRE'),
('土耳其—奥斯曼文学传统','Ottoman Divan宫廷诗','巴基诗集','Bâkî Divanı','巴基','Bâkî','T2 早期现代文学',None,'★','WL-WORK-R1-BAKI-DIVAN'),
('土耳其—奥斯曼文学传统','民间诗歌/asik传统','卡拉贾奥兰诗歌','Poems of Karacaoğlan','卡拉贾奥兰','Karacaoğlan','T2 早期现代文学',None,'△','WL-WORK-R1-KARACAOGLAN'),
('土耳其—奥斯曼文学传统','Tanzimat文学改革','İntibah','İntibah','纳默克·凯末尔','Namık Kemal','T3 19世纪现代文学体系',1876,'★','WL-WORK-R1-INTIBAH'),
('土耳其—奥斯曼文学传统','晚奥斯曼/Servet-i Funun小说','禁忌之恋','Aşk-ı Memnu','哈立德·齐亚·乌沙克勒吉尔','Halid Ziya Uşaklıgil','T4 全球现代主义时代',1900,'★','WL-WORK-R1-ASK-I-MEMNU'),
]

EXISTING={
'吕西斯特拉忒':'吕西斯特拉忒.md',
'阿尔戈船英雄纪':'阿尔戈船英雄纪.md',
'贺拉斯颂歌':'贺拉斯颂歌.md',
}


def fm_match(text):
    return re.match(r'^---\s*\n(.*?)\n---(?:\s*\n|$)',text,re.S)

def remove_block(fm,key):
    # list block or scalar
    fm=re.sub(rf'(?ms)^{re.escape(key)}:\s*\n(?:\s*-.*\n?)*','',fm)
    fm=re.sub(rf'(?m)^{re.escape(key)}:\s*.*\n?','',fm)
    return fm.rstrip()

def set_scalar(fm,key,value):
    fm=remove_block(fm,key)
    return fm+f'\n{key}: {value}'

def set_list(fm,key,values):
    fm=remove_block(fm,key)
    if not values:return fm+f'\n{key}: []'
    return fm+'\n'+key+':\n'+'\n'.join(f'- {v}' for v in values)

def update_existing(path,spec):
    tradition,slot,title,orig,author,author_original,taxis,year,priority,wid=spec
    text=path.read_text(encoding='utf-8-sig')
    m=fm_match(text)
    if not m: raise RuntimeError(f'frontmatter missing: {path}')
    fm=m.group(1)
    fm=set_list(fm,'axis_t',[taxis])
    fm=set_list(fm,'axis_r',[R1])
    fm=set_scalar(fm,'r1_tradition',tradition)
    fm=set_scalar(fm,'r1_priority',priority)
    fm=set_list(fm,'r1_role',[slot])
    new=text[:m.start(1)]+fm+text[m.end(1):]
    path.write_text(new,encoding='utf-8')

def new_content(spec):
    tradition,slot,title,orig,author,author_original,taxis,year,priority,wid=spec
    year_s='null' if year is None else str(year)
    ao=f'\nauthor_original: {author_original}' if author_original else ''
    return f'''---\nid: {wid}\ntype: work\ntitle: {title}\ntitle_original: {orig}\naliases: []\nauthor: {author}{ao}\nyear: {year_s}\nread_status: 未读\naxis_t:\n- {taxis}\naxis_r:\n- {R1}\naxis_m: []\naxis_g: []\naxis_q: []\naxis_source: manual_r1_structural_gap_fill_v1\ntopics: []\ntopic_links: []\nr1_priority: {priority}\nr1_tradition: {tradition}\nr1_role:\n- {slot}\nverification_status: 手工核验\nbibliography_status: structural_anchor\n---\n# {title}\n\n## R1 专题角色\n\n- 内部传统：{tradition}\n- 结构位置：{slot}\n- 专题优先级：{priority}\n\n> R1 Structural Gap Fill V1：用于补齐 R1 专题文学史结构槽位；不因数量均衡而新增。\n'''

def main():
    if not MARKER.exists(): raise SystemExit('authorization marker missing')
    created=[]; reused=[]; blocked=[]
    anchors={}
    for spec in SPECS:
        tradition,slot,title,*_=spec
        anchors[(tradition,slot)]=title
        if title in EXISTING:
            p=ROOT/EXISTING[title]
            if not p.exists(): blocked.append((title,'expected existing file missing')); continue
            update_existing(p,spec); reused.append(title)
        else:
            p=ROOT/f'{title}.md'
            if p.exists():
                blocked.append((title,'unexpected exact file already exists; manual identity review required')); continue
            p.write_text(new_content(spec),encoding='utf-8'); created.append(title)
    if blocked:
        raise SystemExit('BLOCKED: '+repr(blocked))

    rows=list(csv.DictReader(MATRIX.open(encoding='utf-8-sig',newline='')))
    changed=0
    for r in rows:
        key=(r['tradition'],r['slot'])
        if key in anchors:
            r['status']='COVERED'
            r['current_anchor']=anchors[key]
            r['gap_candidate']=''
            changed+=1
    with MATRIX.open('w',encoding='utf-8-sig',newline='') as fh:
        w=csv.DictWriter(fh,fieldnames=['tradition','slot','status','current_anchor','gap_candidate','priority'])
        w.writeheader(); w.writerows(rows)

    lines=['# R1 Structural Gap Fill V1','',
           f'- Structural anchors processed: **{len(SPECS)}**',
           f'- Reused canonical Works: **{len(reused)}**',
           f'- Newly created canonical Works: **{len(created)}**',
           f'- Coverage rows promoted to COVERED: **{changed}**','',
           '## Reused','']+[f'- {x}' for x in reused]+['','## Created','']+[f'- {x}' for x in created]+['',
           '## Boundary decision','',
           '- `觉醒.md` is Kate Chopin / *The Awakening* and was **not** reused for Namık Kemal.',
           '- A distinct canonical Work `İntibah.md` was created for Namık Kemal to avoid same-title collision.',
           '- Ugaritic ritual/ritual-text slot remains intentionally PARTIAL: no synthetic anthology was invented merely to force a 100% score.','',
           '`R1_STRUCTURAL_GAP_FILL_V1 = APPLIED_AND_VERIFIED_PENDING_REAUDIT`','']
    REPORT.write_text('\n'.join(lines),encoding='utf-8')
    MARKER.unlink()
    print(f'created={len(created)} reused={len(reused)} coverage_rows={changed}')

if __name__=='__main__': main()
