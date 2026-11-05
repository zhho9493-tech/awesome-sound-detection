# Paper Downloader

扫描仓库中的结构化论文索引及 Markdown/HTML/CSV 页面，去重并下载所有明确提供下载地址的论文。

## 快速使用

在仓库根目录运行：

```bash
python3 tools/paper-downloader/paper_downloader.py
```

论文默认保存到 `downloads/papers/`。目录中同时生成：

- `download-report.json`：汇总数量、每篇论文状态及失败原因；
- `download-report.csv`：便于用表格筛选失败记录；
- `*.pdf.part`：下载中断时保留的临时文件，下次运行自动尝试续传。

## 常用参数

```bash
# 只查看将要下载的论文，不访问网络
python3 tools/paper-downloader/paper_downloader.py --list-only

# 先下载 10 篇验证环境
python3 tools/paper-downloader/paper_downloader.py --limit 10

# 指定目录、并发数和输出位置
python3 tools/paper-downloader/paper_downloader.py \
  --source papers/sound-event \
  --workers 8 \
  --output /path/to/papers

# 企业网络使用自定义 CA 证书包
python3 tools/paper-downloader/paper_downloader.py --ca-bundle /path/to/ca-bundle.pem

# 重新下载已存在的有效 PDF
python3 tools/paper-downloader/paper_downloader.py --overwrite
```

完整参数可通过 `--help` 查看。

## 识别与安全规则

- 读取 JSON 中的 `pdf`、`pdf_url`、`download_url`、`drive_download_url` 字段；
- 从 Markdown、HTML、CSV 和 TSV 中提取 arXiv 摘要/PDF、`.pdf` 及明确下载链接；arXiv 摘要链接会转换为官方 PDF 地址；
- 同一 arXiv ID 只下载一次，其他链接按规范化 URL 去重；
- 下载完成后检查文件头是否为 PDF，网页错误页不会被误存为论文；
- 已存在且有效的 PDF 默认跳过；下载失败不会删除 `.part` 文件；
- Python 运行环境证书链异常时会自动回退到系统 `curl`（若已安装），仍会校验 PDF；
- 工具不会下载普通网页，也不会尝试绕过需要登录或无公开权限的下载页面。

部分 Google Drive 文件可能需要登录、确认页或额外权限，此类记录会进入失败报告，便于后续人工处理。
