# arXiv cs.SD 2026-11-17 公告｜跨域鲁棒性与多模态噪声

> 2026-11-17 cs.SD 公告包含交叉列表；首次提交日期与公告日期可能不同。工业声学/DAS迁移价值均为**研究假设**。

## 1. Attribution-Guided Shared-Private Decoupling for Noise-Reduced Audio-Visual Representation Learning

- **作者**：Linge Wang, Yingying Chen, Bingke Zhu, Lu Zhou, Haixin Wang, Zhipiao Liu, Jinqiao Wang
- **首次提交**：2026-11-14；**arXiv**：[2611.19236](https://arxiv.org/abs/2611.19236)；**PDF**：[下载](https://arxiv.org/pdf/2611.19236)；**DOI**：10.48550/arXiv.2611.19236
- **任务/方法**：音视频表征学习；使用截断层归因（LTA）识别可靠共享语义子视图，以教师学生监督分离跨模态共享信息和模态私有残差，减少无关 token 的语义噪声；学生推理不额外增加归因计算。
- **原论文评价**：作者报告音视频检索、分类和声提示语义分割收益；与DAS无直接实验关系。
- **工业声学/DAS迁移（研究假设）**：多模态DAS+可见光/设备日志融合时区分共享故障证据与传感器私有噪声；对单模态DAS不能直接套用音视频共享语义假设。
- **代码/复现**：[官方仓库](https://github.com/wanglg20/LTA) 当前仅 README，标示计划 2026-12-05 开源，**尚未公开可复现代码**。

## 2. Winning the Leaderboard, Losing the Distribution: Diagnosing and Mitigating Acoustic Narrowing in Low-Resource ASR

- **作者**：Kadir Goksel Gunduz
- **首次提交**：2026-10-16；**2026-11-17 进入 cs.SD 交叉列表**；**arXiv**：[2611.18653](https://arxiv.org/abs/2611.18653)；**PDF**：[下载](https://arxiv.org/pdf/2611.18653)；**DOI**：10.48550/arXiv.2611.18653
- **任务/方法**：低资源 ASR 跨分布评估；提出“acoustic narrowing”现象，即特定数据源微调在同源榜单提升却收缩模型在外部分布的声学覆盖；以独立来源测试集与多条件鲁棒性评价识别，探索数据混合与基座参照模型选择。
- **原论文评价**：在土耳其语ASR跨条件测试中观察到模型排名逆转，且不同架构的微调表现不同；属于ASR证据，不能直接视作工业异常检测结论。
- **工业声学/DAS迁移（研究假设）**：为跨项目精度下降提供评估设计：同源validation不能替代项目外测试，保留冻结基座与历史模型作参照；比较跨项目低FPR pAUC、设备级召回与域内提升是否互相牺牲。
- **代码/复现**：论文声明公开代码、逐句预测与事实记录，参见 [论文页](https://arxiv.org/abs/2611.18653) 的官方代码链接；未执行复现。

## 技术判断

- **时间线（2026-11）**：跨域鲁棒性从单一同源榜单扩展为**独立来源多条件检验和模型选择偏差诊断**；多模态学习从全token对齐走向**共享/私有证据归因解耦**。
- **技术趋势**：加强“仅优化源域精度 → 监控域外声学覆盖”和“全局跨模态对齐 → 选择性可信语义对齐”，尚不推断DAS实际增益。
- **当前判断/待关注**：DAS项目外固定测试集、分项目验证集、基座参照与异常保真检查；多模态融合须对照单模态基线和模态缺失/冲突场景。
