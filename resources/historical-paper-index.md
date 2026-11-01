# Historical Paper Index / 历史论文总索引

本页用于把仓库中已经整理过的历史论文、近期重点论文和跨领域可迁移论文串成一个长期维护入口。  
原则：**不重复复制同一篇论文**，优先链接到各方向现有索引；只有需要跨领域强调的方法才在这里做“重点条目”。

## 1. 声学异常检测 / Industrial ASD

- [声学异常检测主入口](../papers/acoustic-anomaly/README.md)
- [Google Drive 已收藏论文初步归类](../papers/acoustic-anomaly/drive-library-index.md)
- 后续重点：DCASE、跨项目泛化、Noise-aware、标签噪声、开放集、异常强度/状态演化。

## 2. 声音事件检测与声音分类

- [声音事件检测主入口](../papers/sound-event/README.md)
- [近一年 arXiv 声音分类精选（2025-2026）](../papers/sound-event/arxiv-sound-classification-2025-2026.md)
- [Google Drive 已收藏论文初步归类](../papers/sound-event/drive-library-index.md)

## 3. DAS / 分布式光纤声学

- [DAS 主入口](../domains/das/README.md)
- [近一年 arXiv DAS 精选（2025-2026）](../domains/das/arxiv-2025-2026.md)
- [Google Drive DAS 历史论文索引](../domains/das/drive-library-index.md)
- [DAS 皮带机企业/项目动态时间线](../industry/das-conveyor-timeline.md)

### 2026 年与皮带机最相关的公开论文

1. **Research on intelligent inspection system for belt conveyor in bulk cargo terminal based on distributed optical fiber sensing**  
   中文题名：基于分布式光纤传感的散货码头带式输送机智能巡检系统  
   来源：重型机械，2026(1):98-105  
   DOI: 10.13551/j.cnki.zxjxqk.2026.01.013  
   链接：https://www.chinamet.cn/zxjx/article/doi/10.13551/j.cnki.zxjxqk.2026.01.013  
   价值：DAS + DTS、全线连续监测、面向散货码头皮带机的工程化架构。

2. **Conveyor Monitoring Through Fiber Optic Cables—Reducing Downtime, Increasing Safety and Improving Preventative Maintenance**  
   来源：SME Annual Meeting 2026  
   链接：https://www.onemine.org/documents/conveyor-monitoring-through-fiber-optic-cables-reducing-downtime-increasing-safety-and-improving-preventative-maintenance-sme-annual-meeting-2026  
   价值：总结矿山/散料输送机光纤监测的部署条件、安装方法、建模、现场限制与商业化经验。

## 4. 泄漏检测

- [水管/气体泄漏主入口](../domains/leakage/README.md)
- [Google Drive 泄漏方向历史论文 Round 3](../domains/leakage/drive-library-round3.md)
- [Google Drive 泄漏方向历史论文 Round 4](../domains/leakage/drive-library-round4.md)

## 5. 声纹识别

- [声纹识别主入口](../related/speaker-recognition/README.md)
- [近一年 arXiv 声纹识别（2025-2026）](../related/speaker-recognition/arxiv-2025-2026.md)
- [Google Drive 历史论文索引](../related/speaker-recognition/drive-library-index.md)

重点迁移价值：Embedding 学习、ArcFace/Sub-center 类间边界、域适应、开放集识别、少样本新增类别。

## 6. 人脸识别 / Metric Learning

- [人脸识别主入口](../related/face-recognition/README.md)
- 重点：ArcFace、Sub-center ArcFace、噪声标签、类别增量学习、Embedding 分类器。

## 7. 图像异常检测

- [图像异常检测主入口](../related/visual-anomaly/README.md)
- [Google Drive 历史论文索引](../related/visual-anomaly/drive-library-index.md)

重点迁移价值：PatchCore/PaDiM 式记忆库、位置级异常、检索增强、视觉基础模型迁移到声学异常检测。

## 8. 基础模型 / 多模态 / 大模型

- [Foundation Models 主入口](../related/foundation-models/README.md)
- [Google Drive 历史论文索引](../related/foundation-models/drive-library-index.md)

### 重点跨领域论文

- **AnomSeer: Reinforcing Multimodal LLMs to Reason for Time-Series Anomaly Detection**  
  ICML 2026 / PMLR 306  
  论文：https://proceedings.mlr.press/v306/zhang26aw.html  
  PDF：https://raw.githubusercontent.com/mlresearch/v306/main/assets/zhang26aw/zhang26aw.pdf  
  代码：https://github.com/jrzhang33/AnomSeer  
  迁移价值：将 FFT、统计量、Matrix Profile 等传统异常证据组织为可验证推理轨迹，再用强化学习训练 MLLM 做异常分类、定位与解释。

- **A physics-informed recurrent neural network for long sequence remaining useful life prediction of rolling bearing with implicit function**  
  Reliability Engineering & System Safety, 2026, Vol.274, 112412  
  DOI: 10.1016/j.ress.2026.112412  
  链接：https://www.sciencedirect.com/science/article/pii/S0951832026002280  
  迁移价值：VRNN + implicit function solver，将未知/不完整物理机理以隐式函数方式嵌入 RUL 预测，适合借鉴到托辊健康演化、强度分级和早中晚期状态预测。

## 9. 跨领域迁移索引

- [跨领域技术矩阵](../cross-domain/transfer-matrix.md)
- [Google Drive 跨领域历史论文索引](../cross-domain/drive-library-index.md)

建议优先迁移到工业声学/DAS的技术：
1. 自监督预训练与基础模型；
2. Prototype / Sub-center / Metric Learning；
3. Memory Bank / Retrieval；
4. Noise-aware / 标签质量建模；
5. Domain Generalization / Test-time Adaptation；
6. Physics-informed / Health-state / RUL；
7. Multimodal LLM reasoning / Agentic diagnosis。

## 10. 统一网盘论文总索引

- [Google Drive 统一扫描索引](drive-unified-scanned-index.md)

该索引已做标题级归一化，适合作为后续“补 DOI / 补公开下载 / 去重 / 自动分类”的母表。
