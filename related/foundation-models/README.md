# Foundation Models / 基础模型

- [CLAP](https://github.com/LAION-AI/CLAP) — 音频文本对齐
- [BEATs](https://github.com/microsoft/unilm/tree/master/beats) — 音频自监督
- [DINOv2](https://github.com/facebookresearch/dinov2) — 视觉特征
- [Google Drive 历史论文索引](drive-library-index.md)

研究方案：冻结编码器、线性探针、微调、Adapter/LoRA、检索增强，和专用音频 CNN 比较。

## 技术时间线

| 阶段 | 技术主线 | 代表性变化 |
|---|---|---|
| 2021–2022 | Audio SSL / BEATs 类预训练 | 大规模无标签音频预训练成为通用特征底座 |
| 2022–2023 | CLAP / Audio-Text Alignment | 音频与文本语义空间对齐，支持 zero-shot 与检索 |
| 2023–2024 | Vision/Multimodal Foundation Features | DINOv2 等强 encoder 证明“冻结特征 + 轻量下游”具有高迁移价值 |
| 2024–2025 | Adapter / LoRA / Retrieval Augmentation | 参数高效适配和外部记忆成为部署友好路线 |
| 2025–2026 | Industrial Foundation Models | 开始面向多模态工业信号、不同采样率、不同设备建立统一表征 |
| 2026 | Audio-LLM / Reasoning RL | 从“编码/检索”进一步走向音频理解、推理、证据组织和诊断解释 |
| 2026-10/11 | Audio-LLM 评估校准与跨模态冲突 | 研究开始量化 Audio-LLM 感知偏差和模态不一致风险，强调证据可靠性而非仅增加模态 |
| 下一阶段 | Domain-specific Foundation Encoder + Agent | 通用 encoder、检索库、工具调用和物理/状态模型组合成工业智能体 |

## 技术趋势

1. **[任务专用 CNN → 通用预训练 Encoder](trends/trend-01.md)**：训练重心从“从零训练分类器”转向“选择/适配基础表征”。
2. **[监督预训练 → Self-supervised / Multimodal pretraining](trends/trend-02.md)**：未标注工业数据价值显著提升。
3. **[全量微调 → Adapter/LoRA/Linear Probe](trends/trend-03.md)**：跨项目快速适配和防遗忘更易工程化。
4. **[单一 embedding → Retrieval-Augmented](trends/trend-04.md)**：历史样本、相似案例和 prototype 可直接参与推理。
5. **[Audio-only → Audio-Text / Multimodal](trends/trend-05.md)**：文本知识、维修记录和设备元数据可与音频联合；但跨模态证据冲突可能使 Audio-LLM 退化，需显式一致性检查与回退机制。
6. **[预测模型 → Reasoning model / Agent](trends/trend-06.md)**：模型开始输出“证据—判断—建议”，而不只是概率。
7. **[通用大模型 → 行业基础模型](trends/trend-07.md)**：工业采样率、传感器、设备物理差异决定专用预训练仍然必要。

## 当前判断 / 对工业声学迁移

- 建议长期基线：专用 ResNet vs 冻结预训练 encoder vs 全量微调 vs Adapter/LoRA vs DAS/工业音频自监督预训练。
- 对海量未标注工业数据，最值得投入的是 **domain-specific self-supervised pretraining**。
- **2026-11 新证据**：Audio-LLM 质量评估存在零样本偏差，LoRA 适配可改善特定任务；多模态情绪证据不一致与错误率上升相关。建议在 DAS 工况/文本融合中增设 conflict-aware gating 和 calibration 对照。
- 新增论文后，应判断是否改变“预训练底座 / 轻量适配 / 检索增强 / 推理智能体”四条趋势。

## 2026-11-02 cs.SD 周度论文更新

- [本周新收录论文、分类关联及 arXiv PDF](arxiv-cs-sd-week-2026-11-02.md)
- 收录按现有研究方向筛选，属于待复现/待全文分析资料；相关结论不代表已在工业现场验证。

## 2026-11-03 每日增量（对应 cs.SD 2026-11-02 公告）

- [新增：Audio-LLM 质量评估与多模态不一致可靠性（2 篇）](arxiv-cs-sd-2026-11-02.md)。
- **趋势更新**：增加“评估校准与证据冲突”时间线节点，并更新多模态融合可靠性条件；未声称已在工业 DAS 验证。

## 2026-10 arXiv cs.SD 月度候选整理

- [10 月论文分类索引（已知候选，非 505 条全量核验）](arxiv-cs-sd-2026-10.md)

- [2026 年 10 月目录逐条核验新增候选（阶段性）](arxiv-cs-sd-2026-10-verified-additions.md)：按标题和类别初筛，尚未完整核验 505 条。
