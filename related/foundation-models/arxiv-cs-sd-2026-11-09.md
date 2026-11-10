# arXiv cs.SD 每日增量｜2026-11-09 公告

本页为2026-11-09公告相关论文。原论文结果与工业声学/DAS迁移假设严格区分，尚无DAS现场复现。

## 1. AudioSphere: Towards Self-Supervised Spatial Audio Representation Models

- **作者**：Goksenin Yuksel; Marcel van Gerven; Kiki van der Heijden
- **首次提交**：2026-11-06（2026-11-09 cs.SD 公告）
- **arXiv / PDF**：[2611.09275](https://arxiv.org/abs/2611.09275) · [官方 PDF](https://arxiv.org/pdf/2611.09275)
- **方法/原论文证据**：多通道 Ambisonics 时频块与强度向量联合掩码重建，学习帧级空间—声学表示；发布RealSELD冻结骨干评估。
- **工业声学/DAS迁移价值（研究假设）**：研究假设：DAS多通道/邻近探测器联合自监督表征，兼顾片段分类与空间事件定位；Ambisonics方位线索与DAS光纤位置/耦合并不等价，需要重新定义空间任务。
- **代码/复现状态**：[作者代码](https://github.com/labhamlet/AudioSphere) 已公开，模型/数据另见论文；未DAS复现。

## 2. Improving Large Audio-Language Model Embedding Baselines for Instruction-Aware Speech Retrieval

- **作者**：Chen-An Li; Cheng-Han Chiang; Hung-yi Lee
- **首次提交**：2026-11-06（2026-11-09 cs.SD 公告）
- **arXiv / PDF**：[2611.09122](https://arxiv.org/abs/2611.09122) · [官方 PDF](https://arxiv.org/pdf/2611.09122)
- **方法/原论文证据**：IRIS-Embed 将大音频语言模型转为对比式检索编码器，依据检索指令加权不同音频编码层；作者报告 INSPIRE Recall@50 62.92%，强基线45.15%。
- **工业声学/DAS迁移价值（研究假设）**：研究假设：用不同检索指令区分托辊异响、警笛干扰、相似项目/探测器等检索目标，探索层权重与prototype库；原论文以语音检索为主。
- **代码/复现状态**：[作者项目](https://github.com/lca0503/IRIS) 存在；论文注明代码/资源将上传，完整可复现性待核验。

## 3. AnomSep: Bridging Optimization-Based Separation and Deep Neural Refinement for Anomaly Detection with Listenable Explanations

- **作者**：Koki Shoda; Jun Younes Louhi Kasahara; Qi An; Atsushi Yamashita
- **首次提交**：2026-11-06（2026-11-09 cs.SD 公告）
- **arXiv / PDF**：[2611.09279](https://arxiv.org/abs/2611.09279) · [官方 PDF](https://arxiv.org/pdf/2611.09279)
- **方法/原论文证据**：以目标环境正常声音字典进行优化式正常/异常分离，再在预训练音频潜空间中深度细化；分离出的异常声可供试听，异常声能量直接定义异常评分。
- **工业声学/DAS迁移价值（研究假设）**：研究假设：为DAS托辊报警提供可试听的异常证据，配合正常基线/异常残差与现有ResNet分数融合；须检验正常字典污染、弱异常被抑制和现场干扰被误分为异常的风险。
- **代码/复现状态**：摘要页未提供官方代码；未复现。
 
## 技术趋势复核

本批包含异常残差可试听解释、空间自监督、场景—事件联合建模、噪声自适应跨站点评估及指令条件检索；仅对出现新任务/证据链的方向更新趋势，其他视为既有范式延伸。
