# arXiv cs.SD 2026-11-19 公告｜跨领域轻量声学与多源表征

> 公告日期：2026-11-19；以下 DAS 迁移均为**研究假设**，非托辊实测。

## 1. RespCCT and FreqCCT: Compact, Explainable and Cost-Aware Convolutional Transformers for Multi-Class Respiratory Disease Classification
- **作者**：Auntor Chakma, Mst. Farhana Akter, Abu Henaf Rashid Ahmad Mufti, Asmana Yasmin
- **首次提交**：2026-11-18；**arXiv**：[2611.24323](https://arxiv.org/abs/2611.24323)；**PDF**：[下载](https://arxiv.org/pdf/2611.24323)；**DOI**：10.48550/arXiv.2611.24323
- **任务/方法**：对呼吸音多类别识别构建12.5万/17.3万参数级紧凑卷积 Transformer，输入 Mel、CQT、倒谱图，比较预训练网络、配对 bootstrap、CPU 单线程分阶段成本与特征来源可辨识性。
- **原论文证据/局限**：作者报告较强分类指标，但跨数据库来源线性探针准确率0.958，提示模型可能编码采集域信息；三种谱图预处理耗时超过模型前向。数据集为呼吸音，非工业数据。
- **工业声学/DAS迁移（研究假设）**：可借鉴轻量分类器+全链路延迟测量、数据来源泄漏诊断；对10秒托辊片段需严格项目级划分并测量预处理时间和跨项目FPR。
- **代码/复现**：arXiv 页面未提供明确官方代码；使用公开呼吸音数据集，但具体实现/权重公开状态待核实。

## 2. Why Multi-Source Audio Fails to Compose: A Geometric Diagnosis and Its Remedy
- **作者**：Anurag Singh, Prajwal Singh, Shanmuganathan Raman
- **首次提交**：2026-11-18；**arXiv**：[2611.24410](https://arxiv.org/abs/2611.24410)；**PDF**：[下载](https://arxiv.org/pdf/2611.24410)；**DOI**：10.48550/arXiv.2611.24410
- **任务/方法**：研究多音源条件音频生成图像的跨模态组合失败，比较 BEATs/CLAP 特征映射至 CLIP 文本 token 空间后的类内紧致度、语义对齐与源间分离；提出多 token 占位与推理时注意力/空间分离优化。
- **原论文证据/局限**：作者在音频到图像生成基准报告多源组合改进；这些是生成质量指标，不是音频检测或 DAS 定位指标。
- **工业声学/DAS迁移（研究假设）**：多干扰混合场景下可借鉴“目标事件与干扰事件是否在联合表征中分离”的几何诊断；评估 CLAP/BEATs 与 DAS 自训练 encoder 的类间分离、检索与混合声鲁棒性，而非直接复用图像生成模块。
- **代码/复现**：arXiv 页面未提供明确官方代码链接；VGGSound 派生基准和实验描述可参考，复现资源状态待核实。

## 技术判断
- **技术时间线复核**：轻量分类器全链路成本核算、多源跨模态表征几何诊断均属已有技术路线的强化，不新增独立 DAS 范式节点。
- **技术趋势复核**：关注“只看模型参数/FLOPs → 测量特征预处理与整体时延”和“只看融合效果 → 检查表征空间中目标/干扰源的可分离性”。
- **当前判断/待关注**：DAS 优先检查跨项目域泄漏、端侧预处理瓶颈、混合声表征可分离性；迁移尚未实验验证。
