---
layout: post
title: 异地恋神器，一个在线同步播放影片的项目
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在当今的互联网如此发达的今天，我们很多的工作和学习都可以远程进行，一些商业和休闲活动也开始转移到在线。看电影或者直播成为了大家联系互动、消磨时间的重要方式。但是，因为地理位置或网络问题，有时我们和我们想要一起看电影或直播的人无法进行同步观看，这就是需要解决的问题。

今天要给大家推荐一个 GitHub 开源项目 synctv-org/synctv，该项目在 GitHub 有差不多 1000 Star，一句话介绍该项目：Synchronized viewing, theater, live streaming, video, long-distance relationship.
![](https://cdn.jsdelivr.net/gh/synctv-org/docs@main/logo/logo.png)

###### 项目介绍

SyncTV 是一个在线同步播放的项目，它可以让我们在远程同时观看电影或直播。SyncTV 有三大主要功能：同步观看、影院和代理。在同步观看功能中，可以保证所有观看者在同一时间看到同一画面，无论暂停、倒带还是快进，所有人都能保持同步。影院功能中可以提供聊天和弹幕功能，同时观看时还可以进行互动交流。代理功能可以帮助你观看连接速度慢的视频和直播。此外，SyncTV 还支持解析多种平台的视频，如 Alist、Bilibili 和 Emby，未来还会支持解析直播。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240406174959434.png)

###### 如何使用

首先，你可以通过下载 GitHub 页面给出的 Release 最新版本的二进制文件进行手动安装，或者你可以通过给定的 script 或 docker 代码进行安装。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240406175125963.png)

安装完成后，你只需运行 `synctv server` 来启动服务器。服务器每次启动，都会检查具有 root 权限的用户。如果没有找到，它将初始化一个 root 用户，其密码为 root。建议你及时修改用户名和密码。用户注册功能需要使用 OAuth2 服务，例如 Google，GitHub 等。以下是一个在线的一个 DEMO。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240406175217747.png)

###### 项目推介

SyncTV 的作者秉持着让大家方便地一起远程观看电影和学习 Golang 的初衷进行开发，并且声明了它只会在客户端播放视频文件/转发流量，不会拦截、存储或篡改任何用户数据。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=synctv-org/synctv&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/synctv-org/synctv 

开源项目作者：synctv-org

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=synctv-org/synctv)

关注我们，一起探索有意思的开源项目。

