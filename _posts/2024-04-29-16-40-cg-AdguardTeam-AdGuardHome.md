---
layout: post
title: GitHub 开源项目 AdguardTeam/AdGuardHome 介绍，Network-wide ads & trackers blocking DNS server
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 AdguardTeam/AdGuardHome，该项目在 GitHub 有超过 22.7k Star，一句话介绍该项目：Network-wide ads & trackers blocking DNS server




![](https://raw.githubusercontent.com/AdguardTeam/AdGuardHome/master/doc/adguard_home_lightmode.svg)

![](https://cdn.adtidy.org/public/Adguard/Common/adguard_home.gif)


###### 项目介绍

### 背景介绍

在互联网日渐成熟的今天，广告与跟踪器无时无刻不在侵扰我们的数字生活，不仅令人感到烦恼，有时还会对隐私安全造成威胁。这种情况尤其在家庭网络环境中更为普遍，因为现代家庭中的智能设备越来越多，从手机、平板到智能电视、智能家居等，众多设备都可能成为广告与跟踪器的目标。而传统的针对单一设备的广告拦截解决方案，往往无法全面覆盖家庭中所有设备，且安装和维护较为繁琐。

### 

![](https://dalleprodsec.blob.core.windows.net/private/images/830371ad-f860-4083-a59a-0559b4428713/generated_00.png?se=2024-04-30T08%3A40%3A09Z&sig=O2vX3rqC8mToFjurdHPoIrnB1a1iVqZEBvd9Z79D6D8%3D&ske=2024-05-06T06%3A50%3A38Z&skoid=e52d5ed7-0657-4f62-bc12-7e5dbb260a96&sks=b&skt=2024-04-29T06%3A50%3A38Z&sktid=33e01921-4d64-4f8c-a055-5bdaffd5e33d&skv=2020-10-02&sp=r&spr=https&sr=b&sv=2020-10-02)

项目介绍

AdGuard Home 是一个强大的、免费且开源的 DNS 服务器，专注于网络范围内的广告和跟踪器拦截。一旦设置完毕，它能覆盖家中的所有设备，而无需在客户端安装任何软件。AdGuard Home 操作起来像是一个 DNS 服务器，将跟踪域重新路由到“黑洞”，从而防止您的设备连接到这些服务器。它基于我们为公共 AdGuard DNS 服务器使用的软件，并与之共享许多代码。其主要特点包括：

- 允许用户自定义拦截何种内容。
- 监控网络活动。
- 增加自定义过滤规则。
- 自建服务器，用户完全掌控私隐。

### 如何使用

#### 安装
AdGuard Home 提供了多种安装方法，包括自动化脚本安装和手动安装等，支持 Linux / Unix / MacOS / FreeBSD / OpenBSD 等操作系统。以 `curl` 的自动化安装为例：
```sh
curl -s -S -L https://raw.githubusercontent.com/AdguardTeam/AdGuardHome/master/scripts/install.sh | sh -s -- -v
```
安装完成后，你可以根据官方 Wiki 指导文章配置你的设备使用 AdGuard Home。

#### 配置和使用
用户可以通过 AdGuard Home 的管理界面进行详细配置，包括设置拦截规则、查看网络活动等。

### 项目推介

AdGuard Home 自从发布以来，就以其强大的广告和跟踪器拦截能力，以及覆盖全家庭设备的便捷性，受到了广大用户的欢迎。除了源源不断的社区贡献，它也被多家媒体和业内人士推荐。同时，AdGuard Home 在 GitHub 上的活跃开发状态，众多已经使用的知名用户/公司的背书，都表明了它是一个值得信赖和投入使用的解决方案。不论是对于追求隐私保护的个人用户，还是需要为家庭网络环境提供全方位保护的家庭，AdGuard Home 无疑都是一个优秀的选择。

###### 如何使用

###### 项目推介

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=AdguardTeam/AdGuardHome&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/AdguardTeam/AdGuardHome 

开源项目作者：AdguardTeam

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=AdguardTeam/AdGuardHome)

关注我们，一起探索有意思的开源项目。

