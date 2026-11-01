# 统一论文主索引

建立日期 2026-11-01。本索引合并技术调研目录扫描与 DCASE 任务索引中的标题，包含 **2145** 条**文件名级唯一候选**，合并前 2743 行。**不能当作经过 DOI 核验的真实唯一论文数量。**

- [完整 JSON](paper-master-index.json)
- [CSV](paper-master-index.csv)
- [目录扫描覆盖报告](technical-research-coverage-2026-11-01.md)

字段：`id`（临时标题哈希）、`title`、`primary_category`、`related_categories`、`sources`（仅公开的技术方向名称）、`doi`、`arxiv_id`、`public_url`、`pdf_url` 和 `verification_status`。未核实资料保留 null，绝不使用私人 Drive URL 充当 PDF 链接。

## 分类统计
- cross-domain: 164
- acoustic-anomaly: 392
- other: 574
- foundation-models: 350
- speaker-recognition: 192
- sound-event: 455
- leakage: 7
- das: 11

## 仍待完成

1. 逐篇读取原文，按 DOI/arXiv ID 合并标题变体、补齐作者年份摘要与官方下载链接。
2. 使用规范 ID 替换临时标题哈希并维护旧 ID 映射。
3. 编写自动增量同步和校验脚本；确保跨项目私人信息不进入公开仓库。
4. 完成尚待检查的 Google Drive 文件及源目录中所有附件的内容核查。

## arXiv 下载链接自动核验

- [自动核验程序](../scripts/verify_arxiv_index.py)：以论文标题检索 arXiv Atom API，标准化标题相似度≥0.96 且不存在竞争候选才自动写入官方 abs / PDF 地址。
- [GitHub Actions 工作流](../.github/workflows/verify-arxiv-index.yml)：可手动触发；配置了每日分批处理（60 条/次），失败会保留待重试状态。
- [人工复核清单](arxiv-match-review.json)：仅工作流实际运行且产生疑似匹配后创建。
- [检查进度状态](arxiv-lookup-state.json)：仅工作流实际运行后创建，不能将配置完成理解为已检查完毕。

**最新实际写入（2026-11-01）：** 主库 2,145 条中已确认 2 条对应的 arXiv PDF。其余条目的 arXiv 存在性仍待查询；不把没有搜索到等同于“不存在”。此工作流是否实际成功运行须查看 GitHub Actions 页面。
