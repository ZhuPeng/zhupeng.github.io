---
layout: post
title: 十行代码即可构建 AI Agent 应用
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

获取、处理各种模式（文本、图像、视频等）的数据和知识已成为人们日常不可或缺的一部分。然而，面对复杂多变的数据处理需求，标准的搜索引擎和工具往往不能完全满足高效、精准地获取信息的需求。用户往往需要整合不同的工具和服务，以构造出能够理解多模态输入、从中提取知识、并进行合理推理的智能代理。然而这一过程充满了挑战，比如如何有效管理和调度不同的工具、如何设计良好的用户交互界面、以及如何让这些代理能够进行复杂的理解和推理。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-c1f6fd5f57f3b1cab51413c8b4e37b77.png)

今天要给大家推荐一个 GitHub 开源项目 phidata，该项目在 GitHub 有超过 16.3k Star。

![](https://stats.deeptrain.net/repo/phidatahq/phidata/?theme=light)

一句话介绍该项目：Build multi-modal Agents with memory, knowledge, tools and reasoning. Chat with them using a beautiful Agent UI.

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241216234701057.png)

###### 项目介绍

Phidata 是一个用于构建具有记忆、知识、工具和推理能力的多模态代理框架。Phidata 不仅允许用户创建可以理解文本、图像、音频和视频的智能代理，还能够实现代理之间的协作，共同解决问题。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241216234805090.png)

它拥有一套简洁而优雅的设计，使得用户可以在十行代码内构建出一个功能完备的网络搜索代理。此外，Phidata 提供了一个美观的代理用户界面，使得与代理的交互更加直观和人性化。核心特性包括多模态输入、多代理协同、内建的监控与调试工具，以及用于实验性理性推理的代理。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241216234816601.png)

###### 如何使用

通过 pip 命令 `pip install -U phidata` 进行安装。

构建代理示例代码如下：

```python
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo

web_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)
web_agent.print_response("Tell me about OpenAI Sora?", stream=True)
```
然后设置好环境变量（例如 `OPENAI_API_KEY`），即可运行相应的 Python 脚本。

###### 项目推介

Phidata 简洁而强大的设计理念，使得无论是数据科学家、软件工程师还是业余爱好者，都能轻松上手并构建出功能强大的智能代理。而且，通过提供一个直观漂亮的界面与代理交互，极大地提升了用户体验。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=phidatahq/phidata&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/phidatahq/phidata 

开源项目作者：phidatahq

开源协议：Mozilla Public License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=phidatahq/phidata)

关注我们，一起探索有意思的开源项目。

