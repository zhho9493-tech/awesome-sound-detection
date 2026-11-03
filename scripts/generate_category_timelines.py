#!/usr/bin/env python3
"""Generate standalone interactive paper timelines for repository categories."""
from __future__ import annotations

import csv
import html
import json
import re
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CATEGORIES = {
    "sound-event": ("声音事件检测", "papers/sound-event/papers-timeline.html"),
    "acoustic-anomaly": ("声学异常检测", "papers/acoustic-anomaly/papers-timeline.html"),
    "das": ("分布式声学传感（DAS）", "domains/das/papers-timeline.html"),
    "leakage": ("泄漏声学检测", "domains/leakage/papers-timeline.html"),
    "speaker-recognition": ("声纹识别", "related/speaker-recognition/papers-timeline.html"),
    "foundation-models": ("音频基础模型", "related/foundation-models/papers-timeline.html"),
    "face-recognition": ("人脸识别", "related/face-recognition/papers-timeline.html"),
    "visual-anomaly": ("图像异常检测", "related/visual-anomaly/papers-timeline.html"),
    "cross-domain": ("跨领域迁移", "cross-domain/papers-timeline.html"),
}

ALIASES = {"speaker": "speaker-recognition", "foundation": "foundation-models"}

CATEGORY_BRIEFS = {
    "sound-event": "声音事件检测与识别", "acoustic-anomaly": "声学异常检测",
    "das": "分布式声学传感", "leakage": "声学泄漏检测",
    "speaker-recognition": "说话人识别", "foundation-models": "音频基础模型",
    "face-recognition": "人脸识别", "visual-anomaly": "图像异常检测",
    "cross-domain": "跨领域迁移",
}

CLUSTERS = {
    "sound-event": {
        "弱监督与少标签": ["weakly supervised", "weak supervision", "semi-supervised", "few-shot", "active learning", "pseudo-label"],
        "基础模型与自监督": ["foundation model", "self-supervised", "pretrained", "pre-trained", "audio-language", "large audio"],
        "定位与空间感知": ["localization", "spatial audio", "sound source localization", "doa", "polyphonic"],
        "鲁棒性与跨域": ["domain adaptation", "domain generalization", "noise robust", "robustness", "out-of-distribution", "open-set"],
        "生物与环境声": ["bioacoustic", "bird", "marine", "soundscape", "ecoacoustic", "wildlife"],
        "轻量化与边缘部署": ["lightweight", "edge deployment", "embedded deployment", "on-device", "tinyml", "low-power"],
    },
    "acoustic-anomaly": {
        "无监督与自监督": ["unsupervised", "self-supervised", "autoencoder", "representation learning"],
        "跨域泛化": ["domain generalization", "domain adaptation", "domain shift", "cross-domain"],
        "开放集与异常拒识": ["open-set", "out-of-distribution", "unknown", "novelty detection"],
        "工业状态监测": ["machine condition", "fault diagnosis", "predictive maintenance", "industrial"],
        "噪声与弱标签": ["noise", "noisy label", "weakly supervised", "pseudo-label"],
    },
    "das": {
        "边缘实时处理": ["edge", "real-time", "lightweight", "efficient"],
        "故障与状态识别": ["fault", "anomaly", "condition monitoring", "diagnosis"],
        "交通与基础设施": ["railway", "pipeline", "traffic", "bridge", "conveyor"],
        "信号表征": ["time-frequency", "representation", "denoising", "signal processing"],
    },
    "leakage": {
        "泄漏定位": ["localization", "locating", "time difference", "cross-correlation"],
        "检测与分类": ["detection", "classification", "recognition"],
        "管网与现场鲁棒性": ["pipeline", "water distribution", "noise", "field", "industrial"],
    },
    "speaker-recognition": {
        "说话人验证": ["speaker verification", "voice verification"],
        "说话人分离": ["speaker diarization", "diarization"],
        "自监督表征": ["self-supervised", "pretrained", "pre-trained", "wav2vec", "hubert"],
        "跨语言与域适应": ["cross-lingual", "domain adaptation", "domain generalization", "multilingual"],
        "隐私与反欺骗": ["spoof", "privacy", "deepfake", "anti-spoofing"],
    },
    "foundation-models": {
        "音频语言模型": ["audio-language", "audio language", "large audio", "audio llm", "multimodal language"],
        "自监督预训练": ["self-supervised", "pretraining", "pre-training", "masked modeling"],
        "音频文本对齐": ["audio-text", "contrastive language-audio", "clap", "text-audio"],
        "推理与代理": ["reasoning", "agent", "instruction", "chain-of-thought"],
        "高效适配": ["adapter", "lora", "parameter-efficient", "prompt tuning", "quantization"],
    },
    "face-recognition": {
        "度量与间隔损失": ["arcface", "margin", "metric learning", "cosine"],
        "噪声标签与长尾": ["noisy label", "noise", "long-tail", "sub-center"],
        "跨域与鲁棒性": ["domain adaptation", "domain generalization", "robust", "cross-domain"],
    },
    "visual-anomaly": {
        "特征记忆与检索": ["patchcore", "memory bank", "nearest neighbor", "retrieval"],
        "分布建模": ["padim", "distribution", "gaussian", "density"],
        "基础模型特征": ["foundation model", "dinov2", "clip", "pretrained"],
        "少样本与零样本": ["few-shot", "zero-shot", "one-shot"],
    },
    "cross-domain": {
        "域泛化": ["domain generalization", "domain shift", "cross-domain"],
        "迁移与适配": ["transfer learning", "domain adaptation", "adapter"],
        "多模态迁移": ["multimodal", "cross-modal", "audio-visual"],
        "开放集": ["open-set", "out-of-distribution", "unknown class"],
    },
}

