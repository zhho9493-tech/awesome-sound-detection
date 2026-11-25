# 2026-11-24 cs.SD 每日增量

公告日期：2026-11-24；筛选日期：2026-11-25。[公告](https://arxiv.org/list/cs.SD/recent)。以下基于原文摘要，未独立复现；工业/DAS迁移均为研究假设。

## Spoof Localization as Boundary Regression

- 作者：Yixuan Xiao, Xin Wang, Yassine El Kheir, Feidi Kallel, Arnab Das, Tim Polzehl, Sebastian Möller, Ngoc Thang Vu
- 首次提交：2026-11-21（UTC）
- [arXiv](https://arxiv.org/abs/2611.29085) · [PDF](https://arxiv.org/pdf/2611.29085) · [DOI](https://doi.org/10.48550/arXiv.2611.29085)
- 方法及证据：单阶段连续起止时间及置信度回归替代固定帧分类；作者报告定位和泛化改善，具体数据集及数值待全文复核。
- 工业声学/DAS迁移假设：用于10秒片段内异常区间定位，比较事件mIoU、边界误差与弱异常召回。
- 复现状态：代码未核实；未独立复现。

## Training speech deepfake detectors against worst-case filters: Gains, Costs and Limits

- 作者：Ali Alavi
- 首次提交：2026-11-21（UTC）
- [arXiv](https://arxiv.org/abs/2611.28718) · [PDF](https://arxiv.org/pdf/2611.28718) · [DOI](https://doi.org/10.48550/arXiv.2611.28718)
- 方法及证据：训练中优化最坏情况短滤波器而非仅随机滤波；作者报告真实录音滤波鲁棒性改善，但干净音频错误增加，独立伪造系统验证选点也能获得近似鲁棒性。具体指标待全文复核。
- 工业声学/DAS迁移假设：模拟物理合理的传感器频响变化，比较随机增强、最坏条件训练及独立项目选点；检查异常频谱保真。
- 复现状态：代码未核实；未独立复现。
