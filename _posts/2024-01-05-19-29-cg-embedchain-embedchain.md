---
layout: post
title: GitHub 开源项目 embedchain/embedchain 介绍，The Open Source RAG framework
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 embedchain/embedchain，该项目在 GitHub 有超过 6.5k Star，用一句话介绍该项目就是：“The Open Source RAG framework”。


![](https://raw.githubusercontent.com/embedchain/embedchain/master/docs/logo/dark.svg)
![](https://raw.githubusercontent.com/embedchain/embedchain/master/docs/images/cover.gif)



项目背景：
在当前的数据驱动社会，优秀的 AI 应用正在看到无所不在的应用。然而，对于大多数开发者来说，创建和部署 AI 应用时依然面临着许多问题，如数据管理困难，数据嵌入的生成与存储问题，以及建立互动对话在用户体验上的挑战。这些问题都阻碍了 AI 应用的快速开发和部署。

项目介绍：
Embedchain 是一个开源的 RAG 框架，倡导的设计原则是"常规但可配置"，旨在为软件工程师和机器学习工程师提供便捷。Embedchain 能够简化 RAG 应用的创建流程，无缝管理各类无结构化数据。它可以有效地将数据切分成易于管理的段落，生成相应的嵌入，并将其存储在向量数据库中以实现优化检索。通过多样化的 API 集合，用户能够提取上下文信息，查找准确答案，或参与互动聊天会话，所有这些都能够量身定制来满足自己的数据要求。

如何使用：
Embedchain 的安装使用方便快捷，你只需要通过 pip install embedchain 就可以进行安装。这里提供一个用 Embedchain 创建 Elon Musk 机器人的示例代码：

```python
import os
from embedchain import Pipeline as App

# Create a bot instance
os.environ["OPENAI_API_KEY"] = "YOUR API KEY"
elon_bot = App()

# Embed online resources
elon_bot.add("https://en.wikipedia.org/wiki/Elon_Musk")
elon_bot.add("https://www.forbes.com/profile/elon-musk")

# Query the bot
elon_bot.query("How many companies does Elon Musk run and name those?")
# Answer: Elon Musk currently runs several companies. As he 
```

项目推介：
Embedchain 是一个相当活跃的开源项目，关注度和参与度都非常高。项目的核心开发团队都是有着丰富经验的资深工程师，团队的背景和技术实力都相当的强。同时，他们非常重视社区的交流与反馈，有 Slack 和 Discord 社区供开发者交流，也可安排 1 对 1 会议与创始人交流反馈，体现出极强的社区参与精神。除此之外，Embedchain 在功能设计上也颇具创新，发布了许多独特功能和实用示例。无论是从项目活跃度、开发团队背景还是针对性功能上看，Embedchain 都是一个值得推荐的优秀开源项目。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=embedchain/embedchain&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/embedchain/embedchain 

开源项目作者：embedchain

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=embedchain/embedchain)

关注我们，一起探索有意思的开源项目。