EVOLUTION_STORIES = {
    "sound-event": [
        ("从手工声学特征与监督分类，走向事件级检测与时空定位", "早期工作从频谱、时频纹理和监督分类器出发，逐步把任务从整段声音标签扩展到事件起止时间、声源方向与多事件共存条件下的联合检测。"),
        ("从封闭集事件识别，迈向弱监督、跨域鲁棒与多声源联合建模", "研究开始减少对强时间标注的依赖，引入弱监督、伪标签和域泛化；同时处理噪声干扰、设备差异与复调场景，使模型从标准数据集识别走向真实声景适配。"),
        ("从专用检测器，迈向基础模型驱动的开放世界感知与音频推理", "近期方法利用自监督预训练和音频语言模型统一表征检测、定位与语义理解，并进一步关注开放集事件、长音频推理、端侧部署和跨任务迁移。"),
    ],
    "acoustic-anomaly": [
        ("从固定声学阈值与重构误差，走向无监督机器状态表征", "研究由人工阈值和单一频谱指标转向自编码器与表征学习，在只有正常样本的条件下建立设备健康基线。"),
        ("从单设备异常分数，迈向跨域泛化与噪声鲁棒诊断", "方法开始显式处理机器型号、采集环境和运行工况造成的域偏移，并通过域适应、伪标签和噪声建模降低现场误报。"),
        ("从异常判别，迈向物理约束的健康状态推理与开放集诊断", "近期工作把周期性、结构先验和工况信息引入模型，从二元异常检测扩展到故障类型、严重度、未知异常拒识与健康演化推理。"),
    ],
    "das": [
        ("从光纤振动可视化，走向时空事件检测与位置识别", "早期研究侧重从长距离光纤信号中恢复可解释振动模式，并建立事件发生位置与时间的基础检测能力。"),
        ("从单点信号分类，迈向空间一致性与多通道联合建模", "方法开始利用相邻通道、传播结构与周期规律，抑制环境干扰并提升交通、管线和工业设备事件的定位稳定性。"),
        ("从离线识别，迈向物理约束的边缘诊断与健康状态推理", "近期工作强调轻量网络、实时推理和工况约束，将DAS从事件告警扩展到故障类型、未知状态和连续健康评估。"),
    ],
    "leakage": [
        ("从声压阈值告警，走向泄漏声纹识别", "研究由简单能量变化判断转向频谱特征和监督分类，以区分泄漏声与泵机、交通及环境背景噪声。"),
        ("从是否泄漏，迈向传播建模与声源定位", "方法进一步结合互相关、到达时差和管网传播特性，在不同材质、压力与传感器布设条件下估计泄漏位置。"),
        ("从实验室检测，迈向复杂现场的鲁棒定位与泄漏状态推理", "近期工作关注域偏移、弱泄漏、混合噪声和多传感器融合，并尝试同时判断位置、泄漏率与可信度。"),
    ],
    "speaker-recognition": [
        ("从人工声纹特征与概率模型，走向深度说话人嵌入", "研究由声学统计特征转向端到端嵌入学习，使验证和识别能够在统一度量空间中完成。"),
        ("从单语封闭集验证，迈向跨语言、跨设备与在线说话人建模", "方法开始处理语言、信道和场景偏移，并把验证扩展到说话人分离、连续注册与多用户记忆。"),
        ("从专用声纹网络，迈向自监督基础表征与隐私安全联合优化", "近期工作利用大规模语音预训练提升低资源泛化，同时强化反欺骗、深度伪造检测、隐私保护和端侧适配。"),
    ],
    "foundation-models": [
        ("从单任务音频编码器，走向大规模自监督预训练", "模型由针对分类或识别的专用网络，转向利用海量无标签音频学习可迁移的通用声学表征。"),
        ("从纯音频表征，迈向音频文本对齐与零样本迁移", "对比学习把声音与自然语言映射到共享语义空间，使检索、开放词表分类和跨任务迁移不再完全依赖专门标注。"),
        ("从感知表征，迈向多模态指令理解、长音频推理与智能体", "近期模型把检测、描述、问答和推理统一进音频语言框架，并探索参数高效适配、检索增强和递归自改进。"),
    ],
    "face-recognition": [
        ("从欧氏特征匹配，走向角度间隔判别学习", "方法通过归一化特征和角度间隔损失增强类间分离，使人脸嵌入具备更稳定的身份判别边界。"),
        ("从单中心身份原型，迈向多子中心与噪声标签建模", "研究开始为同一身份建立多个子中心，以吸收姿态、质量和错误标签造成的类内多样性。"),
        ("从标准基准识别，迈向长尾、跨域与开放世界身份验证", "后续方向进一步处理低质量图像、未知身份、隐私约束和跨设备部署条件下的可靠性。"),
    ],
    "visual-anomaly": [
        ("从重构误差，走向预训练特征的局部异常度量", "方法由像素重构转向深层特征空间，在不生成图像的情况下比较正常模式与局部缺陷。"),
        ("从全局异常分数，迈向记忆库检索与像素级定位", "Patch级特征记忆和分布建模提升了细粒度缺陷定位能力，并减少对异常样本的依赖。"),
        ("从单类别工业检测，迈向基础模型驱动的少样本与零样本泛化", "近期研究利用视觉基础模型和文本语义，把异常检测扩展到新类别、新工厂和开放词表描述。"),
    ],
    "cross-domain": [
        ("从源域监督拟合，走向可迁移的共享表征学习", "研究首先通过特征对齐和迁移学习，降低源域与目标域在设备、环境和数据分布上的差异。"),
        ("从目标域适配，迈向未知目标域的泛化与开放集拒识", "方法不再假设可访问目标域数据，而是通过域泛化、元学习和不确定性估计提升对新场景的适应能力。"),
        ("从单模态迁移，迈向多模态先验、基础模型与持续适应", "近期工作结合文本、视觉和物理先验，在参数高效更新的同时处理类别增量、未知类别与长期分布漂移。"),
    ],
}

