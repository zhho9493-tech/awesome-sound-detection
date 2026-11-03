# 2025–2026 DAS 皮带机监测论文增量索引

截至 2026-11-03，本专题共列出 15 条候选/已核验文献，含直接相关 10 条与可迁移方法 5 条。已核对表示本次重新查验期刊来源，待复核表示沿用先前检索线索。PDF 列仅为论文官方PDF入口，不代表逐一验证成功下载。不得将未找到 arXiv 等同于不存在。

## 直接涉及 DAS/分布式光纤皮带监测

|论文|原始来源|PDF入口|DOI|核验状态|
|---|---|---|---|---|
|Toward Open-Set Fault Diagnosis for Belt Conveyors Using Distributed Acoustic Sensing|[DOI](https://doi.org/10.1109/JSEN.2026.3709836)|待核实|10.1109/JSEN.2026.3709836|2026 IEEE Sensors Journal，题名/DOI/卷期经作者页面与文献记录核对；全文待复核|
|Distributed Acoustic Sensor for Real-Time Fault Detection in Belt Conveyors: A Signal Processing Approach|[DOI](https://doi.org/10.1109/JSEN.2026.3701460)|待核实|10.1109/JSEN.2026.3701460|2026 IEEE Sensors Journal，题名/DOI经文献记录核对；全文方法与指标待复核|
|Full-Line Idler Fault Monitoring in Belt Conveyors via UWFBG-DAS and Characteristic Energy Feature Analysis|[论文页](https://www.mdpi.com/1424-8220/26/15/4905)|[PDF](https://www.mdpi.com/1424-8220/26/15/4905/pdf)|10.3390/s26154905|已核对|
|Towards a physics-informed network paradigm with data generation and background noise removal for different distributed acoustic sensing applications|[论文页](https://www.nature.com/articles/s41377-026-02295-5)|待核实|10.1038/s41377-026-02295-5|已核对|
|Φ-OTDR Distributed Acoustic Sensing with EMD–CWT and 2D-CNN for Fault Diagnosis of Belt Conveyor Idlers|[论文页](https://doi.org/10.1364/OPTCON.603370)|待核实|10.1364/OPTCON.603370|待复核|
|Belt Conveyor Idler Fault Detection System Based on uwDAS Cable and Fiber Optic Microphone Combined Sensing|[论文页](https://ray-sensor.com/publication-conveyor-fault/)|待核实|待核实|待复核|
|基于DAS的带式输送机声音异常监测识别技术研究|[论文页](https://mkjx.cbpt.cnki.net/portal/journal/portal/client/paper/933a1a927d5e75e52603e093fc7b1d15)|待核实|待核实|待复核|
|基于分布式光纤传感的散货码头带式输送机智能巡检系统|[论文页](https://www.chinamet.cn/zxjx/article/doi/10.13551/j.cnki.zxjxqk.2026.01.013)|待核实|10.13551/j.cnki.zxjxqk.2026.01.013|待复核|
|分布式光纤传感带式输送机故障诊断系统研究|[论文页](https://mkjx.cbpt.cnki.net/portal/journal/portal/client/paper/a0336febe0496705a126a1b749ac40b8)|待核实|待核实|待复核|
|基于分布式光纤的带式输送机托辊故障诊断系统设计与应用|[论文页](https://mtjs.cbpt.cnki.net/portal/journal/portal/client/paper/f5e3fa03f1994534472d50c183e952c0)|待核实|待核实|待复核|

## 跨领域相关方法与综述

|论文|原始来源|PDF入口|DOI|核验状态|
|---|---|---|---|---|
|MIRA: A Transformer-Based Framework for Idler Roller Anomaly Detection and Localization|[期刊原文](https://www.mdpi.com/1424-8220/25/24/7469)|[PDF](https://www.mdpi.com/1424-8220/25/24/7469/pdf)|10.3390/s25247469|2025 Sensors 已核对；声学+振动点式传感器，**不是 DAS**|
|基于VMD-Matrix的DAS振动信号物理可解释压缩表征与快速诊断|[论文页](https://jvs.sjtu.edu.cn/CN/Y2026/V45/I2/216)|待核实|待核实|待复核|
|From Detection to Prediction: A Systematic Review of Intelligent Fault Detection in Industrial Conveyor Belt Systems|[论文页](https://www.mdpi.com/1424-8220/26/21/6741)|[PDF](https://www.mdpi.com/1424-8220/26/21/6741/pdf)|待核实|待复核|
|Dual-Channel Acoustic Temporal–Spectral Representation and Noise-Perturbation Learning for Mining Conveyor Fault Diagnosis|[论文页](https://www.papers.phmsociety.org/index.php/ijphm/article/view/4841)|待核实|10.36001/ijphm.2026.v17i2.4841|已核对|
|基于NSST4-SVD-DBN的带式输送机托辊轴承故障诊断方法|[论文页](https://opaj.napstic.cn/periodicalArticle/0120260401796666)|待核实|待核实|待复核|

## 技术趋势

- 位置级正常基线与分区阈值：UWFBG-DAS 研究结合VMD、时序累积及传感器位置优化，适合比较不同探测器阈值差异。
- 物理约束与跨场景：物理建模生成DAS训练样本并抑制背景噪声，有助于研究目标现场故障样本不足的迁移问题。
- 时频特征与Noise-aware训练：EMD-CWT和双流谱图/波形属于需在固定跨项目测试集上消融的候选方案。
- 开集拒识：Lv 等（2026）提出直接面向 DAS 皮带机开集诊断的论文，支持将未知故障/干扰识别列为重点；具体开放集基准、阈值与误报率仍须阅读全文验证。
- 无监督空间定位（跨传感模态）：MIRA 使用麦克风+加速度计和 masked Transformer autoencoder，原论文报告测试台架检测准确率 98.70%、定位准确率 96.09%；不等于 DAS 现场指标，迁移到光纤信号属于待验证假设。
- 实时信号处理：Luo 等（2026）提供 DAS 皮带机实时检测的研究入口；不应在未阅读正文前断言具体滤波、峰值检测或跑偏定位性能。
- 健康演化：由单次故障检测进一步探索状态分级和趋势，但需现场长期数据支持。

后续需将 DOI/归一化标题与统一主索引去重并核对论文作者、出版日期及 PDF 可获取性。

## 2026-11-03 新增文献核验说明

- 上述新增 3 篇以 DOI 去重，不宣称 PDF 已成功下载；IEEE 2 篇目前主要核实的是书目信息，方法细节和性能仍需阅读全文确认。
- 用户提供的 `Multi-class fault classification in conveyor systems using distributed acoustic sensing` 未核实到同名正式文献，**暂不作为论文收录**；避免将普通输送机多分类研究误标为 DAS。
- 建议后续在主索引更新时按 DOI 和规范化题名统一去重，并补全来源及下载可用性。
