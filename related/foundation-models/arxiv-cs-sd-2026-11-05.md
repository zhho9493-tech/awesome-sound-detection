# arXiv cs.SD 每日增量｜2026-11-05 公告｜基础音频模型

本页收录 2 篇，均与现有仓库的自监督预训练或 Audio-LLM 证据可靠性方向有关。摘要为论文作者报告，不代表工业 DAS 复现结论。

## 1. Drowning in Noise: On Signal Saliency in Self-Supervised Learning for Ocean Acoustics

- **作者**：Shikhar Bharadwaj; Samuele Cornell; Shinji Watanabe; Malcolm Slaney
- **首次提交**：2026-11-04
- **arXiv**：[2611.06725](https://arxiv.org/abs/2611.06725) · [官方 PDF](https://arxiv.org/pdf/2611.06725)
- **方法与结论**：以 BEATs 为测试平台，对海洋被动录音做显著事件筛选。作者报告：30 小时含目标声事件的精选预训练音频，在 31 类海洋哺乳动物分类上优于 1,240 小时未筛选录音；自动显著性筛选虽改善未筛选训练，但仍落后人工精选。
- **工业声学/DAS 迁移假设**：海量未标注 10s 片段的 SSL 训练不宜仅追求数据规模，可比较运行状态、声学信息密度、设备位置、异常候选/背景多样性引导的采样；避免只保留强异常而丢失正常工况多样性。
- **代码/复现**：论文页未标示官方代码；未复现，工业收益待验证。

## 2. Speaker-Consistent Grounding for Confusion-Resilient LLM-Based Target Speech Extraction

- **作者**：Hanyu Meng; Hao Shi; Zhanhong He; Qiquan Zhang; Yang Xiao; Sungwoo Cho; Haowei Lou; Haizhou Li
- **首次提交**：2026-11-04（cs.SD cross-list，主类 eess.AS）
- **arXiv**：[2611.06297](https://arxiv.org/abs/2611.06297) · [官方 PDF](https://arxiv.org/pdf/2611.06297)
- **方法与结论**：先对冻结目标说话人提取器产生的候选证据进行身份一致性筛选，再用于约束生成式语音提取；作者在 Libri2Mix 上报告错误说话人提取率下降，并降低生成式输出的身份/内容漂移。
- **工业声学/DAS 迁移假设**：大模型复核前先校验检索到的事件/设备/探测器证据身份与来源，防止错误证据被大模型强化；这是跨任务类比，非直接 DAS 性能证据。
- **代码/复现**：作者提供[项目页与代码入口](https://hanyu-meng.github.io/)；代码版本及可复现性未核验，未复现。

## 技术趋势判断

- SSL 数据选择从“数量优先”向“信息密度/有效事件覆盖优先”推进；单篇海洋声学研究不代表所有工业域均如此。
- Audio-LLM 从直接依赖检索证据走向“先校验/修复证据，再进行 grounding”，强化既有可核查推理趋势。
