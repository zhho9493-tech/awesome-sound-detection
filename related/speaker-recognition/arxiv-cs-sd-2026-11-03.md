# arXiv cs.SD 每日增量｜2026-11-03 公告

来源：https://arxiv.org/list/cs.SD/new （2026-11-03 公告）；本页已与现有年度索引进行 ID 去重后按相关性筛选，包含 cs.SD new submissions 和 cross-lists。日期为公告日期，**不是全部论文的首次提交日期**；arXiv ID 前缀 2611 仅代表 2026-11。以下首次提交的精确日期尚待逐篇版本元数据复核。条目均未在工业DAS场景复现。

| arXiv | 论文 | 作者 | 技术类别 | 首次提交日期 | 官方PDF | 代码/复现 |
|---|---|---|---|---|---|---|
| [2611.00894](https://arxiv.org/abs/2611.00894) | Microphone Geometry Aware Regional Target Speaker Extraction | Shitong Xu; Niki Trigoni; Andrew Markham | geometry-aware multichannel extraction | 待核验（2026-11 公告） | [PDF](https://arxiv.org/pdf/2611.00894) | 官方代码待核验；未复现 |
| [2611.01757](https://arxiv.org/abs/2611.01757) | Spatially-Guided Speaker Extraction Based on Relative Position Cues | Aviad Eisenberg; Shlomo E. Chazan; Sharon Gannot | relative spatial cue extraction | 待核验（2026-11 公告） | [PDF](https://arxiv.org/pdf/2611.01757) | 官方代码待核验；未复现 |
| [2611.02628](https://arxiv.org/abs/2611.02628) | ReplayFactor: Replay-Aware Dual-Attribute Learning for Practical Speech Deepfake Detection | Miao He; Jiayi Zhou; Yu Zheng; Zhongjie Ba; Peng Cheng; Yuxi Zhou; Junjie Zhu; Changhao Zhang; Jian Liu | open-set robustness / SSL and acoustic priors | 待核验（2026-11 公告） | [PDF](https://arxiv.org/pdf/2611.02628) | 官方代码待核验；未复现 |

## 方法摘要及工业声学/DAS迁移假设

### 1. Microphone Geometry Aware Regional Target Speaker Extraction

- **arXiv**: https://arxiv.org/abs/2611.00894
- **PDF**: https://arxiv.org/pdf/2611.00894
- **作者**: Shitong Xu; Niki Trigoni; Andrew Markham
- **技术类别**: geometry-aware multichannel extraction
- **论文摘要层面的贡献**: Attention-based multichannel front end encodes inter-microphone phase with spatial reconstruction auxiliary objective, generalizing to variable microphone geometries and counts.
- **潜在迁移（未经验证）**: 借鉴跨通道/探测器几何感知编码；但空气麦克风阵列与DAS光纤的相位物理不同，需重新验证。
- **代码/复现状态**: 未核验官方代码；尚未复现。


### 3. Spatially-Guided Speaker Extraction Based on Relative Position Cues

- **arXiv**: https://arxiv.org/abs/2611.01757
- **PDF**: https://arxiv.org/pdf/2611.01757
- **作者**: Aviad Eisenberg; Shlomo E. Chazan; Sharon Gannot
- **技术类别**: relative spatial cue extraction
- **论文摘要层面的贡献**: Relative position cues such as left/right and near/far guide target speaker extraction without explicit DOA or clean enrollment; tested under varied acoustic conditions.
- **潜在迁移（未经验证）**: 可探索相邻探测器相对空间关系作为目标异音分离的辅助条件，不直接迁移麦克风DOA假设。
- **代码/复现状态**: 未核验官方代码；尚未复现。

### 4. ReplayFactor: Replay-Aware Dual-Attribute Learning for Practical Speech Deepfake Detection

- **arXiv**: https://arxiv.org/abs/2611.02628
- **PDF**: https://arxiv.org/pdf/2611.02628
- **作者**: Miao He; Jiayi Zhou; Yu Zheng; Zhongjie Ba; Peng Cheng; Yuxi Zhou; Junjie Zhu; Changhao Zhang; Jian Liu
- **技术类别**: open-set robustness / SSL and acoustic priors
- **论文摘要层面的贡献**: Replay-aware deepfake detection combines SSL features with acoustic priors and multi-task contrastive learning; tests physical replay and open-set robustness.
- **潜在迁移（未经验证）**: 可借鉴预训练表征+物理先验双分支对抗跨设备/传播链变化，非直接证明工业异常声有效。
- **代码/复现状态**: 未核验官方代码；尚未复现。


> 去重范围：本次写入前检查仓库已有每日文件路径和历史分类入口；未声明对全部历史论文的 DOI/标题变体完成穷尽式全库核验。
