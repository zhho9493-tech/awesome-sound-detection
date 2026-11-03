# arXiv PDF 下载链接审计

- 结构化 arXiv 论文记录：8087 条，7646 个唯一 ID。
- 结构化记录缺失 PDF 字段：**0** 条。
- 资源目录此前只有摘要页、缺少 PDF 字段：**5** 条。
- 经 arXiv 官方 PDF 文件头验证可下载：**5** 条；不可下载：**0** 条。

## 已核验条目

| arXiv ID | 论文 | 官方 PDF | 验证结果 |
|---|---|---|---|
| [2005.07143](https://arxiv.org/abs/2005.07143) | ECAPA-TDNN | [PDF](https://arxiv.org/pdf/2005.07143) | 可下载，已补齐 |
| [1801.07698](https://arxiv.org/abs/1801.07698) | ArcFace | [PDF](https://arxiv.org/pdf/1801.07698) | 可下载，已补齐 |
| [2004.00288](https://arxiv.org/abs/2004.00288) | Sub-center ArcFace | [PDF](https://arxiv.org/pdf/2004.00288) | 可下载，已补齐 |
| [2106.08265](https://arxiv.org/abs/2106.08265) | PatchCore | [PDF](https://arxiv.org/pdf/2106.08265) | 可下载，已补齐 |
| [2011.08785](https://arxiv.org/abs/2011.08785) | PaDiM | [PDF](https://arxiv.org/pdf/2011.08785) | 可下载，已补齐 |

## 口径

仅把正式收录的结构化论文记录和 `catalog.json` 中 `type=paper` 的资源作为论文；`arxiv-match-review.json` 中尚待人工确认的候选不计入缺失。PDF 可用性通过 arXiv 官方地址返回的 `%PDF` 文件签名验证。
