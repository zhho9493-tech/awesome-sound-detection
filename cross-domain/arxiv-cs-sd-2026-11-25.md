# 2026-11-25 cs.SD 每日增量

公告日期：2026-11-25；筛选日期：2026-11-26。[公告](https://arxiv.org/list/cs.SD/recent)。依据原文摘要，迁移均为研究假设。

## IncrementDET: Continual AI-Generated Music Detection via Enrollment

- 作者：Runbao Du, Wei Li, Qile He
- 首次提交：2026-11-24（UTC）
- [arXiv](https://arxiv.org/abs/2611.32023) · [PDF](https://arxiv.org/pdf/2611.32023) · [DOI](https://doi.org/10.48550/arXiv.2611.32023)
- 方法及证据：每个生成器独立训练线性分类头，共用固定真人参考集，新增头不修改旧头；Sidak 校正控制整体误报。EvoMusicFake-17K 六个生成器、四个人类音乐平台，作者报告少样本更新及旧类保持优于 SpecTTTra。
- 工业声学/DAS迁移假设：新增干扰类型或故障类型时尝试独立注册分类头；需验证相关头下整体误报校准、未知故障拒识及旧类召回。
- 复现状态：代码未核实；未独立复现。

## ClusterVAD: Threshold-Free Unsupervised Voice Activity Detection with Pre-Trained Neural Representations

- 作者：Karl El Hajal, Mathew Magimai.-Doss
- 首次提交：2026-11-24（UTC）
- [arXiv](https://arxiv.org/abs/2611.33059) · [PDF](https://arxiv.org/pdf/2611.33059) · [DOI](https://doi.org/10.48550/arXiv.2611.33059)
- 方法及证据：冻结语音底座特征聚类，以 sonority 标记语音/非语音簇，逐录音拟合双状态 HMM，避免固定检测阈值；作者报告多种会议、远场、噪声及非典型语音基准上停顿级检测误差最低。
- 工业声学/DAS迁移假设：尝试以工业声学属性标记运行/停机簇，逐探测器拟合状态模型；需验证混合片段、短时状态及弱异常保真。
- 复现状态：代码未核实；未独立复现。
