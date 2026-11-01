# 全仓技术趋势地图 · Trend Evidence Map

**最后更新**：2026-11-01 · **技术趋势详情页：51 页** · 8 个研究方向。

每个趋势都可点击进入自己的 Markdown 页面，查看：**趋势主张、分析链路、证据/原文入口、支持与反证、迁移条件、建议对照实验及不确定性**。

> 本图谱是对仓库已列出技术趋势的**可追溯解释**，并不是基于 2,145 条候选论文的系统文献计量证明。详情中的部分论文链接属于领域背景资料，尚未完成逐趋势直接证据匹配；研究假设与已证实结果严格分开。

## 工业异常声检测（6）

[返回方向首页](../papers/acoustic-anomaly/README.md)

1. [重构式 ASD → 判别式/表征式 ASD](../papers/acoustic-anomaly/trends/trend-01.md)
2. [单项目最优 → 跨项目泛化](../papers/acoustic-anomaly/trends/trend-02.md)
3. [干净标签假设 → Noise-aware 学习](../papers/acoustic-anomaly/trends/trend-03.md)
4. [单一异常分数 → 可解释证据](../papers/acoustic-anomaly/trends/trend-04.md)
5. [片段级 → 事件/设备级](../papers/acoustic-anomaly/trends/trend-05.md)
6. [固定模型 → 部署后持续适应](../papers/acoustic-anomaly/trends/trend-06.md)

## 声音事件检测（6）

[返回方向首页](../papers/sound-event/README.md)

1. [单任务分类 → 持续/增量学习](../papers/sound-event/trends/trend-01.md)
2. [单一分类头 → 层级结构 + Prototype + Retrieval](../papers/sound-event/trends/trend-02.md)
3. [纯音频输入 → 音频 + 元数据](../papers/sound-event/trends/trend-03.md)
4. [统一网络 → Domain-specific Experts / MoE](../papers/sound-event/trends/trend-04.md)
5. [离线分类 → 事件级决策](../papers/sound-event/trends/trend-05.md)
6. [静态类别集合 → Open-world / Class-incremental](../papers/sound-event/trends/trend-06.md)

## DAS 光纤听诊（7）

[返回方向首页](../domains/das/README.md)

1. [全局分类器 → 位置级 baseline + 时空聚合](../domains/das/trends/trend-01.md)
2. [10 s clip → 时空事件](../domains/das/trends/trend-02.md)
3. [固定探测器 → 通道质量感知](../domains/das/trends/trend-03.md)
4. [纯数据驱动 → 物理约束 + 数据驱动](../domains/das/trends/trend-04.md)
5. [单项目模型 → 标准化 + 自监督预训练 + 跨项目适配](../domains/das/trends/trend-05.md)
6. [异常/正常 → 严重度/健康状态/RUL](../domains/das/trends/trend-06.md)
7. [离线高精度 → 边缘实时与工程指标](../domains/das/trends/trend-07.md)

## 泄漏检测（6）

[返回方向首页](../domains/leakage/README.md)

1. [检测 → 定位 → 泄漏率/严重度估计](../domains/leakage/trends/trend-01.md)
2. [单传感器 → 多模态](../domains/leakage/trends/trend-02.md)
3. [实验室高精度 → 现场跨域泛化](../domains/leakage/trends/trend-03.md)
4. [固定特征 → 自适应波形/表征学习](../domains/leakage/trends/trend-04.md)
5. [黑盒分类 → 物理约束推理](../domains/leakage/trends/trend-05.md)
6. [单点检测 → 长期健康监测](../domains/leakage/trends/trend-06.md)

## 声纹识别（7）

[返回方向首页](../related/speaker-recognition/README.md)

1. [封闭集分类 → 通用 Embedding + 后端判别](../related/speaker-recognition/trends/trend-01.md)
2. [单原型 → 多原型/Sub-center/MoE](../related/speaker-recognition/trends/trend-02.md)
3. [监督训练 → 自监督预训练 + 轻量适配](../related/speaker-recognition/trends/trend-03.md)
4. [统一域 → Domain-invariant / Domain-specific Experts 并存](../related/speaker-recognition/trends/trend-04.md)
5. [点估计分数 → Uncertainty-aware calibration](../related/speaker-recognition/trends/trend-05.md)
6. [不可解释 embedding → 可解释/可听表征](../related/speaker-recognition/trends/trend-06.md)
7. [Embedding matching → Audio-LLM reasoning](../related/speaker-recognition/trends/trend-07.md)

## 人脸识别（6）

[返回方向首页](../related/face-recognition/README.md)

1. [分类 logits → Embedding space](../related/face-recognition/trends/trend-01.md)
2. [单中心类分布 → 多子中心](../related/face-recognition/trends/trend-02.md)
3. [默认标签正确 → 质量/噪声感知](../related/face-recognition/trends/trend-03.md)
4. [固定类别 → 增量类别](../related/face-recognition/trends/trend-04.md)
5. [统一阈值 → 质量感知/校准阈值](../related/face-recognition/trends/trend-05.md)
6. [黑盒错误 → Embedding 可视化与样本审计](../related/face-recognition/trends/trend-06.md)

## 图像异常检测（6）

[返回方向首页](../related/visual-anomaly/README.md)

1. [重构 → 预训练特征空间检测](../related/visual-anomaly/trends/trend-01.md)
2. [全局图像 → Patch / Region](../related/visual-anomaly/trends/trend-02.md)
3. [参数模型 → Memory Bank / Retrieval](../related/visual-anomaly/trends/trend-03.md)
4. [同域 benchmark → Domain Shift / TTA](../related/visual-anomaly/trends/trend-04.md)
5. [Closed-set → Zero-shot / Open-vocabulary](../related/visual-anomaly/trends/trend-05.md)
6. [单帧 → 时序/视频异常](../related/visual-anomaly/trends/trend-06.md)

## 基础模型（7）

[返回方向首页](../related/foundation-models/README.md)

1. [任务专用 CNN → 通用预训练 Encoder](../related/foundation-models/trends/trend-01.md)
2. [监督预训练 → Self-supervised / Multimodal pretraining](../related/foundation-models/trends/trend-02.md)
3. [全量微调 → Adapter/LoRA/Linear Probe](../related/foundation-models/trends/trend-03.md)
4. [单一 embedding → Retrieval-Augmented](../related/foundation-models/trends/trend-04.md)
5. [Audio-only → Audio-Text / Multimodal](../related/foundation-models/trends/trend-05.md)
6. [预测模型 → Reasoning model / Agent](../related/foundation-models/trends/trend-06.md)
7. [通用大模型 → 行业基础模型](../related/foundation-models/trends/trend-07.md)

## 证据等级与维护规范

- **A · Direct**：论文明确提出与该技术趋势直接相关的技术机制，并有相应公开实验。
- **B · Comparative**：多篇同协议的比较或挑战赛任务演变显示共同方向。
- **C · Context**：代表论文可证实背景方法存在，但未独立证明趋势方向。
- **H · Hypothesis**：面向工业声学迁移的推断，未实测。

目前多数页面处于 **C/H 级**。后续更新需要把具体论文与每一环论据建立对应关系，记录 DOI/arXiv、公开 PDF、代码、支持/不支持结论和时间戳，并明确是否在工业场景重现。

## 质量校验

- 所有原有技术趋势标题应在本图谱及各方向 README 中拥有可点击详情页。
- 每页须有“结论→证据→推理→边界→可证伪实验”的完整结构。
- 不公开私人 Google Drive 文件 ID、私人 URL 和企业内部研究数据。
