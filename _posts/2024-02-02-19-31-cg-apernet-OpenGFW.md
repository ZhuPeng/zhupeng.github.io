---
layout: post
title: GitHub 开源项目 apernet/OpenGFW 介绍，OpenGFW is a flexible, easy-to-use, open source implementation of GFW on Linux
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 apernet/OpenGFW，该项目在 GitHub 有超过 4.8k Star，用一句话介绍该项目就是：“OpenGFW is a flexible, easy-to-use, open source implementation of GFW on Linux”。


![OpenGFW](https://raw.githubusercontent.com/apernet/OpenGFW/master/docs/logo.png)



背景介绍：在如今的网络环境中，我们有时会遇到一些如广告拦截、家长控制、恶意软件保护、VPN/代理服务的滥用预防、流量分析等问题，这些都与本项目有紧密的联系。些许问题难以避过且陷入困境，特别是在对这些问题了解不够深入的情况下，希望能有一个工具能够有力的解决这些问题。

项目介绍：OpenGFW 是一款灵活且易于使用的开源 GFW 实现程序，具备许多比实际 GFW 更强大的地方，是你能在家庭路由器上拥有的网络主权。然而，本项目还处于早期发展阶段，请自行承担风险。我们正在寻找有志同行的贡献者来帮助我们推进项目，尤其是实现更多协议的分析器！这个项目的特点有：完全的 IP/TCP 重组，各种协议分析器，全面的 IPv4 和 IPv6 支持，基于流的多核负载平衡，连接卸载，基于 expr 的强大规则引擎，灵活的分析器 & 修改器框架，可扩展的 IO 实现 (目前仅 NFQueue)，Web UI 等。

如何使用：首先需要构建项目，使用 go build 命令即可。然后设置环境变量 OPENGFW_LOG_LEVEL 为 debug。最后运行 ./OpenGFW -c config.yaml rules.yaml 命令即可进行项目的运行。项目还提供了详细的配置示例和规则示例用于参考，你可以根据自己的需求进行调整。

项目推介：OpenGFW 项目虽然处于早期的开发阶段，但已得到许多开发者的关注，其开发活动也很活跃。该项目具备广泛的用途，如广告屏蔽，家长控制，恶意软件保护，VPN/代理服务的滥用预防，流量分析等。此外，项目还在积极寻找贡献者，参与其中不仅可以获得丰富的开源开发经验，也会有机会与一群有志同行的开发者共同进步。我强烈推荐所有关注网络安全和数据分析的研究者和工程师关注并尝试使用 OpenGFW。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=apernet/OpenGFW&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/apernet/OpenGFW 

开源项目作者：apernet

开源协议：Mozilla Public License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=apernet/OpenGFW)

关注我们，一起探索有意思的开源项目。

