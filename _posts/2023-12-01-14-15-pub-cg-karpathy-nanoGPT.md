---
layout: post
title: nanoGPT - 每一个团队都需要训练一个大规模语言模型嘛？
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在生成式人工智能领域，训练一个通用的大语言模型是非常耗费资源的，然而并不是所有领域都需要一个通用的模型。为了拓宽深度学习领域的应用，我们同时也需要一个简单的、易于上手的、并且能够快速训练中等规模 GPT （小型生成预训练模型）的开发工具，而这，正是我们面临的一项主要挑战。

今天要给大家推荐一个 GitHub 开源项目 karpathy/nanoGPT，该项目在 GitHub 有超过 26.4k Star，用一句话介绍该项目就是：“The simplest, fastest repository for training/finetuning medium-sized GPTs.”。

![](https://raw.githubusercontent.com/karpathy/nanoGPT/master/assets/nanogpt.jpg)

###### 项目介绍

nanoGPT 是一个最简单、最快速用于训练和微调中等规模 GPT 模型的开源项目。它将 minGPT 用极简的代码重写，更追求实用性。不仅如此，该项目代码简单，易于针对你的需求进行修改，训练新模型，或者微调预训练的检查点，给深度学习的入门者们带来极大的便利。通过 300 行左右的代码，即可复现通过 GPT-2 参数进行微调的模型训练。

###### 如何使用

nanoGPT 的安装与使用非常简单，首先进行如下依赖库的安装：

```
pip install torch numpy transformers datasets tiktoken wandb tqdm
```

然后，你可以下载并预处理开放网络文本数据，也可以用 OpenAI 的 GPT-2 模型权重作为初始点进行微调。下图有一些示例的代码：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240106232155699.png)

此外，如果你是深度学习的新手并且想要体验一下魔力，最快的方式就是训练一个以莎士比亚的作品为基础的字符级 GPT 模型。它还提供了一种非常友好的方式用于在浏览器中可视化训练进度。

![](https://raw.githubusercontent.com/karpathy/nanoGPT/master/assets/gpt2_124M_loss.png)

###### 项目推介

nanoGPT 项目的作者 karpathy（Andrei Karpathy）是知名的 AI 专家，他的主要研究领域就是深度学习，特别是自然语言处理，他的博客关于 RNN 的一篇文章被广泛引用，而他的另一篇文章关于超神经网络在论文写作中的应用也引发了业界的热议。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=karpathy/nanoGPT&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/karpathy/nanoGPT 

开源项目作者：karpathy

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=karpathy/nanoGPT)

关注我们，一起探索有意思的开源项目。

