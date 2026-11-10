# 炸街车检测技术趋势（证据链版）

最后审核：2026-11-10。**技术趋势不等于已被大规模实证验证的统一结论**；逐条给出证据及尚待验证点。

## 1. 传统过车声分类 → 特定改装排气声事件级检测
- **起点**：IDMT-TRAFFIC（2021）提供车辆/道路条件分类基准；日本 NTSEL / INTER-NOISE（2023）研究从过车声时频图判断非法消声器。
- **进展**：Wang 等（2026）针对改装排气事件，使用 SEDT 与 MSResNet，直接输出事件时间，并对合成/现场结果分别报告 event-F1（0.7277 / 0.6629）。
- **实质变化**：从“车是什么类型”走向“哪一段时间出现了疑似改装排气特征”，有利于现场声视频联动。
- **边界**：研究针对特定目标与实验条件；F1 不能外推至所有城市，也不是违法判定准确率。
- **证据**：[IDMT](https://www.idmt.fraunhofer.de/en/publications/datasets/traffic.html) · [NTSEL](https://www.ntsel.go.jp/Portals/0/resources/report/files28/ronbungaiyo28.pdf) · [Wang 2026](https://doi.org/10.1016/j.trd.2026.105241)。

## 2. 少量实录训练 → 前景/背景合成增强 + 独立现场验证
- **起点**：专门改装排气声公开训练数据不足。
- **进展**：2026 研究采用 Scaper 进行混音合成并保留真实现场测试；SHAP 发现模型关注加速谐波与回火瞬态，同时发现合成数据可能带来时间位置偏差。
- **方向**：事件频谱/响度/距离/混响多样性生成，辅以真实过车声音留出验证；不仅提升合成验证集，还须改善真实场景表现。
- **待验证**：未确认其原始专项训练集和代码公开；需自建小规模可信事件标签，按道路与录音设备留出。
- **证据**：[2026 期刊](https://www.sciencedirect.com/science/article/pii/S1361920926000349) · [Scaper](https://github.com/justinsalamon/scaper)。

## 3. 单麦检测 → 阵列方向估计与多车声源归属
- **起点**：单点麦克风的高能量峰值不能证明是哪辆车发声。
- **支撑工作**：Schulz 等（2021）以 OVAD/56 通道阵列对遮挡车辆进行检测和方向推断；NTSEL（2023）也研究麦克风阵列用于改装车判别。
- **应用构想**：检测事件时间 → DOA/波束形成 → 跨时间跟踪 → 可选的视频车辆匹配。
- **边界**：OVAD 并非改装排气数据；从车辆定位迁移到炸街车归属需独立验证，尤其是多车同时过车与反射声。
- **证据**：[OVAD 论文/数据](https://research.tudelft.nl/en/datasets/ovad-occluded-vehicle-acoustic-detection-dataset/) · [OVAD 代码](https://github.com/tudelft-iv/occluded_vehicle_acoustic_detection)。

## 4. 同域测评 → 跨地点、车型、设备与交通密度的可靠性评估
- **证据**：IDMT 提供多地点、多传感器信息；MELAUDIS 包括复杂的多车/背景；NTSEL 报告跨车型、道路数据补充改善模型；Wang 2026 现场 F1 低于验证 F1。
- **建议**：强制 site-out/device-out/vehicle-out/time-out；记录每小时误报、每百辆车误报、event-F1、PSDS、目标检测延时与声源归属率。
- **研究假设（非已证结果）**：域泛化、声学校准、模型不确定性/OOD 与主动学习可能改善上线稳定性；须用独立现场实验验证。
- **证据**：[IDMT](https://www.idmt.fraunhofer.de/en/publications/datasets/traffic.html) · [MELAUDIS](https://doi.org/10.1038/s41597-025-04689-3) · [2026 期刊](https://doi.org/10.1016/j.trd.2026.105241)。

## 推荐的端到端实验（未执行）
1. 建立人工核验的目标事件与高混淆负样本，区分“疑似改装声学表现”和“已被独立证实的非法改装”。
2. B0：log-mel + ResNet18/PANNs clip 分类；B1：CRNN/SEDT 事件级检测；B2：B1+Scaper；B3：B2+DOA/多车跟踪。
3. 统一训练/验证，锁定独立真实道路测试集；对比随机切分与地点隔离以量化泄漏影响。
4. 量化 event-F1、PSDS、误报/小时、每百辆误报、误归属率、算力/延迟、场景分层置信区间。
5. 产出失败案例：正常高转速、摩托/货车、喇叭、警笛、强风、混合车流、交通拥堵、回声。
6. 报警与执法证据严格分离；不使用未经校准的绝对声压值推导超标结论。
