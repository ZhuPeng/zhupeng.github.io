---
layout: post
title: GitHub 开源项目 SpecterOps/BloodHound 介绍，Six Degrees of Domain Admin
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 SpecterOps/BloodHound，该项目在 GitHub 有超过 249 Star，用一句话介绍该项目就是：“Six Degrees of Domain Admin”。


![](https://raw.githubusercontent.com/SpecterOps/BloodHound/master/cmd/ui/public/img/logo-white-full.svg)





背景介绍：
在Active Directory或Azure环境中，隐藏的、意外的关系往往会导致复杂的攻击路径，这些路径难以快速识别。BloodHound使用图论来揭示这些关系，帮助攻击者轻松识别高度复杂的攻击路径，同时帮助防御者识别和消除这些攻击路径。BloodHound是一个由嵌入式React前端和基于Go的REST API后端组成的单体Web应用程序，使用Postgresql应用程序数据库和Neo4j图数据库，由SharpHound和AzureHound数据收集器提供数据。

项目介绍：
BloodHound是一个用于识别Active Directory或Azure环境中的特权关系的工具，它使用图论来揭示隐藏的、意外的关系。BloodHound的主要功能包括：1）识别特权关系；2）识别特权关系的攻击路径；3）识别攻击者可能使用的攻击路径；4）识别可能的攻击路径的防御方法。BloodHound的主要设计要点包括：1）使用图论来揭示隐藏的、意外的关系；2）使用Postgresql应用程序数据库和Neo4j图数据库来存储和查询数据；3）使用SharpHound和AzureHound数据收集器来收集数据；4）使用嵌入式React前端和基于Go的REST API后端来呈现数据。

如何使用：
BloodHound CE是作为Docker镜像分发的，可以在https://hub.docker.com/r/specterops/bloodhound上获取。为了开始使用，提供了一个示例docker-compose文件夹，在examples/docker-compose中提供。运行示例Docker Compose项目需要以下先决条件：Docker和Docker Compose。最简单的方法是安装Docker Desktop，因为它将提供两个先决条件，不需要额外的配置。运行Docker Compose的方法是：1）下载示例docker-compose.yml；2）在复制docker-compose.yml文件的任何目录中，运行docker compose up；3）当API服务器完全启动时，初始密码将显示在日志中；4）转到http://localhost:8080/ui/login，并使用用户名admin和随机生成的密码；5）恭喜，您现在正在运行BloodHound并可以完成应用程序设置。

项目推介：
BloodHound CE由BloodHound Enterprise团队创建和维护，原始的BloodHound由@_wald0、@CptJesus和@harmj0y创建。BloodHound CE是一个活跃的开源项目，拥有许多贡献者和用户，被广泛应用于安全领域。BloodHound CE的文档和开发人员快速入门指南都非常详细，可以帮助用户快速上手使用。如果您是一个安全从业者，BloodHound CE是一个非常有用的工具，可以帮助您更好地理解和防御攻击。




以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=SpecterOps/BloodHound&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/SpecterOps/BloodHound 

开源项目作者：SpecterOps

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=SpecterOps/BloodHound)

关注我们，一起探索有意思的开源项目。

