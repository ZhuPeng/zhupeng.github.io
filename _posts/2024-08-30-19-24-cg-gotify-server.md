---
layout: post
title: 一个基于 WebSocket 的简洁、实时消息服务器
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

随着移动互联网和物联网（IoT）的迅速发展，实时消息传输成为应用和服务之间通信不可或缺的一环。无论是智能家居通知、即时消息聊天、还是服务器监控告警，一个稳定、高效的实时消息服务器对于保障信息顺畅流动至关重要。然而，市面上存在的解决方案要么过于复杂难以自主部署，要么长期无人维护缺乏灵活性，让许多企业和开发者在构建自己的即时消息系统时遇到了困难。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-dbbdaa53995e349def8d84594a11b9b9.png)

今天要给大家推荐一个 GitHub 开源项目 gotify-server，该项目在 GitHub 有超过 10.8k Star。

![](https://stats.deeptrain.net/repo/gotify/server/?theme=light)

一句话介绍该项目：A simple server for sending and receiving messages in real-time per WebSocket. (Includes a sleek web-ui)

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240913213016562.png)


###### 项目介绍

gotify/server 是一个基于 WebSocket 的简洁、实时消息服务器，支持自我托管，为开发者提供了一个易于部署、灵活的实时消息解决方案。

![](https://raw.githubusercontent.com/gotify/server/master/ui.png)

`gotify/server` 的核心功能包括：

1、通过 REST-API 发送消息：简化了消息发送过程，让服务和应用能够轻松集成消息推送功能。

2、通过 WebSocket 接收消息：实现了实时的消息接收，保证信息能够迅速准确地送达。

3、用户、客户端和应用管理：提供了一套完善的管理界面，使得用户和权限控制变得简单直观。

4、插件系统支持：通过强大的插件系统，`gotify/server` 可以轻松扩展更多功能，满足特定的业务需求。

5、附带 Web-UI：提供了一套优雅的 Web 用户界面，使得操作和管理变得友好、直观。

6、可用的 CLI 和 Android 应用：通过 CLI 工具和 Android 应用，增强了 `gotify/server` 的可接入性和便利性。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240913213209758.png)

###### 如何使用

详细的安装流程可以在官方文档 [Installation](https://gotify.net/docs/install) 中找到，包括但不限于 Docker、二进制安装等方式。以 Docker 为例，只需简单的几行命令就可以完成部署：

```bash
docker pull gotify/server
docker run -p 80:80 gotify/server
```

之后，开发者可以通过 REST-API 向服务器发送消息，同时通过 WebSocket 在客户端接收实时消息。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240913213344003.png)

###### 项目推介

多个开源项目和企业已经开始采用 `gotify/server` 作为他们的实时通信基础服务。加上强大的插件系统和开源的客户端应用（包括 Android 客户端），`gotify/server` 可以成为构建现代应用实时通信架构的可选方案。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=gotify/server&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/gotify/server 

开源项目作者：gotify

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=gotify/server)

关注我们，一起探索有意思的开源项目。

