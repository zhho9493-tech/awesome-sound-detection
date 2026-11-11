# arXiv cs.SD 每日增量｜2026-11-10 公告

> 来源：[arXiv cs.SD recent](https://arxiv.org/list/cs.SD/recent)。首次提交日期以论文版本记录为准（不等于公告日期）。工业声学/DAS迁移价值均为**研究假设**，非现场验证结论。

## SCLAP: Temporal structural alignment improves localization in long-form audio

- **作者**：Yacouba Kaloga; Ina Kodrasi
- **首次提交**：2026-11-09；**arXiv ID**：2611.12124
- **原文**：[arXiv](https://arxiv.org/abs/2611.12124) · [PDF](https://arxiv.org/pdf/2611.12124)
- **方法摘要**：以单调一维最优传输对齐音频帧和文本token，在仅有clip级caption时学习细粒度时间定位；推理无需执行最优传输。
- **工业声学/DAS迁移（研究假设）**：可探索托辊长时声学记录中短暂异常事件定位和弱监督标注，但目标声学语义描述质量可能限制性能。
- **复现/代码状态**：论文未声明公开代码；待核实。
- **局限与适用条件**：原始任务、传感器与工业DAS不同；须在项目隔离的固定测试集上验证，不能直接外推原论文指标。

## Discriminator-free adversarial domain adaptation for robust speech classification

- **作者**：Yacouba Kaloga; Ina Kodrasi
- **首次提交**：2026-11-09；**arXiv ID**：2611.12119
- **原文**：[arXiv](https://arxiv.org/abs/2611.12119) · [PDF](https://arxiv.org/pdf/2611.12119)
- **方法摘要**：提出无独立域判别器的DALN，复用任务分类头并利用分类输出上的核范数Wasserstein差异进行无监督域对齐；在语音情感/病理语音跨语言及噪声迁移中验证。
- **工业声学/DAS迁移（研究假设）**：DAS跨项目性能下降可对比DALN与DANN、CORAL及域专用专家；源/目标项目严格隔离，防止无标签目标数据泄漏。
- **复现/代码状态**：论文未声明公开代码；待核实。
- **局限与适用条件**：原始任务、传感器与工业DAS不同；须在项目隔离的固定测试集上验证，不能直接外推原论文指标。

