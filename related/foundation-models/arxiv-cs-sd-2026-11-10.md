# arXiv cs.SD 每日增量｜2026-11-10 公告

> 来源：[arXiv cs.SD recent](https://arxiv.org/list/cs.SD/recent)。首次提交日期以论文版本记录为准（不等于公告日期）。工业声学/DAS迁移价值均为**研究假设**，非现场验证结论。

## LAION-Audio-XL: A Web-Scale Corpus and Scaling Studies for Contrastive Language-Audio Pretraining

- **作者**：Gijs Wijngaard; Felix Förster; Ross Wightman; Marianna Nezhurina; Christoph Schuhmann; Jenia Jitsev; A. Sophia Koepke
- **首次提交**：2026-11-08；**arXiv ID**：2611.11592
- **原文**：[arXiv](https://arxiv.org/abs/2611.11592) · [PDF](https://arxiv.org/pdf/2611.11592)
- **方法摘要**：1.48B音频样本多阶段清洗及补全长短描述，基于NaFlex音频编码器研究对比式音频—文本预训练规模与计算预算；发布CLAP2模型。
- **工业声学/DAS迁移（研究假设）**：工业DAS海量无标注数据可借鉴数据清洗、信息密度筛选和对比预训练，但web音频与DAS采集分布不同，必须验证跨项目迁移。
- **复现/代码状态**：作者声明开放数据、caption、权重与代码；具体许可与可获取性待逐项核验。
- **局限与适用条件**：原始任务、传感器与工业DAS不同；须在项目隔离的固定测试集上验证，不能直接外推原论文指标。

## Machine Hearing: Can Audio LLMs Generalize Beyond Human Auditory Perception?

- **作者**：Liwei Liu; Jun Tao; Xingyuan Li; Xuenan Xu; Chen Zhang; Junyi Wang; Boya Zhang; Xiaoyu Yang; Zhen-Hua Ling; Wen Wu; Chao Zhang
- **首次提交**：2026-11-07；**arXiv ID**：2611.10693
- **原文**：[arXiv](https://arxiv.org/abs/2611.10693) · [PDF](https://arxiv.org/pdf/2611.10693)
- **方法摘要**：提出Machine Hearing Benchmark：7领域13任务6128样本，测试超越人耳范围的波动/振动感知；发现现有Audio-LLM零样本迁移有限，提出MachEar轻量编码器扩展。
- **工业声学/DAS迁移（研究假设）**：DAS是非传统空气声学传感，适合作为检验前端错配与专用适配器的研究假设；不可将基准成绩视为DAS效果。
- **复现/代码状态**：摘要未声明开源代码或权重；待核实。
- **局限与适用条件**：原始任务、传感器与工业DAS不同；须在项目隔离的固定测试集上验证，不能直接外推原论文指标。

## LongCap: Hour-Scale Timestamped Audio Captioning via Chunk-wise Processing

- **作者**：Jinchuan Tian; Sen Chen; Wenbin Huang; Chao Weng; Zhengwei Huang; Jiatong Shi; Yichen Lu; Haoran Wang; Shinji Watanabe; Cong Zhou
- **首次提交**：2026-11-08；**arXiv ID**：2611.11125
- **原文**：[arXiv](https://arxiv.org/abs/2611.11125) · [PDF](https://arxiv.org/pdf/2611.11125)
- **方法摘要**：提出LongCapBench与TER/GER/tcpCapSim指标；分块结构化事件描述和相对时间戳保留上下文，实现长时间音频事件时间线描述。
- **工业声学/DAS迁移（研究假设）**：可探索DAS 10秒检测结果跨窗口聚合、长时事件解释与时间线审计；先比较事件级检测精度及延迟，不直接替换实时告警。
- **复现/代码状态**：有项目主页；代码/权重是否公开待核实。
- **局限与适用条件**：原始任务、传感器与工业DAS不同；须在项目隔离的固定测试集上验证，不能直接外推原论文指标。

