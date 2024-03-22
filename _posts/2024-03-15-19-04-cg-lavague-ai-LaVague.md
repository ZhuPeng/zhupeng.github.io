---
layout: post
title: GitHub 开源项目 lavague-ai/LaVague 介绍，Automate automation with Large Action Model framework
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 lavague-ai/LaVague，该项目在 GitHub 有超过 1.9k Star，一句话介绍该项目：Automate automation with Large Action Model framework




![](https://raw.githubusercontent.com/lavague-ai/LaVague/master/static/logo.png)

![](https://raw.githubusercontent.com/lavague-ai/LaVague/master/static/hf_lavague.gif)

![](https://raw.githubusercontent.com/lavague-ai/LaVague/master/static/irs_lavague.gif)



背景介绍：在日常生活和工作中，我们经常需要在网络上进行各种操作，比如支付账单、填写表单或从特定网站提取数据。这些任务往往是重复性的，费时且不需要过多认知努力。但是，手动执行这些任务却需要消耗我们大量的时间和注意力。这个问题就是我们今天要介绍的项目 " LaVague " 所要解决的。

项目介绍： " LaVague " 是一个开源项目，目标是通过将自然语言指令转化为无缝的浏览器交互，重新定义网络浏览体验 。该项目利用了Selenium自动化测试工具来自动化网站的交互，同时还利用了象如transformers和llama-index这样的开源项目。项目的亮点在于，它能够理解自然语言指令，然后将这些指令转化为Selenium代码进行浏览器交互。同时，该项目还允许使用本地模型，如 " Gemma-7b " ，以确保用户可以充分控制他们的AI助手并保证隐私。此外， " LaVague " 还使用先进的AI技术，通过用 " bge-small-en-v1.5 " 检索最相关的HTML片段，然后利用少数样本学习和思维链技术引出最相关的Selenium代码来执行操作，而不需要对 " Nous-Hermes-2-Mixtral-8x7B-DPO " 的LLM模型进行微调。

如何使用：你可以在 [Colab notebook](https://colab.research.google.com/github/dhuynh95/LaVague/blob/main/examples/gradio-demo.ipynb) 上尝试使用 " LaVague " 。为了在本地建立开发环境，你需要首先在Linux上安装chrome浏览器和驱动，并运行 ```bash install-dependencies.sh``` 来安装依赖项。接下来在虚拟环境中运行 ```pip install -e .[dev]``` 来设定开发环境。

项目推介：" LaVague " 是一个既有实用性又有创新性的项目。尽管这是个早期的项目，但在作者们引导下却有着让人期待的未来。除了自己的活跃开发以外，" LaVague " 还鼓励社区参与项目的开发，通过 [contributing guide](./contributing.md) 提供了详细的贡献指南，也设置了 [Discord](https://discord.gg/SDxn9KpqX9) 社群让所有对这个项目有兴趣的人讨论和提出建议。总的来说， " LaVague " 是一个值得关注和参与的项目，无论你是一个开发者还是一个对提高自己网络操作效率有需求的用户。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=lavague-ai/LaVague&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/lavague-ai/LaVague 

开源项目作者：lavague-ai

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=lavague-ai/LaVague)

关注我们，一起探索有意思的开源项目。

