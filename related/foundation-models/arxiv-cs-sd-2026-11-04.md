# cs.SD 2026-11-04｜Audio-LLM / 多模态推理

## 1. SciPhi-Chat: Training a Spatial Audio Agent for Question Answering, Dialogue, and Tool Use
- 作者：Gijs Wijngaard; Hannes Gamper; Sebastian Braun
- 首次提交：2026-11-04；arXiv: https://arxiv.org/abs/2611.04114；PDF: https://arxiv.org/pdf/2611.04114
- 方法：基于一阶 Ambisonics 的空间音频 Agent，支持问答、多轮对话和工具调用；MASU 含 12,000 样本/42 类任务；作者报告 MASU 44.9%，较先前 SOTA +7.4 个百分点。
- 工业声学/DAS 迁移假设：多通道声源定位证据与工具调用式异常复核；Ambisonics 与 DAS 物理机制不同，不直接迁移其空间表示。
- 代码/复现：论文称将公开材料，当前未核实实际可用性；未复现。

## 2. Confidence-Aware Aggregation for Multimodal Audio Reasoning
- 作者：Michel Olvera; Paraskevas Stamatiadis; Gaël Richard
- 首次提交：2026-11-04；arXiv: https://arxiv.org/abs/2611.04580；PDF: https://arxiv.org/pdf/2611.04580
- 方法：利用 LALM 推理时多候选自一致性与对数似然加权，Borda 等聚合提高回答准确率与校准；DCASE 2026 workshop。
- 工业声学/DAS 迁移假设：大模型复核输出置信度、分歧与拒识，不能直接用回答一致性替代真实故障标签。
- 代码/复现：论文称项目代码可用，链接需单独核验；未复现。

## 3. ReListen: Training-Free Evidence Localization in Hour-Long Audio with Frozen Audio Language Models
- 作者：Ming-Hao Hsu; Shujie Liu; Yuxuan Hu; Yuxiang Wang; Yingda Shen; Jinyu Li; Zhizheng Wu
- 首次提交：2026-11-04；arXiv: https://arxiv.org/abs/2611.04480；PDF: https://arxiv.org/pdf/2611.04480
- 方法：冻结 Audio-LLM 对长音频以 20 秒窗口扫描，选出最相关一分钟证据后回答，无需训练；作者报告 VoiceGiraffe 证据重合率 88.5%。
- 工业声学/DAS 迁移假设：10 秒片段海量长程事件证据检索→局部精听→可追溯复核，需独立验证时序定位与检准。
- 代码/复现：未核实官方代码；未复现。

## 4. VeriSpoof: Beyond Real or Fake with One Audio LLM
- 作者：Yang Xiao; Ting Dang
- 首次提交：2026-11-04；arXiv: https://arxiv.org/abs/2611.04634；PDF: https://arxiv.org/pdf/2611.04634
- 方法：统一伪造检测、生成器归因、录音条件分析、局部定位、来源验证，输出可验证证据；作者报告 Plus 模型 pooled EER 2.14%（语音取证场景）。
- 工业声学/DAS 迁移假设：从单一异常二分类转向“类型+定位+条件+可核查证据”多任务诊断，不应移用语音取证指标。
- 代码/复现：论文声称模型与代码开放，尚未核实链接；未复现。
