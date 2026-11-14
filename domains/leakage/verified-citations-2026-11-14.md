# citations.csv 首批正式来源核验（2026-11-14）

> **核验等级：出版商/机构/PubMed 直接确认题名和 DOI。** 每篇的发表年份以出版商正式卷期为准。此处“2026 在线”不等于“2026 正式卷期”；未读取全部付费全文，不声称核实代码和数据下载。

| CSV 序号 | 论文 | 正式年份 | 出版物 | DOI | 方法/主要任务 | 来源 |
|---:|---|---|---|---|---|---|
| 1 | **Interpretable deep learning for acoustic leak detection in water distribution systems** | 2025 | Water Research | [10.1016/j.watres.2024.123076](https://doi.org/10.1016/j.watres.2024.123076) | 多通道 CNN + 多通道 Grad-CAM，解释声学关键频段；水管声学检测、可解释性 | [官方/机构记录](https://pubmed.ncbi.nlm.nih.gov/39756226/) |
| 2 | **A review on gas pipeline leak detection: Acoustic-based, OGI-based, and multimodal fusion methods** | 2025 | Information | [10.3390/info16090731](https://doi.org/10.3390/info16090731) | 声学、光学气体成像（OGI）、多模态方法综述；气体泄漏、跨模态综述 | [官方/机构记录](https://www.mdpi.com/2078-2489/16/9/731) |
| 3 | **Evaluating the generalizability and transferability of acoustic leak detection models for water distribution networks** | 2025 | Water Research | [10.1016/j.watres.2025.124273](https://doi.org/10.1016/j.watres.2025.124273) | 多管网测试、跨管材和管径迁移；比较微调与直接迁移；跨域泛化 | [官方/机构记录](https://pubmed.ncbi.nlm.nih.gov/40716211/) |
| 4 | **Enhanced semi-supervised model for acoustic leak detection in water distribution networks** | 2025 | Automation in Construction | [10.1016/j.autcon.2025.106228](https://doi.org/10.1016/j.autcon.2025.106228) | ESSM 半监督学习、时频增强（SpecAugment）、未标注数据利用；少标注/半监督 | [官方/机构记录](https://www.sciencedirect.com/science/article/pii/S0926580525002687) |
| 17 | **Time-Transformer for acoustic leak detection in water distribution network** | 2025 | Journal of Civil Structural Health Monitoring | [10.1007/s13349-024-00845-2](https://doi.org/10.1007/s13349-024-00845-2) | Transformer 时间建模；香港管网现场试验；检测模型/时序表征 | [官方/机构记录](https://research.polyu.edu.hk/en/publications/time-transformer-for-acoustic-leak-detection-in-water-distributio/) |
| 43 | **Learning from Silence: Unsupervised Deep Learning for Acoustic Leak Detection in Data-Scarce Water Distribution Networks** | 2027（正式卷期；2026 在线） | Reliability Engineering & System Safety | [10.1016/j.ress.2026.113139](https://doi.org/10.1016/j.ress.2026.113139) | 仅正常声训练 AnoGAN，STFT 时频异常评分；作者报告准确率 84.6%、召回 92.5%；无监督/异常检测 | [官方/机构记录](https://www.sciencedirect.com/science/article/pii/S0951832026009488) |

## 需要纠正的书目信息

- **CSV 第 43 篇 Learning from Silence**：附件标为 2026；出版商当前正式卷期是 **2027 年 1 月，第 277 卷，文章 113139**，DOI 中的 2026 是标识年份；本索引同时保留附件原始年份与正式出版年份，避免时间线误标。
- **第 17 篇 Time-Transformer**：正式发表于 2025 年，DOI 末尾 2024 不等于卷期年份。
- **跨域研究**不能直接作为手持式听漏仪的实测效果；**无监督研究**也只是在论文指定管网数据中验证。

## 面向听漏仪的优先实验路线

1. **不同管材/工况泛化（P0）**：第 3 篇跨管网，划分不同管材、管径、压力、安装方式、采集日的独立测试域。报告跨域 AUPRC、固定误报率召回、ECE。
2. **少标注和无泄漏标注建模（P0）**：第 4 篇 ESSM 对比第 43 篇正常样本 AnoGAN，并加入有监督 ResNet18。用 1%、5%、20%、100% 标签量对比，防止时间与管段泄漏。
3. **时序与解释性（P1）**：第 17 篇 Transformer 对比第 1 篇 CNN；分析不同管材、弱泄漏与背景噪声下的特征可解释性。
4. **气体与水管方法不可直接混算（P2）**：第 2 篇主要为工业气体、OGI 和多模态综述，作为技术地图而非水管声学精度排行榜。

## 核验边界

- 当前仅六篇具有独立外部核验；其余附件条目仍为**候选**，不可由 Google Scholar 检索入口推断真实 DOI、PDF 或源码。
- 原先专题已存在的 12 篇不因本次“已出现”而自动获得“出版商已核验”身份。
- 后续以 DOI + 标准化题名 + 作者/正式卷期进行重复排查，避免预印本与正式版双重计数。
