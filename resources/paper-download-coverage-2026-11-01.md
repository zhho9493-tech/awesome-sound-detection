# 论文公开来源与网盘下载核验报告

生成日期：2026-11-01。范围：GitHub 现有统一主数据库中的 **2145** 条标题级候选。

| 指标 | 数量 |
|---|---:|
| 主索引候选论文 | 2145 |
| 已匹配 Google Drive PDF 文件页 | 2139 |
| 已填 arXiv 官方论文编号 | 4 |
| 已添加可尝试的 Google Drive 下载入口 | 2138 |
| 完全缺少 PDF 入口 | 3 |

> **重要区别**：已匹配网盘 PDF ≠ 已核实这篇论文不存在于 arXiv。全库尚未逐篇完成 arXiv API 查询。对于未核实 arXiv 身份的论文，已先回填用户明确请求的网盘文件入口。Google Drive 下载入口受文件原有权限、浏览器登录状态和 Google 限制影响，**并非公开匿名可下载保证**。

## 未能与网盘 PDF 明确配对的条目

- `title-04b72369` — A Survey on Speech Large Language Models for Understanding
- `title-645035ab` — SOUND EVENT RECOGNITION IN A SMART CITY SURVEILLANCE CONTEXT
- `title-4d88982b` — Sound of Guns- Digital Forensics of Gun Audio Samples meets Artificial Intelligence

## 文件字段

- `public_url`, `pdf_url`, `arxiv_id`：已独立匹配的 arXiv 论文身份。
- `drive_file_url`：从 Google Drive 搜索结果获得的原始文件页面。
- `drive_download_url`：基于已确认文件 ID 的 Google Drive 下载端点；不改变共享设置。
- `download_url`：优先 arXiv 官方 PDF，其次网盘下载端点。
- `verification_status`：`official-url-verified` 或 `drive-file-matched`；不代表论文 DOI/作者等其他字段都已核实。

## 后续校验

保留使用 arXiv API 的逐条精确比对工作流，对新匹配到 arXiv 的论文优先写官方 PDF，同时保留已验证的原始 Drive 文件页面，不要将未匹配视为不在 arXiv。

## 2026-11-01 补充人工抽样核验（实时查询）

以下为对主索引中具体论文标题进行的独立 arXiv 标题核查，不代表对全库完成核验：

| 主索引论文标题 | arXiv 论文页 | 官方 PDF | 核验结论 |
|---|---|---|---|
| 3D-LLaVA: Towards Generalist 3D LMMs with Omni Superpoint Transformer | https://arxiv.org/abs/2501.01163 | https://arxiv.org/pdf/2501.01163 | 标题一致；原索引已有链接 |
| A Causal Framework to Unify Common Domain Generalization Approaches | https://arxiv.org/abs/2307.06825 | https://arxiv.org/pdf/2307.06825 | 标题一致；原索引未填写 arXiv PDF，待主索引补写 |
| 6DoF SELD: Sound Event Localization and Detection Using Microphones and Motion Tracking Sensors on self-motioning human | https://arxiv.org/abs/2403.01670 | https://arxiv.org/pdf/2403.01670 | 标题一致；原索引未填写 arXiv PDF，待主索引补写 |

**注意**：本次只完成以上三篇的外部 arXiv 标题验证和核查报告写入，未修改 2,145 条主索引记录；其余尚不能被标为“不在 arXiv”。Google Drive 下载入口已按上述覆盖报告预先回填；链接访问仍取决于文件权限。仓库中的自动 arXiv 工作流尚未发现 `resources/arxiv-lookup-state.json` 进度文件，因此不能据此认定自动批量核验已经执行成功。

## 全量 arXiv 自动查询完成后的最新状态（2026-11-01）

本节为完成工作流后直接读取 `resources/arxiv-lookup-state.json` 和 `resources/arxiv-match-review.json` 所得；**覆盖本文前面的初始统计**。

| 统计项 | 当前数量 |
|---|---:|
| 标题级候选记录 | 2,145 |
| 已完成 arXiv API 查询并记为 checked | 2,145 |
| 已记录官方 arXiv PDF | 1,061 |
| 未确认 arXiv PDF | 1,084 |
| 需要人工复核的近似候选 | 52 |
| 当前查询错误记录 | 0 |
| 最后一批查询尝试 | 41 |
| 最后一批新增匹配 | 27 |

**解释**：`checked` 只表明自动标题检索已处理过该条，不表示论文一定不存在于 arXiv。尤其对于被截断的标题、作者版本差异或非 arXiv 发表论文，自动检索可能漏检。52 条人工复核项见 [arxiv-match-review.json](arxiv-match-review.json)，不应未经人工确认便当作官方匹配。主数据库中的 `download_url` 优先指向确认的 arXiv PDF；未确认者继续保留已有 Google Drive 入口（能否下载取决于现有文件权限）。

### 下一步核验重点

1. 逐条检查 52 条相似候选，标题截断的条目特别需要确认 DOI、作者或原 PDF 首页，防止误配。
2. 对其余没有 arXiv 匹配的条目补充 DOI、出版社、OpenReview 等官方来源检索；没有 arXiv 不等于没有合法下载来源。
3. 对 Google Drive 下载链接单独进行登录/权限校验，不能以链接字段非空替代可下载性验证。

