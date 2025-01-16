---
layout: post
title: 一个简单易用的 Discord API 封装库
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

Discord 已成为很多游戏玩家、技术社区和各类讨论组的首选社交平台。但随着社区日益壮大，管理和维护社区的难度也随之增加。社区管理员和开发者需要一个工具，能够简化频道管理，实现自动化操作，从而提高效率。同时，为了让社区更加活跃和有趣，也需要能够轻松创建和部署机器人来增加用户互动。然而，直接使用 Discord 的 API 存在一定的复杂性，需要开发者具备较强的编程技能和深入的 API 理解，这对很多有意向但是编程基础不足的人来说是一个很大的阻碍。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-4738bd5d14f02bda672cbde460aba3e2.png)

今天要给大家推荐一个 GitHub 开源项目 Rapptz/discord.py，该项目在 GitHub 有超过 15.0k Star。

![](https://stats.deeptrain.net/repo/Rapptz/discord.py/?theme=light)

一句话介绍该项目：An API wrapper for Discord written in Python.

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241219214241368.png)

###### 项目介绍

discord.py 是一个用 Python 编写的 Discord API 封装库，旨在简化 Discord 机器人的开发流程。该项目通过提供一套易于理解的抽象和便捷的接口，让开发者无需深入研究 Discord 的底层 API 细节，就能轻松创建功能丰富的 Discord 机器人。`discord.py` 支持几乎 Discord API 的全部功能，包括但不限于发送消息、处理事件、管理服务器和频道等。此外，它还具备异步处理能力，能有效提高机器人响应速度和性能。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241219214326212.png)

###### 如何使用

通过 pip 即可安装 `discord.py`：

```bash
pip install -U discord.py
```

以下是一个简单的示例，展示了如何创建一个响应特定消息的机器人：

```python
import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content.startswith('!hello'):
            await message.channel.send('Hello!')

client = MyClient()
client.run('your token here')
```

###### 项目推介

`discord.py` 已经聚集了大量的使用者和贡献者，形成了一个活跃的社区。项目的文档完善，新手友好，极大地降低了新用户的入门门槛。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=Rapptz/discord.py&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/Rapptz/discord.py 

开源项目作者：Rapptz

开源协议：MIT License

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=Rapptz/discord.py)

关注我们，一起探索有意思的开源项目。

