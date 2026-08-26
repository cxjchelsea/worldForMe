from __future__ import annotations
import re
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
LIT = ROOT/'个人通识知识系统_v2_A2'/'30 世界文学'
TOPICS = LIT/'30 专题'
WORKS = LIT/'40 作品'

CFG = {
'M1': dict(folder='M1 早期现代思想与美学', home='00 早期现代思想与美学', topic='WL-TOPIC-M1-EARLY-MODERN', prefix='m1', priority='m1_priority', cluster='m1_movement_cluster', axes='m1_axes', history='m1_history_position', cluster_label='专题思潮', group_view='按专题思潮', history_map={
'人文主义':'古典复兴与人文主义奠基','文艺复兴':'文艺复兴展开与世俗主体形成','巴洛克':'秩序危机与巴洛克复杂化','古典主义':'规则、宫廷与公共规范化','启蒙主义':'启蒙公共领域与理性批判成熟','感伤主义':'情感转向与浪漫主义前夜'}),
'M2': dict(folder='M2 19世纪文学思潮', home='00 19世纪文学思潮', topic='WL-TOPIC-M2-19C-MOVEMENTS', prefix='m2', priority='m2_priority', cluster='m2_movement_cluster', axes='m2_axes', history='m2_history_position', cluster_label='专题思潮', group_view='按专题思潮', history_map={
'浪漫主义':'革命后浪漫主义形成与扩张','超验主义':'19世纪中期美国精神独立与自然观重构','现实主义':'19世纪中期现实主义成熟','自然主义':'19世纪后期科学化与社会决定论','象征主义':'世纪末象征主义与现代主义前夜','唯美主义':'世纪末审美自主与艺术至上','颓废主义':'世纪末颓废意识与文化危机','拉美 Modernismo':'世纪末拉美现代主义前驱'}),
'M3.1': dict(folder='M3.1 现代主义', home='00 现代主义文学', topic='WL-TOPIC-M3-MODERNISM', prefix='modernism', priority='modernism_priority', cluster='modernism_tradition_cluster', axes='modernism_axes', history='modernism_history_position', cluster_label='现代主义传统', group_view='按现代主义传统', history_map={}),
'M3.2': dict(folder='M3.2 先锋派', home='00 先锋派', topic='WL-TOPIC-M3.2-AVANT-GARDE', prefix='m32', priority='m32_priority', cluster='m32_movement_cluster', axes='m32_axes', history='m32_history_position', cluster_label='先锋运动', group_view='按先锋运动', history_map={
'意大利未来主义':'1909后第一波先锋宣言与技术崇拜','俄国未来主义':'1910年代革命前后的语言与形式激进化','德语表现主义':'一战前后都市、战争与主体危机','达达主义':'一战时期反艺术与制度否定','超现实主义':'1920年代后无意识、自动书写与革命想象','意象主义与漩涡主义':'1910年代英语诗歌形式革新','构成主义、LEF与事实文学':'革命后苏俄艺术生产与事实文学','伊比利亚与拉美先锋派':'1920—1930年代跨大西洋先锋扩散'}),
'M4': dict(folder='M4 集体文学运动与文化政治', home='00 集体文学运动与文化政治', topic='WL-TOPIC-M4-COLLECTIVE-MOVEMENTS', prefix='m4', priority='m4_priority', cluster='m4_movement_cluster', axes='m4_axes', history='m4_history_position', cluster_label='集体运动', group_view='按集体运动', history_map={
'民族主义文学':'19世纪民族建构与语言文化共同体形成','无产阶级文学':'工业资本主义后阶级文学组织化','革命文学':'革命动员与集体主体形成','社会主义现实主义':'革命后制度化文学与国家文化政策','哈莱姆文艺复兴':'1920年代黑人都市文化复兴','Négritude':'1930—1950年代法语黑人国际主义与文化解放','反殖民文学运动':'二战后去殖民与民族解放文学','垮掉的一代':'1950年代反文化文学共同体','拉丁美洲Boom':'1960—1970年代跨国出版与全球文学网络'}),
'M5.1': dict(folder='M5.1 战后思想与美学范式', home='00 战后思想与美学范式', topic='WL-TOPIC-M5.1-POSTWAR-AESTHETICS', prefix='m51', priority='m51_priority', cluster='m51_movement_cluster', axes='m51_axes', history='m51_history_position', cluster_label='战后范式', group_view='按战后范式', history_map={
'存在主义':'1940—1950年代主体、自由与责任危机','荒诞':'1950—1960年代语言与行动失效','法国新小说':'1950—1970年代再现与人物危机','魔幻现实主义':'1940年代后现实层级重组与全球扩展','后现代主义':'1960年代后文本权威、媒介与历史叙事危机'}),
'M5.2': dict(folder='M5.2 权力、身份与世界批评', home='00 权力、身份与世界批评', topic='WL-TOPIC-M5.2-POWER-IDENTITY-WORLD', prefix='m52', priority='m52_priority', cluster='m52_framework_cluster', axes='m52_axes', history='m52_history_position', cluster_label='批评框架', group_view='按批评框架', history_map={
'后殖民':'二战后帝国解体与表述政治形成','去殖民':'20世纪后期殖民性与知识体系批判','女性主义':'20世纪女性解放运动与文学批评制度化','酷儿':'1980—1990年代后性别/性规范解构','生态批评':'20世纪后期环境危机与人类中心主义反思','生态文学':'环境危机进入文学世界建构与叙事实践'}),
}

