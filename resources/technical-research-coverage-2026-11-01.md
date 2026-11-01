# Google Drive / 我的云端硬盘 / 技术调研 — 递归目录覆盖报告

**核查日期**：2026-11-01

## 纠正此前遗漏

之前的全盘 PDF 关键词搜索并未限定到「技术调研」文件夹树，不能代表该目录完成入库。现在已根据实际文件夹 ID，从「技术调研」根目录展开其 17 个一级目录，进一步扫描其「工作时间线」「综述文章」「核心技术点」等中间层，以及 DCASE 六个年度文件夹中的各 Task 文件夹。

| 路径 | 扫描结果 | GitHub |
|---|---|---|
| 异音检测/工作时间线 | **875 文件，456 个文件名去重标题** | [完整标题索引](../papers/acoustic-anomaly/drive-technical-research-anomaly-full-index.md) |
| 声音分类/工作时间线 | 1000 文件，507 归一标题 | [技术调研索引 A](technical-research-folder-index-a.md) |
| 声纹识别/工作时间线 | 357 文件，180 归一标题 | [技术调研索引 A](technical-research-folder-index-a.md) |
| 跨域检测/工作时间线 | 420 文件，208 归一标题 | [技术调研索引 A](technical-research-folder-index-a.md) |
| 半监督训练/工作时间线 | 30 文件，15 归一标题 | [技术调研索引 A](technical-research-folder-index-a.md) |
| Omni/工作时间线 | 364 文件，182 归一标题 | [技术调研索引 B](technical-research-folder-index-b.md) |
| ALLM/技术时间线 | 440 文件，211 归一标题 | [技术调研索引 B](technical-research-folder-index-b.md) |
| 音频基座/工作时间线 | 203 文件，99 归一标题 | [技术调研索引 B](technical-research-folder-index-b.md) |
| 综述文章/工作时间线 | 106 文件，52 归一标题 | [技术调研索引 A](technical-research-folder-index-a.md) |
| DCASE 2020–2025 Task 子目录 | 各 Task 已分别枚举，参见下方 | [任务索引 A](../papers/acoustic-anomaly/drive-dcase-task-inventory-a.md) · [任务索引 B](../papers/acoustic-anomaly/drive-dcase-task-inventory-b.md) |

其他一级分支，包括语音增强、音频数据集、少数据量训练、可解释性、音频生成、数据扩增、设备运维等，亦见索引 A/B/C。跨域检测「平坦最小值」已进入索引 C。

## 当前完成与局限

- 已完成：递归发现目标目录已识别的子文件夹，逐目录列出文件名，部分目录按规范标题合并 PDF 与总结，建立 GitHub 分方向入口。
- 尚未完成：**每篇 PDF 正文解析、作者/DOI/arXiv 核实、官方 PDF 下载链接和代码链接补齐、跨目录唯一论文统计。**
- **扫描边界风险**：声音分类/工作时间线返回恰好 1000 个文件，虽然此查询未返回下一页 token，仍可能涉及服务端数量上限，故不宣称该文件夹已严格证明 100% 全覆盖。
- **分类边界**：DCASE 含多种任务，按官方 Task 分类精细分流尚未完成；A/B/C 为目录级原始书目快照，不等于每条论文已进唯一标准化主数据库。
- 不公开任何私人 Google Drive 文件 ID、URL、PDF 正文或私有总结。

## 建议的最终验收方式

为每个论文建立 `doi || arxiv_id || normalized_title` 主键，提供 `source_path`（仅内部，不发布）、主领域、关联标签、公开 PDF、官方代码、状态，生成 CSV/JSON 统一知识库并自动输出未覆盖差异清单。