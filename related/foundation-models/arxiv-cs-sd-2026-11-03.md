# arXiv cs.SD 每日增量｜2026-11-03 公告

来源：https://arxiv.org/list/cs.SD/new （2026-11-03 公告）；本页按本仓库相关性筛选，包含 cs.SD new submissions 和 cross-lists。日期为公告日期，**不是全部论文的首次提交日期**；arXiv ID 前缀 2611 仅代表 2026-11。以下首次提交的精确日期尚待逐篇版本元数据复核。条目均未在工业DAS场景复现。

| arXiv | 论文 | 作者 | 技术类别 | 首次提交日期 | 官方PDF | 代码/复现 |
|---|---|---|---|---|---|---|
| [2611.00325](https://arxiv.org/abs/2611.00325) | One Waveform, Two Stories: Benchmarking Speech-Acoustic Conflict in Audio-Language Models | Wenbin Wang; Yuheng Li; Koichiro Yoshino | Audio-LLM conflict evaluation | 待核验（2026-11 公告） | [PDF](https://arxiv.org/pdf/2611.00325) | 官方代码待核验；未复现 |
| [2611.02330](https://arxiv.org/abs/2611.02330) | Spatial Transfusion: From Structured Spatial Scene Understanding to Generation and Editing | Jaeyeon Kim; Sebastian Braun; Hannes Gamper | spatial audio foundation model / LoRA | 待核验（2026-11 公告） | [PDF](https://arxiv.org/pdf/2611.02330) | 官方代码待核验；未复现 |
| [2611.00333](https://arxiv.org/abs/2611.00333) | C3: Speech-Guided KV Retrieval for Long-Context SpeechLLM Inference | Dancheng Liu; Markus Müller; Rupak Vignesh Swaminathan; Jing Liu; Srikanth Ronanki; Aram Galstyan | long-context audio retrieval | 待核验（2026-11 公告） | [PDF](https://arxiv.org/pdf/2611.00333) | 官方代码待核验；未复现 |

## 方法摘要及工业声学/DAS迁移假设

### 1. One Waveform, Two Stories: Benchmarking Speech-Acoustic Conflict in Audio-Language Models

- **arXiv**: https://arxiv.org/abs/2611.00325
- **PDF**: https://arxiv.org/pdf/2611.00325
- **作者**: Wenbin Wang; Yuheng Li; Koichiro Yoshino
- **技术类别**: Audio-LLM conflict evaluation
- **论文摘要层面的贡献**: SAC-Bench: 616,031 clips / 188 event classes, testing contradictions between spoken claims and environmental acoustic evidence; reported event identity degradation of 24.8–46.5 points under conflict.
- **潜在迁移（未经验证）**: 工业DAS告警中将文本/工单/人工描述与原始声学证据分开校准；研究冲突检测与声学优先回退。
- **代码/复现状态**: 未核验官方代码；尚未复现。

### 2. Spatial Transfusion: From Structured Spatial Scene Understanding to Generation and Editing

- **arXiv**: https://arxiv.org/abs/2611.02330
- **PDF**: https://arxiv.org/pdf/2611.02330
- **作者**: Jaeyeon Kim; Sebastian Braun; Hannes Gamper
- **技术类别**: spatial audio foundation model / LoRA
- **论文摘要层面的贡献**: Unified FOA understanding, generation and editing via frozen spatial understanding backbone, flow matching and modality-routed LoRA.
- **潜在迁移（未经验证）**: 借鉴冻结预训练编码器+多任务适配，以及声学事件的结构化空间表示；FOA与DAS存在模态差异。
- **代码/复现状态**: 未核验官方代码；尚未复现。

### 3. C3: Speech-Guided KV Retrieval for Long-Context SpeechLLM Inference

- **arXiv**: https://arxiv.org/abs/2611.00333
- **PDF**: https://arxiv.org/pdf/2611.00333
- **作者**: Dancheng Liu; Markus Müller; Rupak Vignesh Swaminathan; Jing Liu; Srikanth Ronanki; Aram Galstyan
- **技术类别**: long-context audio retrieval
- **论文摘要层面的贡献**: C3 hierarchical key-space KV retrieval reallocates attention budget adaptively for long-form speech language models.
- **潜在迁移（未经验证）**: 长期DAS事件复核与多窗口检索可参考稀疏时序证据选择，但需独立验证推理延迟和召回。
- **代码/复现状态**: 未核验官方代码；尚未复现。


> 去重范围：本次写入前检查仓库已有每日文件路径和历史分类入口；未声明对全部历史论文的 DOI/标题变体完成穷尽式全库核验。
