# arXiv cs.SD 2026-11-16 公告｜开放说话人流式聚类

## eDIAR: Training-Free Open-Speaker Streaming Diarization for Long Meetings and Large Archives via e-means

- **作者**：Kyudan Jung; Jihwan Kim; Minwoo Lee; Eunji Shin; Jaegul Choo
- **首次提交**：2026-11-13；**arXiv**：https://arxiv.org/abs/2611.18529；**PDF**：https://arxiv.org/pdf/2611.18529
- **方法**：固定槽位神经说话人分离头负责流式活动/重叠判断，槽位耗尽后用 e-means 对单槽内 speaker embedding 再聚类；仅在有界时间窗内重聚类并短期修正身份，避免输出说话人数被槽位上限限制。
- **数据/指标**：长会议流式 diarization、超槽位说话人、百万级 embedding 聚类；作者报告相对固定槽位系统更稳健且增量计算开销不随会议长度增长。
- **代码/复现**：论文提供项目演示页 https://kyudan1.github.io/ ，未确认完整官方训练/推理代码，未独立复现。
- **工业声学/DAS 迁移（研究假设）**：固定异常类型/探测器分类头与开放世界 embedding 聚类解耦，允许发现新增异音模式；研究有界窗口在线更新、身份漂移和错误聚类污染。说话人身份不等于托辊设备身份，不能外推效果。

## 技术判断
强化“固定分类头 → 开放身份/原型库增量扩展”的在线聚类路线；任务设定与工业异常新类别发现有潜在关联，但尚未验证。
