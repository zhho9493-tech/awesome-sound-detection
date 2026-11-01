# Awesome Sound Detection 🔊

A curated repository for **sound detection, acoustic anomaly detection, industrial acoustics, audio foundation models, and cross-domain AI research**.

中文 | [研究路线](roadmap.md) | [资源目录](resources/catalog.json) | [历史论文总索引](resources/historical-paper-index.md) | [贡献指南](CONTRIBUTING.md)

## 资源导航

| 方向 | 入口 | 重点 |
|---|---|---|
| 声学异常检测 | [ASD](papers/acoustic-anomaly/README.md) | DCASE、跨域泛化、Noise-aware |
| 声音事件检测 | [SED](papers/sound-event/README.md) | 分类、定位、弱监督 |
| DAS 光纤听诊 | [DAS](domains/das/README.md) | 皮带机托辊、时空一致性 |
| 听漏及泄漏 | [Leakage](domains/leakage/README.md) | 水管、气体泄漏、定位 |
| 声纹识别 | [Speaker](related/speaker-recognition/README.md) | ECAPA、Embedding、域适应 |
| 人脸识别 | [Face](related/face-recognition/README.md) | ArcFace、Sub-center、标签噪声 |
| 图像异常检测 | [Vision AD](related/visual-anomaly/README.md) | PatchCore、PaDiM、异常定位 |
| 基础模型 | [Foundation](related/foundation-models/README.md) | CLAP、BEATs、DINOv2 |

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
