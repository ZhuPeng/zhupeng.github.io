---
layout: post
title: GitHub 开源项目 pufferffish/wireproxy 介绍，Wireguard client that exposes itself as a socks5 proxy
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 pufferffish/wireproxy，该项目在 GitHub 有超过 3.7k Star，一句话介绍该项目：Wireguard client that exposes itself as a socks5 proxy






**背景介绍：**

在日常的网络使用中，我们有时会遇到需要通过特定通道连接某些网站的需求，比如访问多地国际网络资源，或者出于安全、隐私等考虑，需要对我们的网络连接进行一级保护。然而，设置全新的网络接口可能成本较高，同时，每次改变 Wireguard 设置都需要根权限也给使用带来了一定的麻烦。那么，我们如何才能轻松、快捷和安全地进行这样的操作呢？

**项目介绍：**

「 Wireproxy 」是一个 GitHub 开源项目，是一个将其自身展示为 Socks5/HTTP 代理或隧道的 Wireguard 客户端。用于在需要通过特定通道连接某些网站，但又不想设置新网络接口的场景下非常有用。它提供了 TCP 静态路由（包括客户端和服务端）和 Socks5/HTTP 代理（目前只支持 CONNECT），并且开发者正在计划为未来的版本添加 SOCKS5 的 UDP 支持和 UDP 静态路由。

此外，项目对配置文件做了详细的说明，使用者可以轻松设置并进行一系列的定制化操作。作者目前已经将 Wireproxy 连接到一个位于其他国家的 Wwireguard 服务器，并将其配置为某些网站的代理，效率非常高。

**如何使用：**

安装与使用「 Wireproxy 」步骤如下：

1. 克隆项目至本地，命令如下：

```bash
git clone https://github.com/pufferffish/wireproxy
cd wireproxy
make
```

2. 根据配置文件的语法，创建你自己的配置文件，配置文件格式参照上方 README 中的样例。指定你的 Wireguard 接口，以及[ 接口 ]和[ Peer ]等配置

3. 通过指定配置文件路径启用 Wireproxy，命令如下：

```bash
./wireproxy -c [path to config]
```

此外，你也可以通过下列命令进行查看帮助、版本信息，或者检查配置文件的有效性。

```bash
./wireproxy -h|--help  #查看帮助信息
./wireproxy -v|--version #打印版本信息
./wireproxy -n|--configtest #配置测试模式，只检查配置文件的有效性。
```

**项目推介：**

「 Wireproxy 」是一个活跃的开源项目，作者自我驱动不断优化和完善这个项目，以满足更多用户的需求。当前，除了作者外，也有更多的开发者为此项目贡献力量，例如全新的 Amnezia VPN 版本是由开发者 [@juev](https://github.com/juev) 提供的。

与此同时，Wireproxy 也得到了许多用户的一致好评，因其便捷性和实用性，得到了广大使用者的青睐。如果你也有相应的需求，那么赶快尝试使用 Wireproxy 吧，它将会给你带来全新的体验。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=pufferffish/wireproxy&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/pufferffish/wireproxy 

开源项目作者：pufferffish

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=pufferffish/wireproxy)

关注我们，一起探索有意思的开源项目。