# Evidence terms are intentionally independent of publication year.  A paper is
# linked to an evolution narrative only when its title or abstract contains a
# method/task signal that can substantively support that narrative.  Papers may
# support more than one transition.
EVOLUTION_EVIDENCE_TERMS = {
    "sound-event": [
        ["spectrogram", "time-frequency", "acoustic feature", "mfcc", "event detection", "sound event detection", "localization", "spatial audio", "direction of arrival", "doa", "seld", "onset", "offset", "polyphonic"],
        ["weakly supervised", "weak supervision", "semi-supervised", "pseudo-label", "few-shot", "active learning", "domain adaptation", "domain generalization", "cross-domain", "robust", "noise", "multi-source", "polyphonic", "data augmentation", "real scene"],
        ["foundation model", "self-supervised", "pretrained", "pre-trained", "audio-language", "audio language", "large audio", "lalm", "open-set", "open set", "open-vocabulary", "open vocabulary", "zero-shot", "reasoning", "long audio", "instruction", "lightweight", "edge deployment", "on-device", "multi-task"],
    ],
    "acoustic-anomaly": [
        ["threshold", "reconstruction error", "autoencoder", "unsupervised", "normal data", "representation learning"],
        ["domain adaptation", "domain generalization", "domain shift", "cross-domain", "robust", "noise", "pseudo-label"],
        ["physics-informed", "physical constraint", "health state", "severity", "open-set", "unknown anomaly", "fault diagnosis", "prognostic"],
    ],
    "das": [
        ["visualization", "event detection", "localization", "location", "distributed acoustic sensing"],
        ["spatial", "multi-channel", "adjacent channel", "propagation", "denoising", "classification"],
        ["physics-informed", "edge", "real-time", "lightweight", "fault", "health monitoring", "diagnosis"],
    ],
    "leakage": [
        ["threshold", "spectral", "classification", "leak detection", "acoustic emission"],
        ["localization", "time difference", "cross-correlation", "propagation", "pipeline", "source location"],
        ["domain adaptation", "robust", "weak leak", "sensor fusion", "leak rate", "uncertainty", "field"],
    ],
    "speaker-recognition": [
        ["i-vector", "x-vector", "embedding", "speaker verification", "metric learning"],
        ["cross-lingual", "multilingual", "cross-device", "domain adaptation", "diarization", "online", "continual"],
        ["self-supervised", "pretrained", "pre-trained", "spoof", "deepfake", "privacy", "on-device", "foundation model"],
    ],
    "foundation-models": [
        ["self-supervised", "pretraining", "pre-training", "masked modeling", "representation learning"],
        ["audio-text", "audio text", "contrastive language-audio", "clap", "zero-shot", "retrieval", "open-vocabulary"],
        ["audio-language", "audio language", "instruction", "reasoning", "agent", "long audio", "adapter", "lora", "retrieval augmented"],
    ],
    "face-recognition": [
        ["arcface", "angular margin", "cosine margin", "metric learning"],
        ["sub-center", "subcenter", "noisy label", "multiple prototype", "intra-class"],
        ["long-tail", "domain adaptation", "domain generalization", "open-set", "unknown identity", "privacy", "low quality"],
    ],
    "visual-anomaly": [
        ["reconstruction", "pretrained feature", "feature space", "anomaly score"],
        ["memory bank", "patchcore", "padim", "nearest neighbor", "pixel-level", "localization"],
        ["foundation model", "dinov2", "clip", "few-shot", "zero-shot", "open-vocabulary", "cross-domain"],
    ],
    "cross-domain": [
        ["transfer learning", "feature alignment", "shared representation", "domain adaptation"],
        ["domain generalization", "unseen domain", "open-set", "out-of-distribution", "uncertainty", "meta-learning"],
        ["multimodal", "cross-modal", "foundation model", "continual", "class-incremental", "adapter", "parameter-efficient"],
    ],
}

EVOLUTION_SUBTRENDS = {
    "sound-event": [
        {
            "时频表征与深度声学编码": ["spectrogram", "time-frequency", "acoustic feature", "mfcc", "convolutional", "cnn", "crnn"],
            "事件起止检测与时间边界建模": ["event detection", "sound event detection", "onset", "offset", "temporal detection", "frame-level"],
            "声源定位与空间声学建模": ["localization", "spatial audio", "direction of arrival", "doa", "seld", "ambisonic"],
            "复调事件与检测定位联合建模": ["polyphonic", "multi-source", "joint detection and localization", "sound event localization and detection"],
        },
        {
            "弱监督、半监督与伪标签学习": ["weakly supervised", "weak supervision", "semi-supervised", "pseudo-label", "mean teacher"],
            "少样本学习与数据增广": ["few-shot", "one-shot", "active learning", "data augmentation", "synthetic soundscape"],
            "跨域适配与域泛化": ["domain adaptation", "domain generalization", "cross-domain", "domain shift", "unseen domain"],
            "噪声鲁棒与真实声景适配": ["robust", "noise", "noisy", "real scene", "reverberant", "interference"],
            "多声源分离与复调场景建模": ["multi-source", "polyphonic", "source separation", "overlapping sound"],
        },
        {
            "自监督预训练与通用音频表征": ["self-supervised", "pretrained", "pre-trained", "foundation model", "universal audio representation"],
            "音频语言模型与跨模态语义对齐": ["audio-language", "audio language", "large audio", "lalm", "audio-text", "multimodal language"],
            "开放词表与零样本事件感知": ["open-set", "open set", "open-vocabulary", "open vocabulary", "zero-shot", "unknown event"],
            "长音频理解与多步音频推理": ["long audio", "long-form audio", "reasoning", "instruction", "question answering", "chain-of-thought"],
            "检测、定位与理解的多任务统一建模": ["multi-task", "unified framework", "unified model", "object-centric", "joint model"],
            "轻量化适配与端侧部署": ["lightweight", "edge deployment", "embedded", "on-device", "tinyml", "low-power", "quantization"],
        },
    ],
}


def normalize_title(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.casefold()).strip()


def brief_summary(value: str, fallback: str, limit: int = 50) -> str:
    text = " ".join((value or "").split())
    if text:
        text = re.split(r"(?<=[.!?。！？])\s+", text, maxsplit=1)[0]
        text = re.sub(r"^(we (?:present|propose|introduce|develop|study|investigate)\s+)", "", text, flags=re.I)
    if not text:
        text = f"聚焦{fallback}相关方法与实验验证"
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def date_for(row: dict) -> str | None:
    for key in ("published", "updated"):
        if re.match(r"20\d\d-\d\d-\d\d", row.get(key, "")):
            return row[key][:10]
    arxiv = row.get("arxiv_id") or row.get("id", "")
    match = re.fullmatch(r"(\d{2})(\d{2})\.\d{4,5}", arxiv or "")
    if match:
        year = 2000 + int(match.group(1))
        month = min(12, max(1, int(match.group(2))))
        return f"{year:04d}-{month:02d}-01"
    match = re.search(r"(?<!\d)(20\d{2})(?:[-_/](\d{2})(?:[-_/](\d{2}))?)?", row.get("title", ""))
    if match:
        return f"{match.group(1)}-{match.group(2) or '01'}-{match.group(3) or '01'}"
    return None


def paper_from(row: dict, category: str, source: str) -> dict | None:
    date = date_for(row)
    if not date:
        return None
    ident = row.get("arxiv_id") or (row.get("id") if re.fullmatch(r"\d{4}\.\d{4,5}", row.get("id", "")) else None)
    abs_url = row.get("abs_url") or row.get("public_url") or (f"https://arxiv.org/abs/{ident}" if ident else None)
    pdf_url = row.get("pdf_url") or (f"https://arxiv.org/pdf/{ident}" if ident else row.get("download_url"))
    title = row.get("title", "Untitled")
    return {
        "id": ident or row.get("id") or normalize_title(row.get("title", ""))[:60],
        "title": title,
        "date": date,
        "authors": row.get("authors", []) if isinstance(row.get("authors"), list) else [],
        "abstract": row.get("abstract", ""),
        "abs": abs_url,
        "pdf": pdf_url,
        "source": source,
        "category": category,
        "brief": brief_summary(row.get("abstract", ""), title),
        "has_abstract": bool(row.get("abstract")),
    }


