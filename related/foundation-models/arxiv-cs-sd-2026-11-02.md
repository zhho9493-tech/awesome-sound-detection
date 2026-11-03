# arXiv cs.SD 每日增量：2026-11-02（Audio-LLM / 多模态可靠性）

> 来源：[cs.SD 2026-11-02 公告](https://arxiv.org/list/cs.SD/recent)。本页区分论文原始实验结论与工业声学迁移假设；全部为 **to-reproduce**。

## 1. Scalable Audio-LLM System for Speech MOS Evaluation: A Diagnostic Case Study and Adaptation Roadmap

- **arXiv ID**：2610.41539（cs.SD）
- **作者**：Dimitrios Kokkinis, Panagiotis Kakoulidis, Nikolaos Ellinas, Chrysovalanti Lymperi, Alexandra Vioni, Georgios Vardaxoglou, Iakovi Alexiou, Myrsini Christidou, Jeasung Lee, Gunu Jho, Inchul Hwang, Pirros Tsiakoulis, Aimilios Chalamandaris
- **首次提交**：2026-10-30（UTC）；**cs.SD 公告**：2026-11-02
- **摘要**：[arXiv](https://arxiv.org/abs/2610.41539) · **PDF**：[官方 PDF](https://arxiv.org/pdf/2610.41539)
- **研究任务**：合成语音 MOS 质量评估的低成本、可扩展自动化。
- **核心方法**：以 Qwen2-Audio-7B-Instruct 进行 zero-shot MOS 诊断，识别感知盲点与偏差；再使用 LoRA 做任务适配，和 UTMOS 等基线比较。
- **论文报告结论**：在其语音质量评估设置中，LoRA 适配改善了基础模型的评估表现；具体幅度与适用范围需查阅正文实验表。
- **工业声学 / DAS 迁移假设**：Audio-LLM 不宜直接零样本替代异常强度评估器；可先做噪声/强度主观-客观标尺校准，再进行小参数适配并检查系统性偏差。
- **代码状态**：未核验官方代码；**复现状态**：to-reproduce（未复现）。

## 2. Incongruence-Aware Evaluation of Multimodal Speech Emotion Recognition in Audio Large Language Models

- **arXiv ID**：2610.40883（主分类 cs.AI；交叉收录 cs.SD）
- **作者**：Fengji Jing, Guy Laban
- **首次提交**：2026-10-29（UTC）；**cs.SD 公告**：2026-11-02
- **摘要**：[arXiv](https://arxiv.org/abs/2610.40883) · **PDF**：[官方 PDF](https://arxiv.org/pdf/2610.40883)
- **研究任务**：评估音频大模型在“文本语义与声学情绪线索冲突”时的多模态错误风险。
- **核心方法**：将音频/文本映射到共享的 valence-arousal-dominance 空间；通过两分量高斯混合得到无阈值不一致分数，并在三个语音情绪语料上分析错误概率。
- **论文报告结论**：在所测试的三种语音情绪数据集上，多模态不一致与 Audio-LLM 错误概率上升相关；说明“多模态融合”并非总能提高可靠性。
- **工业声学 / DAS 迁移假设**：声学证据与设备工况、维修文本或视觉证据冲突时，不应无条件融合；可设计模态一致性得分、证据冲突报警及降级到单模态的策略。
- **代码状态**：论文摘要声明已公开代码/数据表/提示词，**具体官方仓库链接尚未核验**；**复现状态**：to-reproduce（未复现）。

## 对当前技术趋势的影响

- **技术时间线候选节点（2026-10/11）**：Audio-LLM 从单纯推理能力扩展到 **评估偏差诊断、任务校准、跨模态证据冲突监测**。
- **趋势修订**：原“Audio-only → Audio-Text / Multimodal”需要附加可靠性条件：更多模态不必然更准确；应先判断证据一致性、校准误差与退化路径。
- **建议实验**：Audio-only、metadata-only、naive fusion、gated fusion、conflict-aware fusion，在跨项目固定测试集上比较 pAUC、误报、校准误差和推理成本。
