# 低信噪比 SED · 技术时间线（2025–2026）

| 时间 | 代表工作 | 解决的问题 | 证据 |
|---|---|---|---|
| 2025 | [Exploring Text-Queried SED with Audio Source Separation](https://doi.org/10.1109/ICASSP49660.2025.10889789) | 文字指定目标，先分离再检测 | ICASSP / [代码](https://github.com/apple-yinhan/TQ-SED) |
| 2025 | [Leveraging LLM and Text-Queried Separation for Noise-Robust SED](https://doi.org/10.1109/ICASSPW65056.2025.11011161) | 噪声条件识别与目标分离 | ICASSPW / [代码](https://github.com/apple-yinhan/Noise-robust-SED)；预印本可能早于 2025 |
| 2025-08 | [Noise-Robust SED and Counting via Language-Queried Separation](https://arxiv.org/abs/2508.07176) | EAD 计数辅助 SED 与分离 | arXiv / [代码](https://github.com/visionchan/EADSED) |
| 2025-08 | [Infant Cry Detection in Noisy Environment](https://arxiv.org/abs/2508.19308) | 嘈杂环境中的轻量哭声检测 | arXiv；仓库既有论文 |
| 2026 | [DAAPNet](https://doi.org/10.1109/TASLPRO.2026.3651989) | 重叠声源的动态时频注意力 | IEEE |
| 2026-04 | [Duration-Adaptive Time-Frequency Perception](https://doi.org/10.1109/TASLPRO.2026.3678192) | 弱事件、变持续时间与频带对齐 | IEEE；明确含 −10～−5 dB 对比 |
| 2026-06 | [Deep Reservoir Networks for Audio Surveillance](https://arxiv.org/abs/2606.22218) | 多 SNR 紧急声音事件检测与边缘效率 | arXiv；仓库既有论文 |
| 2026-06 | [Soroll-IA](https://arxiv.org/abs/2606.26195) | 强背景噪声、远距离和重叠事件的工业港口数据 | arXiv；数据集支撑工作 |
| 2026 | [Noise-Robust Environmental Sound Understanding with Text Anchors](https://dcase.community/workshop2026/proceedings) | 极低 SNR 的目标/噪声语义锚点与可靠性 | DCASE 2026 |
| 2026 | [Noise-aware SSL for ASD](https://dcase.community/workshop2026/proceedings) | 工业噪声参考辅助表征 | **相邻 ASD 工作，非直接 SED** |
| 2026-10 | [From Signals to Evidence - Part II](https://arxiv.org/abs/2610.31346) | 低 SNR 水下目标的物理证据与可解释检测 | arXiv；仓库水下目标专题 |
| 2026-10 | [Dolphin broadband transient vocalization detection](https://arxiv.org/abs/2610.35641) | 脉冲环境噪声中的瞬态叫声检测 | arXiv；仓库海洋生物声音专题 |

## 趋势轴标题
**2025：目标分离辅助检测 → 2026：事件结构与动态时频联合建模 → 噪声感知及置信可靠性成为重要研究分支。**

说明：时间顺序是公开发表顺序近似，会议与预印本应分开；同一论文多个版本只统计一次。
