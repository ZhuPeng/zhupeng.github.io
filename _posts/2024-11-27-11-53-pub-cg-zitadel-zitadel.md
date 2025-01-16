---
layout: post
title: 简化身份基础设施的构建和管理
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

安全有效的用户认证与授权管理是各类网络应用和服务不可或缺的一环。但是，构建一个既安全又灵活的身份验证系统对于许多企业和开发者来说是一项挑战。他们需要应对的问题包括但不限于多租户支持、自服务能力、多因素认证、单点登录（SSO）以及合规性等要求。这些问题不仅对于技术团队而言是复杂的，同时也需要投入大量的时间和资源去实现。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-aed9de1cffdfa89f168958eac6575e8a.png)

今天要给大家推荐一个 GitHub 开源项目 zitadel，该项目在 GitHub 有超过 9.3k Star

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241227001749022.png)

一句话介绍该项目：ZITADEL - Identity infrastructure, simplified for you.

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241201214451426.png)


###### 项目介绍

ZITADEL 致力于简化身份基础设施的构建和管理。它为开发者和企业提供了一个快速部署的用户管理工具，与 Auth0 类似的简洁体验，同时又保持了像 Keycloak 那样的开源灵活性。ZITADEL 提供了包括多租户管理、安全登录、自我服务、OpenID Connect、OAuth2.x、SAML2、LDAP、Passkeys / FIDO2、OTP 等众多现成的功能，并且支持无限的审计跟踪，使其成为一款功能全面且强大的身份验证和授权解决方案。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241201214514249.png)

###### 如何使用

1、部署自托管的 ZITADEL

使用者可以根据自己的需求选择适合的环境部署 ZITADEL，包括 Linux、MacOS、Docker compose、Knative 和 Kubernetes。具体的安装指引可以在项目的官方文档中找到相应的教程和步骤，部署过程少于 3 分钟，快速且高效。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241201214557155.png)

2、设置 ZITADEL Cloud （SaaS）

为了追求更轻松的体验，用户也可以选择使用 ZITADEL Cloud，提供与开源版相同的功能，同时还提供免费的入门级别服务，并支持按需计费。

![](https://user-images.githubusercontent.com/1366906/223662449-f17b734d-405c-4945-a8a1-200440c459e5.gif)

###### 项目推介

ZITADEL 的设计考虑了复杂的多租户架构需求，以 API 优先的方法来确保灵活性和可扩展性。存储模式采用事件溯源，增强了审计能力。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241201214907054.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=zitadel/zitadel&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/zitadel/zitadel 

开源项目作者：zitadel

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=zitadel/zitadel)

关注我们，一起探索有意思的开源项目。