EXPECTED={'M1':76,'M2':85,'M3.1':149,'M3.2':68,'M4':90,'M5.1':80,'M5.2':74}


def split_fm(text):
    if not text.startswith('---\n'): return '', text
    i=text.find('\n---\n',4)
    if i<0:return '',text
    return text[4:i],text[i+5:]

def scalar(fm,key):
    m=re.search(rf'(?m)^{re.escape(key)}:\s*["\']?([^\n"\']*)["\']?\s*$',fm)
    return m.group(1).strip() if m else ''

def list_field(fm,key):
    lines=fm.splitlines(); out=[]
    for i,l in enumerate(lines):
        if l.startswith(key+':'):
            tail=l.split(':',1)[1].strip()
            if tail.startswith('[') and tail.endswith(']'):
                return [x.strip().strip('"\'') for x in tail[1:-1].split(',') if x.strip()]
            j=i+1
            while j<len(lines) and (lines[j].startswith('- ') or lines[j].startswith('  - ')):
                out.append(lines[j].split('- ',1)[1].strip().strip('"\'')); j+=1
            return out
    return out

def replace_scalar(text,key,val):
    fm,body=split_fm(text); lines=fm.splitlines(); done=False; out=[]; i=0
    while i<len(lines):
        if re.match(rf'^{re.escape(key)}:',lines[i]):
            out.append(f'{key}: "{val}"'); done=True; i+=1
            while i<len(lines) and (lines[i].startswith('- ') or lines[i].startswith('  - ')): i+=1
            continue
        out.append(lines[i]); i+=1
    if not done: out.append(f'{key}: "{val}"')
    return '---\n'+'\n'.join(out)+'\n---\n'+body

def replace_list(text,key,vals):
    fm,body=split_fm(text); lines=fm.splitlines(); out=[]; done=False; i=0
    while i<len(lines):
        if re.match(rf'^{re.escape(key)}:',lines[i]):
            out.append(f'{key}:'); out.extend([f'- {v}' for v in vals]); done=True; i+=1
            while i<len(lines) and (lines[i].startswith('- ') or lines[i].startswith('  - ')): i+=1
            continue
        out.append(lines[i]); i+=1
    if not done:
        out.append(f'{key}:'); out.extend([f'- {v}' for v in vals])
    return '---\n'+'\n'.join(out)+'\n---\n'+body

def resolve_history(code,cfg,fm):
    cl=scalar(fm,cfg['cluster'])
    if cl in cfg['history_map']: return cfg['history_map'][cl]
    if code=='M3.1':
        t4=scalar(fm,'t4_history_position')
        if t4:return t4
        # fallback by broad tradition when no T4 history is available
        return '现代主义跨地域展开（具体阶段待中央年代元数据校准）'
    return f'{cl}（历史位置待细化）' if cl else '待专题历史定位'

