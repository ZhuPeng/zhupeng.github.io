---
layout: post
title: GitHub 开源项目 openpubkey/openpubkey 介绍，Reference implementation of OpenPubkey
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 openpubkey/openpubkey，该项目在 GitHub 有差不多 1000 Star，用一句话介绍该项目就是：“Reference implementation of OpenPubkey”。





背景介绍：
在日常的网络环境中，我们不可避免地会遇到一些信息保密和数据认证的问题。在网络身份管理领域，公钥加密技术和证书颁发机构（ CA ）已经是我们解决这些问题的标准工具。但是，这些传统方案并不是无懈可击的。其一，当我们使用公钥加密时，我们需要知道并信任另一方的公钥，否则加密和签名的行为都将不具备任何意义。其二，证书颁发机构的工作量和复杂性非常大，需要处理大量的证书请求，这将增加维护和管理的成本。

项目介绍：
面对以上问题，OpenPubkey 项目的推出为我们提供了简单高效的解决方案。OpenPubkey 是一个利用 OpenID Providers ( OPs ) 将身份绑定到公钥的协议。它将用户或工作负载产生的公钥加入到 OpenID Connect ( OIDC ) 中，使得各个身份可以在其 OIDC 身份下签署信息或者制品。在这个过程中 OpenPubkey 没有添加任何新的信任方，它与现有的 OpenID Providers 像 Google 、Azure/Microsoft 、Okta 、OneLogin 、Keycloak 完全兼容，无需改变 OpenID Provider 便可使用。OpenPubkey 将公钥和身份的绑定关系表示为一个 PK Token ，这种方式额外的好处是，这个处于 CA 位置的 OP 不需要去处理大量的证书请求，大幅度减轻了管理的复杂性和工作量。这个 token 可以和证书一样分发，作为签名的基础。OpenPubkey 是由 Linux Foundation 主导的开源项目，已经有像 Docker, Inc 和 BastionZero 这样的公司正在使用 OpenPubkey 进行开发。

如何使用：
要创建和验证 PK Tokens ，需要安装 OpenPubkey 客户端和验证器。首先，你需要参考 README 中的概述部分和用户身份小节，理解 OpenPubkey 是如何工作的。然后，在用户身份，nonce，ID Token 和 PK Tokens 这几项的说明中，你会找到具体的使用方法和样例，你可以参考这些步骤尝试使用 OpenPubkey 。

项目推介：
OpenPubkey 是一个值得推荐的开源项目。首先，该项目是由 Linux Foundation 发起并维护的，这个机构的威望和影响力在全球的开源社区中都是非常高的，这意味着 OpenPubkey 有很高的项目质量和可依赖性。其次，知名的开源公司 Docker, Inc 正在使用 OpenPubkey 来对 Docker 官方镜像进行签名，这说明 OpenPubkey 的实用性和实用价值已经得到了市场的初步认可。最后，OpenPubkey 的代码完全开源，并且遵循 Apache 2.0 协议，这意味着任何人都可以自由地使用和改进这个项目。总的来说，无论是对于开发者还是公司，OpenPubkey 都是一个值得尝试和投入使用的项目。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=openpubkey/openpubkey&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/openpubkey/openpubkey 

开源项目作者：openpubkey

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=openpubkey/openpubkey)

关注我们，一起探索有意思的开源项目。

