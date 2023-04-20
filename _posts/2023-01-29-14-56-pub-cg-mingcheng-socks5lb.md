---
layout: post
title: 一款简单的 Socks5 负载均衡代理工具
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 mingcheng/socks5lb，该项目在 GitHub 有超过 400 Star，用一句话介绍该项目就是：“A simple socks5 proxy load balance and transparent proxy”，一款简单的 Socks5 负载均衡代理工具。

![](https://raw.githubusercontent.com/mingcheng/socks5lb/master/asserts/socks5lb.png)

socks5lb 是一个 SOCKS5 代理负载均衡器，可以将多个 SOCKS5 代理服务器组合在一起，提供一个单一的入口点，并且能够自动分配请求到各个代理服务器上。有时候我们在使用 Socks5 无法联通的情况，这有可能是因为网络或者线路的调整和波动，这时候往往需要我们自己手工切换节点，非常的麻烦。而借助 socks5lb 增加多个负载节点，可以增加代理服务器的可用性和稳定性。

以下是项目实现的特性及更新记录：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230409205742478.png)


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=mingcheng/socks5lb&type=Timeline)

### 如何安装使用

该项目建议使用 docker-compose 编译生成镜像文件，直接执行 docker-compose build 即可运行使用。


### 使用示例 DEMO

要使用 socks5lb 首先要做基本的配置，例如以下配置了三个 Socks5 Proxy 同时暴露到本地的 1080 端口，针对 Linux 的透明代理暴露在 8848 端口。

```yaml
server:
  http:
    addr: ":8080"
  socks5:
    addr: ":1080"
  tproxy:
    addr: ":8848"
backends:
  - addr: 192.168.100.254:1086
    check_config:
      check_url: https://www.google.com/robots.txt
      initial_alive: true
      timeout: 3
  - addr: 10.1.0.254:1086
    check_config:
      check_url: https://www.google.com/robots.txt
      initial_alive: false
      timeout: 30
  - addr: 172.16.100.254:1086
    check_config:
      check_url: https://www.google.com/robots.txt
      initial_alive: true
      timeout: 3
```

通过如下 docker-compose 配置即可进行启动：

```yaml
version: "3"
services:
  socks5lb:
    image: ghcr.io/mingcheng/socks5lb:latest
    restart: always
    dns:
      - 8.8.8.8
      - 8.8.4.4
    environment:
      TZ: "Asia/Shanghai"
      CHECK_TIME_INTERVAL: 3600
    network_mode: "host"
    privileged: true
    volumes:
      - ./socks5lb.yml:/etc/socks5lb.yml:ro
```

启动后有 Web 管理界面对代理服务节点进行管理。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230409210209060.png)


更多项目详情请查看如下链接。

开源项目地址：https://github.com/mingcheng/socks5lb 

开源项目作者：mingcheng

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=mingcheng/socks5lb)



关注我们，一起探索有意思的开源项目。
