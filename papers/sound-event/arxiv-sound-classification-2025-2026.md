# arXiv 声音分类论文精选：2025-10-31—2026-10-31

更新：2026-10-31。覆盖声音事件分类、异构声音分类、增量领域学习、层级分类和元数据融合。**这是经过搜索选出的 5 篇相关论文，不是此时间段全部论文。**

| 首发日期 | 论文 | 研究主题 | PDF 下载 |
|---|---|---|---|
| 2026-10-10 | [FAM-gate: field-aware metadata attention with prior-constrained vector gating for audio classification](https://arxiv.org/abs/2610.14673) | metadata fusion | [PDF](https://arxiv.org/pdf/2610.14673) |
| 2026-09-13 | [Parameter isolation with domain-specific experts for incremental audio classification](https://arxiv.org/abs/2609.14730) | domain incremental | [PDF](https://arxiv.org/pdf/2609.14730) |
| 2026-07-02 | [A Multi-Branch Hierarchy-Aware Framework for Heterogeneous Audio Classification](https://arxiv.org/abs/2607.01974) | hierarchical classification | [PDF](https://arxiv.org/pdf/2607.01974) |
| 2026-06-22 | [Domain-incremental audio classification using domain-specific experts and prototype classifier](https://arxiv.org/abs/2606.22952) | prototype / domain incremental | [PDF](https://arxiv.org/pdf/2606.22952) |
| 2026-06-01 | [Domain-Agnostic Incremental Learning for Sound Classification. A DCASE 2026 Challenge task](https://arxiv.org/abs/2606.02173) | benchmark / domain incremental | [PDF](https://arxiv.org/pdf/2606.02173) |

## 方法与可迁移启发

### 1. FAM-gate: field-aware metadata attention with prior-constrained vector gating for audio classification

- arXiv: [2610.14673](https://arxiv.org/abs/2610.14673)
- 日期：2026-10-10
- 类型：metadata fusion
- 论文方法摘要：音频与多字段元数据的受限门控融合；BSD10k/BSD35k/FSD50K
- 工业声学/DAS 迁移假设：项目ID、采集条件等元数据辅助分类，但需防止项目捷径
- 官方 PDF 下载：https://arxiv.org/pdf/2610.14673
- 状态：文献信息已按 arXiv 搜索结果核对；未复现，未进行 PDF 文件下载与代码验证。

### 2. Parameter isolation with domain-specific experts for incremental audio classification

- arXiv: [2609.14730](https://arxiv.org/abs/2609.14730)
- 日期：2026-09-13
- 类型：domain incremental
- 论文方法摘要：冻结历史专家、生成回放与跨域特征生成；DCASE 2026 Task 7
- 工业声学/DAS 迁移假设：跨项目增量扩展与遗忘控制
- 官方 PDF 下载：https://arxiv.org/pdf/2609.14730
- 状态：文献信息已按 arXiv 搜索结果核对；未复现，未进行 PDF 文件下载与代码验证。

### 3. A Multi-Branch Hierarchy-Aware Framework for Heterogeneous Audio Classification

- arXiv: [2607.01974](https://arxiv.org/abs/2607.01974)
- 日期：2026-07-02
- 类型：hierarchical classification
- 论文方法摘要：CLAP、声学多分支、层级分类器与 KNN 后处理；DCASE 2026 Task 1
- 工业声学/DAS 迁移假设：多层级异常类别及检索复核
- 官方 PDF 下载：https://arxiv.org/pdf/2607.01974
- 状态：文献信息已按 arXiv 搜索结果核对；未复现，未进行 PDF 文件下载与代码验证。

### 4. Domain-incremental audio classification using domain-specific experts and prototype classifier

- arXiv: [2606.22952](https://arxiv.org/abs/2606.22952)
- 日期：2026-06-22
- 类型：prototype / domain incremental
- 论文方法摘要：冻结专家特征、原型分类器、生成回放；DCASE 2026 Task 7
- 工业声学/DAS 迁移假设：多项目原型分类与持续学习
- 官方 PDF 下载：https://arxiv.org/pdf/2606.22952
- 状态：文献信息已按 arXiv 搜索结果核对；未复现，未进行 PDF 文件下载与代码验证。

### 5. Domain-Agnostic Incremental Learning for Sound Classification. A DCASE 2026 Challenge task

- arXiv: [2606.02173](https://arxiv.org/abs/2606.02173)
- 日期：2026-06-01
- 类型：benchmark / domain incremental
- 论文方法摘要：三域顺序学习的声音分类任务与基线
- 工业声学/DAS 迁移假设：跨项目泛化和不能回看原始数据时的基准设计
- 官方 PDF 下载：https://arxiv.org/pdf/2606.02173
- 状态：文献信息已按 arXiv 搜索结果核对；未复现，未进行 PDF 文件下载与代码验证。


## 优先实验建议

1. **跨项目持续学习**：以 2606.02173 为任务基线，对照冻结专家、原型分类和参数隔离（2606.22952、2609.14730）。
2. **多级分类**：基于 2607.01974 评估层级分类头和 Embedding 检索后处理。
3. **元数据鲁棒性**：基于 2610.14673 设计元数据引导的辅助门控；必须在项目隔离的验证集防范数据泄漏。

注：`https://arxiv.org/pdf/ID` 是 arXiv 官方 PDF 地址。实验收益属于研究假设，非已验证性能。
