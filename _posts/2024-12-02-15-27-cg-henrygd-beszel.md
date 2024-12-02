---
layout: post
title: GitHub 开源项目 henrygd/beszel 介绍，Lightweight server monitoring hub with historical data, docker stats, and alerts.
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 henrygd/beszel，该项目在 GitHub 有超过 3.2k Star。

![](https://stats.deeptrain.net/repo/henrygd/beszel/?theme=light)

一句话介绍该项目：Lightweight server monitoring hub with historical data, docker stats, and alerts.




![Screenshot of the hub](https://henrygd-assets.b-cdn.net/beszel/screenshot.png)


###### 项目介绍

### 背景介绍

在当今这个信息技术快速发展的时代，服务器和容器的健康监控成为了 IT 行业的一项重要任务。服务器作为提供各种服务的基础，其稳定性、性能以及资源使用情况直接影响到企业的运营效率和服务质量。传统的监控工具虽然功能强大，但往往资源消耗大、配置复杂且难以管理。在面对大量服务器和容器时，企业需要一个轻量级、易于部署和使用的监控解决方案来简化管理过程，同时保证有效的资源监控和及时的异常警报。

### 

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-5a98e4b69a62c93105239e390526d218.png)

项目介绍

**Beszel** 是一个轻量级服务器资源监控工具，它专为简化服务器和容器的健康监控而设计。Beszel 提供了历史数据记录、Docker 统计信息和警报功能，结合其占用资源少的优势，成为了一个高效的监控解决方案。

该项目的核心特点包含：

- **轻量级**：与主流解决方案相比，Beszel 使用更少的资源。
- **易用性**：简易的设置过程，无需公共互联网暴露。
- **Docker 统计**：追踪每个容器的 CPU、内存和网络使用历史。
- **警报系统**：为 CPU、内存、磁盘、带宽、温度和系统状态配置警报。
- **多用户支持**：每个用户可管理自己的系统，管理员可跨用户共享系统。
- **OAuth / OIDC 支持**：支持多个 OAuth2 提供商。可以禁用密码认证。
- **自动备份**：支持从磁盘或 S3 兼容存储保存和恢复数据。
- **REST API**：在自己的脚本和应用程序中使用或更新数据。

Beszel 由两个主要组件构成：**Hub**（一个提供用于查看和管理连接系统的仪表板的 Web 应用程序）和 **Agent**（运行在您想要监控的每个系统上的最小 SSH 服务器，用于向 Hub 通报系统指标）。

### 如何使用

通过以下步骤可轻松部署 Beszel：

1. 启动 Hub（参见[安装](#installation)部分）。
2. 打开并创建一个管理员用户。
3. 点击“添加系统”。输入要监控的系统的名称和主机。
4. 点击“复制 docker compose”，以将 agent 的 docker-compose.yml 文件复制到剪贴板。
5. 在 agent 系统上，创建 compose 文件并运行 `docker compose up` 启动 agent。
6. 在 Hub 中，点击对话框中的“添加系统”按钮完成添加系统。

### 项目推介

Beszel 由于其轻量级和简易性特点，已经在多个企业和个人项目中得到应用。开源项目的活跃状态、简洁而强大的功能让它在社区中获得了好评。尽管 Beszel 并非市场上唯一的资源监控解决方案，但其对 Docker 容器监控的原生支持、易于部署的特性和灵活的配置选项使它成为小型到中型企业和技术爱好者的理想选择。此外，项目作者 Henrygd 通过 GitHub 提供实时的支持和更新，保证了该项目的持续发展和稳定性。

无论您是正在寻找简化 IT 基础设施管理的解决方案，还是需要一个低开销的服务器监控工具，Beszel 都能满足您的需求，帮

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=henrygd/beszel&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/henrygd/beszel 

开源项目作者：henrygd

开源协议：MIT License

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=henrygd/beszel)

关注我们，一起探索有意思的开源项目。

