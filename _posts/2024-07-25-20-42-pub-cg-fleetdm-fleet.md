---
layout: post
title: 为企业 IT 和安全团队打造的开源管理平台
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

企业和组织面临着日益复杂的 IT 和安全挑战，管理成千上万台计算机设备，确保它们的软件更新、安全漏洞得到及时修复，并监控设备健康状况，对 IT 和安全团队来说是一项艰巨的任务。此外，随着远程工作模式的兴起，设备管理（MDM）、设备健康监测和基于姿态的访问控制变得尤为重要。令问题更加复杂的是，很多企业仍在使用笨重、不灵活的软件工具，这些工具难以满足现代 IT 和安全需求，更不用说与现代 DevOps 和 GitOps 实践的整合了。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-dd98d3b5ffee86cee55d13f8390d9a33.png)

今天要给大家推荐一个 GitHub 开源项目 fleet，该项目在 GitHub 有超过 2.7k Star。

![](https://stats.deeptrain.net/repo/fleetdm/fleet/?theme=light)

一句话介绍该项目：Open-source platform for IT, security, and infrastructure teams. (Linux, macOS, Chrome, Windows, cloud, data center)

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240801221154342.png)


###### 项目介绍

Fleet 是一个为 IT 和安全团队设计的开源平台，专注于简化和自动化成千上万台计算机的管理任务。Fleet 支持 Linux、macOS、Windows、Chromebooks 等多个平台，并扩展到云服务和数据中心环境中。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240801221251031.png)

Fleet 的核心特性包括：

1、灵活的 API 与 GitOps 集成：Fleet 提供了灵活的 API 和与 GitOps 实践紧密集成的能力，使设备管理自动化更加高效。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240801221448699.png)

2、安全和设备健康监控：支持漏洞报告、安全态势监控和设备健康状况检查。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240801221511076.png)

3、CIS 基准和策略支持：内置支持 macOS 和 Windows 的 CIS 基准，以及多种安全策略和查询。

4、多平台支持：支持从 Linux 到 IoT 设备的广泛平台。

5、轻量级和模块化设计：Fleet 设计轻量级且模块化，便于定制使用。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240801221525103.png)

###### 如何使用

为了快速开始使用 Fleet，您可以访问 [Fleet 官方网站](https://fleetdm.com) 查看详细文档和教程。基本的安装步骤很简单：

1、访问 Fleet 的 [GitHub 仓库](https://github.com/fleetdm/fleet) 或其 [官网](https://fleetdm.com/docs/get-started/tutorials-and-guides)。

2、根据提供的指南，选择适合您的安装方式：自托管或 Fleet 托管服务。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240801221628861.png)

3、遵循文档完成安装和配置过程，开始管理您的设备。

代码示例和更详细的使用指南，请参考官方文档。

###### 项目推介

Fleet 已在生产环境中获得了广泛应用，包括互联网公司 Fastly 和 Gusto 等。它支持从小规模到大型组织管理成千上万台主机，一些大型组织的响应部署甚至支持超过 400000 台主机。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240801221815770.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=fleetdm/fleet&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/fleetdm/fleet 

开源项目作者：fleetdm

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=fleetdm/fleet)

关注我们，一起探索有意思的开源项目。

