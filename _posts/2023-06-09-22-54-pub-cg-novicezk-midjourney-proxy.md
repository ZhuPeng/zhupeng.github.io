---
layout: post
title: MidJourney-proxy：代理 MJ 的 discord 频道，实现 API 形式调用 AI 绘图
tags: Java
---

大家好，又见面了，我是 GitHub 精选君！

##### 背景介绍

在日常开发中，我们经常需要使用 MidJourney 的 discord 频道来调用 AI 进行绘图，但使用过程中可能会遇到一些问题。例如，操作复杂、图像处理功能不完善等。这些问题限制了我们在AI绘图方面的效率和体验。

##### 项目介绍

为了解决这些问题，今天要介绍一个开源项目 midjourney-proxy。该项目旨在提供一个API形式调用AI绘图的代理，使得使用MidJourney的discord频道更加便捷高效。该项目在 GitHub 有超过 2.4k Star，用一句话介绍该项目就是：“代理 MidJourney 的discord频道，实现 api 形式调用 AI 绘图”。

midjourney-proxy的主要功能包括：
- 支持Imagine指令和相关的U、V操作，满足绘图需求
- 支持将图像以base64的形式添加到绘图，方便叠加图层
- 支持Describe指令，根据图像生成相应的prompt
- 支持Blend指令，实现多个图像的混合
- 支持Imagine、V、Blend图像生成进度的监控
- 支持中文prompt翻译，可配置百度翻译或gpt
- 支持prompt敏感词判断，支持调整

除此之外，midjourney-proxy还拥有一支任务队列，队列默认为10，可参考MidJourney订阅等级进行调整。同时，你可以选择user-token连接wss，以获取错误信息和完整功能。

##### 如何使用

目前支持 Railway 部署、Zeabur 部署和 Docker 部署，具体可参考如下：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_image-20230720212652567.png)

如果你正在寻找一个方便易用的代理工具来调用MidJourney的discord频道进行AI绘图，midjourney-proxy将是你的不错选择。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=novicezk/midjourney-proxy&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/novicezk/midjourney-proxy 

开源项目作者：novicezk

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=novicezk/midjourney-proxy)

关注我们，一起探索有意思的开源项目。

