# 2026-11-25 cs.SD 每日增量

公告日期：2026-11-25；筛选日期：2026-11-26。[公告](https://arxiv.org/list/cs.SD/recent)。依据原文摘要，迁移均为研究假设。

## Do Layer Rankings Survive Silence Trimming? The Silence Shortcut in Frozen WavLM Representations for Audio Deepfake Detection

- 作者：Nur Elabid, Mahmud Esad Arar
- 首次提交：2026-11-24（UTC）
- [arXiv](https://arxiv.org/abs/2611.32457) · [PDF](https://arxiv.org/pdf/2611.32457) · [DOI](https://doi.org/10.48550/arXiv.2611.32457)
- 方法及证据：冻结 WavLM Base 12 层探针，在 ASVspoof 2019 LA 与 In-the-Wild 比较训练/测试静音裁剪组合。仅测试端40 dB裁剪使 EER 增加6.3–19.9个百分点；域内层排序 Kendall tau=0.58。零填充经 group normalization 影响特征，attention mask 无法完全消除。
- 工业声学/DAS迁移假设：对 DAS 运行/停机比例、片段边界及补零做反事实消融，避免把非目标静音差异当成故障证据。
- 复现状态：arXiv 原文提供代码及结果表链接，未独立复现。
