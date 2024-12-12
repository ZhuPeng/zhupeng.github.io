---
layout: post
title: GitHub 开源项目 pytorch/torchtitan 介绍，A native PyTorch Library for large model training
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 pytorch/torchtitan，该项目在 GitHub 有超过 2.7k Star。

![](https://stats.deeptrain.net/repo/pytorch/torchtitan/?theme=light)

一句话介绍该项目：A native PyTorch Library for large model training




![Welcome to torchtitan!](https://raw.githubusercontent.com/pytorch/torchtitan/master/assets/images/titan_play_video.png)


###### 项目介绍

随着人工智能研究的不断深入，我们进入了大模型（Large Language Models，LLMs）的时代。然而，训练这样庞大的模型面临着极大的挑战，包括但不限于昂贵的计算成本、内存限制、分布式数据通信等问题。对于深度学习研究人员和工程师而言，如何高效、有效地训练这些大型模型，是一个亟待解决的核心痛点。

`torchtitan` 为解决这一问题提供了新的思路和方案。作为一个原生的 PyTorch 库，`torchtitan` 专门针对大模型训练而设计，它展示了如何利用 PyTorch 的最新分布式训练特性来进行大规模语言模型的训练。与 Megatron、Megablocks 等其他大规模 LLM 训练代码库相比，`torchtitan` 更重视在清晰、最小的代码基础上展示这些特性，并不旨在替代它们。`torchtitan` 的设计原则在于简易理解、使用和扩展，以及如何对模型代码进行最小的改动就能应用 1D、2D 甚至是 (即将支持的) 3D 并行。

使用 `torchtitan` 有多个关键优势，包括多维的可组合并行性、选择性层和操作的激活检查点、分布式检查点、`torch.compile` 支持和 `Float8` 技术等。它还提供了关于如何优化大模型训练的详细文档，帮助你快速入门。

### 如何使用 `torchtitan`

要开始使用 `torchtitan`，首先需要安装最新的 PyTorch nightly 版本和项目的依赖项：

```bash
git clone https://github.com/pytorch/torchtitan
cd torchtitan
pip install -r requirements.txt
pip3 install --pre torch --index-url https://download.pytorch.org/whl/nightly/cu124 --force-reinstall
```

接着，下载并准备 Llama 3.1 模型的 tokenizer：

```bash
# 针对 Llama 3.1 tokenizer.model
python torchtitan/datasets/download_tokenizer.py --repo_id meta-llama/Meta-Llama-3.1-8B --tokenizer_path "original" --hf_token=...
```

开始训练：

```bash
CONFIG_FILE="./train_configs/llama3_8b.toml" ./run_llama_train.sh
```

`torchtitan` 是一个处于前期发布状态且正处在积极开发中的项目，但其提供的大规模训练特性和指导原则对于希望探索 PyTorch 分布式训练新特性的研究者和工程师来说，是一个极具吸引力的起点。虽然 `torchtitan` 可能不会形成一个庞大的社区，但它将通过展示 PyTorch 的最新特性，激发人们对于大模型训练的新思考。

不管你是一个致力于推动人工智能边界的科研工作者，还是在业务中寻求利用大模型优势的工程师，`torchtitan` 都提供了一种值得考虑的方案。当前，随着项目的持续开发，我们有理由相信 `torchtitan` 将在不久的将来为大模型训练提供更多的支持和更深的洞见。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=pytorch/torchtitan&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/pytorch/torchtitan 

开源项目作者：pytorch

开源协议：BSD 3-Clause "New" or "Revised" License

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=pytorch/torchtitan)

关注我们，一起探索有意思的开源项目。

