# 炸街车检测 / Noisy Vehicle & Modified-Exhaust Sound Detection

> 更新：2026-11-10。范围：声学识别异常响亮车辆、疑似改装排气声、排气回火声、道路多车声源归属与事件级告警。**“声学疑似”不等于违法判定**；执法需满足当地声级、工况、设备计量和证据链规范。

[交通与运输](../README.md) · [SED 专题导航](../../TOPICS.md) · [技术趋势](TRENDS.md) · [论文时间线](papers-timeline.html) · [机器可读时间线](timeline.json) · [数据集与代码](RESOURCES.md) · [近一年 arXiv cs.SD 筛选](arxiv-cs-sd-2025-11-to-2026-11.md) · [历史补充 8 篇](HISTORICAL-RELATED-PAPERS.md)

## 一句话技术主线
**一般交通声分类 → 车辆过车声与多车检测 → 疑似改装排气声事件级定位 → 真实路段跨域验证与声源归属。**

## 近一年 arXiv cs.SD（2025-11-10—2026-11-10）

[已核查的相关论文与官方 PDF、公开代码及筛选边界](arxiv-cs-sd-2025-11-to-2026-11.md)：筛选出 2609.13595（多车声学跟踪）、2603.13903（DAS 道路识别）与 2606.27751（空间 SELD）三篇技术支撑论文。**本轮未查到该窗口内直接针对炸街车/非法改装排气检测的 cs.SD 论文**；相关不等于已验证违法排气识别。

## 2026-11-13 历史论文补充

已新增 **8 篇**：直接研究改装排气的 Cheng 等（2023）期刊论文，以及 7 篇相关 arXiv 工作（2302.02945、2309.03544、2401.09308、2305.14579、2401.00154、2409.10259、2609.28793）。按直接相关、空气声方法、DAS 跨模态参考分类，提供 PDF、官方分类与实验边界，见[完整清单](HISTORICAL-RELATED-PAPERS.md)。**这些是历史补充，不应算作近一年 cs.SD 的新增首发。**

## 学术论文：直接相关 vs 方法支撑

