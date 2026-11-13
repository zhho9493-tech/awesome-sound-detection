# 声学泄漏检测：10 轮检索核验与 GitHub 增量（2026-11-13）

> 检索范围：2025–2026 重点，10 组主题查询；Web 搜索提供 Google Scholar 可用的近似检索覆盖，随后以出版社 / PubMed / DOI 交叉核验。**未能直接枚举 Google Scholar 的完整结果页，因此不是 Google Scholar 全量结果，也不是系统综述意义的穷尽式检索。**

## 一、10 组检索式（可直接粘贴 Google Scholar）

1. `"acoustic water leak detection" 2025 2026 deep learning` — [Google Scholar](https://scholar.google.com/scholar?q=%22acoustic%20water%20leak%20detection%22%202025%202026%20deep%20learning)
2. `"acoustic pipeline leak localization" 2025 2026 MVDR correlation` — [Google Scholar](https://scholar.google.com/scholar?q=%22acoustic%20pipeline%20leak%20localization%22%202025%202026%20MVDR%20correlation)
3. `"gas leakage" "acoustic emission" deep learning 2025 2026` — [Google Scholar](https://scholar.google.com/scholar?q=%22gas%20leakage%22%20%22acoustic%20emission%22%20deep%20learning%202025%202026)
4. `"leak detection" "hydrophone" "machine learning" 2025 2026` — [Google Scholar](https://scholar.google.com/scholar?q=%22leak%20detection%22%20%22hydrophone%22%20%22machine%20learning%22%202025%202026)
5. `"acoustic leak detection" "few shot" 2025 2026` — [Google Scholar](https://scholar.google.com/scholar?q=%22acoustic%20leak%20detection%22%20%22few%20shot%22%202025%202026)
6. `"acoustic leak detection" "self supervised" "unsupervised" 2025` — [Google Scholar](https://scholar.google.com/scholar?q=%22acoustic%20leak%20detection%22%20%22self%20supervised%22%20%22unsupervised%22%202025)
7. `"pipeline leak" "low SNR" "acoustic" 2025 2026` — [Google Scholar](https://scholar.google.com/scholar?q=%22pipeline%20leak%22%20%22low%20SNR%22%20%22acoustic%22%202025%202026)
8. `"leak detection" "audio spectrogram transformer" pipeline` — [Google Scholar](https://scholar.google.com/scholar?q=%22leak%20detection%22%20%22audio%20spectrogram%20transformer%22%20pipeline)
9. `"acoustic emission" "pipeline leakage" systematic review 2025 2026` — [Google Scholar](https://scholar.google.com/scholar?q=%22acoustic%20emission%22%20%22pipeline%20leakage%22%20systematic%20review%202025%202026)
10. `"water pipeline" "acoustic" leak detection sensors dataset 2025 2026` — [Google Scholar](https://scholar.google.com/scholar?q=%22water%20pipeline%22%20%22acoustic%22%20leak%20detection%20sensors%20dataset%202025%202026)

## 二、核验后新增的独立论文条目

|优先级|年份|论文 / DOI|研究方向|对听漏仪的具体启示|场景|
|---|---|---|---|---|---|
|P0|2026|[Few-shot acoustic leak detection in water pipelines via hierarchical consistency learning and class-wise gating fusion](https://doi.org/10.1016/j.watres.2026.125969) · Water Research|水管声学、少样本、层次一致性、class-wise gated fusion|在小样本/类别不均衡数据集上对比现有 ResNet 与 prototype 基线|水管/声学|
|P0|2026|[Acoustic water pipe leak detection using transformer-based variational autoencoder](https://doi.org/10.1016/j.ndteint.2026.103684) · NDT & E International|管内自由游动检测器、Transformer-VAE、KDE 阈值|正常数据建模，特别注明管内游动采集与手持接触式听漏的域差别|水管/管内|
|P0|2026|[Comparative analysis of machine learning approaches for leak detection in pipelines using hydrophone acoustic sensing](https://doi.org/10.1016/j.measurement.2025.120005) · Measurement|水听器、物理统计特征+原始数据 Feature-Informed CNN|多种管路几何和水听器布设，融合原始信号与物理特征|水管/水听器|
|P0|2026|[A Survey of Water Pipeline Leak Detection Using Acoustic Sensing](https://doi.org/10.1109/TIM.2026.3666017) · IEEE Transactions on Instrumentation and Measurement|水管声学泄漏检测综述；传感器、传统机器学习及深度学习|搭建技术分类和硬件性能指标体系|水管/综述|
|P0|2025|[A two-stage leak monitoring framework for water distribution networks based on acoustic signals](https://doi.org/10.1016/j.ymssp.2024.112275) · Mechanical Systems and Signal Processing|声学两阶段检测/评估，考虑高误报和维修优先级|分离检漏与风险评估，后处理策略|水管/监测|
|P0|2025|[Automatic pipeline leak detection based on AST deep learning using a free-swimming detector with acoustic resonance cavity](https://doi.org/10.1088/1361-6501/adf90d) · Measurement Science and Technology|管内自由游动球形检测器，AST、迁移学习、碰撞噪声识别|声音事件误报分类、标签不均衡；不直接视作外置听漏仪实验|水管/管内|
|P0|2026|[Acoustic based leak location detection for water supply pipelines in urban areas via multi-task deep learning](https://doi.org/10.1016/j.engappai.2025.112718) · Engineering Applications of Artificial Intelligence|现场声学记录、DWT 去噪、多任务检测与定位、VAE 表征|联合定位、迁移学习、跨金属/非金属管路|水管/定位|
|P0|2026|[Improving acoustic leak localization accuracy using an adaptive denoising algorithm in water distribution pipes](https://doi.org/10.1016/j.apacoust.2025.110984) · Applied Acoustics|FIR 自适应降噪 + 相关定位；铸铁与塑料管现场验证|低 SNR 相关定位，基于管壁传播先验|水管/定位|
|P0|2025|[Adaptive noise cancellation based on CEEMDAN-LMS for pipeline leak location under low SNR](https://doi.org/10.1016/j.psep.2025.107668) · Process Safety and Environmental Protection|CEEMDAN 模态分解、跨传感器相关选择 IMF、LMS 抵消噪声|噪声鲁棒声学定位，适合和 GCC-PHAT 及自适应 FIR 比较|声学/低SNR|
|P1|2026|[Calibrated Acoustic Leak Signatures in Pressurised Plastic Water Pipes: A Laboratory Analysis](https://doi.org/10.3390/s26144325) · Sensors|塑料管壁加速度声学标定；受控压力与漏孔设置|建立频段、压力、耦合与孔径的物理基线|水管/物理|
|P1|2025|[Pipeline Leakage Identification Based on Acoustic Sensors and EPSO-1D-CNN-Bi-LSTM Model](https://doi.org/10.3390/s25237355) · Sensors|声学传感器，优化 CNN-BiLSTM 识别|轻量化时序学习和工程识别基线|水管/深度学习|
|P1|2026|[Lightweight Graph Neural Network-Driven Acoustic Anomaly Detection Method for Gas Pipeline Leakage Levels in Underground Utility Tunnels](https://doi.org/10.3390/s26134114) · Sensors|气体泄漏声学时空 GNN、泄漏孔径/风险等级|泄漏分级与多节点建模，跨介质实验需重新验证|气体/等级|
|P1|2026|[Systematic review for fluid pipeline leakage monitoring: present status and challenges of acoustic emission technique](https://doi.org/10.1016/j.measurement.2026.121271) · Measurement|声发射技术综述，含检测/定位/定量及低压/高噪声场景|声发射信号链与定位技术全景|声发射/综述|
|P1|2026|[A novel method for sound speed estimation and leak localization in urban water supply pipelines using active acoustic sources](https://doi.org/10.1016/j.jwpe.2026.110166) · Journal of Water Process Engineering|主动声源与管内声速原位估计、反射延迟定位|修正管材/压力造成的声速误差，需要主动激励硬件|水管/定位|
|P1|2026|[Research on leakage location of buried gas non-metallic pipeline based on acoustic signal attenuation mechanism](https://doi.org/10.1016/j.flowmeasinst.2026.103520) · Flow Measurement and Instrumentation|改进 MVMD 去噪、能量梯度初定位及衰减精定位|地下非金属管弱信号定位，需验证水管迁移|气体/定位|
|P2|2026|[A technology for early warning of leaks in oil and gas storage and transmission pipelines based on deep neural networks and multimodal fusion](https://doi.org/10.1093/ijlct/ctag148) · International Journal of Low-Carbon Technologies|声发射、振动、压力流量温度多模态，VMD 与 ProtoNet|多模态工程监测，非纯声学设备直接基线|油气/多模态|
|P2|2026|[A gas leakage intelligent monitoring method based on multi-channel spatiotemporal perception and multi-view learning](https://doi.org/10.1016/j.engappai.2026.116244) · Engineering Applications of Artificial Intelligence|多通道时空学习与融合，气体泄漏监测|多通道融合启发；需核实所用传感模态后再认定声学适用性|气体/多通道|

## 三、与已有仓库的去重范围

- 已读取 `domains/leakage/README.md`、`domains/leakage/literature-screening-2026-11-13.md`、`resources/historical-paper-index.md`，并检查泄漏专题的两个 Drive 索引以及 arXiv 索引；这些题名未见于已读取的专题正文。
- 另尝试 GitHub code search 精确题名检索，未返回匹配条目；**这并非全仓内容级去重完成的证明**。尤其大型 `resources/paper-master-index.json` 当前连接器未返回完整正文，因此这一文件仍有重复风险。
- 与前期用户提交的法兰泄漏、MVDR、2025 FENDT 复杂管声发射论文是不同条目；不重复记录。
- 每篇以上通过 DOI 标识，**只有研究记录/网页链接被提交；没有声称 PDF 或开源代码已经保存**。

## 四、技术趋势与关键证据

1. **传统二分类 → 少样本/无监督/细粒度识别**：Water Research 2026 少样本 HCL+CWGF；NDT&E 2026 Transformer-VAE+KDE；Sensors 2026 气体泄漏分级 GNN。对应问题：故障数据稀少、非平稳工况、风险等级。
2. **纯声谱 → 物理特征 + 学习表征**：Measurement 2026 FI-CNN 用水听器声学和流固相互作用特征；Sensors 2026 塑料管的标定振动数据，为跨管材可靠性评价提供物理证据。
3. **相关定位 → 传播物理/自适应抗噪/声速校准**：Applied Acoustics 2026 FIR 自适应；PSEP 2025 CEEMDAN-LMS；JWPE 2026 主动声源原位声速；相对于传统 GCC-PHAT，应分别对比定位 MAE/P90、有效 SNR 范围和硬件成本。
4. **检测 → 检测+定位+风险评估**：EAAI 2026 多任务检测定位；MSSP 2025 两阶段监测与漏损评估；多任务输出的优势必须在独立测试域检验。
5. **模型能力受到采集方式制约**：水听器、自由游动管内设备、接触式加速度计、外置听音器以及气体 AE 具有不同传播与耦合条件，禁止直接比较跨设备的论文准确率。

## 五、建议实验矩阵

|子任务|基线|新增方法|关键控制变量|指标|
|---|---|---|---|---|
|单点声学检测|log-mel + ResNet18|FI-CNN、AST、少样本 HCL/CWGF、Transformer-VAE|管材/水压/孔径/采集点/背景声/不同管道|AUPRC、指定误报率召回、ECE|
|低 SNR 检测|频域阈值/普通降噪 + CNN|多尺度卷积、时频增强、物理特征融合|SNR、瞬态噪声、管壁耦合|SNR 分层 AUPRC、事件级误报率|
|双点声学定位|BCC/GCC-PHAT|CEEMDAN-LMS、自适应 FIR、跨谱 MVDR|管距/传播速度/塑料管/阀门弯头|MAE、P90、误定位率|
|泄漏强弱分级|能量阈值|监督分级、时空 GNN、校准分类|孔径/流量/压力/安装方式|macro-F1、序数误差、校准|

## 六、论文权重的注意事项

- 作者在论文中报告的数字仅作原作者证据，不是本项目实测，不能由高准确率推导跨管材泛化。
- 2025 或 2026 年份依据期刊正式发表时间；DOI 字符串内包含的年份不一定是期刊卷期年份。
- 近期发表论文不保证代码/数据集公开，需单独核查，不填写虚构的 GitHub 项目或 PDF 镜像地址。
- 推荐优先开展三组对比：**少样本 vs 无监督异常检测**、**原始声谱 vs 物理特征融合**、**GCC-PHAT vs 自适应低 SNR 定位**。
