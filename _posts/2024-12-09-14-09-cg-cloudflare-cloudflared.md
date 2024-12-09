---
layout: post
title: GitHub 开源项目 cloudflare/cloudflared 介绍，Cloudflare Tunnel client (formerly Argo Tunnel)
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 cloudflare/cloudflared，该项目在 GitHub 有超过 9.4k Star。

![](https://stats.deeptrain.net/repo/cloudflare/cloudflared/?theme=light)

一句话介绍该项目：Cloudflare Tunnel client (formerly Argo Tunnel)





###### 项目介绍

### **Cloudflare Tunnel 客户端介绍**

在这个快速发展的数字时代，网络安全和数据隐私变得越来越重要。各种网络攻击和数据泄露事件频发，尤其是对于企业和有着敏感数据交换的团体来说，保护内部网络对外界的暴露是一项巨大的挑战。传统的解决方案往往需要在防火墙上开启特定端口，这不仅复杂且风险高。这就是我们需要 Cloudflare Tunnel 客户端的原因。

#### **项目背景**

Cloudflare Tunnel 客户端旨在为企业或个人提供一条安全的数据通道，将 Cloudflare 网络和您的来源服务器（例如网站服务器）之间建立起一个安全的隧道。利用 Cloudflare 强大的网络服务，通过这一客户端，无需对外开放源服务器的任何接口，便可以实现数据的高效、安全传输。

#### **主要功能与设计要点**

- **安全连接**：它在 Cloudflare 网络和您的源（例如，Web 服务器）之间创建一个代理通道，通过 Cloudflare 将客户端请求发送给您，同时保持您的源服务器对外界的关闭状态，以最大程度上保障您的数据安全。
- **灵活访问**：除了 HTTP/websocket 流量外，还可以利用 `cloudflared` 访问通过 `cloudflared tunnel` 保护的 TCP 流量，适用于 SSH、RDP 等多种用例。
- **容易安装**：提供多种安装方式，包括二进制文件、Docker 镜像、Debian包、RPM包和Homebrew包等，支持多种操作系统。
- **用户友好的文档**：提供了全面的使用文档，帮助用户快速上手。

#### **如何使用**

1. 前提条件：在 Cloudflare 控制台完成一些步骤，包括添加一个网站到 Cloudflare 账户，更改您的域名服务器到 Cloudflare。
2. 安装：根据您的操作系统选择合适的安装方式。例如，在 macOS 上可以通过 Homebrew 安装，或下载最新的 Darwin amd64 版本。
3. 创建隧道和路由流量：安装后，可将 `cloudflared` 认证到您的 Cloudflare 账户，并开始创建隧道来为您的源服务流量。

#### **项目推介**

Cloudflare Tunnel 客户端是 Cloudflare 提供的成熟产品之一，目前已广泛应用于各行各业。它的活跃开发状态、强大的 Cloudflare 后盾、丰富的文档资料，以及简单的安装过程使其成为保护网站安全、保持内部网络隐私的首选工具。无论是小型企业还是大型企业，都可以从 Cloudflare Tunnel 中受益，实现数据的安全无忧传输。

结合 Cloudflare 的广泛用户基础和行业内的高知名度，Cloudflare Tunnel 客户端是目前市场上最值得信赖的网络安全解决方案之一，无疑将为您的网络安全提供强有力的支持。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=cloudflare/cloudflared&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/cloudflare/cloudflared 

开源项目作者：cloudflare

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=cloudflare/cloudflared)

关注我们，一起探索有意思的开源项目。

