# DAS Conveyor Industry Timeline / DAS 皮带机企业动态时间线

> 目标：记录与 **DAS / 分布式光纤传感 + 带式输送机 / 托辊监测** 直接相关的企业产品、项目招标、客户案例、商业化路径与技术路线变化。  
> 仅记录公开信息；企业自报性能须与第三方验证区分。

## 2026 时间线

| 日期 | 企业/机构 | 事件 | 与 DAS 皮带机监测的关联 | 对算法/产品的启示 | 来源 |
|---|---|---|---|---|---|
| 2026-03-20 | 华为 × 海螺水泥/海螺智质 | 发布托辊听诊光纤感知解决方案 | 分布式光纤 + AI 用于托辊 7×24h 异响监测；官方披露实际使用中告警准确率 >95% | 商业验收应关注误报/漏报，而非只看离线 Accuracy | https://e.huawei.com/cn/news/2026/solutions/enterprise-optical-network/conch-cement |
| 2026-06-16 | 海康威视 | 发布“皮带托辊异常监测场景方案” | PDC φ-OTDR 解调 + 深度学习；异常后由人工复核 | “AI 自动召回 + 人工复核”是现实可行闭环；需要声音证据可回放 | https://partners.hikvision.com/solution/795219013142859776 |
| 2026-07-10 | 国能北电胜利能源 | “基于光纤声呐的智能监测系统服务”公开招标 | 明确要求 DAS 对输煤胶带机异音识别、准确识别托辊故障，并融合 DTS、断纤/外破、巡检机器人 | 产品竞争从单一模型转向“DAS+DTS+定位+机器人+运维平台” | https://www.chnenergybidding.com.cn/bidweb/001/001002/001002003/20260710/f2bc34a6-0218-4ea6-ab3a-38f0a3545391.html |
| 2026-08 | REMA TIP TOP × Terra15 | ARMS（Automated Roller Monitoring System）商业部署信息持续公开 | DAS 沿输送机连续采集声振，采用位置正常基线和多算法组合 | 位置级 normal baseline、位置自适应、长周期趋势比单一全局阈值更重要 | https://www.rema-tiptop.com/ |
| 2026-08 | 讯飞潮汐力 | 对外展示矿山/钢铁长距离 DAS 皮带监测案例 | 公开案例包含长距离皮带托辊声学异常监测、持续性异常判定 | “持续性异常 Precision”“设备级长期趋势”可作为项目级验收指标 | https://www.iflytek.com/ |
| 2026-08 | 光格科技 | 半年报披露分布式光纤声波/振动/温度与 AI Agent PHM 路线 | 将带式运输机实时监测、故障预测、健康管理纳入核心技术 | 从异常检测向 PHM/健康状态/RUL 延伸；需要设备级状态建模 | https://vip.stock.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?id=12556007&stockid=688450 |
| 2026-09 | Mining3 → PositioNXT / Vuuma | DAS 输送机状态监测达到 TRL8，并由 PositioNXT、Vuuma 商业化 | 标准光纤作为“虚拟麦克风”，输出位置、故障类型与严重度，并融合速度/负载工况 | severity + 工况条件 + 历史位置趋势，是从“异常”走向“预测维护”的关键 | https://www.mining3.com/portfolio/conveyor-condition-monitoring |
| 2026-09-17 | 华为 × 海纳科技 | 发布带式运输机光纤听诊感知解决方案 | DAS + AI 大模型用于煤矿带式输送机托辊故障检测 | “光纤底层感知 + 大规模预训练/AI + 矿山工程能力”成为典型产业组合 | https://e.huawei.com/cn/news/2026/solutions/enterprise-optical-network/launch-optical-fiber-sensing-solution |
| 2026-09-17 | 海纳科技 | 同步发布矿山全过程自适应智能输送方案 | 将光纤听诊纳入更大的皮带机智能运维体系 | DAS 不应孤立部署，应接入设备健康、工况和维修决策闭环 | https://www.hainakj.com/h-col-125.html |
| 2026-10 | 海纳科技 | “一眼通”式皮带机智能运维平台路线持续公开 | 光纤听诊与测温、振动、张力、跑偏、电气参数等多源信息融合 | 推荐分层：DAS 全线筛查 → 多源确认 → 健康分级 → 运维决策 | https://www.hainakj.com/ |

## 代表性企业与路线

### 国内

- **华为**：低噪声光纤感知硬件 + AI/大模型 + 行业伙伴联合方案。
- **海纳科技**：矿山/皮带机设备与运维场景能力，侧重系统集成和健康管理。
- **海康威视**：光纤听诊 + 深度学习 + 人工复核，强调工业场景落地。
- **讯飞潮汐力**：长距离 DAS + 声学算法 + 工业 AI 平台。
- **光格科技**：DAS/DTS + AI Agent + PHM/数字化运维。
- **胜利能源**：作为甲方推动正式招标，体现能源行业对 DAS 胶带机监测的真实采购需求。

### 海外

- **Mining3 / PositioNXT / Vuuma**：TRL8，强调故障类型、严重度、工况融合和商业化。
- **REMA TIP TOP / Terra15**：DAS 连续监测 + 位置级基线 + 多算法融合，强调不同负载与安装条件下的适配。

## 技术趋势总结

1. **从单一异常分类器转向分层系统**：采集稳定性 → 片段检出 → 位置聚合 → 持续性确认 → 设备健康状态。
2. **从统一阈值转向位置级基线**：不同光纤耦合、探测位置、设备结构差异必须被显式建模。
3. **从“正常/异常”转向严重度与健康演化**：Weak/Early → Developing → Severe → Maintenance。
4. **从单模态 DAS 转向多源融合**：DAS + DTS + 点式声振温 + 视频 + 机器人。
5. **从模型指标转向工程指标**：FP/km/day、漏报率、定位误差、连续运行稳定性、检修效率。
6. **从单项目训练转向预训练和跨项目泛化**：工业声学预训练、DAS 自监督、现场少量正常数据自适应。

## 对托辊异常检测研发的直接建议

优先构建以下统一输出：

```
10 s clip anomaly score
+ detector/location baseline deviation
+ temporal persistence
+ spatial consistency
+ interference evidence
+ operating condition
→ equipment-level health state
```

建议把 **FP/km/day、设备级 Precision/Recall、弱异常提前量、跨项目性能下降幅度** 纳入长期基准。
