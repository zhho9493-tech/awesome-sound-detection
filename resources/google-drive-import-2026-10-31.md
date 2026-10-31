# Google Drive 论文收藏归总（首批）

更新：2026-10-31。

## 目的

将 Google Drive 中的论文 PDF 与 Markdown 论文总结作为**私人资料源**，在公开 GitHub 中仅保留不敏感的论文题名及研究方向索引。未经核实不披露网盘文件 ID、私人下载链接、总结正文或内部项目内容。

| 方向 | 已初步归类（去重题名） | GitHub 索引 |
|---|---:|---|
| 工业声学异常检测 | 7 | [查看](../papers/acoustic-anomaly/drive-library-index.md) |
| 声音事件检测/分类 | 5 | [查看](../papers/sound-event/drive-library-index.md) |
| DAS 分布式光纤 | 6 | [查看](../domains/das/drive-library-index.md) |
| 声纹识别 | 5 | [查看](../related/speaker-recognition/drive-library-index.md) |
| 音频/工业基础模型 | 4 | [查看](../related/foundation-models/drive-library-index.md) |
| 视觉异常与跨域 | 3 | [查看](../related/visual-anomaly/drive-library-index.md) |
| 跨领域方法 | 3 | [查看](../cross-domain/drive-library-index.md) |

**合计 33 条首批初步归类论文题名**。此数字不代表整个云盘的论文总量，也不表示逐篇 DOI/arXiv 元数据已经核验。Google Drive 中还存在年度文献清单和大量摘要文件，后续需要进一步增量扫描。

## 数据质量与下一步

1. 读取 PDF 首页面/文献摘要，识别作者、题名、年份、DOI/arXiv ID。
2. 利用 DOI/arXiv ID 去重；同论文 PDF 和 Markdown 总结建立关联，但不公开私有链接。
3. 查询合法公开的论文主页、PDF 下载及官方代码。
4. 分类分支维护机器可读索引、核验状态及与工业声学任务相关的实验假设。
5. 所有发布到 GitHub 的信息均应适合公开；不把 Drive 共享链接伪装成公网下载。

## 状态

这是**首批入库**，不是 Google Drive 全量同步，也不是自动双向同步。