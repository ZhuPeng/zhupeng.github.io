---
layout: post
title: 一款开源可视化的路由追踪工具
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 sjlleo/nexttrace，该项目在 GitHub 有超过 700 Star，用一句话介绍该项目就是：“An open source visual route tracking CLI tool”，一款开源可视化的路由追踪工具。

![](https://raw.githubusercontent.com/sjlleo/nexttrace/master/asset/logo.png)

![](https://user-images.githubusercontent.com/13616352/208289553-7f633f9c-7356-40d1-bbc4-cc2687419cca.png)
![](https://user-images.githubusercontent.com/13616352/208289568-2a135c2d-ae4a-4a3e-8a43-f5a9a87ade4a.png)

nexttrace 是一个用 Go 语言编写的高性能、轻量化的分布式追踪系统。它是一个命令行工具，在命令行使用可以展示清晰的 TraceRoute 路由信息，同时支持根据地图进行可视化的展示，看完一目了然。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=sjlleo/nexttrace&type=Timeline)

### 如何安装使用

使用如下方式即可安装 nexttrace 工具：

```bash
# Linux 一键安装脚本
bash <(curl -Ls https://raw.githubusercontent.com/sjlleo/nexttrace/main/nt_install.sh)

# GHPROXY 镜像（国内使用）
bash <(curl -Ls https://ghproxy.com/https://raw.githubusercontent.com/sjlleo/nexttrace/main/nt_install.sh)

# macOS brew 安装命令
brew tap xgadget-lab/nexttrace && brew install nexttrace
```


### 使用示例 DEMO

nexttrace 默认使用 ICMP 协议发起 TraceRoute 请求，该协议同时支持 IPv4 和 IPv6，以下是基本的用法：

```bash
# IPv4 ICMP Trace
nexttrace 1.0.0.1
# URL
nexttrace http://example.com:8080/index.html?q=1

# 表格打印，使用 --table / -t 参数，将实时显示结果
nexttrace --table 1.0.0.1

# IPv6 ICMP Trace
nexttrace 2606:4700:4700::1111

# 禁用路径可视化 使用 --map / -M 参数
nexttrace koreacentral.blob.core.windows.net
# MapTrace URL: https://api.leo.moe/tracemap/html/c14e439e-3250-5310-8965-42a1e3545266.html
```

除以上以外，nexttrace 还支持如下功能：

1、支持快速测试，有一次性测试回程路由需求的朋友可以使用

```bash
# 北上广（电信+联通+移动+教育网）IPv4 / IPv6 ICMP 快速测试
nexttrace --fast-trace

# 也可以使用 TCP SYN 而非 ICMP 进行测试
nexttrace --fast-trace --tcp
```

2、支持指定网卡进行路由跟踪

```bash
# 请注意 Lite 版本此参数不能和快速测试联用，如有需要请使用 enhanced 版本
# 使用 eth0 网卡
nexttrace --dev eth0 2606:4700:4700::1111

# 使用 eth0 网卡IP
# 网卡 IP 可以使用 ip a 或者 ifconfig 获取
# 使用网卡IP进行路由跟踪时需要注意跟踪的IP类型应该和网卡IP类型一致（如都为 IPv4）
nexttrace --source 204.98.134.56 9.9.9.9
```

3、支持使用`TCP`和`UDP`协议发起`Traceroute`请求，不过目前`UDP`只支持`IPv4`

```bash
# TCP SYN Trace
nexttrace --tcp www.bing.com

# 可以自行指定端口[此处为443]，默认80端口
nexttrace --tcp --port 443 2001:4860:4860::8888

# UDP Trace
nexttrace --udp 1.0.0.1

# 可以自行指定端口[此处为5353]，默认53端口
nexttrace --udp --port 5353 1.0.0.1
```

另外也同样支持一些进阶功能，如 TTL 控制、并发数控制、模式切换等。

更多项目详情请查看如下链接。

开源项目地址：https://github.com/sjlleo/nexttrace 

开源项目作者：sjlleo

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=sjlleo/nexttrace)



关注我们，一起探索有意思的开源项目。
