# Awesome Sound Detection 🔊

> **新入口 · Knowledge Portal：** [交互式研究导航](portal/index.html) ｜ [架构与迁移规范](docs/KNOWLEDGE_ARCHITECTURE.md) ｜ [多维分类数据](resources/research-taxonomy.json)。当前为第一阶段兼容式重构，原始论文与历史页面保持不变。建议通过 `python3 scripts/preview_timelines.py` 本地预览门户（打开 `/portal/`）。
> **全库论文检索（第二阶段）：** [论文探索页面](portal/library.html) · [自动构建脚本](scripts/build_paper_discovery.py) · [定时刷新工作流](.github/workflows/build-paper-discovery.yml)。论文索引按官方 DOI/arXiv 明确编号进行保守合并，未进行标题级强制去重。

> **技术洞察（第三阶段）：** [交互式论文时间线与趋势证据](portal/insights.html) · [论文详情与相似方向关联](portal/library.html) · [Pages 部署工作流](.github/workflows/publish-research-portal.yml)。Pages 仅发布经字段白名单处理的数据，**不直接部署包含私人云盘信息的原始主索引**；首次部署还需在仓库 Settings → Pages 中选用 GitHub Actions。
> **各方向论文详情（专题目录）：** [打开逐篇论文列表](portal/topic.html?topic=das) · 支持切换 DAS、泄漏、ASD、SED、炸街车、OOD、低 SNR 等应用与方法专题，并逐篇查看标题、作者、日期、摘要、分类依据、来源与 PDF。可按年份、来源、关键词筛选，分页展示及导出 CSV；关键词规则结果标记为待复核候选。

> **逐篇论文总结：** 已为每个专题和全库论文详情添加结构化的「研究目标 / 方法要点 / 作者报告结果 / 证据限制」字段。内容基于公开摘要提取；缺少摘要的记录显示待补充，不代表全文审核完成。参见 [总结字段规范](docs/PAPER_SUMMARY_CONTRACT.md)。

A curated repository for **sound detection, acoustic anomaly detection, industrial acoustics, audio foundation models, and cross-domain AI research**.

中文 | [研究路线](roadmap.md) | [资源目录](resources/catalog.json) | [历史论文总索引](resources/historical-paper-index.md) | [arXiv cs.SD 2025–2026 全量索引](resources/arxiv-cs-sd/README.md) | [缺失 PDF 复核](resources/public-pdf-audit.md) | [贡献指南](CONTRIBUTING.md)

## 一键本地查看交互页面

- macOS：双击 [`查看论文时间线.command`](查看论文时间线.command)，将自动启动本地服务并打开全部类别的预览导航。
- 命令行：运行 `python3 scripts/preview_timelines.py`。
- 默认地址为 `http://127.0.0.1:8765/`；若端口被占用会自动选择下一个可用端口。关闭启动预览的终端窗口即可停止服务。

## 批量下载论文

- 运行 `python3 tools/paper-downloader/paper_downloader.py`，扫描并下载仓库中所有提供公开下载地址的论文。
- 使用 `--list-only` 可先查看下载清单，使用 `--limit 10` 可先进行小批量验证。
- 详细参数、断点续传与失败报告说明见 [Paper Downloader](tools/paper-downloader/README.md)。

## 资源导航

### 深度学习通用问题

- **[通用问题专题总览](general-problems/README.md)**：跨域泛化、少样本、长尾、噪声标签、开放集/OOD、持续学习、半/弱监督、对抗鲁棒性、校准与不确定性。
- **[OOD（分布外检测）独立专题](general-problems/ood/README.md)**：近一年论文、技术趋势、DAS 适用性及[论文时间线](general-problems/ood/TIMELINE.md)。
- **[经典论文机器可读索引](general-problems/classic-papers.json)**：按问题方向整理经典解决方案及公开 PDF，可由 Paper Downloader 批量下载。

