# Speaker Recognition / 声纹识别

- [ECAPA-TDNN](https://arxiv.org/abs/2005.07143)
- [SpeechBrain](https://github.com/speechbrain/speechbrain)
- [WeSpeaker](https://github.com/wenet-e2e/wespeaker)

迁移议题：Embedding 聚合、多原型、度量学习、域适应、开放集拒识和小样本类扩展。

应比较跨项目验证，不应以声纹 benchmark 推断工业声学效果。

## 近一年 arXiv 精选（2025-10-31—2026-10-31）

- [论文清单、方法解读和 PDF 下载链接](arxiv-2025-2026.md)
- [机器可读论文元数据 JSON](arxiv-2025-2026.json)

当前收录 11 篇精选论文；持续更新，非穷尽列表。

## 技术时间线

| 时间 | 技术主线 | 代表性变化 |
|---|---|---|
| 2017–2020 | x-vector / ECAPA / Margin-based embedding | 从分类网络转向高判别 speaker embedding |
| 2020–2023 | ArcFace/Sub-center、强数据增强、后端校准 | 提升类间 margin、处理难样本和多中心分布 |
| 2023–2025 | SSL pretrained speaker encoder | wav2vec/HuBERT/w2v-BERT 等预训练表征用于低资源与跨域 |
| 2026-02 | SSL speaker recognition 系统性比较 | 自监督成为主流底座之一 |
| 2026-03–08 | Language-invariant / noisy-domain adaptation | 跨语言、真实噪声和 domain-invariant 表征成为重点 |
| 2026-05 | SpeakerLLM | 从 embedding 匹配扩展到 audio-LLM reasoning |
| 2026-06 | Interpretable Embedding | 可听、可分解、可解释的 embedding 受到关注 |
| 2026-09 | Uncertainty-aware calibration / MoE | 不确定性校准、多专家路由强化低误报和多域鲁棒性 |
| 2026-10 | Parameter-efficient adaptation | 通过 residual adapter / layer aggregation 降低跨域微调成本 |

## 技术趋势

1. **[封闭集分类 → 通用 Embedding + 后端判别](trends/trend-01.md)**：更适合新增类别、检索和开放集识别。
2. **[单原型 → 多原型/Sub-center/MoE](trends/trend-02.md)**：同一类别存在多工况/多模式时，单中心假设越来越弱。
3. **[监督训练 → 自监督预训练 + 轻量适配](trends/trend-03.md)**：无标签数据规模成为重要资产。
4. **[统一域 → Domain-invariant / Domain-specific Experts 并存](trends/trend-04.md)**：一类方法消除域信息，另一类显式建模不同域。
5. **[点估计分数 → Uncertainty-aware calibration](trends/trend-05.md)**：置信度、拒识阈值和低误报报警更受重视。
6. **[不可解释 embedding → 可解释/可听表征](trends/trend-06.md)**：有利于诊断错误、标签噪声和异常模式。
7. **[Embedding matching → Audio-LLM reasoning](trends/trend-07.md)**：大模型开始承担证据组织、解释和复核，但尚未替代高效 embedding 检索。

## 当前判断 / 对工业声学迁移

- 最值得迁移：SSL encoder、Sub-center/Prototype、uncertainty calibration、parameter-efficient adaptation、MoE。
- 对跨项目工业分类，建议优先验证“共享 encoder + 项目/工况专家 + 校准后端”。
- 新增论文后，检查是否改变“预训练、域适应、不确定性、多中心”四条趋势。

## 2026-11-02 cs.SD 周度论文更新

- [本周新收录论文、分类关联及 arXiv PDF](arxiv-cs-sd-week-2026-11-02.md)
- 收录按现有研究方向筛选，属于待复现/待全文分析资料；相关结论不代表已在工业现场验证。

## 2026-10 arXiv cs.SD 月度候选整理

- [10 月论文分类索引（已知候选，非 505 条全量核验）](arxiv-cs-sd-2026-10.md)

- [2026 年 10 月目录逐条核验新增候选（阶段性）](arxiv-cs-sd-2026-10-verified-additions.md)：按标题和类别初筛，尚未完整核验 505 条。
