---
layout: post
title: 更易于 Go 集成的反向代理工具
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 ngrok/ngrok-go，该项目在 GitHub 有超过 300 Star，用一句话介绍该项目就是：“The ngrok agent in library form, suitable for integrating directly into your Go application.”，方便使用 Go 集成的 ngrok 库。


ngrok-go 是用 Go 语言编写的 ngrok 的实现。ngrok 是一个反向代理工具，它可以将本地运行的服务暴露到公网上，并为其生成一个可以访问的公网 URL。这样就可以在本地开发环境中进行远程调试和测试。ngrok-go 是一个轻量级工具，它可以在命令行中简单配置和使用，支持 http, https, tcp, tls 等协议，可以在项目地址 https://github.com/inconshreveable/ngrok 上进行下载和查看源代码。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=ngrok/ngrok-go&type=Timeline)

### 如何安装使用

ngrok-go 项目可以通过多种方式安装，下面是几种常见的方法：

1. 通过 go get 安装:
```
go get -u github.com/inconshreveable/ngrok
```

2. 下载二进制文件安装:
   你可以在 https://github.com/inconshreveable/ngrok/releases 这里下载最新版本的二进制文件，并将其放到你的 PATH 中。

3. 通过包管理器安装:
   在 Debian / Ubuntu 上，可以使用 apt 安装：
```
sudo apt-get install ngrok-client
```
   在 Fedora / CentOS 上，可以使用 yum 安装:
```
sudo yum install ngrok
```

在安装完成后，可以使用 `ngrok` 命令来启动和配置 ngrok-go。 使用 `ngrok --help` 查看更多命令行选项。

请注意，在使用 ngrok 之前，你需要到 ngrok 官网 (https://ngrok.com/) 注册并获取一个 authtoken.

在使用ngrok之前可以先配置一下配置文件，也可以在运行命令的时候进行配置，可以参考官网文档来了解更多。


### 使用示例 DEMO

以下是一个简单的 ngrok-go 示例代码，它将本地的 3000 端口暴露到公网上：
```go
package main

import (
    "fmt"
    "log"
    "net/http"

    "github.com/inconshreveable/ngrok"
)

func main() {
    // Start a local web server
    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprint(w, "Hello, World!")
    })
    go http.ListenAndServe(":3000", nil)

    // Connect ngrok to the local web server
    ngrokUrl, err := ngrok.Start("http", "3000")
    if err != nil {
        log.Fatal(err)
    }

    // Print the public ngrok URL
    fmt.Println(ngrokUrl)
}
```
在运行上面的代码之前，需要在你的系统上安装 ngrok-go 并获取一个 authtoken。

运行上面的程序后，将会在终端输出一个 ngrok 提供的 URL。 你可以将这个 URL 分享给其他人，让他们访问你本地运行的服务。


更多项目详情请查看如下链接。

开源项目地址：https://github.com/ngrok/ngrok-go 

开源项目作者：ngrok

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=ngrok/ngrok-go)

