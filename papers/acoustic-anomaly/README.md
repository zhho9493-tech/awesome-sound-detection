# Acoustic Anomaly Detection / 声学异常检测

关注无监督 ASD、First-shot、Noise-aware、Domain Generalization、开放集及工业状态识别。

- [arXiv cs.SD 2025-01-01—2026-11-03 相关论文全量初筛](arxiv-cs-sd-2025-2026.md)
- [论文技术趋势与交互时间线（HTML）](papers-timeline.html)
- [云端“论文仓库”新增论文（2026-11-12，含 Drive 下载链接）](drive-cloud-library-2026-11-12.md)

官方入口：
- [DCASE](https://dcase.community/)
- [DCASE 2020 Task 2](https://dcase.community/challenge2020/task-unsupervised-detection-of-anomalous-sounds)
- [DCASE 2023 Task 2](https://dcase.community/challenge2023/task-first-shot-unsupervised-anomalous-sound-detection-for-machine-condition-monitoring)
- [MIMII Dataset](https://zenodo.org/records/3384388)
- [Google Drive 已收藏论文索引](drive-library-index.md)

优先研究：跨项目泛化、类别不平衡、伪标签、低检准误报、噪声标签识别、强度分级。

## 技术时间线

| 阶段 | 技术主线 | 代表性变化 |
|---|---|---|
| 2019–2020 | 无监督机器异常声检测 | 以 AutoEncoder、重构误差、MIMII/DCASE 为核心，重点解决“只有正常数据” |
| 2021–2022 | 判别式表征与度量学习 | 从纯重构转向 embedding、angular margin、one-class / outlier exposure，提高类间可分性 |
| 2023–2024 | Domain Shift / First-shot ASD | DCASE 明确把跨域和极少目标域样本作为核心问题，开始强调 domain generalization 与 adaptation |
| 2024–2025 | 多尺度、Transformer、图结构与高频特征 | 从单尺度谱图 CNN 转向多尺度时频建模、Transformer/GCN 和细粒度频谱结构 |
| 2025–2026 | Noise-aware、标签质量、开放集与持续适应 | 关注错误标签、未知异常、跨项目稳定性、低误报校准以及部署后的持续学习 |
| 下一阶段 | 从“异常分数”走向“健康状态” | 事件级聚合、异常强度、长期趋势、状态演化与预测性维护成为工业落地重点 |

## 技术趋势

1. **[重构式 ASD → 判别式/表征式 ASD](trends/trend-01.md)**：工业复杂噪声下，单纯“重构不出来就是异常”越来越难支撑低误报要求。
2. **[单项目最优 → 跨项目泛化](trends/trend-02.md)**：评价重点从同域 AUC 转向 Domain Shift、First-shot、目标域少样本与未知工况。
3. **[干净标签假设 → Noise-aware 学习](trends/trend-03.md)**：标签质量评估、伪标签置信、样本难度建模和错误标签修正成为重要组成。
4. **[单一异常分数 → 可解释证据](trends/trend-04.md)**：频带、时序、原型距离、检索近邻和显式干扰类别共同参与最终判断。
5. **[片段级 → 事件/设备级](trends/trend-05.md)**：工业系统真正关心持续异常、设备位置、严重度和维修决策，而非单个 clip 的分类结果。
6. **[固定模型 → 部署后持续适应](trends/trend-06.md)**：Test-time Adaptation、动态基线、prototype refresh 和 domain-specific calibration 将更重要。

## 当前判断 / 待关注

- 近期最值得跟踪：Noise-aware ASD、跨域 First-shot、开放集拒识、异常严重度/健康演化。
- 对工业声学建议长期同时报告：pAUC、Precision/Recall、设备级误报率、跨项目性能下降幅度。
- **2026-11 新证据提醒**：生态声学研究 [2610.42042](https://arxiv.org/abs/2610.42042) 显示随机帧划分会显著高估性能；跨项目/探测器/时段分组验证和高置信误报审计应作为工业音频必选项（迁移假设）。
- 新增论文后，需要检查：是否改变“Domain Shift / Noise-aware / Health-state”三条主趋势的优先级。

## 2026-11-02 cs.SD 周度论文更新

- [本周新收录论文、分类关联及 arXiv PDF](arxiv-cs-sd-week-2026-11-02.md)
- 收录按现有研究方向筛选，属于待复现/待全文分析资料；相关结论不代表已在工业现场验证。

## 2026-11-03 每日增量（对应 cs.SD 2026-11-02 公告）

- [新增：分组验证、误报控制与生态声学跨领域证据](arxiv-cs-sd-2026-11-02.md)。
- **趋势复核**：强化已有跨项目泛化/误报治理判断，尚不足以新增 ASD 算法范式或技术时间线节点。

## 2026-11-03 工业托辊异常检测可迁移论文

- [MIRA: A Transformer-Based Framework for Idler Roller Anomaly Detection and Localization](https://doi.org/10.3390/s25247469)（Sensors 2025；Younho Nam 等）：采用分布式布置的**麦克风+加速度计**、masked Transformer autoencoder、正常样本重构误差与空间映射，在试验台架报告异常检测准确率 98.70% 和故障定位准确率 96.09%。**该论文不是 DAS 研究**，需在 DAS 跨项目独立测试集验证后才能推断迁移效果。详见 [DAS 皮带机专题的可迁移方法部分](../../domains/das/conveyor-papers-2025-2026.md)。

## 2026-10 arXiv cs.SD 月度候选整理

- [10 月论文分类索引（已知候选，非 505 条全量核验）](arxiv-cs-sd-2026-10.md)

- [2026 年 10 月目录逐条核验新增候选（阶段性）](arxiv-cs-sd-2026-10-verified-additions.md)：按标题和类别初筛，尚未完整核验 505 条。

## 2026-11 新增：可听解释与异常声分离

- **[AnomSep (Shoda et al., 2026)：优化分离 + 潜空间神经细化](anomsep-2026.md)**｜[arXiv](https://arxiv.org/abs/2611.09279)｜[PDF](https://arxiv.org/pdf/2611.09279)。先由目标环境正常声字典得到初步正常/异常分量，再在预训练音频潜在空间中细化；以分离异常声的能量作为检测分数，直接提供可播放的判断依据。
- **技术时间线节点（2026-11-06）**：从单一数值异常分数扩展为“检测与可听异常声解释同源”；属于可解释 ASD 方向的新案例，尚未在 DAS 场景复现。详见[趋势 4](trends/trend-04.md)。
