# 炸街车检测：历史相关 arXiv 论文与直接专项研究

> 更新：2026-11-13。本文补充已有专题此前未完整收录的历史文献。**论文相关性 ≠ 该论文直接研究非法改装排气**。年份为 arXiv 首发年份（期刊另标）；arXiv 分类以论文官方页面为准。2025-11—2026-11 cs.SD 的近期筛选见 [单独清单](arxiv-cs-sd-2025-11-to-2026-11.md)。

## A. 直接研究改装排气（非已确认 arXiv 版本）

| 年份 | 研究 | 方法与原文结果 | 证据 |
|---|---|---|---|
| 2023 | **Cheng 等，Spectrogram-based classification on vehicles with modified loud exhausts via convolutional neural networks** | 经过声 STFT 谱图 → AlexNet 区分普通/改装排气的目标乘用车；YOLOv4-Tiny 辅助车型识别；论文报告总体准确率 **96%**（其研究数据及测试条件下），包含现场验证；文中介绍 4 类共 912 条音频 | [期刊 DOI](https://doi.org/10.1016/j.apacoust.2023.109254) · [出版社摘要](https://www.sciencedirect.com/science/article/pii/S0003682X2300052X) |
| 2025 预印本 / 2026 期刊 | **Wang 等，Sound event detection for modified-exhaust vehicles in urban environment** | Scaper 合成声景、SEDT / 多骨干网络对比，现场 Event-F1 0.6629；参见专题主文献页，**不重复计数** | [DOI](https://doi.org/10.1016/j.trd.2026.105241) |

## B. arXiv：空气声车辆检测、数据与干扰分类（方法支撑）

| arXiv（首发） | 官方题目 | 官方分类 | 内容、对炸街车研究的用途及边界 | 链接 |
|---|---|---|---|---|
| **2302.02945 (2023-02)** | Improved Vehicle Sub-type Classification for Acoustic Traffic Monitoring | **cs.SD; eess.AS** | MFCC、GFCC、Mel 特征 + CNN，在 IDMT Traffic 上对汽车、卡车、摩托车/自行车类以及无车共四类分类，论文报告使用 MFCC 达 **98.95%**；适合车辆声源前置分类，**未检测排气改装**。 | [arXiv](https://arxiv.org/abs/2302.02945) · [PDF](https://arxiv.org/pdf/2302.02945) |
| **2309.03544 (2023-09)** | MVD:A Novel Methodology and Dataset for Acoustic Vehicle Type Classification | **cs.SD; cs.LG; eess.AS** | MVD/MVDA 两套开放车辆声音数据集、四类车辆/背景，多输入声学特征分类；作者报告 **91.98% / 96.66%**（分别对应 MVD/MVDA）；适合作为真实交通负例及车型基线，**无改装排气标注声明**。 | [arXiv](https://arxiv.org/abs/2309.03544) · [PDF](https://arxiv.org/pdf/2309.03544) |
| **2401.09308 (2024-01)** | Can Synthetic Data Boost the Training of Deep Acoustic Vehicle Counting Networks? | **eess.AS; cs.SD** | 车辆经过声模拟及真实/合成数据混训，研究双车道车辆计数和方向；作者报告汽车计数准确率 **63%→88%**（论文工况）；可借鉴稀缺事件合成，**不等于改装排气检测提升**。 | [arXiv](https://arxiv.org/abs/2401.09308) · [PDF](https://arxiv.org/pdf/2401.09308) |
| **2305.14579 (2023-05)** | Real-Time Idling Vehicles Detection using Combined Audio-Visual Deep Learning | **cs.CV（不属于 cs.SD）** | 音视频融合检测车辆运动/静止发动机开关，对比学习发动机声音表征；适合视音频目标归属和发动机状态负例，**不判定排气改装**。 | [arXiv](https://arxiv.org/abs/2305.14579) · [PDF](https://arxiv.org/pdf/2305.14579) |
| **2401.00154 (2023-12 首发、2024 修订)** | AClassiHonk: A System Framework to Annotate and Classify Vehicular Honk from Road Traffic | **cs.SI（不属于 cs.SD）** | 车辆鸣笛标注与分类，自动编码器辅助标注和迁移学习分类；适合作为高声级**非目标事件**抑制，**不是改装排气论文**。 | [arXiv](https://arxiv.org/abs/2401.00154) · [PDF](https://arxiv.org/pdf/2401.00154) |

## C. arXiv：DAS 道路车流监测（跨模态参考；非空气声）

| arXiv | 官方题目 | 分类 | 内容及使用边界 | 链接 |
|---|---|---|---|---|
| **2409.10259 (2024-09)** | Self-Updating Vehicle Monitoring Framework Employing Distributed Acoustic Sensing towards Real-World Settings | **physics.geo-ph; cs.CV; cs.LG; eess.SP（非 cs.SD）** | DAS 地面振动的车辆轨迹检测，少标注半监督、自更新和轨迹形状先验损失；适合时空一致性/跨期自适应，**不能当作麦克风改装排气识别结果**。 | [arXiv](https://arxiv.org/abs/2409.10259) · [PDF](https://arxiv.org/pdf/2409.10259) |
| **2609.28793 (2026-09)** | Monitoring Urban Traffic Dynamics at Fine Spatiotemporal Resolution Using Distributed Acoustic Sensing and Deep Learning | **cs.LG（未确认 cs.SD）** | 道路 DAS 地震振动转换为时空图像、车辆轨迹检测与流量/速度聚合；合成+人工标注训练，**非炸街车专项、非空气声、不得列入近一年 cs.SD 命中清单**。 | [arXiv](https://arxiv.org/abs/2609.28793) · [PDF](https://arxiv.org/pdf/2609.28793) |

## 推荐实验与核查原则

1. **直接目标**：Cheng 2023（改装排气片段分类）对比 Wang 2026（事件级 SED），先复现任务定义、输入、评估划分，再比较现场误报。
2. **交通负例**：MVD、IDMT 和 AClassiHonk 所对应的车型、鸣笛声音可用于构建困难负例，但不能自动视为许可可商用训练的数据。
3. **样本生成**：2401.09308 提供车辆经过声合成思路，目标排气音仍需要真实标注与独立道路测试。
4. **目标归属**：2305.14579 对应音视频方案；多车声源定位另见专题 2026 论文（2609.13595、2606.27751）。
5. **跨模态边界**：DAS 的车流轨迹、空间先验和自更新可以迁移方法思路，但地面振动与空气传声分布不同，不应合并汇报识别精度。

**状态**：已验证官方 arXiv 摘要、分类、PDF 链接与期刊摘要；未运行代码、未做本仓库复现、未确认公开的专项训练数据许可。
