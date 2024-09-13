---
layout: post
title: GitHub 开源项目 aceberg/WatchYourLAN 介绍，Lightweight network IP scanner. Can be used to notify about new hosts and monitor host online/offline history
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 aceberg/WatchYourLAN，该项目在 GitHub 有超过 2.6k Star。

![](https://stats.deeptrain.net/repo/aceberg/WatchYourLAN/?theme=light)

一句话介绍该项目：Lightweight network IP scanner. Can be used to notify about new hosts and monitor host online/offline history




![Screenshot_1](https://raw.githubusercontent.com/aceberg/WatchYourLAN/main/assets/Screenshot_1.png)

![Screenshot_5](https://raw.githubusercontent.com/aceberg/WatchYourLAN/main/assets/Screenshot_5.png)

![Screenshot_2](https://raw.githubusercontent.com/aceberg/WatchYourLAN/main/assets/Screenshot_2.png)

![Screenshot_3](https://raw.githubusercontent.com/aceberg/WatchYourLAN/main/assets/Screenshot_3.png)

![Screenshot_4](https://raw.githubusercontent.com/aceberg/WatchYourLAN/main/assets/Screenshot_4.png)

![](https://raw.githubusercontent.com/aceberg/WatchYourLAN/main/assets/logo.png)


###### 项目介绍

**WatchYourLAN：一个轻量级网络 IP 扫描器，助力网络管理与监控**

在数字化时代，网络安全和管理已成为企业和个人不可忽视的重要组成部分。由于网络设备的快速增加，实时监控网络状态、发现新接入设备以及维护网络设备清单变得复杂而繁琐。特别是在大型网络环境中，未授权设备的接入可能导致安全漏洞，而设备在线/离线状态的变化需要被即时捕捉以确保业务连续性。针对这些问题，一个轻量级且功能丰富的网络监控工具应运而生，它就是 **WatchYourLAN**。

**

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-fc17f65aa448232e193cf6123be17e84.png)

项目介绍：**

**WatchYourLAN** 是一个开源的轻量级网络 IP 扫描工具，它提供了一个便捷的 Web 图形用户界面（GUI），允许用户轻松管理和监控局域网内的网络设备。它的主要功能包含：
- 发现新接入的主机时发送通知
- 监控主机的在线/离线历史记录
- 维护网络中所有主机的列表
- 支持将数据发送到 `InfluxDB2` ，进而通过 `Grafana` 仪表板实现数据可视化

**WatchYourLAN** 主要设计要点是它的轻量级和易用性，同时支持复杂网络环境的扫描，包括 `VLAN`、`docker0` 等。从版本 `v2.0.1` 开始，该工具加入了对这些高级网络环境的支持。

**如何使用：**

安装 **WatchYourLAN** 非常简单，你可以通过 Docker 运行它。首先，确保你的系统已安装 Docker，然后通过以下命令启动 **WatchYourLAN** 容器，别忘了替换 `$YOURTIMEZONE`、`$YOURIFACE` 和 `$DOCKERDATAPATH` 为你自己的设置：

```sh
docker run --name wyl \
	-e "IFACES=$YOURIFACE" \
	-e "TZ=$YOURTIMEZONE" \
	--network="host" \
	-v $DOCKERDATAPATH/wyl:/data/WatchYourLAN \
    aceberg/watchyourlan:v2
```

之后，你可以通过访问 `http://localhost:8840` 来使用 Web 图形界面进行操作。

**项目推介：**

**WatchYourLAN** 目前处于活跃开发状态，它是由一群热心的开源贡献者维护的，确保了项目的持续更新和改进。通过使用 **WatchYourLAN**，网络管理员可以轻松管理和监控网络状态，及时发现和处理网络安全问题。它能够帮助个人用户或企业节省大量时间，提高网络管理的效率和准确性。

此外，**WatchYourLAN** 的作者和社区积极响应用户反馈和问题，使得该项目能够快速适应用户的需求，提供更好的体验。无论你是网络安全专家、IT 管理员还是对网络管理感兴趣的技术爱好者，**WatchYourLAN** 都是一个值得尝试和使用的优秀工具。

立即加入 **WatchYourLAN** 的用户社区，开始你的网络管理和监控之旅吧！

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=aceberg/WatchYourLAN&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/aceberg/WatchYourLAN 

开源项目作者：aceberg

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=aceberg/WatchYourLAN)

关注我们，一起探索有意思的开源项目。

