---
layout: post
title: Open Interpreter - 可以在命令行终端本地运行的 OpenAI 代码执行器
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在我们的日常编程工作中，经常会遇到一些复杂的编程问题，比如创建和编辑图片、视频、PDF 等，控制 Chrome 浏览器进行自动化处理，处理和分析大型数据集等。这些问题需要我们具备丰富的编程知识和经验，而且在解决问题的过程中，我们可能需要花费大量的时间和精力。那么，有没有一种工具，可以帮助我们以自然语言的方式来运行代码，从而更高效地解决这些问题呢？

今天要给大家推荐一个 GitHub 开源项目 KillianLucas/open-interpreter，该项目在 GitHub 有超过 31.3k Star，用一句话介绍该项目就是：“OpenAI's Code Interpreter in your terminal, running locally”。


![poster](https://github.com/KillianLucas/open-interpreter/assets/63927363/08f0d493-956b-4d49-982e-67d4b20c4b56)

###### 项目介绍

Open Interpreter 是 OpenAI 的代码解释器，它可以在你的终端本地运行。这是一个开源的项目，可以让语言模型在你的电脑上运行代码，包括 Python、Javascript、Shell 等。你可以通过一个类似于 ChatGPT 的界面在你的终端与 Open Interpreter 进行交谈。这为你的电脑提供了一个自然语言的接口，可以创建和编辑图片、视频、PDF 等，控制 Chrome 浏览器进行研究，处理和分析大型数据集等。但在运行代码之前，你需要确认代码是否可以运行，避免造成不必要的影响。

DEMO 视频：https://user-images.githubusercontent.com/63927363/264166941-37152071-680d-4423-9af3-64836a6f7b60.mp4

###### 如何使用

首先，你需要通过 pip 安装 open-interpreter。安装完成后，只需要运行 interpreter 就可以开始使用了。你可以通过 interpreter.chat("命令") 来执行单个命令，也可以通过 interpreter.chat() 来开始一个交互式的聊天。此外，你还可以通过 .chat(message) 来直接传递消息。

```python
import interpreter

interpreter.chat("Plot AAPL and META's normalized stock prices") # Executes a single command
interpreter.chat() # Starts an interactive chat
```

###### 项目推介

Open Interpreter 项目克服了 OpenAI 的服务的限制，比如没有互联网访问，预安装包的数量有限，上传的最大限制是 100 MB，运行时间的最大限制是 120.0 秒。Open Interpreter 通过在你的本地环境运行，消除了这些限制。它可以全面访问互联网，不受时间或文件大小的限制，可以使用任何包或库。这结合了 GPT-4 的代码解释器的强大功能和你的本地开发环境的灵活性。我强烈推荐你试试这个项目，相信它会给你的编程工作带来很大的帮助。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=KillianLucas/open-interpreter&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/KillianLucas/open-interpreter 

开源项目作者：KillianLucas

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=KillianLucas/open-interpreter)

关注我们，一起探索有意思的开源项目。