# cs.SD 2026-11-04｜声纹识别与边缘开集

## HyVox: Rethinking Low-Power Voice Intelligence towards Neuromorphic-von Neumann Edge Computing
- 作者：Snehasis Addy; Eduardo Calle Ortiz; Prashant Shenoy; Phuc Nguyen
- 首次提交：2026-11-04；arXiv: https://arxiv.org/abs/2611.03735；PDF: https://arxiv.org/pdf/2611.03735
- 方法：脉冲神经网络编码器与 MCU 原型库解耦；余弦匹配、unknown 拒识与新增 speaker prototype 无需更新权重。作者报告 3 秒输入推理 0.96 秒、动态能耗 1.63mJ（特定硬件）。
- 工业声学/DAS 迁移假设：固定声学编码器 + 增量原型 + 开集拒识，适用于低功耗边缘端；需验证多探测器、工业噪声与非语音场景。
- 代码/复现：未核实官方代码；未复现。
