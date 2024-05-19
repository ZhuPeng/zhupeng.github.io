---
layout: post
title: 探索生活中的每一帧，一款 AI 驱动的照片应用
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在这个数字化时代，我们每天都会产生海量的照片和视频，从日常生活到特殊场合，这些珍贵的记忆被保存在我们的设备中。然而，随着时间的积累，管理和检索这些图片变得越来越困难。传统的照片应用往往因缺乏智能化、隐私担忧以及依赖集中式云服务的限制而不尽人意。我们需要一个更自由、更隐私、更智能的解决方案来管理我们的数字记忆。

今天要给大家推荐一个 GitHub 开源项目 photoprism/photoprism，该项目在 GitHub 有超过 32.6k Star，一句话介绍该项目：AI-Powered Photos App for the Decentralized Web

![](https://dl.photoprism.app/img/ui/search-cards-view.jpg)


###### 项目介绍

PhotoPrism 是一个完全开源的 AI 驱动的照片应用，旨在为去中心化网络打造。

![](https://www.photoprism.app/user/pages/01.home/03._screenshots/iphone-maps-hybrid-540px.png)

利用最新技术，PhotoPrism 自动标记和查找图片，无需繁复操作。你可以在家中、私有服务器或云端运行它，无需担忧原始文件的转换、重复文件或视频格式问题。其丰富的功能，如高效图片检索、人脸识别、自动分类、实时照片播放、元数据提取等，都设计得既用户友好又注重隐私。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240504224752493.png)

###### 如何使用

安装 PhotoPrism，你只需要一个 Web 浏览器和 Docker。官方文档提供了详尽的逐步安装指南，涵盖了 Mac、Linux 和 Windows 平台。对于 64 位 AMD、Intel 和 ARM 处理器，提供了多架构镜像，意味着从 Raspberry Pi 到 Apple Silicon 的用户都能享受相同的功能和安装步骤。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240504225132117.png)

示例命令安装参考如下，这将下载并启动最新版的 PhotoPrism。
```bash
docker pull photoprism/photoprism:latest
docker run -d --name photoprism -p 2342:2342 photoprism/photoprism:latest
```
###### 项目推介

PhotoPrism 是由一个独立的团队完全自资开发的，这保证了它的独立性和对隐私的尊重。它不会将你的数据出售给任何第三方。其开源特性、强大的 AI 功能、注重用户隐私的设计理念吸引了广泛的社区参与和支持。此外，通过其公开的演示版本和活跃的社区支持，PhotoPrism 已经得到了包括技术爱好者、专业摄影师以及隐私倡导者在内的广泛认可。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240504225256543.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=photoprism/photoprism&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/photoprism/photoprism 

开源项目作者：photoprism

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=photoprism/photoprism)

关注我们，一起探索有意思的开源项目。

