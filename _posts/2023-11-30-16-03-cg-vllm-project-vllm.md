---
layout: post
title: GitHub 开源项目 vllm-project/vllm 介绍，A high-throughput and memory-efficient inference and serving engine for LLMs
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 vllm-project/vllm，该项目在 GitHub 有超过 10.3k Star，用一句话介绍该项目就是：“A high-throughput and memory-efficient inference and serving engine for LLMs”。


![](https://raw.githubusercontent.com/vllm-project/vllm/main/docs/source/assets/logos/vllm-logo-text-light.png)



背景介绍：
在语言模型（LLM）的应用领域，用户或开发者在机器学习服务过程中通常会遇到各种问题，例如：处理速度不够快、内存利用率不高、应用于流行模型的困难等。这些问题会大大影响项目的运行效率和用户体验，如果解决这些挑战，将大大优化语言模型运用的流程。

项目介绍：
vLLM 是一个高吞吐量、内存高效的语言模型推理和服务引擎，这个开源项目的目标是为每个人提供简便、快捷、经济的 LLM 服务。vLLM 能够高效地管理注意力键值内存，优化 CUDA 内核，并且能够处理连续的输入请求，这使得它的服务吞吐量处于行业领先地位。vLLM 非常灵活并易于使用，它能够与许多流行的 Hugging Face 模型无缝集成，并提供高吞吐量的服务。具备并行采样、波束搜索等解码算法，支持分布式推理的张量并行性，同时还有开放接口的 API 服务器。此外，vLLM 的安装和使用也非常简单，只需要利用 pip 进行安装即可。

如何使用：

首先，使用 pip 安装 vLLM：

```bash
pip install vllm
```

然后，访问官方[文档](https://vllm.readthedocs.io/en/latest/)来获取更详细的使用信息，包括[安装步骤](https://vllm.readthedocs.io/en/latest/getting_started/installation.html)、[快速上手指南](https://vllm.readthedocs.io/en/latest/getting_started/quickstart.html)以及[支持的模型](https://vllm.readthedocs.io/en/latest/models/supported_models.html)等内容。

项目推介：
vLLM 的开发团队是非常活跃，也得到了许多知名机构的支持，例如 Andreessen Horowitz 提供了大量的资金支持这个项目的开源开发和研究。并且，vLLM 已经被包括 LMSYS Vicuna 和 Chatbot Arena 在内的平台用来支持其自从 2023 年 4 月份的运行，这也表明了 vLLM 项目的实用性和稳定性。vLLM 也发布了其 PagedAttention 技术的论文，从学术的角度来看，vLLM 是一个有很高研究价值的项目。我们非常欢迎大家加入我们的 Discord 服务器，参与到 vLLM 和 LLM 服务的讨论中来，我们也会在那里发布最新的消息和更新。如果你对 LLM 的应用有着长期的研究或者开发需要，那么 vLLM 无疑是一个非常值得你去关注的项目。



以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=vllm-project/vllm&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/vllm-project/vllm 

开源项目作者：vllm-project

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=vllm-project/vllm)

关注我们，一起探索有意思的开源项目。

