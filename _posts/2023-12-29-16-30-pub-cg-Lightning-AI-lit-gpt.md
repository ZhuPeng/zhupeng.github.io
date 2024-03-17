---
layout: post
title: NeurIPS 官方推荐的开源大模型启动套件
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在处于大数据和高性能计算领域的今天，大型语言模型（LLMs）正逐渐成为人工智能领域最有成效的工具之一。然而，尽管 LLMs 在一系列任务中表现出来的微妙性和宽广的知识使其非常强大，但是它们的部署和实施却很复杂。接触到的问题可能包括：需要处理大量的数据，需要大量的计算能力，对内存和存储需求较高，模型微调和部署的复杂性等。同时，我们也需要一个一站式的解决方案，可以方便地查找和实现不同的模型，这样可以节省我们的时间并提高工作效率。

今天要给大家推荐一个 GitHub 开源项目 Lightning-AI/lit-gpt，该项目在 GitHub 有超过 4.5k Star，用一句话介绍该项目就是：“Hackable implementation of state-of-the-art open-source LLMs based on nanoGPT. Supports flash attention, 4-bit and 8-bit quantization, LoRA and LLaMA-Adapter fine-tuning, pre-training. Apache 2.0-licensed.”。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240221223827154.png)

###### 项目介绍

Lit-GPT 是基于 nanoGPT 的最新的开源大型语言模型的实现方案，支持 flash attention、4-bit 和 8-bit 的量化，LoRA 和 LLaMA-Adapter 进行的微调和预训练。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240221224319541.png)

Lit-GPT 提供了一种 hackable 的实现方式，它的特点是支持多种流行的模型检查点，比如 EleutherAI Pythia、LMSYS LongChat、Meta AI Code Llama、Microsoft Research Phi 等。该项目通过 Lightning Fabric 进行支持，并且使用 Apache 2.0 的开源许可。

以下是一个具体的使用示例，相应速度还是很快的。

![](https://pl-public-data.s3.amazonaws.com/assets_lightning/LitStableLM.gif)

目前支持如下模型：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240221224046526.png)

###### 如何使用

参考如下命令即可安装：

```bash
git clone https://github.com/Lightning-AI/lit-gpt
cd lit-gpt
pip install -r requirements-all.txt
```

安装好之后，使用如下命令即可开始使用：

```bash
python generate/base.py --prompt "Hello, my name is"
```

###### 项目推介

Lit-GPT 在 2023 年的 NeurIPS Large Language Model Efficiency Challenge 上，即使用一个大型语言模型和一个 GPU 在一天内完成微调的比赛中，获得了大赛的官方推荐，是官方的启动的套件。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240221224204769.png)


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=Lightning-AI/lit-gpt&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/Lightning-AI/lit-gpt 

开源项目作者：Lightning-AI

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=Lightning-AI/lit-gpt)

关注我们，一起探索有意思的开源项目。

