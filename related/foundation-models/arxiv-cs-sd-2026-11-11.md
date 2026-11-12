# arXiv cs.SD 每日增量｜2026-11-11 公告

> 来源：[arXiv cs.SD](https://arxiv.org/list/cs.SD/recent)。公告日期与首次提交日期不同。DAS迁移价值均为**研究假设**，并非托辊现场验证。

## AURA: Auditory Spatial Intelligence via a Unified Representation from a General-Audio Encoder through Complete Alignment

- **作者**：Boyan Han; Xiaoyan Wang; Zhe Sun; Ziqi Wang; Yujun Cai; Hongli Cao; Yiwei Wang; Ming-Hsuan Yang; Liang An
- **首次提交**：2026-11-10；**arXiv ID**：2611.13687；**DOI**：10.48550/arXiv.2611.13687（arXiv DOI）
- **原文**：[arXiv](https://arxiv.org/abs/2611.13687) · [PDF](https://arxiv.org/pdf/2611.13687)
- **任务/方法摘要**：针对多声源空间音频问答，分析冻结通用音频codec的双耳差分空间线索与音频—文本信息不对称；通过完整场景描述和显式通道差分实现目标声源与方向绑定，冻结codec和语言模型，仅训练轻量对齐模块。
- **数据/指标**：SpatialSoundQA；论文报告双声源方向准确率较最强专用系统提高10.31个百分点，训练参数约为其40%；这是原论文任务结果。
- **工业声学/DAS迁移（研究假设）**：可借鉴“空间线索显式化 + 声源身份绑定”，探索相邻DAS探测器时空证据与异常托辊位置的绑定；双耳立体声与DAS空间采样机理不同，不可直接移植通道差分或性能。
- **复现/代码状态**：arXiv摘要未给出官方代码/权重地址；待核实。
- **局限/适用条件**：需验证多异常并发、空间耦合、通道轮巡及跨项目定位鲁棒性。

## Exploring Post-Hoc Disentanglement of Audio Foundation Models for Music Similarity

- **作者**：Lucas de Souza Brandão; Gabriel da Costa Merlin; Diego Furtado Silva
- **首次提交**：2026-11-10；**arXiv ID**：2611.14415；**DOI**：10.48550/arXiv.2611.14415（arXiv DOI）
- **原文**：[arXiv](https://arxiv.org/abs/2611.14415) · [PDF](https://arxiv.org/pdf/2611.14415)
- **任务/方法摘要**：在冻结CLAP、MuQ、MERT等预训练embedding上应用条件相似网络（CSN）属性掩码和轻量适配，实现按属性选择的子空间相似度；对比不同mask、pooling与适配深度。
- **数据/指标**：两个音乐相似性数据集；论文报告属性解耦与检索表现改善，摘要未提供可直接引用的数值。
- **工业声学/DAS迁移（研究假设）**：探索“故障类型/运行状态/探测器背景”条件化embedding检索，减少工况与异常语义纠缠；需与原型学习、ArcFace和单一embedding检索对照。
- **复现/代码状态**：摘要未给出官方代码链接；待核实。
- **局限/适用条件**：音乐属性和工业故障属性不同，且需确保故障信号未被掩码过滤。
