---
layout: post
title: 只需少量计算和内存资源即可运行的小型 Llama 大模型
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在当今这个数据爆炸的时代，语言模型的训练变得越来越复杂和困难。我们需要巨大的计算资源和时间来训练一个高效的语言模型。然而，这对许多人来说并不现实。与此同时，我们也遇到了如何在有限的内存和计算资源中使用大型语言模型的挑战，特别是在边缘设备上。

今天要给大家推荐一个 GitHub 开源项目 jzhang38/TinyLlama，该项目在 GitHub 有超过 4.3k Star，用一句话介绍该项目就是：“The TinyLlama project is an open endeavor to pretrain a 1.1B Llama model on 3 trillion tokens.”。

![](https://raw.githubusercontent.com/jzhang38/TinyLlama/master/.github/TinyLlama_logo.png)

###### 项目介绍

TinyLlama 旨在预训练一个在 3 万亿的 token 上的 1.1B Llama 模型。在一些恰当的优化下，我们可以在短短 90 天内使用 16 个 A100-40G GPUs 来达到这个目标。该项目采用了与 Llama 2 完全相同的架构和 tokenizer，这意味着 TinyLlama 可以在许多基于 Llama 的开源项目中插入并使用。此外，TinyLlama 非常紧凑，只有 1.1B 的参数。这种紧凑性使其能够满足许多需要限制计算和内存占用的应用。

![](https://raw.githubusercontent.com/jzhang38/TinyLlama/master/.github/llama2-training.png)
![](https://raw.githubusercontent.com/jzhang38/TinyLlama/master/.github/Pythia_saturation.png)

###### 如何使用

直接下载模型就可以使用，或者通过 huggingface 使用 demo。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240224223816342.png)

如果你想自己训练的话，参考如下训练详情。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240224223624027.png)

###### 项目推介

TinyLlama 是一个令人兴奋的开源项目，它正在积极解决一些关键问题，并在开源社区中得到了广泛的关注。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240224223913027.png)


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=jzhang38/TinyLlama&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/jzhang38/TinyLlama 

开源项目作者：jzhang38

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=jzhang38/TinyLlama)

关注我们，一起探索有意思的开源项目。

