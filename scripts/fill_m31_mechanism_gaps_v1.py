from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]
WORKS=ROOT/'个人通识知识系统_v2_A2'/'30 世界文学'/'40 作品'
TOPIC='WL-TOPIC-M3-MODERNISM'
DEFAULT={
'19世纪前史':['现代主义前史','主体与现实秩序松动'],
'英国—爱尔兰现代主义':['主体、时间与叙事实验'],
'法国现代主义':['感知、语言与形式实验'],
'德语—奥地利—中欧':['主体危机与都市现代性'],
'俄罗斯与东欧':['革命现代性与形式实验'],
'美国与Harlem Renaissance':['都市现代性与种族经验'],
'伊比利亚与意大利':['形式革新与文化现代性'],
'拉丁美洲与Brazilian Modernismo':['本土现代性与先锋转译'],
'日本与中国现代主义':['非同步现代性与语言重构'],
'南亚、波斯与阿拉伯现代主义':['殖民现代性与语言转型'],
'殖民与跨国现代主义':['殖民现代性与跨国网络'],
}
def split(text):
    if not text.startswith('---\n'):return '',text
    e=text.find('\n---\n',4); return (text[4:e],text[e+5:]) if e>=0 else ('',text)
def scalar(fm,key):
    m=re.search(rf'(?m)^{re.escape(key)}:\s*["\']?(.*?)["\']?\s*$',fm)
    return m.group(1).strip().strip('"\'') if m else ''
def lst(fm,key):
    ls=fm.splitlines();out=[]
    for i,l in enumerate(ls):
        if l.startswith(key+':'):
            tail=l.split(':',1)[1].strip()
            if tail.startswith('[') and tail.endswith(']'):return [x.strip().strip('"\'') for x in tail[1:-1].split(',') if x.strip()]
            j=i+1
            while j<len(ls) and ls[j].startswith('-'):
                out.append(ls[j][1:].strip().strip('"\''));j+=1
            return out
    return out
def replace_list(text,key,vals):
    fm,body=split(text);ls=fm.splitlines();out=[];done=False;i=0
    while i<len(ls):
        if ls[i].startswith(key+':'):
            out.append(key+':');out.extend('- '+v for v in vals);done=True;i+=1
            while i<len(ls) and ls[i].startswith('-'):i+=1
        else:out.append(ls[i]);i+=1
    if not done:
        out.append(key+':');out.extend('- '+v for v in vals)
    return '---\n'+'\n'.join(out)+'\n---\n'+body
def replace_scalar(text,key,val):
    fm,body=split(text);ls=fm.splitlines();out=[];done=False
    for l in ls:
        if l.startswith(key+':'):
            out.append(f'{key}: "{val}"');done=True
        else:out.append(l)
    if not done:out.append(f'{key}: "{val}"')
    return '---\n'+'\n'.join(out)+'\n---\n'+body

filled_t4=0;filled_default=0
for p in WORKS.glob('*.md'):
    text=p.read_text(encoding='utf-8');fm,_=split(text)
    if TOPIC not in lst(fm,'topics') or lst(fm,'modernism_axes'):continue
    bridge=lst(fm,'t4_mechanism')
    if bridge:
        text=replace_list(text,'modernism_axes',bridge)
        text=replace_scalar(text,'modernism_axes_source','t4_mechanism_bridge')
        filled_t4+=1
    else:
        tr=scalar(fm,'modernism_tradition_cluster')
        vals=DEFAULT.get(tr,['现代主义形式与经验重构'])
        text=replace_list(text,'modernism_axes',vals)
        text=replace_scalar(text,'modernism_axes_source','tradition_level_fallback')
        filled_default+=1
    p.write_text(text,encoding='utf-8')
print('filled_from_t4',filled_t4,'filled_from_tradition',filled_default)
