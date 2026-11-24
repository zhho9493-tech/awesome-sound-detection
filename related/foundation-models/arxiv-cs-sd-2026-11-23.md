# arXiv cs.SD 2026-11-23 公告增量

## SLP-Bench: Evaluating and Improving Acoustic Claims of Reasoning Audio Language Models on Clinical Speech
- 作者：Côme Hosxe, Rachid Riad, Quentin Spinat；首次提交：2026-11-20。
- [arXiv](https://arxiv.org/abs/2611.27810) | [PDF](https://arxiv.org/pdf/2611.27810) | DOI: 10.48550/arXiv.2611.27810
- 方法：以五个临床专家标注数据集、25个感知维度逐条审计推理中的声学陈述，评价事实性、重采样稳定性和问题改写一致性；采用 GRPO 奖励优化陈述与专家判断的一致性。
- 结果：作者报告十个开放权重模型零样本陈述 balanced accuracy 为0.52–0.58；7B模型优化后由0.54至0.60，平均 kappa 由0.39至0.61。
- 复现：基准需申请并获数据提供者批准；公开训练代码未核实。
- DAS迁移研究假设：为周期冲击、窄带摩擦、持续性等声学属性构建专家标注，分别评估解释事实性与报警准确率；临床语音结果不可直接外推。

## Neural Defend ARCAS 290M: A Robust Foundation Model for AI-Generated Audio Detection
- 作者：Sivashankar Selvarajan, Piyush Verma, Sumit Kumar, Sharayu N. Deshmukh；首次提交：2026-11-20。
- [arXiv](https://arxiv.org/abs/2611.27784) | [PDF](https://arxiv.org/pdf/2611.27784) | DOI: 10.48550/arXiv.2611.27784
- 方法：冻结290M生产检测模型，在十个公开基准官方测试集上进行跨生成器、信道、语言的零样本评价，不做基准专属微调。
- 结果：作者报告多项基准表现优于已有比较系统；商业团队自报结果，尚未独立复核。
- 复现：公开权重及训练代码未核实。同期榜单报告 [2611.27215](https://arxiv.org/abs/2611.27215) 属同一系统，不独立计为方法贡献。
- DAS迁移研究假设：冻结模型跨项目盲测、统一阈值与低误报召回评估；语音伪造检测并非工业异常检测。
