---
layout: post
title: GitHub 开源项目 microsoft/LLMLingua 介绍，To speed up LLMs' inference and enhance LLM's perceive of key information, compress the prompt and KV-Cache, which achieves up to 20x compression with minimal performance loss. 
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 microsoft/LLMLingua，该项目在 GitHub 有超过 1.2k Star，用一句话介绍该项目就是：“To speed up LLMs' inference and enhance LLM's perceive of key information, compress the prompt and KV-Cache, which achieves up to 20x compression with minimal performance loss. ”。


![Background](https://raw.githubusercontent.com/microsoft/LLMLingua/master/./images/LLMLingua_motivation.png)
![Motivation for LLMLingua](https://raw.githubusercontent.com/microsoft/LLMLingua/master/./images/motivation.png)
![Framework of LLMLingua](https://raw.githubusercontent.com/microsoft/LLMLingua/master/./images/LLMLingua.png)
![Framework of LongLLMLingua](https://raw.githubusercontent.com/microsoft/LLMLingua/master/./images/LongLLMLingua.png)
![Demo of LLMLingua](https://raw.githubusercontent.com/microsoft/LLMLingua/master/./images/LLMLingua_demo.png)
![](https://raw.githubusercontent.com/microsoft/LLMLingua/master/images/LLMLingua_logo.png)



背景介绍：在大规模语言模型推断过程中，我们经常会面临几个问题：如何加快语言模型的推断速度；如何增强语言模型对关键信息的感知；如何压缩提示和 KV-Cache。这些问题让人头痛，因此，你需要一款工具来帮助你解决这些问题。

项目介绍：让我们向你介绍 Github 上的开源项目：LLMLingua 。这是一个由微软开发的专注于加快大规模语言模型 ( LLMs ) 的推断速度和增强模型对关键信息感知的开源项目。通过创新的方式压缩提示和 KV-Cache，LLMLingua 能达到高达 20 倍的压缩效果，而且性能损失微乎其微。无论是 GPT2-samll，还是 LLaMA-7B，LLMLingua 都能有效地识别并移除非必需的提示字符串，从而实现高效的大规模语言模型推断。在微软的 LLMLingua 项目中，还推出了 LongLLMLingua 工具，它专门解决 LLMs 中\ '在中部迷失的问题'，增强了长上下文信息处理的能力。只使用 1/4 的 Token，就可以提高达 21.4% 的 RAG 性能。

如何使用：关于使用（Long）LLMLingua 的过程非常简单，只需按照下述步骤。首先，通过 pip 安装，运行 ```pip install llmlingua``` 即可。然后，你就可以使用（Long）LLMLingua 来压缩你的提示了，如下：
```python
from llmlingua import PromptCompressor
llm_lingua = PromptCompressor()
compressed_prompt = llm_lingua.compress_prompt(prompt, instruction="", question="", target_token=200)
```

项目推介：当前 LLMLingua 在全球范围内的使用度非常广，许多研究人员和开发者都受益于这个项目。作为微软发布的开源项目，LLMLingua 是由经验丰富的开发者团队开发的，他们定期更新和维护此项目，致力于为 LLMLingua 提供最新的功能和改进。根据多篇学术论文的研究表明，LLMLingua 在压缩提示、加速推断、增强大规模语言模型的信息处理能力等方面取得了显著的成果。如果你在大规模语言模型推断方面有挑战，我强烈推荐你尝试使用 LLMLingua，感受它带给你的惊喜。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=microsoft/LLMLingua&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/microsoft/LLMLingua 

开源项目作者：microsoft

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=microsoft/LLMLingua)

关注我们，一起探索有意思的开源项目。

