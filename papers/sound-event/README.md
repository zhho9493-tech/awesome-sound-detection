# Sound Event Detection / 声音事件检测

多标签分类、事件开始结束时间、弱监督与事件级聚合。

- [DCASE](https://dcase.community/)
- [AudioSet](https://research.google.com/audioset/)

建议记录 event-based F1、PSDS、检测延迟及目标噪声条件。

## 近一年 arXiv 声音分类精选（2025-10-31—2026-10-31）

- [论文目录、方法解读与官方 PDF 下载](arxiv-sound-classification-2025-2026.md)
- [结构化元数据 JSON](arxiv-sound-classification-2025-2026.json)

当前精选 5 篇，非穷尽索引。重点为领域增量学习、层级声音分类和元数据融合。

## 技术时间线

| 时间 | 技术主线 | 代表性变化 |
|---|---|---|
| 2017–2021 | CNN/CRNN + 弱监督 SED | 从 clip 分类逐渐扩展到事件起止时间检测 |
| 2021–2024 | Transformer / Conformer / 大规模预训练 | 通过更强时序建模和预训练改善长时依赖与少样本能力 |
| 2024–2025 | 层级分类、检索增强、多标签结构化输出 | 处理细粒度类别、相近声音和复杂事件关系 |
| 2026-06 | Domain-Agnostic Incremental Learning | DCASE 2026 将“跨域顺序学习、不能回看全部旧数据”明确为任务 |
| 2026-06 | Domain-specific Experts + Prototype | 冻结专家、原型分类与生成回放用于降低跨域遗忘 |
| 2026-07 | Hierarchy-Aware Multi-Branch | CLAP + 多分支 + 层级分类器 + KNN 后处理 |
| 2026-09 | Parameter Isolation / Domain Experts | 参数隔离与专家路由进一步强化持续学习能力 |
| 2026-10 | Metadata-aware Gating | 音频与场景/字段元数据融合，但需防止 domain shortcut |

## 技术趋势

1. **[单任务分类 → 持续/增量学习](trends/trend-01.md)**：新项目、新类别、新环境加入时，不再默认可以全量重训。
2. **[单一分类头 → 层级结构 + Prototype + Retrieval](trends/trend-02.md)**：更适合“一级异常/二级原因/other”这类工业多级分类。
3. **[纯音频输入 → 音频 + 元数据](trends/trend-03.md)**：项目、位置、工况等信息有价值，但必须严格做项目隔离验证，避免泄漏。
4. **[统一网络 → Domain-specific Experts / MoE](trends/trend-04.md)**：不同工况、设备或项目可使用共享 backbone + 局部专家。
5. **[离线分类 → 事件级决策](trends/trend-05.md)**：持续时间、开始/结束、重复周期和跨窗口一致性越来越重要。
6. **[静态类别集合 → Open-world / Class-incremental](trends/trend-06.md)**：未来更强调新增类别、unknown、拒识和历史类别不遗忘。

## 当前判断 / 待关注

- 对工业异常声最可直接迁移的是：**Prototype + Domain Experts + 层级分类 + 元数据门控**。
- 最关键实验应是“新增项目/新增类别时，旧类别性能是否保持”，而不是只看单次训练最优结果。
- 新论文加入后，优先判断其是否改变持续学习、层级分类或元数据融合三条趋势。

## 2026-11-02 cs.SD 周度论文更新

- [本周新收录论文、分类关联及 arXiv PDF](arxiv-cs-sd-week-2026-11-02.md)
- 收录按现有研究方向筛选，属于待复现/待全文分析资料；相关结论不代表已在工业现场验证。
