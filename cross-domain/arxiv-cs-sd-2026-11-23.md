# arXiv cs.SD 2026-11-23 公告增量

## Impact of Edge Software Evolution on Audio Tagging Models: An Empirical Study on NVIDIA Jetson Orin Nano
- 作者：Guillem Fustier-Castillo, Ruben Ribes-Serrano, Jordi Grau-Haro, Marta Garcia-Ballesteros, Javier Naranjo-Alcazar；首次提交：2026-11-19。
- [arXiv](https://arxiv.org/abs/2611.26831) | [PDF](https://arxiv.org/pdf/2611.26831) | DOI: 10.48550/arXiv.2611.26831
- 方法：同一 Jetson Orin Nano 硬件比较 JetPack 6.2/7.2 下 PANNs、AST、PaSST 的延迟、能耗、资源利用和内存，覆盖多种后端和功耗模式。
- 结果：作者报告 TensorRT 下部分 CNN 延迟与能耗降低超过50%，AST 改善有限，PaSST 居中；不可泛化到所有架构或硬件。
- 复现：Computing 2027 已接收（作者说明）；公开实验代码未核实。
- DAS迁移研究假设：固定模型和硬件，按软件栈、推理后端、功耗模式做全链路基准，验证精度一致性、P95延迟、吞吐、内存和能耗。
