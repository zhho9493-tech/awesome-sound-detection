# arXiv cs.SD 2026-11-13 公告｜边缘持续异常检测与多接收端声学表征

> 包含 cs.SD cross-list。首次提交日期不等于公告日期；工业 DAS 迁移均为研究假设。

## 1. On-Edge Acoustic Continual Anomaly Detection: A Cross-Platform Comparative Study
- **作者**：Rami Zewail; Yehia Ehab; Karim Ali; Ahmed Mahrous; Mohamed Awad; Bassem Mokhtar
- **首次提交**：2026-11-11；**arXiv**：[2611.15465](https://arxiv.org/abs/2611.15465)；**PDF**：https://arxiv.org/pdf/2611.15465
- **方法**：ShallowNet 将谱图映射为 32 维嵌入，采用对比式原型学习及 EMA 在线更新；在 ESP32-S3 与 Arduino Nicla Vision 上使用相同 TFLM 编码器，结合 MQTT/Firebase 云端重训。
- **数据/指标**：DCASE Task 2 机器声音的受控扬声器回放；作者报告两平台不同机器类别准确率分别约 82.35–95.00% 与 79.41–95.00%。这不是实际现场持续漂移、低误报率或跨项目 DAS 性能证据。
- **代码/复现**：摘要未给出官方代码；需要进一步核查资源、回放协议和在线更新防污染策略。
- **DAS 迁移（研究假设）**：对比边缘端固定原型、EMA 原型、置信门控原型更新；防止异常伪正常进入更新；关注嵌入维度、推理时延、功耗及跨设备一致性。

## 2. FineSpeaker: Reliable Speaker Representation Learning at Fine Temporal Resolution
- **作者**：Yongkang Yin; Wenhao Yang; Lichun Fan; Jian Luan; Hang Su; Yuexian Zou
- **首次提交**：2026-11-11；**arXiv**：[2611.15288](https://arxiv.org/abs/2611.15288)；**PDF**：https://arxiv.org/pdf/2611.15288
- **方法**：可调 n 帧池化构造不同时间分辨率说话人表示，结合局部时序编码器与 VAE/flow matching 解耦非身份变化。
- **数据/指标**：VoxCeleb、CN-Celeb；短时说话人验证与零样本分离；摘要未列具体数值。
- **代码/复现**：摘要未声明官方代码；待核查。
- **DAS 迁移（研究假设）**：研究“短时异常定位精度 vs 设备身份/类别嵌入稳定性”权衡；说话人身份与托辊设备身份并不等价。

## 3. MESH: Multi-receiver Evaluation of Spatial Hearing across Egocentric and Allocentric Views
- **作者**：Wen Wen; Bohan Li; KwanHo Tam; Yu Xi; Jing Peng; Shuai Wang; Kai Yu
- **首次提交**：2026-11-12；**arXiv**：[2611.16787](https://arxiv.org/abs/2611.16787)；**PDF**：https://arxiv.org/pdf/2611.16787
- **方法**：通过本地录音+同伴元数据，以及同步多接收器共享 3D 坐标系两种视角，评估声源身份与位置/运动的一致性。约 4 万问题、13 项任务；作者指出现有模型利用跨接收端信息能力不足。
- **数据/指标**：分布式语音空间定位/转写；非 DAS。作者报告最优静态距离准确率 21.90%、动态方向跟踪准确率 41.54%，不能迁移为托辊定位数值。
- **代码/复现**：作者声明公开评估代码及数据集，链接见 arXiv 页面；独立复现未核实。
- **DAS 迁移（研究假设）**：建立相邻探测器共享时钟、空间位置、异常事件身份关联的评价基准；特别验证多源干扰下同一异常是否跨探测器保持一致。

## 技术判断
边缘原型持续更新与多接收器身份—位置绑定均有明确工程价值，但现有证据分别来自受控扬声器回放和分布式语音场景；应先设计 DAS 现场基准，不外推准确率。
