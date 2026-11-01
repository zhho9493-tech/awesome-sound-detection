# Face Recognition / 人脸识别

- [ArcFace](https://arxiv.org/abs/1801.07698) — 角度间隔损失
- [Sub-center ArcFace](https://arxiv.org/abs/2004.00288) — 多子中心和噪声标签
- [InsightFace](https://github.com/deepinsight/insightface) — 官方生态实现

声学迁移：标签噪声、多模式异常、类间距离、嵌入空间校准与增量类别。

## 技术时间线

| 时间 | 技术主线 | 对声学迁移的意义 |
|---|---|---|
| 2015–2017 | Softmax → Metric Learning | 从类别概率转向可度量 embedding |
| 2018 | ArcFace | 角度间隔直接优化 embedding 类间边界 |
| 2020 | Sub-center ArcFace | 一个类别多个子中心，兼顾类内多模态和噪声标签 |
| 2021–2024 | 大规模清洗、难样本、质量感知 | 关注标签质量、样本可靠性、低质量输入 |
| 2024–2026 | Foundation features / Parameter-efficient adaptation | 预训练大模型与轻量适配开始进入识别系统 |
| 下一阶段 | Open-world / Incremental identity | 新类别扩展、未知类别拒识和持续更新更重要 |

## 技术趋势

1. **分类 logits → Embedding space**：识别问题越来越依赖空间结构而非单次 softmax。
2. **单中心类分布 → 多子中心**：天然适合工业异常中“一类多种声学模式”。
3. **默认标签正确 → 质量/噪声感知**：高权重难样本可能是难例，也可能是错标，需要额外判断。
4. **固定类别 → 增量类别**：新身份/新类别加入时，冻结 backbone + 新原型/权重成为重要方向。
5. **统一阈值 → 质量感知/校准阈值**：输入质量和域差异决定阈值不应完全固定。
6. **黑盒错误 → Embedding 可视化与样本审计**：聚类、近邻、margin、AUM 等可辅助标签治理。

## 当前判断 / 对工业声学迁移

- ArcFace/Sub-center 仍是工业 embedding 分类器非常强的参考范式。
- 最值得继续追踪：增量类别、噪声标签、多中心表示、质量感知阈值。
- 新增论文后，需判断是否改变“多中心 / 标签质量 / 增量类别 / 校准”四条主线。
