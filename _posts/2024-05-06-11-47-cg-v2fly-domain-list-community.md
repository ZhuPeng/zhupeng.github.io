---
layout: post
title: GitHub 开源项目 v2fly/domain-list-community 介绍，Community managed domain list. Generate geosite.dat for V2Ray.
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 v2fly/domain-list-community，该项目在 GitHub 有超过 4.1k Star，一句话介绍该项目：Community managed domain list. Generate geosite.dat for V2Ray.





###### 项目介绍

在当今的互联网世界中，越来越多的服务和应用依赖于精准而高效的内容路由与访问控制。用户和服务提供商面临的一个主要问题是如何根据地理位置、内容类型或服务提供者等因素，对网络请求进行适当的导向。这不仅涉及到优化用户体验，提高访问速度，也关乎某些区域对内容访问的特殊要求或限制。手动管理和维护一个庞大且实时更新的域名列表，并据此实施路由决策，是一个极具挑战的任务。

**[v2fly/domain-list-community](https://github.com/v2fly/domain-list-community)** 项目应运而生，旨在提供一个由社区管理的域名列表，支持生成用于 V2Ray 项目的 `geosite.dat` 文件，为项目 V 中的路由用途服务。该项目的核心目标是集合广大社群的力量，共同维护一个公正、全面的域名清单，而不倾向于支持或暗示任何特定的域名应被封锁或代理。

这个项目特别突出了其工作原理：通过社区成员的共同努力，根据不同的需求和标准（如公司归属、内容类别等）整理域名，并用特定的格式记录在文件中，这些文件最终会被构建成一个外部的 `geosite` 文件。这样，用户便可以轻松根据这个文件实施复杂的路由策略，比如针对特定的广告域名、成人内容域名或特定地理位置的域名实施拦截、直连或代理。

### 如何使用：

1. 安装 `golang` 和 `git`。
2. 克隆项目代码：`git clone https://github.com/v2fly/domain-list-community.git`。
3. 进入项目根目录：`cd domain-list-community`。
4. 安装项目依赖：`go mod download`。
5. 生成 `dlc.dat` 文件：`go run ./`（不带 `datapath` 选项使用的是当前工作目录下的 `data` 目录中的域名列表）。

此外，项目还提供了生成自定义数据目录的 `dlc.dat` 文件的选项，以及详细的使用示例，引导用户在 V2Ray 配置中如何利用这些域名列表提高路由决策的效率和准确度。

### 项目推介：

自项目启动以来，**v2fly/domain-list-community** 因其高度开放和社区驱动的特性，吸引了众多开发者和用户的关注和贡献。不仅活跃的开发社区保证了域名列表的及时更新，其背后强大的社区支持也确保了数据质量和可靠性。许多寻求高效内容路由解决方案的用户和公司已经开始采用这个项目，其中不乏对网络性能有严苛要求的企业用户。

结合其用途、社区活力和持续增长的用户基础，**v2fly/domain-list-community** 是为那些需要优化其网络路由策略、提高内容访问效率及满足特定地域访问规则的个人或组织的理想选择。该项目的开放性、透明性以及强大的社区支持，使其成为了在全球不断增长的网络挑战中，值得信赖的伙伴。

###### 如何使用

###### 项目推介

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=v2fly/domain-list-community&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/v2fly/domain-list-community 

开源项目作者：v2fly

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=v2fly/domain-list-community)

关注我们，一起探索有意思的开源项目。

