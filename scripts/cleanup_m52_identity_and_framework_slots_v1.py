from __future__ import annotations
import re, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
WORKS=ROOT/'个人通识知识系统_v2_A2'/'30 世界文学'/'40 作品'
TOPIC_ID='WL-TOPIC-M5.2-POWER-IDENTITY-WORLD'; AXIS='M5.2 权力、身份与世界批评'

def fm_parts(text):
    end=text.find('\n---\n',4); return (text[4:end],text[end+5:])
def scalar(fm,key):
    m=re.search(rf'(?m)^{re.escape(key)}:\s*["\']?(.*?)["\']?\s*$',fm); return m.group(1).strip() if m else ''
def list_values(fm,key):
    lines=fm.splitlines(); out=[]
    for i,line in enumerate(lines):
        if line.startswith(key+':'):
            inline=line.split(':',1)[1].strip()
            if inline.startswith('['): return [x.strip().strip('"\'') for x in inline.strip('[]').split(',') if x.strip()]
            j=i+1
            while j<len(lines) and re.match(r'^\s*- ',lines[j]): out.append(lines[j].split('-',1)[1].strip().strip('"\'')); j+=1
            return out
    return out
def set_list(fm,key,vals):
    vals=list(dict.fromkeys(vals)); lines=fm.splitlines(); i=next((i for i,x in enumerate(lines) if x.startswith(key+':')),None); block=[key+':']+[f'- "{v}"' for v in vals]
    if i is None: return fm+'\n'+'\n'.join(block)
    j=i+1
    while j<len(lines) and re.match(r'^\s*- ',lines[j]): j+=1
    lines[i:j]=block; return '\n'.join(lines)
def set_scalar(fm,key,val):
    line=f'{key}: {json.dumps(val,ensure_ascii=False)}'; pat=rf'(?m)^{re.escape(key)}:.*$'
    return re.sub(pat,line,fm,count=1) if re.search(pat,fm) else fm+'\n'+line

def apply_fields(p,priority,framework,role,axes):
    text=p.read_text(encoding='utf-8'); fm,body=fm_parts(text)
    fm=set_list(fm,'topics',list_values(fm,'topics')+[TOPIC_ID])
    fm=set_scalar(fm,'m52_priority',priority); fm=set_scalar(fm,'m52_framework_cluster',framework); fm=set_scalar(fm,'m52_role',role); fm=set_list(fm,'m52_axes',axes)
    p.write_text('---\n'+fm+'\n---\n'+body,encoding='utf-8')

def max_id():
    n=0
    for p in WORKS.glob('*.md'):
        m=re.search(r'WL-WORK-(\d+)',p.read_text(encoding='utf-8',errors='ignore'))
        if m: n=max(n,int(m.group(1)))
    return n

def create_work(wid,title,author,priority,framework,role,axes):
    q=lambda s: json.dumps(s,ensure_ascii=False)
    text=f'''---\nid: "WL-WORK-{wid:04d}"\ntype: "work"\ntitle: {q(title)}\nauthor: {q(author)}\ntopics:\n- "{TOPIC_ID}"\naxis_m:\n- "{AXIS}"\nm52_priority: {q(priority)}\nm52_framework_cluster: {q(framework)}\nm52_role: {q(role)}\nm52_axes:\n'''+''.join(f'- {q(x)}\n' for x in axes)+'''verification_status: "metadata_pending"\nsource_note: "M5.2 V2 structural bibliography gap-fill"\n---\n\n# '''+title+'\n'
    (WORKS/(title+'.md')).write_text(text,encoding='utf-8')

def main():
    # Transliteration-only collisions: merge M5.2 projection into existing canonical entity and delete duplicate.
    merges=[
      ('午夜之子.md','午夜之子（萨尔曼·鲁西迪）.md','★','后殖民','文学',['国家寓言','混杂身份']),
      ('微物之神.md','微物之神（阿兰达蒂·洛伊）.md','★','后殖民','文学',['种姓','后殖民家庭']),
      ('酷儿.md','酷儿（威廉·巴勒斯）.md','◆','酷儿','文学',['同性欲望','边缘生活']),
    ]
    for original,dup,priority,framework,role,axes in merges:
        op,dp=WORKS/original,WORKS/dup
        if op.exists(): apply_fields(op,priority,framework,role,axes)
        if dp.exists(): dp.unlink()

    # Replace three duplicated framework seats with unique structural anchors.
    additions=[
      ('半轮黄日','奇玛曼达·恩戈齐·阿迪契','★','后殖民','文学',['比亚法拉战争','殖民边界']),
      ('典仪','莱斯利·马蒙·西尔科','★','去殖民','文学',['原住民知识','疗愈与土地']),
      ('卡彭塔利亚湾','亚历克西斯·赖特','◆','去殖民','文学',['原住民主权','土地与殖民性']),
    ]
    wid=max_id()
    for title,author,priority,framework,role,axes in additions:
        p=WORKS/(title+'.md')
        if p.exists(): apply_fields(p,priority,framework,role,axes)
        else:
            wid+=1; create_work(wid,title,author,priority,framework,role,axes)
    print('merged=3 additions=3')
if __name__=='__main__': main()