def valid_topic_link(target):
    # target is path without alias, relative to WORKS
    p=(WORKS/target).resolve()
    candidates=[p, Path(str(p)+'.md')]
    return any(c.exists() and str(c).startswith(str(ROOT.resolve())) for c in candidates)

def clean_and_add_topic_links(text,cfg):
    fm,_=split_fm(text); existing=list_field(fm,'topic_links'); good=[]
    for item in existing:
        raw=item.strip("'\"")
        if not (raw.startswith('[[') and raw.endswith(']]')): continue
        inner=raw[2:-2]; target=inner.split('|',1)[0]
        if valid_topic_link(target): good.append(raw)
    new=f"[[../30 专题/{cfg['folder']}/{cfg['home']}|{cfg['folder'].split(' ',1)[1]}]]"
    # avoid duplicate same target even if alias differs
    targets={x[2:-2].split('|',1)[0] for x in good}
    nt=new[2:-2].split('|',1)[0]
    if nt not in targets: good.append(new)
    return replace_list(text,'topic_links',[f"'{x}'" for x in good])

def build_work_base(code,cfg):
    p,c,a,h=cfg['priority'],cfg['cluster'],cfg['axes'],cfg['history']
    props=[('file.name','作品'),('note.author','作者'),('note.read_status','阅读状态'),('note.topic_links','专题'),('note.topics','专题编号'),(f'note.{p}','优先级'),(f'note.{c}',cfg['cluster_label']),(f'note.{h}','历史位置'),(f'note.{a}','专题机制'),('note.axis_t','时间'),('note.axis_r','地域'),('note.axis_m','M轴坐标'),('note.axis_g','类型'),('note.axis_q','主题'),('note.id','编号'),('note.verification_status','校验状态')]
    order=['file.name','author','read_status','topic_links',p,c,h,a,'axis_t','axis_r','axis_m','axis_g','axis_q','id']
    s='filters:\n  and:\n    - type == "work"\n    - file.folder == "个人通识知识系统_v2_A2/30 世界文学/40 作品"\n    - topics.contains("'+cfg['topic']+'")\nproperties:\n'
    for k,label in props:s+=f'  {k}:\n    displayName: {label}\n'
    def view(name,filters=None,group=None):
        nonlocal s
        s+=f'  - type: table\n    name: {name}\n'
        if filters:
            s+='    filters:\n'+filters
        if group:s+=f'    groupBy:\n      property: {group}\n      direction: ASC\n'
        s+='    order:\n'+''.join(f'      - {x}\n' for x in order)
    s+='views:\n'; view('全部作品')
    view('核心 ★',f'      and:\n        - {p} == "★"\n')
    view('重点 ◆',f'      and:\n        - {p} == "◆"\n')
    view('扩展 △',f'      and:\n        - {p} == "△"\n')
    view('未读', '      and:\n        - read_status == "未读"\n')
    view('已读','      and:\n        - or:\n            - read_status == "已读"\n            - read_status == "重读"\n')
    view('按历史位置',group=h); view(cfg['group_view'],group=c); view('按地域',group='axis_r'); view('按M轴坐标',group='axis_m'); view('按类型',group='axis_g'); view('按主题',group='axis_q')
    view('待校验','      and:\n        - verification_status != "自动通过"\n        - verification_status != "手工核验"\n')
    return s

