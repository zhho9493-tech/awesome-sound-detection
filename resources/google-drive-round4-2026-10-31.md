# Google Drive 论文归总 · 四轮进度与统一导航

更新 2026-10-31。公开仓库只收录论文公开元信息；不暴露私人 Google Drive 文件 URL、PDF 原文或内部笔记。

| 轮次 | 分类记录 | 分类目录数 | 详情 |
|---|---:|---:|---|
| round1 | 33 | 7 | [查看](../resources/google-drive-import-2026-10-31.md) |
| round2 | 23 | 6 | [查看](../resources/google-drive-round2-2026-10-31.md) |
| round3 | 22 | 5 | [查看](../resources/google-drive-round3-2026-10-31.md) |
| round4 | 16 | 4 | [查看](../resources/google-drive-round4-2026-10-31.md) |

累计 **94 条分类记录（33 + 23 + 22 + 16）**。此数不是唯一论文量，因为跨目录和跨轮次可能重复；尚未完成全面 DOI/arXiv 级别去重，切勿据此宣称 94 篇不同论文。

## 第四轮新增方向

- [跨项目泛化与开放集 6 条](../cross-domain/drive-library-round4.md)
- [工业声学/皮带机原型学习 5 条](../papers/acoustic-anomaly/drive-library-round4.md)
- [泄漏识别 2 条](../domains/leakage/drive-library-round4.md)
- [声纹与音频基础模型自适应 3 条](../related/speaker-recognition/drive-library-round4.md)

## 数据清洗的正确下一步

1. **统一主键**：优先 DOI，次选 arXiv ID，最后使用规范标题哈希（临时主键）。
2. **同一论文多标签**：主分类仅有一个，关联分类在数组中表示；多个标签不生成多个文献实体。
3. **溯源级别**：`filename-only` → `metadata-checked` → `official-url-verified` → `code-verified` → `reproduced`。
4. **补全下载**：只在 arXiv、出版商或合法开放获取存储库匹配后填公开 PDF URL。网盘私人 URL 不得同步。
5. **增量更新**：后续轮次应将新增唯一 ID 合并进主索引，并保留每次导入的变更记录。

目前完成的是初步论文发现和分类，不是全量分页同步或自动定时同步。