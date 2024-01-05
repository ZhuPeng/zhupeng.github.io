---
layout: post
title: GitHub 开源项目 iusztinpaul/hands-on-llms 介绍，🦖 𝗟𝗲𝗮𝗿𝗻 about 𝗟𝗟𝗠𝘀, 𝗟𝗟𝗠𝗢𝗽𝘀, and 𝘃𝗲𝗰𝘁𝗼𝗿 𝗗𝗕𝘀 for free by designing, training, and deploying a real-time financial advisor LLM system ~ 𝘴𝘰𝘶𝘳𝘤𝘦 𝘤𝘰𝘥𝘦 + 𝘷𝘪𝘥𝘦𝘰 & 𝘳𝘦𝘢𝘥𝘪𝘯𝘨 𝘮𝘢𝘵𝘦𝘳𝘪𝘢𝘭𝘴
tags: 
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 iusztinpaul/hands-on-llms，该项目在 GitHub 有差不多 1000 Star，用一句话介绍该项目就是：“🦖 𝗟𝗲𝗮𝗿𝗻 about 𝗟𝗟𝗠𝘀, 𝗟𝗟𝗠𝗢𝗽𝘀, and 𝘃𝗲𝗰𝘁𝗼𝗿 𝗗𝗕𝘀 for free by designing, training, and deploying a real-time financial advisor LLM system ~ 𝘴𝘰𝘶𝘳𝘤𝘦 𝘤𝘰𝘥𝘦 + 𝘷𝘪𝘥𝘦𝘰 & 𝘳𝘦𝘢𝘥𝘪𝘯𝘨 𝘮𝘢𝘵𝘦𝘳𝘪𝘢𝘭𝘴”。


![architecture](https://raw.githubusercontent.com/iusztinpaul/hands-on-llms/master/media/architecture.png)
![EDA](https://raw.githubusercontent.com/iusztinpaul/hands-on-llms/master/./media/eda_prompts_dataset.png)
![](https://raw.githubusercontent.com/iusztinpaul/hands-on-llms/master/media/youtube_thumbnails/00_intro.png)
![](https://raw.githubusercontent.com/iusztinpaul/hands-on-llms/master/media/youtube_thumbnails/01_fine_tuning_pipeline_overview.png)
![](https://raw.githubusercontent.com/iusztinpaul/hands-on-llms/master/media/youtube_thumbnails/02_fine_tuning_pipeline_hands_on.png)
![](https://raw.githubusercontent.com/iusztinpaul/hands-on-llms/master/media/youtube_thumbnails/03_real_time_embeddings.png)
![](https://raw.githubusercontent.com/iusztinpaul/hands-on-llms/master/media/youtube_thumbnails/04_inference_pipeline.png)
![](https://github.com/Paulescu.png)
![](https://github.com/Joywalker.png)
![](https://github.com/iusztinpaul.png)



背景介绍：在实时金融咨询领域，我们经常面临如何高效准确地分析和回应用户问题这样的复杂任务，同时，如何将最新的金融新闻与用户的咨询内容结合起来，以产生更深入、更贴近当前金融形势的答复，也是一项挑战。此外，许多开发者可能在如何配置和部署相关系统上遇到困难，这可能导致开发的效率和效果下降。

项目介绍：[hands-on-llms](https://github.com/iusztinpaul/hands-on-llms) 是一款用于设计、训练和部署实时金融咨询语料库模型（LLM）系统的开源项目，可帮助您免费学习并理解语料库模型、语料库操作（LLMOps）和向量数据库等内容。本项目包含以下几部分构成：训练引擎、实时特性流处理流水线、推理流水线和财务问答数据集。在这些部分中，您将学到如何加载专有的问答数据集，使用 QLoRA 微调开源 LLM，同时利用 [Comet ML](https://www.comet.com?utm_source=thepauls&utm_medium=partner&utm_content=github) 记录训练实验和推理结果，最后将最好的模型存储在 Comet ML 的模型注册中心。此外，此项目值得一提的是，其在解决复杂的金融咨询任务上表现出色，结合了语言链技术和以用户问题为输入的推理模型，以提供富有洞见的金融建议。

如何使用：首先，需要设置外部服务，包括 Alpaca、Qdrant、Comet ML、Beam、AWS 等。然后，仅需下载项目代码并按照 README 文件中的步骤进行操作即可。请注意，如果您没有满足项目需求的硬件配置，我们会向您展示如何将训练流水线部署到 Beam 的无服务器架构中并在那里训练 LLM。

项目推介：hands-on-llms 是一个活跃且有深度的开源项目，它由 Paul Iusztin, Pau Labarta Bajo 和 Alexandru Razvant 创建与维护，他们是在 AI 领域有丰富经验的专家。该项目可有效地解决我们在实时金融咨询中面临的问题，受到许多开发者和用户的积极反响，也因此获得了大量的星星关注。hands-on-llms 不仅值得 AI 和金融领域的专家研究，也适合那些希望通过公司级的项目来提升技能的开发者。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=iusztinpaul/hands-on-llms&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/iusztinpaul/hands-on-llms 

开源项目作者：iusztinpaul

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=iusztinpaul/hands-on-llms)

关注我们，一起探索有意思的开源项目。

