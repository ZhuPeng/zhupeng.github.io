---
layout: post
title: 重新定义网络浏览体验，通过自然语言无缝进行浏览器交互
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在日常生活和工作中，我们经常需要在网络上进行各种操作，比如支付账单、填写表单或从特定网站提取数据。这些任务往往是重复性的，费时且不需要过多认知努力。但是，手动执行这些任务却需要消耗我们大量的时间和注意力。

今天要给大家推荐一个 GitHub 开源项目 lavague-ai/LaVague，该项目在 GitHub 有超过 1.9k Star，一句话介绍该项目：Automate automation with Large Action Model framework

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240418224741533.png)

###### 项目介绍

 LaVague 的目标是通过将自然语言指令转化为无缝的浏览器交互，重新定义网络浏览体验。该项目利用了Selenium 自动化测试工具来自动化网站的交互，同时还利用了象如 transformers 和 llama-index 这样的开源项目。项目的亮点在于，它能够理解自然语言指令，然后将这些指令转化为 Selenium 代码进行浏览器交互。同时，该项目还允许使用本地模型，如 Gemma-7b，以确保用户可以充分控制他们的 AI 助手并保证隐私。此外，LaVague 还使用先进的 AI 技术，通过用 bge-small-en-v1.5 检索最相关的 HTML 片段，然后利用少数样本学习和思维链技术引出最相关的 Selenium 代码来执行操作，而不需要对 Nous-Hermes-2-Mixtral-8x7B-DPO 的 LLM 模型进行微调。


以下是一个演示示例：

![](https://raw.githubusercontent.com/lavague-ai/LaVague/master/static/hf_lavague.gif)

###### 如何使用

你可以在 [Colab notebook](https://colab.research.google.com/github/dhuynh95/LaVague/blob/main/examples/gradio-demo.ipynb) 上尝试使用 LaVague。为了在本地建立开发环境，你需要首先在 Linux 上安装 Chrome 浏览器和驱动，并运行 ```bash install-dependencies.sh``` 来安装依赖项。接下来在虚拟环境中运行 ```pip install -e .[dev]``` 来设定开发环境。

![](https://raw.githubusercontent.com/lavague-ai/LaVague/master/static/irs_lavague.gif)

###### 项目推介

LaVague 是一个既有实用性又有创新性的项目。尽管这是个早期的项目，但在作者们引导下却有着让人期待的未来。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=lavague-ai/LaVague&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/lavague-ai/LaVague 

开源项目作者：lavague-ai

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=lavague-ai/LaVague)

关注我们，一起探索有意思的开源项目。

