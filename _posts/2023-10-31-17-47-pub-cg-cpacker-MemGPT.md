layout: post
title: MemGPT - 一个智能的大模型记忆管理系统，提供大量的上下文长度信息支持
tags: Python

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在今天的信息化社会，我们每天都会接触到大量的数据和信息，如何有效地管理和利用这些数据成为了一个重要的问题。同时，随着人工智能技术的发展，大语言模型能够帮助我们更好地与数据进行交互，但是其支持的上下文容量是有限的，会导致我们并不能充分运用已经拥有的数据和信息，上下文长度受限是一个急需解决的问题。例如，我们是否可以在与大模型聊天的过程中，也能同时去查询数据库，或者与本地文件进行交互。

今天要给大家推荐一个 GitHub 开源项目 cpacker/MemGPT，该项目在 GitHub 有超过 5.2k Star，用一句话介绍该项目就是：“Teaching LLMs memory management for unbounded context”。

![](https://memgpt.ai/assets/img/memgpt_logo_circle.png)

###### 项目介绍

MemGPT 是一个智能的记忆管理系统，它能够有效地管理和提供大量的上下文信息。例如，MemGPT 知道何时将关键信息推送到向量数据库，以及何时在聊天中检索这些信息，从而实现持久的对话。你可以通过 MemGPT 与你的 SQL 数据库或本地文件进行交互，甚至可以询问关于 LlamaIndex 的问题。更多关于 MemGPT 的信息，你可以在他们的论文中了解。

以下是一个与本地文件数据进行交互的示例：

![](https://camo.githubusercontent.com/fc10cedb1942081c72b67de9544ac1545425c46a8cbc06bcdb6e7758bb543a07/68747470733a2f2f6d656d6770742e61692f6173736574732f696d672f646f632e676966)

###### 如何使用

首先，你需要在你的环境中添加你的 OpenAI API 密钥，然后通过 pip 安装 pymemgpt。如果你需要更新这个包，只需要运行 pip install pymemgpt -U。然后，你就可以通过运行 memgpt 来使用 MemGPT 作为一个会话代理。如果你遇到了命令未找到的问题，你可以将 pip 安装脚本的目录添加到你的 PATH 中，或者直接运行 python -m memgpt。

同时你也可以去 Discord 使用对应的 MemGPT 机器人，可以直接快速开始试用。

![](https://memgpt.ai/assets/img/discord/dm_settings.png)

![](https://memgpt.ai/assets/img/discord/slash_commands.png)

###### 项目推介

MemGPT 的开发者在人工智能和记忆管理方面有着丰富的经验。如果你在寻找一个能够帮助你更好地管理和利用数据的工具，那么 MemGPT 就是你的最佳选择。以下是 MemGPT 项目未来的 Roadmap。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231111204646778.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=cpacker/MemGPT&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/cpacker/MemGPT 

开源项目作者：cpacker

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=cpacker/MemGPT)

关注我们，一起探索有意思的开源项目。