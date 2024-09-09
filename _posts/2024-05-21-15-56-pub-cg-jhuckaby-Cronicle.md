---
layout: post
title: 一个简洁的分布式任务调度系统
tags: 
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

任务调度和管理是一个重要且常见的需求，开发团队经常需要定时执行一系列任务，比如数据备份、报告生成、系统监控等。传统的方法如使用 Linux 的 Cron 工具虽然能够满足基本的定时任务执行，但在面对跨服务器、分布式环境、实时监控和任务失败自动重试等复杂场景时，就显得力不从心。此外，对于非技术人员而言，Cron 的配置和管理并不友好。因此，一个简单易用、功能强大且支持分布式环境的任务调度系统的需求日益增长。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-7ac3d407579b79fa22419dc329a129fc.png)

今天要给大家推荐一个 GitHub 开源项目 Cronicle，该项目在 GitHub 有超过 3.6k Star。

![](https://stats.deeptrain.net/repo/jhuckaby/Cronicle/?theme=light)

一句话介绍该项目：A simple, distributed task scheduler and runner with a web based UI.


![](https://pixlcore.com/software/cronicle/screenshots-new/job-details-complete.png)


###### 项目介绍

Cronicle  是一个基于 Node.js 开发的多服务器任务调度和运行系统，它具有网页前端 UI，支持计划任务、重复任务以及即时任务。它不仅可以替代传统的 Cron，还提供了多项高级功能，如自动故障转移到备份服务器、自动发现附近的服务器、实时任务状态监控、支持任何语言编写的插件等。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240601225749713.png)

Cronicle 设计了简单的 JSON 消息系统供插件使用，支持多时区事件调度，并提供简单 REST API 以及外部通知系统的 Web 钩子。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240601225809266.png)

###### 如何使用

执行如下命令即可快速安装：

```bash
curl -s https://raw.githubusercontent.com/jhuckaby/Cronicle/master/bin/install.js | node
```

使用 Cronicle 创建和管理任务非常直观，你可以通过友好的 Web UI 进行大部分操作。比如，创建一个任务仅需点击几下鼠标，指定任务的执行命令、运行频率以及目标服务器即可。更详细的使用指南，可以参考其 [Web UI Document](https://github.com/jhuckaby/Cronicle/blob/master/docs/WebUI.md)。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240601230021092.png)

###### 项目推介

Cronicle 由于其简单、强大和高度可配置的特性，已经被多家知名公司采用于生产环境。项目自推出以来，一直保持着较高的开发活跃度。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240601230058695.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=jhuckaby/Cronicle&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/jhuckaby/Cronicle 

开源项目作者：jhuckaby

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=jhuckaby/Cronicle)

关注我们，一起探索有意思的开源项目。

