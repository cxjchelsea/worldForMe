from pathlib import Path
import json

ROOT=Path('个人通识知识系统_v2_A2/30 世界文学')
TOP=ROOT/'30 专题'/'R3 南亚文学'
NODE=ROOT/'20 节点'/'R 地域'/'R3 南亚文学.md'

CORE={
'01 定义与边界.md':'''---\nid: WL-TOPIC-R3-DEFINITION\ntype: literature_topic_section\ntopic_id: WL-TOPIC-R3-SOUTH-ASIA\ndimension: definition\nsequence: 1\n---\n# 01｜定义与边界\n\nR3 以南亚的长期语言—宗教—书写—制度网络为对象，而不是把现代国家直接当作文学生成单位。\n\n核心空间包括印度、巴基斯坦、孟加拉国、尼泊尔、斯里兰卡及与这些传统紧密相连的跨境文学共同体。内部分析以文学语言和历史共同体为主：梵语、巴利/普拉克里特、泰米尔及南印度语言、印地及北印度俗语、乌尔都、孟加拉、旁遮普/信德、僧伽罗、尼泊尔语与英语。\n\n边界原则：\n- 波斯语南亚文学与 R1 波斯语文化圈建立关系，但主坐标按作品主要文学场判断。\n- 佛教文本的南亚形成属于 R3；向东南亚、东亚的传播建立 R8/R2 关系。\n- 南亚离散英语文学可同时连接 R10。\n- 宗教、哲学文本仅在其诗学、叙事、语言史或文学经典化意义明确时进入作品层。\n''',
'02 历史层与连续性.md':'''---\nid: WL-TOPIC-R3-HISTORY\ntype: literature_topic_section\ntopic_id: WL-TOPIC-R3-SOUTH-ASIA\ndimension: history\nsequence: 2\n---\n# 02｜历史层与连续性\n\nR3 的连续性不是一条单线文学史，而是多个文学中心不断叠加：\n\n1. 吠陀口传、梵语经典与史诗形成早期高文化层。\n2. 巴利、普拉克里特、泰米尔等语言形成并行经典世界，佛教与耆那传统扩大文本网络。\n3. 古典梵语戏剧、诗歌、叙事和诗学与地方宫廷文学长期共存。\n4. 中古时期地方语言文学扩张；Bhakti、苏菲和区域宫廷推动俗语诗歌与叙事。\n5. 德里苏丹国和莫卧儿时期形成强大的波斯语—Hindavi—乌尔都文学场。\n6. 殖民印刷、英语教育、报刊和翻译改变作者、读者、文类与公共领域。\n7. 民族主义、分治、独立和语言政治重组现代南亚文学。\n8. 当代文学同时存在区域语言、英语写作、迁徙与全球出版网络。\n''',
'03 语言文字与媒介.md':'''---\nid: WL-TOPIC-R3-LANGUAGE\ntype: literature_topic_section\ntopic_id: WL-TOPIC-R3-SOUTH-ASIA\ndimension: language_media\nsequence: 3\n---\n# 03｜语言文字与媒介\n\n南亚文学的关键不是寻找一种“共同语言”，而是理解多语制度。\n\n- 梵语长期承担经典、宫廷、学术和跨区域高文化功能。\n- 巴利与多种普拉克里特承载佛教、耆那及戏剧中的差异化语言层。\n- 泰米尔拥有独立而早期的古典文学传统，并与梵语世界长期互动。\n- 中古以后印地诸俗语、孟加拉、马拉地、古吉拉特、旁遮普、泰卢固、卡纳达、马拉雅拉姆等形成强大的地方文学。\n- 波斯语和乌尔都连接宫廷、城市、苏菲与近代公共文化。\n- 殖民时期印刷和英语教育制造新的标准化、翻译与双语写作条件。\n\n媒介链条包括口传、吟诵、手稿、棕榈叶、宫廷抄写、宗教表演、印刷、报刊和现代出版。\n''',
'04 文学制度与传播.md':'''---\nid: WL-TOPIC-R3-INSTITUTION\ntype: literature_topic_section\ntopic_id: WL-TOPIC-R3-SOUTH-ASIA\ndimension: institution\nsequence: 4\n---\n# 04｜文学制度与传播\n\nR3 的文本由多种制度共同生产和保存：\n\n- 吠陀吟诵和师徒传承；\n- 寺院、僧团与佛教/耆那手稿文化；\n- 王朝宫廷与诗人赞助；\n- 寺庙、朝圣、Bhakti 与苏菲圣徒网络；\n- 莫卧儿及区域宫廷的波斯语书写和翻译机构；\n- 城市 mushaira、讲唱、戏剧和民间表演；\n- 殖民学校、大学、出版社、报刊和文学社团；\n- 独立后的国家语言政策、文学奖、电影、翻译和全球英语出版。\n\n制度变化解释了为什么同一故事可以在多个语言和宗教共同体中持续改写。\n''',
'05 阅读路线.md':'''---\nid: WL-TOPIC-R3-READING\ntype: literature_topic_section\ntopic_id: WL-TOPIC-R3-SOUTH-ASIA\ndimension: reading_route\nsequence: 5\n---\n# 05｜阅读路线\n\n推荐按“共享骨架 → 地方化 → 波斯化/宗教互动 → 殖民现代 → 分治与全球化”阅读。\n\n1. 《梨俱吠陀》、两大史诗和古典梵语作品建立早期骨架。\n2. 同时进入巴利/普拉克里特和桑伽姆泰米尔，避免把梵语当作整个南亚。\n3. 读 Bhakti、苏菲、乌尔都和孟加拉作品，观察地方语言与跨宗教网络。\n4. 进入泰戈尔、普列姆昌德等殖民现代文学。\n5. 以分治文学、区域现代主义和南亚英语文学进入当代。\n\n完整作品按 [[../03 R3文学作品.base|R3 作品数据库]] 动态查看。\n'''
}

