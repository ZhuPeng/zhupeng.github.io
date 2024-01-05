---
layout: post
title: GitHub 开源项目 ihmily/DouyinLiveRecorder 介绍，可循环值守和多人录制的直播录制软件，支持抖音、Tiktok、快手、虎牙、斗鱼、B站、小红书等平台直播录制，抓取多平台直播源地址，抖音无水印解析，快手无水印解析
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 ihmily/DouyinLiveRecorder，该项目在 GitHub 有差不多 1000 Star，用一句话介绍该项目就是：“可循环值守和多人录制的直播录制软件，支持抖音、Tiktok、快手、虎牙、斗鱼、B站、小红书等平台直播录制，抓取多平台直播源地址，抖音无水印解析，快手无水印解析”。


![video_spider](https://socialify.git.ci/ihmily/DouyinLiveRecorder/image?font=Inter&forks=1&language=1&owner=1&pattern=Circuit%20Board&stargazers=1&theme=Light)
![Hmily](https://github.com/ihmily.png?size=50)



背景介绍：
随着直播行业的繁荣发展，越来越多的粉丝希望能够保存他们最爱的主播的直播内容，无论是用于个人收藏，还是进行回放学习。然而，大多数直播平台并没有提供直播录制功能，而专业的录屏软件操作复杂、功能过于庞大，不适合一般用户的使用。同时，直播内容实时性强，人为操作不可能做到全天候监控。因此，如何找到一款面向多平台，且能实现自动值守录制的工具，成为了亟待解决的问题。

项目介绍：
《抖音直播录制工具》是一个基于 `FFmpeg` 实现的，面向多直播平台（包括抖音、Tiktok、快手、虎牙、斗鱼、B站、小红书等）的录制工具。这个工具不仅可以实现自动化、循环的值守直播录制，而且支持自定义配置录制以及直播状态推送。在项目结构上，所有配置、日志、备份文件、依赖库以及主要执行文件等都分别放在各自的文件夹内，简单明了，利于维护。同时，项目支持Docker容器化运行，使用本项目提供的 `Dockerfile` 可以在Docker环境中快速运行，方便部署。

如何使用：
你可以直接克隆项目到本地，运行主文件 `main.py` 启动程序。录制配置在 `config` 文件夹内的配置文件中进行，并在 `URL_config.ini` 中添加录制直播间地址。抖音录制需要使用到PC网页端直播间页面的Cookie，请在 `config.ini` 配置文件中添加。同时支持按链接进行录制的关闭和启动。如果想要在Docker容器中运行，你需要先安装[Docker](https://docs.docker.com/get-docker/) 和 [Docker Compose](https://docs.docker.com/compose/install/)，然后运行项目中的 `docker-compose.yaml` 文件即可。

项目推介：
该项目由知名开发者 ihmily 开发，维护活跃，问题回复迅速。且目前已经在多个场景中得到了实际应用，比如进行直播教学内容的后期编辑，进行竞品直播内容的分析等等。在业内也得到了一定的好评。无论你是想记录下自己喜欢的直播内容，还是进行相关的研究分析，如果遇到了直播录制的问题，都十分值得尝试这个项目。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=ihmily/DouyinLiveRecorder&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/ihmily/DouyinLiveRecorder 

开源项目作者：ihmily

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=ihmily/DouyinLiveRecorder)

关注我们，一起探索有意思的开源项目。

