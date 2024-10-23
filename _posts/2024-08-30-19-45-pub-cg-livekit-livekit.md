---
layout: post
title: 一个端到端 WebRTC 解决方案
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在当下互联网时代，线上教育、远程工作、虚拟社交等行业的迅猛发展，促使视频、音频通信技术成为了软件开发中不可或缺的一部分。然而，要从零开始构建一个稳定、高效且支持多用户的实时通信系统，无疑是一项艰巨挑战。开发者需要面对网络连接的稳定性、数据传输的安全性、系统的可扩展性等多方面的技术难题。此外，实现跨平台支持、提供良好的用户体验也是大家普遍关心的问题。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-bf4cc900e946298d3ec706b73f9f471d.png)

今天要给大家推荐一个 GitHub 开源项目 livekit，该项目在 GitHub 有超过 10.1k Star。

![](https://stats.deeptrain.net/repo/livekit/livekit/?theme=light)

一句话介绍该项目：End-to-end stack for WebRTC. SFU media server and SDKs.

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241013222221837.png)


###### 项目介绍

LiveKit 是一个端到端的 WebRTC 解决方案，它提供了一套可扩展的、多用户视频会议基础设施。该项目基于 Go 语言开发，利用了 Pion WebRTC 实现，旨在为开发者打造一个全面且易于部署的实时视频、音频和数据交互平台。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241013222444649.png)

LiveKit 的亮点包括：

1、可扩展的分布式 WebRTC SFU（选择性转发单元）

2、现代化、功能丰富的客户端 SDKs

3、针对生产环境设计，支持 JWT 认证

4、强大的网络连接能力，支持 UDP/TCP/TURN

5、简便的部署流程，支持单可执行文件、Docker 或 Kubernetes 部署

6、其他高级特性，如：扬声器检测、视频 simulcast、端到端加密、多区域部署等

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241013222504654.png)

###### 如何使用

在 MacOS 上安装 LiveKit：

```shell
brew install livekit
```

也可以通过 Docker 或 Helm Charts 方便地在其他环境中部署。

LiveKit 提供了丰富的客户端 SDKs，覆盖了各大主流开发语言和平台，如 JavaScript (包含 TypeScript 支持)、Swift (iOS/MacOS)、Kotlin (Android)、Flutter 以及更多。以下是使用 JavaScript SDK 的一个示例：

```javascript
const livekit = require('livekit-client');

const room = new livekit.Room(...);

// call this some time before actually connecting to speed up the actual connection
room.prepareConnection(url, token);

await room.connect(...);
```

通过简短的代码即可实现客户端连接和事件监听，极大地降低了实时通讯功能的开发难度。

###### 项目推介

LiveKit 项目开源活跃，持续获得社区的贡献和优化。借助它强大的文档和社区支持，开发者可以轻松构建起属于自己的实时视频、音频通信系统。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241013223016938.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=livekit/livekit&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/livekit/livekit 

开源项目作者：livekit

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=livekit/livekit)

关注我们，一起探索有意思的开源项目。

