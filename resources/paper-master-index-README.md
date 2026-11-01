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
