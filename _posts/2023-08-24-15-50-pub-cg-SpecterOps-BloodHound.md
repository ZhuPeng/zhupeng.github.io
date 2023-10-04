---
layout: post
title: BloodHound - 一个用于识别 AD 或 Azure 环境中安全漏洞关系的工具
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在 Active Directory 或 Azure 环境中，隐藏的、意外的关系往往会导致复杂的攻击路径，这些路径难以快速识别。BloodHound 使用图论来揭示这些关系，帮助攻击者轻松识别高度复杂的攻击路径，同时帮助防御者识别和消除这些攻击路径。BloodHound 是一个由嵌入式 React 前端和基于 Go 的 REST API 后端组成的单体 Web 应用程序，使用 Postgresql 应用程序数据库和 Neo4j 图数据库，由 SharpHound 和 AzureHound 数据收集器提供数据。


![](https://raw.githubusercontent.com/SpecterOps/BloodHound/master/cmd/ui/public/img/logo-white-full.svg)

###### 项目介绍

BloodHound 是一个用于识别 Active Directory 或 Azure 环境中的特权关系的工具，它使用图论来揭示隐藏的、意外的关系。BloodHound的主要功能包括：

1、识别特权关系；

2、识别特权关系的攻击路径；

3、识别攻击者可能使用的攻击路径；

4、识别可能的攻击路径的防御方法。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230902213132224.png)

BloodHound的主要设计要点包括：

1、使用图论来揭示隐藏的、意外的关系；

2、使用Postgresql应用程序数据库和Neo4j图数据库来存储和查询数据；

3、使用SharpHound和AzureHound数据收集器来收集数据；

4、使用嵌入式 React 前端和基于Go的REST API后端来呈现数据。

###### 如何使用

BloodHound CE 是作为 Docker 镜像分发的，可以在 https://hub.docker.com/r/specterops/bloodhound 上获取。为了更快速的开始使用，项目提供了一个示例 docker-compose 文件夹，在 examples/docker-compose 中提供。按下图方式即可快速开始。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230902213206666.png)

###### 项目推介

BloodHound CE 的文档和开发人员快速入门指南都非常详细，可以帮助用户快速上手使用。如果您是一个安全从业者，BloodHound CE 是一个非常有用的工具，可以帮助您更好地理解和防御攻击。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=SpecterOps/BloodHound&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/SpecterOps/BloodHound 

开源项目作者：SpecterOps

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=SpecterOps/BloodHound)

关注我们，一起探索有意思的开源项目。