def load_data() -> dict[str, list[dict]]:
    master = json.loads((ROOT / "resources/paper-master-index.json").read_text(encoding="utf-8"))["records"]
    cs_sd = json.loads((ROOT / "resources/arxiv-cs-sd/papers.json").read_text(encoding="utf-8"))["records"]
    catalog = json.loads((ROOT / "resources/catalog.json").read_text(encoding="utf-8"))["resources"]
    grouped = defaultdict(list)
    for row in cs_sd:
        for raw in row.get("repository_categories", []):
            category = ALIASES.get(raw, raw)
            if category in CATEGORIES:
                paper = paper_from(row, category, "arXiv cs.SD")
                if paper:
                    grouped[category].append(paper)
    for row in master:
        category = row.get("primary_category")
        if category in CATEGORIES:
            paper = paper_from(row, category, "仓库论文主索引")
            if paper:
                grouped[category].append(paper)
        title = (row.get("title") or "").casefold()
        inferred = None
        if any(k in title for k in ("face recognition", "facial recognition", "arcface")):
            inferred = "face-recognition"
        elif any(k in title for k in ("visual anomaly", "image anomaly", "industrial defect", "surface defect", "patchcore", "padim")):
            inferred = "visual-anomaly"
        if inferred:
            paper = paper_from(row, inferred, "仓库论文主索引（标题归类）")
            if paper:
                grouped[inferred].append(paper)
    for row in catalog:
        category = row.get("domain")
        if row.get("type") == "paper" and category in CATEGORIES:
            ident_match = re.search(r"arxiv\.org/abs/(\d{4}\.\d{4,5})", row.get("url", ""))
            paper = paper_from({"id": ident_match.group(1) if ident_match else row["id"], "title": row["title"], "public_url": row.get("url"), "pdf_url": row.get("pdf_url")}, category, "资源目录")
            if paper:
                grouped[category].append(paper)
    for category, papers in grouped.items():
        dedup = {}
        for paper in papers:
            key = paper["id"] if re.fullmatch(r"\d{4}\.\d{4,5}", str(paper["id"])) else normalize_title(paper["title"])
            current = dedup.get(key)
            if not current or (paper.get("abstract") and not current.get("abstract")):
                dedup[key] = paper
        grouped[category] = sorted(dedup.values(), key=lambda p: (p["date"], p["title"]))
    return grouped


def classify_themes(papers: list[dict], category: str) -> None:
    clusters = CLUSTERS.get(category, {})
    for paper in papers:
        text = (paper["title"] + " " + paper.get("abstract", "")).casefold()
        paper["themes"] = [name for name, terms in clusters.items() if any(term in text for term in terms)] or ["其他"]
        paper["brief"] = chinese_brief(text, category, paper["themes"])


def chinese_brief(text: str, category: str, themes: list[str]) -> str:
    method_rules = [
        (("foundation model", "large audio", "audio-language", "audio language"), "基础模型"),
        (("self-supervised", "self supervised"), "自监督学习"),
        (("weakly supervised", "weak supervision"), "弱监督学习"),
        (("transformer", "attention"), "注意力模型"),
        (("contrastive",), "对比学习"), (("graph neural", "gnn"), "图神经网络"),
        (("few-shot", "few shot"), "少样本学习"), (("domain adaptation", "domain generalization"), "跨域学习"),
        (("convolutional", "cnn"), "卷积网络"),
    ]
    scene_rules = [
        (("underwater", "marine", "vessel", "dolphin", "whale"), "水下声场景"),
        (("bird", "bioacoustic", "ecoacoustic", "wildlife"), "生物与环境声场景"),
        (("industrial", "machine", "motor", "bearing", "conveyor"), "工业设备场景"),
        (("urban", "smart city", "traffic"), "城市声景"),
        (("medical", "heart sound", "respiratory", "cough"), "医疗生理声场景"),
        (("speaker", "speech", "voice"), "语音与说话人场景"),
    ]
    task_rules = [
        (("localization", "direction of arrival", "seld"), "声源定位"),
        (("source separation", "sound separation"), "声源分离"),
        (("classification", "recognition"), "分类识别"),
        (("detection", "detecting"), "目标检测"),
        (("verification",), "身份验证"), (("diarization",), "说话人分离"),
        (("reasoning",), "音频推理"), (("anomaly", "fault"), "异常与故障识别"),
    ]
    def pick(rules, fallback):
        return next((name for terms, name in rules if any(term in text for term in terms)), fallback)
    method = pick(method_rules, "数据驱动方法")
    scene = pick(scene_rules, "通用声学场景")
    task = pick(task_rules, CATEGORY_BRIEFS.get(category, "相关任务"))
    if themes and themes[0] != "其他" and method == "数据驱动方法":
        method = themes[0]
    value = f"采用{method}，面向{scene}开展{task}研究。"
    return value if len(value) <= 50 else value[:49] + "…"


def insight_for(label: str, subset: list[dict], previous: list[dict] | None = None) -> dict:
    counts = Counter(theme for paper in subset for theme in paper["themes"] if theme != "其他")
    leaders = counts.most_common(3)
    themes = [name for name, _ in leaders]
    previous_counts = Counter(theme for paper in (previous or []) for theme in paper["themes"] if theme != "其他")
    previous_leaders = previous_counts.most_common(2)
    rising = None
    if counts and previous:
        current_n, previous_n = max(1, len(subset)), max(1, len(previous))
        candidates = [(counts[t] / current_n - previous_counts[t] / previous_n, t) for t in counts if counts[t] >= 2]
        if candidates:
            delta, name = max(candidates)
            if delta > 0:
                rising = {"name": name, "delta": delta}
    examples = []
    for paper in reversed(subset):
        if not themes or any(theme in paper["themes"] for theme in themes[:2]):
            examples.append({"title": paper["title"], "brief": paper["brief"], "url": paper.get("abs") or paper.get("pdf") or "#"})
        if len(examples) == 3:
            break
    if themes:
        origin = "、".join(name for name, _ in previous_leaders) if previous_leaders else "基础任务与可行性验证"
        destination = "、".join(themes[:2])
        transition_title = f"从{origin}走向{destination}"
        narrative = f"{label} 呈现出从{origin}向{destination}的技术迁移"
        if rising:
            narrative += f"，其中{rising['name']}的论文占比较上一阶段上升 {rising['delta']:+.1%}"
        narrative += "。"
    else:
        transition_title = "从问题定义走向方法验证"
        narrative = f"{label} 当前可识别主题样本较少，建议结合代表论文人工复核。"
    return {"label": label, "count": len(subset), "themes": leaders, "transition_title": transition_title, "narrative": narrative, "examples": examples}


