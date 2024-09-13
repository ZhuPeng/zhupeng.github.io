---
layout: post
title: GitHub 开源项目 smallstep/certificates 介绍，🛡️ A private certificate authority (X.509 & SSH) & ACME server for secure automated certificate management, so you can use TLS everywhere & SSO for SSH.
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 smallstep/certificates，该项目在 GitHub 有超过 6.5k Star。

![](https://stats.deeptrain.net/repo/smallstep/certificates/?theme=light)

一句话介绍该项目：🛡️ A private certificate authority (X.509 & SSH) & ACME server for secure automated certificate management, so you can use TLS everywhere & SSO for SSH.





###### 项目介绍

### 背景介绍
在现代的互联网应用开发和运维中，TLS/SSL 证书的管理变得越来越重要，它们是确保数据传输安全的关键。然而，企业面临着密钥和证书管理的复杂挑战，例如如何自动化地发放、更新和吊销证书，特别是在涉及大量不同用途（例如 HTTPS、SSH 等）的证书管理时。传统的证书颁发机构（CA）操作繁琐，无法满足自动化和灵活性的需求。因此，开发者和企业迫切需要一个能够简化和自动化证书管理过程的解决方案。

### 

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-0d2027193c809551cc7caf24aea0b0bc.png)

项目介绍
`step-ca` 是 Smallstep Labs 维护的一个开源在线证书颁发机构，专为 DevOps 环境中的安全、自动化证书管理而设计。它不仅支持发放与浏览器兼容的 HTTPS 服务端和客户端证书，还覆盖了 DevOps 所需的 TLS 证书，例如 VM、容器、API、数据库连接、Kubernetes Pods 等。此外，`step-ca` 提供了 SSH 证书的发放解决方案，支持单点登录（SSO）和云实例身份验证。通过支持 ACME 协议和提供 Go 语言封装以及命令行客户端，`step-ca` 显著简化了证书的自动化管理流程。

项目特点包括：
- 对标准互联网 X.509 认证，支持 RFC5280 和 CA/Browser Forum 规范
- 支持多种类型的证书发放，包括 HTTPS、TLS、SSH 等
- 提供灵活的自动化证书管理方案，如 ACME 服务器、Go 包装器、命令行客户端
- 支持多种数据库后端，如 Badger, BoltDB, Postgres 和 MySQL
- 支持多种授权方式以适应不同的使用场景

### 如何使用
要开始使用 `step-ca`，您首先需要安装该软件包。安装指南可在其 [官方文档](https://smallstep.com/docs/step-ca/installation) 中找到。安装完成后，您可以根据文档设置您的证书颁发机构，创建和管理证书。例如，使用 `step-ca` 进行 ACME 协议的证书自动化管理：

```
# 初始化 step-ca 配置
$ step ca init

# 启动 step-ca 服务器
$ step-ca $(step path)/config/ca.json
```

对于客户端，可以使用 Smallstep 提供的 `step` CLI 工具与 `step-ca` 交互，完成证书的申请、续期等操作。

### 项目推介
`step-ca` 由 Smallstep Labs 维护，这是一个致力于简化和改善现代互联网安全标准的公司。项目在 GitHub 上开源，拥有活跃的开发社区，持续进行优化和功能扩展。该项目不仅被许多开发人员和企业用于构建安全的 DevOps 环境，还经常出现在安全和 DevOps 相关的专业讨论和会议中。无论您是需要为您的网站自动化 HTTPS 证书的管理，还是在您的 DevOps 工作流中实现 TLS 和 SSH 证书的自动化，`step-ca` 都能以灵活、高效的方式满足您的需求。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=smallstep/certificates&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/smallstep/certificates 

开源项目作者：smallstep

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=smallstep/certificates)

关注我们，一起探索有意思的开源项目。

