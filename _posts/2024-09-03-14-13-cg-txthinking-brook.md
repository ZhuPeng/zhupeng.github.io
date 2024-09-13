---
layout: post
title: GitHub 开源项目 txthinking/brook 介绍，A cross-platform programmable network tool
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 txthinking/brook，该项目在 GitHub 有超过 14.5k Star。

![](https://stats.deeptrain.net/repo/txthinking/brook/?theme=light)

一句话介绍该项目：A cross-platform programmable network tool




![](https://brook.app/images/appstore.png)

![](https://brook.app/images/android.png)

![](https://brook.app/images/mac.png)

![Windows](https://brook.app/images/windows.png)

![](https://brook.app/images/linux.png)

![OpenWrt](https://brook.app/images/openwrt.png)


###### 项目介绍

**背景介绍：**

在当今的网络世界里，网络安全和隐私保护愈发成为人们日益关注的话题。随着人们对网络自由和信息安全的需求增加，如何在确保网络通信安全的同时，优化网络访问体验，就成了一个重要的技术难题。传统的网络工具往往只能提供基础的代理功能，不能很好地解决如 DNS 污染、不稳定的网络环境，以及不同平台间配置复杂性的问题，且缺少自定义网络请求处理的能力，这些问题限制了用户在享受网络服务时的自由度和安全性。

**

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-1600e786739213c3cca3d06df23bf885.png)

项目介绍：**

`Brook` 是一个跨平台的可编程网络工具，致力于解决上述网络中遇到的问题。它通过提供 Socks5 /HTTP 代理以及基于虚拟网络卡的技术，能够全面接管系统网络请求，包括基于 UDP 的 http3，从而有效规避 DNS 污染，优化网络环境。此外，`Brook` 的另一个显著特点是支持网络请求的编程控制，使用户能根据自己的需求定制具体的网络请求处理逻辑，极大地提高了网络工具的灵活性和适用性。其全平台兼容性也极大简化了用户的使用成本，为用户在不同的操作系统平台上提供了一致的网络优化体验。

**如何使用：**

1. 首先在服务器端开启 `Brook` 服务：
    ```bash
    bash <(curl https://bash.ooo/nami.sh)
    nami install brook
    brook server -l :9999 -p hello
    ```
2. 客户端的使用取决于不同的平台，`Brook` 提供了 iOS、Android、Mac、Windows、Linux 以及 OpenWrt 的版本，用户可以根据自己的设备选择相应的安装方式。具体的安装方法请参见项目的官方文档。

3. 对于希望通过命令行使用 `Brook` 的用户，可以通过简单的 `brook` 命令来创建本地的 Socks5 或 HTTP 代理，并通过系统或浏览器的代理设置来使用该代理。

**项目推介：**

`Brook` 是一个活跃发展中的开源项目，它的功能强大与使用简便使其在开源社区中获得了不错的声誉。`Brook` 不仅被单个用户所喜爱，也被多个公司和组织广泛应用于他们的网络解决方案中。作者 txthinking 的贡献赢得了开源社区的广泛认可。此外，`Brook` 还拥有着丰富的文档和教程，帮助用户轻松上手并快速解决问题。无论是对于追求网络自由的个人用户，还是需要定制网络请求处理逻辑的开发者而言，`Brook` 都是一个不容错过的工具。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=txthinking/brook&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/txthinking/brook 

开源项目作者：txthinking

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=txthinking/brook)

关注我们，一起探索有意思的开源项目。

