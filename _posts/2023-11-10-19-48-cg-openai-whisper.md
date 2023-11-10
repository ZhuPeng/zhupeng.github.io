---
layout: post
title: GitHub 开源项目 openai/whisper 介绍，Robust Speech Recognition via Large-Scale Weak Supervision
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 openai/whisper，该项目在 GitHub 有超过 48.7k Star，用一句话介绍该项目就是：“Robust Speech Recognition via Large-Scale Weak Supervision”。


![Approach](https://raw.githubusercontent.com/openai/whisper/main/approach.png)
![WER breakdown by language](https://github.com/openai/whisper/assets/266841/f4619d66-1058-4005-8f67-a9d811b77c62)



背景介绍：
在音频识别和翻译领域，我们常常会遇到一些问题，比如：音频数据多元化和多语种处理的困难，传统的音频处理流程复杂繁琐，一些阶段性的处理结果需要进行手动连接和调整。有效的自动语音识别（ASR）系统对于全球交流和语言辅助系统至关重要，比如智能语音助手、电话语音翻译等方面。然而，设计一个可以广泛适用于各种任务，如多语言、语音翻译和语言识别的模型仍然是具有挑战性的。对于这些困扰我们的问题，一个来自 OpenAI 的开源项目 —— Whisper，或许能提供我们新的解决方案。

项目介绍：
Whisper 是一个用于语音识别的通用模型，通过大规模的多样化音频数据集进行训练，可以处理包括多语言语音识别、语音翻译和语言识别在内的任务。项目的核心独到之处在于，通过一个 Transformer 序列到序列模型，来进行多种语音处理任务的训练，并通过译码器来预测一系列的代表任务的特殊标记(token)，可以替代传统音频处理流程的多个阶段，实现多任务训练。Whisper 提供5种模型以及英文单一版本来实现速度和精度的权衡，适应不同的需求。

如何使用：
首先，需要在 Python 3.9.9 和 PyTorch 1.10.1 的环境下进行操作，同时需要依赖 OpenAI's tiktoken 包来进行快速的标记(tokenize)处理。安装方式如下命令：

```
pip install -U openai-whisper
```
更新到最新版本的命令如下：

```
pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git
```
需要注意的是，这个项目还要求在您的系统上安装了命令行工具 ffmpeg，如果您遇到在安装过程中出现错误，可能需要安装 Rust 开发环境。

项目推介：
Whisper 的开发者来自 OpenAI，此项目基于大规模弱监督的方法进行训练，为研究人员提供重要的研究工具，同时也为行业开发者提供了实用的开发工具，可以广泛应用于各种语音识别需求。它对各种语言的处理能力具有显著的优势，符合多元化、多任务化的发展趋势。这个项目现在处于活跃开发状态，接受社区的反馈和贡献，非常值得大家的关注和试用。



以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=openai/whisper&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/openai/whisper 

开源项目作者：openai

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=openai/whisper)

关注我们，一起探索有意思的开源项目。

