# 声音事件检测技术趋势分析

> 从“识别一段录音中有什么声音”，发展到在复杂声景中判断**什么事件、何时发生、来自哪里，以及模型的判断是否可靠**。

[交互式专题页面](../../portal/topic.html?topic=sed) · [交互时间线](papers-timeline.html) · [事件对象导航](TOPICS.md) · [2025–2026 arXiv 索引](arxiv-cs-sd-2025-2026.md)

---

## 01 · 总览

声音事件检测（Sound Event Detection, SED）同时处理事件类别与时间边界。仓库采用两个可以交叠的维度组织论文：

- **研究方向**：按声音来源与应用场景划分，例如安防、交通、生态、工业、医疗、水下声学。
- **解决的问题**：按方法要解决的共性困难划分，例如少样本、弱监督、跨域泛化、长尾、低信噪比与开放集识别。
- **允许交叠**：一篇“跨域少样本鸟鸣检测”论文可以同时归入动物声音、少样本和跨域泛化，不重复创建论文身份。

### 方向导航

| 方向 | 主要对象 | 专题入口 |
|---|---|---|
| 安防与危险事件 | 枪声、爆炸、玻璃破碎、警报 | [进入专题](security/README.md) |
| 人类非语言声音 | 哭声、尖叫、咳嗽、鼾声 | [进入专题](human/README.md) |
| 动物与生态声音 | 鸟鸣、犬吠、昆虫及野生动物 | [动物声音](animal/README.md) · [农业与生态](agriculture/README.md) |
| 工业机械声音 | 电机、齿轮、托辊、机械冲击 | [进入专题](industrial/README.md) |
| 交通与运输 | 道路车辆、轨道、飞机、船舶 | [进入专题](transportation/README.md) · [炸街车](transportation/noisy-vehicle/README.md) |
| 医疗与生理声音 | 呼吸音、心音、睡眠声音 | [进入专题](medical/README.md) |
| 城市、家居与环境 | 公共警报、人群、家居及自然声 | [城市](urban/README.md) · [家居](domestic/README.md) · [环境](environmental/README.md) |
| 水下与基础设施 | 海洋生物、船舶、结构与管线事件 | [水下](underwater/README.md) · [基础设施](infrastructure/README.md) |

### 该方向正在解决的问题

| 问题 | 在 SED 中的具体表现 | 专题入口 |
|---|---|---|
| 少样本与低资源 | 新事件只有少量示例，细粒度类别难以完整标注 | [少样本学习](../../general-problems/few-shot-learning/README.md) |
| 半监督与弱监督 | 只有录音级标签，缺少准确的事件起止时间 | [半/弱监督](../../general-problems/semi-weak-supervision/README.md) |
| 跨域泛化 | 换设备、地点或声景后性能明显下降 | [跨域泛化](../../general-problems/domain-generalization/README.md) |
| 长尾与类别不平衡 | 常见事件占据多数，罕见事件召回率低 | [长尾学习](../../general-problems/long-tail-learning/README.md) |
| 开放集与 OOD | 未知声音被高置信度归入已知类别 | [开放集/OOD](../../general-problems/ood/README.md) |
| 低信噪比 | 弱目标被强背景噪声或重叠事件掩盖 | [低信噪比 SED](low-snr/README.md) |
| 持续与增量学习 | 新项目、新域或新类别加入后遗忘旧知识 | [持续学习](../../general-problems/continual-learning/README.md) |
| 校准与可靠性 | 模型分数不能直接代表事件判断可信度 | [校准与不确定性](../../general-problems/calibration-uncertainty/README.md) |

> [在交互页面中按问题筛选本方向论文](../../portal/topic.html?topic=sed#details)

---

## 02 · 技术时间线

### 2017–2020 · 从录音分类迈向事件时间边界

CNN/CRNN 将局部时频模式与循环时序建模结合，研究目标由 clip 级“是否存在”扩展为事件起止时间检测。弱标签开始通过多实例学习和事件级聚合转化为帧级预测，但边界质量容易受到标签粒度和阈值影响。

### 2021–2023 · 从专用网络迈向预训练与长时上下文

Transformer、Conformer 与自监督音频预训练增强长时依赖建模。方法逐渐从单数据集训练转向复用通用声学表征，并通过教师—学生、伪标签和一致性训练利用未标注录音。

### 2024–2025 · 从封闭标签集迈向跨域、少样本与结构化检测

研究开始显式处理设备、场景和录音源变化；少样本检测、层级分类、原型学习及检索增强成为重要分支。事件检测也更多地与声源定位、分离和多模态信息结合。

### 2025–2026 · 从单任务检测器迈向基础模型驱动的开放世界声音理解

音频—语言对齐和基础模型将文本语义引入事件查询，推动开放词表、零样本定位和音频推理。与此同时，领域增量学习、专家路由、元数据条件和证据校准开始解决长期部署中的新域、新类别与可靠性问题。

### 2026 近期变化 · 从预测结果迈向可核验的声学证据

近期工作不只输出类别，还关注模型是否真正依据声学线索：帧—词对齐用于长音频定位，场景—事件联合建模用于发现语义冲突，录音源隔离评估用于排除数据捷径，可信推理基准则检查音频语言模型是否给出有证据的结论。

---

## 03 · 技术趋势

### 1. 从固定标签集到开放词表事件感知

文本—音频对齐使检测器能够用自然语言查询事件，并尝试识别训练标签之外的声音。真正落地仍需要解决开放词表的时间边界、相似概念混淆和未知类别置信度校准。

**支撑工作类型：** CLAP/音频语言模型、零样本 SED、文本条件定位、开放集识别。

### 2. 从录音级判断到时间、空间与声源联合解析

技术目标由“录音里有什么”扩展为“何时发生、来自哪里、由哪个声源产生”。检测、定位和分离逐渐协同建模，尤其适用于复调事件、移动声源和长音频。

**支撑工作类型：** SELD、复调表示学习、目标声源分离、帧—词对齐。

### 3. 从强时间标注到弱监督和人机协同标注

强标注成本限制了数据规模。弱标签、伪标签、主动学习和人工复核式 AI 标注工作流正在形成组合方案：机器生成候选，人类处理不确定样本并修正边界。

**支撑工作类型：** Mean Teacher、伪标签、自训练、不确定性采样、人机复核。

### 4. 从同分布准确率到跨设备、跨地点和跨项目泛化

声音事件模型容易学习录音设备、背景环境和数据来源捷径。研究由随机切分转向 source-disjoint、site-disjoint 和 leave-one-domain-out 评估，并通过域适配、域泛化及动态噪声建模提高迁移稳定性。

**支撑工作类型：** 域不变表征、归一化、风格扰动、无监督目标域适配。

### 5. 从平均性能到长尾、低信噪比与风险控制

真实声景中罕见事件和微弱目标通常决定系统价值。方法由统一重采样和前置降噪，转向类别感知损失、目标条件增强、动态噪声底建模，以及面向漏检与误报成本的事件级校准。

**支撑工作类型：** 长尾损失、目标条件分离、Noise-aware 表征、置信度校准。

### 6. 从一次训练到持续学习与领域专家系统

部署后的模型需要持续接收新类别和新项目。参数隔离、原型记忆、回放和领域专家路由用于降低灾难性遗忘，但必须同时报告新任务学习能力与旧任务保持程度。

**支撑工作类型：** 类别增量、领域增量、原型回放、Domain Experts / MoE。

---

## 04 · 论文详情

本节收录当前统一索引中归入声音事件检测方向的 **1,269 篇论文**。论文按年份分组、年份默认折叠；展开后按日期从最新到最旧排列。

> 中文简述由论文题目与公开摘要中的方法、场景和问题标签生成，用于快速浏览；题名级候选与自动归类仍需结合原文复核。

**问题分布：** 通用检测与分类 547 · 轻量化部署 256 · 定位与分离 233 · 多模态与基础模型 159 · 少样本 74 · 可解释与可靠性 71 · 低信噪比 54 · 开放集/OOD 53 · 跨域泛化 44 · 半/弱监督 35 · 长尾与不平衡 21 · 持续学习 19

<details>
<summary><strong>2026 年（296 篇）</strong></summary>

#### [A Human-Verified AI Workflow for Annotating Environmental Sound Data](https://arxiv.org/abs/2611.03271)

- **日期：** 2026-11-02
- **问题 / 中文简述：** 长尾与不平衡 · 开放集/OOD；采用Transformer 表征，面向工业与机械声音解决长尾与不平衡问题。
- **来源：** [论文主页](https://arxiv.org/abs/2611.03271) · [PDF](https://arxiv.org/pdf/2611.03271) · arXiv 2611.03271

#### [Self-Supervised Object-Centric Representation for Multi-Task Audio Analysis](https://arxiv.org/abs/2610.41870)

- **日期：** 2026-10-30
- **问题 / 中文简述：** 开放集/OOD · 定位与分离；采用自监督表征，面向声音事件解决开放集/OOD问题。
- **来源：** [论文主页](https://arxiv.org/abs/2610.41870) · [PDF](https://arxiv.org/pdf/2610.41870) · arXiv 2610.41870

#### [One Waveform, Two Stories: Benchmarking Speech-Acoustic Conflict in Audio-Language Models](https://arxiv.org/abs/2611.00325)

- **日期：** 2026-10-30
- **问题 / 中文简述：** 多模态与基础模型 · 可解释与可靠性；采用音频语言模型，面向环境与城市声音解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2611.00325) · [PDF](https://arxiv.org/pdf/2611.00325) · arXiv 2611.00325

#### [A richness-sensitive Acoustic Biodiversity Index from species-level detections: classifier benchmarking, false-positive control and validation against standard soundscape indices in an African savanna and an urban zoo](https://arxiv.org/abs/2610.42042)

- **日期：** 2026-10-30
- **问题 / 中文简述：** 可解释与可靠性；采用数据驱动方法，面向生态与动物声音解决可解释与可靠性问题。
- **来源：** [论文主页](https://arxiv.org/abs/2610.42042) · [PDF](https://arxiv.org/pdf/2610.42042) · arXiv 2610.42042

#### [Lightweight Underwater Acoustic Vessel Classification for Embedded Deployment](https://arxiv.org/abs/2610.39371)

- **日期：** 2026-10-29
- **问题 / 中文简述：** 轻量化部署；采用Transformer 表征，面向工业与机械声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2610.39371) · [PDF](https://arxiv.org/pdf/2610.39371) · arXiv 2610.39371

#### [Bridging Neural Representations and Symbolic Semantics in Audio Classification](https://arxiv.org/abs/2610.40414)

- **日期：** 2026-10-29
- **问题 / 中文简述：** 可解释与可靠性；采用数据驱动方法，面向声音事件解决可解释与可靠性问题。
- **来源：** [论文主页](https://arxiv.org/abs/2610.40414) · [PDF](https://arxiv.org/pdf/2610.40414) · arXiv 2610.40414

#### [Universal Short-Time Fourier Transform: Data-Adaptive Window-Length Selection for Time-Frequency Analysis](https://arxiv.org/abs/2610.37795)

- **日期：** 2026-10-27
- **问题 / 中文简述：** 通用检测与分类；采用数据增强与生成开展生态与动物声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2610.37795) · [PDF](https://arxiv.org/pdf/2610.37795) · arXiv 2610.37795

#### [Graph Neural Network for Wide-Area 6DoF Ambisonic Rendering](https://arxiv.org/abs/2610.35741)

- **日期：** 2026-10-26
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向环境与城市声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2610.35741) · [PDF](https://arxiv.org/pdf/2610.35741) · arXiv 2610.35741

#### [Dolphin broadband transient vocalization detection in impulsive ambient noise](https://arxiv.org/abs/2610.35641)

- **日期：** 2026-10-26
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向生态与动物声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2610.35641) · [PDF](https://arxiv.org/pdf/2610.35641) · arXiv 2610.35641

#### [A Hierarchical Method for Environmental Sounds Recognition in Complex Acoustic Scenes](https://arxiv.org/abs/2610.34931)

- **日期：** 2026-10-26
- **问题 / 中文简述：** 长尾与不平衡 · 轻量化部署；采用Transformer 表征，面向环境与城市声音解决长尾与不平衡问题。
- **来源：** [论文主页](https://arxiv.org/abs/2610.34931) · [PDF](https://arxiv.org/pdf/2610.34931) · arXiv 2610.34931

#### [STFT Frontend Mismatch in Pretrained Audio Spectrogram Transformers: Analysis and Adaptation](https://arxiv.org/abs/2610.34533)

- **日期：** 2026-10-25
- **问题 / 中文简述：** 轻量化部署；采用Transformer 表征，面向工业与机械声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2610.34533) · [PDF](https://arxiv.org/pdf/2610.34533) · arXiv 2610.34533

#### [Supervised Source Separation of Electric Vehicle Interior Noise Using a Hybrid Transformer Architecture](https://arxiv.org/abs/2610.32310)

- **日期：** 2026-10-23
- **问题 / 中文简述：** 定位与分离；采用Transformer 表征，面向交通与水下声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2610.32310) · [PDF](https://arxiv.org/pdf/2610.32310) · arXiv 2610.32310

#### [Efficient Streaming Audio-Visual Target Speaker Extraction for Real-World Acoustic Scenes](https://arxiv.org/abs/2610.32749)

- **日期：** 2026-10-23
- **问题 / 中文简述：** 定位与分离 · 轻量化部署；采用对比与原型学习，面向环境与城市声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2610.32749) · [PDF](https://arxiv.org/pdf/2610.32749) · arXiv 2610.32749

#### [From Signals to Evidence: Interpretable Underwater Acoustic Target Sensing with Large Language Models - Part II: Passive Detection](https://arxiv.org/abs/2610.31346)

- **日期：** 2026-10-22
- **问题 / 中文简述：** 可解释与可靠性；采用音频语言模型，面向工业与机械声音解决可解释与可靠性问题。
- **来源：** [论文主页](https://arxiv.org/abs/2610.31346) · [PDF](https://arxiv.org/pdf/2610.31346) · arXiv 2610.31346

#### [MarineSet: Large-Scale Underwater Acoustic Data Curation and evaluation](https://arxiv.org/abs/2610.33080)

- **日期：** 2026-10-21
- **问题 / 中文简述：** 通用检测与分类；采用自监督表征开展交通与水下声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2610.33080) · [PDF](https://arxiv.org/pdf/2610.33080) · arXiv 2610.33080

#### [Qwen-Audio-3.1-ASR Technical Report](https://arxiv.org/abs/2610.28711)

- **日期：** 2026-10-20
- **问题 / 中文简述：** 多模态与基础模型；采用音频语言模型，面向声音事件解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2610.28711) · [PDF](https://arxiv.org/pdf/2610.28711) · arXiv 2610.28711

#### [MiCLA: Mixture-to-Constituent Latent Alignment for Polyphonic Audio Representation Learning](https://arxiv.org/abs/2610.27491)

- **日期：** 2026-10-20
- **问题 / 中文简述：** 轻量化部署；采用自监督表征，面向声音事件解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2610.27491) · [PDF](https://arxiv.org/pdf/2610.27491) · arXiv 2610.27491

#### [APRIL: Ambiguity-Aware Expert Routing for Respiratory Sound Domain-Incremental Learning](https://arxiv.org/abs/2610.27942)

- **日期：** 2026-10-20
- **问题 / 中文简述：** 跨域泛化 · 持续学习 · 可解释与可靠性 · 轻量化部署；采用对比与原型学习，面向医疗与生理声音解决跨域泛化问题。
- **来源：** [论文主页](https://arxiv.org/abs/2610.27942) · [PDF](https://arxiv.org/pdf/2610.27942) · arXiv 2610.27942

#### [AudioScorer: Learning Question-Aware Token Relevance for Large Audio Language Models](https://arxiv.org/abs/2610.26258)

- **日期：** 2026-10-19
- **问题 / 中文简述：** 多模态与基础模型 · 轻量化部署；采用音频语言模型，面向环境与城市声音解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2610.26258) · [PDF](https://arxiv.org/pdf/2610.26258) · arXiv 2610.26258

#### [DF-PALM: Dynamic Fusion Prompt Learning for Audio--Language Models](https://arxiv.org/abs/2610.24921)

- **日期：** 2026-10-18
- **问题 / 中文简述：** 少样本 · 多模态与基础模型；采用音频语言模型，面向声音事件解决少样本问题。
- **来源：** [论文主页](https://arxiv.org/abs/2610.24921) · [PDF](https://arxiv.org/pdf/2610.24921) · arXiv 2610.24921

#### [MOMO: Human Motion from Moving Sounds](https://arxiv.org/abs/2610.24522)

- **日期：** 2026-10-17
- **问题 / 中文简述：** 定位与分离；采用数据增强与生成，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2610.24522) · [PDF](https://arxiv.org/pdf/2610.24522) · arXiv 2610.24522

#### [Semantic-Critical Regions for Video-to-Audio Generation](https://arxiv.org/abs/2610.23021)

- **日期：** 2026-10-16
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2610.23021) · [PDF](https://arxiv.org/pdf/2610.23021) · arXiv 2610.23021

#### [PAC-KD: Pathology-Aware Compositional Knowledge Distillation for Respiratory Sound Classification](https://arxiv.org/abs/2610.22826)

- **日期：** 2026-10-16
- **问题 / 中文简述：** 可解释与可靠性 · 轻量化部署；采用数据驱动方法，面向医疗与生理声音解决可解释与可靠性问题。
- **来源：** [论文主页](https://arxiv.org/abs/2610.22826) · [PDF](https://arxiv.org/pdf/2610.22826) · arXiv 2610.22826

#### [Clinically Informed Acoustic-Aware Attribute Modeling for Respiratory Sound Classification](https://arxiv.org/abs/2610.22854)

- **日期：** 2026-10-16
- **问题 / 中文简述：** 长尾与不平衡；采用数据驱动方法，面向医疗与生理声音解决长尾与不平衡问题。
- **来源：** [论文主页](https://arxiv.org/abs/2610.22854) · [PDF](https://arxiv.org/pdf/2610.22854) · arXiv 2610.22854

#### [TRACE: Trustworthy Reasoning from Acoustic Cues and Evidence](https://arxiv.org/abs/2610.26894)

- **日期：** 2026-10-15
- **问题 / 中文简述：** 多模态与基础模型 · 可解释与可靠性；采用音频语言模型，面向环境与城市声音解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2610.26894) · [PDF](https://arxiv.org/pdf/2610.26894) · arXiv 2610.26894

#### [D-Composer: Language Modeling for Simultaneous Drum Transcription and Sound Event Decomposition](https://arxiv.org/abs/2610.22535)

- **日期：** 2026-10-15
- **问题 / 中文简述：** 少样本 · 定位与分离；采用音频语言模型，面向声音事件解决少样本问题。
- **来源：** [论文主页](https://arxiv.org/abs/2610.22535) · [PDF](https://arxiv.org/pdf/2610.22535) · arXiv 2610.22535

#### [ONCship: A Large-Scale Underwater Acoustic Corpus for Ship Recognition](https://arxiv.org/abs/2610.19722)

- **日期：** 2026-10-14
- **问题 / 中文简述：** 通用检测与分类；采用自监督表征开展交通与水下声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2610.19722) · [PDF](https://arxiv.org/pdf/2610.19722) · arXiv 2610.19722

#### [SpectralBridge: Adding High-Frequency Capability to Large Audio-Language Models](https://arxiv.org/abs/2610.17048)

- **日期：** 2026-10-12
- **问题 / 中文简述：** 开放集/OOD · 多模态与基础模型 · 轻量化部署；采用音频语言模型，面向生态与动物声音解决开放集/OOD问题。
- **来源：** [论文主页](https://arxiv.org/abs/2610.17048) · [PDF](https://arxiv.org/pdf/2610.17048) · arXiv 2610.17048

#### [Feature Scaling Beats Architecture Choice in Offline Respiratory Screening for Low-Resource Clinics](https://arxiv.org/abs/2610.33030)

- **日期：** 2026-10-12
- **问题 / 中文简述：** 少样本 · 长尾与不平衡；采用数据增强与生成，面向医疗与生理声音解决少样本问题。
- **来源：** [论文主页](https://arxiv.org/abs/2610.33030) · [PDF](https://arxiv.org/pdf/2610.33030) · arXiv 2610.33030

#### [Sleep Sound Event Detection Powered by Learnable Multi-Resolution Adaptive Line Enhancer](https://arxiv.org/abs/2610.15532)

- **日期：** 2026-10-11
- **问题 / 中文简述：** 可解释与可靠性；采用Transformer 表征，面向声音事件解决可解释与可靠性问题。
- **来源：** [论文主页](https://arxiv.org/abs/2610.15532) · [PDF](https://arxiv.org/pdf/2610.15532) · arXiv 2610.15532

#### [AnyEdit: A Unified Framework for Speech and Singing Voice Editing with Real-World Environmental Consistency](https://arxiv.org/abs/2610.15665)

- **日期：** 2026-10-11
- **问题 / 中文简述：** 低信噪比 · 定位与分离；采用数据增强与生成，面向环境与城市声音解决低信噪比问题。
- **来源：** [论文主页](https://arxiv.org/abs/2610.15665) · [PDF](https://arxiv.org/pdf/2610.15665) · arXiv 2610.15665

#### [FAM-gate: field-aware metadata attention with prior-constrained vector gating for audio classification](https://arxiv.org/abs/2610.14673)

- **日期：** 2026-10-10
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2610.14673) · [PDF](https://arxiv.org/pdf/2610.14673) · arXiv 2610.14673

#### [Sonic-AMG: Streaming Human Motion Generation from Spatial Audio](https://arxiv.org/abs/2610.13300)

- **日期：** 2026-10-09
- **问题 / 中文简述：** 定位与分离 · 轻量化部署；采用Transformer 表征，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2610.13300) · [PDF](https://arxiv.org/pdf/2610.13300) · arXiv 2610.13300

#### [QC-MI-OVSEL: Benchmarking Query-Conditioned Multi-Instance Open-Vocabulary Sound Event Localization](https://arxiv.org/abs/2610.13198)

- **日期：** 2026-10-09
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2610.13198) · [PDF](https://arxiv.org/pdf/2610.13198) · arXiv 2610.13198

#### [MiDashengLM-Spatial: Unifying General Audio Understanding and Spatial Awareness](https://arxiv.org/abs/2610.11156)

- **日期：** 2026-10-08
- **问题 / 中文简述：** 定位与分离 · 多模态与基础模型 · 轻量化部署；采用音频语言模型，面向环境与城市声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2610.11156) · [PDF](https://arxiv.org/pdf/2610.11156) · arXiv 2610.11156

#### [Lightweight Systems for Spatial Semantic Segmentation of Sound Scenes](https://arxiv.org/abs/2610.12693)

- **日期：** 2026-10-08
- **问题 / 中文简述：** 定位与分离 · 轻量化部署；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2610.12693) · [PDF](https://arxiv.org/pdf/2610.12693) · arXiv 2610.12693

#### [SECURE-AI: Multi-Signal Uncertainty Quantification for Trustworthy Acoustic Cough Detection](https://arxiv.org/abs/2610.23937)

- **日期：** 2026-10-07
- **问题 / 中文简述：** 可解释与可靠性；采用数据驱动方法，面向医疗与生理声音解决可解释与可靠性问题。
- **来源：** [论文主页](https://arxiv.org/abs/2610.23937) · [PDF](https://arxiv.org/pdf/2610.23937) · arXiv 2610.23937

#### [Robust Prediction of Internal Wave-Affected Multi-Scale Sound Speed Distribution Using Lightweight Kolmogorov-Arnold Networks with Hybrid Basis Functions](https://arxiv.org/abs/2610.10877)

- **日期：** 2026-10-07
- **问题 / 中文简述：** 定位与分离 · 轻量化部署；采用数据驱动方法，面向交通与水下声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2610.10877) · [PDF](https://arxiv.org/pdf/2610.10877) · arXiv 2610.10877

#### [Listen-to-Reason: Listen with Experts, Retrieve over a Graph, Reason with LLMs](https://arxiv.org/abs/2610.10749)

- **日期：** 2026-10-07
- **问题 / 中文简述：** 多模态与基础模型；采用音频语言模型，面向环境与城市声音解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2610.10749) · [PDF](https://arxiv.org/pdf/2610.10749) · arXiv 2610.10749

#### [CARES: A Controlled Synthetic Benchmark of Speaker Reactions to Sound](https://arxiv.org/abs/2610.10208)

- **日期：** 2026-10-07
- **问题 / 中文简述：** 多模态与基础模型；采用音频语言模型，面向声音事件解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2610.10208) · [PDF](https://arxiv.org/pdf/2610.10208) · arXiv 2610.10208

#### [WorldSonus: Bringing Sound to Worlds](https://arxiv.org/abs/2610.08760)

- **日期：** 2026-10-06
- **问题 / 中文简述：** 通用检测与分类；采用数据增强与生成开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2610.08760) · [PDF](https://arxiv.org/pdf/2610.08760) · arXiv 2610.08760

#### [Logbook: Extremely Long-form Audio Event Understanding](https://arxiv.org/abs/2610.07338)

- **日期：** 2026-10-05
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2610.07338) · [PDF](https://arxiv.org/pdf/2610.07338) · arXiv 2610.07338

#### [Evaluating Inference-time Algorithms for Semantic Sound Scene Segmentation](https://arxiv.org/abs/2610.03602)

- **日期：** 2026-10-02
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2610.03602) · [PDF](https://arxiv.org/pdf/2610.03602) · arXiv 2610.03602

#### [RMS-AQA: A Two-Stage Spatial Audio Question Answering Benchmark for Real-World Domestic Environments](https://arxiv.org/abs/2610.00935)

- **日期：** 2026-10-01
- **问题 / 中文简述：** 定位与分离 · 多模态与基础模型 · 轻量化部署；采用音频语言模型，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2610.00935) · [PDF](https://arxiv.org/pdf/2610.00935) · arXiv 2610.00935

#### [AudioJev: Direct Audio Decisions with Order-Calibrated Probabilities](https://arxiv.org/abs/2610.01293)

- **日期：** 2026-10-01
- **问题 / 中文简述：** 可解释与可靠性；采用数据驱动方法，面向环境与城市声音解决可解释与可靠性问题。
- **来源：** [论文主页](https://arxiv.org/abs/2610.01293) · [PDF](https://arxiv.org/pdf/2610.01293) · arXiv 2610.01293

#### [When Capabilities Fail to Compose: Diagnosing the Compositionality Gap in Large Audio-Language Models](https://arxiv.org/abs/2609.36921)

- **日期：** 2026-09-29
- **问题 / 中文简述：** 多模态与基础模型；采用音频语言模型，面向环境与城市声音解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2609.36921) · [PDF](https://arxiv.org/pdf/2609.36921) · arXiv 2609.36921

#### [2-Dimensional spectral gating for denoising bioacoustics recordings](https://arxiv.org/abs/2609.37910)

- **日期：** 2026-09-29
- **问题 / 中文简述：** 低信噪比；采用数据驱动方法，面向生态与动物声音解决低信噪比问题。
- **来源：** [论文主页](https://arxiv.org/abs/2609.37910) · [PDF](https://arxiv.org/pdf/2609.37910) · arXiv 2609.37910

#### [Trigger Sound Suppression for Misophonia](https://arxiv.org/abs/2609.36351)

- **日期：** 2026-09-28
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展医疗与生理声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2609.36351) · [PDF](https://arxiv.org/pdf/2609.36351) · arXiv 2609.36351

#### [SAIL: Spatial Audio Intelligence with Large Language Models via Disentangled Acoustic-Spatial Encoding and Dual-Stream Q-Former](https://arxiv.org/abs/2609.34347)

- **日期：** 2026-09-28
- **问题 / 中文简述：** 定位与分离；采用音频语言模型，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2609.34347) · [PDF](https://arxiv.org/pdf/2609.34347) · arXiv 2609.34347

#### [Probing Large Audio-Language Models for Compositional Understanding of Sounding Actions](https://arxiv.org/abs/2609.35345)

- **日期：** 2026-09-28
- **问题 / 中文简述：** 多模态与基础模型；采用音频语言模型，面向声音事件解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2609.35345) · [PDF](https://arxiv.org/pdf/2609.35345) · arXiv 2609.35345

#### [On Temporal Binding in Large Audio Language Models](https://arxiv.org/abs/2609.34806)

- **日期：** 2026-09-28
- **问题 / 中文简述：** 定位与分离 · 多模态与基础模型；采用音频语言模型，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2609.34806) · [PDF](https://arxiv.org/pdf/2609.34806) · arXiv 2609.34806

#### [An Efficient Parametric Codec for Low-Bitrate First-Order Ambisonics](https://arxiv.org/abs/2609.33554)

- **日期：** 2026-09-27
- **问题 / 中文简述：** 定位与分离 · 轻量化部署；采用数据增强与生成，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2609.33554) · [PDF](https://arxiv.org/pdf/2609.33554) · arXiv 2609.33554

#### [VoxMem: Benchmarking Multimodal Memory in Large Audio Language Models](https://arxiv.org/abs/2609.32607)

- **日期：** 2026-09-26
- **问题 / 中文简述：** 多模态与基础模型；采用音频语言模型，面向环境与城市声音解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2609.32607) · [PDF](https://arxiv.org/pdf/2609.32607) · arXiv 2609.32607

#### [Binaural Audio-Visual Instance Segmentation](https://arxiv.org/abs/2609.32180)

- **日期：** 2026-09-26
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2609.32180) · [PDF](https://arxiv.org/pdf/2609.32180) · arXiv 2609.32180

#### [Symbiotic Architecture for Post-Hoc Audio Extension of Frozen Language Models](https://arxiv.org/abs/2609.30784)

- **日期：** 2026-09-25
- **问题 / 中文简述：** 多模态与基础模型；采用音频语言模型，面向环境与城市声音解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2609.30784) · [PDF](https://arxiv.org/pdf/2609.30784) · arXiv 2609.30784

#### [SAID: Semantic Acoustic Imaging Detector for Sound Event Localization and Detection](https://arxiv.org/abs/2609.31492)

- **日期：** 2026-09-25
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2609.31492) · [PDF](https://arxiv.org/pdf/2609.31492) · arXiv 2609.31492

#### [Towards Deployable Underwater Vessel Classification](https://arxiv.org/abs/2609.29179)

- **日期：** 2026-09-24
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向工业与机械声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2609.29179) · [PDF](https://arxiv.org/pdf/2609.29179) · arXiv 2609.29179

#### [AnomaSense: Anomaly-based Sensor Activation for Fine-Grained Human Activity Recognition](https://arxiv.org/abs/2609.28936)

- **日期：** 2026-09-24
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展工业与机械声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2609.28936) · [PDF](https://arxiv.org/pdf/2609.28936) · arXiv 2609.28936

#### [Do Audio Representations Compose Additively?](https://arxiv.org/abs/2609.27187)

- **日期：** 2026-09-23
- **问题 / 中文简述：** 多模态与基础模型；采用音频语言模型，面向环境与城市声音解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2609.27187) · [PDF](https://arxiv.org/pdf/2609.27187) · arXiv 2609.27187

#### [REVE: Efficient Hallucination Correction for Large Audio-Language Models via Reused Encoder States](https://arxiv.org/abs/2609.26028)

- **日期：** 2026-09-22
- **问题 / 中文简述：** 多模态与基础模型 · 轻量化部署；采用音频语言模型，面向声音事件解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2609.26028) · [PDF](https://arxiv.org/pdf/2609.26028) · arXiv 2609.26028

#### [MuLA-Bench: A Multilingual Long-Form Audio Understanding Benchmark via Multi-Tier Auditing](https://arxiv.org/abs/2609.23416)

- **日期：** 2026-09-20
- **问题 / 中文简述：** 跨域泛化 · 多模态与基础模型；采用音频语言模型，面向声音事件解决跨域泛化问题。
- **来源：** [论文主页](https://arxiv.org/abs/2609.23416) · [PDF](https://arxiv.org/pdf/2609.23416) · arXiv 2609.23416

#### [MoSAT: Human Motion Generation from Spatial Audio and Textual Description](https://arxiv.org/abs/2609.23797)

- **日期：** 2026-09-20
- **问题 / 中文简述：** 定位与分离；采用Transformer 表征，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2609.23797) · [PDF](https://arxiv.org/pdf/2609.23797) · arXiv 2609.23797

#### [Misrecognition or Abstraction? Rethinking Outputs of Sound Event Recognition](https://arxiv.org/abs/2609.23411)

- **日期：** 2026-09-20
- **问题 / 中文简述：** 可解释与可靠性；采用数据驱动方法，面向声音事件解决可解释与可靠性问题。
- **来源：** [论文主页](https://arxiv.org/abs/2609.23411) · [PDF](https://arxiv.org/pdf/2609.23411) · arXiv 2609.23411

#### [Normalise or condition? Noise-floor front-ends for on-board keyword spotting under UAV rotor ego-noise](https://arxiv.org/abs/2609.31699)

- **日期：** 2026-09-19
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展交通与水下声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2609.31699) · [PDF](https://arxiv.org/pdf/2609.31699) · arXiv 2609.31699

#### [EquiSELD: Efficient training of equivariant sound event localization and detection networks](https://arxiv.org/abs/2609.23156)

- **日期：** 2026-09-19
- **问题 / 中文简述：** 定位与分离 · 轻量化部署；采用Transformer 表征，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2609.23156) · [PDF](https://arxiv.org/pdf/2609.23156) · arXiv 2609.23156

#### [Bearings: Self-Supervised Soundfield Embeddings from First-Order Ambisonics](https://arxiv.org/abs/2609.23152)

- **日期：** 2026-09-19
- **问题 / 中文简述：** 定位与分离 · 轻量化部署；采用自监督表征，面向工业与机械声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2609.23152) · [PDF](https://arxiv.org/pdf/2609.23152) · arXiv 2609.23152

#### [The Unbearable Weight: Scaling Models and Methods for UAV Audio Classification](https://arxiv.org/abs/2609.17884)

- **日期：** 2026-09-15
- **问题 / 中文简述：** 轻量化部署；采用Transformer 表征，面向交通与水下声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2609.17884) · [PDF](https://arxiv.org/pdf/2609.17884) · arXiv 2609.17884

#### [The Internet Archive Music Dataset](https://arxiv.org/abs/2609.20870)

- **日期：** 2026-09-15
- **问题 / 中文简述：** 多模态与基础模型 · 可解释与可靠性 · 轻量化部署；采用音频语言模型，面向声音事件解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2609.20870) · [PDF](https://arxiv.org/pdf/2609.20870) · arXiv 2609.20870

#### [Parameter isolation with domain-specific experts for incremental audio classification](https://arxiv.org/abs/2609.14730)

- **日期：** 2026-09-13
- **问题 / 中文简述：** 跨域泛化 · 持续学习 · 轻量化部署；采用Transformer 表征，面向声音事件解决跨域泛化问题。
- **来源：** [论文主页](https://arxiv.org/abs/2609.14730) · [PDF](https://arxiv.org/pdf/2609.14730) · arXiv 2609.14730

#### [UniqueShip: Mitigating Data Leakage in Acoustic Ship Classification Benchmark Datasets](https://arxiv.org/abs/2609.13659)

- **日期：** 2026-09-12
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展工业与机械声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2609.13659) · [PDF](https://arxiv.org/pdf/2609.13659) · arXiv 2609.13659

#### [What Did the MLLM Hear? Token-Level Spectro-Temporal Grounding for Audio MLLM Explainability](https://arxiv.org/abs/2609.12663)

- **日期：** 2026-09-11
- **问题 / 中文简述：** 定位与分离 · 多模态与基础模型 · 可解释与可靠性 · 轻量化部署；采用音频语言模型，面向环境与城市声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2609.12663) · [PDF](https://arxiv.org/pdf/2609.12663) · arXiv 2609.12663

#### [Overview and Meta-Analysis of DCASE 2026 Challenge Task 6: Audio Moment Retrieval from Long Audio](https://arxiv.org/abs/2609.12484)

- **日期：** 2026-09-11
- **问题 / 中文简述：** 多模态与基础模型 · 可解释与可靠性；采用音频语言模型，面向环境与城市声音解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2609.12484) · [PDF](https://arxiv.org/pdf/2609.12484) · arXiv 2609.12484

#### [Investigating catastrophic forgetting in sound event classification](https://arxiv.org/abs/2609.11447)

- **日期：** 2026-09-10
- **问题 / 中文简述：** 持续学习 · 轻量化部署；采用数据驱动方法，面向声音事件解决持续学习问题。
- **来源：** [论文主页](https://arxiv.org/abs/2609.11447) · [PDF](https://arxiv.org/pdf/2609.11447) · arXiv 2609.11447

#### [SpeechAnnotator: A Context-Aware Multi-Agent Framework and Benchmark for Multidimensional Speech Annotation](https://arxiv.org/abs/2609.09947)

- **日期：** 2026-09-09
- **问题 / 中文简述：** 多模态与基础模型；采用数据驱动方法，面向环境与城市声音解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2609.09947) · [PDF](https://arxiv.org/pdf/2609.09947) · arXiv 2609.09947

#### [Bridging Echolocation Gaps in Automated Beaked Whale Tracking](https://arxiv.org/abs/2609.10768)

- **日期：** 2026-09-09
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2609.10768) · [PDF](https://arxiv.org/pdf/2609.10768) · arXiv 2609.10768

#### [Semantic Refinement of Universal Audio Representations through Audio-Description Alignment](https://arxiv.org/abs/2609.08429)

- **日期：** 2026-09-08
- **问题 / 中文简述：** 通用检测与分类；采用对比与原型学习开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2609.08429) · [PDF](https://arxiv.org/pdf/2609.08429) · arXiv 2609.08429

#### [TAD: Token-Adaptive Contrastive Decoding with Confidence-Guided Gating for Hallucination Mitigation in Large Audio-Language Models](https://arxiv.org/abs/2609.07286)

- **日期：** 2026-09-07
- **问题 / 中文简述：** 多模态与基础模型 · 可解释与可靠性；采用音频语言模型，面向声音事件解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2609.07286) · [PDF](https://arxiv.org/pdf/2609.07286) · arXiv 2609.07286

#### [Geometry-Informed Distributed Acoustic Scene Understanding](https://arxiv.org/abs/2609.08026)

- **日期：** 2026-09-07
- **问题 / 中文简述：** 通用检测与分类；采用音频语言模型开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2609.08026) · [PDF](https://arxiv.org/pdf/2609.08026) · arXiv 2609.08026

#### [Where Does the Sound Go? Tracing Acoustic Information Loss in Audio-Conditioned LLMs](https://arxiv.org/abs/2609.05871)

- **日期：** 2026-09-05
- **问题 / 中文简述：** 可解释与可靠性；采用音频语言模型，面向环境与城市声音解决可解释与可靠性问题。
- **来源：** [论文主页](https://arxiv.org/abs/2609.05871) · [PDF](https://arxiv.org/pdf/2609.05871) · arXiv 2609.05871

#### [SCAPES: Semantically Conditioned Autoregressive Prior for Environmental Sounds](https://arxiv.org/abs/2609.04634)

- **日期：** 2026-09-04
- **问题 / 中文简述：** 轻量化部署；采用数据增强与生成，面向工业与机械声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2609.04634) · [PDF](https://arxiv.org/pdf/2609.04634) · arXiv 2609.04634

#### [One-Stage Multi-Task Instruction-Guided 3D Spatial Audio Editing](https://arxiv.org/abs/2609.04975)

- **日期：** 2026-09-04
- **问题 / 中文简述：** 定位与分离；采用层级与多任务学习，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2609.04975) · [PDF](https://arxiv.org/pdf/2609.04975) · arXiv 2609.04975

#### [Removing Speech, Keeping Activities: Speech Removal for Privacy-Preserving Acoustic Sensing in Assisted Living](https://arxiv.org/abs/2609.02376)

- **日期：** 2026-09-02
- **问题 / 中文简述：** 定位与分离；采用数据增强与生成，面向环境与城市声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2609.02376) · [PDF](https://arxiv.org/pdf/2609.02376) · arXiv 2609.02376

#### [MADS: A Multiview Acoustic Descriptor Set Beyond Standard Spectral Summaries](https://arxiv.org/abs/2609.00792)

- **日期：** 2026-09-01
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展工业与机械声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2609.00792) · [PDF](https://arxiv.org/pdf/2609.00792) · arXiv 2609.00792

#### [Efficient Passive Acoustic Monitoring of Killer Whales Using a Two-Stage Detection and Ecotype Classification Cascade](https://arxiv.org/abs/2609.01792)

- **日期：** 2026-09-01
- **问题 / 中文简述：** 长尾与不平衡 · 轻量化部署；采用数据驱动方法，面向生态与动物声音解决长尾与不平衡问题。
- **来源：** [论文主页](https://arxiv.org/abs/2609.01792) · [PDF](https://arxiv.org/pdf/2609.01792) · arXiv 2609.01792

#### [XVAE-WMT: Explainable Wavelet-Temporal Variational Autoencoder for Blind Source Separation of Heart and Lung Sounds](https://arxiv.org/abs/2609.00238)

- **日期：** 2026-08-31
- **问题 / 中文简述：** 定位与分离 · 可解释与可靠性；采用数据增强与生成，面向医疗与生理声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2609.00238) · [PDF](https://arxiv.org/pdf/2609.00238) · arXiv 2609.00238

#### [DreamX-Creator: Democratizing Native Audio-Video Generation at 2K Resolution](https://arxiv.org/abs/2608.31106)

- **日期：** 2026-08-31
- **问题 / 中文简述：** 低信噪比 · 多模态与基础模型；采用Transformer 表征，面向声音事件解决低信噪比问题。
- **来源：** [论文主页](https://arxiv.org/abs/2608.31106) · [PDF](https://arxiv.org/pdf/2608.31106) · arXiv 2608.31106

#### [Zero-Shot Respiratory Sound Classification through LLM-Augmented Audio-Text Alignment](https://arxiv.org/abs/2609.00055)

- **日期：** 2026-08-30
- **问题 / 中文简述：** 开放集/OOD · 多模态与基础模型；采用音频语言模型，面向医疗与生理声音解决开放集/OOD问题。
- **来源：** [论文主页](https://arxiv.org/abs/2609.00055) · [PDF](https://arxiv.org/pdf/2609.00055) · arXiv 2609.00055

#### [SPECTRA: Subspace-Preserving Embedding Calibration, Transport, and Replay for Fully Few-Shot Class-Incremental Audio Classification](https://arxiv.org/abs/2608.25054)

- **日期：** 2026-08-25
- **问题 / 中文简述：** 少样本 · 持续学习 · 可解释与可靠性 · 轻量化部署；采用对比与原型学习，面向声音事件解决少样本问题。
- **来源：** [论文主页](https://arxiv.org/abs/2608.25054) · [PDF](https://arxiv.org/pdf/2608.25054) · arXiv 2608.25054

#### [CoSTALA: Compositional Spatio-Temporal Audio-Language Alignment via Multi-Grain Hierarchical Contrastive Learning](https://arxiv.org/abs/2608.24374)

- **日期：** 2026-08-25
- **问题 / 中文简述：** 定位与分离 · 多模态与基础模型；采用音频语言模型，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2608.24374) · [PDF](https://arxiv.org/pdf/2608.24374) · arXiv 2608.24374

#### [AT-ADD: A Benchmark and Challenge for Robust and All-Type Audio Deepfake Detection](https://arxiv.org/abs/2608.23437)

- **日期：** 2026-08-24
- **问题 / 中文简述：** 通用检测与分类；采用自监督表征开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2608.23437) · [PDF](https://arxiv.org/pdf/2608.23437) · arXiv 2608.23437

#### [MRMAD: A Multi-Round Multi-Audio Benchmark for Evaluating Acoustic Degradation Perception in Large Audio-Language Models](https://arxiv.org/abs/2608.22236)

- **日期：** 2026-08-23
- **问题 / 中文简述：** 多模态与基础模型；采用音频语言模型，面向声音事件解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2608.22236) · [PDF](https://arxiv.org/pdf/2608.22236) · arXiv 2608.22236

#### [FlowSep 2: Self-Supervised Flow Matching for Language-Queried Audio Source Separation](https://arxiv.org/abs/2608.22111)

- **日期：** 2026-08-22
- **问题 / 中文简述：** 定位与分离；采用自监督表征，面向环境与城市声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2608.22111) · [PDF](https://arxiv.org/pdf/2608.22111) · arXiv 2608.22111

#### [Dancing Through Soundscapes: Designing a Low-Cost, Sound-Based Device for Sensing and Interpreting Movement and Dance](https://arxiv.org/abs/2608.19827)

- **日期：** 2026-08-20
- **问题 / 中文简述：** 通用检测与分类；采用数据增强与生成开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2608.19827) · [PDF](https://arxiv.org/pdf/2608.19827) · arXiv 2608.19827

#### [UniVerse: Benchmarking and Enhancing LALMs on Culturally Inclusive Low-Resource Music Understanding](https://arxiv.org/abs/2608.17852)

- **日期：** 2026-08-18
- **问题 / 中文简述：** 少样本 · 多模态与基础模型；采用音频语言模型，面向声音事件解决少样本问题。
- **来源：** [论文主页](https://arxiv.org/abs/2608.17852) · [PDF](https://arxiv.org/pdf/2608.17852) · arXiv 2608.17852

#### [Listen, Reason, and Segment: Aligning LALMs with Editorial Judgment for Media Chapterization](https://arxiv.org/abs/2608.16539)

- **日期：** 2026-08-17
- **问题 / 中文简述：** 多模态与基础模型；采用音频语言模型，面向声音事件解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2608.16539) · [PDF](https://arxiv.org/pdf/2608.16539) · arXiv 2608.16539

#### [INSPIRE: A Benchmark for Instruction-Aware Speech Retrieval](https://arxiv.org/abs/2608.16203)

- **日期：** 2026-08-17
- **问题 / 中文简述：** 多模态与基础模型；采用音频语言模型，面向环境与城市声音解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2608.16203) · [PDF](https://arxiv.org/pdf/2608.16203) · arXiv 2608.16203

#### [ARENA: Automated Red-Teaming for Large Audio Language Models](https://arxiv.org/abs/2608.15578)

- **日期：** 2026-08-16
- **问题 / 中文简述：** 多模态与基础模型；采用音频语言模型，面向环境与城市声音解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2608.15578) · [PDF](https://arxiv.org/pdf/2608.15578) · arXiv 2608.15578

#### ["What's That Sound?": A Versatile, Robust, and Lightweight Convolutional Transformer for Environment Sound Recognition](https://arxiv.org/abs/2609.27762)

- **日期：** 2026-08-16
- **问题 / 中文简述：** 轻量化部署；采用Transformer 表征，面向工业与机械声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2609.27762) · [PDF](https://arxiv.org/pdf/2609.27762) · arXiv 2609.27762

#### [AT-ADD: All-Type Audio Deepfake Detection Challenge Summary](https://arxiv.org/abs/2608.14249)

- **日期：** 2026-08-14
- **问题 / 中文简述：** 通用检测与分类；采用自监督表征开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2608.14249) · [PDF](https://arxiv.org/pdf/2608.14249) · arXiv 2608.14249

#### [VoxAudio: Vocalized Audio Synthesis via Multi-Reward Autoregressive Flow Matching](https://arxiv.org/abs/2608.12951)

- **日期：** 2026-08-13
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向环境与城市声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2608.12951) · [PDF](https://arxiv.org/pdf/2608.12951) · arXiv 2608.12951

#### [DINO-A: Adapting Self-Distillation Vision Transformers to General Audio Representation Learning](https://arxiv.org/abs/2608.10659)

- **日期：** 2026-08-11
- **问题 / 中文简述：** 轻量化部署；采用自监督表征，面向环境与城市声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2608.10659) · [PDF](https://arxiv.org/pdf/2608.10659) · arXiv 2608.10659

#### [Physics-Informed Learning for Robust Acoustic Localization with Calibrated Uncertainty](https://arxiv.org/abs/2608.08911)

- **日期：** 2026-08-09
- **问题 / 中文简述：** 定位与分离 · 可解释与可靠性；采用数据驱动方法，面向生态与动物声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2608.08911) · [PDF](https://arxiv.org/pdf/2608.08911) · arXiv 2608.08911

#### [MMAG: A Multi-Control Mixed Audio Generation Benchmark](https://arxiv.org/abs/2608.06900)

- **日期：** 2026-08-07
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2608.06900) · [PDF](https://arxiv.org/pdf/2608.06900) · arXiv 2608.06900

#### [Smartphone Audio Based Distress Detection](https://arxiv.org/abs/2608.04176)

- **日期：** 2026-08-04
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展工业与机械声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2608.04176) · [PDF](https://arxiv.org/pdf/2608.04176) · arXiv 2608.04176

#### [Hear to See: Discerning Stateful Listening for Audio-Visual Instance Segmentation](https://arxiv.org/abs/2608.03264)

- **日期：** 2026-08-04
- **问题 / 中文简述：** 通用检测与分类；采用层级与多任务学习开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2608.03264) · [PDF](https://arxiv.org/pdf/2608.03264) · arXiv 2608.03264

#### [Deep Learning for Real-Time Sound Order Recognition in Human-Robot Interaction](https://arxiv.org/abs/2608.04072)

- **日期：** 2026-08-04
- **问题 / 中文简述：** 轻量化部署；采用Transformer 表征，面向声音事件解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2608.04072) · [PDF](https://arxiv.org/pdf/2608.04072) · arXiv 2608.04072

#### [SwanTale: Unified Multi-Speaker Speech and Audio Generation for Instruct and Zero-Shot Tasks](https://arxiv.org/abs/2608.02023)

- **日期：** 2026-08-03
- **问题 / 中文简述：** 开放集/OOD；采用层级与多任务学习，面向环境与城市声音解决开放集/OOD问题。
- **来源：** [论文主页](https://arxiv.org/abs/2608.02023) · [PDF](https://arxiv.org/pdf/2608.02023) · arXiv 2608.02023

#### [Can Foundation Models Hear What Made That Sound? A Tiered Benchmark of Audio-Language Models and Traditional Classifiers for Closed-Set Sound Source Identification](https://arxiv.org/abs/2608.02397)

- **日期：** 2026-08-03
- **问题 / 中文简述：** 开放集/OOD · 多模态与基础模型 · 可解释与可靠性；采用音频语言模型，面向声音事件解决开放集/OOD问题。
- **来源：** [论文主页](https://arxiv.org/abs/2608.02397) · [PDF](https://arxiv.org/pdf/2608.02397) · arXiv 2608.02397

#### [AcoustiTrace: When Plausible Sound Violates Physics](https://arxiv.org/abs/2608.02035)

- **日期：** 2026-08-03
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2608.02035) · [PDF](https://arxiv.org/pdf/2608.02035) · arXiv 2608.02035

#### [Hidden-Domain Routing for All-Type Audio Deepfake Detection](https://arxiv.org/abs/2608.00493)

- **日期：** 2026-08-01
- **问题 / 中文简述：** 跨域泛化 · 定位与分离；采用数据驱动方法，面向环境与城市声音解决跨域泛化问题。
- **来源：** [论文主页](https://arxiv.org/abs/2608.00493) · [PDF](https://arxiv.org/pdf/2608.00493) · arXiv 2608.00493

#### [DRONEAUDIONET: Noise Suppression for Drone Audition-based Search and Rescue](https://arxiv.org/abs/2608.00875)

- **日期：** 2026-08-01
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向生态与动物声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2608.00875) · [PDF](https://arxiv.org/pdf/2608.00875) · arXiv 2608.00875

#### [Few-Shot Open-Set Audio Classification via Transductive Prototype Refinement and Class Logit Enhancement](https://arxiv.org/abs/2607.26607)

- **日期：** 2026-07-29
- **问题 / 中文简述：** 少样本 · 开放集/OOD；采用对比与原型学习，面向声音事件解决少样本问题。
- **来源：** [论文主页](https://arxiv.org/abs/2607.26607) · [PDF](https://arxiv.org/pdf/2607.26607) · arXiv 2607.26607

#### [Device Invariance using Domain Adaptation on Acoustic Scene Classification](https://arxiv.org/abs/2607.25887)

- **日期：** 2026-07-28
- **问题 / 中文简述：** 跨域泛化；采用Transformer 表征，面向环境与城市声音解决跨域泛化问题。
- **来源：** [论文主页](https://arxiv.org/abs/2607.25887) · [PDF](https://arxiv.org/pdf/2607.25887) · arXiv 2607.25887

#### [PathRIR: Physics-Guided Acoustic Path Selection and Late-Tail Compensation for Fast Room Impulse Response Simulation](https://arxiv.org/abs/2607.23293)

- **日期：** 2026-07-25
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向环境与城市声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2607.23293) · [PDF](https://arxiv.org/pdf/2607.23293) · arXiv 2607.23293

#### [Music Hallucination in Audio-Language Models: A Hierarchical Formulation and Empirical Study](https://arxiv.org/abs/2609.20195)

- **日期：** 2026-07-24
- **问题 / 中文简述：** 多模态与基础模型 · 轻量化部署；采用音频语言模型，面向声音事件解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2609.20195) · [PDF](https://arxiv.org/pdf/2609.20195) · arXiv 2609.20195

#### [An Evaluation Framework for Structured Audio Captions Validated by Controlled Perturbations](https://arxiv.org/abs/2607.21424)

- **日期：** 2026-07-23
- **问题 / 中文简述：** 通用检测与分类；采用音频语言模型开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2607.21424) · [PDF](https://arxiv.org/pdf/2607.21424) · arXiv 2607.21424

#### [RealDESED: A Real-World Domestic Sound Event Detection Benchmark](https://arxiv.org/abs/2607.16736)

- **日期：** 2026-07-18
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2607.16736) · [PDF](https://arxiv.org/pdf/2607.16736) · arXiv 2607.16736

#### [Component-Level Ensemble Fusion for Speech and Environmental Sound Deepfake Detection](https://arxiv.org/abs/2607.16369)

- **日期：** 2026-07-17
- **问题 / 中文简述：** 可解释与可靠性 · 轻量化部署；采用数据驱动方法，面向环境与城市声音解决可解释与可靠性问题。
- **来源：** [论文主页](https://arxiv.org/abs/2607.16369) · [PDF](https://arxiv.org/pdf/2607.16369) · arXiv 2607.16369

#### [Improving Text-to-Audio Instruction Following via Fine-Grained Feedback from Audio-Aware Large Language Models](https://arxiv.org/abs/2607.13408)

- **日期：** 2026-07-15
- **问题 / 中文简述：** 通用检测与分类；采用音频语言模型开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2607.13408) · [PDF](https://arxiv.org/pdf/2607.13408) · arXiv 2607.13408

#### [Cover First, Disagree Softly: Rethinking Mismatch-First Active Learning for Frame-Level Audio Classification](https://arxiv.org/abs/2607.13571)

- **日期：** 2026-07-15
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2607.13571) · [PDF](https://arxiv.org/pdf/2607.13571) · arXiv 2607.13571

#### [The Sound of Absence: Audio-Language Embedding Models Struggle with Negation](https://arxiv.org/abs/2607.12290)

- **日期：** 2026-07-14
- **问题 / 中文简述：** 多模态与基础模型；采用音频语言模型，面向声音事件解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2607.12290) · [PDF](https://arxiv.org/pdf/2607.12290) · arXiv 2607.12290

#### [PC-Mix: Partial-Component Audio Spoofing Detection under Mixed Speech and Environmental Sound Conditions](https://arxiv.org/abs/2607.10345)

- **日期：** 2026-07-11
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向环境与城市声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2607.10345) · [PDF](https://arxiv.org/pdf/2607.10345) · arXiv 2607.10345

#### [From Sound to Symptom: Real-Time Respiratory Signal Understanding for Conversational Healthcare Agents](https://arxiv.org/abs/2608.26163)

- **日期：** 2026-07-10
- **问题 / 中文简述：** 定位与分离 · 多模态与基础模型 · 可解释与可靠性 · 轻量化部署；采用音频语言模型，面向医疗与生理声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2608.26163) · [PDF](https://arxiv.org/pdf/2608.26163) · arXiv 2608.26163

#### [A Production-Oriented Framework for Evaluation of SFX Generation](https://arxiv.org/abs/2607.09973)

- **日期：** 2026-07-10
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向工业与机械声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2607.09973) · [PDF](https://arxiv.org/pdf/2607.09973) · arXiv 2607.09973

#### [ForestIR: Physics-Informed Forest Sound Simulation for Array-Based Bioacoustic Remote Sensing](https://arxiv.org/abs/2607.06299)

- **日期：** 2026-07-07
- **问题 / 中文简述：** 定位与分离；采用数据增强与生成，面向生态与动物声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2607.06299) · [PDF](https://arxiv.org/pdf/2607.06299) · arXiv 2607.06299

#### [A Self-Supervised Approach for Minimal-Annotation Hydroacoustic Data Exploration](https://arxiv.org/abs/2607.07733)

- **日期：** 2026-07-07
- **问题 / 中文简述：** 通用检测与分类；采用自监督表征开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2607.07733) · [PDF](https://arxiv.org/pdf/2607.07733) · arXiv 2607.07733

#### [Adaptive Diversity-Uncertainty Active Learning with Redundancy Control for Bioacoustic Event Classification](https://arxiv.org/abs/2607.04868)

- **日期：** 2026-07-06
- **问题 / 中文简述：** 可解释与可靠性；采用数据驱动方法，面向生态与动物声音解决可解释与可靠性问题。
- **来源：** [论文主页](https://arxiv.org/abs/2607.04868) · [PDF](https://arxiv.org/pdf/2607.04868) · arXiv 2607.04868

#### [Sampling Bias Compensation for Robust Evaluation of Audio Classification Systems with Partially Labeled Evaluation Datasets](https://arxiv.org/abs/2607.04463)

- **日期：** 2026-07-05
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展工业与机械声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2607.04463) · [PDF](https://arxiv.org/pdf/2607.04463) · arXiv 2607.04463

#### [Doppelganger: Sound Effects and Their Synthetic Twins](https://arxiv.org/abs/2607.04337)

- **日期：** 2026-07-05
- **问题 / 中文简述：** 通用检测与分类；采用数据增强与生成开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2607.04337) · [PDF](https://arxiv.org/pdf/2607.04337) · arXiv 2607.04337

#### [Auto-AEG: Scalable Data Construction for Open-Vocabulary Audio Event Grounding](https://arxiv.org/abs/2607.04383)

- **日期：** 2026-07-05
- **问题 / 中文简述：** 半/弱监督 · 定位与分离 · 多模态与基础模型；采用音频语言模型，面向声音事件解决半/弱监督问题。
- **来源：** [论文主页](https://arxiv.org/abs/2607.04383) · [PDF](https://arxiv.org/pdf/2607.04383) · arXiv 2607.04383

#### [Trajectory Variance: An Unsupervised Measure of Developmental Vocal Plasticity in Birdsong](https://arxiv.org/abs/2607.03496)

- **日期：** 2026-07-03
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向生态与动物声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2607.03496) · [PDF](https://arxiv.org/pdf/2607.03496) · arXiv 2607.03496

#### [SelectTSL: Prompt-Guided Selective Target Sound Localization in Complex Scenarios](https://arxiv.org/abs/2607.02343)

- **日期：** 2026-07-02
- **问题 / 中文简述：** 定位与分离 · 多模态与基础模型；采用Transformer 表征，面向环境与城市声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2607.02343) · [PDF](https://arxiv.org/pdf/2607.02343) · arXiv 2607.02343

#### [Neural Audio Codec with Adjustable Token Temporal Resolution Using Sampling-Frequency-Independent Convolutional Layers](https://arxiv.org/abs/2607.01865)

- **日期：** 2026-07-02
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2607.01865) · [PDF](https://arxiv.org/pdf/2607.01865) · arXiv 2607.01865

#### [A Multi-Branch Hierarchy-Aware Framework for Heterogeneous Audio Classification](https://arxiv.org/abs/2607.01974)

- **日期：** 2026-07-02
- **问题 / 中文简述：** 多模态与基础模型；采用音频语言模型，面向声音事件解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2607.01974) · [PDF](https://arxiv.org/pdf/2607.01974) · arXiv 2607.01974

#### [CNN Models for Microphone Array Covariance Matrix Upsampling and Acoustic Imaging](https://arxiv.org/abs/2607.01295)

- **日期：** 2026-07-01
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2607.01295) · [PDF](https://arxiv.org/pdf/2607.01295) · arXiv 2607.01295

#### [ZEBRA: Zero-Shot Entropy-Regularized Prompt Learning for Base-to-Novel Generalization in Audio-Language Models](https://arxiv.org/abs/2606.31587)

- **日期：** 2026-06-30
- **问题 / 中文简述：** 少样本 · 开放集/OOD · 多模态与基础模型；采用音频语言模型，面向声音事件解决少样本问题。
- **来源：** [论文主页](https://arxiv.org/abs/2606.31587) · [PDF](https://arxiv.org/pdf/2606.31587) · arXiv 2606.31587

#### [BEST-RQ-2: Contextualize-Then-Predict, a Two-Step Approach for Self-Supervised Audio Representations](https://arxiv.org/abs/2606.30700)

- **日期：** 2026-06-29
- **问题 / 中文简述：** 跨域泛化 · 轻量化部署；采用自监督表征，面向环境与城市声音解决跨域泛化问题。
- **来源：** [论文主页](https://arxiv.org/abs/2606.30700) · [PDF](https://arxiv.org/pdf/2606.30700) · arXiv 2606.30700

#### [EchoHawk: A Reproducible Acoustic Pipeline for Drone Detection, Classification, and Direction-Finding, with a Cautionary Study of Session-Level Data Leakage](https://arxiv.org/abs/2606.29589)

- **日期：** 2026-06-28
- **问题 / 中文简述：** 通用检测与分类；采用数据增强与生成开展交通与水下声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2606.29589) · [PDF](https://arxiv.org/pdf/2606.29589) · arXiv 2606.29589

#### [Underwater Source Detection and Classification for Signal-based Surveillance: Audio Dataset Curation and Cross-Domain Evaluation](https://arxiv.org/abs/2606.28988)

- **日期：** 2026-06-27
- **问题 / 中文简述：** 跨域泛化 · 开放集/OOD · 轻量化部署；采用数据驱动方法，面向工业与机械声音解决跨域泛化问题。
- **来源：** [论文主页](https://arxiv.org/abs/2606.28988) · [PDF](https://arxiv.org/pdf/2606.28988) · arXiv 2606.28988

#### [From General-Purpose Audio Tagging to Spatially Grounded Sound Event Localization and Detection](https://arxiv.org/abs/2606.27751)

- **日期：** 2026-06-26
- **问题 / 中文简述：** 定位与分离 · 可解释与可靠性；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2606.27751) · [PDF](https://arxiv.org/pdf/2606.27751) · arXiv 2606.27751

#### [Soroll-IA: A Weakly Labeled Audio Dataset for Real-World Industrial Port Monitoring](https://arxiv.org/abs/2606.26195)

- **日期：** 2026-06-24
- **问题 / 中文简述：** 少样本 · 半/弱监督 · 定位与分离 · 轻量化部署；采用数据驱动方法，面向工业与机械声音解决少样本问题。
- **来源：** [论文主页](https://arxiv.org/abs/2606.26195) · [PDF](https://arxiv.org/pdf/2606.26195) · arXiv 2606.26195

#### [From Sounds to Scenes: A Benchmark for Evaluating Context-Aware Auditory Scene Understanding in Large Audio Language Models](https://arxiv.org/abs/2606.25391)

- **日期：** 2026-06-24
- **问题 / 中文简述：** 多模态与基础模型；采用音频语言模型，面向交通与水下声音解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2606.25391) · [PDF](https://arxiv.org/pdf/2606.25391) · arXiv 2606.25391

#### [Unlocking Spatial Grounding in Large Audio-Visual Retrieval models](https://arxiv.org/abs/2607.24786)

- **日期：** 2026-06-22
- **问题 / 中文简述：** 半/弱监督 · 定位与分离 · 多模态与基础模型 · 轻量化部署；采用数据驱动方法，面向声音事件解决半/弱监督问题。
- **来源：** [论文主页](https://arxiv.org/abs/2607.24786) · [PDF](https://arxiv.org/pdf/2607.24786) · arXiv 2607.24786

#### [Improving Engine Sound Analysis in Hot-Test Environments via a RAB-U-Net (Residual Attention Block U-Net) Noise Removal Method](https://arxiv.org/abs/2606.21887)

- **日期：** 2026-06-20
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2606.21887) · [PDF](https://arxiv.org/pdf/2606.21887) · arXiv 2606.21887

#### [An Analysis of Untrained Deep Reservoir Networks for Audio Surveillance](https://arxiv.org/abs/2606.22218)

- **日期：** 2026-06-20
- **问题 / 中文简述：** 低信噪比 · 轻量化部署；采用数据驱动方法，面向声音事件解决低信噪比问题。
- **来源：** [论文主页](https://arxiv.org/abs/2606.22218) · [PDF](https://arxiv.org/pdf/2606.22218) · arXiv 2606.22218

#### [Towards Detecting Neural Audio Codec Synthesized Heart Sounds](https://arxiv.org/abs/2606.21727)

- **日期：** 2026-06-19
- **问题 / 中文简述：** 通用检测与分类；采用自监督表征开展医疗与生理声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2606.21727) · [PDF](https://arxiv.org/pdf/2606.21727) · arXiv 2606.21727

#### [Gradient-Based Learning of Parametric Engine Sound Representations for Real-Time Resynthesis and Tuning on Embedded Systems](https://arxiv.org/abs/2606.21521)

- **日期：** 2026-06-19
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向工业与机械声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2606.21521) · [PDF](https://arxiv.org/pdf/2606.21521) · arXiv 2606.21521

#### [CoughPhase-CLR: Designing an acoustics-informed foundation model for coughing sound classification](https://arxiv.org/abs/2606.21411)

- **日期：** 2026-06-19
- **问题 / 中文简述：** 多模态与基础模型；采用自监督表征，面向医疗与生理声音解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2606.21411) · [PDF](https://arxiv.org/pdf/2606.21411) · arXiv 2606.21411

#### [RFM-Editing 2: Text-Guided Audio Editing with Rectified Flow Matching and Coarse-to-Fine Diffusion Transformers](https://arxiv.org/abs/2606.20101)

- **日期：** 2026-06-18
- **问题 / 中文简述：** 定位与分离 · 多模态与基础模型 · 轻量化部署；采用Transformer 表征，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2606.20101) · [PDF](https://arxiv.org/pdf/2606.20101) · arXiv 2606.20101

#### [MixProLAP: Mixture-Induced Uncertainty Modeling for Probabilistic Language-Audio Pretraining](https://arxiv.org/abs/2606.20418)

- **日期：** 2026-06-18
- **问题 / 中文简述：** 多模态与基础模型 · 可解释与可靠性；采用音频语言模型，面向环境与城市声音解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2606.20418) · [PDF](https://arxiv.org/pdf/2606.20418) · arXiv 2606.20418

#### [Exploiting Neural Audio Codec Latents for Adversarial Audio Attacks](https://arxiv.org/abs/2606.20893)

- **日期：** 2026-06-18
- **问题 / 中文简述：** 通用检测与分类；采用数据增强与生成开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2606.20893) · [PDF](https://arxiv.org/pdf/2606.20893) · arXiv 2606.20893

#### [NeuralMUSIC: A Hybrid Neural-Subspace Framework for Robot Sound Source Localization](https://arxiv.org/abs/2606.18664)

- **日期：** 2026-06-17
- **问题 / 中文简述：** 跨域泛化 · 定位与分离；采用自监督表征，面向声音事件解决跨域泛化问题。
- **来源：** [论文主页](https://arxiv.org/abs/2606.18664) · [PDF](https://arxiv.org/pdf/2606.18664) · arXiv 2606.18664

#### [Exploring Feature Extraction Technique Parameters for Acoustic Gunshot Classification](https://arxiv.org/abs/2606.19568)

- **日期：** 2026-06-17
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2606.19568) · [PDF](https://arxiv.org/pdf/2606.19568) · arXiv 2606.19568

#### [ELSA: Acoustic Event-Level Semantic Alignment for Fine-Grained Reference-Free Text-to-Audio Evaluation](https://arxiv.org/abs/2606.17404)

- **日期：** 2026-06-16
- **问题 / 中文简述：** 多模态与基础模型；采用音频语言模型，面向声音事件解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2606.17404) · [PDF](https://arxiv.org/pdf/2606.17404) · arXiv 2606.17404

#### [Descriptor: Certus Caliber Classification Gunshot Dataset (C3GD)](https://arxiv.org/abs/2606.18135)

- **日期：** 2026-06-16
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2606.18135) · [PDF](https://arxiv.org/pdf/2606.18135) · arXiv 2606.18135

#### [A Neuromorphic Trigger for Efficient Audio Event Detection](https://arxiv.org/abs/2606.17775)

- **日期：** 2026-06-16
- **问题 / 中文简述：** 可解释与可靠性 · 轻量化部署；采用数据驱动方法，面向环境与城市声音解决可解释与可靠性问题。
- **来源：** [论文主页](https://arxiv.org/abs/2606.17775) · [PDF](https://arxiv.org/pdf/2606.17775) · arXiv 2606.17775

#### [Transductive Zero-Shot Audio Classification with Audio-Language Models](https://arxiv.org/abs/2606.17160)

- **日期：** 2026-06-15
- **问题 / 中文简述：** 长尾与不平衡 · 开放集/OOD · 多模态与基础模型；采用音频语言模型，面向环境与城市声音解决长尾与不平衡问题。
- **来源：** [论文主页](https://arxiv.org/abs/2606.17160) · [PDF](https://arxiv.org/pdf/2606.17160) · arXiv 2606.17160

#### [MambAdapter: Lightweight Mamba-Based Adapters for Parameter-Efficient Transfer Learning in Speech and Audio](https://arxiv.org/abs/2606.15638)

- **日期：** 2026-06-14
- **问题 / 中文简述：** 跨域泛化 · 多模态与基础模型 · 轻量化部署；采用Transformer 表征，面向声音事件解决跨域泛化问题。
- **来源：** [论文主页](https://arxiv.org/abs/2606.15638) · [PDF](https://arxiv.org/pdf/2606.15638) · arXiv 2606.15638

#### [Acoustic Prompting via Stage-wise Modulation for Few-Shot Learning in Audio Language Models](https://arxiv.org/abs/2606.15751)

- **日期：** 2026-06-14
- **问题 / 中文简述：** 少样本 · 开放集/OOD · 多模态与基础模型；采用音频语言模型，面向声音事件解决少样本问题。
- **来源：** [论文主页](https://arxiv.org/abs/2606.15751) · [PDF](https://arxiv.org/pdf/2606.15751) · arXiv 2606.15751

#### [Spatio-Temporal Audio Language Modeling for Dynamic Sound Sources](https://arxiv.org/abs/2606.14141)

- **日期：** 2026-06-12
- **问题 / 中文简述：** 开放集/OOD · 定位与分离 · 多模态与基础模型；采用音频语言模型，面向声音事件解决开放集/OOD问题。
- **来源：** [论文主页](https://arxiv.org/abs/2606.14141) · [PDF](https://arxiv.org/pdf/2606.14141) · arXiv 2606.14141

#### [Comparing Spectrogram Front-Ends for Abnormal Heart-Sound Detection with a Convolutional Neural Network](https://arxiv.org/abs/2607.16220)

- **日期：** 2026-06-12
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向医疗与生理声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2607.16220) · [PDF](https://arxiv.org/pdf/2607.16220) · arXiv 2607.16220

#### [Quality Adaptive Angular Margin Learning for Respiratory Sound Classification](https://arxiv.org/abs/2606.11915)

- **日期：** 2026-06-10
- **问题 / 中文简述：** 长尾与不平衡 · 开放集/OOD；采用数据驱动方法，面向医疗与生理声音解决长尾与不平衡问题。
- **来源：** [论文主页](https://arxiv.org/abs/2606.11915) · [PDF](https://arxiv.org/pdf/2606.11915) · arXiv 2606.11915

#### [Lung-SRAD: Spectral-Aware Regularized Audio DASS with Dual-Axis Patch-Mix Contrastive Learning for Respiratory Sound Classification](https://arxiv.org/abs/2606.11922)

- **日期：** 2026-06-10
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展医疗与生理声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2606.11922) · [PDF](https://arxiv.org/pdf/2606.11922) · arXiv 2606.11922

#### [Dolph2Vec: Self-Supervised Representations of Dolphin Vocalizations](https://arxiv.org/abs/2606.12503)

- **日期：** 2026-06-10
- **问题 / 中文简述：** 通用检测与分类；采用自监督表征开展生态与动物声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2606.12503) · [PDF](https://arxiv.org/pdf/2606.12503) · arXiv 2606.12503

#### [Steering Where to Listen: Instruction-Based Activation Steering Redirects Temporal Attention in Large Audio-Language Models](https://arxiv.org/abs/2606.11400)

- **日期：** 2026-06-09
- **问题 / 中文简述：** 多模态与基础模型；采用音频语言模型，面向声音事件解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2606.11400) · [PDF](https://arxiv.org/pdf/2606.11400) · arXiv 2606.11400

#### [Overview of ESDD2: Environment-Aware Speech and Sound Deepfake Detection Challenge](https://arxiv.org/abs/2606.10791)

- **日期：** 2026-06-09
- **问题 / 中文简述：** 跨域泛化 · 定位与分离；采用自监督表征，面向环境与城市声音解决跨域泛化问题。
- **来源：** [论文主页](https://arxiv.org/abs/2606.10791) · [PDF](https://arxiv.org/pdf/2606.10791) · arXiv 2606.10791

#### [RespiraMFM: A Multimodal Foundation Model with Contrastive Audio-Language Alignment for Respiratory Disease Identification](https://arxiv.org/abs/2606.09966)

- **日期：** 2026-06-08
- **问题 / 中文简述：** 开放集/OOD · 多模态与基础模型；采用音频语言模型，面向医疗与生理声音解决开放集/OOD问题。
- **来源：** [论文主页](https://arxiv.org/abs/2606.09966) · [PDF](https://arxiv.org/pdf/2606.09966) · arXiv 2606.09966

#### [Towards Event-Robust Acoustic Scene Classification](https://arxiv.org/abs/2606.06921)

- **日期：** 2026-06-05
- **问题 / 中文简述：** 通用检测与分类；采用音频语言模型开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2606.06921) · [PDF](https://arxiv.org/pdf/2606.06921) · arXiv 2606.06921

#### [MyGardenBird: A Machine-Learning-Ready Bird Sound Dataset for Twelve Common Malaysian Birds](https://arxiv.org/abs/2606.06975)

- **日期：** 2026-06-05
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2606.06975) · [PDF](https://arxiv.org/pdf/2606.06975) · arXiv 2606.06975

#### [Continuous Audio Thinking for Large Audio Language Models](https://arxiv.org/abs/2606.18273)

- **日期：** 2026-06-05
- **问题 / 中文简述：** 多模态与基础模型 · 轻量化部署；采用音频语言模型，面向声音事件解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2606.18273) · [PDF](https://arxiv.org/pdf/2606.18273) · arXiv 2606.18273

#### [BiEAR: A Human Auditory-Inspired Adaptive Binaural Front-end for Multi-Speaker Localisation and Distance Estimation](https://arxiv.org/abs/2606.06795)

- **日期：** 2026-06-05
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展工业与机械声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2606.06795) · [PDF](https://arxiv.org/pdf/2606.06795) · arXiv 2606.06795

#### [Audio-Oscar: A Multi-Agent System for Complex Audio Scene Generation, Orchestration, and Refinement](https://arxiv.org/abs/2606.07397)

- **日期：** 2026-06-05
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2606.07397) · [PDF](https://arxiv.org/pdf/2606.07397) · arXiv 2606.07397

#### [Sound Effects Dataset Unification With the Universal Category System](https://arxiv.org/abs/2606.05571)

- **日期：** 2026-06-04
- **问题 / 中文简述：** 通用检测与分类；采用层级与多任务学习开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2606.05571) · [PDF](https://arxiv.org/pdf/2606.05571) · arXiv 2606.05571

#### [SagnacAssisted Enhanced OTDR for Distributed Acoustic Sensing: A Standardized Benchmark and Engineering Evaluation Framework](https://arxiv.org/abs/2606.05754)

- **日期：** 2026-06-04
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2606.05754) · [PDF](https://arxiv.org/pdf/2606.05754) · arXiv 2606.05754

#### [Drift-Augmented Scoring: Text-Derived Noise Robustness for Zero-Shot Audio-Language Classification](https://arxiv.org/abs/2606.04844)

- **日期：** 2026-06-03
- **问题 / 中文简述：** 低信噪比 · 开放集/OOD · 多模态与基础模型；采用音频语言模型，面向环境与城市声音解决低信噪比问题。
- **来源：** [论文主页](https://arxiv.org/abs/2606.04844) · [PDF](https://arxiv.org/pdf/2606.04844) · arXiv 2606.04844

#### [Representation Matters in Randomized Smoothing for Audio Classification](https://arxiv.org/abs/2606.04210)

- **日期：** 2026-06-02
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2606.04210) · [PDF](https://arxiv.org/pdf/2606.04210) · arXiv 2606.04210

#### [Parameter-efficient Dual-encoder Architecture with Differentiable Choquet Integral Fusion for Underwater Acoustic Classification](https://arxiv.org/abs/2606.02341)

- **日期：** 2026-06-01
- **问题 / 中文简述：** 跨域泛化 · 低信噪比 · 轻量化部署；采用Transformer 表征，面向交通与水下声音解决跨域泛化问题。
- **来源：** [论文主页](https://arxiv.org/abs/2606.02341) · [PDF](https://arxiv.org/pdf/2606.02341) · arXiv 2606.02341

#### [MOSS-Audio Technical Report](https://arxiv.org/abs/2606.01802)

- **日期：** 2026-06-01
- **问题 / 中文简述：** 多模态与基础模型；采用音频语言模型，面向环境与城市声音解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2606.01802) · [PDF](https://arxiv.org/pdf/2606.01802) · arXiv 2606.01802

#### [EntangleCodec: A Unified Discrete Audio Tokenizer via Semantic-Acoustic Entanglement](https://arxiv.org/abs/2606.02739)

- **日期：** 2026-06-01
- **问题 / 中文简述：** 多模态与基础模型；采用音频语言模型，面向环境与城市声音解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2606.02739) · [PDF](https://arxiv.org/pdf/2606.02739) · arXiv 2606.02739

#### [Diffusion-Based Heart Sound Generation: Evaluation with Physiological Signal Metrics, Classifiers, and Expert Listening](https://arxiv.org/abs/2606.02448)

- **日期：** 2026-06-01
- **问题 / 中文简述：** 轻量化部署；采用数据增强与生成，面向医疗与生理声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2606.02448) · [PDF](https://arxiv.org/pdf/2606.02448) · arXiv 2606.02448

#### [Description and Discussion on DCASE 2026 Challenge Task 2: Noise-aware Unsupervised Anomalous Sound Detection for Machine Condition Monitoring](https://arxiv.org/abs/2606.01578)

- **日期：** 2026-06-01
- **问题 / 中文简述：** 低信噪比；采用数据驱动方法，面向工业与机械声音解决低信噪比问题。
- **来源：** [论文主页](https://arxiv.org/abs/2606.01578) · [PDF](https://arxiv.org/pdf/2606.01578) · arXiv 2606.01578

#### [C2GA: A Class-Controllable Generative Augmentation Framework for Respiratory Sound Classification](https://arxiv.org/abs/2606.02212)

- **日期：** 2026-06-01
- **问题 / 中文简述：** 长尾与不平衡；采用Transformer 表征，面向医疗与生理声音解决长尾与不平衡问题。
- **来源：** [论文主页](https://arxiv.org/abs/2606.02212) · [PDF](https://arxiv.org/pdf/2606.02212) · arXiv 2606.02212

#### [SVHalluc: Benchmarking Speech-Vision Hallucination in Audio-Visual Large Language Models](https://arxiv.org/abs/2606.02642)

- **日期：** 2026-05-31
- **问题 / 中文简述：** 通用检测与分类；采用音频语言模型开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2606.02642) · [PDF](https://arxiv.org/pdf/2606.02642) · arXiv 2606.02642

#### [Mitigating Stethoscope-Induced Shortcuts in Respiratory Sound Classification under Federated Domain Generalization with Causality-Inspired Interventions](https://arxiv.org/abs/2605.29862)

- **日期：** 2026-05-28
- **问题 / 中文简述：** 跨域泛化 · 开放集/OOD · 多模态与基础模型；采用音频语言模型，面向医疗与生理声音解决跨域泛化问题。
- **来源：** [论文主页](https://arxiv.org/abs/2605.29862) · [PDF](https://arxiv.org/pdf/2605.29862) · arXiv 2605.29862

#### [ChildVox: A Speech, Audio, and Large Audio-Language Model Benchmark in Understanding and Characterizing Sound across Childhood](https://arxiv.org/abs/2605.29257)

- **日期：** 2026-05-28
- **问题 / 中文简述：** 跨域泛化 · 多模态与基础模型；采用音频语言模型，面向声音事件解决跨域泛化问题。
- **来源：** [论文主页](https://arxiv.org/abs/2605.29257) · [PDF](https://arxiv.org/pdf/2605.29257) · arXiv 2605.29257

#### [Dasheng AudioGen: A Unified Model for Generating Coherent Audio Scenes from Text](https://arxiv.org/abs/2605.27838)

- **日期：** 2026-05-27
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2605.27838) · [PDF](https://arxiv.org/pdf/2605.27838) · arXiv 2605.27838

#### [Cross-modal characterization of infant cry: validation of a chest-surface accelerometer in extracting acoustic vocal function measures](https://arxiv.org/abs/2605.28687)

- **日期：** 2026-05-27
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向医疗与生理声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2605.28687) · [PDF](https://arxiv.org/pdf/2605.28687) · arXiv 2605.28687

#### [Evaluating the Temporal Detection Capability of Integrated Gradients Applied on Sound Classifier](https://arxiv.org/abs/2605.23293)

- **日期：** 2026-05-22
- **问题 / 中文简述：** 半/弱监督 · 定位与分离；采用数据增强与生成，面向声音事件解决半/弱监督问题。
- **来源：** [论文主页](https://arxiv.org/abs/2605.23293) · [PDF](https://arxiv.org/pdf/2605.23293) · arXiv 2605.23293

#### [Automatic Contextual Audio Denoising](https://arxiv.org/abs/2605.22262)

- **日期：** 2026-05-21
- **问题 / 中文简述：** 低信噪比；采用数据驱动方法，面向交通与水下声音解决低信噪比问题。
- **来源：** [论文主页](https://arxiv.org/abs/2605.22262) · [PDF](https://arxiv.org/pdf/2605.22262) · arXiv 2605.22262

#### [CoarseSoundNet: Building a reliable model for ecological soundscape analysis](https://arxiv.org/abs/2605.21143)

- **日期：** 2026-05-20
- **问题 / 中文简述：** 低信噪比 · 可解释与可靠性；采用数据驱动方法，面向生态与动物声音解决低信噪比问题。
- **来源：** [论文主页](https://arxiv.org/abs/2605.21143) · [PDF](https://arxiv.org/pdf/2605.21143) · arXiv 2605.21143

#### [Executable Boundary Contracts for Sound Event Traces](https://arxiv.org/abs/2605.19632)

- **日期：** 2026-05-19
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2605.19632) · [PDF](https://arxiv.org/pdf/2605.19632) · arXiv 2605.19632

#### [Heterogeneity-Aware Dataset Scheduling for Efficient Audio Large Language Model Training](https://arxiv.org/abs/2605.19101)

- **日期：** 2026-05-18
- **问题 / 中文简述：** 轻量化部署；采用音频语言模型，面向环境与城市声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2605.19101) · [PDF](https://arxiv.org/pdf/2605.19101) · arXiv 2605.19101

#### [EnvTriCascade: An Environment-Aware Tri-Stage Cascaded Framework for ESDD2 2026 Challenge](https://arxiv.org/abs/2605.18409)

- **日期：** 2026-05-18
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2605.18409) · [PDF](https://arxiv.org/pdf/2605.18409) · arXiv 2605.18409

#### [Robust Audio Tagging under Class-wise Supervision Unreliability](https://arxiv.org/abs/2605.17512)

- **日期：** 2026-05-17
- **问题 / 中文简述：** 可解释与可靠性；采用数据驱动方法，面向声音事件解决可解释与可靠性问题。
- **来源：** [论文主页](https://arxiv.org/abs/2605.17512) · [PDF](https://arxiv.org/pdf/2605.17512) · arXiv 2605.17512

#### [FSD50K-Solo: Automated Curation of Single-Source Sound Events](https://arxiv.org/abs/2605.13931)

- **日期：** 2026-05-13
- **问题 / 中文简述：** 低信噪比；采用数据增强与生成，面向声音事件解决低信噪比问题。
- **来源：** [论文主页](https://arxiv.org/abs/2605.13931) · [PDF](https://arxiv.org/pdf/2605.13931) · arXiv 2605.13931

#### [Unison: Harmonizing Motion, Speech, and Sound for Human-Centric Audio-Video Generation](https://arxiv.org/abs/2605.08729)

- **日期：** 2026-05-09
- **问题 / 中文简述：** 低信噪比 · 多模态与基础模型；采用Transformer 表征，面向环境与城市声音解决低信噪比问题。
- **来源：** [论文主页](https://arxiv.org/abs/2605.08729) · [PDF](https://arxiv.org/pdf/2605.08729) · arXiv 2605.08729

#### [Towards Open World Sound Event Detection](https://arxiv.org/abs/2605.03934)

- **日期：** 2026-05-05
- **问题 / 中文简述：** 开放集/OOD；采用Transformer 表征，面向声音事件解决开放集/OOD问题。
- **来源：** [论文主页](https://arxiv.org/abs/2605.03934) · [PDF](https://arxiv.org/pdf/2605.03934) · arXiv 2605.03934

#### [Deepfake Audio Detection Using Self-supervised Fusion Representations](https://arxiv.org/abs/2605.03420)

- **日期：** 2026-05-05
- **问题 / 中文简述：** 通用检测与分类；采用自监督表征开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2605.03420) · [PDF](https://arxiv.org/pdf/2605.03420) · arXiv 2605.03420

#### [MMAudio-LABEL: Audio Event Labeling via Audio Generation for Silent Video](https://arxiv.org/abs/2605.00495)

- **日期：** 2026-05-01
- **问题 / 中文简述：** 多模态与基础模型；采用数据驱动方法，面向声音事件解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2605.00495) · [PDF](https://arxiv.org/pdf/2605.00495) · arXiv 2605.00495

#### [From Birdsong to Rumbles: Classifying Elephant Calls with Out-of-Species Embeddings](https://arxiv.org/abs/2605.00225)

- **日期：** 2026-04-30
- **问题 / 中文简述：** 跨域泛化 · 轻量化部署；采用Transformer 表征，面向生态与动物声音解决跨域泛化问题。
- **来源：** [论文主页](https://arxiv.org/abs/2605.00225) · [PDF](https://arxiv.org/pdf/2605.00225) · arXiv 2605.00225

#### [UniSonate: A Unified Model for Speech, Music, and Sound Effect Generation with Text Instructions](https://arxiv.org/abs/2604.22209)

- **日期：** 2026-04-24
- **问题 / 中文简述：** 多模态与基础模型；采用Transformer 表征，面向环境与城市声音解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2604.22209) · [PDF](https://arxiv.org/pdf/2604.22209) · arXiv 2604.22209

#### [HalluAudio: A Comprehensive Benchmark for Hallucination Detection in Large Audio-Language Models](https://arxiv.org/abs/2604.19300)

- **日期：** 2026-04-21
- **问题 / 中文简述：** 多模态与基础模型；采用音频语言模型，面向环境与城市声音解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2604.19300) · [PDF](https://arxiv.org/pdf/2604.19300) · arXiv 2604.19300

#### [Environmental Sound Deepfake Detection Using Deep-Learning Framework](https://arxiv.org/abs/2604.19652)

- **日期：** 2026-04-21
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2604.19652) · [PDF](https://arxiv.org/pdf/2604.19652) · arXiv 2604.19652

#### [Listen, Pause, and Reason: Toward Perception-Grounded Hybrid Reasoning for Audio Understanding](https://arxiv.org/abs/2604.14806)

- **日期：** 2026-04-16
- **问题 / 中文简述：** 多模态与基础模型；采用音频语言模型，面向环境与城市声音解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2604.14806) · [PDF](https://arxiv.org/pdf/2604.14806) · arXiv 2604.14806

#### [Towards Fine-grained Temporal Perception: Post-Training Large Audio-Language Models with Audio-Side Time Prompt](https://arxiv.org/abs/2604.13715)

- **日期：** 2026-04-15
- **问题 / 中文简述：** 多模态与基础模型；采用音频语言模型，面向声音事件解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2604.13715) · [PDF](https://arxiv.org/pdf/2604.13715) · arXiv 2604.13715

#### [Comparison of window shapes and lengths in short-time feature extraction for classification of heart sound signals](https://arxiv.org/abs/2604.13567)

- **日期：** 2026-04-15
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展医疗与生理声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2604.13567) · [PDF](https://arxiv.org/pdf/2604.13567) · arXiv 2604.13567

#### [SpotSound: Enhancing Large Audio-Language Models with Fine-Grained Temporal Grounding](https://arxiv.org/abs/2604.13023)

- **日期：** 2026-04-14
- **问题 / 中文简述：** 多模态与基础模型；采用音频语言模型，面向声音事件解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2604.13023) · [PDF](https://arxiv.org/pdf/2604.13023) · arXiv 2604.13023

#### [Elastic Net Regularization and Gabor Dictionary for Classification of Heart Sound Signals using Deep Learning](https://arxiv.org/abs/2604.12483)

- **日期：** 2026-04-14
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展医疗与生理声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2604.12483) · [PDF](https://arxiv.org/pdf/2604.12483) · arXiv 2604.12483

#### [Beyond Transcription: Unified Audio Schema for Perception-Aware AudioLLMs](https://arxiv.org/abs/2604.12506)

- **日期：** 2026-04-14
- **问题 / 中文简述：** 通用检测与分类；采用音频语言模型开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2604.12506) · [PDF](https://arxiv.org/pdf/2604.12506) · arXiv 2604.12506

#### [Adaptive Test-Time Scaling for Zero-Shot Respiratory Audio Classification](https://arxiv.org/abs/2604.12647)

- **日期：** 2026-04-14
- **问题 / 中文简述：** 开放集/OOD · 可解释与可靠性；采用音频语言模型，面向医疗与生理声音解决开放集/OOD问题。
- **来源：** [论文主页](https://arxiv.org/abs/2604.12647) · [PDF](https://arxiv.org/pdf/2604.12647) · arXiv 2604.12647

#### [Audio Flamingo Next: Next-Generation Open Audio-Language Models for Speech, Sound, and Music](https://arxiv.org/abs/2604.10905)

- **日期：** 2026-04-13
- **问题 / 中文简述：** 多模态与基础模型；采用音频语言模型，面向环境与城市声音解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2604.10905) · [PDF](https://arxiv.org/pdf/2604.10905) · arXiv 2604.10905

#### [Whisper-AuT: Domain-Adapted Audio Encoder for Efficient Audio-LLM Training](https://arxiv.org/abs/2604.10438)

- **日期：** 2026-04-12
- **问题 / 中文简述：** 轻量化部署；采用音频语言模型，面向环境与城市声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2604.10438) · [PDF](https://arxiv.org/pdf/2604.10438) · arXiv 2604.10438

#### [Cross-Cultural Bias in Mel-Scale Representations: Evidence and Alternatives from Speech and Music](https://arxiv.org/abs/2604.10503)

- **日期：** 2026-04-12
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2604.10503) · [PDF](https://arxiv.org/pdf/2604.10503) · arXiv 2604.10503

#### [Tora3: Trajectory-Guided Audio-Video Generation with Physical Coherence](https://arxiv.org/abs/2604.09057)

- **日期：** 2026-04-10
- **问题 / 中文简述：** 多模态与基础模型；采用数据驱动方法，面向声音事件解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2604.09057) · [PDF](https://arxiv.org/pdf/2604.09057) · arXiv 2604.09057

#### [AudioGuard: Toward Comprehensive Audio Safety Protection Across Diverse Threat Models](https://arxiv.org/abs/2604.08867)

- **日期：** 2026-04-10
- **问题 / 中文简述：** 多模态与基础模型；采用数据驱动方法，面向声音事件解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2604.08867) · [PDF](https://arxiv.org/pdf/2604.08867) · arXiv 2604.08867

#### [DeepForestSound: a multi-species automatic detector for passive acoustic monitoring in African tropical forests, a case study in Kibale National Park](https://arxiv.org/abs/2604.08087)

- **日期：** 2026-04-09
- **问题 / 中文简述：** 半/弱监督；采用Transformer 表征，面向生态与动物声音解决半/弱监督问题。
- **来源：** [论文主页](https://arxiv.org/abs/2604.08087) · [PDF](https://arxiv.org/pdf/2604.08087) · arXiv 2604.08087

#### [Generating Synthetic Doctor-Patient Conversations for Long-form Audio Summarization](https://arxiv.org/abs/2604.06138)

- **日期：** 2026-04-07
- **问题 / 中文简述：** 通用检测与分类；采用数据增强与生成开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2604.06138) · [PDF](https://arxiv.org/pdf/2604.06138) · arXiv 2604.06138

#### [OmniSonic: Towards Universal and Holistic Audio Generation from Video and Text](https://arxiv.org/abs/2604.04348)

- **日期：** 2026-04-06
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2604.04348) · [PDF](https://arxiv.org/pdf/2604.04348) · arXiv 2604.04348

#### [If It's Good Enough for You, It's Good Enough for Me: Transferability of Audio Sufficiencies across Models](https://arxiv.org/abs/2604.02937)

- **日期：** 2026-04-03
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2604.02937) · [PDF](https://arxiv.org/pdf/2604.02937) · arXiv 2604.02937

#### [Sona: Personalized Soundscape Mediation to Support People with Sound Sensitivity](https://arxiv.org/abs/2604.00447)

- **日期：** 2026-04-01
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2604.00447) · [PDF](https://arxiv.org/pdf/2604.00447) · arXiv 2604.00447

#### [FineLAP: Taming Heterogeneous Supervision for Fine-grained Language-Audio Pretraining](https://arxiv.org/abs/2604.01155)

- **日期：** 2026-04-01
- **问题 / 中文简述：** 多模态与基础模型；采用音频语言模型，面向声音事件解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2604.01155) · [PDF](https://arxiv.org/pdf/2604.01155) · arXiv 2604.01155

#### [EvA: An Evidence-First Audio Understanding Paradigm for LALMs](https://arxiv.org/abs/2603.27667)

- **日期：** 2026-03-29
- **问题 / 中文简述：** 开放集/OOD · 多模态与基础模型；采用音频语言模型，面向环境与城市声音解决开放集/OOD问题。
- **来源：** [论文主页](https://arxiv.org/abs/2603.27667) · [PDF](https://arxiv.org/pdf/2603.27667) · arXiv 2603.27667

#### [A Human-Inspired Decoupled Architecture for Efficient Audio Representation Learning](https://arxiv.org/abs/2603.26098)

- **日期：** 2026-03-27
- **问题 / 中文简述：** 多模态与基础模型 · 轻量化部署；采用自监督表征，面向声音事件解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2603.26098) · [PDF](https://arxiv.org/pdf/2603.26098) · arXiv 2603.26098

#### [Unlocking Strong Supervision: A Data-Centric Study of General-Purpose AudioPre-Training Methods](https://arxiv.org/abs/2603.25767)

- **日期：** 2026-03-26
- **问题 / 中文简述：** 少样本 · 低信噪比；采用数据驱动方法，面向环境与城市声音解决少样本问题。
- **来源：** [论文主页](https://arxiv.org/abs/2603.25767) · [PDF](https://arxiv.org/pdf/2603.25767) · arXiv 2603.25767

#### [Rethinking Masking Strategies for Masked Prediction-based Audio Self-supervised Learning](https://arxiv.org/abs/2603.23810)

- **日期：** 2026-03-25
- **问题 / 中文简述：** 轻量化部署；采用自监督表征，面向声音事件解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2603.23810) · [PDF](https://arxiv.org/pdf/2603.23810) · arXiv 2603.23810

#### [The Interspeech 2026 Audio Encoder Capability Challenge for Large Audio Language Models](https://arxiv.org/abs/2603.22728)

- **日期：** 2026-03-24
- **问题 / 中文简述：** 多模态与基础模型；采用音频语言模型，面向环境与城市声音解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2603.22728) · [PDF](https://arxiv.org/pdf/2603.22728) · arXiv 2603.22728

#### [Towards the Vision-Sound-Language-Action Paradigm: The HEAR Framework for Sound-Centric Manipulation](https://arxiv.org/abs/2603.16086)

- **日期：** 2026-03-17
- **问题 / 中文简述：** 多模态与基础模型；采用数据驱动方法，面向声音事件解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2603.16086) · [PDF](https://arxiv.org/pdf/2603.16086) · arXiv 2603.16086

#### [Patient-level validation of a foundation-model pipeline for pediatric lung sounds: physician-annotated adventitious events are recognized, disease groups are not reliably predicted](https://arxiv.org/abs/2603.15688)

- **日期：** 2026-03-15
- **问题 / 中文简述：** 可解释与可靠性；采用数据驱动方法，面向医疗与生理声音解决可解释与可靠性问题。
- **来源：** [论文主页](https://arxiv.org/abs/2603.15688) · [PDF](https://arxiv.org/pdf/2603.15688) · arXiv 2603.15688

#### [Geo-ATBench: A Benchmark for Geospatial Audio Tagging with Geospatial Semantic Context](https://arxiv.org/abs/2603.10623)

- **日期：** 2026-03-11
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向环境与城市声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2603.10623) · [PDF](https://arxiv.org/pdf/2603.10623) · arXiv 2603.10623

#### [Abjad-Kids: An Arabic Speech Classification Dataset for Primary Education](https://arxiv.org/abs/2603.20255)

- **日期：** 2026-03-11
- **问题 / 中文简述：** 少样本；采用层级与多任务学习，面向工业与机械声音解决少样本问题。
- **来源：** [论文主页](https://arxiv.org/abs/2603.20255) · [PDF](https://arxiv.org/pdf/2603.20255) · arXiv 2603.20255

#### [Physics-Informed Neural Engine Sound Modeling with Differentiable Pulse-Train Synthesis](https://arxiv.org/abs/2603.09391)

- **日期：** 2026-03-10
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2603.09391) · [PDF](https://arxiv.org/pdf/2603.09391) · arXiv 2603.09391

#### [Soundscapes in Spectrograms: Pioneering Multilabel Classification for South Asian Sounds](https://arxiv.org/abs/2603.08154)

- **日期：** 2026-03-09
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向环境与城市声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2603.08154) · [PDF](https://arxiv.org/pdf/2603.08154) · arXiv 2603.08154

#### [Towards Lightweight Adaptation of Speech Enhancement Models in Real-World Environments](https://arxiv.org/abs/2603.07471)

- **日期：** 2026-03-08
- **问题 / 中文简述：** 轻量化部署；采用自监督表征，面向环境与城市声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2603.07471) · [PDF](https://arxiv.org/pdf/2603.07471) · arXiv 2603.07471

#### [Analysis-Driven Procedural Generation of an Engine Sound Dataset with Embedded Control Annotations](https://arxiv.org/abs/2603.07584)

- **日期：** 2026-03-08
- **问题 / 中文简述：** 轻量化部署；采用数据增强与生成，面向声音事件解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2603.07584) · [PDF](https://arxiv.org/pdf/2603.07584) · arXiv 2603.07584

#### [Adaptive Discovery of Interpretable Audio Attributes with Multimodal LLMs for Low-Resource Classification](https://arxiv.org/abs/2603.06991)

- **日期：** 2026-03-07
- **问题 / 中文简述：** 少样本 · 多模态与基础模型 · 可解释与可靠性；采用音频语言模型，面向声音事件解决少样本问题。
- **来源：** [论文主页](https://arxiv.org/abs/2603.06991) · [PDF](https://arxiv.org/pdf/2603.06991) · arXiv 2603.06991

#### [The First Environmental Sound Deepfake Detection Challenge: Benchmarking Robustness, Evaluation, and Insights](https://arxiv.org/abs/2603.04865)

- **日期：** 2026-03-05
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2603.04865) · [PDF](https://arxiv.org/pdf/2603.04865) · arXiv 2603.04865

#### [PolyBench: A Benchmark for Compositional Reasoning in Polyphonic Audio](https://arxiv.org/abs/2603.05128)

- **日期：** 2026-03-05
- **问题 / 中文简述：** 多模态与基础模型；采用音频语言模型，面向声音事件解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2603.05128) · [PDF](https://arxiv.org/pdf/2603.05128) · arXiv 2603.05128

#### [A Sensitivity Analysis of Multi-Event Audio Grounding in Audio LLMs](https://arxiv.org/abs/2603.03855)

- **日期：** 2026-03-04
- **问题 / 中文简述：** 可解释与可靠性；采用数据驱动方法，面向环境与城市声音解决可解释与可靠性问题。
- **来源：** [论文主页](https://arxiv.org/abs/2603.03855) · [PDF](https://arxiv.org/pdf/2603.03855) · arXiv 2603.03855

#### [Fine-grained Soundscape Control for Augmented Hearing](https://arxiv.org/abs/2603.00395)

- **日期：** 2026-02-28
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2603.00395) · [PDF](https://arxiv.org/pdf/2603.00395) · arXiv 2603.00395

#### [StethoLM Audio Language Model for Cardiopulmonary Analysis Across Clinical Tasks](https://arxiv.org/abs/2603.00355)

- **日期：** 2026-02-27
- **问题 / 中文简述：** 开放集/OOD · 多模态与基础模型；采用音频语言模型，面向医疗与生理声音解决开放集/OOD问题。
- **来源：** [论文主页](https://arxiv.org/abs/2603.00355) · [PDF](https://arxiv.org/pdf/2603.00355) · arXiv 2603.00355

#### [DashengTokenizer- One layer is enough for unified audio understanding and generation](https://arxiv.org/abs/2602.23765)

- **日期：** 2026-02-27
- **问题 / 中文简述：** 轻量化部署；采用数据增强与生成，面向环境与城市声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2602.23765) · [PDF](https://arxiv.org/pdf/2602.23765) · arXiv 2602.23765

#### [AudioCapBench: Quick Evaluation on Audio Captioning across Sound, Music, and Speech](https://arxiv.org/abs/2602.23649)

- **日期：** 2026-02-27
- **问题 / 中文简述：** 多模态与基础模型；采用数据驱动方法，面向环境与城市声音解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2602.23649) · [PDF](https://arxiv.org/pdf/2602.23649) · arXiv 2602.23649

#### [UniWhisper- Efficient Continual Multi-task Training for Robust Universal Audio Representation](https://arxiv.org/abs/2602.21772)

- **日期：** 2026-02-25
- **问题 / 中文简述：** 轻量化部署；采用层级与多任务学习，面向环境与城市声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2602.21772) · [PDF](https://arxiv.org/pdf/2602.21772) · arXiv 2602.21772

#### [LMU-Based Sequential Learning and Posterior Ensemble Fusion for Cross-Domain Infant Cry Classification](https://arxiv.org/abs/2603.02245)

- **日期：** 2026-02-24
- **问题 / 中文简述：** 跨域泛化 · 轻量化部署；采用数据驱动方法，面向声音事件解决跨域泛化问题。
- **来源：** [论文主页](https://arxiv.org/abs/2603.02245) · [PDF](https://arxiv.org/pdf/2603.02245) · arXiv 2603.02245

#### [Lend me an Ear: Speech Enhancement Using a Robotic Arm with a Microphone Array](https://arxiv.org/abs/2602.17818)

- **日期：** 2026-02-19
- **问题 / 中文简述：** 低信噪比 · 定位与分离 · 多模态与基础模型；采用数据驱动方法，面向工业与机械声音解决低信噪比问题。
- **来源：** [论文主页](https://arxiv.org/abs/2602.17818) · [PDF](https://arxiv.org/pdf/2602.17818) · arXiv 2602.17818

#### [Detection and Classification of Cetacean Echolocation Clicks using Image-based Object Detection Methods applied to Advanced Wavelet-based Transformations](https://arxiv.org/abs/2602.17749)

- **日期：** 2026-02-19
- **问题 / 中文简述：** 可解释与可靠性；采用数据驱动方法，面向生态与动物声音解决可解释与可靠性问题。
- **来源：** [论文主页](https://arxiv.org/abs/2602.17749) · [PDF](https://arxiv.org/pdf/2602.17749) · arXiv 2602.17749

#### [AudioChat: Unified Audio Storytelling, Editing, and Understanding with Transfusion Forcing](https://arxiv.org/abs/2602.17097)

- **日期：** 2026-02-19
- **问题 / 中文简述：** 多模态与基础模型；采用数据驱动方法，面向环境与城市声音解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2602.17097) · [PDF](https://arxiv.org/pdf/2602.17097) · arXiv 2602.17097

#### [Spatial Audio Question Answering and Reasoning on Dynamic Source Movements](https://arxiv.org/abs/2602.16334)

- **日期：** 2026-02-18
- **问题 / 中文简述：** 定位与分离 · 多模态与基础模型；采用音频语言模型，面向工业与机械声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2602.16334) · [PDF](https://arxiv.org/pdf/2602.16334) · arXiv 2602.16334

#### [Real time fault detection in 3D printers using Convolutional Neural Networks and acoustic signals](https://arxiv.org/abs/2602.16118)

- **日期：** 2026-02-18
- **问题 / 中文简述：** 可解释与可靠性；采用数据驱动方法，面向工业与机械声音解决可解释与可靠性问题。
- **来源：** [论文主页](https://arxiv.org/abs/2602.16118) · [PDF](https://arxiv.org/pdf/2602.16118) · arXiv 2602.16118

#### [Hardware-accelerated graph neural networks an alternative approach for neuromorphic event-based audio classification and keyword spotting on SoC FPGA](https://arxiv.org/abs/2602.16442)

- **日期：** 2026-02-18
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向声音事件解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2602.16442) · [PDF](https://arxiv.org/pdf/2602.16442) · arXiv 2602.16442

#### [TAC: Timestamped Audio Captioning](https://arxiv.org/abs/2602.15766)

- **日期：** 2026-02-17
- **问题 / 中文简述：** 多模态与基础模型；采用音频语言模型，面向环境与城市声音解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2602.15766) · [PDF](https://arxiv.org/pdf/2602.15766) · arXiv 2602.15766

#### [MAEB- Massive Audio Embedding Benchmark](https://arxiv.org/abs/2602.16008)

- **日期：** 2026-02-17
- **问题 / 中文简述：** 通用检测与分类；采用音频语言模型开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2602.16008) · [PDF](https://arxiv.org/pdf/2602.16008) · arXiv 2602.16008

#### [Resp-Agent An Agent-Based System for Multimodal Respiratory Sound Generation and Disease Diagnosis](https://arxiv.org/abs/2602.15909)

- **日期：** 2026-02-16
- **问题 / 中文简述：** 长尾与不平衡 · 多模态与基础模型；采用音频语言模型，面向医疗与生理声音解决长尾与不平衡问题。
- **来源：** [论文主页](https://arxiv.org/abs/2602.15909) · [PDF](https://arxiv.org/pdf/2602.15909) · arXiv 2602.15909

#### [A two-step approach for speech enhancement in low-SNR scenarios using cyclostationary beamforming and DNNs](https://arxiv.org/abs/2602.12986)

- **日期：** 2026-02-13
- **问题 / 中文简述：** 低信噪比 · 轻量化部署；采用数据增强与生成，面向工业与机械声音解决低信噪比问题。
- **来源：** [论文主页](https://arxiv.org/abs/2602.12986) · [PDF](https://arxiv.org/pdf/2602.12986) · arXiv 2602.12986

#### [From Diet to Free Lunch: Estimating Auxiliary Signal Properties using Dynamic Pruning Masks in Speech Enhancement Networks](https://arxiv.org/abs/2602.10666)

- **日期：** 2026-02-11
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向环境与城市声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2602.10666) · [PDF](https://arxiv.org/pdf/2602.10666) · arXiv 2602.10666

#### [Positive-Unlabelled Active Learning to Curate a Dataset for Orca Resident Interpretation](https://arxiv.org/abs/2602.09295)

- **日期：** 2026-02-10
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展生态与动物声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2602.09295) · [PDF](https://arxiv.org/pdf/2602.09295) · arXiv 2602.09295

#### [Evaluating CNN with Stacked Feature Representations and Audio Spectrogram Transformer Models for Sound Classification](https://arxiv.org/abs/2602.09321)

- **日期：** 2026-02-10
- **问题 / 中文简述：** 轻量化部署；采用Transformer 表征，面向工业与机械声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2602.09321) · [PDF](https://arxiv.org/pdf/2602.09321) · arXiv 2602.09321

#### [BioME: A Resource-Efficient Bioacoustic Foundational Model for IoT Applications](https://arxiv.org/abs/2602.09970)

- **日期：** 2026-02-10
- **问题 / 中文简述：** 轻量化部署；采用自监督表征，面向生态与动物声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2602.09970) · [PDF](https://arxiv.org/pdf/2602.09970) · arXiv 2602.09970

#### [AI-Driven Cardiorespiratory Signal Processing Separation, Clustering, and Anomaly Detection](https://arxiv.org/abs/2602.09210)

- **日期：** 2026-02-09
- **问题 / 中文简述：** 定位与分离 · 可解释与可靠性；采用音频语言模型，面向医疗与生理声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2602.09210) · [PDF](https://arxiv.org/pdf/2602.09210) · arXiv 2602.09210

#### [Misophonia Trigger Sound Detection on Synthetic Soundscapes Using a Hybrid Model with a Frozen Pre-Trained CNN and a Time-Series Module](https://arxiv.org/abs/2602.06271)

- **日期：** 2026-02-06
- **问题 / 中文简述：** 少样本；采用数据增强与生成，面向环境与城市声音解决少样本问题。
- **来源：** [论文主页](https://arxiv.org/abs/2602.06271) · [PDF](https://arxiv.org/pdf/2602.06271) · arXiv 2602.06271

#### [CALM Class-Conditional Sparse Attention Vectors for Large Audio-Language Models](https://arxiv.org/abs/2602.07077)

- **日期：** 2026-02-06
- **问题 / 中文简述：** 少样本 · 开放集/OOD · 多模态与基础模型 · 可解释与可靠性；采用音频语言模型，面向声音事件解决少样本问题。
- **来源：** [论文主页](https://arxiv.org/abs/2602.07077) · [PDF](https://arxiv.org/pdf/2602.07077) · arXiv 2602.07077

#### [Bagpiper Solving Open-Ended Audio Tasks via Rich Captions](https://arxiv.org/abs/2602.05220)

- **日期：** 2026-02-05
- **问题 / 中文简述：** 多模态与基础模型 · 轻量化部署；采用数据驱动方法，面向声音事件解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2602.05220) · [PDF](https://arxiv.org/pdf/2602.05220) · arXiv 2602.05220

#### [Audio ControlNet for Fine-Grained Audio Generation and Editing](https://arxiv.org/abs/2602.04680)

- **日期：** 2026-02-04
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向声音事件解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2602.04680) · [PDF](https://arxiv.org/pdf/2602.04680) · arXiv 2602.04680

#### [Synthetic Data Augmentation for Medical Audio Classification A Preliminary Evaluation](https://arxiv.org/abs/2602.02955)

- **日期：** 2026-02-03
- **问题 / 中文简述：** 长尾与不平衡；采用数据增强与生成，面向医疗与生理声音解决长尾与不平衡问题。
- **来源：** [论文主页](https://arxiv.org/abs/2602.02955) · [PDF](https://arxiv.org/pdf/2602.02955) · arXiv 2602.02955

#### [Sounding Highlights: Dual-Pathway Audio Encoders for Audio-Visual Video Highlight Detection](https://arxiv.org/abs/2602.03891)

- **日期：** 2026-02-03
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2602.03891) · [PDF](https://arxiv.org/pdf/2602.03891) · arXiv 2602.03891

#### [PACE Pretrained Audio Continual Learning](https://arxiv.org/abs/2602.03355)

- **日期：** 2026-02-03
- **问题 / 中文简述：** 持续学习 · 轻量化部署；采用数据驱动方法，面向环境与城市声音解决持续学习问题。
- **来源：** [论文主页](https://arxiv.org/abs/2602.03355) · [PDF](https://arxiv.org/pdf/2602.03355) · arXiv 2602.03355

#### [Instantaneous Spectra Analysis of Pulse Series - Application to Lung Sounds with Abnormalities](https://arxiv.org/abs/2602.03680)

- **日期：** 2026-02-03
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展医疗与生理声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2602.03680) · [PDF](https://arxiv.org/pdf/2602.03680) · arXiv 2602.03680

#### [SSNAPS: Audio-Visual Separation of Speech and Background Noise with Diffusion Inverse Sampling](https://arxiv.org/abs/2602.01394)

- **日期：** 2026-02-01
- **问题 / 中文简述：** 定位与分离；采用数据增强与生成，面向环境与城市声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2602.01394) · [PDF](https://arxiv.org/pdf/2602.01394) · arXiv 2602.01394

#### [Hearing is Believing Evaluating and Analyzing Audio Language Model Sycophancy with SYAUDIO](https://arxiv.org/abs/2601.23149)

- **日期：** 2026-01-30
- **问题 / 中文简述：** 多模态与基础模型；采用音频语言模型，面向声音事件解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2601.23149) · [PDF](https://arxiv.org/pdf/2601.23149) · arXiv 2601.23149

#### [A Semantically Consistent Dataset for Data-Efficient Query-Based Universal Sound Separation](https://arxiv.org/abs/2601.22599)

- **日期：** 2026-01-30
- **问题 / 中文简述：** 开放集/OOD · 定位与分离 · 多模态与基础模型 · 轻量化部署；采用数据增强与生成，面向环境与城市声音解决开放集/OOD问题。
- **来源：** [论文主页](https://arxiv.org/abs/2601.22599) · [PDF](https://arxiv.org/pdf/2601.22599) · arXiv 2601.22599

#### [SemanticAudio: Audio Generation and Editing in Semantic Space](https://arxiv.org/abs/2601.21402)

- **日期：** 2026-01-29
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2601.21402) · [PDF](https://arxiv.org/pdf/2601.21402) · arXiv 2601.21402

#### [DNN-Based Online Source Counting Based on Spatial Generalized Magnitude Squared Coherence](https://arxiv.org/abs/2601.21114)

- **日期：** 2026-01-28
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向环境与城市声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2601.21114) · [PDF](https://arxiv.org/pdf/2601.21114) · arXiv 2601.21114

#### [VoxMorph: Scalable Zero-shot Voice Identity Morphing via Disentangled Embeddings](https://arxiv.org/abs/2601.20883)

- **日期：** 2026-01-27
- **问题 / 中文简述：** 开放集/OOD；采用音频语言模型，面向环境与城市声音解决开放集/OOD问题。
- **来源：** [论文主页](https://arxiv.org/abs/2601.20883) · [PDF](https://arxiv.org/pdf/2601.20883) · arXiv 2601.20883

#### [Noise-Robust Contrastive Learning with an MFCC-Conformer For Coronary Artery Disease Detection](https://arxiv.org/abs/2601.18295)

- **日期：** 2026-01-26
- **问题 / 中文简述：** 低信噪比 · 轻量化部署；采用Transformer 表征，面向医疗与生理声音解决低信噪比问题。
- **来源：** [论文主页](https://arxiv.org/abs/2601.18295) · [PDF](https://arxiv.org/pdf/2601.18295) · arXiv 2601.18295

#### [Analytic Incremental Learning For Sound Source Localization With Imbalance Rectification](https://arxiv.org/abs/2601.18335)

- **日期：** 2026-01-26
- **问题 / 中文简述：** 长尾与不平衡 · 持续学习 · 定位与分离；采用数据增强与生成，面向声音事件解决长尾与不平衡问题。
- **来源：** [论文主页](https://arxiv.org/abs/2601.18335) · [PDF](https://arxiv.org/pdf/2601.18335) · arXiv 2601.18335

#### [ToS A Team of Specialists ensemble framework for Stereo Sound Event Localization and Detection with](https://arxiv.org/abs/2601.17611)

- **日期：** 2026-01-24
- **问题 / 中文简述：** 定位与分离 · 多模态与基础模型；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2601.17611) · [PDF](https://arxiv.org/pdf/2601.17611) · arXiv 2601.17611

#### [PC-MCL PATIENT-CONSISTENT MULTI-CYCLE LEARNING WITH MULTI-LABEL BIAS CORRECTION FOR RESPIRATORY SOUND CLASSIFICATION](https://arxiv.org/abs/2601.17080)

- **日期：** 2026-01-23
- **问题 / 中文简述：** 通用检测与分类；采用层级与多任务学习开展医疗与生理声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2601.17080) · [PDF](https://arxiv.org/pdf/2601.17080) · arXiv 2601.17080

#### [Bangla Music Genre Classification Using Bidirectional LSTMS](https://arxiv.org/abs/2601.15083)

- **日期：** 2026-01-21
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向工业与机械声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2601.15083) · [PDF](https://arxiv.org/pdf/2601.15083) · arXiv 2601.15083

#### [Ultra-Lightweight Network for Ship-Radiated Sound Classification on Embedded Deployment](https://arxiv.org/abs/2601.13679)

- **日期：** 2026-01-20
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向交通与水下声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2601.13679) · [PDF](https://arxiv.org/pdf/2601.13679) · arXiv 2601.13679

#### [Transformer Architectures for Respiratory Sound Analysis and Multimodal Diagnosis](https://arxiv.org/abs/2601.14227)

- **日期：** 2026-01-20
- **问题 / 中文简述：** 多模态与基础模型；采用音频语言模型，面向医疗与生理声音解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2601.14227) · [PDF](https://arxiv.org/pdf/2601.14227) · arXiv 2601.14227

#### [Event Classification by Physics-informed Inpainting for Distributed Multichannel Acoustic Sensor wit](https://arxiv.org/abs/2601.13513)

- **日期：** 2026-01-20
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2601.13513) · [PDF](https://arxiv.org/pdf/2601.13513) · arXiv 2601.13513

#### [SoundPlot: An Open-Source Framework for Birdsong Acoustic Analysis and Neural Synthesis with Interactive 3D Visualization](https://arxiv.org/abs/2601.12752)

- **日期：** 2026-01-19
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向生态与动物声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2601.12752) · [PDF](https://arxiv.org/pdf/2601.12752) · arXiv 2601.12752

#### [Sound2Hap: Learning Audio-to-Vibrotactile Haptic Generation from Human Ratings](https://arxiv.org/abs/2601.12245)

- **日期：** 2026-01-18
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2601.12245) · [PDF](https://arxiv.org/pdf/2601.12245) · arXiv 2601.12245

#### [SLAP Scalable Language-Audio Pretraining with Variable-Duration Audio and Multi-Objective Training](https://arxiv.org/abs/2601.12594)

- **日期：** 2026-01-18
- **问题 / 中文简述：** 开放集/OOD · 多模态与基础模型；采用音频语言模型，面向声音事件解决开放集/OOD问题。
- **来源：** [论文主页](https://arxiv.org/abs/2601.12594) · [PDF](https://arxiv.org/pdf/2601.12594) · arXiv 2601.12594

#### [Guided by the Plan: Enhancing Faithful Autoregressive Text-to-Audio Generation with Guided Decoding](https://arxiv.org/abs/2601.14304)

- **日期：** 2026-01-18
- **问题 / 中文简述：** 多模态与基础模型 · 轻量化部署；采用音频语言模型，面向声音事件解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2601.14304) · [PDF](https://arxiv.org/pdf/2601.14304) · arXiv 2601.14304

#### [Do Neural Codecs Generalize? A Controlled Study Across Unseen Languages and Non-Speech Tasks](https://arxiv.org/abs/2601.12205)

- **日期：** 2026-01-18
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2601.12205) · [PDF](https://arxiv.org/pdf/2601.12205) · arXiv 2601.12205

#### [RSA-Bench: Benchmarking Audio Large Models in Real-World Acoustic Scenarios](https://arxiv.org/abs/2601.10384)

- **日期：** 2026-01-15
- **问题 / 中文简述：** 低信噪比；采用Transformer 表征，面向工业与机械声音解决低信噪比问题。
- **来源：** [论文主页](https://arxiv.org/abs/2601.10384) · [PDF](https://arxiv.org/pdf/2601.10384) · arXiv 2601.10384

#### [BickGraphing: Web-Based Application for Visual Inspection of Audio Recordings](https://arxiv.org/abs/2601.17014)

- **日期：** 2026-01-14
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2601.17014) · [PDF](https://arxiv.org/pdf/2601.17014) · arXiv 2601.17014

#### [Linear probing enables Ship-Radiated Noise recognition with pretrained audio embeddings](https://arxiv.org/abs/2601.08358)

- **日期：** 2026-01-13
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展工业与机械声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2601.08358) · [PDF](https://arxiv.org/pdf/2601.08358) · arXiv 2601.08358

#### [ESDD2 Environment-Aware Speech and Sound Deepfake Detection Challenge Evaluation Plan](https://arxiv.org/abs/2601.07303)

- **日期：** 2026-01-12
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向环境与城市声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2601.07303) · [PDF](https://arxiv.org/pdf/2601.07303) · arXiv 2601.07303

#### [MoEScore: Mixture-of-Experts-Based Text-Audio Relevance Score Prediction for Text-to-Audio System Evaluation](https://arxiv.org/abs/2601.06829)

- **日期：** 2026-01-11
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2601.06829) · [PDF](https://arxiv.org/pdf/2601.06829) · arXiv 2601.06829

#### [Leveraging Prediction Entropy for Automatic Prompt Weighting in Zero-Shot Audio-Language Classification](https://arxiv.org/abs/2601.05011)

- **日期：** 2026-01-08
- **问题 / 中文简述：** 开放集/OOD · 多模态与基础模型 · 可解释与可靠性；采用音频语言模型，面向环境与城市声音解决开放集/OOD问题。
- **来源：** [论文主页](https://arxiv.org/abs/2601.05011) · [PDF](https://arxiv.org/pdf/2601.05011) · arXiv 2601.05011

#### [Sound Event Detection with Boundary-Aware Optimization and Inference](https://arxiv.org/abs/2601.04178)

- **日期：** 2026-01-07
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2601.04178) · [PDF](https://arxiv.org/pdf/2601.04178) · arXiv 2601.04178

#### [Investigation into respiratory sound classification for an imbalanced data set using hybrid LSTM-KAN architectures](https://arxiv.org/abs/2601.03610)

- **日期：** 2026-01-07
- **问题 / 中文简述：** 长尾与不平衡；采用数据增强与生成，面向医疗与生理声音解决长尾与不平衡问题。
- **来源：** [论文主页](https://arxiv.org/abs/2601.03610) · [PDF](https://arxiv.org/pdf/2601.03610) · arXiv 2601.03610

#### [The World is Not Mono Enabling Spatial Understanding in Large Audio-Language Models](https://arxiv.org/abs/2601.02954)

- **日期：** 2026-01-06
- **问题 / 中文简述：** 定位与分离 · 多模态与基础模型；采用音频语言模型，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2601.02954) · [PDF](https://arxiv.org/pdf/2601.02954) · arXiv 2601.02954

#### [Interpretable All-Type Audio Deepfake Detection with Audio LLMs via Frequency-Time Reinforcement Learning](https://arxiv.org/abs/2601.02983)

- **日期：** 2026-01-06
- **问题 / 中文简述：** 通用检测与分类；采用音频语言模型开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2601.02983) · [PDF](https://arxiv.org/pdf/2601.02983) · arXiv 2601.02983

</details>

<details>
<summary><strong>2025 年（345 篇）</strong></summary>

#### [Environmental Sound Deepfake Detection Challenge: An Overview](https://arxiv.org/abs/2512.24140)

- **日期：** 2025-12-30
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2512.24140) · [PDF](https://arxiv.org/pdf/2512.24140) · arXiv 2512.24140

#### [Geometry-Aware Optimization for Respiratory Sound Classification: Enhancing Sensitivity with SAM-Optimized Audio Spectrogram Transformers](https://arxiv.org/abs/2512.22564)

- **日期：** 2025-12-27
- **问题 / 中文简述：** 长尾与不平衡；采用Transformer 表征，面向医疗与生理声音解决长尾与不平衡问题。
- **来源：** [论文主页](https://arxiv.org/abs/2512.22564) · [PDF](https://arxiv.org/pdf/2512.22564) · arXiv 2512.22564

#### [QuarkAudio Technical Report](https://arxiv.org/abs/2512.20151)

- **日期：** 2025-12-23
- **问题 / 中文简述：** 定位与分离；采用自监督表征，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2512.20151) · [PDF](https://arxiv.org/pdf/2512.20151) · arXiv 2512.20151

#### [MMEDIT A Unified Framework for Multi-Type Audio Editing via Audio Language Model](https://arxiv.org/abs/2512.20339)

- **日期：** 2025-12-23
- **问题 / 中文简述：** 定位与分离 · 多模态与基础模型；采用音频语言模型，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2512.20339) · [PDF](https://arxiv.org/pdf/2512.20339) · arXiv 2512.20339

#### [EnvSSLAM-FFN: Lightweight Layer-Fused System for ESDD 2026 Challenge](https://arxiv.org/abs/2512.20369)

- **日期：** 2025-12-23
- **问题 / 中文简述：** 少样本 · 轻量化部署；采用自监督表征，面向环境与城市声音解决少样本问题。
- **来源：** [论文主页](https://arxiv.org/abs/2512.20369) · [PDF](https://arxiv.org/pdf/2512.20369) · arXiv 2512.20369

#### [AUDRON: A Deep Learning Framework with Fused Acoustic Signatures for Drone Type Recognition](https://arxiv.org/abs/2512.20407)

- **日期：** 2025-12-23
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向交通与水下声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2512.20407) · [PDF](https://arxiv.org/pdf/2512.20407) · arXiv 2512.20407

#### [Pushing the Frontier of Audiovisual Perception with Large-Scale Multimodal Correspondence Learning](https://arxiv.org/abs/2512.19687)

- **日期：** 2025-12-22
- **问题 / 中文简述：** 开放集/OOD · 多模态与基础模型；采用对比与原型学习，面向声音事件解决开放集/OOD问题。
- **来源：** [论文主页](https://arxiv.org/abs/2512.19687) · [PDF](https://arxiv.org/pdf/2512.19687) · arXiv 2512.19687

#### [X-Talk: On the Underestimated Potential of Modular Speech-to-Speech Dialogue System](https://arxiv.org/abs/2512.18706)

- **日期：** 2025-12-21
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2512.18706) · [PDF](https://arxiv.org/pdf/2512.18706) · arXiv 2512.18706

#### [Domain-Agnostic Causal-Aware Audio Transformer for Infant Cry Classification](https://arxiv.org/abs/2512.16271)

- **日期：** 2025-12-18
- **问题 / 中文简述：** 跨域泛化；采用Transformer 表征，面向医疗与生理声音解决跨域泛化问题。
- **来源：** [论文主页](https://arxiv.org/abs/2512.16271) · [PDF](https://arxiv.org/pdf/2512.16271) · arXiv 2512.16271

#### [BEAT2AASIST model with layer fusion for ESDD 2026 Challenge](https://arxiv.org/abs/2512.15180)

- **日期：** 2025-12-17
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2512.15180) · [PDF](https://arxiv.org/pdf/2512.15180) · arXiv 2512.15180

#### [A robust framework for sound event localization and detection on real recordings](https://arxiv.org/abs/2512.22156)

- **日期：** 2025-12-16
- **问题 / 中文简述：** 定位与分离；采用数据增强与生成，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2512.22156) · [PDF](https://arxiv.org/pdf/2512.22156) · arXiv 2512.22156

#### [Privacy-Enhancing Infant Cry Classification with Federated Transformers and Denoising Regularization](https://arxiv.org/abs/2512.13880)

- **日期：** 2025-12-15
- **问题 / 中文简述：** 跨域泛化 · 低信噪比 · 开放集/OOD · 可解释与可靠性；采用Transformer 表征，面向声音事件解决跨域泛化问题。
- **来源：** [论文主页](https://arxiv.org/abs/2512.13880) · [PDF](https://arxiv.org/pdf/2512.13880) · arXiv 2512.13880

#### [Ensemble-Guided Distillation for Compact and Robust Acoustic Scene Classification on Edge Devices](https://arxiv.org/abs/2512.13905)

- **日期：** 2025-12-15
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向环境与城市声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2512.13905) · [PDF](https://arxiv.org/pdf/2512.13905) · arXiv 2512.13905

#### [Neural personal sound zones with flexible bright zone control](https://arxiv.org/abs/2512.10375)

- **日期：** 2025-12-11
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2512.10375) · [PDF](https://arxiv.org/pdf/2512.10375) · arXiv 2512.10375

#### [Mitigation of multi-path propagation artefacts in acoustic targets with adaptive cepstral filtering](https://arxiv.org/abs/2512.11165)

- **日期：** 2025-12-11
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向交通与水下声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2512.11165) · [PDF](https://arxiv.org/pdf/2512.11165) · arXiv 2512.11165

#### [VocSim A Training-free Benchmark for Zero-shot Content Identity in Single-source Audio](https://arxiv.org/abs/2512.10120)

- **日期：** 2025-12-10
- **问题 / 中文简述：** 少样本 · 跨域泛化 · 开放集/OOD · 定位与分离；采用数据驱动方法，面向生态与动物声音解决少样本问题。
- **来源：** [论文主页](https://arxiv.org/abs/2512.10120) · [PDF](https://arxiv.org/pdf/2512.10120) · arXiv 2512.10120

#### [VABench A Comprehensive Benchmark for Audio-Video Generation](https://arxiv.org/abs/2512.09299)

- **日期：** 2025-12-10
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2512.09299) · [PDF](https://arxiv.org/pdf/2512.09299) · arXiv 2512.09299

#### [Continual Learning for Acoustic Event Classification](https://arxiv.org/abs/2512.17932)

- **日期：** 2025-12-10
- **问题 / 中文简述：** 持续学习 · 可解释与可靠性 · 轻量化部署；采用数据增强与生成，面向环境与城市声音解决持续学习问题。
- **来源：** [论文主页](https://arxiv.org/abs/2512.17932) · [PDF](https://arxiv.org/pdf/2512.17932) · arXiv 2512.17932

#### [Improving Underwater Acoustic Classification Through Learnable Gabor Filter Convolution and Attention Mechanisms](https://arxiv.org/abs/2512.14714)

- **日期：** 2025-12-09
- **问题 / 中文简述：** 定位与分离；采用Transformer 表征，面向工业与机械声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2512.14714) · [PDF](https://arxiv.org/pdf/2512.14714) · arXiv 2512.14714

#### [Unsupervised Single-Channel Audio Separation with Diffusion Source Priors](https://arxiv.org/abs/2512.07226)

- **日期：** 2025-12-08
- **问题 / 中文简述：** 低信噪比 · 定位与分离；采用Transformer 表征，面向声音事件解决低信噪比问题。
- **来源：** [论文主页](https://arxiv.org/abs/2512.07226) · [PDF](https://arxiv.org/pdf/2512.07226) · arXiv 2512.07226

#### [Technical Report of Nomi Team in the Environmental Sound Deepfake Detection Challenge 2026](https://arxiv.org/abs/2512.06041)

- **日期：** 2025-12-05
- **问题 / 中文简述：** 少样本；采用Transformer 表征，面向环境与城市声音解决少样本问题。
- **来源：** [论文主页](https://arxiv.org/abs/2512.06041) · [PDF](https://arxiv.org/pdf/2512.06041) · arXiv 2512.06041

#### [Language Models as Semantic Teachers Post-Training Alignment for Medical Audio Understanding](https://arxiv.org/abs/2512.04847)

- **日期：** 2025-12-04
- **问题 / 中文简述：** 多模态与基础模型 · 轻量化部署；采用音频语言模型，面向医疗与生理声音解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2512.04847) · [PDF](https://arxiv.org/pdf/2512.04847) · arXiv 2512.04847

#### [State Space Models for Bioacoustics A comparative Evaluation with Transformers](https://arxiv.org/abs/2512.03563)

- **日期：** 2025-12-03
- **问题 / 中文简述：** 多模态与基础模型 · 轻量化部署；采用自监督表征，面向生态与动物声音解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2512.03563) · [PDF](https://arxiv.org/pdf/2512.03563) · arXiv 2512.03563

#### [WhAM: Towards A Translative Model of Sperm Whale Vocalization](https://arxiv.org/abs/2512.02206)

- **日期：** 2025-12-01
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展生态与动物声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2512.02206) · [PDF](https://arxiv.org/pdf/2512.02206) · arXiv 2512.02206

#### [Parallel Delayed Memory Units for Enhanced Temporal Modeling in Biomedical and Bioacoustic Signal An](https://arxiv.org/abs/2512.01626)

- **日期：** 2025-12-01
- **问题 / 中文简述：** 轻量化部署；采用Transformer 表征，面向生态与动物声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2512.01626) · [PDF](https://arxiv.org/pdf/2512.01626) · arXiv 2512.01626

#### [Advancing Marine Bioacoustics with Deep Generative Models A Hybrid Augmentation Strategy for Southe](https://arxiv.org/abs/2511.21872)

- **日期：** 2025-11-26
- **问题 / 中文简述：** 低信噪比；采用数据增强与生成，面向生态与动物声音解决低信噪比问题。
- **来源：** [论文主页](https://arxiv.org/abs/2511.21872) · [PDF](https://arxiv.org/pdf/2511.21872) · arXiv 2511.21872

#### [AudioScene: Integrating Object-Event Audio into 3D Scenes](https://arxiv.org/abs/2512.07845)

- **日期：** 2025-11-25
- **问题 / 中文简述：** 通用检测与分类；采用音频语言模型开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2512.07845) · [PDF](https://arxiv.org/pdf/2512.07845) · arXiv 2512.07845

#### [Real-Time Object Tracking with On-Device Deep Learning for Adaptive Beamforming in Dynamic Acoustic Environments](https://arxiv.org/abs/2511.19396)

- **日期：** 2025-11-24
- **问题 / 中文简述：** 定位与分离 · 轻量化部署；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2511.19396) · [PDF](https://arxiv.org/pdf/2511.19396) · arXiv 2511.19396

#### [Frequency-Invariant Beamforming in Elevation and Azimuth via Autograd and Concentric Circular Microphone Arrays](https://arxiv.org/abs/2511.19403)

- **日期：** 2025-11-24
- **问题 / 中文简述：** 定位与分离；采用Transformer 表征，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2511.19403) · [PDF](https://arxiv.org/pdf/2511.19403) · arXiv 2511.19403

#### [Dynamic Multi-Species Bird Soundscape Generation with Acoustic Patterning and 3D Spatialization](https://arxiv.org/abs/2511.19275)

- **日期：** 2025-11-24
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2511.19275) · [PDF](https://arxiv.org/pdf/2511.19275) · arXiv 2511.19275

#### [DHAuDS- A Dynamic and Heterogeneous Audio Benchmark for Test-Time Adaptation](https://arxiv.org/abs/2511.18421)

- **日期：** 2025-11-23
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2511.18421) · [PDF](https://arxiv.org/pdf/2511.18421) · arXiv 2511.18421

#### [SceneGuard: Training-Time Voice Protection with Scene-Consistent Audible Background Noise](https://arxiv.org/abs/2511.16114)

- **日期：** 2025-11-20
- **问题 / 中文简述：** 低信噪比 · 轻量化部署；采用数据驱动方法，面向环境与城市声音解决低信噪比问题。
- **来源：** [论文主页](https://arxiv.org/abs/2511.16114) · [PDF](https://arxiv.org/pdf/2511.16114) · arXiv 2511.16114

#### [Better audio representations are more brain-like: linking model-brain alignment with performance in downstream auditory tasks](https://arxiv.org/abs/2511.16849)

- **日期：** 2025-11-20
- **问题 / 中文简述：** 通用检测与分类；采用自监督表征开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2511.16849) · [PDF](https://arxiv.org/pdf/2511.16849) · arXiv 2511.16849

#### [Step-Audio-R1 Technical Report](https://arxiv.org/abs/2511.15848)

- **日期：** 2025-11-19
- **问题 / 中文简述：** 多模态与基础模型 · 轻量化部署；采用音频语言模型，面向环境与城市声音解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2511.15848) · [PDF](https://arxiv.org/pdf/2511.15848) · arXiv 2511.15848

#### [Audio Question Answering with GRPO-Based Fine-Tuning and Calibrated Segment-Level Predictions](https://arxiv.org/abs/2511.14307)

- **日期：** 2025-11-18
- **问题 / 中文简述：** 通用检测与分类；采用音频语言模型开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2511.14307) · [PDF](https://arxiv.org/pdf/2511.14307) · arXiv 2511.14307

#### [Systematic Evaluation of Time-Frequency Features for Binaural Sound Source Localization](https://arxiv.org/abs/2511.13487)

- **日期：** 2025-11-17
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2511.13487) · [PDF](https://arxiv.org/pdf/2511.13487) · arXiv 2511.13487

#### [Segmenting Collision Sound Sources in Egocentric Videos](https://arxiv.org/abs/2511.13863)

- **日期：** 2025-11-17
- **问题 / 中文简述：** 多模态与基础模型；采用数据驱动方法，面向声音事件解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2511.13863) · [PDF](https://arxiv.org/pdf/2511.13863) · arXiv 2511.13863

#### [Real-Time Speech Enhancement via a Hybrid ViT: A Dual-Input Acoustic-Image Feature Fusion](https://arxiv.org/abs/2511.11825)

- **日期：** 2025-11-14
- **问题 / 中文简述：** 低信噪比 · 轻量化部署；采用Transformer 表征，面向环境与城市声音解决低信噪比问题。
- **来源：** [论文主页](https://arxiv.org/abs/2511.11825) · [PDF](https://arxiv.org/pdf/2511.11825) · arXiv 2511.11825

#### [MSMT-FN: Multi-segment Multi-task Fusion Network for Marketing Audio Classification](https://arxiv.org/abs/2511.11006)

- **日期：** 2025-11-14
- **问题 / 中文简述：** 轻量化部署；采用层级与多任务学习，面向声音事件解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2511.11006) · [PDF](https://arxiv.org/pdf/2511.11006) · arXiv 2511.11006

#### [Investigation of Feature Selection and Pooling Methods for Environmental Sound Classification](https://arxiv.org/abs/2511.09802)

- **日期：** 2025-11-12
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向环境与城市声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2511.09802) · [PDF](https://arxiv.org/pdf/2511.09802) · arXiv 2511.09802

#### [Uncertainty Calibration of Multi-Label Bird Sound Classifiers](https://arxiv.org/abs/2511.08261)

- **日期：** 2025-11-11
- **问题 / 中文简述：** 长尾与不平衡 · 可解释与可靠性；采用数据驱动方法，面向生态与动物声音解决长尾与不平衡问题。
- **来源：** [论文主页](https://arxiv.org/abs/2511.08261) · [PDF](https://arxiv.org/pdf/2511.08261) · arXiv 2511.08261

#### [DOA Estimation with Lightweight Network on LLM-Aided Simulated Acoustic Scenes](https://arxiv.org/abs/2511.08012)

- **日期：** 2025-11-11
- **问题 / 中文简述：** 定位与分离 · 轻量化部署；采用音频语言模型，面向环境与城市声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2511.08012) · [PDF](https://arxiv.org/pdf/2511.08012) · arXiv 2511.08012

#### [Metric Analysis for Spatial Semantic Segmentation of Sound Scenes](https://arxiv.org/abs/2511.07075)

- **日期：** 2025-11-10
- **问题 / 中文简述：** 定位与分离；采用数据增强与生成，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2511.07075) · [PDF](https://arxiv.org/pdf/2511.07075) · arXiv 2511.07075

#### [SAR-LM Symbolic Audio Reasoning with Large Language Models](https://arxiv.org/abs/2511.06483)

- **日期：** 2025-11-09
- **问题 / 中文简述：** 通用检测与分类；采用音频语言模型开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2511.06483) · [PDF](https://arxiv.org/pdf/2511.06483) · arXiv 2511.06483

#### [Model Merging Improves Zero-Shot Generalization in Bioacoustic Foundation Models](https://arxiv.org/abs/2511.05171)

- **日期：** 2025-11-07
- **问题 / 中文简述：** 开放集/OOD · 多模态与基础模型；采用音频语言模型，面向生态与动物声音解决开放集/OOD问题。
- **来源：** [论文主页](https://arxiv.org/abs/2511.05171) · [PDF](https://arxiv.org/pdf/2511.05171) · arXiv 2511.05171

#### [Lightweight Hopfield Neural Networks for Bioacoustic Detection and Call Monitoring of Captive Primat](https://arxiv.org/abs/2511.11615)

- **日期：** 2025-11-04
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向生态与动物声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2511.11615) · [PDF](https://arxiv.org/pdf/2511.11615) · arXiv 2511.11615

#### [H-Infinity Filter Enhanced CNN-LSTM for Arrhythmia Detection from Heart Sound Recordings](https://arxiv.org/abs/2511.02379)

- **日期：** 2025-11-04
- **问题 / 中文简述：** 低信噪比；采用数据驱动方法，面向医疗与生理声音解决低信噪比问题。
- **来源：** [论文主页](https://arxiv.org/abs/2511.02379) · [PDF](https://arxiv.org/pdf/2511.02379) · arXiv 2511.02379

#### [AudioRAG+- Feedback-driven Retrieval-augmented Audio Generation with Large Audio Language Models](https://arxiv.org/abs/2511.01091)

- **日期：** 2025-11-02
- **问题 / 中文简述：** 多模态与基础模型；采用音频语言模型，面向声音事件解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2511.01091) · [PDF](https://arxiv.org/pdf/2511.01091) · arXiv 2511.01091

#### [More Than A Shortcut: A Hyperbolic Approach To Early-Exit Networks](https://arxiv.org/abs/2511.00641)

- **日期：** 2025-11-01
- **问题 / 中文简述：** 可解释与可靠性 · 轻量化部署；采用层级与多任务学习，面向声音事件解决可解释与可靠性问题。
- **来源：** [论文主页](https://arxiv.org/abs/2511.00641) · [PDF](https://arxiv.org/pdf/2511.00641) · arXiv 2511.00641

#### [NaturalVoices: A Large-Scale, Spontaneous and Emotional Podcast Dataset for Voice Conversion](https://arxiv.org/abs/2511.00256)

- **日期：** 2025-10-31
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2511.00256) · [PDF](https://arxiv.org/pdf/2511.00256) · arXiv 2511.00256

#### [Expressive Range Characterization of Open Text-to-Audio Models](https://arxiv.org/abs/2510.27102)

- **日期：** 2025-10-31
- **问题 / 中文简述：** 多模态与基础模型；采用数据增强与生成，面向环境与城市声音解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2510.27102) · [PDF](https://arxiv.org/pdf/2510.27102) · arXiv 2510.27102

#### [Retaining Mixture Representations for Domain Generalized Anomalous Sound Detection](https://arxiv.org/abs/2510.25182)

- **日期：** 2025-10-29
- **问题 / 中文简述：** 低信噪比；采用自监督表征，面向工业与机械声音解决低信噪比问题。
- **来源：** [论文主页](https://arxiv.org/abs/2510.25182) · [PDF](https://arxiv.org/pdf/2510.25182) · arXiv 2510.25182

#### [Multi-Representation Attention Framework for Underwater Bioacoustic Denoising and Recognition](https://arxiv.org/abs/2510.26838)

- **日期：** 2025-10-29
- **问题 / 中文简述：** 低信噪比 · 开放集/OOD · 轻量化部署；采用Transformer 表征，面向生态与动物声音解决低信噪比问题。
- **来源：** [论文主页](https://arxiv.org/abs/2510.26838) · [PDF](https://arxiv.org/pdf/2510.26838) · arXiv 2510.26838

#### [Joint Analysis of Acoustic Scenes and Sound Events Based on Semi-Supervised Training of Sound Events With Partial Labels](https://arxiv.org/abs/2510.25075)

- **日期：** 2025-10-29
- **问题 / 中文简述：** 半/弱监督 · 轻量化部署；采用层级与多任务学习，面向环境与城市声音解决半/弱监督问题。
- **来源：** [论文主页](https://arxiv.org/abs/2510.25075) · [PDF](https://arxiv.org/pdf/2510.25075) · arXiv 2510.25075

#### [Binaspect -- A Python Library for Binaural Audio Analysis, Visualization & Feature Generation](https://arxiv.org/abs/2510.25714)

- **日期：** 2025-10-29
- **问题 / 中文简述：** 定位与分离 · 轻量化部署；采用数据驱动方法，面向工业与机械声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2510.25714) · [PDF](https://arxiv.org/pdf/2510.25714) · arXiv 2510.25714

#### [Sound Source Localization for Spatial Mapping of Surgical Actions in Dynamic Scenes](https://arxiv.org/abs/2510.24332)

- **日期：** 2025-10-28
- **问题 / 中文简述：** 定位与分离 · 多模态与基础模型；采用Transformer 表征，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2510.24332) · [PDF](https://arxiv.org/pdf/2510.24332) · arXiv 2510.24332

#### [FOA Tokenizer: Low-bitrate Neural Codec for First Order Ambisonics with Spatial Consistency Loss](https://arxiv.org/abs/2510.22241)

- **日期：** 2025-10-25
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2510.22241) · [PDF](https://arxiv.org/pdf/2510.22241) · arXiv 2510.22241

#### [WhaleVAD-BPN: Improving Baleen Whale Call Detection with Boundary Proposal Networks and Post-processing Optimisation](https://arxiv.org/abs/2510.21280)

- **日期：** 2025-10-24
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向生态与动物声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2510.21280) · [PDF](https://arxiv.org/pdf/2510.21280) · arXiv 2510.21280

#### [Compressing Quaternion Convolutional Neural Networks for Audio Classification](https://arxiv.org/abs/2510.21388)

- **日期：** 2025-10-24
- **问题 / 中文简述：** 轻量化部署；采用Transformer 表征，面向声音事件解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2510.21388) · [PDF](https://arxiv.org/pdf/2510.21388) · arXiv 2510.21388

#### [AMAuT A Flexible and Efficient Multiview Audio Transformer Framework Trained from Scratch](https://arxiv.org/abs/2510.19368)

- **日期：** 2025-10-22
- **问题 / 中文简述：** 可解释与可靠性 · 轻量化部署；采用Transformer 表征，面向声音事件解决可解释与可靠性问题。
- **来源：** [论文主页](https://arxiv.org/abs/2510.19368) · [PDF](https://arxiv.org/pdf/2510.19368) · arXiv 2510.19368

#### [Adaptive Per-Channel Energy Normalization Front-end for Robust Audio Signal Processing](https://arxiv.org/abs/2510.18206)

- **日期：** 2025-10-21
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2510.18206) · [PDF](https://arxiv.org/pdf/2510.18206) · arXiv 2510.18206

#### [TopSeg: A Multi-Scale Topological Framework for Data-Efficient Heart Sound Segmentation](https://arxiv.org/abs/2510.17346)

- **日期：** 2025-10-20
- **问题 / 中文简述：** 定位与分离 · 轻量化部署；采用数据驱动方法，面向医疗与生理声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2510.17346) · [PDF](https://arxiv.org/pdf/2510.17346) · arXiv 2510.17346

#### [DDSC Dynamic Dual-Signal Curriculum for Data-Efficient Acoustic Scene Classification under Domain Shift](https://arxiv.org/abs/2510.17345)

- **日期：** 2025-10-20
- **问题 / 中文简述：** 跨域泛化 · 轻量化部署；采用数据驱动方法，面向环境与城市声音解决跨域泛化问题。
- **来源：** [论文主页](https://arxiv.org/abs/2510.17345) · [PDF](https://arxiv.org/pdf/2510.17345) · arXiv 2510.17345

#### [SS-DPPN: A self-supervised dual-path foundation model for the generalizable cardiac audio representation](https://arxiv.org/abs/2510.10719)

- **日期：** 2025-10-12
- **问题 / 中文简述：** 多模态与基础模型 · 可解释与可靠性；采用自监督表征，面向医疗与生理声音解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2510.10719) · [PDF](https://arxiv.org/pdf/2510.10719) · arXiv 2510.10719

#### [MRSAudio: A Large-Scale Multimodal Recorded Spatial Audio Dataset with Refined Annotations](https://arxiv.org/abs/2510.10396)

- **日期：** 2025-10-12
- **问题 / 中文简述：** 定位与分离 · 多模态与基础模型；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2510.10396) · [PDF](https://arxiv.org/pdf/2510.10396) · arXiv 2510.10396

#### [Phase-Aware Deep Learning with Complex-Valued CNNs for Audio Signal Applications](https://arxiv.org/abs/2510.09926)

- **日期：** 2025-10-10
- **问题 / 中文简述：** 轻量化部署；采用数据增强与生成，面向声音事件解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2510.09926) · [PDF](https://arxiv.org/pdf/2510.09926) · arXiv 2510.09926

#### [Detecting and Mitigating Insertion Hallucination in Video-to-Audio Generation](https://arxiv.org/abs/2510.08078)

- **日期：** 2025-10-09
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2510.08078) · [PDF](https://arxiv.org/pdf/2510.08078) · arXiv 2510.08078

#### [Audible Networks: Deconstructing and Manipulating Sounds with Deep Non-Negative Autoencoders](https://arxiv.org/abs/2510.08816)

- **日期：** 2025-10-09
- **问题 / 中文简述：** 通用检测与分类；采用层级与多任务学习开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2510.08816) · [PDF](https://arxiv.org/pdf/2510.08816) · arXiv 2510.08816

#### [Sci-Phi- A Large Language Model Spatial Audio Descriptor](https://arxiv.org/abs/2510.05542)

- **日期：** 2025-10-07
- **问题 / 中文简述：** 定位与分离 · 多模态与基础模型；采用音频语言模型，面向环境与城市声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2510.05542) · [PDF](https://arxiv.org/pdf/2510.05542) · arXiv 2510.05542

#### [Differentiable physics for sound field reconstruction](https://arxiv.org/abs/2510.04459)

- **日期：** 2025-10-06
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2510.04459) · [PDF](https://arxiv.org/pdf/2510.04459) · arXiv 2510.04459

#### [Lightweight and Generalizable Acoustic Scene Representations via Contrastive Fine-Tuning and Distillation](https://arxiv.org/abs/2510.03728)

- **日期：** 2025-10-04
- **问题 / 中文简述：** 少样本 · 轻量化部署；采用对比与原型学习，面向环境与城市声音解决少样本问题。
- **来源：** [论文主页](https://arxiv.org/abs/2510.03728) · [PDF](https://arxiv.org/pdf/2510.03728) · arXiv 2510.03728

#### [Mirage Fools the Ear, Mute Hides the Truth: Precise Targeted Adversarial Attacks on Polyphonic Sound Event Detection Systems](https://arxiv.org/abs/2510.02158)

- **日期：** 2025-10-02
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向工业与机械声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2510.02158) · [PDF](https://arxiv.org/pdf/2510.02158) · arXiv 2510.02158

#### [Latent Multi-view Learning for Robust Environmental Sound Representations](https://arxiv.org/abs/2510.02500)

- **日期：** 2025-10-02
- **问题 / 中文简述：** 通用检测与分类；采用自监督表征开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2510.02500) · [PDF](https://arxiv.org/pdf/2510.02500) · arXiv 2510.02500

#### [When Silence Matters- The Impact of Irrelevant Audio on Text Reasoning in Large Audio-Language Models](https://arxiv.org/abs/2510.00626)

- **日期：** 2025-10-01
- **问题 / 中文简述：** 低信噪比 · 多模态与基础模型 · 轻量化部署；采用音频语言模型，面向环境与城市声音解决低信噪比问题。
- **来源：** [论文主页](https://arxiv.org/abs/2510.00626) · [PDF](https://arxiv.org/pdf/2510.00626) · arXiv 2510.00626

#### [ARIONet: An Advanced Self-supervised Contrastive Representation Network for Birdsong Classification and Future Frame Prediction](https://arxiv.org/abs/2510.00522)

- **日期：** 2025-10-01
- **问题 / 中文简述：** 通用检测与分类；采用自监督表征开展生态与动物声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2510.00522) · [PDF](https://arxiv.org/pdf/2510.00522) · arXiv 2510.00522

#### [When Audio Generators Become Good Listeners: Generative Features for Understanding Tasks](https://arxiv.org/abs/2509.24635)

- **日期：** 2025-09-29
- **问题 / 中文简述：** 通用检测与分类；采用数据增强与生成开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2509.24635) · [PDF](https://arxiv.org/pdf/2509.24635) · arXiv 2509.24635

#### [Unmute the Patch Tokens Rethinking Probing in Multi-Label Audio Classification](https://arxiv.org/abs/2509.24901)

- **日期：** 2025-09-29
- **问题 / 中文简述：** 轻量化部署；采用自监督表征，面向工业与机械声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2509.24901) · [PDF](https://arxiv.org/pdf/2509.24901) · arXiv 2509.24901

#### [Sparse Autoencoders Make Audio Foundation Models more Explainable](https://arxiv.org/abs/2509.24793)

- **日期：** 2025-09-29
- **问题 / 中文简述：** 多模态与基础模型 · 可解释与可靠性；采用自监督表征，面向声音事件解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2509.24793) · [PDF](https://arxiv.org/pdf/2509.24793) · arXiv 2509.24793

#### [Topographic Constraints Shape Brain-Like Component Structure in Auditory Models](https://arxiv.org/abs/2509.24039)

- **日期：** 2025-09-28
- **问题 / 中文简述：** 可解释与可靠性；采用数据驱动方法，面向环境与城市声音解决可解释与可靠性问题。
- **来源：** [论文主页](https://arxiv.org/abs/2509.24039) · [PDF](https://arxiv.org/pdf/2509.24039) · arXiv 2509.24039

#### [A Recall-First CNN for Sleep Apnea Screening from Snoring Audio](https://arxiv.org/abs/2510.00052)

- **日期：** 2025-09-28
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展医疗与生理声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2510.00052) · [PDF](https://arxiv.org/pdf/2510.00052) · arXiv 2510.00052

#### [AudioFuse: Unified Spectral-Temporal Learning via a Hybrid ViT-1D CNN Architecture for Robust Phonocardiogram Classification](https://arxiv.org/abs/2509.23454)

- **日期：** 2025-09-27
- **问题 / 中文简述：** 跨域泛化 · 轻量化部署；采用Transformer 表征，面向医疗与生理声音解决跨域泛化问题。
- **来源：** [论文主页](https://arxiv.org/abs/2509.23454) · [PDF](https://arxiv.org/pdf/2509.23454) · arXiv 2509.23454

#### [Text2Move: Text-to-moving sound generation via trajectory prediction and temporal alignment](https://arxiv.org/abs/2509.21919)

- **日期：** 2025-09-26
- **问题 / 中文简述：** 定位与分离；采用数据增强与生成，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2509.21919) · [PDF](https://arxiv.org/pdf/2509.21919) · arXiv 2509.21919

#### [Cross-Dialect Bird Species Recognition with Dialect-Calibrated Augmentation](https://arxiv.org/abs/2509.22317)

- **日期：** 2025-09-26
- **问题 / 中文简述：** 轻量化部署；采用数据增强与生成，面向生态与动物声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2509.22317) · [PDF](https://arxiv.org/pdf/2509.22317) · arXiv 2509.22317

#### [CMDAR: A Chinese Multi-scene Dynamic Audio Reasoning Benchmark with Diverse Challenges](https://arxiv.org/abs/2509.22461)

- **日期：** 2025-09-26
- **问题 / 中文简述：** 多模态与基础模型；采用音频语言模型，面向环境与城市声音解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2509.22461) · [PDF](https://arxiv.org/pdf/2509.22461) · arXiv 2509.22461

#### [Investigating Modality Contribution in Audio LLMs for Music](https://arxiv.org/abs/2509.20641)

- **日期：** 2025-09-25
- **问题 / 中文简述：** 可解释与可靠性；采用音频语言模型，面向声音事件解决可解释与可靠性问题。
- **来源：** [论文主页](https://arxiv.org/abs/2509.20641) · [PDF](https://arxiv.org/pdf/2509.20641) · arXiv 2509.20641

#### [Thinking While Listening Simple Test Time Scaling For Audio Classification](https://arxiv.org/abs/2509.19676)

- **日期：** 2025-09-24
- **问题 / 中文简述：** 开放集/OOD · 轻量化部署；采用音频语言模型，面向声音事件解决开放集/OOD问题。
- **来源：** [论文主页](https://arxiv.org/abs/2509.19676) · [PDF](https://arxiv.org/pdf/2509.19676) · arXiv 2509.19676

#### [MultiSoundGen: Video-to-Audio Generation for Multi-Event Scenarios via SlowFast Contrastive Audio-Visual Pretraining and Direct Preference Optimization](https://arxiv.org/abs/2509.19999)

- **日期：** 2025-09-24
- **问题 / 中文简述：** 通用检测与分类；采用对比与原型学习开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2509.19999) · [PDF](https://arxiv.org/pdf/2509.19999) · arXiv 2509.19999

#### [Enabling Multi-Species Bird Classification on Low-Power Bioacoustic Loggers](https://arxiv.org/abs/2509.20103)

- **日期：** 2025-09-24
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向生态与动物声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2509.20103) · [PDF](https://arxiv.org/pdf/2509.20103) · arXiv 2509.20103

#### [SynSonic Augmenting Sound Event Detection through Text-to-Audio Diffusion ControlNet and Effective](https://arxiv.org/abs/2509.18603)

- **日期：** 2025-09-23
- **问题 / 中文简述：** 定位与分离；采用数据增强与生成，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2509.18603) · [PDF](https://arxiv.org/pdf/2509.18603) · arXiv 2509.18603

#### [SoundCompass: Navigating Target Sound Extraction With Effective Directional Clue Integration In Complex Acoustic Scenes](https://arxiv.org/abs/2509.18561)

- **日期：** 2025-09-23
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2509.18561) · [PDF](https://arxiv.org/pdf/2509.18561) · arXiv 2509.18561

#### [FlexSED Towards Open-Vocabulary Sound Event Detection](https://arxiv.org/abs/2509.18606)

- **日期：** 2025-09-23
- **问题 / 中文简述：** 少样本 · 开放集/OOD · 定位与分离 · 多模态与基础模型；采用音频语言模型，面向声音事件解决少样本问题。
- **来源：** [论文主页](https://arxiv.org/abs/2509.18606) · [PDF](https://arxiv.org/pdf/2509.18606) · arXiv 2509.18606

#### [An overview of neural architectures for self-supervised audio representation learning from masked spectrograms](https://arxiv.org/abs/2509.18691)

- **日期：** 2025-09-23
- **问题 / 中文简述：** 多模态与基础模型；采用自监督表征，面向声音事件解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2509.18691) · [PDF](https://arxiv.org/pdf/2509.18691) · arXiv 2509.18691

#### [Scattering Transformer: A Training-Free Transformer Architecture for Heart Murmur Detection](https://arxiv.org/abs/2509.18424)

- **日期：** 2025-09-22
- **问题 / 中文简述：** 多模态与基础模型 · 轻量化部署；采用自监督表征，面向医疗与生理声音解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2509.18424) · [PDF](https://arxiv.org/pdf/2509.18424) · arXiv 2509.18424

#### [Identifying birdsong syllables without labelled data](https://arxiv.org/abs/2509.18412)

- **日期：** 2025-09-22
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2509.18412) · [PDF](https://arxiv.org/pdf/2509.18412) · arXiv 2509.18412

#### [STAR: Speech-to-Audio Generation via Representation Learning](https://arxiv.org/abs/2509.17164)

- **日期：** 2025-09-21
- **问题 / 中文简述：** 多模态与基础模型；采用数据驱动方法，面向声音事件解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2509.17164) · [PDF](https://arxiv.org/pdf/2509.17164) · arXiv 2509.17164

#### [DeepASA: An Object-Oriented Multi-Purpose Network for Auditory Scene Analysis](https://arxiv.org/abs/2509.17247)

- **日期：** 2025-09-21
- **问题 / 中文简述：** 定位与分离；采用Transformer 表征，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2509.17247) · [PDF](https://arxiv.org/pdf/2509.17247) · arXiv 2509.17247

#### [MAGENTA: Magnitude and Geometry-Enhanced Training Approach for Long-Tailed Sound Event Localization and Detection](https://arxiv.org/abs/2509.15599)

- **日期：** 2025-09-19
- **问题 / 中文简述：** 长尾与不平衡 · 定位与分离；采用数据驱动方法，面向声音事件解决长尾与不平衡问题。
- **来源：** [论文主页](https://arxiv.org/abs/2509.15599) · [PDF](https://arxiv.org/pdf/2509.15599) · arXiv 2509.15599

#### [CompSpoof: A Dataset and Joint Learning Framework for Component-Level Audio Anti-spoofing Countermeasures](https://arxiv.org/abs/2509.15804)

- **日期：** 2025-09-19
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向环境与城市声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2509.15804) · [PDF](https://arxiv.org/pdf/2509.15804) · arXiv 2509.15804

#### [AFT: An Exemplar-Free Class Incremental Learning Method for Environmental Sound Classification](https://arxiv.org/abs/2509.15523)

- **日期：** 2025-09-19
- **问题 / 中文简述：** 持续学习 · 轻量化部署；采用数据驱动方法，面向生态与动物声音解决持续学习问题。
- **来源：** [论文主页](https://arxiv.org/abs/2509.15523) · [PDF](https://arxiv.org/pdf/2509.15523) · arXiv 2509.15523

#### [A Steered Response Power Method for Sound Source Localization With Generic Acoustic Models](https://arxiv.org/abs/2509.15702)

- **日期：** 2025-09-19
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2509.15702) · [PDF](https://arxiv.org/pdf/2509.15702) · arXiv 2509.15702

#### [Temporally Heterogeneous Graph Contrastive Learning for Multimodal Acoustic event Classification](https://arxiv.org/abs/2509.14893)

- **日期：** 2025-09-18
- **问题 / 中文简述：** 多模态与基础模型 · 轻量化部署；采用对比与原型学习，面向声音事件解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2509.14893) · [PDF](https://arxiv.org/pdf/2509.14893) · arXiv 2509.14893

#### [Pre-training Autoencoder for Acoustic Event Classification via Blinky](https://arxiv.org/abs/2509.15261)

- **日期：** 2025-09-18
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向声音事件解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2509.15261) · [PDF](https://arxiv.org/pdf/2509.15261) · arXiv 2509.15261

#### [DSpAST Disentangled Representations for Spatial Audio Reasoning with Large Language Models](https://arxiv.org/abs/2509.13927)

- **日期：** 2025-09-17
- **问题 / 中文简述：** 定位与分离；采用音频语言模型，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2509.13927) · [PDF](https://arxiv.org/pdf/2509.13927) · arXiv 2509.13927

#### [Comprehensive Evaluation of CNN-Based Audio Tagging Models on Resource-Constrained Devices](https://arxiv.org/abs/2509.14049)

- **日期：** 2025-09-17
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向声音事件解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2509.14049) · [PDF](https://arxiv.org/pdf/2509.14049) · arXiv 2509.14049

#### [Improving Anomalous Sound Detection with Attribute-aware Representation from Domain-adaptive Pre-tra](https://arxiv.org/abs/2509.12845)

- **日期：** 2025-09-16
- **问题 / 中文简述：** 通用检测与分类；采用层级与多任务学习开展工业与机械声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2509.12845) · [PDF](https://arxiv.org/pdf/2509.12845) · arXiv 2509.12845

#### [Scaling to Multimodal and Multichannel Heart Sound Classification with Synthetic and Augmented Biosignals](https://arxiv.org/abs/2509.11606)

- **日期：** 2025-09-15
- **问题 / 中文简述：** 低信噪比 · 多模态与基础模型 · 轻量化部署；采用Transformer 表征，面向医疗与生理声音解决低信噪比问题。
- **来源：** [论文主页](https://arxiv.org/abs/2509.11606) · [PDF](https://arxiv.org/pdf/2509.11606) · arXiv 2509.11606

#### [An Entropy-Guided Curriculum Learning Strategy for Data-Efficient Acoustic Scene Classification under Domain Shift](https://arxiv.org/abs/2509.11168)

- **日期：** 2025-09-14
- **问题 / 中文简述：** 少样本 · 跨域泛化 · 可解释与可靠性 · 轻量化部署；采用数据增强与生成，面向环境与城市声音解决少样本问题。
- **来源：** [论文主页](https://arxiv.org/abs/2509.11168) · [PDF](https://arxiv.org/pdf/2509.11168) · arXiv 2509.11168

#### [Prototypical Contrastive Learning For Improved Few-Shot Audio Classification](https://arxiv.org/abs/2509.10074)

- **日期：** 2025-09-12
- **问题 / 中文简述：** 少样本；采用Transformer 表征，面向声音事件解决少样本问题。
- **来源：** [论文主页](https://arxiv.org/abs/2509.10074) · [PDF](https://arxiv.org/pdf/2509.10074) · arXiv 2509.10074

#### [Improving Audio Event Recognition with Consistency Regularization](https://arxiv.org/abs/2509.10391)

- **日期：** 2025-09-12
- **问题 / 中文简述：** 半/弱监督；采用数据增强与生成，面向声音事件解决半/弱监督问题。
- **来源：** [论文主页](https://arxiv.org/abs/2509.10391) · [PDF](https://arxiv.org/pdf/2509.10391) · arXiv 2509.10391

#### [Region-Specific Audio Tagging for Spatial Sound](https://arxiv.org/abs/2509.09526)

- **日期：** 2025-09-11
- **问题 / 中文简述：** 定位与分离；采用Transformer 表征，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2509.09526) · [PDF](https://arxiv.org/pdf/2509.09526) · arXiv 2509.09526

#### [Deep Learning for Tuberculosis Screening in a High-burden Setting using Cough Analysis and Speech Foundation Models](https://arxiv.org/abs/2509.09746)

- **日期：** 2025-09-11
- **问题 / 中文简述：** 多模态与基础模型；采用数据驱动方法，面向医疗与生理声音解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2509.09746) · [PDF](https://arxiv.org/pdf/2509.09746) · arXiv 2509.09746

#### [Adaptive Knowledge Distillation using a Device-Aware Teacher for Low-Complexity Acoustic Scene Classification](https://arxiv.org/abs/2509.09262)

- **日期：** 2025-09-11
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向环境与城市声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2509.09262) · [PDF](https://arxiv.org/pdf/2509.09262) · arXiv 2509.09262

#### [Spectral and Rhythm Feature Performance Evaluation for Category and Class Level Audio Classification with Deep Convolutional Neural Networks](https://arxiv.org/abs/2509.07756)

- **日期：** 2025-09-09
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向环境与城市声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2509.07756) · [PDF](https://arxiv.org/pdf/2509.07756) · arXiv 2509.07756

#### [TSPC: A Two-Stage Phoneme-Centric Architecture for code-switching Vietnamese-English Speech Recognition](https://arxiv.org/abs/2509.05983)

- **日期：** 2025-09-07
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向声音事件解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2509.05983) · [PDF](https://arxiv.org/pdf/2509.05983) · arXiv 2509.05983

#### [DreamAudio- Customized Text-to-Audio Generation with Diffusion Models](https://arxiv.org/abs/2509.06027)

- **日期：** 2025-09-07
- **问题 / 中文简述：** 通用检测与分类；采用数据增强与生成开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2509.06027) · [PDF](https://arxiv.org/pdf/2509.06027) · arXiv 2509.06027

#### [Recomposer- Event-roll-guided generative audio editing](https://arxiv.org/abs/2509.05256)

- **日期：** 2025-09-05
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2509.05256) · [PDF](https://arxiv.org/pdf/2509.05256) · arXiv 2509.05256

#### [A Multiclass Acoustic Dataset and Interactive Tool for Analyzing Drone Signatures in Real-World Environments](https://arxiv.org/abs/2509.04715)

- **日期：** 2025-09-05
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向交通与水下声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2509.04715) · [PDF](https://arxiv.org/pdf/2509.04715) · arXiv 2509.04715

#### [On Time Delay Interpolation for Improved Acoustic Reflector Localization](https://arxiv.org/abs/2509.04629)

- **日期：** 2025-09-04
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向环境与城市声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2509.04629) · [PDF](https://arxiv.org/pdf/2509.04629) · arXiv 2509.04629

#### [GetNetUPAM: Ecologically Informed Nested Cross-Validation and Noise-Robust Attention for Marine Bioacoustic Monitoring](https://arxiv.org/abs/2509.04682)

- **日期：** 2025-09-04
- **问题 / 中文简述：** 低信噪比 · 定位与分离；采用Transformer 表征，面向生态与动物声音解决低信噪比问题。
- **来源：** [论文主页](https://arxiv.org/abs/2509.04682) · [PDF](https://arxiv.org/pdf/2509.04682) · arXiv 2509.04682

#### [IS${}^3$ : Generic Impulsive--Stationary Sound Separation in Acoustic Scenes using Deep Filtering](https://arxiv.org/abs/2509.02622)

- **日期：** 2025-09-01
- **问题 / 中文简述：** 定位与分离 · 轻量化部署；采用数据驱动方法，面向生态与动物声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2509.02622) · [PDF](https://arxiv.org/pdf/2509.02622) · arXiv 2509.02622

#### [EZhouNet:A framework based on graph neural network and anchor interval for the respiratory sound event detection](https://arxiv.org/abs/2509.01153)

- **日期：** 2025-09-01
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向医疗与生理声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2509.01153) · [PDF](https://arxiv.org/pdf/2509.01153) · arXiv 2509.01153

#### [PicoAudio2: Temporal Controllable Text-to-Audio Generation with Natural Language Description](https://arxiv.org/abs/2509.00683)

- **日期：** 2025-08-31
- **问题 / 中文简述：** 通用检测与分类；采用数据增强与生成开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2509.00683) · [PDF](https://arxiv.org/pdf/2509.00683) · arXiv 2509.00683

#### [Towards High-Fidelity and Controllable Bioacoustic Generation via Enhanced Diffusion Learning](https://arxiv.org/abs/2509.00318)

- **日期：** 2025-08-30
- **问题 / 中文简述：** 低信噪比 · 轻量化部署；采用数据增强与生成，面向生态与动物声音解决低信噪比问题。
- **来源：** [论文主页](https://arxiv.org/abs/2509.00318) · [PDF](https://arxiv.org/pdf/2509.00318) · arXiv 2509.00318

#### [WoW-Bench Evaluating Fine-Grained Acoustic Perception in Audio-Language Models via Marine Mammal Vocalizations](https://arxiv.org/abs/2508.20976)

- **日期：** 2025-08-28
- **问题 / 中文简述：** 开放集/OOD · 多模态与基础模型 · 轻量化部署；采用音频语言模型，面向生态与动物声音解决开放集/OOD问题。
- **来源：** [论文主页](https://arxiv.org/abs/2508.20976) · [PDF](https://arxiv.org/pdf/2508.20976) · arXiv 2508.20976

#### [Full-Frequency Temporal Patching and Structured Masking for Enhanced Audio Classification](https://arxiv.org/abs/2508.21243)

- **日期：** 2025-08-28
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2508.21243) · [PDF](https://arxiv.org/pdf/2508.21243) · arXiv 2508.21243

#### [Infant Cry Detection In Noisy Environment Using Blueprint Separable Convolutions and Time-Frequency Recurrent Neural Network](https://arxiv.org/abs/2508.19308)

- **日期：** 2025-08-26
- **问题 / 中文简述：** 低信噪比 · 轻量化部署；采用Transformer 表征，面向声音事件解决低信噪比问题。
- **来源：** [论文主页](https://arxiv.org/abs/2508.19308) · [PDF](https://arxiv.org/pdf/2508.19308) · arXiv 2508.19308

#### [Multi-scale Scanning Network for Machine Anomalous Sound Detection](https://arxiv.org/abs/2508.17194)

- **日期：** 2025-08-24
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向工业与机械声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2508.17194) · [PDF](https://arxiv.org/pdf/2508.17194) · arXiv 2508.17194

#### [AudioSet-R- A Refined AudioSet with Multi-Stage LLM Label Reannotation](https://arxiv.org/abs/2508.15429)

- **日期：** 2025-08-21
- **问题 / 中文简述：** 多模态与基础模型 · 可解释与可靠性；采用音频语言模型，面向声音事件解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2508.15429) · [PDF](https://arxiv.org/pdf/2508.15429) · arXiv 2508.15429

#### [An Enhanced Audio Feature Tailored for Anomalous Sound Detection Based on Pre-trained Models](https://arxiv.org/abs/2508.15334)

- **日期：** 2025-08-21
- **问题 / 中文简述：** 可解释与可靠性 · 轻量化部署；采用Transformer 表征，面向工业与机械声音解决可解释与可靠性问题。
- **来源：** [论文主页](https://arxiv.org/abs/2508.15334) · [PDF](https://arxiv.org/pdf/2508.15334) · arXiv 2508.15334

#### [ASCMamba: Multimodal Time-Frequency Mamba for Acoustic Scene Classification](https://arxiv.org/abs/2508.15632)

- **日期：** 2025-08-21
- **问题 / 中文简述：** 半/弱监督 · 多模态与基础模型；采用层级与多任务学习，面向环境与城市声音解决半/弱监督问题。
- **来源：** [论文主页](https://arxiv.org/abs/2508.15632) · [PDF](https://arxiv.org/pdf/2508.15632) · arXiv 2508.15632

#### [XAI-Driven Spectral Analysis of Cough Sounds for Respiratory Disease Characterization](https://arxiv.org/abs/2508.14949)

- **日期：** 2025-08-20
- **问题 / 中文简述：** 可解释与可靠性；采用数据驱动方法，面向医疗与生理声音解决可解释与可靠性问题。
- **来源：** [论文主页](https://arxiv.org/abs/2508.14949) · [PDF](https://arxiv.org/pdf/2508.14949) · arXiv 2508.14949

#### [Denoising by neural network for muzzle blast detection](https://arxiv.org/abs/2508.14919)

- **日期：** 2025-08-18
- **问题 / 中文简述：** 低信噪比 · 轻量化部署；采用数据驱动方法，面向交通与水下声音解决低信噪比问题。
- **来源：** [论文主页](https://arxiv.org/abs/2508.14919) · [PDF](https://arxiv.org/pdf/2508.14919) · arXiv 2508.14919

#### [HDA-SELD Hierarchical Cross-Modal Distillation with Multi-Level Data Augmentation for Low-Resource Audio-Visual Sound Event Localization and Detection](https://arxiv.org/abs/2508.12334)

- **日期：** 2025-08-17
- **问题 / 中文简述：** 少样本 · 定位与分离 · 轻量化部署；采用层级与多任务学习，面向声音事件解决少样本问题。
- **来源：** [论文主页](https://arxiv.org/abs/2508.12334) · [PDF](https://arxiv.org/pdf/2508.12334) · arXiv 2508.12334

#### [Towards Automatic Evaluation and High-Quality Pseudo-Parallel Dataset Construction for Audio Editing: A Human-in-the-Loop Method](https://arxiv.org/abs/2508.11966)

- **日期：** 2025-08-16
- **问题 / 中文简述：** 轻量化部署；采用数据增强与生成，面向声音事件解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2508.11966) · [PDF](https://arxiv.org/pdf/2508.11966) · arXiv 2508.11966

#### [A dataset and model for auditory scene recognition for hearing devices: AHEAD-DS and OpenYAMNet](https://arxiv.org/abs/2508.10360)

- **日期：** 2025-08-14
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向工业与机械声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2508.10360) · [PDF](https://arxiv.org/pdf/2508.10360) · arXiv 2508.10360

#### [No Free Lunch from Audio Pretraining in Bioacoustics A Benchmark Study of Embeddings](https://arxiv.org/abs/2508.10230)

- **日期：** 2025-08-13
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展生态与动物声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2508.10230) · [PDF](https://arxiv.org/pdf/2508.10230) · arXiv 2508.10230

#### [Transient Noise Removal via Diffusion-based Speech Inpainting](https://arxiv.org/abs/2508.08890)

- **日期：** 2025-08-12
- **问题 / 中文简述：** 通用检测与分类；采用数据增强与生成开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2508.08890) · [PDF](https://arxiv.org/pdf/2508.08890) · arXiv 2508.08890

#### [Real-time CARFAC Cochlea Model Acceleration on FPGA for Underwater Acoustic Sensing Systems](https://arxiv.org/abs/2508.07523)

- **日期：** 2025-08-11
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向交通与水下声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2508.07523) · [PDF](https://arxiv.org/pdf/2508.07523) · arXiv 2508.07523

#### [Auditory Intelligence Understanding the World Through Sound](https://arxiv.org/abs/2508.07829)

- **日期：** 2025-08-11
- **问题 / 中文简述：** 可解释与可靠性；采用层级与多任务学习，面向工业与机械声音解决可解释与可靠性问题。
- **来源：** [论文主页](https://arxiv.org/abs/2508.07829) · [PDF](https://arxiv.org/pdf/2508.07829) · arXiv 2508.07829

#### [Noise-Robust Sound Event Detection and Counting via Language-Queried Sound Separation](https://arxiv.org/abs/2508.07176)

- **日期：** 2025-08-10
- **问题 / 中文简述：** 低信噪比 · 定位与分离；采用层级与多任务学习，面向声音事件解决低信噪比问题。
- **来源：** [论文主页](https://arxiv.org/abs/2508.07176) · [PDF](https://arxiv.org/pdf/2508.07176) · arXiv 2508.07176

#### [ESDD 2026: Environmental Sound Deepfake Detection Challenge Evaluation Plan](https://arxiv.org/abs/2508.04529)

- **日期：** 2025-08-06
- **问题 / 中文简述：** 少样本；采用数据驱动方法，面向环境与城市声音解决少样本问题。
- **来源：** [论文主页](https://arxiv.org/abs/2508.04529) · [PDF](https://arxiv.org/pdf/2508.04529) · arXiv 2508.04529

#### [Binaural Sound Event Localization and Detection Neural Network based on HRTF Localization Cues for H](https://arxiv.org/abs/2508.04333)

- **日期：** 2025-08-06
- **问题 / 中文简述：** 定位与分离 · 轻量化部署；采用数据驱动方法，面向环境与城市声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2508.04333) · [PDF](https://arxiv.org/pdf/2508.04333) · arXiv 2508.04333

#### [CoughViT: A Self-Supervised Vision Transformer for Cough Audio Representation Learning](https://arxiv.org/abs/2508.03764)

- **日期：** 2025-08-04
- **问题 / 中文简述：** 通用检测与分类；采用自监督表征开展医疗与生理声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2508.03764) · [PDF](https://arxiv.org/pdf/2508.03764) · arXiv 2508.03764

#### [Foundation Models for Bioacoustics -- a Comparative Review](https://arxiv.org/abs/2508.01277)

- **日期：** 2025-08-02
- **问题 / 中文简述：** 多模态与基础模型；采用自监督表征，面向生态与动物声音解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2508.01277) · [PDF](https://arxiv.org/pdf/2508.01277) · arXiv 2508.01277

#### [Acoustic Imaging for UAV Detection: Dense Beamformed Energy Maps and U-Net SELD](https://arxiv.org/abs/2508.00307)

- **日期：** 2025-08-01
- **问题 / 中文简述：** 长尾与不平衡 · 定位与分离；采用数据驱动方法，面向交通与水下声音解决长尾与不平衡问题。
- **来源：** [论文主页](https://arxiv.org/abs/2508.00307) · [PDF](https://arxiv.org/pdf/2508.00307) · arXiv 2508.00307

#### [A Two-Step Learning Framework for Enhancing Sound Event Localization and Detection](https://arxiv.org/abs/2507.22322)

- **日期：** 2025-07-30
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2507.22322) · [PDF](https://arxiv.org/pdf/2507.22322) · arXiv 2507.22322

#### [MIMII-Agent Leveraging LLMs with Function Calling for Relative Evaluation of Anomalous Sound Detection](https://arxiv.org/abs/2507.20666)

- **日期：** 2025-07-28
- **问题 / 中文简述：** 通用检测与分类；采用音频语言模型开展工业与机械声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2507.20666) · [PDF](https://arxiv.org/pdf/2507.20666) · arXiv 2507.20666

#### [JAM: A Tiny Flow-based Song Generator with Fine-grained Controllability and Aesthetic Alignment](https://arxiv.org/abs/2507.20880)

- **日期：** 2025-07-28
- **问题 / 中文简述：** 轻量化部署；采用数据增强与生成，面向声音事件解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2507.20880) · [PDF](https://arxiv.org/pdf/2507.20880) · arXiv 2507.20880

#### [Binaural Sound Event Localization and Detection based on HRTF Cues for Humanoid Robots](https://arxiv.org/abs/2507.20530)

- **日期：** 2025-07-28
- **问题 / 中文简述：** 定位与分离；采用数据增强与生成，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2507.20530) · [PDF](https://arxiv.org/pdf/2507.20530) · arXiv 2507.20530

#### [Improving Deep Learning-based Respiratory Sound Analysis with Frequency Selection and Attention Mechanism](https://arxiv.org/abs/2507.20052)

- **日期：** 2025-07-26
- **问题 / 中文简述：** 低信噪比 · 轻量化部署；采用Transformer 表征，面向医疗与生理声音解决低信噪比问题。
- **来源：** [论文主页](https://arxiv.org/abs/2507.20052) · [PDF](https://arxiv.org/pdf/2507.20052) · arXiv 2507.20052

#### [Improving Audio Classification by Transitioning from Zero- to Few-Shot](https://arxiv.org/abs/2507.20036)

- **日期：** 2025-07-26
- **问题 / 中文简述：** 少样本 · 低信噪比 · 开放集/OOD；采用对比与原型学习，面向声音事件解决少样本问题。
- **来源：** [论文主页](https://arxiv.org/abs/2507.20036) · [PDF](https://arxiv.org/pdf/2507.20036) · arXiv 2507.20036

#### [Joint Feature and Output Distillation for Low-complexity Acoustic Scene Classification](https://arxiv.org/abs/2507.19557)

- **日期：** 2025-07-25
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向环境与城市声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2507.19557) · [PDF](https://arxiv.org/pdf/2507.19557) · arXiv 2507.19557

#### [CatchPhrase: EXPrompt-Guided Encoder Adaptation for Audio-to-Image Generation](https://arxiv.org/abs/2507.18750)

- **日期：** 2025-07-24
- **问题 / 中文简述：** 轻量化部署；采用音频语言模型，面向声音事件解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2507.18750) · [PDF](https://arxiv.org/pdf/2507.18750) · arXiv 2507.18750

#### [Resnet-conformer network with shared weights and attention mechanism for sound event localization, d](https://arxiv.org/abs/2507.17941)

- **日期：** 2025-07-23
- **问题 / 中文简述：** 定位与分离；采用Transformer 表征，面向工业与机械声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2507.17941) · [PDF](https://arxiv.org/pdf/2507.17941) · arXiv 2507.17941

#### [On Temporal Guidance and Iterative Refinement in Audio Source Separation](https://arxiv.org/abs/2507.17297)

- **日期：** 2025-07-23
- **问题 / 中文简述：** 定位与分离；采用Transformer 表征，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2507.17297) · [PDF](https://arxiv.org/pdf/2507.17297) · arXiv 2507.17297

#### [TTMBA: Towards Text To Multiple Sources Binaural Audio Generation](https://arxiv.org/abs/2507.16564)

- **日期：** 2025-07-22
- **问题 / 中文简述：** 通用检测与分类；采用音频语言模型开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2507.16564) · [PDF](https://arxiv.org/pdf/2507.16564) · arXiv 2507.16564

#### [SALM Spatial Audio Language Model with Structured Embeddings for Understanding and Editing](https://arxiv.org/abs/2507.16724)

- **日期：** 2025-07-22
- **问题 / 中文简述：** 开放集/OOD · 定位与分离 · 多模态与基础模型；采用音频语言模型，面向环境与城市声音解决开放集/OOD问题。
- **来源：** [论文主页](https://arxiv.org/abs/2507.16724) · [PDF](https://arxiv.org/pdf/2507.16724) · arXiv 2507.16724

#### [Detect Any Sound Open-Vocabulary Sound Event Detection with Multi-Modal Queries](https://arxiv.org/abs/2507.16343)

- **日期：** 2025-07-22
- **问题 / 中文简述：** 开放集/OOD · 定位与分离 · 多模态与基础模型；采用音频语言模型，面向声音事件解决开放集/OOD问题。
- **来源：** [论文主页](https://arxiv.org/abs/2507.16343) · [PDF](https://arxiv.org/pdf/2507.16343) · arXiv 2507.16343

#### [An Investigation of Test-time Adaptation for Audio Classification under Background Noise](https://arxiv.org/abs/2507.15523)

- **日期：** 2025-07-21
- **问题 / 中文简述：** 跨域泛化；采用数据驱动方法，面向声音事件解决跨域泛化问题。
- **来源：** [论文主页](https://arxiv.org/abs/2507.15523) · [PDF](https://arxiv.org/pdf/2507.15523) · arXiv 2507.15523

#### [Enhancing Lung Disease Diagnosis via Semi-Supervised Machine Learning](https://arxiv.org/abs/2507.16845)

- **日期：** 2025-07-20
- **问题 / 中文简述：** 半/弱监督；采用数据驱动方法，面向医疗与生理声音解决半/弱监督问题。
- **来源：** [论文主页](https://arxiv.org/abs/2507.16845) · [PDF](https://arxiv.org/pdf/2507.16845) · arXiv 2507.16845

#### [OpenBEATs A Fully Open-Source General-Purpose Audio Encoder](https://arxiv.org/abs/2507.14129)

- **日期：** 2025-07-18
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2507.14129) · [PDF](https://arxiv.org/pdf/2507.14129) · arXiv 2507.14129

#### [Task-Specific Audio Coding for Machines: Machine-Learned Latent Features Are Codes for That Machine](https://arxiv.org/abs/2507.12701)

- **日期：** 2025-07-17
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向工业与机械声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2507.12701) · [PDF](https://arxiv.org/pdf/2507.12701) · arXiv 2507.12701

#### [Stereo Sound Event Localization and Detection with Onscreen_Offscreen Classification](https://arxiv.org/abs/2507.12042)

- **日期：** 2025-07-16
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2507.12042) · [PDF](https://arxiv.org/pdf/2507.12042) · arXiv 2507.12042

#### [Developing an AI-Guided Assistant Device for the Deaf and Hearing Impaired](https://arxiv.org/abs/2507.14215)

- **日期：** 2025-07-16
- **问题 / 中文简述：** 定位与分离 · 多模态与基础模型；采用音频语言模型，面向工业与机械声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2507.14215) · [PDF](https://arxiv.org/pdf/2507.14215) · arXiv 2507.14215

#### [A Multimodal Data Fusion Attention-Empowered Generative Adversarial Network for Real Time 3D Underwater Sound Speed Field Construction](https://arxiv.org/abs/2507.11812)

- **日期：** 2025-07-16
- **问题 / 中文简述：** 多模态与基础模型；采用Transformer 表征，面向交通与水下声音解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2507.11812) · [PDF](https://arxiv.org/pdf/2507.11812) · arXiv 2507.11812

#### [Standardized Evaluation of Fetal Phonocardiography Processing Methods](https://arxiv.org/abs/2507.10783)

- **日期：** 2025-07-14
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展医疗与生理声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2507.10783) · [PDF](https://arxiv.org/pdf/2507.10783) · arXiv 2507.10783

#### [AUDIOMAE++ LEARNING BETTER MASKED AUDIO REPRESENTATIONS WITH SWIGLU FFNS](https://arxiv.org/abs/2507.10464)

- **日期：** 2025-07-14
- **问题 / 中文简述：** 通用检测与分类；采用自监督表征开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2507.10464) · [PDF](https://arxiv.org/pdf/2507.10464) · arXiv 2507.10464

#### [Ensemble Confidence Calibration for Sound Event Detection in Open-environment](https://arxiv.org/abs/2507.09606)

- **日期：** 2025-07-13
- **问题 / 中文简述：** 开放集/OOD · 可解释与可靠性；采用数据驱动方法，面向声音事件解决开放集/OOD问题。
- **来源：** [论文主页](https://arxiv.org/abs/2507.09606) · [PDF](https://arxiv.org/pdf/2507.09606) · arXiv 2507.09606

#### [Enhancing Stereo Sound Event Detection with BiMamba and Pretrained PSELDnet](https://arxiv.org/abs/2507.09570)

- **日期：** 2025-07-13
- **问题 / 中文简述：** 定位与分离；采用Transformer 表征，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2507.09570) · [PDF](https://arxiv.org/pdf/2507.09570) · arXiv 2507.09570

#### [Towards Spatial Audio Understanding Via Question Answering](https://arxiv.org/abs/2507.09195)

- **日期：** 2025-07-12
- **问题 / 中文简述：** 定位与分离；采用音频语言模型，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2507.09195) · [PDF](https://arxiv.org/pdf/2507.09195) · arXiv 2507.09195

#### [Enforcing Speech Content Privacy in Environmental Sound Recordings using Segment-wise Waveform Reversal](https://arxiv.org/abs/2507.08412)

- **日期：** 2025-07-11
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向环境与城市声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2507.08412) · [PDF](https://arxiv.org/pdf/2507.08412) · arXiv 2507.08412

#### [Distilling Spectrograms into Tokens Fast and Lightweight Bioacoustic Classification for BirdCLEF+ 2](https://arxiv.org/abs/2507.08236)

- **日期：** 2025-07-11
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向生态与动物声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2507.08236) · [PDF](https://arxiv.org/pdf/2507.08236) · arXiv 2507.08236

#### [LISTEN: Lightweight Industrial Sound-representable Transformer for Edge Notification](https://arxiv.org/abs/2507.07879)

- **日期：** 2025-07-10
- **问题 / 中文简述：** 多模态与基础模型 · 轻量化部署；采用Transformer 表征，面向工业与机械声音解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2507.07879) · [PDF](https://arxiv.org/pdf/2507.07879) · arXiv 2507.07879

#### [AV-SSAN: Audio-Visual Selective DoA Estimation through Explicit Multi-Band Semantic-Spatial Alignment](https://arxiv.org/abs/2507.07384)

- **日期：** 2025-07-10
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2507.07384) · [PDF](https://arxiv.org/pdf/2507.07384) · arXiv 2507.07384

#### [IMPACT: Industrial Machine Perception via Acoustic Cognitive Transformer](https://arxiv.org/abs/2507.06481)

- **日期：** 2025-07-09
- **问题 / 中文简述：** 多模态与基础模型 · 轻量化部署；采用自监督表征，面向工业与机械声音解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2507.06481) · [PDF](https://arxiv.org/pdf/2507.06481) · arXiv 2507.06481

#### [Comparative Analysis of CNN and Transformer Architectures with Heart Cycle Normalization for Automated Phonocardiogram Classification](https://arxiv.org/abs/2507.07058)

- **日期：** 2025-07-08
- **问题 / 中文简述：** 开放集/OOD；采用Transformer 表征，面向医疗与生理声音解决开放集/OOD问题。
- **来源：** [论文主页](https://arxiv.org/abs/2507.07058) · [PDF](https://arxiv.org/pdf/2507.07058) · arXiv 2507.07058

#### [Direction Estimation of Sound Sources Using Microphone Arrays and Signal Strength](https://arxiv.org/abs/2507.03466)

- **日期：** 2025-07-04
- **问题 / 中文简述：** 定位与分离 · 轻量化部署；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2507.03466) · [PDF](https://arxiv.org/pdf/2507.03466) · arXiv 2507.03466

#### [Padé Approximant Neural Networks for Enhanced Electric Motor Fault Diagnosis Using Vibration and Acoustic Data](https://arxiv.org/abs/2507.02599)

- **日期：** 2025-07-03
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展工业与机械声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2507.02599) · [PDF](https://arxiv.org/pdf/2507.02599) · arXiv 2507.02599

#### [DeSTA2.5-Audio: Toward General-Purpose Large Audio Language Model with Self-Generated Cross-Modal Alignment](https://arxiv.org/abs/2507.02768)

- **日期：** 2025-07-03
- **问题 / 中文简述：** 开放集/OOD · 多模态与基础模型 · 轻量化部署；采用音频语言模型，面向环境与城市声音解决开放集/OOD问题。
- **来源：** [论文主页](https://arxiv.org/abs/2507.02768) · [PDF](https://arxiv.org/pdf/2507.02768) · arXiv 2507.02768

#### [ASDA Audio Spectrogram Differential Attention Mechanism for Self-Supervised Representation Learning](https://arxiv.org/abs/2507.02666)

- **日期：** 2025-07-03
- **问题 / 中文简述：** 轻量化部署；采用自监督表征，面向环境与城市声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2507.02666) · [PDF](https://arxiv.org/pdf/2507.02666) · arXiv 2507.02666

#### [Real-Time Emergency Vehicle Siren Detection with Efficient CNNs on Embedded Hardware](https://arxiv.org/abs/2507.01563)

- **日期：** 2025-07-02
- **问题 / 中文简述：** 可解释与可靠性 · 轻量化部署；采用数据驱动方法，面向工业与机械声音解决可解释与可靠性问题。
- **来源：** [论文主页](https://arxiv.org/abs/2507.01563) · [PDF](https://arxiv.org/pdf/2507.01563) · arXiv 2507.01563

#### [AudioBERTScore: Objective Evaluation of Environmental Sound Synthesis Based on Similarity of Audio embedding Sequences](https://arxiv.org/abs/2507.00475)

- **日期：** 2025-07-01
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2507.00475) · [PDF](https://arxiv.org/pdf/2507.00475) · arXiv 2507.00475

#### [A Review on Sound Source Localization in Robotics Focusing on Deep Learning Methods](https://arxiv.org/abs/2507.01143)

- **日期：** 2025-07-01
- **问题 / 中文简述：** 定位与分离；采用Transformer 表征，面向工业与机械声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2507.01143) · [PDF](https://arxiv.org/pdf/2507.01143) · arXiv 2507.01143

#### [From Large-scale Audio Tagging to Real-Time Explainable Emergency Vehicle Sirens Detection](https://arxiv.org/abs/2506.23437)

- **日期：** 2025-06-30
- **问题 / 中文简述：** 跨域泛化 · 可解释与可靠性 · 轻量化部署；采用数据驱动方法，面向交通与水下声音解决跨域泛化问题。
- **来源：** [论文主页](https://arxiv.org/abs/2506.23437) · [PDF](https://arxiv.org/pdf/2506.23437) · arXiv 2506.23437

#### [Feasibility of spectral-element modeling of wave propagation through the anatomy of marine mammals](https://arxiv.org/abs/2506.22944)

- **日期：** 2025-06-28
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向生态与动物声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2506.22944) · [PDF](https://arxiv.org/pdf/2506.22944) · arXiv 2506.22944

#### [Step-by-Step Video-to-Audio Synthesis via Negative Audio Guidance](https://arxiv.org/abs/2506.20995)

- **日期：** 2025-06-26
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2506.20995) · [PDF](https://arxiv.org/pdf/2506.20995) · arXiv 2506.20995

#### [Deciphering GunType Hierarchy through Acoustic Analysis of Gunshot Recordings](https://arxiv.org/abs/2506.20609)

- **日期：** 2025-06-25
- **问题 / 中文简述：** 低信噪比；采用数据驱动方法，面向工业与机械声音解决低信噪比问题。
- **来源：** [论文主页](https://arxiv.org/abs/2506.20609) · [PDF](https://arxiv.org/pdf/2506.20609) · arXiv 2506.20609

#### [Audio-JEPA: Joint-Embedding Predictive Architecture for Audio Representation Learning](https://arxiv.org/abs/2507.02915)

- **日期：** 2025-06-25
- **问题 / 中文简述：** 通用检测与分类；采用自监督表征开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2507.02915) · [PDF](https://arxiv.org/pdf/2507.02915) · arXiv 2507.02915

#### [USAD Universal Speech and Audio Representation via Distillation](https://arxiv.org/abs/2506.18843)

- **日期：** 2025-06-23
- **问题 / 中文简述：** 轻量化部署；采用自监督表征，面向声音事件解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2506.18843) · [PDF](https://arxiv.org/pdf/2506.18843) · arXiv 2506.18843

#### [SHAMaNS: Sound Localization with Hybrid Alpha-Stable Spatial Measure and Neural Steerer](https://arxiv.org/abs/2506.18954)

- **日期：** 2025-06-23
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2506.18954) · [PDF](https://arxiv.org/pdf/2506.18954) · arXiv 2506.18954

#### [Blind Source Separation in Biomedical Signals Using Variational Methods](https://arxiv.org/abs/2506.18281)

- **日期：** 2025-06-23
- **问题 / 中文简述：** 定位与分离 · 轻量化部署；采用数据驱动方法，面向医疗与生理声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2506.18281) · [PDF](https://arxiv.org/pdf/2506.18281) · arXiv 2506.18281

#### [Acoustic evaluation of a neural network dedicated to the detection of animal vocalisations](https://arxiv.org/abs/2507.01974)

- **日期：** 2025-06-23
- **问题 / 中文简述：** 通用检测与分类；采用数据增强与生成开展生态与动物声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2507.01974) · [PDF](https://arxiv.org/pdf/2507.01974) · arXiv 2507.01974

#### [Episode-specific Fine-tuning for Metric-based Few-shot Learners with Optimization-based Training](https://arxiv.org/abs/2506.17499)

- **日期：** 2025-06-20
- **问题 / 中文简述：** 少样本；采用数据驱动方法，面向声音事件解决少样本问题。
- **来源：** [论文主页](https://arxiv.org/abs/2506.17499) · [PDF](https://arxiv.org/pdf/2506.17499) · arXiv 2506.17499

#### [Adaptive Control Attention Network for Underwater Acoustic Localization and Domain Adaptation](https://arxiv.org/abs/2506.17409)

- **日期：** 2025-06-20
- **问题 / 中文简述：** 跨域泛化 · 定位与分离；采用Transformer 表征，面向交通与水下声音解决跨域泛化问题。
- **来源：** [论文主页](https://arxiv.org/abs/2506.17409) · [PDF](https://arxiv.org/pdf/2506.17409) · arXiv 2506.17409

#### [Single-Microphone-Based Sound Source Localization for Mobile Robots in Reverberant Environments](https://arxiv.org/abs/2506.16173)

- **日期：** 2025-06-19
- **问题 / 中文简述：** 定位与分离 · 轻量化部署；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2506.16173) · [PDF](https://arxiv.org/pdf/2506.16173) · arXiv 2506.16173

#### [AeroGPT: Leveraging Large-Scale Audio Model for Aero-Engine Bearing Fault Diagnosis](https://arxiv.org/abs/2506.16225)

- **日期：** 2025-06-19
- **问题 / 中文简述：** 可解释与可靠性 · 轻量化部署；采用数据增强与生成，面向工业与机械声音解决可解释与可靠性问题。
- **来源：** [论文主页](https://arxiv.org/abs/2506.16225) · [PDF](https://arxiv.org/pdf/2506.16225) · arXiv 2506.16225

#### [Acoustic scattering AI for non-invasive object classifications: A case study on hair assessment](https://arxiv.org/abs/2506.14148)

- **日期：** 2025-06-17
- **问题 / 中文简述：** 多模态与基础模型；采用自监督表征，面向声音事件解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2506.14148) · [PDF](https://arxiv.org/pdf/2506.14148) · arXiv 2506.14148

#### [Stereo sound event localization and detection based on PSELDnet pretraining and BiMamba sequence modeling](https://arxiv.org/abs/2506.13455)

- **日期：** 2025-06-16
- **问题 / 中文简述：** 定位与分离；采用Transformer 表征，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2506.13455) · [PDF](https://arxiv.org/pdf/2506.13455) · arXiv 2506.13455

#### [Frequency Dynamic Convolutions for Sound Event Detection](https://arxiv.org/abs/2506.12785)

- **日期：** 2025-06-15
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2506.12785) · [PDF](https://arxiv.org/pdf/2506.12785) · arXiv 2506.12785

#### [SSLAM Enhancing Self-Supervised Models with Audio Mixtures for Polyphonic Soundscapes](https://arxiv.org/abs/2506.12222)

- **日期：** 2025-06-13
- **问题 / 中文简述：** 通用检测与分类；采用音频语言模型开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2506.12222) · [PDF](https://arxiv.org/pdf/2506.12222) · arXiv 2506.12222

#### [Abstract Sound Fusion with Unconditional Inversion Models](https://arxiv.org/abs/2506.11811)

- **日期：** 2025-06-13
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2506.11811) · [PDF](https://arxiv.org/pdf/2506.11811) · arXiv 2506.11811

#### [MUDAS: Mote-scale Unsupervised Domain Adaptation in Multi-label Sound Classification](https://arxiv.org/abs/2506.11331)

- **日期：** 2025-06-12
- **问题 / 中文简述：** 半/弱监督 · 跨域泛化 · 可解释与可靠性 · 轻量化部署；采用数据驱动方法，面向工业与机械声音解决半/弱监督问题。
- **来源：** [论文主页](https://arxiv.org/abs/2506.11331) · [PDF](https://arxiv.org/pdf/2506.11331) · arXiv 2506.11331

#### [Disentangling Dual-Encoder Masked Autoencoder for Respiratory Sound Classification](https://arxiv.org/abs/2506.10698)

- **日期：** 2025-06-12
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展医疗与生理声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2506.10698) · [PDF](https://arxiv.org/pdf/2506.10698) · arXiv 2506.10698

#### [Description and Discussion on DCASE 2025 Challenge Task 4 Spatial Semantic Segmentation of Sound Scenes](https://arxiv.org/abs/2506.10676)

- **日期：** 2025-06-12
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向环境与城市声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2506.10676) · [PDF](https://arxiv.org/pdf/2506.10676) · arXiv 2506.10676

#### [Tracking of Intermittent and Moving Speakers : Dataset and Metrics](https://arxiv.org/abs/2506.11145)

- **日期：** 2025-06-11
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向环境与城市声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2506.11145) · [PDF](https://arxiv.org/pdf/2506.11145) · arXiv 2506.11145

#### [FedMLAC: Mutual Learning Driven Heterogeneous Federated Audio Classification](https://arxiv.org/abs/2506.10207)

- **日期：** 2025-06-11
- **问题 / 中文简述：** 低信噪比 · 轻量化部署；采用数据驱动方法，面向声音事件解决低信噪比问题。
- **来源：** [论文主页](https://arxiv.org/abs/2506.10207) · [PDF](https://arxiv.org/pdf/2506.10207) · arXiv 2506.10207

#### [Description and Discussion on DCASE 2025 Challenge Task 2_ First-Shot Unsupervised Anomalous Sound Detection for Machine Condition Monitoring](https://arxiv.org/abs/2506.10097)

- **日期：** 2025-06-11
- **问题 / 中文简述：** 跨域泛化；采用数据驱动方法，面向工业与机械声音解决跨域泛化问题。
- **来源：** [论文主页](https://arxiv.org/abs/2506.10097) · [PDF](https://arxiv.org/pdf/2506.10097) · arXiv 2506.10097

#### [Domain Adaptation Method and Modality Gap Impact in Audio-Text Models for Prototypical Sound Classif](https://arxiv.org/abs/2506.04376)

- **日期：** 2025-06-04
- **问题 / 中文简述：** 跨域泛化 · 开放集/OOD；采用数据驱动方法，面向环境与城市声音解决跨域泛化问题。
- **来源：** [论文主页](https://arxiv.org/abs/2506.04376) · [PDF](https://arxiv.org/pdf/2506.04376) · arXiv 2506.04376

#### [Benchmarking Time-localized Explanations for Audio Classification Models](https://arxiv.org/abs/2506.04391)

- **日期：** 2025-06-04
- **问题 / 中文简述：** 可解释与可靠性；采用数据驱动方法，面向声音事件解决可解释与可靠性问题。
- **来源：** [论文主页](https://arxiv.org/abs/2506.04391) · [PDF](https://arxiv.org/pdf/2506.04391) · arXiv 2506.04391

#### [UltrasonicSpheres: Localized, Multi-Channel Sound Spheres Using Off-the-Shelf Speakers and Earables](https://arxiv.org/abs/2506.02715)

- **日期：** 2025-06-03
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向环境与城市声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2506.02715) · [PDF](https://arxiv.org/pdf/2506.02715) · arXiv 2506.02715

#### [CapSpeech Enabling Downstream Applications in Style-Captioned Text-to-Speech](https://arxiv.org/abs/2506.02863)

- **日期：** 2025-06-03
- **问题 / 中文简述：** 轻量化部署；采用数据增强与生成，面向工业与机械声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2506.02863) · [PDF](https://arxiv.org/pdf/2506.02863) · arXiv 2506.02863

#### [AuralNet: Hierarchical Attention-based 3D Binaural Localization of Overlapping Speakers](https://arxiv.org/abs/2506.02773)

- **日期：** 2025-06-03
- **问题 / 中文简述：** 低信噪比 · 定位与分离 · 轻量化部署；采用Transformer 表征，面向声音事件解决低信噪比问题。
- **来源：** [论文主页](https://arxiv.org/abs/2506.02773) · [PDF](https://arxiv.org/pdf/2506.02773) · arXiv 2506.02773

#### [Adaptive Differential Denoising for Respiratory Sounds Classification](https://arxiv.org/abs/2506.02505)

- **日期：** 2025-06-03
- **问题 / 中文简述：** 低信噪比；采用Transformer 表征，面向医疗与生理声音解决低信噪比问题。
- **来源：** [论文主页](https://arxiv.org/abs/2506.02505) · [PDF](https://arxiv.org/pdf/2506.02505) · arXiv 2506.02505

#### [Enhancing Speech Emotion Recognition with Graph-Based Multimodal Fusion and Prosodic Features for the Speech Emotion Recognition in Naturalistic Conditions Challenge at Interspeech 2025](https://arxiv.org/abs/2506.02088)

- **日期：** 2025-06-02
- **问题 / 中文简述：** 多模态与基础模型；采用Transformer 表征，面向声音事件解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2506.02088) · [PDF](https://arxiv.org/pdf/2506.02088) · arXiv 2506.02088

#### [Towards Fusion of Neural Audio Codec-based Representations with Spectral for Heart Murmur Classification via Bandit-based Cross-Attention Mechanism](https://arxiv.org/abs/2506.01148)

- **日期：** 2025-06-01
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展医疗与生理声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2506.01148) · [PDF](https://arxiv.org/pdf/2506.01148) · arXiv 2506.01148

#### [CLAP-ART- Automated Audio Captioning with Semantic-rich Audio Representation Tokenizer](https://arxiv.org/abs/2506.00800)

- **日期：** 2025-06-01
- **问题 / 中文简述：** 多模态与基础模型；采用音频语言模型，面向声音事件解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2506.00800) · [PDF](https://arxiv.org/pdf/2506.00800) · arXiv 2506.00800

#### [When Humans Growl and Birds Speak: High-Fidelity Voice Conversion from Human to Animal and Designed Sounds](https://arxiv.org/abs/2505.24336)

- **日期：** 2025-05-30
- **问题 / 中文简述：** 通用检测与分类；采用数据增强与生成开展生态与动物声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2505.24336) · [PDF](https://arxiv.org/pdf/2505.24336) · arXiv 2505.24336

#### [FeatureSense: Protecting Speaker Attributes in Always-On Audio Sensing System](https://arxiv.org/abs/2505.24115)

- **日期：** 2025-05-30
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2505.24115) · [PDF](https://arxiv.org/pdf/2505.24115) · arXiv 2505.24115

#### [ZeroSep: Separate Anything in Audio with Zero Training](https://arxiv.org/abs/2505.23625)

- **日期：** 2025-05-29
- **问题 / 中文简述：** 低信噪比 · 开放集/OOD · 定位与分离 · 多模态与基础模型；采用数据增强与生成，面向工业与机械声音解决低信噪比问题。
- **来源：** [论文主页](https://arxiv.org/abs/2505.23625) · [PDF](https://arxiv.org/pdf/2505.23625) · arXiv 2505.23625

#### [Spectrotemporal Modulation: Efficient and Interpretable Feature Representation for Classifying Speech, Music, and Environmental Sounds](https://arxiv.org/abs/2505.23509)

- **日期：** 2025-05-29
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向工业与机械声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2505.23509) · [PDF](https://arxiv.org/pdf/2505.23509) · arXiv 2505.23509

#### [Patient Domain Supervised Contrastive Learning for Lung Sound Classification Using Mobile Phone](https://arxiv.org/abs/2505.23132)

- **日期：** 2025-05-29
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展医疗与生理声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2505.23132) · [PDF](https://arxiv.org/pdf/2505.23132) · arXiv 2505.23132

#### [Patient-Aware Feature Alignment for Robust Lung Sound Classification:Cohesion-Separation and Global Alignment Losses](https://arxiv.org/abs/2505.23834)

- **日期：** 2025-05-28
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向医疗与生理声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2505.23834) · [PDF](https://arxiv.org/pdf/2505.23834) · arXiv 2505.23834

#### [Improving Respiratory Sound Classification with Architecture-Agnostic Knowledge Distillation from Ensembles](https://arxiv.org/abs/2505.22027)

- **日期：** 2025-05-28
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向医疗与生理声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2505.22027) · [PDF](https://arxiv.org/pdf/2505.22027) · arXiv 2505.22027

#### [AudioGenie: A Training-Free Multi-Agent Framework for Diverse Multimodality-to-Multiaudio Generation](https://arxiv.org/abs/2505.22053)

- **日期：** 2025-05-28
- **问题 / 中文简述：** 多模态与基础模型；采用层级与多任务学习，面向声音事件解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2505.22053) · [PDF](https://arxiv.org/pdf/2505.22053) · arXiv 2505.22053

#### [Text-Queried Audio Source Separation via Hierarchical Modeling](https://arxiv.org/abs/2505.21025)

- **日期：** 2025-05-27
- **问题 / 中文简述：** 定位与分离 · 轻量化部署；采用层级与多任务学习，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2505.21025) · [PDF](https://arxiv.org/pdf/2505.21025) · arXiv 2505.21025

#### [Hybrid Disagreement-Diversity Active Learning for Bioacoustic Sound Event Detection](https://arxiv.org/abs/2505.20956)

- **日期：** 2025-05-27
- **问题 / 中文简述：** 少样本 · 长尾与不平衡 · 轻量化部署；采用数据驱动方法，面向生态与动物声音解决少样本问题。
- **来源：** [论文主页](https://arxiv.org/abs/2505.20956) · [PDF](https://arxiv.org/pdf/2505.20956) · arXiv 2505.20956

#### [Foundation Model Hidden Representations for Heart Rate Estimation from Auscultation](https://arxiv.org/abs/2505.20745)

- **日期：** 2025-05-27
- **问题 / 中文简述：** 多模态与基础模型；采用音频语言模型，面向医疗与生理声音解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2505.20745) · [PDF](https://arxiv.org/pdf/2505.20745) · arXiv 2505.20745

#### [Efficient and Microphone-Fault-Tolerant 3D Sound Source Localization](https://arxiv.org/abs/2505.20961)

- **日期：** 2025-05-27
- **问题 / 中文简述：** 定位与分离 · 可解释与可靠性 · 轻量化部署；采用Transformer 表征，面向工业与机械声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2505.20961) · [PDF](https://arxiv.org/pdf/2505.20961) · arXiv 2505.20961

#### [Automated data curation for self-supervised learning in underwater acoustic analysis](https://arxiv.org/abs/2505.20066)

- **日期：** 2025-05-26
- **问题 / 中文简述：** 通用检测与分类；采用自监督表征开展工业与机械声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2505.20066) · [PDF](https://arxiv.org/pdf/2505.20066) · arXiv 2505.20066

#### [A Comprehensive Real-World Assessment of Audio Watermarking Algorithms: Will They Survive Neural Codecs?](https://arxiv.org/abs/2505.19663)

- **日期：** 2025-05-26
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向环境与城市声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2505.19663) · [PDF](https://arxiv.org/pdf/2505.19663) · arXiv 2505.19663

#### [Self-supervised learning method using multiple sampling strategies for general-purpose audio representation](https://arxiv.org/abs/2505.18984)

- **日期：** 2025-05-25
- **问题 / 中文简述：** 通用检测与分类；采用自监督表征开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2505.18984) · [PDF](https://arxiv.org/pdf/2505.18984) · arXiv 2505.18984

#### [EnvSDD: Benchmarking Environmental Sound Deepfake Detection](https://arxiv.org/abs/2505.19203)

- **日期：** 2025-05-25
- **问题 / 中文简述：** 多模态与基础模型；采用数据驱动方法，面向环境与城市声音解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2505.19203) · [PDF](https://arxiv.org/pdf/2505.19203) · arXiv 2505.19203

#### [Making deep neural networks work for medical audio: representation, compression and domain adaptation](https://arxiv.org/abs/2506.13970)

- **日期：** 2025-05-24
- **问题 / 中文简述：** 少样本 · 跨域泛化 · 轻量化部署；采用数据驱动方法，面向医疗与生理声音解决少样本问题。
- **来源：** [论文主页](https://arxiv.org/abs/2506.13970) · [PDF](https://arxiv.org/pdf/2506.13970) · arXiv 2506.13970

#### [CosyVoice 3: Towards In-the-wild Speech Generation via Scaling-up and Post-training](https://arxiv.org/abs/2505.17589)

- **日期：** 2025-05-23
- **问题 / 中文简述：** 开放集/OOD；采用音频语言模型，面向声音事件解决开放集/OOD问题。
- **来源：** [论文主页](https://arxiv.org/abs/2505.17589) · [PDF](https://arxiv.org/pdf/2505.17589) · arXiv 2505.17589

#### [X-ARES: A Comprehensive Framework for Assessing Audio Encoder Performance](https://arxiv.org/abs/2505.16369)

- **日期：** 2025-05-22
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2505.16369) · [PDF](https://arxiv.org/pdf/2505.16369) · arXiv 2505.16369

#### [Towards Pre-training an Effective Respiratory Audio Foundation Model](https://arxiv.org/abs/2505.15307)

- **日期：** 2025-05-21
- **问题 / 中文简述：** 多模态与基础模型；采用数据驱动方法，面向医疗与生理声音解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2505.15307) · [PDF](https://arxiv.org/pdf/2505.15307) · arXiv 2505.15307

#### [Discrete Audio Representations for Automated Audio Captioning](https://arxiv.org/abs/2505.14989)

- **日期：** 2025-05-21
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2505.14989) · [PDF](https://arxiv.org/pdf/2505.14989) · arXiv 2505.14989

#### [4,500 Seconds: Small Data Training Approaches for Deep UAV Audio Classification](https://arxiv.org/abs/2505.23782)

- **日期：** 2025-05-21
- **问题 / 中文简述：** 轻量化部署；采用Transformer 表征，面向交通与水下声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2505.23782) · [PDF](https://arxiv.org/pdf/2505.23782) · arXiv 2505.23782

#### [U-SAM An audio language Model for Unified Speech, Audio, and Music Understanding](https://arxiv.org/abs/2505.13880)

- **日期：** 2025-05-20
- **问题 / 中文简述：** 多模态与基础模型；采用音频语言模型，面向声音事件解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2505.13880) · [PDF](https://arxiv.org/pdf/2505.13880) · arXiv 2505.13880

#### [Teaching Audio-Aware Large Language Models What Does Not Hear: Mitigating Hallucinations through Synthesized Negative Samples](https://arxiv.org/abs/2505.14518)

- **日期：** 2025-05-20
- **问题 / 中文简述：** 可解释与可靠性 · 轻量化部署；采用音频语言模型，面向声音事件解决可解释与可靠性问题。
- **来源：** [论文主页](https://arxiv.org/abs/2505.14518) · [PDF](https://arxiv.org/pdf/2505.14518) · arXiv 2505.14518

#### [Large Language Models Implicitly Learn to See and Hear Just By Reading](https://arxiv.org/abs/2505.17091)

- **日期：** 2025-05-20
- **问题 / 中文简述：** 通用检测与分类；采用音频语言模型开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2505.17091) · [PDF](https://arxiv.org/pdf/2505.17091) · arXiv 2505.17091

#### [AquaSignal: An Integrated Framework for Robust Underwater Acoustic Analysis](https://arxiv.org/abs/2505.14285)

- **日期：** 2025-05-20
- **问题 / 中文简述：** 低信噪比 · 可解释与可靠性 · 轻量化部署；采用数据驱动方法，面向交通与水下声音解决低信噪比问题。
- **来源：** [论文主页](https://arxiv.org/abs/2505.14285) · [PDF](https://arxiv.org/pdf/2505.14285) · arXiv 2505.14285

#### [The Computation of Generalized Embeddings for Underwater Acoustic Target Recognition using Contrastive Learning](https://arxiv.org/abs/2505.12904)

- **日期：** 2025-05-19
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展工业与机械声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2505.12904) · [PDF](https://arxiv.org/pdf/2505.12904) · arXiv 2505.12904

#### [SounDiT: Geo-Contextual Soundscape-to-Landscape Generation](https://arxiv.org/abs/2505.12734)

- **日期：** 2025-05-19
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2505.12734) · [PDF](https://arxiv.org/pdf/2505.12734) · arXiv 2505.12734

#### [Revisiting SSL for sound event detection complementary fusion and adaptive post-processing](https://arxiv.org/abs/2505.11889)

- **日期：** 2025-05-17
- **问题 / 中文简述：** 通用检测与分类；采用自监督表征开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2505.11889) · [PDF](https://arxiv.org/pdf/2505.11889) · arXiv 2505.11889

#### [Seeing Sound, Hearing Sight: Uncovering Modality Bias and Conflict of AI models in Sound Localization](https://arxiv.org/abs/2505.11217)

- **日期：** 2025-05-16
- **问题 / 中文简述：** 定位与分离 · 多模态与基础模型；采用数据驱动方法，面向工业与机械声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2505.11217) · [PDF](https://arxiv.org/pdf/2505.11217) · arXiv 2505.11217

#### [Multi-Domain Audio Question Answering Benchmark Toward Acoustic Content Reasoning](https://arxiv.org/abs/2505.07365)

- **日期：** 2025-05-12
- **问题 / 中文简述：** 多模态与基础模型；采用音频语言模型，面向生态与动物声音解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2505.07365) · [PDF](https://arxiv.org/pdf/2505.07365) · arXiv 2505.07365

#### [Bridging Ears and Eyes: Analyzing Audio and Visual Large Language Models to Humans in Visible Sound Recognition and Reducing Their Sensory Gap via Cross-Modal Distillation](https://arxiv.org/abs/2505.06803)

- **日期：** 2025-05-11
- **问题 / 中文简述：** 多模态与基础模型 · 轻量化部署；采用音频语言模型，面向声音事件解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2505.06803) · [PDF](https://arxiv.org/pdf/2505.06803) · arXiv 2505.06803

#### [Hearing and Seeing Through CLIP: A Framework for Self-Supervised Sound Source Localization](https://arxiv.org/abs/2505.05343)

- **日期：** 2025-05-08
- **问题 / 中文简述：** 开放集/OOD · 定位与分离 · 多模态与基础模型 · 轻量化部署；采用音频语言模型，面向声音事件解决开放集/OOD问题。
- **来源：** [论文主页](https://arxiv.org/abs/2505.05343) · [PDF](https://arxiv.org/pdf/2505.05343) · arXiv 2505.05343

#### [FLAM- Frame-Wise Language-Audio Modeling](https://arxiv.org/abs/2505.05335)

- **日期：** 2025-05-08
- **问题 / 中文简述：** 开放集/OOD · 定位与分离 · 多模态与基础模型 · 轻量化部署；采用音频语言模型，面向声音事件解决开放集/OOD问题。
- **来源：** [论文主页](https://arxiv.org/abs/2505.05335) · [PDF](https://arxiv.org/pdf/2505.05335) · arXiv 2505.05335

#### [Tri-MTL: A Triple Multitask Learning Approach for Respiratory Disease Diagnosis](https://arxiv.org/abs/2505.06271)

- **日期：** 2025-05-06
- **问题 / 中文简述：** 轻量化部署；采用层级与多任务学习，面向医疗与生理声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2505.06271) · [PDF](https://arxiv.org/pdf/2505.06271) · arXiv 2505.06271

#### [Probing Audio-Generation Capabilities of Text-Based Language Models](https://arxiv.org/abs/2506.00003)

- **日期：** 2025-05-04
- **问题 / 中文简述：** 多模态与基础模型；采用音频语言模型，面向环境与城市声音解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2506.00003) · [PDF](https://arxiv.org/pdf/2506.00003) · arXiv 2506.00003

#### [Low-Complexity Acoustic Scene Classification with Device Information in the DCASE 2025 Challenge](https://arxiv.org/abs/2505.01747)

- **日期：** 2025-05-03
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2505.01747) · [PDF](https://arxiv.org/pdf/2505.01747) · arXiv 2505.01747

#### [ECOSoundSet: a finely annotated dataset for the automated acoustic identification of Orthoptera and Cicadidae in North, Central and temperate Western Europe](https://arxiv.org/abs/2504.20776)

- **日期：** 2025-04-29
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2504.20776) · [PDF](https://arxiv.org/pdf/2504.20776) · arXiv 2504.20776

#### [DiffusionRIR: Room Impulse Response Interpolation using Diffusion Models](https://arxiv.org/abs/2504.20625)

- **日期：** 2025-04-29
- **问题 / 中文简述：** 低信噪比 · 定位与分离；采用数据增强与生成，面向声音事件解决低信噪比问题。
- **来源：** [论文主页](https://arxiv.org/abs/2504.20625) · [PDF](https://arxiv.org/pdf/2504.20625) · arXiv 2504.20625

#### [Pediatric Asthma Detection with Googles HeAR Model: An AI-Driven Respiratory Sound Classifier](https://arxiv.org/abs/2504.20124)

- **日期：** 2025-04-28
- **问题 / 中文简述：** 少样本 · 多模态与基础模型 · 轻量化部署；采用数据驱动方法，面向医疗与生理声音解决少样本问题。
- **来源：** [论文主页](https://arxiv.org/abs/2504.20124) · [PDF](https://arxiv.org/pdf/2504.20124) · arXiv 2504.20124

#### [Unsupervised outlier detection to improve bird audio dataset labels](https://arxiv.org/abs/2504.18650)

- **日期：** 2025-04-25
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2504.18650) · [PDF](https://arxiv.org/pdf/2504.18650) · arXiv 2504.18650

#### [Assessing the Utility of Audio Foundation Models for Heart and Respiratory Sound Analysis](https://arxiv.org/abs/2504.18004)

- **日期：** 2025-04-25
- **问题 / 中文简述：** 低信噪比 · 多模态与基础模型；采用数据驱动方法，面向医疗与生理声音解决低信噪比问题。
- **来源：** [论文主页](https://arxiv.org/abs/2504.18004) · [PDF](https://arxiv.org/pdf/2504.18004) · arXiv 2504.18004

#### [Waveform-Logmel Audio Neural Networks for Respiratory Sound Classification](https://arxiv.org/abs/2504.17156)

- **日期：** 2025-04-24
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展医疗与生理声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2504.17156) · [PDF](https://arxiv.org/pdf/2504.17156) · arXiv 2504.17156

#### [STNet: Prediction of Underwater Sound Speed Profiles with An Advanced Semi-Transformer Neural Network](https://arxiv.org/abs/2504.17912)

- **日期：** 2025-04-24
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展交通与水下声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2504.17912) · [PDF](https://arxiv.org/pdf/2504.17912) · arXiv 2504.17912

#### [Improving Sound Source Localization with Joint Slot Attention on Image and Audio](https://arxiv.org/abs/2504.15118)

- **日期：** 2025-04-21
- **问题 / 中文简述：** 定位与分离；采用Transformer 表征，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2504.15118) · [PDF](https://arxiv.org/pdf/2504.15118) · arXiv 2504.15118

#### [Temporal Attention Pooling for Frequency Dynamic Convolution in Sound Event Detection](https://arxiv.org/abs/2504.12670)

- **日期：** 2025-04-17
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2504.12670) · [PDF](https://arxiv.org/pdf/2504.12670) · arXiv 2504.12670

#### [Can Masked Autoencoders Also Listen to Birds?](https://arxiv.org/abs/2504.12880)

- **日期：** 2025-04-17
- **问题 / 中文简述：** 少样本 · 轻量化部署；采用自监督表征，面向生态与动物声音解决少样本问题。
- **来源：** [论文主页](https://arxiv.org/abs/2504.12880) · [PDF](https://arxiv.org/pdf/2504.12880) · arXiv 2504.12880

#### [A Multi-task Learning Balanced Attention Convolutional Neural Network Model for Few-shot Underwater Acoustic Target Recognition](https://arxiv.org/abs/2504.13102)

- **日期：** 2025-04-17
- **问题 / 中文简述：** 少样本 · 轻量化部署；采用Transformer 表征，面向生态与动物声音解决少样本问题。
- **来源：** [论文主页](https://arxiv.org/abs/2504.13102) · [PDF](https://arxiv.org/pdf/2504.13102) · arXiv 2504.13102

#### [Progressive Rock Music Classification](https://arxiv.org/abs/2504.10821)

- **日期：** 2025-04-15
- **问题 / 中文简述：** 轻量化部署；采用Transformer 表征，面向工业与机械声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2504.10821) · [PDF](https://arxiv.org/pdf/2504.10821) · arXiv 2504.10821

#### [Reverberation-based Features for Sound Event Localization and Detection with Distance Estimation](https://arxiv.org/abs/2504.08644)

- **日期：** 2025-04-11
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2504.08644) · [PDF](https://arxiv.org/pdf/2504.08644) · arXiv 2504.08644

#### [Passive Underwater Acoustic Signal Separation based on Feature Decoupling Dual-path Network](https://arxiv.org/abs/2504.08371)

- **日期：** 2025-04-11
- **问题 / 中文简述：** 定位与分离；采用Transformer 表征，面向交通与水下声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2504.08371) · [PDF](https://arxiv.org/pdf/2504.08371) · arXiv 2504.08371

#### [Location-Oriented Sound Event Localization and Detection with Spatial Mapping and Regression Localiz](https://arxiv.org/abs/2504.08365)

- **日期：** 2025-04-11
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2504.08365) · [PDF](https://arxiv.org/pdf/2504.08365) · arXiv 2504.08365

#### [BowelRCNN: Region-based Convolutional Neural Network System for Bowel Sound Auscultation](https://arxiv.org/abs/2504.08659)

- **日期：** 2025-04-11
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2504.08659) · [PDF](https://arxiv.org/pdf/2504.08659) · arXiv 2504.08659

#### [Quantum-Inspired Genetic Algorithm for Robust Source Separation in Smart City Acoustics](https://arxiv.org/abs/2504.07345)

- **日期：** 2025-04-10
- **问题 / 中文简述：** 低信噪比 · 定位与分离 · 轻量化部署；采用数据驱动方法，面向环境与城市声音解决低信噪比问题。
- **来源：** [论文主页](https://arxiv.org/abs/2504.07345) · [PDF](https://arxiv.org/pdf/2504.07345) · arXiv 2504.07345

#### [Réduire le bruit grâce à la réalité augmentée sonore -- Auditory Concealer](https://arxiv.org/abs/2504.05847)

- **日期：** 2025-04-08
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2504.05847) · [PDF](https://arxiv.org/pdf/2504.05847) · arXiv 2504.05847

#### [Formula-Supervised Sound Event Detection Pre-Training Without Real Data](https://arxiv.org/abs/2504.04428)

- **日期：** 2025-04-06
- **问题 / 中文简述：** 通用检测与分类；采用数据增强与生成开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2504.04428) · [PDF](https://arxiv.org/pdf/2504.04428) · arXiv 2504.04428

#### [Mind the Prompt Prompting Strategies in Audio Generations for Improving Sound Classification](https://arxiv.org/abs/2504.03329)

- **日期：** 2025-04-04
- **问题 / 中文简述：** 轻量化部署；采用数据增强与生成，面向声音事件解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2504.03329) · [PDF](https://arxiv.org/pdf/2504.03329) · arXiv 2504.03329

#### [An Efficient GPU-based Implementation for Noise Robust Sound Source Localization](https://arxiv.org/abs/2504.03373)

- **日期：** 2025-04-04
- **问题 / 中文简述：** 低信噪比 · 定位与分离 · 轻量化部署；采用数据驱动方法，面向工业与机械声音解决低信噪比问题。
- **来源：** [论文主页](https://arxiv.org/abs/2504.03373) · [PDF](https://arxiv.org/pdf/2504.03373) · arXiv 2504.03373

#### [Generating Diverse Audio-Visual 360 Soundscapes for Sound Event Localization and Detection](https://arxiv.org/abs/2504.02988)

- **日期：** 2025-04-03
- **问题 / 中文简述：** 定位与分离；采用数据增强与生成，面向环境与城市声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2504.02988) · [PDF](https://arxiv.org/pdf/2504.02988) · arXiv 2504.02988

#### [Token pruning in audio transformers- Optimizing performance and decoding patch importance](https://arxiv.org/abs/2504.01690)

- **日期：** 2025-04-02
- **问题 / 中文简述：** 可解释与可靠性；采用自监督表征，面向声音事件解决可解释与可靠性问题。
- **来源：** [论文主页](https://arxiv.org/abs/2504.01690) · [PDF](https://arxiv.org/pdf/2504.01690) · arXiv 2504.01690

#### [Make Some Noise Towards LLM audio reasoning and generation using sound tokens](https://arxiv.org/abs/2503.22275)

- **日期：** 2025-03-28
- **问题 / 中文简述：** 多模态与基础模型；采用音频语言模型，面向声音事件解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2503.22275) · [PDF](https://arxiv.org/pdf/2503.22275) · arXiv 2503.22275

#### [Baseline Systems and Evaluation Metrics for Spatial Semantic Segmentation of Sound Scenes](https://arxiv.org/abs/2503.22088)

- **日期：** 2025-03-28
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2503.22088) · [PDF](https://arxiv.org/pdf/2503.22088) · arXiv 2503.22088

#### [Hierarchical Label Propagation: A Model-Size-Dependent Performance Booster for AudioSet Tagging](https://arxiv.org/abs/2503.21826)

- **日期：** 2025-03-26
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2503.21826) · [PDF](https://arxiv.org/pdf/2503.21826) · arXiv 2503.21826

#### [Benchmarking Machine Learning Methods for Distributed Acoustic Sensing](https://arxiv.org/abs/2503.20681)

- **日期：** 2025-03-26
- **问题 / 中文简述：** 可解释与可靠性；采用数据增强与生成，面向工业与机械声音解决可解释与可靠性问题。
- **来源：** [论文主页](https://arxiv.org/abs/2503.20681) · [PDF](https://arxiv.org/pdf/2503.20681) · arXiv 2503.20681

#### [Symbolic Audio Classification via Modal Decision Tree Learning](https://arxiv.org/abs/2503.17018)

- **日期：** 2025-03-21
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展医疗与生理声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2503.17018) · [PDF](https://arxiv.org/pdf/2503.17018) · arXiv 2503.17018

#### [Improving Acoustic Scene Classification with City Features](https://arxiv.org/abs/2503.16862)

- **日期：** 2025-03-21
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向环境与城市声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2503.16862) · [PDF](https://arxiv.org/pdf/2503.16862) · arXiv 2503.16862

#### [Solla: Towards a Speech-Oriented LLM That Hears Acoustic Context](https://arxiv.org/abs/2503.15338)

- **日期：** 2025-03-19
- **问题 / 中文简述：** 多模态与基础模型；采用音频语言模型，面向声音事件解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2503.15338) · [PDF](https://arxiv.org/pdf/2503.15338) · arXiv 2503.15338

#### [InsectSet459 an open dataset of insect sounds for bioacoustic machine learning](https://arxiv.org/abs/2503.15074)

- **日期：** 2025-03-19
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2503.15074) · [PDF](https://arxiv.org/pdf/2503.15074) · arXiv 2503.15074

#### [A Bird Song Detector for improving bird identification through Deep Learning- a case study from Donana](https://arxiv.org/abs/2503.15576)

- **日期：** 2025-03-19
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2503.15576) · [PDF](https://arxiv.org/pdf/2503.15576) · arXiv 2503.15576

#### [Neural Edge Histogram Descriptors for Underwater Acoustic Target Recognition](https://arxiv.org/abs/2503.13763)

- **日期：** 2025-03-17
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向交通与水下声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2503.13763) · [PDF](https://arxiv.org/pdf/2503.13763) · arXiv 2503.13763

#### [A General Close-loop Predictive Coding Framework for Auditory Working Memory](https://arxiv.org/abs/2503.12506)

- **日期：** 2025-03-16
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2503.12506) · [PDF](https://arxiv.org/pdf/2503.12506) · arXiv 2503.12506

#### [Spike Encoding for Environmental Sound: A Comparative Benchmark](https://arxiv.org/abs/2503.11206)

- **日期：** 2025-03-14
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向环境与城市声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2503.11206) · [PDF](https://arxiv.org/pdf/2503.11206) · arXiv 2503.11206

#### [Exploring Performance-Complexity Trade-Offs in Sound Event Detection Models](https://arxiv.org/abs/2503.11373)

- **日期：** 2025-03-14
- **问题 / 中文简述：** 轻量化部署；采用Transformer 表征，面向声音事件解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2503.11373) · [PDF](https://arxiv.org/pdf/2503.11373) · arXiv 2503.11373

#### [Creating a Good Teacher for Knowledge Distillation in Acoustic Scene Classification](https://arxiv.org/abs/2503.11363)

- **日期：** 2025-03-14
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向环境与城市声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2503.11363) · [PDF](https://arxiv.org/pdf/2503.11363) · arXiv 2503.11363

#### [Mellow a small audio language model for reasoning](https://arxiv.org/abs/2503.08540)

- **日期：** 2025-03-11
- **问题 / 中文简述：** 开放集/OOD · 多模态与基础模型 · 轻量化部署；采用音频语言模型，面向环境与城市声音解决开放集/OOD问题。
- **来源：** [论文主页](https://arxiv.org/abs/2503.08540) · [PDF](https://arxiv.org/pdf/2503.08540) · arXiv 2503.08540

#### [Boundary Regression for Leitmotif Detection in Music Audio](https://arxiv.org/abs/2503.07977)

- **日期：** 2025-03-11
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2503.07977) · [PDF](https://arxiv.org/pdf/2503.07977) · arXiv 2503.07977

#### [Infant Cry Detection Using Causal Temporal Representation](https://arxiv.org/abs/2503.06247)

- **日期：** 2025-03-08
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2503.06247) · [PDF](https://arxiv.org/pdf/2503.06247) · arXiv 2503.06247

#### [Robust Detection of Overlapping Bioacoustic Sound Events](https://arxiv.org/abs/2503.02389)

- **日期：** 2025-03-04
- **问题 / 中文简述：** 通用检测与分类；采用自监督表征开展生态与动物声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2503.02389) · [PDF](https://arxiv.org/pdf/2503.02389) · arXiv 2503.02389

#### [Aggregation Strategies for Efficient Annotation of Bioacoustic Sound Events Using Active Learning](https://arxiv.org/abs/2503.02422)

- **日期：** 2025-03-04
- **问题 / 中文简述：** 可解释与可靠性 · 轻量化部署；采用数据驱动方法，面向生态与动物声音解决可解释与可靠性问题。
- **来源：** [论文主页](https://arxiv.org/abs/2503.02422) · [PDF](https://arxiv.org/pdf/2503.02422) · arXiv 2503.02422

#### [CNN-based Robust Sound Source Localization with SRP-PHAT for the Extreme Edge](https://arxiv.org/abs/2503.02046)

- **日期：** 2025-03-03
- **问题 / 中文简述：** 定位与分离 · 轻量化部署；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2503.02046) · [PDF](https://arxiv.org/pdf/2503.02046) · arXiv 2503.02046

#### [Synthetic data enables context-aware bioacoustic sound event detection](https://arxiv.org/abs/2503.00296)

- **日期：** 2025-03-01
- **问题 / 中文简述：** 少样本 · 多模态与基础模型；采用Transformer 表征，面向生态与动物声音解决少样本问题。
- **来源：** [论文主页](https://arxiv.org/abs/2503.00296) · [PDF](https://arxiv.org/pdf/2503.00296) · arXiv 2503.00296

#### [JiTTER Jigsaw Temporal Transformer for Event Reconstruction for Self-Supervised Sound Event Detecti](https://arxiv.org/abs/2502.20857)

- **日期：** 2025-02-28
- **问题 / 中文简述：** 通用检测与分类；采用自监督表征开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2502.20857) · [PDF](https://arxiv.org/pdf/2502.20857) · arXiv 2502.20857

#### [DualSpec: Text-to-spatial-audio Generation via Dual-Spectrogram Guided Diffusion Model](https://arxiv.org/abs/2502.18952)

- **日期：** 2025-02-26
- **问题 / 中文简述：** 定位与分离；采用音频语言模型，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2502.18952) · [PDF](https://arxiv.org/pdf/2502.18952) · arXiv 2502.18952

#### [ENACT-Heart -- ENsemble-based Assessment Using CNN and Transformer on Heart Sounds](https://arxiv.org/abs/2502.16914)

- **日期：** 2025-02-24
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展医疗与生理声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2502.16914) · [PDF](https://arxiv.org/pdf/2502.16914) · arXiv 2502.16914

#### [voc2vec: A Foundation Model for Non-Verbal Vocalization](https://arxiv.org/abs/2502.16298)

- **日期：** 2025-02-22
- **问题 / 中文简述：** 多模态与基础模型 · 轻量化部署；采用数据驱动方法，面向声音事件解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2502.16298) · [PDF](https://arxiv.org/pdf/2502.16298) · arXiv 2502.16298

#### [Offload Rethinking by Cloud Assistance for Efficient Environmental Sound Recognition on LPWANs](https://arxiv.org/abs/2502.15285)

- **日期：** 2025-02-21
- **问题 / 中文简述：** 轻量化部署；采用Transformer 表征，面向环境与城市声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2502.15285) · [PDF](https://arxiv.org/pdf/2502.15285) · arXiv 2502.15285

#### [Audio signal interpolation using optimal transportation of spectrograms](https://arxiv.org/abs/2502.15430)

- **日期：** 2025-02-21
- **问题 / 中文简述：** 通用检测与分类；采用数据增强与生成开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2502.15430) · [PDF](https://arxiv.org/pdf/2502.15430) · arXiv 2502.15430

#### [Fundamental Survey on Neuromorphic Based Audio Classification](https://arxiv.org/abs/2502.15056)

- **日期：** 2025-02-20
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2502.15056) · [PDF](https://arxiv.org/pdf/2502.15056) · arXiv 2502.15056

#### [An Attention-Assisted AI Model for Real-Time Underwater Sound Speed Estimation Leveraging Remote Sensing Sea Surface Temperature Data](https://arxiv.org/abs/2502.12817)

- **日期：** 2025-02-18
- **问题 / 中文简述：** 多模态与基础模型 · 轻量化部署；采用Transformer 表征，面向交通与水下声音解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2502.12817) · [PDF](https://arxiv.org/pdf/2502.12817) · arXiv 2502.12817

#### [Masked Latent Prediction and Classification for Self-Supervised Audio Representation Learning](https://arxiv.org/abs/2502.12031)

- **日期：** 2025-02-17
- **问题 / 中文简述：** 通用检测与分类；采用自监督表征开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2502.12031) · [PDF](https://arxiv.org/pdf/2502.12031) · arXiv 2502.12031

#### [AudioSpa: Spatializing Sound Events with Text](https://arxiv.org/abs/2502.11219)

- **日期：** 2025-02-16
- **问题 / 中文简述：** 定位与分离 · 多模态与基础模型；采用音频语言模型，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2502.11219) · [PDF](https://arxiv.org/pdf/2502.11219) · arXiv 2502.11219

#### [Hyperdimensional Intelligent Sensing for Efficient Real-Time Audio Processing on Extreme Edge](https://arxiv.org/abs/2502.10718)

- **日期：** 2025-02-15
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向声音事件解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2502.10718) · [PDF](https://arxiv.org/pdf/2502.10718) · arXiv 2502.10718

#### [Quantum Approaches for Dysphonia Assessment in Small Speech Datasets](https://arxiv.org/abs/2502.08968)

- **日期：** 2025-02-13
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展医疗与生理声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2502.08968) · [PDF](https://arxiv.org/pdf/2502.08968) · arXiv 2502.08968

#### [Towards Understanding of Frequency Dependence on Sound Event Detection](https://arxiv.org/abs/2502.07208)

- **日期：** 2025-02-11
- **问题 / 中文简述：** 通用检测与分类；采用数据增强与生成开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2502.07208) · [PDF](https://arxiv.org/pdf/2502.07208) · arXiv 2502.07208

#### [Evaluation of Deep Audio Representations for Hearables](https://arxiv.org/abs/2502.06664)

- **日期：** 2025-02-10
- **问题 / 中文简述：** 多模态与基础模型；采用数据驱动方法，面向环境与城市声音解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2502.06664) · [PDF](https://arxiv.org/pdf/2502.06664) · arXiv 2502.06664

#### [Calibration of Multiple Asynchronous Microphone Arrays using Hybrid TDOA](https://arxiv.org/abs/2502.06195)

- **日期：** 2025-02-10
- **问题 / 中文简述：** 定位与分离 · 可解释与可靠性；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2502.06195) · [PDF](https://arxiv.org/pdf/2502.06195) · arXiv 2502.06195

#### [Large Language Model-based Nonnegative Matrix Factorization For Cardiorespiratory Sound Separation](https://arxiv.org/abs/2502.05757)

- **日期：** 2025-02-09
- **问题 / 中文简述：** 定位与分离；采用音频语言模型，面向医疗与生理声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2502.05757) · [PDF](https://arxiv.org/pdf/2502.05757) · arXiv 2502.05757

#### [ADIFF: Explaining audio difference using natural language](https://arxiv.org/abs/2502.04476)

- **日期：** 2025-02-06
- **问题 / 中文简述：** 多模态与基础模型 · 可解释与可靠性；采用音频语言模型，面向环境与城市声音解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2502.04476) · [PDF](https://arxiv.org/pdf/2502.04476) · arXiv 2502.04476

#### [Should Audio Front-ends be Adaptive? Comparing Learnable and Adaptive Front-ends](https://arxiv.org/abs/2502.03260)

- **日期：** 2025-02-05
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2502.03260) · [PDF](https://arxiv.org/pdf/2502.03260) · arXiv 2502.03260

#### [CycleGuardian: A Framework for Automatic RespiratorySound classification Based on Improved Deep clustering and Contrastive Learning](https://arxiv.org/abs/2502.00734)

- **日期：** 2025-02-02
- **问题 / 中文简述：** 轻量化部署；采用对比与原型学习，面向医疗与生理声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2502.00734) · [PDF](https://arxiv.org/pdf/2502.00734) · arXiv 2502.00734

#### [acoupi An Open-Source Python Framework for Deploying Bioacoustic AI Models on Edge Devices](https://arxiv.org/abs/2501.17841)

- **日期：** 2025-01-29
- **问题 / 中文简述：** 可解释与可靠性 · 轻量化部署；采用数据驱动方法，面向生态与动物声音解决可解释与可靠性问题。
- **来源：** [论文主页](https://arxiv.org/abs/2501.17841) · [PDF](https://arxiv.org/pdf/2501.17841) · arXiv 2501.17841

#### [Variational Bayesian Adaptive Learning of Deep Latent Variables for Acoustic Knowledge Transfer](https://arxiv.org/abs/2501.15496)

- **日期：** 2025-01-26
- **问题 / 中文简述：** 跨域泛化 · 轻量化部署；采用数据驱动方法，面向环境与城市声音解决跨域泛化问题。
- **来源：** [论文主页](https://arxiv.org/abs/2501.15496) · [PDF](https://arxiv.org/pdf/2501.15496) · arXiv 2501.15496

#### [The ICME 2025 Audio Encoder Capability Challenge](https://arxiv.org/abs/2501.15302)

- **日期：** 2025-01-25
- **问题 / 中文简述：** 通用检测与分类；采用层级与多任务学习开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2501.15302) · [PDF](https://arxiv.org/pdf/2501.15302) · arXiv 2501.15302

#### [Leveraging Spatial Cues from Cochlear Implant Microphones to Efficiently Enhance Speech Separation in Real-World Listening Scenes](https://arxiv.org/abs/2501.14610)

- **日期：** 2025-01-24
- **问题 / 中文简述：** 定位与分离 · 轻量化部署；采用数据驱动方法，面向环境与城市声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2501.14610) · [PDF](https://arxiv.org/pdf/2501.14610) · arXiv 2501.14610

#### [Exploring Finetuned Audio-LLM on Heart Murmur Features](https://arxiv.org/abs/2501.13884)

- **日期：** 2025-01-23
- **问题 / 中文简述：** 长尾与不平衡；采用音频语言模型，面向医疗与生理声音解决长尾与不平衡问题。
- **来源：** [论文主页](https://arxiv.org/abs/2501.13884) · [PDF](https://arxiv.org/pdf/2501.13884) · arXiv 2501.13884

#### [Water Flow Detection Device Based on Sound Data Analysis and Machine Learning to Detect Water Leakage](https://arxiv.org/abs/2501.11151)

- **日期：** 2025-01-19
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展工业与机械声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2501.11151) · [PDF](https://arxiv.org/pdf/2501.11151) · arXiv 2501.11151

#### [An Experimental Study on Joint Modeling for Sound Event Localization and Detection with Source Dista](https://arxiv.org/abs/2501.10755)

- **日期：** 2025-01-18
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2501.10755) · [PDF](https://arxiv.org/pdf/2501.10755) · arXiv 2501.10755

#### [Quantum-Enhanced Transformers for Robust Acoustic Scene Classification in IoT Environments](https://arxiv.org/abs/2501.09394)

- **日期：** 2025-01-16
- **问题 / 中文简述：** 少样本 · 低信噪比；采用Transformer 表征，面向工业与机械声音解决少样本问题。
- **来源：** [论文主页](https://arxiv.org/abs/2501.09394) · [PDF](https://arxiv.org/pdf/2501.09394) · arXiv 2501.09394

#### [LHGNN: Local-Higher Order Graph Neural Networks For Audio Classification and Tagging](https://arxiv.org/abs/2501.03464)

- **日期：** 2025-01-07
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2501.03464) · [PDF](https://arxiv.org/pdf/2501.03464) · arXiv 2501.03464

#### [Structural and Statistical Audio Texture Knowledge Distillation for Acoustic Classification](https://arxiv.org/abs/2501.01921)

- **日期：** 2025-01-03
- **问题 / 中文简述：** 轻量化部署；采用Transformer 表征，面向交通与水下声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2501.01921) · [PDF](https://arxiv.org/pdf/2501.01921) · arXiv 2501.01921

#### [Disentangling Hierarchical Features for Anomalous Sound Detection Under Domain Shift](https://arxiv.org/abs/2501.01604)

- **日期：** 2025-01-03
- **问题 / 中文简述：** 跨域泛化；采用层级与多任务学习，面向工业与机械声音解决跨域泛化问题。
- **来源：** [论文主页](https://arxiv.org/abs/2501.01604) · [PDF](https://arxiv.org/pdf/2501.01604) · arXiv 2501.01604

#### [Robust COVID-19 Detection from Cough Sounds using Deep Neural Decision Tree and Forest: A Comprehensive Cross-Datasets Evaluation](https://arxiv.org/abs/2501.01117)

- **日期：** 2025-01-02
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向医疗与生理声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2501.01117) · [PDF](https://arxiv.org/pdf/2501.01117) · arXiv 2501.01117

#### [OmniChat: Enhancing Spoken Dialogue Systems with Scalable Synthetic Data for Diverse Scenarios](https://arxiv.org/abs/2501.01384)

- **日期：** 2025-01-02
- **问题 / 中文简述：** 通用检测与分类；采用音频语言模型开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2501.01384) · [PDF](https://arxiv.org/pdf/2501.01384) · arXiv 2501.01384

#### [FAST: Fast Audio Spectrogram Transformer](https://arxiv.org/abs/2501.01104)

- **日期：** 2025-01-02
- **问题 / 中文简述：** 轻量化部署；采用Transformer 表征，面向声音事件解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2501.01104) · [PDF](https://arxiv.org/pdf/2501.01104) · arXiv 2501.01104

#### [The Search for Squawk Agile Modeling in Bioacoustics](https://arxiv.org/abs/2505.03071)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2505.03071) · [PDF](https://arxiv.org/pdf/2505.03071) · arXiv 2505.03071

#### [Spatial and Semantic Embedding Integration for Stereo Sound Event Localization and Detection in Regu](https://arxiv.org/abs/2507.04845)

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2507.04845) · [PDF](https://arxiv.org/pdf/2507.04845) · arXiv 2507.04845

#### [Sound separation and classification with object and semantic guidance](https://arxiv.org/abs/2509.15899)

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2509.15899) · [PDF](https://arxiv.org/pdf/2509.15899) · arXiv 2509.15899

#### [Sound event detection with audio-text models and heterogeneous temporal annotations](https://arxiv.org/abs/2508.20703)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2508.20703) · [PDF](https://arxiv.org/pdf/2508.20703) · arXiv 2508.20703

#### [Sex and age determination in European lobsters using AI-Enhanced bioacoustics](https://arxiv.org/abs/2511.16848)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2511.16848) · [PDF](https://arxiv.org/pdf/2511.16848) · arXiv 2511.16848

#### [Pseudo Strong Labels from Frame-Level Predictions for Weakly Supervised Sound Event Detection](https://arxiv.org/abs/2501.03740)

- **日期：** 日期待核验
- **问题 / 中文简述：** 半/弱监督；采用数据驱动方法，面向声音事件解决半/弱监督问题。
- **来源：** [论文主页](https://arxiv.org/abs/2501.03740) · [PDF](https://arxiv.org/pdf/2501.03740) · arXiv 2501.03740

#### [Predictive maintenance of electric motors using supervised learning models: A comparative analysis](https://arxiv.org/abs/2504.03670)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展工业与机械声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2504.03670) · [PDF](https://arxiv.org/pdf/2504.03670) · arXiv 2504.03670

#### [Integrating Spatial and Semantic Embeddings for Stereo Sound Event Localization in Videos](https://arxiv.org/abs/2509.06598)

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2509.06598) · [PDF](https://arxiv.org/pdf/2509.06598) · arXiv 2509.06598

#### [Improving Stereo 3D Sound Event Localization and Detection Perceptual Features, Stereo-specific Dat](https://arxiv.org/abs/2507.00874)

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2507.00874) · [PDF](https://arxiv.org/pdf/2507.00874) · arXiv 2507.00874

#### [Hidden assumptions of integer ratio analyses in bioacoustics and music](https://arxiv.org/abs/2502.04464)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2502.04464) · [PDF](https://arxiv.org/pdf/2502.04464) · arXiv 2502.04464

#### [Fully Few-shot Class-incremental Audio Classification Using Multi-level Embedding Extractor and Ridge Regression Classifier](https://arxiv.org/abs/2506.18406)

- **日期：** 日期待核验
- **问题 / 中文简述：** 少样本 · 持续学习；采用数据驱动方法，面向声音事件解决少样本问题。
- **来源：** [论文主页](https://arxiv.org/abs/2506.18406) · [PDF](https://arxiv.org/pdf/2506.18406) · arXiv 2506.18406

#### [First-of-its-kind AI model for bioacoustic detection using a lightweight associative memory Hopfield](https://arxiv.org/abs/2507.10642)

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向生态与动物声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2507.10642) · [PDF](https://arxiv.org/pdf/2507.10642) · arXiv 2507.10642

#### [Comparing Self-Supervised Learning Models Pre-Trained on Human Speech and Animal Vocalizations for B](https://arxiv.org/abs/2501.05987)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用自监督表征开展生态与动物声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2501.05987) · [PDF](https://arxiv.org/pdf/2501.05987) · arXiv 2501.05987

#### [Clustering and novel class recognition evaluating bioacoustic deep learning feature extractors](https://arxiv.org/abs/2504.06710)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2504.06710) · [PDF](https://arxiv.org/pdf/2504.06710) · arXiv 2504.06710

#### [CST-former Multidimensional Attention-based Transformer for Sound Event Localization and Detection](https://arxiv.org/abs/2504.12870)

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用Transformer 表征，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2504.12870) · [PDF](https://arxiv.org/pdf/2504.12870) · arXiv 2504.12870

</details>

<details>
<summary><strong>2024 年（57 篇）</strong></summary>

#### [WildDESED An LLM-Powered Dataset for Wild Domestic Environment Sound Event Detection System](https://arxiv.org/abs/2407.03656)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2407.03656) · [PDF](https://arxiv.org/pdf/2407.03656) · arXiv 2407.03656

#### [Vision Transformer Segmentation for Visual Bird Sound Denoising](https://arxiv.org/abs/2406.09167)

- **日期：** 日期待核验
- **问题 / 中文简述：** 低信噪比；采用Transformer 表征，面向生态与动物声音解决低信噪比问题。
- **来源：** [论文主页](https://arxiv.org/abs/2406.09167) · [PDF](https://arxiv.org/pdf/2406.09167) · arXiv 2406.09167

#### [UCIL An Unsupervised Class Incremental Learning Approach for Sound Event Detection](https://arxiv.org/abs/2407.03657)

- **日期：** 日期待核验
- **问题 / 中文简述：** 持续学习；采用数据驱动方法，面向声音事件解决持续学习问题。
- **来源：** [论文主页](https://arxiv.org/abs/2407.03657) · [PDF](https://arxiv.org/pdf/2407.03657) · arXiv 2407.03657

#### [The Sounds of Home A Speech-Removed Residential Audio Dataset for Sound Event Detection](https://arxiv.org/abs/2409.11262)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2409.11262) · [PDF](https://arxiv.org/pdf/2409.11262) · arXiv 2409.11262

#### [Synthio- Augmenting Small-Scale Audio Classification Datasets with Synthetic Data](https://arxiv.org/abs/2410.02056)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据增强与生成开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2410.02056) · [PDF](https://arxiv.org/pdf/2410.02056) · arXiv 2410.02056

#### [Spatial Scaper A Library to Simulate and Augment Soundscapes for Sound Event Localization and Detec](https://arxiv.org/abs/2401.12238)

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向环境与城市声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2401.12238) · [PDF](https://arxiv.org/pdf/2401.12238) · arXiv 2401.12238

#### [Sound event localization and classification using WASN in Outdoor Environment](https://arxiv.org/abs/2403.20130)

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2403.20130) · [PDF](https://arxiv.org/pdf/2403.20130) · arXiv 2403.20130

#### [Sound Event Detection and Localization with Distance Estimation](https://arxiv.org/abs/2403.11827)

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2403.11827) · [PDF](https://arxiv.org/pdf/2403.11827) · arXiv 2403.11827

#### [Sound Event Bounding Boxes](https://arxiv.org/abs/2406.04212)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2406.04212) · [PDF](https://arxiv.org/pdf/2406.04212) · arXiv 2406.04212

#### [Self Training and Ensembling Frequency Dependent Networks with Coarse Prediction Pooling and Sound E](https://arxiv.org/abs/2406.15725)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2406.15725) · [PDF](https://arxiv.org/pdf/2406.15725) · arXiv 2406.15725

#### [Scaling up masked audio encoder learning for general audio classification](https://arxiv.org/abs/2406.06992)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2406.06992) · [PDF](https://arxiv.org/pdf/2406.06992) · arXiv 2406.06992

#### [SOUND EVENT DETECTION BASED ON AUXILIARY DECODER AND MAXIMUM PROBABILITY AGGREGATION FOR DCASE CHALLENGE 2024 TASK 4](https://arxiv.org/abs/2406.12721)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2406.12721) · [PDF](https://arxiv.org/pdf/2406.12721) · arXiv 2406.12721

#### [SELD-Mamba Selective State-Space Model for Sound Event Localization and Detection with Source Dista](https://arxiv.org/abs/2408.05057)

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2408.05057) · [PDF](https://arxiv.org/pdf/2408.05057) · arXiv 2408.05057

#### [Real-Time Sound Event Localization and Detection Deployment Challenges on Edge Devices](https://arxiv.org/abs/2409.11700)

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离 · 轻量化部署；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2409.11700) · [PDF](https://arxiv.org/pdf/2409.11700) · arXiv 2409.11700

#### [Pushing the Limit of Sound Event Detection with Multi-Dilated Frequency Dynamic Convolution](https://arxiv.org/abs/2406.13312)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2406.13312) · [PDF](https://arxiv.org/pdf/2406.13312) · arXiv 2406.13312

#### [Prototype based Masked Audio Model for Self-Supervised Learning of Sound Event Detection](https://arxiv.org/abs/2409.17656)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用自监督表征开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2409.17656) · [PDF](https://arxiv.org/pdf/2409.17656) · arXiv 2409.17656

#### [PSELDNets Pre-trained Neural Networks on a Large-scale Synthetic Dataset for Sound Event Localizati](https://arxiv.org/abs/2411.06399)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据增强与生成开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2411.06399) · [PDF](https://arxiv.org/pdf/2411.06399) · arXiv 2411.06399

#### [Onset and offset weighted loss function for sound event detection](https://arxiv.org/abs/2403.13254)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2403.13254) · [PDF](https://arxiv.org/pdf/2403.13254) · arXiv 2403.13254

#### [Multitask frame-level learning for few-shot sound event detection](https://arxiv.org/abs/2403.11091)

- **日期：** 日期待核验
- **问题 / 中文简述：** 少样本；采用层级与多任务学习，面向声音事件解决少样本问题。
- **来源：** [论文主页](https://arxiv.org/abs/2403.11091) · [PDF](https://arxiv.org/pdf/2403.11091) · arXiv 2403.11091

#### [Multi-Iteration Multi-Stage Fine-Tuning of Transformers for Sound Event Detection with Heterogeneous](https://arxiv.org/abs/2407.12997)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2407.12997) · [PDF](https://arxiv.org/pdf/2407.12997) · arXiv 2407.12997

#### [Mind the Domain Gap a Systematic Analysis on Bioacoustic Sound Event Detection](https://arxiv.org/abs/2403.18638)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2403.18638) · [PDF](https://arxiv.org/pdf/2403.18638) · arXiv 2403.18638

#### [MVANet Multi-Stage Video Attention Network for Sound Event Localization and Detection with Source Distance Estimation](https://arxiv.org/abs/2411.14153)

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用Transformer 表征，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2411.14153) · [PDF](https://arxiv.org/pdf/2411.14153) · arXiv 2411.14153

#### [MTDA-HSED Mutual-Assistance Tuning and Dual-Branch Aggregating for Heterogeneous Sound Event Detection](https://arxiv.org/abs/2409.06196)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2409.06196) · [PDF](https://arxiv.org/pdf/2409.06196) · arXiv 2409.06196

#### [MICROPHONE CONVERSION MITIGATING DEVICE VARIABILITY IN SOUND EVENT CLASSIFICATION](https://arxiv.org/abs/2401.06913)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2401.06913) · [PDF](https://arxiv.org/pdf/2401.06913) · arXiv 2401.06913

#### [MFF-EINV2 Multi-scale Feature Fusion across Spectral-Spatial-Temporal Domains for Sound Event Localization and Detection](https://arxiv.org/abs/2406.08771)

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2406.08771) · [PDF](https://arxiv.org/pdf/2406.08771) · arXiv 2406.08771

#### [MAT-SED A Masked Audio Transformer with Masked-Reconstruction Based Pre-training for Sound Event De](https://arxiv.org/abs/2408.08673)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2408.08673) · [PDF](https://arxiv.org/pdf/2408.08673) · arXiv 2408.08673

#### [Leveraging Self-Supervised Audio Representations for Data-Efficient Acoustic Scene Classification](https://arxiv.org/abs/2408.14862)

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用自监督表征，面向环境与城市声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2408.14862) · [PDF](https://arxiv.org/pdf/2408.14862) · arXiv 2408.14862

#### [Leveraging Reverberation and Visual Depth Cues for Sound Event Localization and Detection with Dista](https://arxiv.org/abs/2410.22271)

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2410.22271) · [PDF](https://arxiv.org/pdf/2410.22271) · arXiv 2410.22271

#### [Leveraging LLM and Text-Queried Separation for Noise-Robust Sound Event Detection](https://arxiv.org/abs/2411.01174)

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2411.01174) · [PDF](https://arxiv.org/pdf/2411.01174) · arXiv 2411.01174

#### [Learning Multi-Target TDOA Features for Sound Event Localization and Detection](https://arxiv.org/abs/2408.17166)

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2408.17166) · [PDF](https://arxiv.org/pdf/2408.17166) · arXiv 2408.17166

#### [LEAD Dataset How Can Labels for Sound Event Detection Vary Depending on Annotators](https://arxiv.org/abs/2410.09778)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2410.09778) · [PDF](https://arxiv.org/pdf/2410.09778) · arXiv 2410.09778

#### [Improving Audio Spectrogram Transformers for Sound Event Detection Through Multi-Stage Training](https://arxiv.org/abs/2408.00791)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2408.00791) · [PDF](https://arxiv.org/pdf/2408.00791) · arXiv 2408.00791

#### [Impact of Noisy Labels on Sound Event Detection Deletion Errors Are More Detrimental Than Insertion](https://arxiv.org/abs/2408.14771)

- **日期：** 日期待核验
- **问题 / 中文简述：** 低信噪比；采用数据驱动方法，面向声音事件解决低信噪比问题。
- **来源：** [论文主页](https://arxiv.org/abs/2408.14771) · [PDF](https://arxiv.org/pdf/2408.14771) · arXiv 2408.14771

#### [Generative AI-based data augmentation for improved bioacoustic classification in noisy environments](https://arxiv.org/abs/2412.01530)

- **日期：** 日期待核验
- **问题 / 中文简述：** 低信噪比；采用数据增强与生成，面向生态与动物声音解决低信噪比问题。
- **来源：** [论文主页](https://arxiv.org/abs/2412.01530) · [PDF](https://arxiv.org/pdf/2412.01530) · arXiv 2412.01530

#### [Full-frequency dynamic convolution a physical frequency-dependent convolution for sound event detec](https://arxiv.org/abs/2401.04976)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2401.04976) · [PDF](https://arxiv.org/pdf/2401.04976) · arXiv 2401.04976

#### [From Weak to Strong Sound Event Labels using Adaptive Change-Point Detection and Active Learning](https://arxiv.org/abs/2403.08525)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2403.08525) · [PDF](https://arxiv.org/pdf/2403.08525) · arXiv 2403.08525

#### [Frequency-aware convolution for sound event detection](https://arxiv.org/abs/2403.13252)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2403.13252) · [PDF](https://arxiv.org/pdf/2403.13252) · arXiv 2403.13252

#### [Fine-Grained Engine Fault Sound Event Detection Using Multimodal Signals](https://arxiv.org/abs/2403.11037)

- **日期：** 日期待核验
- **问题 / 中文简述：** 多模态与基础模型；采用数据驱动方法，面向工业与机械声音解决多模态与基础模型问题。
- **来源：** [论文主页](https://arxiv.org/abs/2403.11037) · [PDF](https://arxiv.org/pdf/2403.11037) · arXiv 2403.11037

#### [FEW-SHOT BIOACOUSTIC EVENT DETECTION WITH FRAME-LEVEL EMBEDDING LEARNING SYSTEM](https://arxiv.org/abs/2407.10182)

- **日期：** 日期待核验
- **问题 / 中文简述：** 少样本；采用数据驱动方法，面向生态与动物声音解决少样本问题。
- **来源：** [论文主页](https://arxiv.org/abs/2407.10182) · [PDF](https://arxiv.org/pdf/2407.10182) · arXiv 2407.10182

#### [Exploring Text-Queried Sound Event Detection with Audio Source Separation](https://arxiv.org/abs/2409.13292)

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2409.13292) · [PDF](https://arxiv.org/pdf/2409.13292) · arXiv 2409.13292

#### [Exploring Audio-Visual Information Fusion for Sound Event Localization and Detection In Low-Resource](https://arxiv.org/abs/2406.15160)

- **日期：** 日期待核验
- **问题 / 中文简述：** 少样本 · 定位与分离；采用数据驱动方法，面向声音事件解决少样本问题。
- **来源：** [论文主页](https://arxiv.org/abs/2406.15160) · [PDF](https://arxiv.org/pdf/2406.15160) · arXiv 2406.15160

#### [Energy Consumption Trends in Sound Event Detection Systems](https://arxiv.org/abs/2409.08763)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2409.08763) · [PDF](https://arxiv.org/pdf/2409.08763) · arXiv 2409.08763

#### [Effective Pre-Training of Audio Transformers for Sound Event Detection](https://arxiv.org/abs/2409.09546)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2409.09546) · [PDF](https://arxiv.org/pdf/2409.09546) · arXiv 2409.09546

#### [ENHANCED SOUND EVENT LOCALIZATION AND DETECTION IN REAL 360 AUDIO-VISUAL SOUNDSCAPES](https://arxiv.org/abs/2401.17129)

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向环境与城市声音解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2401.17129) · [PDF](https://arxiv.org/pdf/2401.17129) · arXiv 2401.17129

#### [Domain-Invariant Representation Learning of Bird Sounds](https://arxiv.org/abs/2409.08589)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2409.08589) · [PDF](https://arxiv.org/pdf/2409.08589) · arXiv 2409.08589

#### [Diversifying and Expanding Frequency-Adaptive Convolution Kernels for Sound Event Detection](https://arxiv.org/abs/2406.05341)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2406.05341) · [PDF](https://arxiv.org/pdf/2406.05341) · arXiv 2406.05341

#### [Description on ieee icme 2024 grand challenge: Semi-supervised acoustic scene classification under domain shift](https://arxiv.org/abs/2402.02694)

- **日期：** 日期待核验
- **问题 / 中文简述：** 半/弱监督 · 跨域泛化；采用数据驱动方法，面向环境与城市声音解决半/弱监督问题。
- **来源：** [论文主页](https://arxiv.org/abs/2402.02694) · [PDF](https://arxiv.org/pdf/2402.02694) · arXiv 2402.02694

#### [DUAL KNOWLEDGE DISTILLATION FOR EFFICIENT SOUND EVENT DETECTION](https://arxiv.org/abs/2402.02781)

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向声音事件解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2402.02781) · [PDF](https://arxiv.org/pdf/2402.02781) · arXiv 2402.02781

#### [DOA-Aware Audio-Visual Self-Supervised Learning for Sound Event Localization and Detection](https://arxiv.org/abs/2410.22803)

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用自监督表征，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2410.22803) · [PDF](https://arxiv.org/pdf/2410.22803) · arXiv 2410.22803

#### [DG-SED Domain Generalization for Sound Event Detection with Heterogeneous Training Data](https://arxiv.org/abs/2407.03654)

- **日期：** 日期待核验
- **问题 / 中文简述：** 跨域泛化；采用数据驱动方法，面向声音事件解决跨域泛化问题。
- **来源：** [论文主页](https://arxiv.org/abs/2407.03654) · [PDF](https://arxiv.org/pdf/2407.03654) · arXiv 2407.03654

#### [DATA EFFICIENT ACOUSTIC SCENE CLASSIFICATION USING TEACHER-INFORMED CONFUSING CLASS INSTRUCTION](https://arxiv.org/abs/2409.11964)

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向环境与城市声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2409.11964) · [PDF](https://arxiv.org/pdf/2409.11964) · arXiv 2409.11964

#### [Contrastive Loss Based Frame-wise Feature disentanglement for Polyphonic Sound Event Detection](https://arxiv.org/abs/2401.05850)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用对比与原型学习开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2401.05850) · [PDF](https://arxiv.org/pdf/2401.05850) · arXiv 2401.05850

#### [Class-Incremental Learning for Sound Event Localization and Detection](https://arxiv.org/abs/2411.12830)

- **日期：** 日期待核验
- **问题 / 中文简述：** 持续学习 · 定位与分离；采用数据驱动方法，面向声音事件解决持续学习问题。
- **来源：** [论文主页](https://arxiv.org/abs/2411.12830) · [PDF](https://arxiv.org/pdf/2411.12830) · arXiv 2411.12830

#### [AudioProtoPNet An interpretable deep learning model for bird sound classification](https://arxiv.org/abs/2404.10420)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2404.10420) · [PDF](https://arxiv.org/pdf/2404.10420) · arXiv 2404.10420

#### [Angular Distance Distribution Loss for Audio Classification](https://arxiv.org/abs/2411.00153)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2411.00153) · [PDF](https://arxiv.org/pdf/2411.00153) · arXiv 2411.00153

#### [A Sound Description Exploring Prompt Templates and Class Descriptions to Enhance Zero-Shot Audio Classification](https://arxiv.org/abs/2409.13676)

- **日期：** 日期待核验
- **问题 / 中文简述：** 开放集/OOD；采用数据驱动方法，面向声音事件解决开放集/OOD问题。
- **来源：** [论文主页](https://arxiv.org/abs/2409.13676) · [PDF](https://arxiv.org/pdf/2409.13676) · arXiv 2409.13676

#### [6DoF SELD Sound Event Localization and Detection Using Microphones and Motion Tracking Sensors on s](https://arxiv.org/abs/2403.01670)

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2403.01670) · [PDF](https://arxiv.org/pdf/2403.01670) · arXiv 2403.01670

</details>

<details>
<summary><strong>2023 年（41 篇）</strong></summary>

#### [w2v-SELD A Sound Event Localization and Detection Framework for Self-Supervised Spatial Audio Pre-TRAINING](https://arxiv.org/abs/2312.06907)

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用自监督表征，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2312.06907) · [PDF](https://arxiv.org/pdf/2312.06907) · arXiv 2312.06907

#### [ZERO- AND FEW-SHOT SOUND EVENT LOCALIZATION AND DETECTION](https://arxiv.org/abs/2309.09223)

- **日期：** 日期待核验
- **问题 / 中文简述：** 少样本 · 定位与分离；采用数据驱动方法，面向声音事件解决少样本问题。
- **来源：** [论文主页](https://arxiv.org/abs/2309.09223) · [PDF](https://arxiv.org/pdf/2309.09223) · arXiv 2309.09223

#### [Two vs. Four-Channel Sound Event Localization and Detection](https://arxiv.org/abs/2309.13343)

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2309.13343) · [PDF](https://arxiv.org/pdf/2309.13343) · arXiv 2309.13343

#### [Training sound event detection with soft labels from crowdsourced annotations](https://arxiv.org/abs/2302.14572)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2302.14572) · [PDF](https://arxiv.org/pdf/2302.14572) · arXiv 2302.14572

#### [Training one model to detect heart and lung sound events from single point auscultations](https://arxiv.org/abs/2301.06078)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展医疗与生理声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2301.06078) · [PDF](https://arxiv.org/pdf/2301.06078) · arXiv 2301.06078

#### [SwG-former A Sliding-Window Graph Convolutional Network for Simultaneous Spatial-Temporal INFORMATION EXTRACTION IN SOUND EVENT LOCALIZATION AND DETECTION](https://arxiv.org/abs/2310.14016)

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2310.14016) · [PDF](https://arxiv.org/pdf/2310.14016) · arXiv 2310.14016

#### [Semi-supervsied Learning-based Sound Event Detection using Freuqency Dynamic Convolution with Large](https://arxiv.org/abs/2306.06461)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2306.06461) · [PDF](https://arxiv.org/pdf/2306.06461) · arXiv 2306.06461

#### [Selective-Memory Meta-Learning with Environment Representations for Sound Event Localization and Det](https://arxiv.org/abs/2312.16422)

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2312.16422) · [PDF](https://arxiv.org/pdf/2312.16422) · arXiv 2312.16422

#### [STARSS23- An Audio-Visual Dataset of Spatial Recordings of Real Scenes with Spatiotemporal Annotations of Sound Events](https://arxiv.org/abs/2306.09126)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2306.09126) · [PDF](https://arxiv.org/pdf/2306.09126) · arXiv 2306.09126

#### [SEMI-SUPERVISED SOUND EVENT DETECTION WITH LOCAL AND GLOBAL CONSISTENCY REGULARIZATION](https://arxiv.org/abs/2309.08355)

- **日期：** 日期待核验
- **问题 / 中文简述：** 半/弱监督；采用数据驱动方法，面向声音事件解决半/弱监督问题。
- **来源：** [论文主页](https://arxiv.org/abs/2309.08355) · [PDF](https://arxiv.org/pdf/2309.08355) · arXiv 2309.08355

#### [REGULARIZED CONTRASTIVE PRE-TRAINING FOR FEW-SHOT BIOACOUSTIC SOUND DETECTION](https://arxiv.org/abs/2309.08971)

- **日期：** 日期待核验
- **问题 / 中文简述：** 少样本；采用对比与原型学习，面向生态与动物声音解决少样本问题。
- **来源：** [论文主页](https://arxiv.org/abs/2309.08971) · [PDF](https://arxiv.org/pdf/2309.08971) · arXiv 2309.08971

#### [Pretraining Representations for Bioacoustic Few-Shot Detection Using Supervised Contrastive Learning](https://arxiv.org/abs/2309.00878)

- **日期：** 日期待核验
- **问题 / 中文简述：** 少样本；采用对比与原型学习，面向生态与动物声音解决少样本问题。
- **来源：** [论文主页](https://arxiv.org/abs/2309.00878) · [PDF](https://arxiv.org/pdf/2309.00878) · arXiv 2309.00878

#### [Post-Processing Independent Evaluation of Sound Event Detection Systems](https://arxiv.org/abs/2306.15440)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2306.15440) · [PDF](https://arxiv.org/pdf/2306.15440) · arXiv 2306.15440

#### [Performance and energy balance a comprehensive study of state-of-the-art sound event detection syst](https://arxiv.org/abs/2310.03455)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2310.03455) · [PDF](https://arxiv.org/pdf/2310.03455) · arXiv 2310.03455

#### [Online Active Learning For Sound Event Detection](https://arxiv.org/abs/2309.14460)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2309.14460) · [PDF](https://arxiv.org/pdf/2309.14460) · arXiv 2309.14460

#### [Multi-dimensional frequency dynamic convolution with confident mean teacher for sound event detectio](https://arxiv.org/abs/2302.09256)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2302.09256) · [PDF](https://arxiv.org/pdf/2302.09256) · arXiv 2302.09256

#### [Multi-Label Open-Set Audio Classification](https://arxiv.org/abs/2310.13759)

- **日期：** 日期待核验
- **问题 / 中文简述：** 开放集/OOD；采用数据驱动方法，面向声音事件解决开放集/OOD问题。
- **来源：** [论文主页](https://arxiv.org/abs/2310.13759) · [PDF](https://arxiv.org/pdf/2310.13759) · arXiv 2310.13759

#### [META-SELD Meta-Learning for Fast Adaptation to the new environment in Sound Event Localization and](https://arxiv.org/abs/2308.08847)

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2308.08847) · [PDF](https://arxiv.org/pdf/2308.08847) · arXiv 2308.08847

#### [Leveraging Language Model Capabilities for Sound Event Detection](https://arxiv.org/abs/2308.11530)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用音频语言模型开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2308.11530) · [PDF](https://arxiv.org/pdf/2308.11530) · arXiv 2308.11530

#### [Leveraging Geometrical Acoustic Simulations of Spatial Room Impulse Responses for Improved Sound Eve](https://arxiv.org/abs/2309.03337)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2309.03337) · [PDF](https://arxiv.org/pdf/2309.03337) · arXiv 2309.03337

#### [Leveraging Audio-Tagging Assisted Sound Event Detection using Weakified Strong Labels and Frequency](https://arxiv.org/abs/2304.12688)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2304.12688) · [PDF](https://arxiv.org/pdf/2304.12688) · arXiv 2304.12688

#### [Killing Two Birds with One Stone Can an Audio Captioning System Also Be Used for Audio-Text Retrieval](https://arxiv.org/abs/2308.15090)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2308.15090) · [PDF](https://arxiv.org/pdf/2308.15090) · arXiv 2308.15090

#### [Interactive Dual-Conformer with Scene-Inspired Mask for Soft Sound Event Detection](https://arxiv.org/abs/2311.14068)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2311.14068) · [PDF](https://arxiv.org/pdf/2311.14068) · arXiv 2311.14068

#### [Incremental Learning of Acoustic Scenes and Sound Events](https://arxiv.org/abs/2302.14815)

- **日期：** 日期待核验
- **问题 / 中文简述：** 持续学习；采用数据驱动方法，面向环境与城市声音解决持续学习问题。
- **来源：** [论文主页](https://arxiv.org/abs/2302.14815) · [PDF](https://arxiv.org/pdf/2302.14815) · arXiv 2302.14815

#### [Improving Weakly Supervised Sound Event Detection with Causal Intervention](https://arxiv.org/abs/2303.05678)

- **日期：** 日期待核验
- **问题 / 中文简述：** 半/弱监督；采用数据驱动方法，面向声音事件解决半/弱监督问题。
- **来源：** [论文主页](https://arxiv.org/abs/2303.05678) · [PDF](https://arxiv.org/pdf/2303.05678) · arXiv 2303.05678

#### [Frequency & Channel Attention for Computationally Efficient Sound Event Detection](https://arxiv.org/abs/2306.11277)

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用Transformer 表征，面向声音事件解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2306.11277) · [PDF](https://arxiv.org/pdf/2306.11277) · arXiv 2306.11277

#### [Frame Pairwise Distance Loss for Weakly-supervised Sound Event Detection](https://arxiv.org/abs/2309.11783)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2309.11783) · [PDF](https://arxiv.org/pdf/2309.11783) · arXiv 2309.11783

#### [FUSION OF AUDIO AND VISUAL EMBEDDINGS FOR SOUND EVENT LOCALIZATION AND DETECTION](https://arxiv.org/abs/2312.09034)

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2312.09034) · [PDF](https://arxiv.org/pdf/2312.09034) · arXiv 2312.09034

#### [FINE-TUNE THE PRETRAINED ATST MODEL FOR SOUND EVENT DETECTION](https://arxiv.org/abs/2309.08153)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2309.08153) · [PDF](https://arxiv.org/pdf/2309.08153) · arXiv 2309.08153

#### [Enhance Temporal Relations in Audio Captioning with Sound Event Detection](https://arxiv.org/abs/2306.01533)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2306.01533) · [PDF](https://arxiv.org/pdf/2306.01533) · arXiv 2306.01533

#### [Dynamic Kernel Convolution Network with Scene-dedicate Training for Sound Event Localization and Det](https://arxiv.org/abs/2307.08239)

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2307.08239) · [PDF](https://arxiv.org/pdf/2307.08239) · arXiv 2307.08239

#### [Divided spectro-temporal attention for sound event localization and detection in real scenes for DCA](https://arxiv.org/abs/2306.02591)

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用Transformer 表征，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2306.02591) · [PDF](https://arxiv.org/pdf/2306.02591) · arXiv 2306.02591

#### [DiffSED Sound Event Detection with Denoising Diffusion](https://arxiv.org/abs/2308.07293)

- **日期：** 日期待核验
- **问题 / 中文简述：** 低信噪比；采用数据增强与生成，面向声音事件解决低信噪比问题。
- **来源：** [论文主页](https://arxiv.org/abs/2308.07293) · [PDF](https://arxiv.org/pdf/2308.07293) · arXiv 2308.07293

#### [Channel-Spatial-Based Few-Shot Bird Sound Event Detection](https://arxiv.org/abs/2306.10499)

- **日期：** 日期待核验
- **问题 / 中文简述：** 少样本；采用数据驱动方法，面向生态与动物声音解决少样本问题。
- **来源：** [论文主页](https://arxiv.org/abs/2306.10499) · [PDF](https://arxiv.org/pdf/2306.10499) · arXiv 2306.10499

#### [CST-FORMER TRANSFORMER WITH CHANNEL-SPECTRO-TEMPORAL ATTENTION FOR SOUND EVENT LOCALIZATION AND DETECTION](https://arxiv.org/abs/2312.12821)

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用Transformer 表征，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2312.12821) · [PDF](https://arxiv.org/pdf/2312.12821) · arXiv 2312.12821

#### [BRINGING THE DISCUSSION OF MINIMA SHARPNESS TO THE AUDIO DOMAIN- A FILTER-NORMALISED EVALUATION FOR ACOUSTIC SCENE CLASSIFICATION](https://arxiv.org/abs/2309.16369)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2309.16369) · [PDF](https://arxiv.org/pdf/2309.16369) · arXiv 2309.16369

#### [Auditory Neural Response Inspired Sound Event Detection Based on Spectro-Temporal Receptive Field](https://arxiv.org/abs/2306.11427)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2306.11427) · [PDF](https://arxiv.org/pdf/2306.11427) · arXiv 2306.11427

#### [AST-SED An Effective Sound Event Detection Method Based on Audio Spectrogram Transformer](https://arxiv.org/abs/2303.03689)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2303.03689) · [PDF](https://arxiv.org/pdf/2303.03689) · arXiv 2303.03689

#### [AD-YOLO You Look Only Once in Training Multiple Sound Event Localization and Detection](https://arxiv.org/abs/2303.15703)

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2303.15703) · [PDF](https://arxiv.org/pdf/2303.15703) · arXiv 2303.15703

#### [A dataset for Audio-Visual Sound Event Detection in Movies](https://arxiv.org/abs/2302.07315)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2302.07315) · [PDF](https://arxiv.org/pdf/2302.07315) · arXiv 2302.07315

#### [A Multi-Task Learning Framework for Sound Event Detection using High-level Acoustic Characteristics](https://arxiv.org/abs/2305.10729)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用层级与多任务学习开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2305.10729) · [PDF](https://arxiv.org/pdf/2305.10729) · arXiv 2305.10729

</details>

<details>
<summary><strong>2022 年（10 篇）</strong></summary>

#### [Sound Event Localization and Detection for Real Spatial Sound Scenes Event-Independent Network and Data Augmentation Chains](https://arxiv.org/abs/2209.01802)

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据增强与生成，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2209.01802) · [PDF](https://arxiv.org/pdf/2209.01802) · arXiv 2209.01802

#### [Segment-Level Metric Learning for Few-Shot Bioacoustic Event Detection](https://arxiv.org/abs/2207.07773)

- **日期：** 日期待核验
- **问题 / 中文简述：** 少样本；采用对比与原型学习，面向生态与动物声音解决少样本问题。
- **来源：** [论文主页](https://arxiv.org/abs/2207.07773) · [PDF](https://arxiv.org/pdf/2207.07773) · arXiv 2207.07773

#### [STARSS22 A Dataset of Spatial Recordings of Real Scenes with Spatiotemporal Annotations of Sound Events](https://arxiv.org/abs/2206.01948)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2206.01948) · [PDF](https://arxiv.org/pdf/2206.01948) · arXiv 2206.01948

#### [Polyphonic Sound Event Detection for Highly Dense Birdsong Scenes](https://arxiv.org/abs/2207.06349)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2207.06349) · [PDF](https://arxiv.org/pdf/2207.06349) · arXiv 2207.06349

#### [Improving the environmental perception of autonomous vehicles using deep learning-based audio classification](https://arxiv.org/abs/2209.04075)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展交通与水下声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2209.04075) · [PDF](https://arxiv.org/pdf/2209.04075) · arXiv 2209.04075

#### [Impact of Temporal Resolution on Convolutional Recurrent Networks for Audio Tagging and Sound Event Detection](https://arxiv.org/abs/2209.12843)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2209.12843) · [PDF](https://arxiv.org/pdf/2209.12843) · arXiv 2209.12843

#### [Frequency Dynamic Convolution Frequency-Adaptive Pattern Recognition for Sound Event Detection](https://arxiv.org/abs/2203.15296)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2203.15296) · [PDF](https://arxiv.org/pdf/2203.15296) · arXiv 2203.15296

#### [CoLoC Conditioned Localizer and Classifier for Sound Event Localization and Detection](https://arxiv.org/abs/2210.13932)

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2210.13932) · [PDF](https://arxiv.org/pdf/2210.13932) · arXiv 2210.13932

#### [BirdSoundsDenoising Deep Visual Audio Denoising for Bird Sounds](https://arxiv.org/abs/2210.10196)

- **日期：** 日期待核验
- **问题 / 中文简述：** 低信噪比；采用数据驱动方法，面向生态与动物声音解决低信噪比问题。
- **来源：** [论文主页](https://arxiv.org/abs/2210.10196) · [PDF](https://arxiv.org/pdf/2210.10196) · arXiv 2210.10196

#### [A passive similarity based CNN filter pruning for efficient acoustic scene classification](https://arxiv.org/abs/2203.15751)

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向环境与城市声音解决轻量化部署问题。
- **来源：** [论文主页](https://arxiv.org/abs/2203.15751) · [PDF](https://arxiv.org/pdf/2203.15751) · arXiv 2203.15751

</details>

<details>
<summary><strong>2021 年（12 篇）</strong></summary>

#### [What Makes Sound Event Localization and Detection Difficult Insights from Error Analysis](https://arxiv.org/abs/2107.10469)

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2107.10469) · [PDF](https://arxiv.org/pdf/2107.10469) · arXiv 2107.10469

#### [The Impact of Non-Target Events in Synthetic Soundscapes for Sound Event Detection](https://arxiv.org/abs/2109.14061)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据增强与生成开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2109.14061) · [PDF](https://arxiv.org/pdf/2109.14061) · arXiv 2109.14061

#### [SPATIAL DATA AUGMENTATION WITH SIMULATED ROOM IMPULSE RESPONSES FOR SOUND EVENT LOCALIZATION AND DETECTION](https://arxiv.org/abs/2110.06501)

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据增强与生成，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2110.06501) · [PDF](https://arxiv.org/pdf/2110.06501) · arXiv 2110.06501

#### [SOUND EVENT DETECTION IN URBAN AUDIO WITH SINGLE AND MULTI-RATE PCEN](https://arxiv.org/abs/2102.03468)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2102.03468) · [PDF](https://arxiv.org/pdf/2102.03468) · arXiv 2102.03468

#### [On the Effect of Coding Artifacts on Acoustic Scene Classification](https://arxiv.org/abs/2112.04841)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2112.04841) · [PDF](https://arxiv.org/pdf/2112.04841) · arXiv 2112.04841

#### [Forward-Backward Convolutional Recurrent Neural Networks and Tag-Conditioned Convolutional Neural Networks for Weakly Labeled Semi-Supervised Sound Event Detection](https://arxiv.org/abs/2103.06581)

- **日期：** 日期待核验
- **问题 / 中文简述：** 半/弱监督；采用数据驱动方法，面向声音事件解决半/弱监督问题。
- **来源：** [论文主页](https://arxiv.org/abs/2103.06581) · [PDF](https://arxiv.org/pdf/2103.06581) · arXiv 2103.06581

#### [Fairness and Underspecification in Acoustic Scene Classification The Case for Disaggregated Evaluations](https://arxiv.org/abs/2110.01506)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2110.01506) · [PDF](https://arxiv.org/pdf/2110.01506) · arXiv 2110.01506

#### [ENSEMBLE OF ACCDOA- AND EINV2-BASED SYSTEMS WITH D3NETS AND IMPULSE RESPONSE SIMULATION FOR SOUND EVENT LOCALIZATION AND DETECTION](https://arxiv.org/abs/2106.10806)

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2106.10806) · [PDF](https://arxiv.org/pdf/2106.10806) · arXiv 2106.10806

#### [Domain Generalization on Efficient Acoustic Scene Classification Using Residual Normalization](https://arxiv.org/abs/2111.06531)

- **日期：** 日期待核验
- **问题 / 中文简述：** 跨域泛化 · 轻量化部署；采用数据驱动方法，面向环境与城市声音解决跨域泛化问题。
- **来源：** [论文主页](https://arxiv.org/abs/2111.06531) · [PDF](https://arxiv.org/pdf/2111.06531) · arXiv 2111.06531

#### [Assessment of Self-Attention on Learned Features For Sound Event Localization and Detection](https://arxiv.org/abs/2107.09388)

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用Transformer 表征，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2107.09388) · [PDF](https://arxiv.org/pdf/2107.09388) · arXiv 2107.09388

#### [A lottery ticket hypothesis framework for low-complexity device-robust neural acoustic scene classification](https://arxiv.org/abs/2107.01461)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2107.01461) · [PDF](https://arxiv.org/pdf/2107.01461) · arXiv 2107.01461

#### [A Dataset of Dynamic Reverberant Sound Scenes with Directional Interferers for Sound Event Localization and Detection](https://arxiv.org/abs/2106.06999)

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2106.06999) · [PDF](https://arxiv.org/pdf/2106.06999) · arXiv 2106.06999

</details>

<details>
<summary><strong>2020 年（9 篇）</strong></summary>

#### [Training Sound Event Detection on a Heterogeneous Dataset](https://arxiv.org/abs/2007.03931)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2007.03931) · [PDF](https://arxiv.org/pdf/2007.03931) · arXiv 2007.03931

#### [Sound Event Localization and Detection Based on CRNN using Rectangular Filters and Channel Rotation Data Augmentation](https://arxiv.org/abs/2010.06422)

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据增强与生成，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2010.06422) · [PDF](https://arxiv.org/pdf/2010.06422) · arXiv 2010.06422

#### [SOUND EVENT LOCALIZATION AND DETECTION USING ACTIVITY-COUPLED CARTESIAN DOA VECTOR AND RD3NET-Rank 3](https://arxiv.org/abs/2006.12014)

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2006.12014) · [PDF](https://arxiv.org/pdf/2006.12014) · arXiv 2006.12014

#### [Low-Complexity Models for Acoustic Scene Classification Based on Receptive Field Regularization and Frequency Damping](https://arxiv.org/abs/2011.02955)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2011.02955) · [PDF](https://arxiv.org/pdf/2011.02955) · arXiv 2011.02955

#### [Improving Sound Event Detection in Domestic Environments using Sound Separation](https://arxiv.org/abs/2007.03932)

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2007.03932) · [PDF](https://arxiv.org/pdf/2007.03932) · arXiv 2007.03932

#### [Guided Multi-Branch Learning Systems for Sound Event Detection with Sound Separation](https://arxiv.org/abs/2007.10638)

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2007.10638) · [PDF](https://arxiv.org/pdf/2007.10638) · arXiv 2007.10638

#### [Event-Independent Network for Polyphonic Sound Event Localization and Detection](https://arxiv.org/abs/2010.00140)

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2010.00140) · [PDF](https://arxiv.org/pdf/2010.00140) · arXiv 2010.00140

#### [Acoustic Scene Classification with Spectrogram Processing Strategies](https://arxiv.org/abs/2007.03781)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/2007.03781) · [PDF](https://arxiv.org/pdf/2007.03781) · arXiv 2007.03781

#### [A Dataset of Reverberant Spatial Sound Scenes with Moving Sources for Sound Event Localization and Detection](https://arxiv.org/abs/2006.01919)

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** [论文主页](https://arxiv.org/abs/2006.01919) · [PDF](https://arxiv.org/pdf/2006.01919) · arXiv 2006.01919

</details>

<details>
<summary><strong>2019 年（2 篇）</strong></summary>

#### [VOICe A Sound Event Detection Dataset For Generalizable Domain Adaptation](https://arxiv.org/abs/1911.07098)

- **日期：** 日期待核验
- **问题 / 中文简述：** 跨域泛化；采用数据驱动方法，面向声音事件解决跨域泛化问题。
- **来源：** [论文主页](https://arxiv.org/abs/1911.07098) · [PDF](https://arxiv.org/pdf/1911.07098) · arXiv 1911.07098

#### [SOUND EVENT RECOGNITION IN A SMART CITY SURVEILLANCE CONTEXT](https://arxiv.org/abs/1910.12369)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/1910.12369) · [PDF](https://arxiv.org/pdf/1910.12369) · arXiv 1910.12369

</details>

<details>
<summary><strong>2017 年（1 篇）</strong></summary>

#### [Impulsive sound detection by a novel energy formula and its usage for gunshot recognition](https://arxiv.org/abs/1706.08759)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** [论文主页](https://arxiv.org/abs/1706.08759) · [PDF](https://arxiv.org/pdf/1706.08759) · arXiv 1706.08759

</details>

<details>
<summary><strong>年份待核验（496 篇）</strong></summary>

#### 基于减小高频混响和 RF-DRSN-EMA 的声音事件分类方法

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### buzzdetect: an open-source deep learning tool for automated bioacoustic pollinator monitoring

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Zero-shot learning for acoustic event classification using an attribute vector and conditional GAN

- **日期：** 日期待核验
- **问题 / 中文简述：** 开放集/OOD；采用数据驱动方法，面向声音事件解决开放集/OOD问题。
- **来源：** 题名级候选，身份待核验

#### YOLO-Based Transfer Learning for Sound Event Detection Using Visual Object Detection Techniques

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Wind turbine blade fault detection based on graph Fourier transform and deep learning

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展工业与机械声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Wind turbine blade anomaly recognition method based on sound feature fusion

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Wild bird species identification based on a lightweight model with frequency dynamic convolution

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向生态与动物声音解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### Whombat- An open‐source audio annotation tool for machine learning assisted bioacoustics

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### What Matters for Bioacoustic Encoding

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Weakly Labeled Environmental Sound Event Detection Based on Dynamic Multi-scale Convolution Attention

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Waveforms and Spectrograms Enhancing Acoustic Scene Classification Using Multimodal Feature Fusion

- **日期：** 日期待核验
- **问题 / 中文简述：** 多模态与基础模型；采用数据驱动方法，面向环境与城市声音解决多模态与基础模型问题。
- **来源：** 题名级候选，身份待核验

#### WABAD A World Annotated Bird Acoustic Dataset

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Visual Bird Sounds

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Vehicle type classification based on acoustic signals using LT-MFCC

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展交通与水下声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### VIBRO-ACOUSTIC ANALYSIS OF LOOSE FOUNDATION EFFECTS IN ELECTRIC MOTORS AT VARYING ROTATIONAL SPEEDS

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展工业与机械声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Urban Sound and Environmental Monitoring using Distributed IoT Sensor Nodes

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Universal Incremental Learning for Few-Shot Bird Sound Classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 少样本 · 持续学习；采用数据驱动方法，面向生态与动物声音解决少样本问题。
- **来源：** 题名级候选，身份待核验

#### Two-way analysis of variance (ANOVA) ranking of features based on wavelet bi-phase and bi-spectrum for the classification of adventitious lung sounds

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展医疗与生理声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Two-stage Acoustic Event Detection and Classification for Horn Signals in Urban Scenarios: Comparing VGGish, YAMNet and Mel Spectrogram Approaches with mRMR Feature Selection

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Two-Stage Domain Adaptation for Sound Event Detection

- **日期：** 日期待核验
- **问题 / 中文简述：** 跨域泛化；采用数据驱动方法，面向声音事件解决跨域泛化问题。
- **来源：** 题名级候选，身份待核验

#### Training Onset-and-Offset-Aware Sound Event Detection on a Heterogeneous Dataset via Probabilistic Sequential Modeling

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Towards cross-lingual audio abuse detection in low-resource settings with few-shot learning

- **日期：** 日期待核验
- **问题 / 中文简述：** 少样本；采用数据驱动方法，面向声音事件解决少样本问题。
- **来源：** 题名级候选，身份待核验

#### Towards User Interface Design Guidelines for Effective Human-AI Interaction in Bioacoustics

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Toward in-context bioacoustic sound event detection

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Toward Interpretable Polyphonic Sound Event Detection with Attention Maps Based on Local Prototypes

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Tmac: Temporal multi-modal graph learning for acoustic event classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Time Series Generation for Augmenting Multi-channel Automotive Audio Data

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### The secret acoustic world of leopards: A paired camera trap and bioacoustics survey facilitates individual identification of leopards via their roars

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### The potential of bioacoustics for surveying carrion insects

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### The Biophone: Developing and Testing a Bioacoustic Recorder for Science and Citizen Science

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### The Bioacoustic Bridge: Using Animal Vocalization & Motion Signals to Predict Natural Hazards

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### The APSIPA ASC 2025 Grand Challenge on City and Time-Aware Semi-Supervised Acoustic Scene Classification- Summary and Results

- **日期：** 日期待核验
- **问题 / 中文简述：** 半/弱监督；采用数据驱动方法，面向环境与城市声音解决半/弱监督问题。
- **来源：** 题名级候选，身份待核验

#### Text-guided Device-realistic Sound Generation for Fiber-based Sound Event Classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Temporal-aware multimodal event network for dense audio-visual event localization

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离 · 多模态与基础模型；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### TINY AUDIO SPECTROGRAM TRANSFORMER- MOBILEVIT FOR LOW-COMPLEXITY ACOUSTIC SCENE CLASSIFICATION WITH DECOUPLED KNOWLEDGE DISTILLATION

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用Transformer 表征，面向环境与城市声音解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### THE USE OF BIOACOUSTICS IN BIODIVERSITY MONITORING AND WILDLIFE CONSERVATION IN PANTI FOREST RESERVE, JOHOR

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### THE SYSTEM USING CONVNEXT, CONFORMER, AND DATA AUGMENTATION FOR SOUND EVENT LOCALIZATION AND DETECTION

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用Transformer 表征，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### TF-AttNet: An Efficient Time-Frequency Structure Modeling For Low-Complexity Acoustic Scene Classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向环境与城市声音解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### TEFFDConv An Improved Approach to Enhance Temporal Localization in Sound Event Detection

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### Systematic design and evaluation of a structure-guided multimodal framework for heart sound classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 多模态与基础模型；采用数据驱动方法，面向医疗与生理声音解决多模态与基础模型问题。
- **来源：** 题名级候选，身份待核验

#### Synthetic data generation techniques for training deep acoustic siren identification networks

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据增强与生成开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### SunEcho: An Optimized Deep Learning Model for Real-Time Urban Environmental Sound Classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Studying Domain Shifts in Bioacoustic Recording Style With Information Theory

- **日期：** 日期待核验
- **问题 / 中文简述：** 跨域泛化；采用数据驱动方法，面向生态与动物声音解决跨域泛化问题。
- **来源：** 题名级候选，身份待核验

#### Stratified Active Learning for Spatiotemporal Generalisation in Bioacoustic Monitoring

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Stereo Sound Event Localization and Detection with Onscreenoffscreen Classification_2

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### Stereo Sound Event Localization and Detection with Onscreenoffscreen Classification_1

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### Stereo Sound Event Localization and Detection with OnscreenOffscreen Classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### Static Sound Event Localization and Detection Using Bipartite Matching Loss for Emergency Monitoring

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### Speeding Up Bioacoustic Data Analysis: Fine-Tuning Deep Models with Active Learning for Efficient Wildlife Detection

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向生态与动物声音解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### Speech Obfuscation in Mel Spectra That Allows for Centralised Annotation and Classification of Sound Events

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Specification of a smart-analysis system of sound events for smart environments

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Spatiotemporal attention-driven joint reconstruction of elevator audio and vibration signals via dual-modality fusion

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Spatial Annotation-free Training for Sound Event Localization and Detection

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### Spatial Annotation-Free Sound Event Localization and Detection via Spatial Instance Classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### Source-Aware Spatial Self-Supervision for Sound Event Localization and Detection

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### Soundscape Identification of Endangered Bird Species using Bidirectional Long Short Term Memory

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Sound event localization and detection using a spatial omni-dimensional dynamic interactions network

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### Sound event localization and classification using wireless acoustic sensor networks in outdoor environments

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### Sound event detection with soft labels- a new perspective on evaluation

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Sound event detection in traffic scenes based on graph convolutional network to obtain multi-modal information

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展交通与水下声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Sound event detection in domestic environment using frequency-dynamic convolution and local attention

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Sound event detection for modified-exhaust vehicles in urban environment

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展交通与水下声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Sound event detection based on soft label

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Sound Events Localization and Detection Using Bio-inspired Gammatone Filters and Temporal Convolutional Neural Networks

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### Sound Event Localization and Detection with Pre-Trained Audio Spectrogram Transformer and Multichannel Seperation Network

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用Transformer 表征，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### Sound Event Localization and Detection Using Parallel Multi-attention Enhancement

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用Transformer 表征，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### Sound Event Localization and Detection Based on Adaptive Hybrid Convolution and Multi-scale Feature Extractor

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### Sound Event Detection using Time-frequency Bounding Boxes with a Self-Supervised Audio Spectrogram Transformer

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用自监督表征开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Sound Event Detection in Traffic Scene Based on Graph Neural Network

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展交通与水下声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Sound Event Detection in Smart Cities: A Systematic Review of Methods, Datasets, and Applications

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Sound Event Detection in Constrained Real-world Environments using Fine Tuned CNNs

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Sound Event Detection for Detecting Modified-Exhaust Vehicles in Urban Environments

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展交通与水下声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Sound Event Classification with Object-Based Labels

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Smartphone for heart sound measurement in hospital: feasibility and influencing factors

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展医疗与生理声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### SmartEars: a practical framework for poultry respiratory monitoring via spectrogram-based audio classification and AI-assisted labeling

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展医疗与生理声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Semi-supervised sound event detection with dynamic convolution and confidence-aware mean teacher

- **日期：** 日期待核验
- **问题 / 中文简述：** 半/弱监督 · 可解释与可靠性；采用数据驱动方法，面向声音事件解决半/弱监督问题。
- **来源：** 题名级候选，身份待核验

#### Semi-supervised sound event detection system for DCASE 2023 task4a

- **日期：** 日期待核验
- **问题 / 中文简述：** 半/弱监督；采用数据驱动方法，面向声音事件解决半/弱监督问题。
- **来源：** 题名级候选，身份待核验

#### Semi-supervised and transfer learning for few-shot audio classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 少样本 · 半/弱监督；采用数据驱动方法，面向声音事件解决少样本问题。
- **来源：** 题名级候选，身份待核验

#### Semi-supervised acoustic scene classification with test-time adaptation

- **日期：** 日期待核验
- **问题 / 中文简述：** 半/弱监督；采用数据驱动方法，面向环境与城市声音解决半/弱监督问题。
- **来源：** 题名级候选，身份待核验

#### Semi-supervised Sound Event Detection Using Multiscale Channel Attention and Multiple Consistency Training

- **日期：** 日期待核验
- **问题 / 中文简述：** 半/弱监督；采用Transformer 表征，面向声音事件解决半/弱监督问题。
- **来源：** 题名级候选，身份待核验

#### Semi-supervised Learning for Acoustic Scene Classification using FixMatch

- **日期：** 日期待核验
- **问题 / 中文简述：** 半/弱监督；采用数据驱动方法，面向环境与城市声音解决半/弱监督问题。
- **来源：** 题名级候选，身份待核验

#### Semi-supervised Acoustic Scene Classification under Spatial-Temporal Variability with a CRNN-based Model

- **日期：** 日期待核验
- **问题 / 中文简述：** 半/弱监督；采用数据驱动方法，面向环境与城市声音解决半/弱监督问题。
- **来源：** 题名级候选，身份待核验

#### Semi-Supervised Sound Event Detection with Pre-Trained Model

- **日期：** 日期待核验
- **问题 / 中文简述：** 半/弱监督；采用数据驱动方法，面向声音事件解决半/弱监督问题。
- **来源：** 题名级候选，身份待核验

#### Semi-Supervised Sound Event Detection System Based on Complex Convolutional Recurrent Neural Network

- **日期：** 日期待核验
- **问题 / 中文简述：** 半/弱监督；采用数据驱动方法，面向声音事件解决半/弱监督问题。
- **来源：** 题名级候选，身份待核验

#### Self-Trained Audio Tagging and Sound Event Detection in Domestic Environments

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Segmentation of heart sound signals using improved Hilbert transform and wavelet packet transform

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展医疗与生理声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Searching for Efficient Network Architectures for Acoustic Scene Classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向环境与城市声音解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### Scene-dependent sound event detection based on multitask learning with deformable large kernel attention convolution

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Scaling Bioacoustic Signal Pre-training with Million Samples Via Mask-Modeling

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Scalable neural architectures for end-to-end environmental sound classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Scalable and low-power edge architecture with Wi-Fi HaLow and on-device spectrograms generation for flexible urban bioacoustics monitoring

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向生态与动物声音解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### Same data, different results? Machine learning approaches in bioacoustics

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### SUPERVISED CONTRASTIVE LEARNING FOR PRE-TRAINING BIOACOUSTIC FEW-SHOT SYSTEMS-Rank 2

- **日期：** 日期待核验
- **问题 / 中文简述：** 少样本；采用对比与原型学习，面向生态与动物声音解决少样本问题。
- **来源：** 题名级候选，身份待核验

#### SUPERVISED CONTRASTIVE LEARNING FOR PRE-TRAINING BIOACOUSTIC FEW-SHOT SYSTEMS

- **日期：** 日期待核验
- **问题 / 中文简述：** 少样本；采用对比与原型学习，面向生态与动物声音解决少样本问题。
- **来源：** 题名级候选，身份待核验

#### STUDY OF THE EFFECTIVENESS OF BIOACOUSTIC CORRECTION (BAC) THERAPY IN CHILDREN WITH FEBRILE SEIZURES

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### SS-ESC: a spectral subtraction denoising based deep network model on environmental sound classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 低信噪比；采用数据驱动方法，面向环境与城市声音解决低信噪比问题。
- **来源：** 题名级候选，身份待核验

#### SOUND EVENT LOCALIZATION AND DETECTION BASED ON OMI-DIMENSIONAL DYNAMIC CONVOLUTION AND FEATURE PYRAMID ATTENTION MODULE

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用Transformer 表征，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### SOUND EVENT DETECTION WITH SOFT LABELS USING SELF-ATTENTION MECHANISMS FOR GLOBAL SCENE FEATURE EXTRACTION

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### SOUND EVENT DETECTION BY AGGREGATING PRE-TRAINED EMBEDDINGS FROM DIFFERENT LAYERS

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### SIAlex Species identification and monitoring based on bird sound features

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### SE-PROTONET- PROTOTYPICAL NETWORK WITH SQUEEZE-AND-EXCITATION BLOCKS FOR BIOACOUSTIC EVENT DETECTION-Rank 3

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### SE-PROTONET- PROTOTYPICAL NETWORK WITH SQUEEZE-AND-EXCITATION BLOCKS FOR BIOACOUSTIC EVENT DETECTION

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Robust classification of urban sounds in noisy environments: A novel approach using SPWVD-MFCC and dual-stream classifier

- **日期：** 日期待核验
- **问题 / 中文简述：** 低信噪比；采用数据驱动方法，面向环境与城市声音解决低信噪比问题。
- **来源：** 题名级候选，身份待核验

#### Robust cepstral feature for bird sound classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Road traffic events monitoring using a multi-head attention mechanism-based transformer and temporal convolutional networks

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展交通与水下声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Rnn-enriched deep transfer learning model for audio-based classification in various environmental settings

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Retrieval-Augmented Bioacoustics: Evidence-Guided Generation for Animal Communication

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Research progress in bird sounds recognition based on acoustic monitoring technology- A systematic review

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Research on acoustic scene classification based on time–frequency–wavelet fusion network

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Research on Traffic Sound Event Detection Based on Multi-Scale Feature Fusion

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展交通与水下声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### ResCapsnet a capsule network with CRAM and BiGRU for sound event detection

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Representations for Acoustic Scene

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### RepSepNet: A Lightweight Reparameterized CNN for Gunshot Detection on Edge Devices

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向声音事件解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### Relaxed Instance Frequency-wise Normalization for Semi-supervised Acoustic Scene Classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 半/弱监督；采用数据驱动方法，面向环境与城市声音解决半/弱监督问题。
- **来源：** 题名级候选，身份待核验

#### Real-Time Sound Event Localization and Detection using IoT Raspberry PI Devices based on Single-Stage CRNN

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### Raw Audio Deep Learning Filter Banks for Acoustic Scene Classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Rare sound event detection using superlets and a convolutional TDPANet: G. Pandey et al.

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Randmasking augment: A simple and randomized data augmentation for acoustic scene classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据增强与生成开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### RQNet: Residual quaternion CNN for performance enhancement in low complexity and device robust acoustic scene classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### RELEVANCE OF RADIATOR INSTALLATION ON THE EFFICACY OF NOISE REDUCTION STRATEGIES IN AN INDUSTRIAL ENGINE COOLING FAN

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展工业与机械声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Quantity Over Quality Investigating the Effects of Volume and Strength of Training Data in Marine Bioacoustics

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Prototyping an internet-of-things-based bioacoustics system to support research and surveillance of avian-associated infectious diseases

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Polyphonic sound event localization and detection using channel-wise FusionNet

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### Polyphonic sound event localization and detection based on Multiple Attention Fusion ResNet

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用Transformer 表征，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### Performance Comparison of Overlapping Sound Event Detection Methods

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Perch 2.0 The Bittern Lesson for Bioacoustics

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Passive acoustic monitoring and acoustic indices reveal noise-related changes in bird vocalisations

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Papafil A Low Complexity Sound Event Localization and Detection Method with Parametric Particle Filtering and Gradient Boosting

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### PLDISET Probabilistic Localization and Detection of Independent Sound Events with Transformers

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用Transformer 表征，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### PLCST- PROBABILISTIC LOCALIZATION AND CLASSIFICATION OF SOUNDS WITH TRANSFORMERS FOR SOUND EVENT LOCALIZATION AND DETECTION

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用Transformer 表征，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### PAT: Parameter-free audio-text aligner to boost zero-shot audio classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 开放集/OOD；采用数据驱动方法，面向声音事件解决开放集/OOD问题。
- **来源：** 题名级候选，身份待核验

#### Optimized Network Combining Depthwise Separable Convolutional with Multi-scale Dilated Convolution Used for Polyphonic Sound Event Detection

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Open-Window A Sound Event Dataset for Window State Detection and Recognition

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Open set classification of sound event

- **日期：** 日期待核验
- **问题 / 中文简述：** 开放集/OOD；采用数据驱动方法，面向声音事件解决开放集/OOD问题。
- **来源：** 题名级候选，身份待核验

#### Onset-and-offset-aware sound event detection via differentiable frame-to-event mapping

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Online incremental learning for audio classification using a pretrained audio model

- **日期：** 日期待核验
- **问题 / 中文简述：** 持续学习；采用数据驱动方法，面向声音事件解决持续学习问题。
- **来源：** 题名级候选，身份待核验

#### One-Class Bioacoustic Detector for Monitoring the Critically Endangered Pied Tamarin

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### One Detector per Bird: A Scalable Binary Classification Approach for BirdCLEF 2025.

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### On the Role of Training Class Distribution in Zero-Shot Audio Classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 开放集/OOD；采用数据驱动方法，面向声音事件解决开放集/OOD问题。
- **来源：** 题名级候选，身份待核验

#### On the Effectiveness of Spatial and Multi-Channel Features for Multi-Channel Polyphonic Sound Event Detection

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Novel sound event and sound activity detection framework based on intrinsic mode functions and deep learning

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Novel generative classifier for acoustic events

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据增强与生成开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### NoisenseDB- An Urban Sound Event Database to Develop Neural Classification Systems for Noise-Monitoring Applications

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Noise-Resilient Bioacoustics Feature Extraction Methods and Their Implications on Audio Classification Performance: Systematic Review

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Neural style transfer architectures for improving generalization in low-resource spoken language identification

- **日期：** 日期待核验
- **问题 / 中文简述：** 少样本；采用数据驱动方法，面向声音事件解决少样本问题。
- **来源：** 题名级候选，身份待核验

#### Multiscale analysis of heart sound signals in the wavelet domain for heart murmur detection

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展医疗与生理声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Multimodal Audio-Visual Approach to Vehicle Detection and Classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 多模态与基础模型；采用数据驱动方法，面向交通与水下声音解决多模态与基础模型问题。
- **来源：** 题名级候选，身份待核验

#### Multilingual audio classification: A scalable approach using Wav2Vec2 and Qdrant

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Multiclass classification of faulty industrial machinery using sound samples

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展工业与机械声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Multi-view Fusion and Parameter Perturbation for Few-Shot Class-Incremental Audio Classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 少样本 · 持续学习；采用数据驱动方法，面向声音事件解决少样本问题。
- **来源：** 题名级候选，身份待核验

#### Multi-modal Language models in bioacoustics with zero-shot transfer a case study Scientific Reports

- **日期：** 日期待核验
- **问题 / 中文简述：** 开放集/OOD；采用音频语言模型，面向生态与动物声音解决开放集/OOD问题。
- **来源：** 题名级候选，身份待核验

#### Multi-granularity acoustic information fusion for sound event detection

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Multi-Task Domain Adaptation with Semi-Supervised Learning for Real-World Acoustic Event Detection.

- **日期：** 日期待核验
- **问题 / 中文简述：** 半/弱监督 · 跨域泛化；采用层级与多任务学习，面向声音事件解决半/弱监督问题。
- **来源：** 题名级候选，身份待核验

#### Multi-Scale Network based on Split Attention for Semi-supervised Sound event detection

- **日期：** 日期待核验
- **问题 / 中文简述：** 半/弱监督；采用Transformer 表征，面向声音事件解决半/弱监督问题。
- **来源：** 题名级候选，身份待核验

#### Multi-Scale Architecture and Device-Aware Data-Random-Drop Based Fine-Tuning Method for Acoustic Scene Classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Multi-Resolution Conformer for Sound Event Detection Analysis and Optimization

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Monitoring with machines: a review of computational bioacoustics

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Moflenet A Low Complexity Model for Acoustic Scene Classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Modelling Spatio-Temporal Dynamics by Graph Attention Network for Distributed Multi-Microphone Sound Event Classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Model Training that Prioritizes Rare Overlapped Labels for Polyphonic Sound Event Detection

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Mixstyle based Domain Generalization for Sound Event Detection with Heterogeneous Training Data

- **日期：** 日期待核验
- **问题 / 中文简述：** 跨域泛化；采用数据驱动方法，面向声音事件解决跨域泛化问题。
- **来源：** 题名级候选，身份待核验

#### Mini-SegNet and Low-Complexity MobileNet for Acoustic Scene Classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Meta-learning-based percussion transcription and $ t\bar {a} la $ identification from low-resource audio

- **日期：** 日期待核验
- **问题 / 中文简述：** 少样本；采用数据驱动方法，面向声音事件解决少样本问题。
- **来源：** 题名级候选，身份待核验

#### Mel-based feature extraction for acoustic event detection and classification: A systematic review and research roadmap

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Marine Bioacoustic Sound Classification Based on Enhanced ResNet: Synergy of Adaptive Attention and Multi-Scale Fusion

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Many-to-Many Audio Spectrogram Tansformer Transformer for Sound Event Localization and Detection

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用Transformer 表征，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### Machine learning based fault classification for improved induction motor performance

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展工业与机械声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Machine Learning-Based Approach to Identifying Bird Species Through Vocalization

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### MaSGAN: a malfunction sound detection model for industrial machines using the generative adversarial networks

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据增强与生成开展工业与机械声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### MULTI-TASK FRAME LEVEL SYSTEM FOR FEW-SHOT BIOACOUSTIC EVENT DETECTION-Rank 1

- **日期：** 日期待核验
- **问题 / 中文简述：** 少样本；采用层级与多任务学习，面向生态与动物声音解决少样本问题。
- **来源：** 题名级候选，身份待核验

#### MULTI-TASK FRAME LEVEL SYSTEM FOR FEW-SHOT BIOACOUSTIC EVENT DETECTION

- **日期：** 日期待核验
- **问题 / 中文简述：** 少样本；采用层级与多任务学习，面向生态与动物声音解决少样本问题。
- **来源：** 题名级候选，身份待核验

#### MULTI-SCALE FEATURE FUSION FOR SOUND EVENT LOCALIZATION AND DETECTION

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### MSA-TCN: Robust Urban Suspicious Sound Detection Using Multi-Scale Temporal Convolutions and Dual Attention

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### MELAUDIS: A large-scale benchmark acoustic dataset for intelligent transportation systems research

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### MAGENTA Magnitude and Geometry-ENhanced Training Approach for Robust Long-Tailed Sound Event Localization and Detection

- **日期：** 日期待核验
- **问题 / 中文简述：** 长尾与不平衡 · 定位与分离；采用数据驱动方法，面向声音事件解决长尾与不平衡问题。
- **来源：** 题名级候选，身份待核验

#### MAGENTA Magnitude and Geometry-ENhanced Training Approach for Robust Long-Tailed Sound Event Locali

- **日期：** 日期待核验
- **问题 / 中文简述：** 长尾与不平衡；采用数据驱动方法，面向声音事件解决长尾与不平衡问题。
- **来源：** 题名级候选，身份待核验

#### M3Net: efficient time-frequency integration network with mirror attention for audio classification on edge

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用Transformer 表征，面向声音事件解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### Lungmix: A mixup-based strategy for generalization in respiratory sound classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展医疗与生理声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Low-complexity acoustic scene classification using data augmentation and lightweight ResNet

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用数据增强与生成，面向环境与城市声音解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### Low-SNR Northern Right Whale upcall detection and classification using passive acoustic monitoring to reduce adverse human–whale interactions

- **日期：** 日期待核验
- **问题 / 中文简述：** 低信噪比；采用数据驱动方法，面向生态与动物声音解决低信噪比问题。
- **来源：** 题名级候选，身份待核验

#### Low-Resource Ecoacoustic Audio Classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 少样本；采用数据驱动方法，面向声音事件解决少样本问题。
- **来源：** 题名级候选，身份待核验

#### Low-Complexity CNNs for Acoustic Scene Classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Low-Complexity Acoustic Scene Classification Using Deep Mutual Learning and Knowledge Distillation Fine-Tuning

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向环境与城市声音解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### Low-Complexity Acoustic Scene Classification Base on Depthwise separable CNN

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Lightweight Convolutional Neural Networks on Binaural Waveforms for Low Complexity Acoustic Scene Classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向环境与城市声音解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### Leveraging an observed-data likelihood improves the use of machine learning labels in a Bayesian hierarchical model for bioacoustic data

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用层级与多任务学习开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Leveraging Multi-Level Features of ATST with Conformer-Based Dual-Branch Network for Sound Event Detection

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Leveraging Machine Learning for Speech Classification Using Librosa and Neural Networks

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展工业与机械声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Learning in the Wild Bioacoustics Few Shot Learning Without Using a Training Set

- **日期：** 日期待核验
- **问题 / 中文简述：** 少样本；采用数据驱动方法，面向生态与动物声音解决少样本问题。
- **来源：** 题名级候选，身份待核验

#### Latent and Adversarial Data Augmentations for Sound Event Detection and Classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据增强与生成开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Label Filtering-Based Self-Learning for Sound Event Detection Using Frequency Dynamic Convolution with Large Kernel Attention

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### LSKFDY-CNN: Large selective kernel frequency dynamic convolutional neural network for sound event detection

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### LOW-COMPLEXITY DEEP LEARNING SYSTEM FOR ACOUSTIC SCENE CLASSIFICATION USING TEACHER-STUDENT SCHEME AND MULTIPLE SPECTROGRAMS

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### LOW-COMPLEXITY ACOUSTIC SCENE CLASSIFICATION WITH LIMITED TRAINING DATA

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### LOW-COMPLEXITY ACOUSTIC SCENE CLASSIFICATION USING DEEP SPACE SEPARABLE DISTILLATION AND MULTI-TASK LEARNING

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用层级与多任务学习，面向环境与城市声音解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### LOW-COMPLEXITY ACOUSTIC SCENE CLASSIFICATION USING CONVOLUTION NEURAL NETWORK

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### LOW-COMPLEXITY ACOUSTIC SCENE CLASSIFICATION USING BLUEPRINT SEPARABLE CONVOLUTION AND KNOWLEDGE DISTILLATION

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向环境与城市声音解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### LOW COMPLEXITY ACOUSTIC SCENE CLASSIFICATION WITH MOFLENET

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### LOCAL AND GLOBAL FEATURES FUSION FOR SOUND EVENT DETECTION WITH HETEROGENEOUS TRAINING DATASET AND POTENTIALLY MISSING LABELS

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Knowledge Distillation from Transformers for Low-Complexity Acoustic Scene Classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用Transformer 表征，面向环境与城市声音解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### KT SUBMISSION- PERIODIC ACTIVATION AND KNOWLEDGE DISTILLATION FOR DATA-EFFICIENT LOW-COMPLEXITY ACOUSTIC SCENE CLASSIFICATION

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向环境与城市声音解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### Joint Training of Guided Learning and Mean Teacher Models for Sound Event Detection

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### IoMT-enabled noninvasive lungs disease detection and classification using deep learning-based analysis of lungs sounds

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Investigations of the Effect of 3D Bioacoustic Signals Reproduced in a VR Room on Patients in a Geriatric Ward of a Hospital

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Investigating the impact of feature extraction techniques for classification and synthesis of dysarthric speech

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Investigating the drivers of temporal and spatial dynamics in urban forest bird acoustic patterns

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Integrating AI models into ecological research workflows: The case of terrestrial bioacoustics

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Installation Effects on the Acoustics of Low-Pressure Axial Fans Aspects of Source, Environment and Receiver

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Insights into Corncrake (Crex crex) movements in a fragmented agricultural landscape using bioacoustics with implications for nature conservation strategies

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Insect bioacoustics and biotremology

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Influence of recording devices and environmental noise on acoustic index scores- Implications for bird sound-based assessments

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Infant cry verification with multi-view self-attention vision transformers

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Increased avian bioacoustic diversity without lost profit after planting perennial vegetation in marginal cropland

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Improving continual learning of acoustic scene classification via mutual information optimization

- **日期：** 日期待核验
- **问题 / 中文简述：** 持续学习；采用数据驱动方法，面向环境与城市声音解决持续学习问题。
- **来源：** 题名级候选，身份待核验

#### Improving bird sounds classification with additional fine-tuning on augmented data

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Improving acoustic scene classification in low-resource conditions

- **日期：** 日期待核验
- **问题 / 中文简述：** 少样本；采用数据驱动方法，面向环境与城市声音解决少样本问题。
- **来源：** 题名级候选，身份待核验

#### Improving Sound Event Detection with Foreground-Background Classification and Domain Adaptation

- **日期：** 日期待核验
- **问题 / 中文简述：** 跨域泛化；采用数据驱动方法，面向声音事件解决跨域泛化问题。
- **来源：** 题名级候选，身份待核验

#### Improving Acoustic Recognition Models/Author Paul Primus

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Improved detection of bird vocalisations using BirdNET embeddings and machine learning

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Importance of the integrated use of bioacoustics and mist nets for bat surveys

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Implementing transfer learning for sound event classification using the realised audio database

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Ifap-Net An Interactive Feature Aggregation and Perception Network for 3D Sound Event Localization and Detection by Yongbo Li, Qinghua Huang, Kai Liu

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### Hypergradient descent based multi-task learning on auscultation point guided respiratory sound classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用层级与多任务学习开展医疗与生理声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Hissnet: Sound event detection and speaker identification via hierarchical prototypical networks for low-resource headphones

- **日期：** 日期待核验
- **问题 / 中文简述：** 少样本；采用层级与多任务学习，面向声音事件解决少样本问题。
- **来源：** 题名级候选，身份待核验

#### High-Accuracy Audio-based Vehicle Detection: Deep Learning vs Machine Learning

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展工业与机械声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Hierarchical Self-Distillation with Attention for Class-Imbalanced Acoustic Event Classification in Elevators

- **日期：** 日期待核验
- **问题 / 中文简述：** 长尾与不平衡 · 轻量化部署；采用Transformer 表征，面向声音事件解决长尾与不平衡问题。
- **来源：** 题名级候选，身份待核验

#### Heartbeat sound classification using mel-spectrogram and CNN optimized by frilled lizard algorithm for cardiovascular disease detection

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Heartbeat audio signal analysis for cardiovascular abnormality diagnosis using neural-networks

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Hearing the Forest: Machine Learning for Biodiversity Monitoring Using Soundscapes

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Hand-Grip Strength Estimation through Bioacoustic Sensing

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### HamNava: A Dataset for Multi‑Label Instrument Classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Habitat use and temporal activity of the Big Crested Mastiff Bat (Promops centralis, Molossidae) along an urban-natural gradient: a bioacoustics approach

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### HOW INFORMATION ON SOFT LABELS AND HARD LABELS MUTUALLY BENEFITS SOUND EVENT DETECTION TASKS

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### HIERARCHICAL ACOUSTIC SCENE CLASSIFICATION WITH KNOWLEDGE DISTILLATION AND PRE-TRAINED DYNAMIC NETWORKS

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用层级与多任务学习，面向环境与城市声音解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### Group feature calibration for sound event detection

- **日期：** 日期待核验
- **问题 / 中文简述：** 可解释与可靠性；采用数据驱动方法，面向声音事件解决可解释与可靠性问题。
- **来源：** 题名级候选，身份待核验

#### Global Enhanced Frame Prompt Tuning for Sound Event Detection

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Giving Cows a Digital Voice–AI-Enabled Bioacoustics and Smart Sensing in Precision Livestock Management–A Review

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Fusion-Based Reduced Variation Representations for Acoustic Scene Classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Fully few-shot class-incremental audio classification with adaptive improvement of stability and plasticity

- **日期：** 日期待核验
- **问题 / 中文简述：** 少样本 · 持续学习；采用数据驱动方法，面向声音事件解决少样本问题。
- **来源：** 题名级候选，身份待核验

#### From traditional to geometric morphometrics: a novel approach in bat bioacoustic analysis

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### From General-Purpose Audio Tagging to Real-Time Emergency Vehicle Siren Detection

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展交通与水下声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Fine-tuning audio spectrogram transformer with task-aware adapters for sound event detection

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Field tests of impulsive acoustic event detection, localization, and classification over telecom fiber networks

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### Few-shot underwater acoustic target recognition using domain adaptation and knowledge distillation

- **日期：** 日期待核验
- **问题 / 中文简述：** 少样本 · 跨域泛化 · 轻量化部署；采用数据驱动方法，面向交通与水下声音解决少样本问题。
- **来源：** 题名级候选，身份待核验

#### Few-Shot_Bioacoustics_Event_Detection_using_Transudative_Inference_with_Data_Augmentation

- **日期：** 日期待核验
- **问题 / 中文简述：** 少样本；采用数据增强与生成，面向生态与动物声音解决少样本问题。
- **来源：** 题名级候选，身份待核验

#### Few-Shot Bioacoustics Event Detection Using Transductive Inference With Data Augmentation

- **日期：** 日期待核验
- **问题 / 中文简述：** 少样本；采用数据增强与生成，面向生态与动物声音解决少样本问题。
- **来源：** 题名级候选，身份待核验

#### Few-Shot Bioacoustic Event Detection Using an Event-Length Adapted Ensemble of Prototypical Networks

- **日期：** 日期待核验
- **问题 / 中文简述：** 少样本；采用数据驱动方法，面向生态与动物声音解决少样本问题。
- **来源：** 题名级候选，身份待核验

#### Few-Shot Bioacoustic Event Detection Enhanced Classifiers for Prototypical Networks

- **日期：** 日期待核验
- **问题 / 中文简述：** 少样本；采用数据驱动方法，面向生态与动物声音解决少样本问题。
- **来源：** 题名级候选，身份待核验

#### Few Shot Bioacoustic Detection Boosting with Finetuning Strategy Using Negative-Based Prototypical Learning

- **日期：** 日期待核验
- **问题 / 中文简述：** 少样本；采用数据驱动方法，面向生态与动物声音解决少样本问题。
- **来源：** 题名级候选，身份待核验

#### Feature extraction for sound detection of industrial parts

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展工业与机械声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Feature Selection Using Alternating Direction Method of Multiplier for Low-Complexity Acoustic Scene Classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Fast prediction of broadband and tonal noise of electronics-cooling axial fans

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### FRAUNHOFER FKIE SUBMISSION FOR TASK 5- FEW-SHOT BIOACOUSTIC EVENT DETECTION

- **日期：** 日期待核验
- **问题 / 中文简述：** 少样本；采用数据驱动方法，面向生态与动物声音解决少样本问题。
- **来源：** 题名级候选，身份待核验

#### FEW-SHOT EMBEDDING LEARNING AND EVENT FILTERING FOR BIOACOUSTIC EVENT DETECTION-Rank 1

- **日期：** 日期待核验
- **问题 / 中文简述：** 少样本；采用数据驱动方法，面向生态与动物声音解决少样本问题。
- **来源：** 题名级候选，身份待核验

#### FEW-SHOT BIOACOUSTIC EVENT DETECTION USING BEATS

- **日期：** 日期待核验
- **问题 / 中文简述：** 少样本；采用数据驱动方法，面向生态与动物声音解决少样本问题。
- **来源：** 题名级候选，身份待核验

#### FEW-SHOT BIOACOUSTIC EVENT DETECTION USING A PROTOTYPICAL NETWORK ENSEMBLE WITH ADAPTIVE EMBEDDING FUNCTIONS-Rank 3

- **日期：** 日期待核验
- **问题 / 中文简述：** 少样本；采用数据驱动方法，面向生态与动物声音解决少样本问题。
- **来源：** 题名级候选，身份待核验

#### FEW SHOT BIOACOUSTIC DETECTION BOOSTING WITH FINE TUNING STRATEGY USING NEGATIVE-BASED PROTOTYPICAL LEARNING

- **日期：** 日期待核验
- **问题 / 中文简述：** 少样本；采用数据驱动方法，面向生态与动物声音解决少样本问题。
- **来源：** 题名级候选，身份待核验

#### FEATURE FUSION BASED ON CROSS-FEATURE TRANSFORMER FOR SOUND EVENT LOCALIZATION AND DETECTION WITH SOURCE DISTANCE ESTIMATION

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用Transformer 表征，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### FAT-Net: A Spectral-Attention Transformer Network for Industrial Audio Anomaly Detection Using MFCC and Raw Features.

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展工业与机械声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### FAF-Filt- Frequency-aware Fourier Filter for Sound Event Detection

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### FA3-Net feature aggregation and augmentation with attention network for sound event localization and detection Applied Intelligence

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用Transformer 表征，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### Exploring current research trends in sound event detection a systematic literature review

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Exploring Multi-Task Learning with Weighted Soft Label Loss for Sound Event Detection with Soft Labels

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用层级与多任务学习开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Exploiting Stereo Spatial Properties with ReCoOP Framework for Joint Sound Event Detection and Localization

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### Evaluation of low-frequency feature restriction and average pooling for acoustic scene classification under unseen-city conditions

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Evaluation of Real-Time Acoustic Event Detection Models in Driving Scenarios

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Evaluation of Pitch-Shift Augmentation and Average Pooling for Acoustic Scene Classification under Unseen-City Conditions

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据增强与生成开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Evaluation of Low-Frequency Restriction, Pitch-Shift Augmentation, and Average Pooling for Acoustic Scene Classification Under Unseen-City Conditions

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据增强与生成开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Evaluation Metric of Sound Event Detection Considering Severe Misdetection by Scenes

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Evaluating few-shot prompting for spectrogram-based lung sound classification using a multimodal language model

- **日期：** 日期待核验
- **问题 / 中文简述：** 少样本 · 多模态与基础模型；采用音频语言模型，面向医疗与生理声音解决少样本问题。
- **来源：** 题名级候选，身份待核验

#### Evaluating and Interpreting Pooling Techniques in Spectrogram-Based Audio Analysis Using Diverse Metrics.

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Environmental sound classification using two-stream deep neural network with interactive time-frequency attention

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Environmental sound classification using convolutional recurrent neural network and data augmentation

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据增强与生成开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Environmental noise dataset for sound event classification and detection

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Environmental acoustic intelligence through sound event localization and detection: a review

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### Environmental Sound Classification Using a Hybrid SVM-CNN Approach

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Environmental Sound Classification Using Advanced Pooling and Hybrid Convolution-KAN Architecture

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Ensemble of Sequence Matching Networks for Dynamic Sound Event Localization, Detection, and Tracking

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### Ensemble of Pruned Low-Complexity Models for Acoustic Scene Classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Ensemble Learning with Parallel-Trained Pretrained Models for Enhanced Environmental Sound Classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Enhancing environmental sounds classification through deep learning techniques

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Enhancing conformer-based sound event detection using frequency dynamic convolutions and BEATs audio embeddings

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Enhancing Multiscale Features for Efficient Acoustic Scene Classification with One-Dimensional Separate CNN

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向环境与城市声音解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### Enhancing Environmental Sound Classification Performance through Data Fusion: A Comparative Machine Learning Analysis

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展工业与机械声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Enhancing Efficiency in CNN-Based Respiratory Sound Analysis through Temporal Self-Attention and Frequency Band Selection

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展医疗与生理声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Enhancing 3-D sound event localization and detection with distance estimation using reverberation and spatial coherence features

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### Enhanced lung disease detection using double denoising and 1D convolutional neural networks on respiratory sound analysis

- **日期：** 日期待核验
- **问题 / 中文简述：** 低信噪比；采用数据驱动方法，面向医疗与生理声音解决低信噪比问题。
- **来源：** 题名级候选，身份待核验

#### Enhanced heart sound analysis through hierarchical spectral basis vector extraction using deep orthogonal non-negative matrix factorization

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用层级与多任务学习开展医疗与生理声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Enhanced forest sound classification dataset: Efsc-24

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Enabling Accessible and Adaptable AI for Bioacoustic Monitoring from Data Annotation to Edge Deployment

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向生态与动物声音解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### Empowering our Critters: Running Energy Efficient Deep Learning Models for On-Edge Bioacoustic Monitoring

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向生态与动物声音解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### Empirical Evidence for Bioacoustic Signaling: The Bioacoustic Cultivation and Communication Protocol (BCCP) Induces Whole-System Modulation of Plant Development, Physiology, and Metabolism

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Embedded Acoustic Scene Classification for Low Power Microcontroller Devices

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向环境与城市声音解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### Efficient end-to-end audio embeddings generation for audio classification on target applications

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向声音事件解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### Efficient Evaluation Algorithms for Sound Event Detection

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向声音事件解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### Effectiveness of bird species identification using Birdnet: Case study at the La Mata coastal lagoon

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Effective Noise Suppression in Whale Bioacoustics using Transfer-Learned Stacked BiLSTM

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Edge computing for driving safety: evaluating deep learning models for cost-effective sound event detection: C. Castorena et al.

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向声音事件解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### Ecologically Valid Benchmarking and Adaptive Attention Scalable Marine Bioacoustic Monitoring

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Echoes of Nature: Harnessing AI-Powered Bioacoustic Monitoring for Enhanced Wildlife Conservation

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Early prediction of harmful environmental changes based on bioacoustics analysis

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### EPIX: Embedded PANNs-Based Intelligent Auscultation with XGBoost for Respiratory Sound Classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向医疗与生理声音解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### EFFICIENT ACOUSTIC SCENE CLASSIFICATION USING MEAN-TEACHER AND KNOWLEDGE DISTILLATION

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向环境与城市声音解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### Dynamic prompting class distribution optimization for semi-supervised sound event detection

- **日期：** 日期待核验
- **问题 / 中文简述：** 半/弱监督；采用数据驱动方法，面向声音事件解决半/弱监督问题。
- **来源：** 题名级候选，身份待核验

#### Dynacp: Dynamic parallel selective convolution in cp-mobile under multi-teacher distillation for acoustic scene classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向环境与城市声音解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### Duration-Aware Sound Event Detection on Ultra-Low-Power Sensor Devices

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### DualStack: A Multi-Resolution Spectrogram Fusion Framework for Enhanced Bird Sound Classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Dual-branch time–frequency network with channel masking for automated insect sound monitoring toward field environments

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Dual-Feature Ensemble Deep Learning Architecture for Robust Spoofing Speech Detection

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Domain‐specific neural networks improve automated bird sound recognition already with small amount of local data

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Domain-specific external data pre-training and device-aware distillation for data-efficient acoustic scene classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向环境与城市声音解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### Domain-enriched knowledge distillation for robust audio edge applications.

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向声音事件解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### Domain-aware deep learning for room acoustics: Parameter estimation, localization, and source separation

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### Domain adaptation for multi-channel acoustic scene classification to different array positions

- **日期：** 日期待核验
- **问题 / 中文简述：** 跨域泛化；采用数据驱动方法，面向环境与城市声音解决跨域泛化问题。
- **来源：** 题名级候选，身份待核验

#### Domain Adaptation of Few-Shot Bioacoustic Event Detection in Different Environments

- **日期：** 日期待核验
- **问题 / 中文简述：** 少样本 · 跨域泛化；采用数据驱动方法，面向生态与动物声音解决少样本问题。
- **来源：** 题名级候选，身份待核验

#### Disentangled prototype-guided dynamic memory replay for continual learning in acoustic signal classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 持续学习；采用对比与原型学习，面向声音事件解决持续学习问题。
- **来源：** 题名级候选，身份待核验

#### DiT-SFDA: A source-free domain adaptation method for intelligent diagnosis of cardiovascular diseases with limited heart sound samples

- **日期：** 日期待核验
- **问题 / 中文简述：** 跨域泛化；采用数据驱动方法，面向医疗与生理声音解决跨域泛化问题。
- **来源：** 题名级候选，身份待核验

#### Developing an AI-Powered Bird Sound Recognition System for Monitoring Avian Biodiversity in Belarus

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Determining the Distribution of Red Deer (Cervus elaphus L.) in the Kopački Rit Nature Park Using Bioacoustic Monitoring_1

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Determining the Distribution of Red Deer (Cervus elaphus L.) in the Kopački Rit Nature Park Using Bioacoustic Monitoring

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Detection of abnormal cardiac rhythms using feature fusion technique with heart sound spectrograms

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展医疗与生理声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Detection of Bolt Loosening Using Acoustic Emission Signal and Domain‐Generalized Machine Learning Method

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展工业与机械声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Detecting changes in air composition based on speed of sound

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Designing a Bioacoustics Gun for the Prevention of Bird Attacks in Farms, Fields & Buildings

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Design of Bird Sound Recognition Model Based on Lightweight

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向生态与动物声音解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### Description and bioacoustics of three new Eurycorypha (Orthoptera, Tettigonioidea) species from Tanzania and Ghana, with notes on their biology

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Deepfake audio detection with spectral fusion and dual-branch Conformer architecture

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Deepfake Audio Detection in Low-Resource Languages: A Case Study of Urdu

- **日期：** 日期待核验
- **问题 / 中文简述：** 少样本；采用数据驱动方法，面向声音事件解决少样本问题。
- **来源：** 题名级候选，身份待核验

#### DeepSoundVisionNet: A new approach to urban sound classification using visual representations of audio signals

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Deep learning based bird sound classification using customized convolutional neural networks

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Deep Learning-Based Acoustic Event Detection and Classification Using Cochleogram Images

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Deep Learning-Based AI-Driven Acoustic Health Monitoring for Quadrocopter Propellers

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Deep Learning Techniques for Acoustic Health Monitoring in AI-Enabled Quadrocopters. pdf

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Deep Learning Models for Acoustic Monitoring of the Himalayan Monal and Other Elusive Bird

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Debiased Training For Semi-supervised Sound Event Detection

- **日期：** 日期待核验
- **问题 / 中文简述：** 半/弱监督；采用数据驱动方法，面向声音事件解决半/弱监督问题。
- **来源：** 题名级候选，身份待核验

#### Data-efficient low-complexity acoustic scene classification via distilling and progressive pruning

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向环境与城市声音解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### Data-Efficient Low-Complexity Acoustic Scene Classification Using Parallel Attention Broadcast-Residual Network

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用Transformer 表征，面向环境与城市声音解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### Data-Efficient Acoustic Scene Classification with Pre-Training, Bayesian Ensemble Averaging, and Extensive Augmentations

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用数据增强与生成，面向环境与城市声音解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### Data Augmentation and Cross-Fusion for Audiovisual Sound Event Localization and Detection with Source Distance Estimation

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据增强与生成，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### DUAL-STRATEGY ENHANCEMENT OF ACOUSTIC SCENE AND EVENT CLASSIFICATION- INTEGRATING RES2NET, GHOSTNET, AND MOBILEFORMER ARCHITECTURES

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### DPAST-LS: A transformer-based self-distillation network for efficient recognition of abnormal pulmonary sounds

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用Transformer 表征，面向声音事件解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### DOA AND EVENT GUIDANCE SYSTEM FOR SOUND EVENT LOCALIZATION AND DETECTION WITH SOURCE DISTANCE ESTIMATION-Rank 2

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### DOA AND EVENT GUIDANCE SYSTEM FOR SOUND EVENT LOCALIZATION AND DETECTION WITH SOURCE DISTANCE ESTIMATION

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### DEW A wavelet approach of rare sound event detection

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### DETECTION OF EMERGENCY SITUATION USING DEEP LEARNING SOUND RECOGNITION METHODS

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### DATA-EFFICIENT LOW-COMPLEXITY ACOUSTIC SCENE CLASSIFICATION WITH CURRICULUM LEARNING AND SE-LAYER

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向环境与城市声音解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### DATA-EFFICIENT LOW-COMPLEXITY ACOUSTIC SCENE CLASSIFICATION USING MOBILENET VARIANT

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向环境与城市声音解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### DATA-EFFICIENT ACOUSTIC SCENE CLASSIFICATION WITH PRE-TRAINED CP-MOBILE

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向环境与城市声音解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### DATA-EFFICIENT ACOUSTIC SCENE CLASSIFICATION VIA ENSEMBLE TEACHERS DISTILLATION AND PRUNING

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向环境与城市声音解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### DATA AUGMENTATION, NEURAL NETWORKS, AND ENSEMBLE METHODS FOR SOUND EVENT LOCALIZATION AND DETECTION

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据增强与生成，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### DASSS and KineScaper: Open Python Frameworks for Physically-Grounded Synthetic Emergency Vehicle Siren Dataset Generation

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据增强与生成开展交通与水下声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Cross-Model Knowledge Distillation and Metadata Fusion for Respiratory Sound Classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向医疗与生理声音解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### Cross-Dimensional Interaction with Inverted Residual Triplet Attention for Low-Complexity Sound Event Detection

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Cosine similarity-based few-shot bioacoustic event detection with automatic frequency range identification in mel-spectrograms

- **日期：** 日期待核验
- **问题 / 中文简述：** 少样本；采用数据驱动方法，面向生态与动物声音解决少样本问题。
- **来源：** 题名级候选，身份待核验

#### Correction: Genomic and bioacoustic variation in a midwife toad hybrid zone: A role for reinforcement?

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Continuous Real-Time Acoustic Monitoring of endangered bird species in Hawai‘i

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Conformer-enhanced hybrid neural architectures for sound event detection in driving scenarios

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Conformer-Based Sound Event Detection with Semi-Supervised Learning and Data Augmentation

- **日期：** 日期待核验
- **问题 / 中文简述：** 半/弱监督；采用Transformer 表征，面向声音事件解决半/弱监督问题。
- **来源：** 题名级候选，身份待核验

#### Confidence Regularized Entropy for Polyphonic Sound Event Detection

- **日期：** 日期待核验
- **问题 / 中文简述：** 可解释与可靠性；采用数据驱动方法，面向声音事件解决可解释与可靠性问题。
- **来源：** 题名级候选，身份待核验

#### Comparative Analysis of Feature Selection Based on Metaheuristic Methods for Human Heart Sounds Classification Using PCG Signal.

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展医疗与生理声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Cognitive prototype learning: Towards self-supervised and semantic-aware few-shot open-set sound recognition

- **日期：** 日期待核验
- **问题 / 中文简述：** 少样本 · 开放集/OOD；采用自监督表征，面向声音事件解决少样本问题。
- **来源：** 题名级候选，身份待核验

#### Cochlscene: Acquisition of acoustic scene data using crowdsourcing

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### CochlScene Pre-Training and Device-Aware Distillation for Low-Complexity Acoustic Scene Classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向环境与城市声音解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### Classification of heart sound signals with Whisper model

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展医疗与生理声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Class-Aware Permutation-Invariant Signal-to-Distortion Ratio for Semantic Segmentation of Sound Scene with Same-Class Sources

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Category-guided multi-resolution fusion approach for polyphonic sound event detection

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### CNN-based bird sound detection: a comparative performance study

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### CNN Augmented Dimensionality Reduction With Neural Network Ensembles for Low Resource Data Classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### CLAP4SED Training-Free Multimodal Few-Shot Retrieval for Real-Time Sound Event Detection on Embedded Devices

- **日期：** 日期待核验
- **问题 / 中文简述：** 少样本 · 多模态与基础模型 · 轻量化部署；采用音频语言模型，面向声音事件解决少样本问题。
- **来源：** 题名级候选，身份待核验

#### CBM-net: Automatic detection and separation of cicada chorus from bee wingbeat audios

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### CAS-TJ: Channel attention shuffle and temporal jigsaw for audio classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### CAA-Net: Conditional atrous CNNs with attention for explainable device-robust acoustic scene classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 可解释与可靠性；采用Transformer 表征，面向环境与城市声音解决可解释与可靠性问题。
- **来源：** 题名级候选，身份待核验

#### Birds bats and beyond evaluating generalization in bioacoustics models

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### BirdDenoiser a bird sound denoising network based on optimized modern convolution Signal, Image and Video Processing Springer Nature Link

- **日期：** 日期待核验
- **问题 / 中文简述：** 低信噪比；采用数据驱动方法，面向生态与动物声音解决低信噪比问题。
- **来源：** 题名级候选，身份待核验

#### Bird-sound-detection-based-on-sub-band-features-and-the-p_2024_Applied-Acous

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Bird sound detection based on sub-band features and the perceptron model

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Bird sound classification based on ECOC-SVM

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Bird Sounds Recognition Based on Optoelectric Reservoir Computing

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Bioacoustics as a Tool for Data Exploration

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Bioacoustics as a Measure of Population Size and Breeding Success of European Storm Petrels Hydrobates pelagicus

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Bioacoustics and rhythm

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Bioacoustic fundamental frequency estimation: a cross-species dataset and deep learning baseline

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Bioacoustic detection of four Bruchid species in bulk red and green bulk-stored beans

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Bioacoustic assessment of mangrove health: Influence of habitat characteristics on bird richness

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### BioSoundSCape A bioacoustic dataset for the Fynbos Biome

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Bio-acoustic Design Principles Through the Integration of Sound, Nature and Multisensory Features into Bio-Architecture

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Big data, sound science, lasting impact: a framework for passive acoustic monitoring

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Bi-level acoustic scene classification using lightweight deep learning model

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向环境与城市声音解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### Benchmarking self-supervised audio representations for iot-enabled acoustic beehive monitoring

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用自监督表征开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Auxiliary Decoder-Based Learning of Sound Event Detection using Multi-Channel Features and Maximum Probability Aggregation

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Automatic synthesis of insects bioacoustics using machine learning a systematic review

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Automatic detection for bioacoustic research: a practical guide from and for biologists and computer scientists

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Automatic and Efficient Sound-Based Early Fault Detection for Vehicles based on GCN-A and LSTM Model

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向工业与机械声音解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### Automatic Recognition of Pelung and Canary Bird Sounds Using Machine Learning and Signal Enhancement

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Automatic Animal Specie Identification Using Bioacoustics Characterization and Modeling

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Automated note annotation after bioacoustic classification- Unsupervised clustering of extracted acoustic features improves detection of a cryptic owl

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Automated classification of humpback whale calls in four regions using convolutional neural networks and multi scale deep feature aggregation (MSDFA)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Automated call detection in big cats: a non-invasive bioacoustic tool for conservation

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Automated bird sound classifications of long-duration recordings produce occupancy model outputs similar to manually annotated data

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Automated Audio Data Augmentation Network Using Bi-Level Optimization for Sound Event Localization and Detection

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据增强与生成，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### Audiosignal based event detection using deep learning techniques

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Audio-Visual Fusion Framework for Low-Resource Language Speech Recognition Based on Progressive Down-Sampling and Grouped Multi-Heads Attention Mechanism

- **日期：** 日期待核验
- **问题 / 中文简述：** 少样本；采用Transformer 表征，面向声音事件解决少样本问题。
- **来源：** 题名级候选，身份待核验

#### Audio Tag Representation Guided Dual Attention Network for Acoustic Scene Classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Assessing the Effective Range for Individual Acoustic Identification: Comparison of Manual and Automatic Methods

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Artificial intelligence-powered environmental sound recognition with explainable AI techniques

- **日期：** 日期待核验
- **问题 / 中文简述：** 可解释与可靠性；采用数据驱动方法，面向环境与城市声音解决可解释与可靠性问题。
- **来源：** 题名级候选，身份待核验

#### Are nonlinear vocal phenomena as distracting as people think?

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### ArcticSoundsNET- BirdNET embeddings facilitate improved bioacoustic classification of Arctic species

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Anuran call synthesis with diffusion models for enhanced bioacoustic classification under data scarcity

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据增强与生成开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Anomaly detection in induction motors through irregular sound and vibrations

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展工业与机械声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Annoyance penalty of impulsive noise–the effect of impulse onset

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Analyzing the Effect of Equal-Angle Spatial Discretization on Sound Event Localization and Detection

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### Analytical model for predicting rotor-stator interaction tonal noise in low-speed axial fans

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### An insight into the bioacoustics of some anurans of Meghalaya, India (Amphibia: Anura)

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### An attention-based time-frequency pyramid pooling strategy in deep convolutional networks for acoustic scene classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### An Intelligent Audio Recognition Model for Gunshot and Forest Animal Sound Classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### An Abnormal Audio Generation Method for Fault Diagnosis of Power Transformers

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展工业与机械声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Aeroacoustics analysis of radiator installation effects in a pulling engine cooling module

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Adversarial attacks and robustness in deep neural networks for sound event detection

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Advancing bioacoustic monitoring: implementing acoustic indices and sonotyping methods in artificial ecosystems with IoT–integrated data dashboards

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Advancing Environmental Surveillance- A Comprehensive Review of Sound Event Classification Techniques and Applications

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Advances in fault detection techniques for automated manufacturing systems in industry 4.0

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展工业与机械声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Advances and challenges in respiratory sound analysis: A technique review based on the icbhi2017 database

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展医疗与生理声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Advancements in environmental sound classification: Evaluating machine learning and deep learning approaches on the UrbanSound8k

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展工业与机械声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Advancements in audio and audiovisual sound event localization and detection with source distance estimation: A survey

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### Advanced prompt engineering techniques for generative sound synthesis models

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据增强与生成开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Advanced Signal Decomposition Techniques for Vibration Diagnostics in Mechanical Systems: A Fourier-Based Approach

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展工业与机械声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Adaptive hierarchical pooling for weakly-supervised sound event detection

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用层级与多任务学习开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Adaptive depth-wise pruning for efficient environmental sound classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向环境与城市声音解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### Adaptive Vehicle Speed Classification via Multi-feature CNN with Reinforcement Learning-Enhanced Acoustic Processing

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展交通与水下声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Adaptive Fine-Grained Pruning via Binary Search for Efficient Environmental Sound Classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向环境与城市声音解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### Adapting Single-Channel Pre-trained Transformer Models for Multi-Channel Sound Event Localization and Detection

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用Transformer 表征，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### Active learning for sound event classification using Bayesian neural networks with Gaussian variational posterior

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Active Learning for Sound Event Classification using Monte-Carlo Dropout and PANN Embeddings

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Acoustics based condition monitoring of industrial machines using deep learning

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展工业与机械声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Acoustic scene classification using dynamic time warping technique based on short time Fourier transform and discrete wavelet transforms

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Acoustic scene classification using deep residual networks with focal loss and mild domain adaptation

- **日期：** 日期待核验
- **问题 / 中文简述：** 跨域泛化；采用数据驱动方法，面向环境与城市声音解决跨域泛化问题。
- **来源：** 题名级候选，身份待核验

#### Acoustic scene classification A comprehensive survey

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Acoustic process monitoring during projection welding using airborne sound analysis and machine learning

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展工业与机械声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Acoustic Scene Classification Across Multiple Devices Through Incremental Learning of Device-Specific Domains

- **日期：** 日期待核验
- **问题 / 中文简述：** 持续学习；采用数据驱动方法，面向环境与城市声音解决持续学习问题。
- **来源：** 题名级候选，身份待核验

#### Acoustic Scene Classification Across Cities and Devices via Feature Disentanglement

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Acoustic Machine Learning Tools and Analysis Software for Advancing Biodiversity Monitoring

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Acoustic Analysis of Fish Tanks for Marine Bioacoustics Research

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### Abnormal heart sound recognition using SVM and LSTM models in real-time mode

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展医疗与生理声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### AUDIO-VISUAL SOUND EVENT LOCALIZATION AND DETECTIONBASEDONCRNNUSING DEPTH-WISE SEPARABLE CONVOLUTION

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### ATTENTION MECHANISM NETWORK AND DATA AUGMENTATIONFOR SOUND EVENT LOCALIZATION AND DETECTION-Rank 2

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用Transformer 表征，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### ATTENTION MECHANISM NETWORK AND DATA AUGMENTATIONFOR SOUND EVENT LOCALIZATION AND DETECTION

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用Transformer 表征，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### ASiT-CRNN A method for sound event detection with fine-tuning of self-supervised pre-trained ASiT-based model

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用自监督表征开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### APPLICATION OF SPECTRO-TEMPORAL RECEPTIVE FIELD ON SOFT LABELED SOUND EVENT DETECTION

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### AMResNet- An automatic recognition model of bird sounds in real environment

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### AI-driven bioacoustics in poultry farming: A critical systematic review on vocalization analysis for stress and disease detection

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### AFDS-Net: An Attention-Fused Depthwise Separable Network for Acoustic Scene Classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### ACOUSTIC SCENE CLASSIFICATION USING CONVOLUTION NEURAL NETWORK WITH LIMITED DATA

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### ACOUSTIC SCENE CLASSIFICATION BASED ON PRUNED_ GHOSTNET AND FHR_MOBILENET

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### ACOUSTIC SCENE CLASSIFICATION BASED ON MULTI-TEACHER KNOWLEDGE DISTILLATION AND SERFR-CNN

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向环境与城市声音解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### A trio-based feature extraction framework for bird sounds classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### A topic-specific representation learning framework for acoustic scene classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### A survey on preprocessing and classification techniques for acoustic scene

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### A squeeze-and-excitation and transformer-based cross-task model for environmental sound recognition

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### A spatio-temporal graph neural network with masked self-supervision for precise anomaly severity measurement of vibrating screens in mineral processing

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### A semi-supervised underwater acoustic target recognition method based on domain adversarial neural networks

- **日期：** 日期待核验
- **问题 / 中文简述：** 半/弱监督；采用数据驱动方法，面向交通与水下声音解决半/弱监督问题。
- **来源：** 题名级候选，身份待核验

#### A safety-oriented framework for sound event detection in driving scenarios

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### A review of sound-based pig monitoring for enhanced precision production

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### A real-time bird sound recognition app via deep learning techniques

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### A parametric survey on polyphonic sound event detection and localization Multimedia Tools and Applications

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### A novel deep learning‐based bioacoustic approach for identification of look‐alike white‐eye (Zosterops) species traded in wildlife markets

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### A method for heart sound classification using sample augmentation and INDANet

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据增强与生成开展医疗与生理声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### A lightweight hybrid machine and deep learning framework via contrastive learning for audio-based multiclass vehicle counting

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用对比与原型学习，面向工业与机械声音解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### A lightweight dual branch masking network for environmental sound classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向环境与城市声音解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### A lightweight deep learning architecture for automatic shrimp disease classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向声音事件解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### A hybrid deep learning framework for acoustic pest detection

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### A genetic algorithm approach to automate architecture design for acoustic scene classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### A dynamic cross-modal learning framework for joint text-to-audio grounding and acoustic scene classification in smart city environments

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### A distributed training framework for abnormal sound detection in industrial devices: Aggregation strategies and performance analysis

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展工业与机械声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### A deep-learning approach to heart sound classification based on combined time-frequency representations

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展医疗与生理声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### A comparative study of preprocessing and model compression techniques in deep learning for forest sound classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用数据驱动方法，面向声音事件解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### A Three-Level Evaluation Protocol for Acoustic Scene Understanding of Large Language Audio Models

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### A Survey on Intelligent Sound Event Detection Systems for Public Safety and Emergency Response

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### A Survey of Audio Enhancement Algorithms for Music, Speech, Bioacoustics, Biomedical, Industrial, and Environmental Sounds by Image U-Net

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### A Study of Improved Two-Stage Dual-Conv Coordinate Attention Model for Sound Event Detection and Localization

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用Transformer 表征，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### A Semi-Supervised Acoustic Scene Classification Network Based on Multi-Modal Information Fusion

- **日期：** 日期待核验
- **问题 / 中文简述：** 半/弱监督；采用数据驱动方法，面向环境与城市声音解决半/弱监督问题。
- **来源：** 题名级候选，身份待核验

#### A Scalable AI Architecture for Audio and Multimodal Analysis on Mobile Devices: A Case of Environmental Monitoring

- **日期：** 日期待核验
- **问题 / 中文简述：** 多模态与基础模型；采用数据驱动方法，面向声音事件解决多模态与基础模型问题。
- **来源：** 题名级候选，身份待核验

#### A Review of Deep Learning Based Methods for Acoustic Scene Classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### A Novel Bird Sound Recognition Method Based on Multifeature Fusion and a Transformer Encoder

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用Transformer 表征开展生态与动物声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### A Novel Approach for Detecting Sound Events in Smart Home Systems Using Diffusion-Based Convolutional Recurrent Neural Network

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据增强与生成开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### A Methodology for Real-Time Audio Event Detection and Generation Using Spectral Flux Analysis

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### A Lightweight Temporal Attention Module for Frequency Dynamic Sound Event Detection

- **日期：** 日期待核验
- **问题 / 中文简述：** 轻量化部署；采用Transformer 表征，面向声音事件解决轻量化部署问题。
- **来源：** 题名级候选，身份待核验

#### A Lightweight Approach for Semi-Supervised Sound Event Detection with Unsupervised Data Augmentation

- **日期：** 日期待核验
- **问题 / 中文简述：** 半/弱监督 · 轻量化部署；采用数据增强与生成，面向声音事件解决半/弱监督问题。
- **来源：** 题名级候选，身份待核验

#### A Human-Expert Approach to Validating Attribution for AI-Generated Audio

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### A Framework of Interaction Between Machine, Experts and Crowd Towards the Generation of Large-Scale, High-Quality Audio Datasets

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展工业与机械声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### A Dual Consistency Training (DCT) strategy for polyphonic sound event detection

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### A Device Classification-Aided Multi-Task Framework for Low-Complexity Acoustic Scene Classification

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用层级与多任务学习开展环境与城市声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### A DOMAIN ADAPTIVE ACOUSTIC SCENE CLASSIFICATION MODEL IN SEMI-SUPERVISED TRANSFER LEARNING.

- **日期：** 日期待核验
- **问题 / 中文简述：** 半/弱监督；采用数据驱动方法，面向环境与城市声音解决半/弱监督问题。
- **来源：** 题名级候选，身份待核验

#### A DATA GENERATION METHOD FOR SOUND EVENT LOCALIZATION AND DETECTION IN REAL SPATIAL SOUND SCENES-Rank 3

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### A DATA GENERATION METHOD FOR SOUND EVENT LOCALIZATION AND DETECTION IN REAL SPATIAL SOUND SCENES

- **日期：** 日期待核验
- **问题 / 中文简述：** 定位与分离；采用数据驱动方法，面向声音事件解决定位与分离问题。
- **来源：** 题名级候选，身份待核验

#### A Comprehensive Review of Polyphonic Sound Event Detection

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展声音事件检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

#### A COMPARATIVE ANALYSIS OF INTERIOR VS. EXTERIOR VEHICLE MICROPHONE PLACEMENT FOR ACOUSTIC EVENT DETECTION IN DRIVING ENVIRONMENTS

- **日期：** 日期待核验
- **问题 / 中文简述：** 通用检测与分类；采用数据驱动方法开展交通与水下声音检测、分类或表征研究。
- **来源：** 题名级候选，身份待核验

</details>

### 论文索引与筛选入口

- [交互专题页：按问题、年份和技术趋势筛选](../../portal/topic.html?topic=sed#details)
- [arXiv cs.SD 2025-01-01—2026-11-03 相关论文初筛](arxiv-cs-sd-2025-2026.md)
- [通用 SED 方法与未细分候选](methods/README.md)

---
## 评估与维护约定

- 检测任务优先报告 event-based F1、PSDS、事件边界误差和检测延迟。
- 长尾任务同时报告头部、中部与尾部类别；跨域任务按设备、地点或项目分别报告。
- 涉及未知类别时，区分闭集分类准确率、OOD 检测能力与置信度校准。
- 自动关键词归类是候选关系；引用论文结论前仍需核对摘要、全文和实验条件。
- 新论文先写入统一索引，再关联多个方向与问题，避免复制出多个不一致记录。
- 新增论文后运行 `python3 scripts/generate_sound_event_readme.py`，即可按年份重新生成本页完整论文目录。

[DCASE](https://dcase.community/) · [AudioSet](https://research.google.com/audioset/) · [返回仓库首页](../../README.md)
