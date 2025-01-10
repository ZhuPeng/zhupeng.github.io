---
layout: post
title: GitHub 开源项目 pytorch/torchtune 介绍，PyTorch native post-training library
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 pytorch/torchtune，该项目在 GitHub 有超过 4.7k Star。

![](https://stats.deeptrain.net/repo/pytorch/torchtune/?theme=light)

一句话介绍该项目：PyTorch native post-training library





###### 项目介绍

背景介绍：
在当今快速发展的人工智能领域中，大型语言模型（LLM）的研究与应用正蓬勃发展，凭借其强大的语言理解和生成能力，广泛应用于文本分析、自然语言处理、内容创作等多个场景。然而，随着模型规模的不断扩大，如何有效、高效地对这些大型模型进行微调和实验成为了一个核心痛点。研究者和开发者需要一个强大的工具库，以便轻松实现模型的自定义训练、微调，同时保证内存和性能的优化。



![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-27cbf745980a2cccc9b2814bc4eba121.png)

项目介绍：
针对上述问题， **PyTorch** 社区推出了 **torchtune** ，这是一个 **PyTorch** 原生的大型语言模型后训练库。 **torchtune** 不仅提供了从 Llama、Gemma、Mistral、Phi、到 Qwen 等多个模型家族的 **PyTorch** 实现，而且还提供了全面微调、LoRA、QLoRA、DPO、PPO、QAT、知识蒸馏等多种微调配方。该库通过最新的 **PyTorch** API 实现了开箱即用的内存效率和性能改进，并通过 **YAML** 配置文件，简化了训练、评估、量化或推理的配置过程。 **torchtune** 支持多种流行的数据集格式和提示模板，是研究和开发人员的强大助手。

如何使用：
首先，通过以下指令安装 **torchtune** ：

```bash
pip install torchtune
```

然后，用户可以根据不同的需求，选择合适的配置文件进行模型训练或微调。例如，使用以下命令进行 Llama 3.3 模型的训练：

```bash
torchtune train --config recipes/configs/llama3_3/<your-config-file>.yaml
```

项目推介：
自 **torchtune** 发布以来，已经吸引了众多开发者和研究人员的关注和使用。该项目持续获得 **PyTorch** 社区的强力支持，根据其 GitHub 页面显示，项目持续更新活跃，定期添加新的模型和功能。其中，对 Llama 3.3 70B 的支持在 2024 年 12 月推出，便引起了广泛的关注。此外，项目的作者和贡献者来自业界知名的研究团队和公司，保证了项目的专业性和前瞻性。 **torchtune** 不仅有详细的文档和社区支持，还通过 **Discord** 为用户提供即时的交流平台。无论是在学术研究还是工业应用中， **torchtune** 都是大型语言模型微调和实验的优选工具。

结合其持续的项目活跃度、社区支持、以及强大的功能特性， **torchtune** 无疑是值得每一位对大型语言模型开发和研究感兴趣的人关注和使用的开源项目。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=pytorch/torchtune&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/pytorch/torchtune 

开源项目作者：pytorch

开源协议：BSD 3-Clause "New" or "Revised" License

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=pytorch/torchtune)

关注我们，一起探索有意思的开源项目。

