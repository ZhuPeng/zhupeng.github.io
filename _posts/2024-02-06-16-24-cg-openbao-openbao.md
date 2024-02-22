---
layout: post
title: GitHub 开源项目 openbao/openbao 介绍，OpenBao exists to provide a software solution to manage, store, and distribute sensitive data including secrets, certificates, and keys.
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 openbao/openbao，该项目在 GitHub 有超过 1.3k Star，用一句话介绍该项目就是：“OpenBao exists to provide a software solution to manage, store, and distribute sensitive data including secrets, certificates, and keys.”。



![](https://raw.githubusercontent.com/openbao/openbao/master/bao.svg)



背景介绍：
随着现代化系统的复杂度不断提升，需对各种敏感信息的安全问题加以关注。例如数据库证书、第三方服务的 API 密钥或者服务间通信的认证信息。理解谁在何时何地访问了何种敏感信息就已经很困难，而如果再加上密钥环转、安全存储、详细审计日志的需求，就几乎无法不借助定制解决方案来解决这些问题。

项目介绍：
[OpenBao](https://github.com/openbao/openbao) 是一个旨在提供管理、存储和发布包括密钥、证书和敏感数据在内的信息的开源软件解决方案。其主要功能包括：

- **安全的秘密存储**：OpenBao 可以存储任意的密钥/值对。在将它们写入持久化存储器前，OpenBao 会先加密这些数据。这样即使你获取到了原始的存储信息，也无法读取到存储的内容。
- **动态秘密**：OpenBao 可以为某些系统（例如 AWS 或 SQL 数据库）动态生成秘密信息。比如，当一个应用需要访问一个 S3 存储桶时，它可以向 OpenBao 请求访问密钥，OpenBao 就会按需生成一个具有有效权限的 AWS 密钥对。在生成这些动态秘密后，OpenBao 还会自动在租赁期结束后撤销它们。
- **数据加密**：OpenBao 可以加密和解密数据，而无需存储它。这样，安全团队可以定义加密参数，而开发人员可以将加密数据存储在例如 SQL 数据库的地方，无需自行设计加密方法。
- **租赁和续签**：OpenBao 中的所有秘密都有一个与之关联的租期。租期结束时，OpenBao 将自动撤销该租期。客户可以通过内置的 renew API 来续签租期。
- **撤销**：OpenBao 内置了密钥撤销支持。OpenBao 不仅可以撤销单个密钥，还可以撤销一系列密钥，例如某个用户读取的所有密钥，或者一种特定类型的所有密钥。

如何使用：
要开始使用 OpenBao，首先需要在您的机器上安装 Go。然后，克隆此存储库。之后，您可以通过执行 `make bootstrap` 下载所需的构建工具，然后运行 `make` 或 `make dev` 来编译 OpenBao。运行测试，只需要输入 `make test`。

项目推介：
OpenBao 是 Linux 基金会边缘计算小组（LF Edge）的成员，是一个社区驱动，采用 OSI 认可的开源协议的项目。项目的活动度很高，且得到了社区的广泛支持。此外，OpenBao 的安全性已经经过了严格的测试和审查，如果你对 OpenBao 的安全性有任何问题或者发现了任何问题，可以通过开放的邮件列表与开发者团队联系。所以，如果你正在寻找一个关于敏感信息管理的解决方案，OpenBao 绝对值得你关注。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=openbao/openbao&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/openbao/openbao 

开源项目作者：openbao

开源协议：Mozilla Public License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=openbao/openbao)

关注我们，一起探索有意思的开源项目。

