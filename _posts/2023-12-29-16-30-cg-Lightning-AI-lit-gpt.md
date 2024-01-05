---
layout: post
title: GitHub 开源项目 Lightning-AI/lit-gpt 介绍，Hackable implementation of state-of-the-art open-source LLMs based on nanoGPT. Supports flash attention, 4-bit and 8-bit quantization, LoRA and LLaMA-Adapter fine-tuning, pre-training. Apache 2.0-licensed.
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 Lightning-AI/lit-gpt，该项目在 GitHub 有超过 4.5k Star，用一句话介绍该项目就是：“Hackable implementation of state-of-the-art open-source LLMs based on nanoGPT. Supports flash attention, 4-bit and 8-bit quantization, LoRA and LLaMA-Adapter fine-tuning, pre-training. Apache 2.0-licensed.”。


![](https://pl-public-data.s3.amazonaws.com/assets_lightning/LitStableLM.gif)
![](https://pl-public-data.s3.amazonaws.com/assets_lightning/LitStableLM_Illustration.png)



背景介绍：
在处于大数据和高性能计算领域的今天，大型语言模型（LLMs）正逐渐成为人工智能领域最有成效的工具之一。然而，尽管 LLMS 在一系列任务中表现出来的微妙性和宽广的知识使其非常强大，但是它们的部署和实施却很复杂。接触到的问题可能包括：需要处理大量的数据，需要大量的计算能力，对内存和存储需求较高，模型微调和部署的复杂性等。同时，我们也需要一个一站式的解决方案，可以方便地查找和实现不同的模型，这样可以节省我们的时间并提高工作效率。

项目介绍：
这是一个名为 " Lit-GPT " 的项目，它是基于 nanoGPT 的最新的开源大型语言模型的实现方案，支持 flash attention、4-bit 和 8-bit 的量化，LoRA 和 LLaMA-Adapter 进行的微调和预训练。Lit-GPT 提供了一种 hackable 的实现方式，它的特点是支持多种流行的模型检查点，比如 EleutherAI Pythia、LMSYS LongChat、Meta AI Code Llama、Microsoft Research Phi 等。该项目通过 Lightning Fabric ⚡进行支持，并且已经获得了 Apache 2.0 的许可。

如何使用：
按照该项目的 README 提供的教程，你可以下载不同的模型并进行运行。例如，运行 Meta AI Code Llama，你可以按照 tutorials/download_code_llama.md 的说明进行操作。下载好模型后，就可以开始根据你的需要进行细粒度的调整了。同时，其官方文档 [Lightning Fabric](https://lightning.ai/docs/fabric/stable/) 也会有详细的使用和设置方法。

项目推介：
Lit-GPT 是目前市场上一个很出色的开源大型语言模型实现方案。它在 2023 年的 NeurIPS Large Language Model Efficiency Challenge 上，即使用一个大型语言模型和一个 GPU 在一天内完成微调的比赛中，获得了大赛的官方推荐。并且，项目在 Github 上拥有很高的星星数量，说明使用者对其评价较高。由此可看出，Lit-GPT 是一个具有高度活跃性、可塑性强、且比较知名的项目，我强烈推荐每位对大型语言模型有兴趣或者需要使用的人进行使用和学习。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=Lightning-AI/lit-gpt&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/Lightning-AI/lit-gpt 

开源项目作者：Lightning-AI

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=Lightning-AI/lit-gpt)

关注我们，一起探索有意思的开源项目。

