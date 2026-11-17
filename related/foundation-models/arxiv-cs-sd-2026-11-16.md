# arXiv cs.SD 2026-11-16 公告｜基础模型与可解释音频评估

> 以下论文首次提交于 2026-11-13；工业声学/DAS 价值仅为研究假设，尚未现场复现。

## 1. CoTTAGE: An Explainable Judge for Text-to-Audio Generation
- **作者**：Yu-Xiang Lin; Yun-Man Hsu; Bo-Ru Lu; Kuan-Po Huang; Wenze Ren; Ming-To Chuang; Chun-Yi Kuan; Jiawei Du; Byeonggeun Kim; Qingming Tang; Chieh-Chi Kao; Ankur Gandhe; Chao Wang; Hung-yi Lee
- **首次提交**：2026-11-13；**arXiv**：https://arxiv.org/abs/2611.17644；**PDF**：https://arxiv.org/pdf/2611.17644
- **方法**：面向文本生成音频的相关性和整体音质评估，采用先给出声学依据再预测分数（reason-then-predict）；以逾万条人工音质标注监督微调，再以 Thurstone 偏好概率和强化学习优化排序。作者报告六个基准上的人类评分相关性提升。
- **数据/指标**：TTA 质量/文本一致性，六个基准；并非工业异常检测基准。
- **代码/复现**：arXiv 摘要未提供官方代码仓库；未独立复现。
- **工业声学/DAS 迁移（研究假设）**：可借鉴“证据解释先于分数”构建托辊异常复核质量评估器，结合人工听感一致性与可追溯声学证据；不能直接使用 TTA 音质指标作为故障检测准确率。

## 2. Any Channel Count, One Token Stream: Incorporating Spatial Audio Understanding and Reasoning into Large Audio-Language Models
- **作者**：Yuhuan You; Wenxiang Guo; Zhifang Guo; Yuxuan Wang; Jin Xu
- **首次提交**：2026-11-13；**arXiv**：https://arxiv.org/abs/2611.18112；**PDF**：https://arxiv.org/pdf/2611.18112
- **模型/方法**：SpheraAudio 用多通道复频谱编码空间 token，与音频 token 在时间轴交错；Spatial Multimodal RoPE 保留模态及时间槽；经空间编码器预训练、投影对齐、监督及强化学习三阶段训练，输出空间推理步骤。
- **数据/指标**：SpheraQA，实验版本 20,492 问，公开版本 22,197 问；覆盖单声源属性、多声源关系及多步空间推理。作者报告多个空间音频基准表现提升。
- **代码/复现**：arXiv 论文页已列代码与 ModelScope 数据集入口；尚未独立运行验证。
- **工业声学/DAS 迁移（研究假设）**：探索变探测器数量下的空间/时间 token 融合、相邻位置事件一致性、故障定位推理。空气声阵列相位关系与沿线 DAS 耦合/传播机制不同，不能直接迁移定位精度。

## 技术判断
SpheraAudio 将“任意通道数 + 显式空间推理”作为新任务设定，值得更新空间基础模型技术时间线；CoTTAGE 属于可解释评估路线的强化。均未验证 DAS 托辊场景。
