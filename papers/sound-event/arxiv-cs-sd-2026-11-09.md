# arXiv cs.SD 每日增量｜2026-11-09 公告

本页为2026-11-09公告相关论文。原论文结果与工业声学/DAS迁移假设严格区分，尚无DAS现场复现。

## 1. SAS: Scene-Annotated AudioSet Strong for Joint Scene-Event Analysis

- **作者**：Michel Olvera; Paraskevas Stamatiadis; Romain Serizel; Slim Essid; Gaël Richard
- **首次提交**：2026-11-06（2026-11-09 cs.SD 公告）
- **arXiv / PDF**：[2611.09199](https://arxiv.org/abs/2611.09199) · [官方 PDF](https://arxiv.org/pdf/2611.09199)
- **方法/原论文证据**：为 AudioSet Strong 补充两套声景分类体系的片段级场景标注，分析场景特异性事件共现和声学—语义表示偏离；后者可预测分类错误。
- **工业声学/DAS迁移价值（研究假设）**：研究假设：将皮带运行状态、位置/探测器和背景工况作为场景条件，测试场景条件化识别与跨项目场景偏移；必须防止元数据捷径。
- **代码/复现状态**：摘要页未提供官方代码入口；尚未复现。

## 2. NAVE: A Normalized, Adaptive Conformer for Antarctic Whale Vocalization Detection

- **作者**：Matthias Nagl; Paul Primus; Gerhard Widmer
- **首次提交**：2026-11-06（2026-11-09 cs.SD 公告）
- **arXiv / PDF**：[2611.09642](https://arxiv.org/abs/2611.09642) · [官方 PDF](https://arxiv.org/pdf/2611.09642)
- **方法/原论文证据**：复数频谱均值扣除、PCEN 动态噪声底归一化、频率动态卷积和事件持续时间匹配的 Conformer 卷积核；采用留一站点阈值调优/测试，评估跨地点事件定位。
- **工业声学/DAS迁移价值（研究假设）**：研究假设：对DAS探测器背景谱差异、风噪与托辊事件长度，比较PCEN/频率动态前端、事件长度匹配卷积和跨项目阈值校准；注意原研究仅为鲸声且250 Hz采样，不能直接照搬。
- **代码/复现状态**：[作者代码、训练及LOSO评估脚本](https://github.com/TheFruitGuy/NAVE-SED) 已公开；未进行DAS复现。
 
## 技术趋势复核

本批包含异常残差可试听解释、空间自监督、场景—事件联合建模、噪声自适应跨站点评估及指令条件检索；仅对出现新任务/证据链的方向更新趋势，其他视为既有范式延伸。
