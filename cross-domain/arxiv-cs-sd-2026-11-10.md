# arXiv cs.SD 每日增量｜2026-11-10 公告

> 来源：[arXiv cs.SD recent](https://arxiv.org/list/cs.SD/recent)。首次提交日期以论文版本记录为准（不等于公告日期）。工业声学/DAS迁移价值均为**研究假设**，非现场验证结论。

## When Normality Shifts: Multi-Level WavLM Modeling for Open-World Audio Deepfake Detection

- **作者**：Daniel Niekurzak; Daniel Kozuch; Weronika Folwarska; Khan Muhammad; Rafał Scherer
- **首次提交**：2026-11-08；**arXiv ID**：2611.11465
- **原文**：[arXiv](https://arxiv.org/abs/2611.11465) · [PDF](https://arxiv.org/pdf/2611.11465)
- **方法摘要**：冻结WavLM多层特征，以收缩Mahalanobis正常分布建模进行仅正常样本训练的开放世界伪造检测；跨域EER由8.45%升至22.12%，无标签阈值重校准无法挽救排序退化。
- **工业声学/DAS迁移（研究假设）**：对DAS异常检测具有重要负面证据：跨项目排序能力退化时，单独更新阈值可能无效；需同时报告pAUC、低FPR召回和校准前后排序。
- **复现/代码状态**：论文未声明代码公开；待核实。
- **局限与适用条件**：原始任务、传感器与工业DAS不同；须在项目隔离的固定测试集上验证，不能直接外推原论文指标。

## CallCleaner: Lightweight Bioacoustic Denoising from an Audio Foundation Model

- **作者**：Michael Xie; Gašper Beguš; Morris Alper
- **首次提交**：2026-11-08；**arXiv ID**：2611.11491
- **原文**：[arXiv](https://arxiv.org/abs/2611.11491) · [PDF](https://arxiv.org/pdf/2611.11491)
- **方法摘要**：利用SAM-Audio与简单动物VAD生成教师去噪结果，再蒸馏19M参数轻量模型；作者报告CPU约90倍实时速度、比Biodenoising少11dB呼叫周围噪声，强调噪声抑制与目标保真应分开评价。
- **工业声学/DAS迁移（研究假设）**：DAS强风噪/机械干扰可借鉴基础模型教师—小模型蒸馏；须核验异常冲击/啾啾声是否被错误抹除，不能仅凭降噪指标判定检测收益。
- **复现/代码状态**：作者声明开放代码及权重，项目主页见论文。
- **局限与适用条件**：原始任务、传感器与工业DAS不同；须在项目隔离的固定测试集上验证，不能直接外推原论文指标。

