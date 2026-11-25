# 2026-11-24 cs.SD 每日增量

公告日期：2026-11-24；筛选日期：2026-11-25。[公告](https://arxiv.org/list/cs.SD/recent)。以下基于原文摘要，未独立复现；工业/DAS迁移均为研究假设。

## What Do Sound Event Embeddings Reveal? Auditing Speaker Leakage in Audio Representations

- 作者：Bhawana Chhaglani
- 首次提交：2026-11-23（UTC）
- [arXiv](https://arxiv.org/abs/2611.31043) · [PDF](https://arxiv.org/pdf/2611.31043) · [DOI](https://doi.org/10.48550/arXiv.2611.31043)
- 方法及证据：对 CLAP、PANNs、AST、YAMNet 使用表征统计依赖与轻量探针审计非目标信息；说话人识别平衡准确率 0.43–0.72。
- 工业声学/DAS迁移假设：将探针目标替换为项目、探测器、工况，诊断跨项目表征混杂；隐私泄漏与域偏差并非同一问题。
- 复现状态：代码未核实；未独立复现。

## MusicListenBench: Can Audio LLMs Hear the Difference Yet?

- 作者：Abhinaba Roy, Ambuj Mehrish, Dorien Herremans
- 首次提交：2026-11-22（UTC）
- [arXiv](https://arxiv.org/abs/2611.29375) · [PDF](https://arxiv.org/pdf/2611.29375) · [DOI](https://doi.org/10.48550/arXiv.2611.29375)
- 方法及证据：配对 FLIP/STAY 测试区分目标属性变化和仅声学干扰变化；GRPO 后干净配对准确率 61.2%→99.0%，但干扰引发错误翻转仍达25.7%。真实录音泛化有限。
- 工业声学/DAS迁移假设：构造故障变化与背景噪声变化的配对测试，独立评价敏感性和不变性。
- 复现状态：作者声明发布数据、代码和榜单；具体仓库未核实；未独立复现。

## Which Layer to Trust? Layer Selection in Frozen Speech Encoders for Singing-Voice Deepfake Detection under Signal Corruption

- 作者：Benjamin Hurt, Yefei Yang
- 首次提交：2026-11-23（UTC）
- [arXiv](https://arxiv.org/abs/2611.29871) · [PDF](https://arxiv.org/pdf/2611.29871) · [DOI](https://doi.org/10.48550/arXiv.2611.29871)
- 方法及证据：CtrSVDD 上逐层比较冻结 XEUS/XLS-R 与学习层混合；噪声、混响、编码影响最优层，开发集选层较测试最优层 EER 高2.3/4.1个百分点。
- 工业声学/DAS迁移假设：跨项目和干扰条件下逐层探针，比较固定层与条件化层融合；论文未验证动态路由。
- 复现状态：代码未核实；未独立复现。

## Characterizing Frozen SSL Encoders and Backends for Cross-Domain Speech Deepfake Detection

- 作者：Benjamin Hurt, Oscar O'Donnell, Yefei Yang, Anjani Sethi, Priyanka Durai
- 首次提交：2026-11-23（UTC）
- [arXiv](https://arxiv.org/abs/2611.29865) · [PDF](https://arxiv.org/pdf/2611.29865) · [DOI](https://doi.org/10.48550/arXiv.2611.29865)
- 方法及证据：交叉比较冻结 XEUS/XLSR-53 与 MHFA/AASIST，在 ASVspoof 与 ITW 多域三种子评价；XEUS+MHFA 相对 XLSR-53 在三个域错误下降58–77%，但冻结方案并非所有域优于微调。
- 工业声学/DAS迁移假设：固定数据划分比较编码器×后端交互及冻结/微调的跨项目低误报召回。
- 复现状态：代码未核实；未独立复现。
