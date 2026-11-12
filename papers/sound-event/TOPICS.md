# 声音事件检测 · 按事件对象的三级分类导航

**组织原则：应用领域 → 具体声音事件 → 检测/分类/定位等任务标签。** 采用非破坏性重组：不移动/删除现有论文、DAS/ASD/Leakage 页面及其历史链接，原有研究趋势页继续有效。

## 横向方法专题（不属于具体声源事件计数）\n\n- **[低信噪比声音事件检测 / Low-SNR SED](low-snr/README.md)**：强背景噪声、弱目标、重叠事件、目标条件分离、Noise-aware 表征及可靠性评估；附 [趋势](low-snr/TRENDS.md)、[时间线](low-snr/TIMELINE.md) 和 [实验建议](low-snr/EXPERIMENTS.md)。\n\n## 12 个应用领域（40 个事件子专题）

| 应用领域 | 事件专题数 | 去重候选数 |
|---|---:|---:|
| [安防与危险事件](security/README.md) | 4 | 12 |
| [人类非语言声音](human/README.md) | 5 | 1 |
| [动物声音](animal/README.md) | 4 | 45 |
| [工业机械声音](industrial/README.md) | 4 | 75 |
| [交通与运输](transportation/README.md) | 4 | 14 |
| [自然环境声](environmental/README.md) | 3 | 1 |
| [医疗与生理声](medical/README.md) | 3 | 20 |
| [城市公共场所](urban/README.md) | 3 | 1 |
| [家居与生活](domestic/README.md) | 3 | 0 |
| [农业与生态](agriculture/README.md) | 2 | 85 |
| [水下与海洋](underwater/README.md) | 2 | 11 |
| [基础设施](infrastructure/README.md) | 3 | 10 |

- **[新专题：炸街车检测 / 改装排气声](transportation/noisy-vehicle/README.md)**：已人工核查直接论文及车辆声学支撑工作，附[技术趋势](transportation/noisy-vehicle/TRENDS.md)、[时间线](transportation/noisy-vehicle/papers-timeline.html)、[数据/代码](transportation/noisy-vehicle/RESOURCES.md)。独立专题不改变原有 40 个自动分类子专题及候选统计。
- [通用 SED 方法论文与无法可靠按声源细分的候选（306 条）](methods/README.md)
- [机器可读分类定义](taxonomy.json)
- [主库论文—专题关联关系](topic-paper-map.json)
- [原综合 SED README：技术时间线及趋势](README.md)

## 如何理解论文数量

输入为现有主库 2,145 条**标题级候选**，优先按 arXiv ID、否则规范化标题去重，得到 2061 条临时候选。按标题关键词进行跨类别专题关联，实际命中至少一个事件子类的去重记录为 261 条。原始 `sound-event` 分类中无明确声源命中的 306 条进入通用方法页。这里的数量是**可检索候选，不是通过全文核查的真实唯一论文数**。

## 技术任务是横向标签，不与事件类型同级

`detection`、`classification`、`localization`、`segmentation`、`source-separation`、`few-shot`、`open-set`、`domain-generalization`、`noise-robustness`、`severity`。

## 去重、审核与维护约束

- 一篇论文可有多个事件标签；主库 ID 作为旧记录引用，不复制私人 Drive 地址或 PDF。
- 对象关键词来自标题；需在后续摘要/全文审核时排除误命中与补齐漏掉的论文。
- 不能将论文提出的方法在生物声学、医疗声学等领域的效果宣称为 DAS 工业场景的实测结论。
- 原技术时间线与趋势页沿用，新增事件专题的趋势应有真实论文依据后再更新。
