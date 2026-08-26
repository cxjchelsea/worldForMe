from pathlib import Path
import ast
ROOT=Path(__file__).resolve().parents[1]
S=ROOT/'scripts'
files=[
'apply_m1_v2_structure_and_bibliography_v1.py',
'apply_m2_v2_structure_and_map_existing_v1.py',
'apply_m2_bibliography_gap_fill_v1.py',
'apply_m31_bibliography_cleanup_v1.py',
'apply_m4_v2_structure_and_bibliography_v1.py',
'apply_m51_v2_structure_and_bibliography_v1.py',
'apply_m52_v2_structure_and_bibliography_v1.py',
]
for fn in files:
    p=S/fn
    print('\n##',fn)
    tree=ast.parse(p.read_text(encoding='utf-8'))
    for node in tree.body:
        if isinstance(node,(ast.Assign,ast.AnnAssign)):
            targets=node.targets if isinstance(node,ast.Assign) else [node.target]
            val=node.value
            try: obj=ast.literal_eval(val)
            except Exception: continue
            names=[t.id for t in targets if isinstance(t,ast.Name)]
            if not names: continue
            if isinstance(obj,(list,tuple,dict,set)):
                print(names[0],type(obj).__name__,len(obj))
                if isinstance(obj,list) and obj:
                    print(' sample=',repr(obj[:2]))