| 方向 | 入口 | 重点 |
|---|---|---|
| 声学异常检测 | [ASD](papers/acoustic-anomaly/README.md) · [交互时间线](papers/acoustic-anomaly/papers-timeline.html) | DCASE、跨域泛化、Noise-aware |
| 声音事件检测 | [SED](papers/sound-event/README.md) · [交互时间线](papers/sound-event/papers-timeline.html) · [事件专题](papers/sound-event/TOPICS.md) | 12 领域、具体声源事件、分类与定位 |
| 低信噪比 SED | [专题](papers/sound-event/low-snr/README.md) · [技术趋势](papers/sound-event/low-snr/TRENDS.md) · [论文时间线](papers/sound-event/low-snr/TIMELINE.md) | 2025–2026 噪声鲁棒检测、目标分离、Noise-aware |\n| 炸街车检测 | [专题](papers/sound-event/transportation/noisy-vehicle/README.md) · [技术趋势](papers/sound-event/transportation/noisy-vehicle/TRENDS.md) · [时间线](papers/sound-event/transportation/noisy-vehicle/papers-timeline.html) | 改装排气事件检测、车辆声源归属、现场验证 |
| DAS 光纤听诊 | [DAS](domains/das/README.md) · [交互时间线](domains/das/papers-timeline.html) | 皮带机托辊、时空一致性 |
| 听漏及泄漏 | [Leakage](domains/leakage/README.md) · [交互时间线](domains/leakage/papers-timeline.html) | 水管、气体泄漏、定位 |
| 声纹识别 | [Speaker](related/speaker-recognition/README.md) · [交互时间线](related/speaker-recognition/papers-timeline.html) | ECAPA、Embedding、域适应 |
| 人脸识别 | [Face](related/face-recognition/README.md) · [交互时间线](related/face-recognition/papers-timeline.html) | ArcFace、Sub-center、标签噪声 |
| 图像异常检测 | [Vision AD](related/visual-anomaly/README.md) · [交互时间线](related/visual-anomaly/papers-timeline.html) | PatchCore、PaDiM、异常定位 |
| 基础模型 | [Foundation](related/foundation-models/README.md) · [交互时间线](related/foundation-models/papers-timeline.html) | CLAP、BEATs、DINOv2 |
| 跨领域迁移 | [迁移矩阵](cross-domain/transfer-matrix.md) · [交互时间线](cross-domain/papers-timeline.html) | 域泛化、迁移学习、多模态迁移 |

## 技术趋势与证据链

- **[技术趋势总地图：8 个研究方向 / 51 个可点击详情页](resources/technology-trend-map.md)**
- 每个方向的「技术趋势」条目均可打开独立页面，查看判断依据、分析链路、适用边界与验证实验。
- 注意：部分证据仅支持方法背景，未构成系统文献计量或在 DAS 工业现场的实证结论。

## 横向资源

- [历史论文总索引](resources/historical-paper-index.md) · [Google Drive 统一扫描索引](resources/drive-unified-scanned-index.md)
- [DAS 皮带机企业动态时间线](industry/das-conveyor-timeline.md) · [行业动态](industry/README.md)
- [跨领域可迁移技术矩阵](cross-domain/transfer-matrix.md)
- [开源代码](code/README.md) · [数据集](datasets/README.md)
- [实验复现记录](experiments/README.md)
- [论文模板](templates/paper-template.md) · [行业信息模板](templates/industry-item-template.md) · [实验模板](templates/experiment-template.md)

## 精选入口

- [DCASE](https://dcase.community/) · [AudioSet](https://research.google.com/audioset/)
- [LAION-CLAP](https://github.com/LAION-AI/CLAP) · [BEATs](https://github.com/microsoft/unilm/tree/master/beats)
- [ECAPA-TDNN](https://arxiv.org/abs/2005.07143) · [ArcFace](https://arxiv.org/abs/1801.07698)
- [Sub-center ArcFace](https://arxiv.org/abs/2004.00288)
- [PatchCore](https://arxiv.org/abs/2106.08265) · [PaDiM](https://arxiv.org/abs/2011.08785)

## 资源状态

**verified-link** 链接经核查；**to-reproduce** 待复现；**reproduced** 已有复现记录；**applied** 已经在规定业务条件下验证；**hypothesis** 未验证的迁移假设。

不要将论文作者报告的结果混同于本项目实测效果。资源内容按原作者许可使用；仓库本身遵循 [MIT](LICENSE)。


## 统一论文知识库

来自 Google Drive「技术调研」的论文主索引现已整合为**一个文件名级去重的主数据库**，减少轮次索引碎片化：

- [统一论文数据库（JSON）](resources/paper-master-index.json)
- [论文下载覆盖情况：arXiv / Google Drive / 未匹配](resources/paper-download-coverage-2026-11-01.md)
- [论文表格（CSV）](resources/paper-master-index.csv)
- [字段说明、分类统计与核验限制](resources/paper-master-index-README.md)
- [目录扫描覆盖报告](resources/technical-research-coverage-2026-11-01.md)

主索引已在 2026-11-12 合并云端“论文仓库”增量；其中 Google Drive 链接按用户要求保留，访问权限沿用云盘设置。尚未完成逐篇 DOI/arXiv 身份核对和官方下载链接补全。

- [2026-11-12 云端论文仓库增量：按现有类别整理并提供 Drive 下载链接](resources/google-drive-paper-library-2026-11-12.md)

## 2026 年 10 月 cs.SD 月度索引

- [10 月分类候选总表（31 篇已知候选；官方月目录 505 条，尚非全量核验）](resources/arxiv-cs-sd-2026-10-audit.md)
- 六个音频方向已建立对应专题索引；同一论文以 arXiv ID 去重，已有精选论文保留原条目。

- [十月 cs.SD 逐条核验进度与新增候选](resources/arxiv-cs-sd-2026-10-verification-progress.md)：已审查目录序号 1–150、201–250，共 200/505；40 篇额外候选已分方向推送。尚不是全量审查。