TRADS={
'01 梵语—吠陀与古典文学传统.md':('WL-TOPIC-R3-TRAD-SANSKRIT','梵语—吠陀与古典文学传统','吠陀赞歌、奥义书、两大史诗、古典戏剧与 kavya、寓言/故事集以及诗学构成这一传统的主骨架。它不是“古印度全部文学”，而是一种长期跨区域的经典与高文化语言体系。','《梨俱吠陀》《摩诃婆罗多》《罗摩衍那》《沙恭达罗》《云使》《五卷书》《故事海》等。'),
'02 巴利—普拉克里特与佛教耆那文学传统.md':('WL-TOPIC-R3-TRAD-PALI-PRAKRIT','巴利—普拉克里特与佛教／耆那文学传统','巴利和多种普拉克里特说明南亚古典文学从来不是梵语单中心。佛教经典、譬喻、本生故事、僧尼诗歌和耆那叙事形成跨地区文本网络。','《法句经》《本生经》《长老偈》《长老尼偈》以及耆那叙事传统。'),
'03 泰米尔与南印度文学传统.md':('WL-TOPIC-R3-TRAD-DRAVIDIAN','泰米尔与南印度文学传统','以桑伽姆诗歌和泰米尔史诗为早期核心，并向泰卢固、卡纳达、马拉雅拉姆等南印度文学扩展。这里既有独立古典传统，也有梵语化、Bhakti 和现代区域文学的长期互动。','《古鲁恩托盖》《普拉南努鲁》《西拉巴提伽拉姆》、安达尔诗歌及现代泰米尔/马拉雅拉姆等作品。'),
'04 北印度俗语—Bhakti与印地文学传统.md':('WL-TOPIC-R3-TRAD-HINDI-BHAKTI','北印度俗语—Bhakti 与印地文学传统','阿瓦迪、布拉杰及其他北印度俗语诗歌在 Bhakti 中形成巨大文学能量，随后标准印地语在殖民现代重组小说、诗歌与公共领域。','卡比尔、苏尔达斯、杜勒西达斯、普列姆昌德以及现代印地文学。'),
'05 波斯语—Hindavi—乌尔都文学传统.md':('WL-TOPIC-R3-TRAD-URDU-PERSIANATE','波斯语—Hindavi—乌尔都文学传统','南亚波斯语宫廷、苏菲网络和城市 Hindavi/乌尔都共同塑造这一传统。ghazal、masnavi、marsiya、dastan、短篇和现代小说在德里、勒克瑙、拉合尔等文学场持续变化。','阿米尔·霍斯陆、米尔、加利卜、伊克巴尔、曼托、伊斯玛特·丘格泰、Qurratulain Hyder 等。'),
'06 孟加拉与东部语言文学传统.md':('WL-TOPIC-R3-TRAD-BENGAL-EAST','孟加拉与东部语言文学传统','孟加拉文学连接佛教早期俗语诗、Vaishnava/Bhakti、殖民现代性、民族主义和孟加拉国文学；阿萨姆、奥里亚等东部语言传统作为条件扩展网络。','《吉祥歌》传统、班金、泰戈尔、萨拉特·钱德拉、纳兹鲁尔、吉本南达·达斯等。'),
'07 旁遮普—信德与西北文学传统.md':('WL-TOPIC-R3-TRAD-NORTHWEST','旁遮普—信德与西北文学传统','西北文学由苏菲诗、锡克经典、qissa 爱情叙事、旁遮普/信德口传与现代分治经验共同塑造，语言跨越今日印度与巴基斯坦国界。','《古鲁·格兰特·萨希卜》中的诗歌传统、Bulleh Shah、Waris Shah《希尔·兰贾》及现代旁遮普/信德作品。'),
'08 僧伽罗—斯里兰卡文学传统.md':('WL-TOPIC-R3-TRAD-SRI-LANKA','僧伽罗—斯里兰卡文学传统','斯里兰卡文学连接巴利佛教编年史、僧伽罗古典诗文、殖民语言接触、僧伽罗/泰米尔双语国家与内战经验。不能只按印度文学附属处理。','《大史》、古典僧伽罗诗文，以及 Martin Wickramasinghe、Michael Ondaatje 等现代/英语写作。'),
'09 尼泊尔—喜马拉雅文学传统.md':('WL-TOPIC-R3-TRAD-NEPAL-HIMALAYA','尼泊尔—喜马拉雅文学传统','尼泊尔语、尼瓦尔语及喜马拉雅多语文化形成南亚北缘文学空间。梵语经典、本地口传、宫廷书写和现代民族文学在此叠加。','Bhanubhakta Acharya 的尼泊尔语《罗摩衍那》改写、Laxmi Prasad Devkota 等。'),
'10 南亚英语文学传统.md':('WL-TOPIC-R3-TRAD-ANGLOPHONE','南亚英语文学传统','英语写作从殖民教育语境进入小说、诗歌和散文，独立后又成为连接印度、巴基斯坦、斯里兰卡、孟加拉及离散作家的跨区域媒介。它不取代区域语言传统。','R.K. Narayan、Mulk Raj Anand、Salman Rushdie、Amitav Ghosh、Arundhati Roy 等。')
}

