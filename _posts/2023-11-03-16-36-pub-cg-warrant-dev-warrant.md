---
layout: post
title: Warrant - 一个高度可扩展的、集中式的权限控制服务
tags: 
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 warrant-dev/warrant，该项目在 GitHub 有差不多 1000 Star，用一句话介绍该项目就是：“Warrant is a highly scalable, centralized authorization service based on Google Zanzibar, used for defining, querying, and auditing application authorization models and access control rules.”。

在应用程序授权模型和访问控制规则的定义、查询和审计方面，Warrant 是一个基于 Google Zanzibar 的高度可扩展的集中式授权服务。Warrant 解决了各种应用程序授权和访问控制方面的问题，包括角色基本访问控制（RBAC）、属性基本访问控制（ABAC）和关系基本访问控制（ReBAC）等。

![](https://warrant.dev/images/logo-primary-wide.png)

###### 项目介绍

Warrant 是一个高度可扩展的、集中式的授权服务，用于定义、存储、查询、检查和审计应用程序授权模型和访问规则。Warrant 的核心是一个基于关系的访问控制（ReBAC）引擎，受到了 Google Zanzibar 的启发。它能够执行任何授权模式，包括角色基本访问控制（RBAC）、属性基本访问控制（ABAC）和关系基本访问控制（ReBAC）。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231119220805232.png)

Warrant 的功能包括：

- 通过 HTTP API 从应用程序、CLI 工具等管理授权模型、访问规则和其他 Warrant 资源（角色、权限、特性、租户、用户等）。
- 实时、低延迟的 API，用于在运行时在应用程序中执行访问检查。
- 与内部和第三方身份验证/身份提供者（如 Auth0 和 Firebase）集成。
- 可查询的全局事件日志，跟踪对授权模型、访问规则和所有其他 Warrant 资源的更新，使审计和调试变得简单。
- 官方支持的大多数流行语言和框架的 SDK。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231119220920647.png)

- 支持多个数据库，包括 MySQL、Postgres 和 SQLite。

###### 如何使用

您可以通过 Warrant Cloud 提供的托管云服务来快速开始使用 Warrant。您可以在 https://app.warrant.dev/signup 注册免费账户。

Warrant Cloud 与此开源版本兼容，并提供额外的功能，例如：
- 管理员仪表板，通过直观、易于使用的用户界面快速管理授权模型和访问规则。
- 实时“查询” API，用于查询和审计给定主体或对象的访问规则。
- 多区域可用性。
- 改进的访问检查延迟和吞吐量。

同时也可以自己克隆代码进行编译使用，参考如下：

```bash
git clone git@github.com:warrant-dev/warrant.git
cd cmd/warrant
make dev
./bin/warrant

# 可以使用如下 curl 命令与 Server 进行交互
curl -g "http://localhost:port/v1/object-types" -H "Authorization: ApiKey YOUR_KEY"
```

###### 项目推介

Warrant 有着较好的开发状态和维护者声誉，它已经得到了许多知名用户和公司的使用，广泛应用于产品、安全和合规性等领域。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231119221108583.png)


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=warrant-dev/warrant&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/warrant-dev/warrant 

开源项目作者：warrant-dev

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=warrant-dev/warrant)

关注我们，一起探索有意思的开源项目。

