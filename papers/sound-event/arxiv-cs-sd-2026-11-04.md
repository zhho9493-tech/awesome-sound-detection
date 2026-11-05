# cs.SD 2026-11-04｜声音事件与多点声学

本页依据 arXiv 2026-11-04 公告新增，均为论文作者报告，尚未在工业 DAS 复现。

## 1. Metadata-Conditioned Audio Transformers for Adaptive Respiratory Sound Classification
- 作者：George Kontogiannis; Pantelis Tzamalis; Sotiris Nikoletseas
- 首次提交：2026-11-04；arXiv: https://arxiv.org/abs/2611.03769；PDF: https://arxiv.org/pdf/2611.03769
- 方法：在 AST 中引入 TAFiLM（区分 patch/class token 的条件调制）及 SoftFiLM（元数据因素与特征子空间软对齐）；ICBHI 四类任务报告 64.11%，比其基线高 3.94 个百分点。
- 工业声学迁移假设：把项目、探测器、运行状态作为条件信息，但需留出未见项目并测试元数据捷径风险。
- 代码/复现：未核实官方代码；未复现。

## 2. Hybrid acoustic and pretrained embedding feature fusion for unmanned aerial vehicle detection using stacking ensemble learning under a leakage-aware evaluation protocol
- 作者：Zahid Iqbal
- 首次提交：2026-11-04；arXiv: https://arxiv.org/abs/2611.04714；PDF: https://arxiv.org/pdf/2611.04714
- 方法：57 维手工声学特征与 YAMNet 1024 维 embedding 双视图 stacking，按录音源分组隔离；作者报告分组准确率 95.29%，随机划分高估 1.89–3.22 个百分点。
- 工业声学迁移假设：项目/通道/时段严格隔离；比较物理特征+预训练表征的互补性。
- 代码/复现：未核实官方代码；未复现。

## 3. Towards Automatic Heart Murmur Characterization from Multi-spot Phonocardiograms
- 作者：Marcelo Nogueira; Jorge H. Oliveira; Carlos G. Ferreira; Miguel T. Coimbra; Alípio M. Jorge
- 首次提交：2026-11-04；arXiv: https://arxiv.org/abs/2611.03654；PDF: https://arxiv.org/pdf/2611.03654
- 方法：比较多点听诊的 late fusion、同步多输入 CNN 和多输出属性识别；在 735 名患者数据中，最大严重度后融合对部分任务优于联合模型；不恰当的少数类片段过采样损害患者级表现。
- 工业声学迁移假设：相邻探测器多点聚合与“异常强度/属性”联合输出；对照 late fusion 与 joint modeling，避免片段标签泄漏到设备级。
- 代码/复现：未核实官方代码；未复现。
