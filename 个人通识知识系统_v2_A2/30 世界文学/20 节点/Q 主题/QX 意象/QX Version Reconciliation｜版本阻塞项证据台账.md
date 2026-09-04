---
id: WL-QX-VERSION-RECONCILIATION
type: literature_qx_governance
name: QX Version Reconciliation｜版本阻塞项证据台账
axis: Q
facet: QX
status: ACTIVE
---

# QX Version Reconciliation｜版本阻塞项证据台账

> 目的：对“已读事实明确，但无法安全恢复最小阅读单元”的条目保存版本证据。没有唯一版本映射时，不创建 story-level Work，不用其他版本目录替代个人阅读事实。

## 01｜《人类的群星闪耀时》

中央事实：

```text
read_status = 已读
publisher = unknown
ISBN = unknown
TOC = unknown
```

版本史：

```text
1927 = 5 historical miniatures
1943 = 12 historical miniatures
1997 onward = 14 historical miniatures in common Fischer complete form
```

决策：

```text
STATUS = DEFER_COLLECTION_VERSION
DO_NOT_ASSUME_14 = TRUE
```

原因：个人记录没有出版社、ISBN、页数或目录，无法证明阅读的是5 / 12 / 14篇中的哪一版。

## 02｜《草》｜韩寒

公开书目信息确认：

```text
《草》不是独立小说集
= 从《一座城池》《光荣日》《他的国》《杂的文》抽取片段的精选集
```

决策：

```text
STATUS = DEFER_EXCERPT_COLLECTION
STORY_LEVEL_QX = NOT_APPLICABLE
PARENT_METADATA_UPSTREAM_FIX_NEEDED = TRUE
```

当前中央 `axis_g = G3 小说` 不能作为 QX 拆篇依据；QX 不在本轮擅自修其他轴。

## 03｜《哑舍》

中央事实：

```text
read_status = 已读
record_title = 哑舍
specific_volume = unknown
```

决策：

```text
STATUS = DEFER_SERIES_GRANULARITY
QX_ON_SERIES_PARENT = PROHIBITED
```

## 04｜《俗世奇人》/《俗世奇人（足本）》

上游阅读覆盖曾记录：

```text
俗世奇人（足本）
```

中央 Work 当前规范名：

```text
俗世奇人
```

公开书目显示：

```text
旧版《俗世奇人》
→ 足本：在旧版基础上增加18篇
→ 后续又存在新增本 / 教育推荐版本等再编形态
```

决策：

```text
STATUS = DEFER_COLLECTION_VERSION
REQUIRE = publisher OR ISBN OR verifiable TOC
```

即使标题出现“足本”，也不直接假定某一公开版本的完整目录就是个人所读目录。

## 05｜《机器人短篇全集》｜已解除阻塞

中央记录明确说明个人阅读的是机器人短篇合集，而不是《我，机器人》等分卷。

公开中文书目中同名合集可稳定恢复为32篇：

```text
孩子最好的朋友
莎莉
总有一天
观点
思考！
真爱
AL-76号走失记
无心的胜利
天堂异乡人
光雕
分离主义者
小机
当我们同在一起
镜像
三百年庆事件
第一法则
转圈圈
理性
抓兔子
骗子！
保证满意
列尼
校工
消失无踪
冒险
逃避
证据
可避免的冲突
女性直觉
汝竟顾念他
机器人之梦
正电子人
```

Batch031 已完成：

```text
32 reviewed
22 FORMAL_QX
10 ZERO_QX
24 formal relations
STATUS = CLOSED
```

## 06｜五本编辑型外国短篇选集

当前待治理：

```text
麦琪的礼物：欧·亨利短篇小说经典
莫泊桑短篇小说精选
欧·亨利短篇小说选
契诃夫短篇小说选
项链：莫泊桑中短篇小说选
```

### 《麦琪的礼物：欧·亨利短篇小说经典》

精确标题可锁定至少一条书目：

```text
上海社会科学院出版社
2003
ISBN 7806812296 / 9787806812297
354 pages
```

但尚未获得该版完整 TOC。

```text
STATUS = DEFER_EDITORIAL_COLLECTION
DO_NOT_SUBSTITUTE_LATER_PEOPLE_LITERATURE_TOC = TRUE
```

### 其余四本

公开检索可见多个同名 / 近同名版本与再版体系，单凭中央标题不足以唯一映射具体目录。

```text
STATUS = DEFER_EDITORIAL_COLLECTION
REQUIRE = edition evidence
```

## 07｜治理原则

```text
EXACT_TITLE ≠ EXACT_TOC
SAME_AUTHOR + SAME_COLLECTION_TYPE ≠ SAME_READING_UNIT
LATER_REPRINT_TOC ≠ PERSONAL_READ_TOC
VERSION_AMBIGUITY → DEFER
```

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Corpus Coverage｜特殊项与上游缺口台账]]
- [[QX Formal Annotation｜增量批次031]]
