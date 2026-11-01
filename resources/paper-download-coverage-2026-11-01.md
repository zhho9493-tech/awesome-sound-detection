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
