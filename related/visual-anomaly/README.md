# Visual Anomaly Detection / 图像异常检测

- [PatchCore](https://arxiv.org/abs/2106.08265) — patch 特征检索
- [PaDiM](https://arxiv.org/abs/2011.08785) — 分布建模
- [Anomalib](https://github.com/open-edge-platform/anomalib) — 开源工具
- [MVTec AD](https://www.mvtec.com/company/research/datasets/mvtec-ad) — 评价数据集
- [Google Drive 历史论文索引](drive-library-index.md)

声学迁移：谱图 patch 异常定位、Memory Bank、无监督、少样本与大规模检索。

## 技术时间线

| 时间 | 技术主线 | 代表性变化 |
|---|---|---|
| 2019–2020 | Reconstruction / Feature Distribution | 从重构误差扩展到 pretrained feature distribution；PaDiM 代表位置条件分布建模 |
| 2021 | PatchCore / Memory Bank | 通过局部 patch 检索显著强化无监督异常定位 |
| 2022–2023 | Transformer / Foundation Feature | 更强预训练特征减少对任务专用训练的依赖 |
| 2023–2024 | Few-shot / Zero-shot / CLIP-based AD | 文本语义与视觉基础模型用于少样本、开放词汇异常 |
| 2024–2025 | Domain-invariant / Distribution Shift | 关注新产线、新设备和不同成像条件的泛化 |
| 2025–2026 | Test-time Adaptation / Retrieval / Multimodal reasoning | 部署后适应、动态记忆库和多模态解释成为新重点 |
| 下一阶段 | Video/Temporal anomaly + Health evolution | 从单帧缺陷定位扩展到时序状态和设备健康演化 |

## 技术趋势

1. **[重构 → 预训练特征空间检测](trends/trend-01.md)**：异常判定更多依赖强 encoder，而非单独训练 decoder。
2. **[全局图像 → Patch / Region](trends/trend-02.md)**：局部异常定位是视觉 AD 的核心优势，可迁移到谱图局部频带/时间块。
3. **[参数模型 → Memory Bank / Retrieval](trends/trend-03.md)**：以正常样本库为参照，适合少异常标注场景。
4. **[同域 benchmark → Domain Shift / TTA](trends/trend-04.md)**：真实部署需要处理设备、项目、光照/采集条件变化。
5. **[Closed-set → Zero-shot / Open-vocabulary](trends/trend-05.md)**：基础模型帮助发现训练时未定义的异常类型。
6. **[单帧 → 时序/视频异常](trends/trend-06.md)**：长期状态和事件持续性开始成为重要研究对象。

## 当前判断 / 对声学迁移

- 最值得迁移到谱图：PatchCore 式局部 memory bank、位置条件分布、test-time adaptation。
- 对跨项目工业声学，可比较“分类器”与“正常记忆库检索”两条路线。
- 新增论文后，应检查“Foundation Feature / Memory Bank / TTA / Temporal”四条趋势是否变化。
