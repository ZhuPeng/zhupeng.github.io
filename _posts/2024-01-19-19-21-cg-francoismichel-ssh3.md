---
layout: post
title: GitHub 开源项目 francoismichel/ssh3 介绍，SSH3: faster and rich secure shell using HTTP/3, checkout our article here: https://arxiv.org/abs/2312.08396
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 francoismichel/ssh3，该项目在 GitHub 有超过 2.3k Star，用一句话介绍该项目就是：“SSH3: faster and rich secure shell using HTTP/3, checkout our article here: https://arxiv.org/abs/2312.08396”。


![](https://raw.githubusercontent.com/francoismichel/ssh3/master/resources/figures/ssh3.png)
![](https://raw.githubusercontent.com/francoismichel/ssh3/master/resources/figures/ssh3_100ms_rtt.gif)
![](https://raw.githubusercontent.com/francoismichel/ssh3/master/resources/figures/ssh3_oidc.gif)



背景介绍：
在当今信息安全对于企业、个人或系统来说都至关重要的背景下，我们需要像 SSH 这样用于加密远程登录的安全协议。然而，SSH2协议虽然在功能上已经相当完善，但是在满足现代网络环境的安全和性能需求上仍存在一些瓶颈。

项目介绍：
SSH3项目是 SSH 协议的全新改造。基于 HTTP 的机制，他使用 QUIC+TLS1.3 进行安全通道的建立，使用 HTTP 授权机制进行用户认证。SSH3 具有以下突出的改进：会话创建速度提升显著；增加了新的 HTTP 认证方法例如 OAuth 2.0 和 OpenID Connect；可以抵抗端口扫描攻击方案，使你的 SSH3 服务器在 Internet 用户眼里变得"看不见"；支持 TCP 和 UDP 的端口转发；以及所有的 QUIC 协议支持的现代特性，比如迁移连接（即将推出）和多路径连接等。

如何使用：
首先，你需要安装 SSH3，详细步骤可在项目 README 中的"install SSH3"部分找到。接下来，按照"Deploying an SSH3 server"和"Using the SSH3 client"部分的指南分别进行服务器设置和客户端的使用。

项目推介：
虽然 SSH3 目前还处于实验阶段，但是已经展示出了巨大的潜力和前景。目前 SSH3 处于活跃的开发状态，由来自知名大学的科研团队负责开发和维护，且已经有一篇相关的论文在顶级会议上被接收。这个项目的开源让更多的开发者、研究人员有机会为其优化和安全性提供建议和贡献。如果你对 SSH3 的开发有相关专业知识，欢迎你的加入和协作。



以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=francoismichel/ssh3&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/francoismichel/ssh3 

开源项目作者：francoismichel

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=francoismichel/ssh3)

关注我们，一起探索有意思的开源项目。