NETWORKS={
'01 史诗—往世书与地方化改写网络.md':('WL-TOPIC-R3-NET-EPIC','史诗—往世书与地方化改写网络','《罗摩衍那》《摩诃婆罗多》以及往世书故事通过梵语、地方语言、口头表演、戏剧和宗教仪式不断重写。关键不是寻找唯一“正版”，而是观察地方化版本如何形成新的文学共同体。'),
'02 佛教—耆那文本与翻译传播网络.md':('WL-TOPIC-R3-NET-BUDDHIST-JAIN','佛教—耆那文本与翻译传播网络','僧团、寺院、朝圣和手稿文化把巴利、普拉克里特、梵语佛教及耆那文本连接到斯里兰卡、中亚、东南亚和东亚。R3 关注其南亚文本生成和语言层。'),
'03 波斯化—苏菲—Bhakti互动网络.md':('WL-TOPIC-R3-NET-PERSIANATE','波斯化—苏菲—Bhakti互动网络','波斯语宫廷、苏菲 khanqah、Hindavi/乌尔都和 Bhakti 俗语诗形成长期接触。不能把这种互动简化成单向“伊斯兰影响”或完全融合；应按具体文本、赞助、翻译和语言实践判断。'),
'04 殖民印刷—英语教育与现代文类网络.md':('WL-TOPIC-R3-NET-COLONIAL-PRINT','殖民印刷—英语教育与现代文类网络','十九世纪以后印刷、报刊、学校、大学、传教出版、翻译与审查重组南亚公共领域。小说、现代诗、短篇、戏剧和文学批评在各语言中以不同速度形成。'),
'05 分治—迁徙与离散文学网络.md':('WL-TOPIC-R3-NET-PARTITION','分治—迁徙与离散文学网络','1947 年分治及其后的战争、边界、语言政治和全球迁徙制造跨印地/乌尔都/旁遮普/孟加拉/英语的记忆网络。这里与 R10 离散文学建立强连接。')
}

