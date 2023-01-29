---
layout: post
title: GitHub 开源项目 mingcheng/socks5lb 介绍，A simple socks5 proxy load balance and transparent proxy
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 mingcheng/socks5lb，该项目在 GitHub 有超过 0.4k Star，用一句话介绍该项目就是：“A simple socks5 proxy load balance and transparent proxy”。

![socks5lb](https://raw.githubusercontent.com/mingcheng/socks5lb/master/./asserts/socks5lb.png)

socks5lb 是一个 SOCKS5 代理负载均衡器，可以将多个 SOCKS5 代理服务器组合在一起，提供一个单一的入口点，并且能够自动分配请求到各个代理服务器上。这样可以增加代理服务器的可用性和稳定性。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=mingcheng/socks5lb&type=Timeline)

### 如何安装使用

mingcheng/socks5lb 可以通过以下步骤安装:

1. 下载项目源代码: 通过命令行工具，在你希望安装的目录中运行 `git clone https://github.com/mingcheng/socks5lb.git`

2. 进入项目文件夹: 运行 `cd socks5lb`

3. 安装依赖: 运行 `npm install` 或 `yarn install`

4. 启动项目: 运行 `npm start` 或 `yarn start`

项目会在本地启动一个 SOCKS5 代理服务器，默认监听本地 1080 端口。

请注意，在运行此项目之前，你需要安装 Node.js 和 npm 或 yarn。


### 使用示例 DEMO

编辑配置文件: `vi config/default.json`, 编辑代理服务器列表, 比如

```
{
  "proxies": [
    {
      "host": "127.0.0.1",
      "port": "1081"
    },
    {
      "host": "127.0.0.1",
      "port": "1082"
    }
  ]
}
```

启动项目: 运行 `npm start` 或 `yarn start`

这样就可以在本地启动 SOCKS5 代理服务器了, 默认监听本地 1080 端口。

如果你想使用其他端口，可以通过在启动命令中添加 `--port` 参数来指定, 比如: `npm start -- --port 1081`

然后你可以在你的程序中设置代理为 `127.0.0.1:1080`, 就能愉快的爬虫啦~

注意: 请确保你本地网络环境可以访问你配置的所有代理服务器。


更多项目详情请查看如下链接。

开源项目地址：https://github.com/mingcheng/socks5lb 

开源项目作者：mingcheng

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=mingcheng/socks5lb)