| 年份 | 论文 | 关联度 | 方法/结论 | 论文 |
|---|---|---|---|---|
| 2023 | AI-based method for determining vehicles with illegal muffler from pass by noise (INTER-NOISE 2023, 日本 NTSEL 报告收录) | **直接：非法消声器/改装** | 过车声时频图监督分类；麦克风阵列；跨车型、真实路段数据影响泛化。原报告指出混合车流条件仍需验证 | [NTSEL 官方概要 PDF](https://www.ntsel.go.jp/Portals/0/resources/report/files28/ronbungaiyo28.pdf) |
| 2025 预印本 / 2026 期刊 | Wang 等：Sound event detection for modified-exhaust vehicles in urban environment, Transportation Research Part D 153, 105241 (2026) | **直接：改装排气** | Scaper 合成 + 真实现场保留测试；SEDT，六种 backbone 比较，MSResNet 表现最好；event F1：验证 0.7277，现场 0.6629；SHAP 显示加速谐波/回火瞬态，也暴露合成时间偏差 | [DOI](https://doi.org/10.1016/j.trd.2026.105241) · [期刊](https://www.sciencedirect.com/science/article/pii/S1361920926000349) · [SSRN 预印本](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5554990) |
| 2023 | Cheng 等：Spectrogram-based classification on vehicles with modified loud exhausts via convolutional neural networks, Applied Acoustics 205, 109254 | **直接：改装排气分类** | STFT 谱图 + AlexNet 判别乘用车改装排气；YOLOv4-Tiny 辅助车辆类别识别；论文报告总体准确率约 96%（仅原文条件） | [DOI](https://doi.org/10.1016/j.apacoust.2023.109254) · [历史补充](HISTORICAL-RELATED-PAPERS.md) |
| 2021 | Abeßer 等：IDMT-Traffic: An Open Benchmark Dataset for Acoustic Traffic Monitoring Research (EUSIPCO) | 支撑：车型/过车检测 | 17,506 条、2 秒、4 类车辆、4 地点、不同天气/道路和麦克风；**没有公开的改装排气标注保证** | [官方数据集说明](https://www.idmt.fraunhofer.de/en/publications/datasets/traffic.html) |
| 2021 | Schulz 等：Hearing What You Cannot See: Acoustic Vehicle Detection Around Corners (IEEE RA-L) | 支撑：阵列定位 | 56 麦阵列、被遮挡车辆检测、跨地点测试；并非改装排气识别 | [DOI](https://doi.org/10.1109/LRA.2021.3062254) · [代码](https://github.com/tudelft-iv/occluded_vehicle_acoustic_detection) |
| 2021 | Ye 等：Sound Event Detection Transformer: An Event-based End-to-End Model for Sound Event Detection | 支撑：事件级建模 | SEDT 从帧级分类转为事件集合预测；2026 改装排气论文采用该系列模型框架 | [arXiv](https://arxiv.org/abs/2110.02011) |
| 2025 | Parineh 等：MELAUDIS: A Large-Scale Benchmark Acoustic Dataset For Intelligent Transportation Systems Research (Scientific Data 12, 362) | 支撑：多车型/复杂背景 | 多车同现、六类交通对象及背景、怠速音；**非改装排气真值库** | [期刊](https://doi.org/10.1038/s41597-025-04689-3) · [代码](https://github.com/parineh/MELAUDIS) |

注：2025 SSRN 预印本与 2026 期刊文为**同一研究工作，不重复计数**；原始结果仅是论文报告，非本仓库复现结论。

## 建议任务定义与标签
- **声事件层**：pass-by / acceleration roar / exhaust afterfire-pop / sustained high-rev / horn / siren / motorcycle normal / heavy-vehicle normal / unknown。
- **风险层**：normal / suspected_modified_exhaust / other_loud_source / uncertain；不能仅依据响度给出违法结论。
- **标注粒度**：事件起止时间、声源ID（多车）、车型、道路/录音设备/距离、交通密度、是否有视频或人工检查证据、置信度。
- **关键难例**：正常大排量摩托、货车制动声、车喇叭、施工、警笛、风噪；多车同时通过、回声/遮挡、手机录音动态压缩。

## 可复现基线建议
1. **音频片段二分类**：log-mel + ResNet18/PANNs，类别平衡与真负样本；输出疑似得分。
2. **事件级**：CRNN/SEDT，输出事件起止；与片段分类按 event-F1、PSDS、误报/小时、响应延迟对比。
3. **空间复核**：双麦/阵列的方向估计与目标过车轨迹；单麦场景不宣称可做准确车辆归属。
4. **评估**：严格留出道路、时间、车型、设备（不可按短片随机切分，防止同一次过车泄漏）；现场测试集不可参与阈值调参。
5. **部署指标**：每小时误报、每百次过车误报、目标事件召回、定位/声源归属错误率、域外性能、端侧时延。
6. **法规层**：声学模型只提供疑似线索，实际违法性需声级校准、测量规程和人工/法定流程佐证。

## 文件与维护
- [HISTORICAL-RELATED-PAPERS.md](HISTORICAL-RELATED-PAPERS.md)：8 篇历史补充论文、arXiv 分类、官方 PDF 与迁移边界。
- [RESOURCES.md](RESOURCES.md)：数据集、开源代码、可用性与限制。
- [TRENDS.md](TRENDS.md)：证据驱动技术趋势与建议实验。
- [papers-timeline.html](papers-timeline.html)：离线可浏览技术时间线。
- [timeline.json](timeline.json)：结构化论文节点（同一研究多版本不重复统计）。

**审核状态**：论文及资源链接来源于公开期刊、机构/项目主页与代码仓库；未下载数据、未复现代码、未获得 2026 研究的训练数据与官方实现授权，不应将方法支持等同于开源实现可用。
