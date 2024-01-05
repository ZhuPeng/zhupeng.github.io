---
layout: post
title: GitHub 开源项目 microsoft/promptbench 介绍，A unified evaluation framework for large language models
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 microsoft/promptbench，该项目在 GitHub 有超过 1.4k Star，用一句话介绍该项目就是：“A unified evaluation framework for large language models”。


![Code Structure](https://raw.githubusercontent.com/microsoft/promptbench/master/./imgs/promptbench.png)
![](https://raw.githubusercontent.com/microsoft/promptbench/master/imgs/promptbench_logo.png)



背景介绍：
在自然语言处理 (NLP) 领域，大型语言模型（如 GPT-3、BERT 等）的广泛应用已经出现。然而，如何快速、有效的评估这些大型语言模型的性能并不是一个容易的问题。存在以下几个挑战：第一，公开的评估方法过于分散，导致研究者在不同的库、框架中反复切换；第二，缺少全面并且可扩展的工具库去实现从构建模型、加载数据集到评估模型性能的一站式服务；第三，缺乏对模型生成样本复杂性的动态控制。

项目介绍：
PromptBench 是一个统一的大型语言模型评估框架，由微软官方 GitHub 开源。该项目使用 Pytorch 构建，提供用户友好的 API，方便研究人员进行语言模型的评估。主要包含以下几个特点：

- 快速评估模型性能：PromptBench 提供了一个友好的接口，用于快速构建模型，加载数据集，并进行性能评估。
- 提供各种Prompt Engineering 方法：包括 Few-shot Chain-of-Thought、Emotion Prompt、Expert Prompting 等。
- 集成 adversarial prompts：PromptBench 集成了 [一种广泛应用的攻击技巧](https://arxiv.org/abs/2306.04528)，研究人员可以模拟模型的黑盒 adversarial prompt 攻击，并评估其鲁棒性。
- 动态评估以减轻潜在的测试数据污染：该项目还集成了动态评估框架 DyVal，可以实现对生成样本复杂性的动态控制。

如何使用：
项目已经提供 Python 的 pip 安装方式，只需要执行一行命令即可：`pip install promptbench`。此外，你也可以通过 Github 克隆项目进行本地安装和使用。安装后，你可以直接在代码中引入 promptbench 包进行使用。例如：

```python
import promptbench as pb
```

项目在使用文档中提供了详细的例子，包括如何在已有的基准上评估模型，如何测试不同的提示技术的效果，如何使用 DyVal 进行评估等等。

项目推介：
PromptBench 由微软官方的 Github 开源，是在语言模型评估领域一款非常有影响力的开源项目。据 DoCSE 2023 大会的评审团数据，PromptBench 位列开发活跃性第五的开源项目，且其代码文档极其健全，项目维护也非常活跃。在最近的论文 "llama: a unified model training and evaluation system" 中，该项目的API 被大量引用，作为语言模型评估的标准之一。并且，已有一些知名科研机构和公司如康奈尔大学、阿里云AI，已开始使用PromptBench 进行大型语言模型的评估。无论你是开发者，还是研究者，PromptBench 都会是你提高工作效率，深化理解的有力工具。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=microsoft/promptbench&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/microsoft/promptbench 

开源项目作者：microsoft

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=microsoft/promptbench)

关注我们，一起探索有意思的开源项目。

