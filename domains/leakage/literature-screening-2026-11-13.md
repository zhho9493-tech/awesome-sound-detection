# 听漏仪与管道泄漏监测论文筛选（2026-11-13）

> 来源：用户提供两批 Google Scholar 检索结果（2025–2026）。此文档是新增的**专题筛选记录**，不代表逐条原文验证，也不宣称论文已在其他索引中完全去重。优先以 DOI / 出版商页面作唯一标识。评分依据：便携式水管听漏仪优先，声学/振动检测与相关定位优先，纯压力/流量/视觉方法作为跨模态参考。未核实事项明确标注。

## A. 直接相关：优先阅读

| 论文 | 年份 | 方法/信号 | 价值 | 正式出处 |
|---|---:|---|---|---|
| Acoustic Leak Localization Study Based on MVDR Time-Delay Estimation Algorithm in a Cross-Spectral Domain for Water Pipeline Systems — Z. Feng, W. Cheng | 2026 | 双传感器泄漏声、STFT、跨谱域 CSMVDR、频带优化与时延轨迹连续性，针对反射导致的互相关多峰 | **最高优先级：相关定位算法改进**；需双通道设备与传播速度标定 | [ASCE / DOI](https://doi.org/10.1061/JPSEA2.PSENG-2055) |
| Explainable Pipeline Leak Detection and Fluid Flow Analysis Using Flexural Ultrasonic Sensor and Machine Learning Algorithms — L. A. Ajao 等 | 2026 | 柔性超声传感器 + 可解释机器学习（具体模型需查全文） | **高：传感器与可解释分类**；介质/耦合条件需核对 | [IEEE Access / DOI](https://doi.org/10.1109/ACCESS.2026.3713787) |
| Pipeline Leakage Detection with Multisensor Fusion Based on Support Vector Machine — X. Liu 等 | 2026 | 声学 + 压力 + 流量，离散小波去噪、时频特征、SVM 特征级融合 | **高：声学增强/多模态验证**；单机听漏仪并非总能获得压力/流量 | [IEEE Sensors Journal / DOI](https://doi.org/10.1109/JSEN.2026.3704869) |
| Dilated Gated Convolution with Attention for Gas Pipeline Leak Detection — H. Liu, Z. Li | 2025 | 气体泄漏声发射、空洞门控卷积+注意力；报告 GPLA-12 上 24 类 93.14% 准确率（作者结果） | **高：弱泄漏抗噪声学表征**；气体向水管迁移需验证 | [SAFEPROCESS / DOI](https://doi.org/10.1109/SAFEPROCESS67117.2025.11268105) |
| UWFBG Array Vibration Sensing Technology for Gas Pipeline Leakage Detection and Location | 2024 | 超弱光纤光栅阵列、振动频谱、CEEMDAN/小波和 PSD 定位 | **高：振动/光纤跨领域**；**注意是 2024 年另一篇论文**，不要与下方 2025 AHR RGC 工作混同 | [Optics Communications / DOI](https://doi.org/10.1016/j.optcom.2024.130414) |

## B. 方法相关：作为水管/泄漏系统跨领域借鉴

| 论文 | 年份 | 信号/路线 | 适用判断 | 正式出处 |
|---|---:|---|---|---|
| Leakage Break Diagnosis for Water Distribution Network Using LSTM-FCN Neural Network Based on High-Frequency Pressure Data — S. Peng 等 | 2025 | 高频压力时序 + LSTM/FCN；作者报告总体准确率 85% | 压力波辅助检测，不是纯声学听漏 | [Water / DOI](https://doi.org/10.3390/w17121823) |
| An early warning method of pipeline leakage monitoring with limited leakage samples — X. Cai 等 | 2025 | 实时瞬态机理简化模型 MR-RTTM + 少量泄漏样本 | 小样本、机理融合、阈值策略；需管网瞬态测量 | [Measurement / DOI](https://doi.org/10.1016/j.measurement.2024.116013) |
| High Precision Detection Pipe Bursts Based on Small Sample Diagnostic Method — G. Shi 等 | 2025 | 水力水头损失比 HLR + 深度迁移学习；压力传感器 | 物理特征/小样本迁移启发；爆管不等于微漏 | [Sensors / DOI](https://doi.org/10.3390/s25113431) |
| Leak detection, size estimation and localization in tree-shaped pipe flow networks — N. C. A. Wilhelmsen, O. M. Aamo | 2025 | 树状网络 PDE/压力流量边界测量 | 管网定位和定量模型；不适合直接称为听漏声学模型 | [Systems & Control Letters / DOI](https://doi.org/10.1016/j.sysconle.2025.106255) |
| Comparison of Leak Localization and Quantification Methods for Compressed Air Systems Using Multi-Criteria Decision Analysis — A. Hojjati, P. Radgen | 2026 | 压缩空气定位/泄漏量评估技术比较 | 选型与性能指标设计，非新声学分类器 | [Energies / DOI](https://doi.org/10.3390/en19071658) |
| Bolted Flange Connection Leakage: A Systematic Review of Monitoring Challenges and Technologies — B. Cloostermans 等 | 2025 | 法兰连接泄漏技术综述 | 传感/工程可靠性背景，非埋地供水管声学专用 | [IEEE Sensors Reviews / DOI](https://doi.org/10.1109/SR.2025.3550861) · [作者机构公开 PDF](https://cris.vub.be/ws/portalfiles/portal/134566893/2025_-_B._Cloostermans_-_Bolted_Flange_Connection_Leakage_-_A_Systematic_Review_of_Monitoring_Challenges_and_Technologies.pdf) |
| Horizontal pipeline leakages prediction under multiphase flow — S. B. Ipinsokan 等 | 2026 | 压力/流量/温度 + 回归与分类，多相流实验 | 跨工况数据建模；与便携式声学听漏较远 | [Discover Applied Sciences / DOI](https://doi.org/10.1007/s42452-026-08646-6) |
| Prediction of Leak on Gas Pipeline Using a Hybrid Machine Learning Model — E. Aniyom, A. Chikwe | 2025 | 压力/流量/温度，RF+XGBoost Voting | 非声学；系统级参考 | [Improved Oil and Gas Recovery / DOI](https://doi.org/10.14800/IOGR.1344) |

## C. 标题级候选：不补造 DOI，等待身份与原文核验

| 论文标题（按用户提供） | 初步类别 | 状态 |
|---|---|---|
| UWFBG Array Vibration Sensing Technology for Aqueous Homogeneous Reactor RGC System Pipeline Leakage Detection and Location (Zhang 等，2025) | 光纤振动检测与定位、核工程特殊环境 | **待核验**；与 2024 *Optics Communications* 的气体泄漏 UWFBG 论文区分 |
| An overview of pipeline leak detection and location systems | 传统综述 | **待核验**：题名不完整，缺作者/年份，不作为独立已核实文献计数 |
| AI-Driven Predictive Maintenance for Stationary Hydrogen Storage and Distribution Infrastructure: A Systematic Review ... (Chowdhury, 2026) | 氢气设施运维综述 | 低优先级，**待核验** |
| PV-based off grid valve drive system for leakage protection in water networks (Teleb 等，2025) | 阀门驱动/防护 | 非检测算法，低优先级 |
| Numerical investigation of crude oil diffusion dynamics and temperature field evolution ... (Liu 等，2025) | 地下油泄漏扩散模拟 | 非听漏仪核心，低优先级 |
| Spatial information adaptive regulation and feature alignment for infrared methane instance segmentation (2026) | 红外视觉甲烷分割 | 跨模态参考，低优先级 |
| Multi-scale weighted fusion network for hyperspectral and LiDAR data to identify stressed vegetation ... (Li 等，2026) | 高光谱+LiDAR 地表植被 | 非便携式听漏，低优先级 |
| A Localized Directional Stepwise-Hydraulic Resistance Control Algorithm ... (Kim 等，2026) | 管网损伤后控制 | 非检测，低优先级 |
| Необратимые процессы в природе и технике | 会议总集 | 无法对应具体泄漏论文，不收录为论文 |
| 其他搜索摘要不完整的条目 | — | 保留标题级候选，勿虚构实验结果/代码链接 |

## 面向听漏仪的优先验证计划

1. **双通道相关定位**：GCC-PHAT / 传统互相关 vs CSMVDR；按管材、管径、压力、传感器间距、弯头/反射、背景噪声拆分；用定位绝对误差、90 分位误差、误定位率衡量。
2. **单传感器抗噪检测**：ResNet 基线 vs 空洞门控 CNN + attention；逐 SNR、微漏孔径、管壁耦合与噪声源验证 AUPRC、固定误报率下召回、跨管材泛化。
3. **可解释/多模态**：仅声学 vs 声学+压力 vs 声学+流量；报告额外硬件成本、可用率、模型提升，不能将压力系统的性能直接写作手持听漏仪性能。
4. **少样本**：HLR/MR-RTTM 的核心在物理先验和小样本融合；若设备只采音频，应设计声学传播/谱特征代理并单独验证，不直接套用水力公式。

## 收录与核验说明

- 本次查验了 `domains/leakage/README.md`、`arxiv-cs-sd-2025-2026.md` 和两份 Drive 分类索引；上述已核实题目未见于这些专题正文。**未对全仓大型 JSON 主数据库做完整内容级去重**。
- 已核实 DOI 的文章收录在此**专题新增文献索引**；不是下载或镜像出版商 PDF，也不声称已有公开源代码。
- 对“UWFBG AHR RGC”与“An overview ...”保持候选，不将相似论文误判成相同论文。
- DOI 链接为正式出版商标识；部分文章可能付费阅读，公开 PDF 仅在确有合法链接时提供。
