# Awesome Sound Detection 🔊

A curated repository for **sound detection, acoustic anomaly detection, industrial acoustics, audio foundation models, and cross-domain AI research**.

中文 | [研究路线](roadmap.md) | [资源目录](resources/catalog.json) | [历史论文总索引](resources/historical-paper-index.md) | [arXiv cs.SD 2025–2026 全量索引](resources/arxiv-cs-sd/README.md) | [PDF 链接审计](resources/arxiv-pdf-link-audit.md) | [贡献指南](CONTRIBUTING.md)

## 资源导航

| 方向 | 入口 | 重点 |
|---|---|---|
| 声学异常检测 | [ASD](papers/acoustic-anomaly/README.md) · [交互时间线](papers/acoustic-anomaly/papers-timeline.html) | DCASE、跨域泛化、Noise-aware |
| 声音事件检测 | [SED](papers/sound-event/README.md) · [交互时间线](papers/sound-event/papers-timeline.html) · [事件专题](papers/sound-event/TOPICS.md) | 12 领域、具体声源事件、分类与定位 |
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

目前共 2,145 条标题级候选，尚未完成逐篇 DOI/arXiv 身份核对和官方下载链接补全。公开仓库不包含私人 Google Drive 链接。

## 2026 年 10 月 cs.SD 月度索引

- [10 月分类候选总表（31 篇已知候选；官方月目录 505 条，尚非全量核验）](resources/arxiv-cs-sd-2026-10-audit.md)
- 六个音频方向已建立对应专题索引；同一论文以 arXiv ID 去重，已有精选论文保留原条目。

- [十月 cs.SD 逐条核验进度与新增候选](resources/arxiv-cs-sd-2026-10-verification-progress.md)：已审查目录序号 1–150、201–250，共 200/505；40 篇额外候选已分方向推送。尚不是全量审查。