def build_struct_base(cfg):
    return f'''filters:\n  and:\n    - topic_id == "{cfg['topic']}"\nformulas:\n  type_zh: if(type == "literature_topic_mechanism", "形成机制", if(type == "literature_topic_section", "专题分支", "核心结构"))\n  dimension_zh: if(dimension, dimension.replace("tradition", "传统与地域").replace("movement", "思潮与运动").replace("paradigm", "美学范式").replace("framework", "批评框架").replace("historical_system", "谱系与内部结构").replace("core_question", "核心问题").replace("reading_route", "阅读路线").replace("transmission", "传播与地域").replace("comparison", "比较与边界").replace("definition", "定义与边界").replace("history", "时间框架与问题意识").replace("mechanism", "形成机制"), "")\nproperties:\n  file.name:\n    displayName: 节点\n  formula.type_zh:\n    displayName: 类型\n  formula.dimension_zh:\n    displayName: 维度\n  note.sequence:\n    displayName: 顺序\n  note.parent:\n    displayName: 父节点\n  note.history_position:\n    displayName: 历史位置\n  note.mechanism:\n    displayName: 机制\n  note.id:\n    displayName: 编号\nviews:\n  - type: table\n    name: 全部知识节点\n    order: [file.name, formula.type_zh, formula.dimension_zh, sequence, parent, history_position, mechanism, id]\n  - type: table\n    name: 核心结构\n    filters:\n      and:\n        - 'type != "literature_topic_section"'\n        - 'type != "literature_topic_mechanism"'\n        - 'dimension != "mechanism"'\n    order: [file.name, formula.type_zh, formula.dimension_zh, sequence, parent, history_position, mechanism, id]\n  - type: table\n    name: 专题分支\n    filters:\n      and:\n        - 'type == "literature_topic_section"'\n    order: [file.name, formula.type_zh, formula.dimension_zh, sequence, parent, history_position, mechanism, id]\n  - type: table\n    name: 形成机制\n    filters:\n      or:\n        - 'type == "literature_topic_mechanism"'\n        - 'dimension == "mechanism"'\n    order: [file.name, formula.type_zh, formula.dimension_zh, sequence, parent, history_position, mechanism, id]\n'''

# Gather canonical paths once for link validation.
for code,cfg in CFG.items():
    members=[]; freq=Counter()
    for wp in WORKS.glob('*.md'):
        text=wp.read_text(encoding='utf-8'); fm,_=split_fm(text)
        if cfg['topic'] not in list_field(fm,'topics'): continue
        members.append(wp)
        hist=resolve_history(code,cfg,fm)
        text=replace_scalar(text,cfg['history'],hist)
        for x in list_field(split_fm(text)[0],cfg['axes']): freq[x]+=1
        text=clean_and_add_topic_links(text,cfg)
        wp.write_text(text,encoding='utf-8')
    if len(members)!=EXPECTED[code]:
        raise SystemExit(f'{code}: canonical member count {len(members)} != {EXPECTED[code]}')
    td=TOPICS/cfg['folder']
    next(td.glob('03 *.base')).write_text(build_work_base(code,cfg),encoding='utf-8')
    next(td.glob('02 *.base')).write_text(build_struct_base(cfg),encoding='utf-8')
    top_mechs=[x for x,_ in freq.most_common(12)]
    for sp in td.rglob('*.md'):
        rel=sp.relative_to(td).as_posix()
        if not rel.startswith(('10 ','11 ','12 ','13 ')): continue
        text=sp.read_text(encoding='utf-8'); title=sp.stem
        if rel.startswith('10 '):
            seq=scalar(split_fm(text)[0],'sequence') or '0'
            pos={'1':'专题入口与边界','2':'历史条件与问题形成','3':'内部谱系展开','4':'机制层解释','5':'传播与地域变体','6':'相邻专题边界','7':'阅读收束'}.get(seq,'核心结构')
        elif rel.startswith('11 '): pos='内部分类与横向展开'
        elif rel.startswith('12 '): pos='横向机制层'
        else: pos='边界、比较与转型'
        text=replace_scalar(text,'history_position',pos)
        if rel.startswith('12 ') or (rel.startswith('10 ') and (scalar(split_fm(text)[0],'sequence')=='4')):
            text=replace_list(text,'mechanism',top_mechs)
        sp.write_text(text,encoding='utf-8')

# Update M-axis status note conservatively.
axis=LIT/'10 轴'/'M轴 文学思潮与美学范式.md'
text=axis.read_text(encoding='utf-8')
text=text.replace('`M_AXIS_STATUS = FROZEN_MATURE`','`M_AXIS_STATUS = FROZEN_MATURE_BASE_SEMANTICS_REPAIRED`')
axis.write_text(text,encoding='utf-8')
print('M-axis Base semantic repair complete')