CANVAS={
  'nodes':[
    {'id':'home','type':'file','file':'00 南亚文学.md','x':0,'y':0,'width':360,'height':180},
    {'id':'core','type':'group','label':'10 核心结构','x':-620,'y':-300,'width':420,'height':620},
    {'id':'trad','type':'group','label':'11 内部传统','x':-100,'y':300,'width':760,'height':760},
    {'id':'net','type':'group','label':'12 跨传统网络','x':500,'y':-320,'width':480,'height':620},
  ],
  'edges':[
    {'id':'e1','fromNode':'home','toNode':'core'},
    {'id':'e2','fromNode':'home','toNode':'trad'},
    {'id':'e3','fromNode':'home','toNode':'net'}
  ]
}

def write_node(path,id_,name,body,works,seq,dimension='internal_tradition'):
    txt=f'''---\nid: {id_}\ntype: literature_topic_section\ntopic_id: WL-TOPIC-R3-SOUTH-ASIA\ndimension: {dimension}\nsequence: {seq}\n---\n# {name}\n\n{body}\n\n## 作品锚点\n\n{works}\n'''
    path.parent.mkdir(parents=True,exist_ok=True); path.write_text(txt,encoding='utf-8')

def main():
    (TOP/'10 核心结构').mkdir(parents=True,exist_ok=True)
    (TOP/'11 内部传统').mkdir(parents=True,exist_ok=True)
    (TOP/'12 跨传统网络').mkdir(parents=True,exist_ok=True)
    for fn,txt in CORE.items(): (TOP/'10 核心结构'/fn).write_text(txt,encoding='utf-8')
    for i,(fn,(id_,name,body,works)) in enumerate(TRADS.items(),1): write_node(TOP/'11 内部传统'/fn,id_,name,body,works,i)
    for i,(fn,(id_,name,body)) in enumerate(NETWORKS.items(),1): write_node(TOP/'12 跨传统网络'/fn,id_,name,body,'本节点以跨语言传播、改写和制度关系为主要证据，不维护独立静态书单。',i,'literary_network')
    (TOP/'01 南亚文学.canvas').write_text(json.dumps(CANVAS,ensure_ascii=False,separators=(',',':')),encoding='utf-8')
    text=NODE.read_text(encoding='utf-8-sig')
    text=text.replace('topic_map: null','topic_map: "[[../../30 专题/R3 南亚文学/00 南亚文学|R3 南亚文学]]"')
    text=text.replace('> 暂未接入。','- [[../../30 专题/R3 南亚文学/00 南亚文学|R3 南亚文学]]\n- [[../../30 专题/R3 南亚文学/01 南亚文学.canvas|R3 Canvas]]\n- [[../../30 专题/R3 南亚文学/03 R3文学作品.base|R3 作品数据库]]')
    NODE.write_text(text,encoding='utf-8')
    print('R3_TOPIC_MAP_STRUCTURE=BUILT')

if __name__=='__main__': main()