def build_evolution(papers: list[dict], category: str) -> tuple[list[dict], dict, str]:
    years = sorted({int(p["date"][:4]) for p in papers})
    if not years:
        return [], {}, "当前没有可定年的论文记录。"
    phase_ranges = []
    if years[-1] - years[0] >= 5:
        phase_ranges = [(years[0], min(2021, years[-1])), (max(years[0], 2022), min(2024, years[-1])), (max(years[0], 2025), years[-1])]
        phase_ranges = [(a, b) for a, b in phase_ranges if a <= b]
    else:
        chunk = max(1, (len(years) + 2) // 3)
        for i in range(0, len(years), chunk):
            phase_ranges.append((years[i], years[min(len(years) - 1, i + chunk - 1)]))
    phases, previous = [], None
    for start, end in phase_ranges:
        subset = [p for p in papers if start <= int(p["date"][:4]) <= end]
        label = str(start) if start == end else f"{start}–{end}"
        info = insight_for(label, subset, previous)
        info["start"], info["end"] = start, end
        phases.append(info)
        previous = subset
    stories = EVOLUTION_STORIES.get(category, [])
    for index, phase in enumerate(phases):
        if stories:
            story_index = min(index, len(stories) - 1)
            phase["transition_title"], phase["narrative"] = stories[story_index]
            phase["narrative"] += f" 本阶段由 {phase['count']} 篇可定年论文提供证据。"
    annual = {}
    previous = None
    for year in years:
        subset = [p for p in papers if int(p["date"][:4]) == year]
        annual[str(year)] = insight_for(str(year), subset, previous)
        previous = subset
        if stories and phase_ranges:
            phase_index = next((i for i, (start, end) in enumerate(phase_ranges) if start <= year <= end), len(stories) - 1)
            story_title, story_text = stories[min(phase_index, len(stories) - 1)]
            annual[str(year)]["transition_title"] = story_title
            annual[str(year)]["narrative"] = story_text + f" {year} 年收录 {len(subset)} 篇论文，代表性工作如下。"
    recent = [p for p in papers if p["date"][:4] in {"2025", "2026"}]
    before_recent = [p for p in papers if p["date"][:4] == "2024"]
    if recent:
        annual["2025–2026"] = insight_for("2025–2026", recent, before_recent)
        if stories:
            annual["2025–2026"]["transition_title"], annual["2025–2026"]["narrative"] = stories[-1]
            annual["2025–2026"]["narrative"] += f" 该判断由 2025—2026 年收录的 {len(recent)} 篇论文及代表性工作支撑。"
    overall_counts = Counter(theme for paper in papers for theme in paper["themes"] if theme != "其他")
    leaders = [name for name, _ in overall_counts.most_common(3)]
    if stories:
        overall = f"整体上，{stories[0][0]}；随后{stories[min(1, len(stories)-1)][0]}；近期则{stories[-1][0]}。"
    elif phases and len(phases) > 1:
        overall = f"整体上，技术路线从{('、'.join(t for t, _ in phases[0]['themes'][:2]) or '基础任务探索')}，经过{('、'.join(t for t, _ in phases[len(phases)//2]['themes'][:2]) or '方法扩展')}，逐步走向{('、'.join(t for t, _ in phases[-1]['themes'][:2]) or '系统化应用')}。"
    else:
        overall = f"当前论文主要围绕{'、'.join(leaders) if leaders else '多类研究任务'}展开。"
    overall += " 该判断由本页论文的标题、摘要与年份聚合得到。"
    return phases, annual, overall


def escape_json(value) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")


def attach_evolution_evidence(papers: list[dict], category: str, phases: list[dict]) -> None:
    rules = EVOLUTION_EVIDENCE_TERMS.get(category, [])
    subtrend_rules = EVOLUTION_SUBTRENDS.get(category, [])
    for paper in papers:
        text = " ".join((paper.get("title", ""), paper.get("abstract", ""))).casefold()
        paper["evolution_trends"] = [
            phase["transition_title"]
            for index, phase in enumerate(phases)
            if index < len(rules) and any(term in text for term in rules[index])
        ]
        paper["evolution_subtrends"] = [
            name
            for group in subtrend_rules
            for name, terms in group.items()
            if any(term in text for term in terms)
        ]
        for index, group in enumerate(subtrend_rules):
            if index < len(phases) and any(name in paper["evolution_subtrends"] for name in group):
                title = phases[index]["transition_title"]
                if title not in paper["evolution_trends"]:
                    paper["evolution_trends"].append(title)
    for index, phase in enumerate(phases):
        title = phase["transition_title"]
        evidence_count = sum(title in paper["evolution_trends"] for paper in papers)
        phase["evidence_count"] = evidence_count
        phase["subtrends"] = [
            {"name": name, "count": sum(name in paper["evolution_subtrends"] for paper in papers)}
            for name in (subtrend_rules[index] if index < len(subtrend_rules) else {})
        ]
        phase["narrative"] = re.sub(
            r" 本阶段由 \d+ 篇可定年论文提供证据。$",
            f" 共有 {evidence_count} 篇论文在标题或摘要中直接体现这一技术变化。",
            phase["narrative"],
        )


def align_annual_evidence(papers: list[dict], annual: dict) -> None:
    for key, info in annual.items():
        years = {int(value) for value in re.findall(r"20\d{2}", key)}
        if len(years) == 2:
            years = set(range(min(years), max(years) + 1))
        evidence = [
            paper for paper in papers
            if int(paper["date"][:4]) in years
            and info["transition_title"] in paper.get("evolution_trends", [])
        ]
        base = re.split(r" (?:(?:20\d{2}) 年收录|该判断由 20\d{2})", info["narrative"], maxsplit=1)[0]
        info["narrative"] = f"{base} {key} 年段共有 {len(evidence)} 篇论文直接支撑这一变化，以下列出近期代表工作。"
        info["examples"] = [
            {"title": paper["title"], "brief": paper["brief"], "url": paper.get("abs") or paper.get("pdf") or "#"}
            for paper in evidence[-3:][::-1]
        ]


def build_html(category: str, title: str, papers: list[dict]) -> str:
    classify_themes(papers, category)
    phases, annual, overall = build_evolution(papers, category)
    attach_evolution_evidence(papers, category, phases)
    align_annual_evidence(papers, annual)
    evolution_trends = list(dict.fromkeys(phase["transition_title"] for phase in phases))
    years = sorted({paper["date"][:4] for paper in papers})
    min_date = papers[0]["date"] if papers else "—"
    max_date = papers[-1]["date"] if papers else "—"
    phase_parts = []
    for index, phase in enumerate(phases):
        subtrend_html = "".join(
            f'<button type="button" class="subtrend-chip" data-major="{html.escape(phase["transition_title"])}" data-subtrend="{html.escape(item["name"])}">{html.escape(item["name"])} <b>{item["count"]}</b></button>'
            for item in phase["subtrends"]
        )
        card = f'<article class="phase"><div class="phase-top"><span>{html.escape(phase["label"])}</span><b>{phase["evidence_count"]} 篇支撑论文</b></div><h3>{html.escape(phase["transition_title"])}</h3><p>{html.escape(phase["narrative"])}</p><div class="subtrend-list">{subtrend_html}</div></article>'
        if index:
            phase_parts.append('<div class="transition" aria-hidden="true"><span>→</span><small>研究重点过渡</small></div>')
        phase_parts.append(card)
    phase_html = "".join(phase_parts)
    annual_keys = list(annual)
    default_annual = "2025–2026" if "2025–2026" in annual else (annual_keys[-1] if annual_keys else "")
    year_buttons = "".join(f'<button type="button" class="year-chip{" active" if key == default_annual else ""}" data-insight="{html.escape(key)}">{html.escape(key)}</button>' for key in annual_keys)
    options_theme = '<option value="">全部技术趋势</option>' + "".join(
        f'<option value="{html.escape(t)}">{html.escape(t)}</option>' for t in evolution_trends
    )
    subtrend_groups = {
        phase["transition_title"]: [item["name"] for item in phase["subtrends"]]
        for phase in phases
    }
    data = escape_json(papers)
    annual_data = escape_json(annual)
    subtrend_data = escape_json(subtrend_groups)
    template = '''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>__TITLE__论文时间线</title>
<style>
:root{--bg:#f6f8fb;--panel:#fff;--text:#172033;--muted:#647085;--line:#d8deea;--accent:#1667d9;--accent2:#14a38b;--soft:#eaf2ff;--shadow:0 12px 30px rgba(23,32,51,.08)}
@media(prefers-color-scheme:dark){:root{--bg:#10141d;--panel:#171d28;--text:#edf2ff;--muted:#a9b3c7;--line:#303a4c;--accent:#6aa6ff;--accent2:#5fd1bc;--soft:#1b2c48;--shadow:none}}
*{box-sizing:border-box} body{margin:0;background:var(--bg);color:var(--text);font:15px/1.6 system-ui,-apple-system,"Segoe UI",sans-serif} a{color:var(--accent)} .wrap{max-width:1380px;margin:auto;padding:28px 24px 60px} header{display:grid;gap:18px} h1{font-size:clamp(28px,4vw,48px);line-height:1.1;margin:0} .subtitle{color:var(--muted);max-width:920px} .stats{display:flex;gap:12px;flex-wrap:wrap}.stat{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:12px 16px;box-shadow:var(--shadow)}.stat b{font-size:22px;display:block}
.trend-shell{position:relative;overflow:hidden;background:linear-gradient(135deg,var(--panel),var(--soft));border:1px solid var(--line);border-radius:24px;padding:26px;box-shadow:var(--shadow)}.trend-shell:before{content:"";position:absolute;width:280px;height:280px;border-radius:50%;right:-110px;top:-150px;background:var(--accent);opacity:.07}.trend-head{position:relative;display:grid;grid-template-columns:minmax(0,1.6fr) minmax(250px,.7fr);gap:28px;align-items:end}.eyebrow{display:block;color:var(--accent);font-weight:700;letter-spacing:.12em;font-size:12px}.trend-head h2{margin:4px 0 7px;font-size:clamp(23px,3vw,34px);line-height:1.25}.trend-head p{margin:0;color:var(--muted)}.trend-note{border-left:3px solid var(--accent2);padding-left:15px;color:var(--muted)}
.phase-flow{position:relative;display:flex;align-items:stretch;gap:10px;margin-top:24px}.phase{flex:1;min-width:0;background:var(--panel);border:1px solid var(--line);border-radius:18px;padding:17px;position:relative}.phase-top{display:flex;align-items:center;justify-content:space-between;color:var(--muted);font-size:12px}.phase-top span{color:var(--accent);font-weight:700}.phase h3{margin:7px 0 5px;font-size:17px}.phase p{margin:0 0 13px;color:var(--muted);font-size:13px;min-height:42px}.subtrend-list{display:flex;gap:6px;flex-wrap:wrap}.subtrend-chip{padding:5px 8px;border-radius:999px;background:var(--soft);font-size:11px;text-align:left}.subtrend-chip b{color:var(--accent);margin-left:3px}.subtrend-chip:hover{border-color:var(--accent)}.transition{width:72px;display:flex;flex-direction:column;justify-content:center;align-items:center;color:var(--accent)}.transition span{font-size:25px}.transition small{color:var(--muted);white-space:nowrap;font-size:10px}.theme-bars{display:grid;gap:7px}.theme-bar{display:grid;grid-template-columns:92px 1fr 28px;gap:7px;align-items:center;font-size:11px;color:var(--muted)}.theme-bar span{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.theme-bar i{display:block;height:5px;border-radius:99px;background:linear-gradient(90deg,var(--accent),var(--accent2));width:var(--w)}.theme-bar b{text-align:right}
.year-explorer{margin-top:18px;display:grid;grid-template-columns:minmax(250px,.55fr) minmax(0,1.45fr);gap:16px}.year-nav{display:flex;gap:7px;align-content:flex-start;flex-wrap:wrap}.year-chip{font:inherit;color:var(--text);background:var(--panel);border:1px solid var(--line);border-radius:999px;padding:7px 12px;cursor:pointer}.year-chip.active{background:var(--accent);border-color:var(--accent);color:#fff}.year-insight{background:var(--panel);border:1px solid var(--line);border-radius:16px;padding:16px;min-height:150px}.year-insight h3{margin:0 0 5px}.year-insight p{margin:0 0 10px;color:var(--muted)}.year-tags{display:flex;gap:7px;flex-wrap:wrap;margin-bottom:10px}.year-tags span{background:var(--soft);border-radius:99px;padding:4px 9px;font-size:12px}.year-evidence{display:grid;gap:5px}.year-evidence a{text-decoration:none;font-size:12px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
main{margin-top:22px;background:var(--panel);border:1px solid var(--line);border-radius:18px;padding:18px;box-shadow:var(--shadow)}.controls{display:flex;gap:10px;flex-wrap:wrap;align-items:end}input,select,button{font:inherit;color:var(--text);background:var(--panel);border:1px solid var(--line);border-radius:9px;padding:9px 11px}.controls>input[type=search]{min-width:250px;flex:1}.filter-label{display:grid;gap:3px;color:var(--muted);font-size:11px}.filter-label input,.filter-label select{min-width:145px;color:var(--text);font-size:14px}.filter-label select{min-width:185px}button{cursor:pointer;background:var(--soft)}.count{margin-left:auto;color:var(--muted);align-self:center}.chart{position:relative;margin-top:16px}svg{display:block;width:100%;height:auto;min-height:400px}.axis,.curve{fill:none;stroke:var(--line)}.curve{stroke:var(--accent);stroke-width:2.2;opacity:.65}.axis-text,.node-label{fill:var(--muted);font-size:11px}.node-summary{fill:var(--muted);font-size:9px}.point{fill:var(--accent2);stroke:var(--panel);stroke-width:1.5;cursor:pointer}.point:hover,.point.active{fill:var(--accent);stroke-width:3}.tooltip{position:absolute;display:none;max-width:390px;background:var(--text);color:var(--bg);border-radius:11px;padding:11px 13px;font-size:12px;pointer-events:none;z-index:4}.tooltip em{display:block;margin-top:5px;opacity:.78;font-style:normal}.detail{display:grid;grid-template-columns:1fr auto;gap:12px;margin-top:8px;padding:14px;border-top:1px solid var(--line)}.detail h2{font-size:18px;margin:0 0 4px}.detail p{margin:0;color:var(--muted)}.detail .brief{color:var(--text);font-weight:600;margin:5px 0}.actions{display:flex;gap:8px;align-items:start}.actions a{text-decoration:none;border:1px solid var(--line);border-radius:8px;padding:7px 10px;white-space:nowrap}.empty{padding:80px 20px;text-align:center;color:var(--muted)}
@media(max-width:900px){.trend-head,.year-explorer{grid-template-columns:1fr}.phase-flow{display:grid}.transition{width:auto;height:38px}.transition span{transform:rotate(90deg)}.phase p{min-height:0}.count{width:100%;margin:0}.detail{grid-template-columns:1fr}.wrap{padding:20px 12px 40px}}
</style></head><body><div class="wrap">
<header><div><h1>__TITLE__论文时间线</h1><p class="subtitle">基于仓库当前论文索引生成。曲线按发表时间排列；节点可悬停查看、点击展开摘要并打开官方页面或下载 PDF。趋势结论只依赖本页收录论文及其标题、摘要和时间，不外推为完整学科计量。</p></div>
<section class="trend-shell" aria-label="技术趋势演进"><div class="trend-head"><div><span class="eyebrow">TECHNOLOGY EVOLUTION</span><h2>从整体脉络到年度过渡</h2><p>__OVERALL__</p></div><div class="trend-note">先阅读三个阶段的研究重心迁移，再选择具体年份查看当年主线、相对上一年的变化与代表论文。默认突出 2025—2026 的最新过渡。</div></div><div class="phase-flow">__PHASES__</div><div class="year-explorer"><nav class="year-nav" aria-label="选择年度趋势">__YEAR_BUTTONS__</nav><article id="year-insight" class="year-insight" aria-live="polite"></article></div></section></header>
<main><div class="controls"><input id="search" type="search" placeholder="搜索标题、中文简述、摘要或作者" aria-label="搜索论文"><label class="filter-label">技术趋势<select id="theme" aria-label="选择技术趋势">__THEME_OPTIONS__</select></label><label class="filter-label">细分技术趋势<select id="subtrend" aria-label="选择细分技术趋势"><option value="">全部细分趋势</option></select></label><label class="filter-label">开始日期<input id="start-date" type="date" min="__MIN_DATE__" max="__MAX_DATE__"></label><label class="filter-label">结束日期<input id="end-date" type="date" min="__MIN_DATE__" max="__MAX_DATE__"></label><button id="clear-range" type="button">清除时间段</button><button id="export" type="button">导出当前 CSV</button><span id="count" class="count"></span></div>
<div class="chart"><svg id="timeline" viewBox="0 0 1200 420" role="img" aria-label="可交互论文时间线"></svg><div id="tooltip" class="tooltip"></div></div>
<section id="detail" class="detail" aria-live="polite"><div><h2>选择曲线上的论文节点</h2><p>悬停可快速查看，点击节点显示摘要与下载入口。</p></div></section></main></div>
<script>
const papers=__PAPER_DATA__, annualInsights=__ANNUAL_DATA__, subtrendGroups=__SUBTREND_DATA__, defaultInsight='__DEFAULT_ANNUAL__'; const svg=document.getElementById('timeline'), tip=document.getElementById('tooltip'), detail=document.getElementById('detail'), search=document.getElementById('search'), theme=document.getElementById('theme'), subtrend=document.getElementById('subtrend'), startDate=document.getElementById('start-date'), endDate=document.getElementById('end-date'), count=document.getElementById('count');
const NS='http://www.w3.org/2000/svg'; const E=(name,attrs={})=>{const e=document.createElementNS(NS,name);Object.entries(attrs).forEach(([k,v])=>e.setAttribute(k,v));return e};
function filtered(){const q=search.value.trim().toLowerCase();return papers.filter(p=>(!theme.value||(p.evolution_trends||[]).includes(theme.value))&&(!subtrend.value||(p.evolution_subtrends||[]).includes(subtrend.value))&&(!startDate.value||p.date>=startDate.value)&&(!endDate.value||p.date<=endDate.value)&&(!q||[p.title,p.brief,p.abstract,(p.authors||[]).join(' ')].join(' ').toLowerCase().includes(q)))}
function render(){const rows=filtered(); count.textContent=`显示 ${rows.length} / ${papers.length} 篇`; svg.replaceChildren(); if(!rows.length){const t=E('text',{x:600,y:210,'text-anchor':'middle',class:'axis-text'});t.textContent='没有匹配论文';svg.append(t);return} const W=1200,H=440,L=58,R=30,T=40,B=58; const ts=rows.map(p=>Date.parse(p.date)), lo=Math.min(...ts),hi=Math.max(...ts),span=Math.max(86400000,hi-lo); const x=t=>L+(t-lo)/span*(W-L-R); const y=t=>220+70*Math.sin(((t-lo)/span)*Math.PI*4); let path=''; for(let i=0;i<220;i++){const t=lo+span*i/219;path+=(i?' L':'M')+x(t).toFixed(1)+' '+y(t).toFixed(1)} svg.setAttribute('viewBox','0 0 1200 440');svg.append(E('path',{d:path,class:'curve'})); svg.append(E('line',{x1:L,y1:H-B,x2:W-R,y2:H-B,class:'axis'})); const startY=new Date(lo).getUTCFullYear(),endY=new Date(hi).getUTCFullYear(); for(let yr=startY;yr<=endY;yr++){const t=Date.parse(yr+'-01-01');if(t<lo||t>hi)continue;const xx=x(t);svg.append(E('line',{x1:xx,y1:H-B,x2:xx,y2:H-B+7,class:'axis'}));const tx=E('text',{x:xx,y:H-B+24,'text-anchor':'middle',class:'axis-text'});tx.textContent=yr;svg.append(tx)} const occupied={}, labelIds=new Set(); const labelCount=rows.length<=30?rows.length:7; for(let n=0;n<labelCount;n++){const target=lo+span*(n+.35)/labelCount;let best=0,dist=Infinity;ts.forEach((t,i)=>{const d=Math.abs(t-target);if(d<dist){dist=d;best=i}});labelIds.add(best)} rows.forEach((p,i)=>{const t=Date.parse(p.date),xx=x(t),bucket=Math.round(xx/7),stack=occupied[bucket]||0;occupied[bucket]=stack+1;const yy=y(t)+(stack%2?1:-1)*Math.ceil(stack/2)*5;const c=E('circle',{cx:xx,cy:yy,r:4,class:'point','aria-label':p.date+' '+p.title+'。'+p.brief});c.addEventListener('mouseenter',ev=>showTip(ev,p));c.addEventListener('mousemove',moveTip);c.addEventListener('mouseleave',()=>tip.style.display='none');c.addEventListener('click',()=>selectPaper(p,c));svg.append(c);if(labelIds.has(i)){const labelX=Math.min(W-R-205,xx+7),labelY=yy+(i%2?-22:19),tx=E('text',{x:labelX,y:labelY,class:'node-label'}),name=E('tspan',{x:labelX,dy:0}),brief=E('tspan',{x:labelX,dy:13,class:'node-summary'});name.textContent=p.date.slice(0,7)+' · '+p.title.slice(0,20);brief.textContent=p.brief.slice(0,30);tx.append(name,brief);svg.append(tx)}})}
function showTip(ev,p){tip.innerHTML='<b>'+escapeHtml(p.date+' · '+p.title)+'</b><em>'+escapeHtml(p.brief)+'</em>';tip.style.display='block';moveTip(ev)} function moveTip(ev){const box=svg.parentElement.getBoundingClientRect();tip.style.left=Math.min(box.width-400,Math.max(0,ev.clientX-box.left+12))+'px';tip.style.top=Math.max(0,ev.clientY-box.top-85)+'px'}
function selectPaper(p,node){svg.querySelectorAll('.active').forEach(n=>n.classList.remove('active'));node.classList.add('active');const links=[];if(p.abs)links.push('<a href="'+attr(p.abs)+'" target="_blank" rel="noopener">论文页</a>');if(p.pdf)links.push('<a href="'+attr(p.pdf)+'" target="_blank" rel="noopener" download>下载 PDF</a>');detail.innerHTML='<div><h2>'+escapeHtml(p.title)+'</h2><p>'+escapeHtml(p.date+' · '+(p.authors||[]).join(', '))+'</p><p class="brief">'+escapeHtml(p.brief)+'</p><p>'+escapeHtml((p.abstract||'暂无摘要').slice(0,900))+'</p></div><div class="actions">'+links.join('')+'</div>'}
function renderInsight(key){const d=annualInsights[key];if(!d)return;document.querySelectorAll('.year-chip').forEach(b=>b.classList.toggle('active',b.dataset.insight===key));const evidence=(d.examples||[]).map(p=>'<a href="'+attr(p.url)+'" target="_blank" rel="noopener"><b>'+escapeHtml(p.title)+'</b> — '+escapeHtml(p.brief)+'</a>').join('');document.getElementById('year-insight').innerHTML='<h3>'+escapeHtml(d.transition_title)+'</h3><p>'+escapeHtml(d.narrative)+'</p><div class="year-evidence">'+evidence+'</div>'}
function updateSubtrends(selected=''){const names=theme.value?(subtrendGroups[theme.value]||[]):Object.values(subtrendGroups).flat();subtrend.innerHTML='<option value="">全部细分趋势</option>'+[...new Set(names)].map(name=>'<option value="'+attr(name)+'">'+escapeHtml(name)+'</option>').join('');if(names.includes(selected))subtrend.value=selected}
function escapeHtml(s){return String(s||'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))} function attr(s){return escapeHtml(s)}
[search,subtrend,startDate,endDate].forEach(el=>el.addEventListener(el===search?'input':'change',render));theme.addEventListener('change',()=>{updateSubtrends();render()});document.getElementById('clear-range').addEventListener('click',()=>{startDate.value='';endDate.value='';render()});document.querySelectorAll('.year-chip').forEach(b=>b.addEventListener('click',()=>renderInsight(b.dataset.insight)));document.querySelectorAll('.subtrend-chip').forEach(b=>b.addEventListener('click',()=>{theme.value=b.dataset.major;updateSubtrends(b.dataset.subtrend);render();document.querySelector('main').scrollIntoView({behavior:'smooth'})}));document.getElementById('export').addEventListener('click',()=>{const rows=filtered(),cols=['date','id','title','brief','authors','evolution_trends','evolution_subtrends','themes','abs','pdf'];const csv=[cols.join(',')].concat(rows.map(p=>cols.map(k=>'"'+String(Array.isArray(p[k])?p[k].join('; '):(p[k]||'')).replace(/"/g,'""')+'"').join(','))).join('\\n');const a=document.createElement('a');a.href=URL.createObjectURL(new Blob(['\ufeff'+csv],{type:'text/csv'}));a.download='__CATEGORY__-papers.csv';a.click();URL.revokeObjectURL(a.href)});updateSubtrends();renderInsight(defaultInsight);render();
</script></body></html>'''
    replacements = {
        "__TITLE__": html.escape(title), "__COUNT__": str(len(papers)),
        "__MIN_DATE__": min_date, "__MAX_DATE__": max_date,
        "__PDF_COUNT__": str(sum(bool(p.get("pdf")) for p in papers)),
        "__OVERALL__": html.escape(overall), "__PHASES__": phase_html,
        "__YEAR_BUTTONS__": year_buttons, "__ANNUAL_DATA__": annual_data,
        "__SUBTREND_DATA__": subtrend_data,
        "__DEFAULT_ANNUAL__": default_annual,
        "__THEME_OPTIONS__": options_theme, "__PAPER_DATA__": data,
        "__CATEGORY__": category,
    }
    for key, value in replacements.items():
        template = template.replace(key, value)
    return template


def main() -> None:
    grouped = load_data()
    manifest = {"generated_at": datetime.utcnow().isoformat() + "Z", "categories": {}}
    for category, (title, relative) in CATEGORIES.items():
        papers = grouped.get(category, [])
        target = ROOT / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(build_html(category, title, papers), encoding="utf-8")
        manifest["categories"][category] = {"title": title, "path": relative, "paper_count": len(papers), "pdf_count": sum(bool(p.get("pdf")) for p in papers)}
        print(f"{category}: {len(papers)} -> {relative}")
    (ROOT / "resources/category-timeline-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
