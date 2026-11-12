# 低信噪比声音事件检测 | Low-SNR / Noise-Robust SED

> 更新：2026-11-13。2025–2026 年代表性文献专题，**不是全量系统性文献检索**。研究对象为低信噪比（SNR）、强背景噪声、重叠声源及弱事件的检测和时间定位。SED 与 ASD / SELD / ESC 结果分开标注。

[声音事件检测总览](../README.md) · [专题导航](../TOPICS.md) · [技术趋势与证据](TRENDS.md) · [论文时间线](TIMELINE.md) · [复现实验建议](EXPERIMENTS.md)

## 一句话趋势

**从统一噪声增强与盲目降噪，发展到目标条件分离、动态时频感知、噪声感知表征及事件级多任务约束；可靠性验证必须包含目标缺失负例和真实场景外测试。**

## 直接相关论文（2025–2026）

| 年份 | 论文 | 核心思路 | 已核验来源 | 证据边界 |
|---|---|---|---|---|
| 2025 | Noise-Robust Sound Event Detection and Counting via Language-Queried Sound Separation | 语言查询分离，EAD 事件计数与 SED 协同 | [arXiv:2508.07176](https://arxiv.org/abs/2508.07176) · [DOI](https://doi.org/10.1109/LSP.2025.3614476) · [代码](https://github.com/visionchan/EADSED) | DESED/WildDESED 噪声条件有相对优势；具体分档数值待全文复核 |
| 2025 | Exploring Text-Queried Sound Event Detection with Audio Source Separation | 文本查询目标分离 + SED | [DOI](https://doi.org/10.1109/ICASSP49660.2025.10889789) · [代码](https://github.com/apple-yinhan/TQ-SED) | 论文报告 F1 改善；具体 SNR 分档与口径待全文复核 |
| 2025 | Leveraging LLM and Text-Queried Separation for Noise-Robust Sound Event Detection | LLM 辅助噪声建模 + 文本查询分离 | [DOI](https://doi.org/10.1109/ICASSPW65056.2025.11011161) · [代码](https://github.com/apple-yinhan/Noise-robust-SED) | 2024 年预印本、2025 年会议；不重复计为两个工作 |
| 2026 | Duration-Adaptive Time-Frequency Perception Network for Overlapping Sound Event Detection | 动态时间/频率卷积，频带对齐，持续时间自适应 | [IEEE / DOI](https://doi.org/10.1109/TASLPRO.2026.3678192) | −10 至 −5 dB 下，论文摘要报告 PSDS 相对 Conformer/CRNN 增益 9.4%/13.02%；非本仓库复现 |
| 2026 | Dynamic Attention-Asymmetric Perceptron Network for Overlapping Sound Event Detection | 非对称时频感知 + 动态注意力 | [DOI](https://doi.org/10.1109/TASLPRO.2026.3651989) | 低 SNR 完整分档需核对原文 |
| 2026 | Noise-Robust Environmental Sound Understanding Using an Audio Foundation Model with Text Anchors | 文本锚点、目标/噪声对齐、分离和 SNR 估计 | [DCASE 2026 官方论文集](https://dcase.community/workshop2026/proceedings) | −20 dB 警笛召回 51.2%、特异度 96.4%；ESC 分类结果不可与 SED 混排 |
| 2026 | Gate-Align-SED: Semi-Supervised Sound Event Detection via Adaptive Feature Gating and Cross-Task Alignment in Situation Awareness | 门控、跨任务对齐与半监督训练 | [DOI](https://doi.org/10.1002/aisy.70355) | 强噪声相关，尚未核实特定负 SNR 档位收益 |

## 仓库内已归入本专题的论文

以下条目均已存在于仓库，并依据摘要中的低 SNR、强背景噪声或噪声条件实验交叉归入本专题；原有婴儿哭声、SELD、工业港口、水下目标等应用分类保持不变。

| 日期 | 论文 | 任务与归入依据 | 原有方向 |
|---|---|---|---|
| 2025-03-08 | [Infant Cry Detection Using Causal Temporal Representation](https://arxiv.org/abs/2503.06247) | 其他声音和背景噪声下的婴儿哭声分割与检测 | 人类声音 / 婴儿哭声 |
| 2025-08-06 | [Binaural Sound Event Localization and Detection Neural Network based on HRTF Localization Cues for Humanoid Robots](https://arxiv.org/abs/2508.04333) | 城市背景噪声下双耳声音事件检测与定位 | SELD / 通用方法 |
| 2025-08-10 | [Noise-Robust Sound Event Detection and Counting via Language-Queried Sound Separation](https://arxiv.org/abs/2508.07176) | 噪声越强优势越明显的语言查询分离、事件计数和 SED 联合方法 | 通用 SED 方法 |
| 2025-08-26 | [Infant Cry Detection In Noisy Environment Using Blueprint Separable Convolutions and Time-Frequency Recurrent Neural Network](https://arxiv.org/abs/2508.19308) | 面向嘈杂环境的轻量婴儿哭声事件检测 | 人类声音 / 婴儿哭声 |
| 2026-06-20 | [An Analysis of Untrained Deep Reservoir Networks for Audio Surveillance](https://arxiv.org/abs/2606.22218) | 多 SNR 条件下的紧急声音事件检测；深层储备池在强噪声下更稳健 | 安防 / 紧急事件 |
| 2026-06-24 | [Soroll-IA: A Weakly Labeled Audio Dataset for Real-World Industrial Port Monitoring](https://arxiv.org/abs/2606.26195) | 强背景噪声、远距离声源与事件重叠条件下的弱监督 SED 数据集 | 工业声音 / 港口监测 |
| 2026-10-22 | [From Signals to Evidence: Interpretable Underwater Acoustic Target Sensing with Large Language Models - Part II: Passive Detection](https://arxiv.org/abs/2610.31346) | 低 SNR 水下被动目标检测，融合 MVDR、多通道证据与 LLM 推理 | 水下目标检测 |
| 2026-10-26 | [Dolphin broadband transient vocalization detection in impulsive ambient noise](https://arxiv.org/abs/2610.35641) | 脉冲环境噪声中的海豚宽带瞬态叫声检测 | 海洋生物声音 |

共 **8 篇仓库论文**归入本横向专题，其中 6 篇为直接检测/定位方法，1 篇为真实强噪声数据集，1 篇为低 SNR 水下被动目标检测。

## 邻接领域的技术迁移证据（不能算作直接 SED）

- **2026 DCASE Task 2：Noise-aware SSL / NA-BEATs（ASD）**：利用近场与远场噪声参考改善工业异常声音表征；[官方论文集](https://dcase.community/workshop2026/proceedings)。ASD 挑战分数不等同 SED PSDS。
- **2026 DCASE：When Speech is Noise（ASD）**：面向人声干扰的抑制与检测误报；[官方论文集](https://dcase.community/workshop2026/proceedings)。
- **2025 SELD：Sound Source Localization Using Hybrid CRNNs in Undesirable Conditions**：低 SNR + 混响下定位；[DOI](https://doi.org/10.3390/electronics14142778)。
- **2026：Drowning in Noise: On Signal Saliency in Self-Supervised Learning for Ocean Acoustics**：噪声占优条件下的预训练数据选择；[arXiv:2611.06725](https://arxiv.org/abs/2611.06725)。属表征学习证据而非 SED 直接验证。

## 核心困难

1. **目标掩蔽**：整体音频能量很高，但目标发生区间/频带的局部 SNR 低。
2. **分离幻觉**：目标不存在时，条件分离模型可能生成目标样结构，引入误报警。
3. **重叠事件与持续时间尺度不同**：同一固定感受野难兼顾短冲击和长时周期事件。
4. **合成与真实噪声不一致**：合成噪声改善不能自动推出跨设备/跨项目现场改善。
5. **阈值迁移与校准**：相同检测分数在不同噪声底下的误报率可能不同。

## 与 DAS 工业声学的关系

优先研究 **Noise-aware 表征（同主干公平消融）→ 目标存在性辅助约束 → 动态时频建模 → 有条件触发的目标分离复核**。DAS 相邻探测器不一定为纯噪声参考；耦合、传播延迟和目标泄漏需评估。目标与非目标在相同频带的干扰，可能比普通宽带加性噪声更具挑战。

## 维护规则

- 新论文须记录：论文 ID / DOI、发表和预印本年份、SED/ASD/SELD/ESC 任务类型、数据集、噪声构造方法、SNR 分档、指标、测试集隔离、代码与 PDF 链接、核验状态。
- 结果只使用来源中明确给出的数字。不同数据集、指标与 SNR 定义不可直接横向排序。
- 论文可同时归入具体声源事件专题与本横向技术专题，引用而非复制同一主库条目。
- 新增论文后同步更新 [技术趋势](TRENDS.md) 与 [时间线](TIMELINE.md)；保持未复现 / 已复现 / 已现场验证状态分离。
