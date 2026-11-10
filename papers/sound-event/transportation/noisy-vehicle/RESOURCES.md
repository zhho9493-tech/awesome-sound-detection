# 炸街车检测：数据集与开源代码

最后检索：2026-11-10。注意 **“车辆音频数据” ≠ “带有改装排气/违法标签的数据”**。

## 数据集

| 数据集 | 规模/特性 | 下载 | 对本任务的角色 | 限制 |
|---|---|---|---|---|
| [IDMT-TRAFFIC](https://www.idmt.fraunhofer.de/en/publications/datasets/traffic.html) | 17,506 个 2 秒立体声片段；轿车/摩托/卡车/公交；4 地点、干湿路面、不同麦克风 | [Zenodo](https://zenodo.org/records/7551553) | 正常过车声、跨设备/道路泛化、车型分类 | CC BY-NC-ND 4.0；非改装排气专项标签 |
| [MELAUDIS](https://doi.org/10.1038/s41597-025-04689-3) | 7,345 车辆样本、5,792 背景、2,955 怠速；含多车同现 | [论文/数据可用性说明](https://www.nature.com/articles/s41597-025-04689-3) | 多车交通负例和现实复杂背景 | 检查作者指定下载位置及许可证；非非法排气标签 |
| [OVAD](https://research.tudelft.nl/en/datasets/ovad-occluded-vehicle-acoustic-detection-dataset/) | 56 通道阵列与视觉数据、户外路口/遮挡 | [数据项目](https://doi.org/10.4121/07c5956a-fd5f-411f-9b4e-ffe7eb7dec5f) | 阵列、声源归属、不同路口泛化 | 非改装排气；数据量大 |
| [UrbanSound8K](https://dcase-repo.github.io/dcase_datalist/datasets/sounds/urbansound8k.html) | 8,732 片段；10 类含 engine idling、car horn | [数据资料](https://serv.cusp.nyu.edu/projects/urbansounddataset/urbansound8k.html) | 通用城市误报/背景预训练 | 没有专门改装排气标签 |

**2026 专项论文数据**：Wang 等利用 Scaper 合成训练场景、真实深圳道路录音评估；论文未确认公开可下载的专项带标注全集。不能将其列为开放下载数据集。详见 [论文 DOI](https://doi.org/10.1016/j.trd.2026.105241)。

## 开源工具 / 参考实现

| 项目 | 地址 | 可用能力 | 证据层级 |
|---|---|---|---|
| Scaper | [github.com/justinsalamon/scaper](https://github.com/justinsalamon/scaper) | 通过前景事件 + 背景生成 SED 训练混音 | 通用合成工具，不是 2026 论文官方实现 |
| OVAD / TU Delft | [github.com/tudelft-iv/occluded_vehicle_acoustic_detection](https://github.com/tudelft-iv/occluded_vehicle_acoustic_detection) | 麦克风阵列特征、分类、声源定位与评估 | 车辆检测/定位参考实现 |
| MELAUDIS | [github.com/parineh/MELAUDIS](https://github.com/parineh/MELAUDIS) | 作者提供的音频时频转换及数据处理代码 | 数据处理，不是炸街车检测器 |
| carzam | [github.com/jiogallardy/carzam](https://github.com/jiogallardy/carzam) | 基于排气音识别车型，PANNs 对比学习等 | 社区项目，非非法排气识别研究 |
| SEDT 论文 | [arxiv.org/abs/2110.02011](https://arxiv.org/abs/2110.02011) | 事件级检测模型原理 | 论文，不在此声称已验证官方代码 |

## 建议新增采集的最小字段
`recording_id, passby_event_id, site_id, date_time, microphone_id, sampling_rate, channel_count, distance_estimate, vehicle_type, traffic_density, event_start, event_end, sound_type, suspected_modified, verified_exhaust_modification, verification_method, annotator, confidence, split`。

采集时须遵守当地合法录音、视频和个人信息保护要求；用场景/车辆/过车事件隔离训练与测试。对于“是否非法改装”的真值应通过独立证据取得，而非依靠声音响度反推。

## 下载/许可证审核
- IDMT-Traffic 的使用条款明确为 CC BY-NC-ND 4.0，不要默认允许商业模型训练或再分发。
- 其他数据集与仓库逐项核对源站许可证、使用范围与版本。
- 本页链接已人工检索对应页面，**未批量执行下载完整性、训练复现或许可证法律审查**。
