---
layout: post
title: GitHub 开源项目 ja9er/Gofreeproxy 介绍，自用的动态代理小工具
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 ja9er/Gofreeproxy，该项目在 GitHub 有超过 0.3k Star，用一句话介绍该项目就是：“自用的动态代理小工具”。


Gofreeproxy 是一个由 Go 语言编写的免费代理池项目，支持 HTTP 和 HTTPS 代理。它可以通过爬取公开代理网站获取代理，并对获取到的代理进行验证和去重，保证代理的可用性。该项目还提供了一个简单的 API 接口，方便其他程序调用。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=ja9er/Gofreeproxy&type=Timeline)

### 如何安装使用

该项目的安装方式可能需要按照该项目的说明文档进行操作，通常需要先安装 Go 环境，再使用 go get 命令将项目源码下载到本地，最后使用 go build 命令编译并生成可执行文件。

具体命令如下:

```
go get -u github.com/ja9er/Gofreeproxy
go build -o gofreeproxy main.go
```

然后执行生成的可执行文件即可。


### 使用示例 DEMO

项目 Gofreeproxy 是一个免费代理池，它提供了一个简单的 API，可以随机获取可用代理。它基于 Go 语言编写，可以在 Linux 和 Windows 上运行。

示例代码：
```
package main

import (
    "fmt"
    "github.com/ja9er/Gofreeproxy"
)

func main() {
    proxy, err := Gofreeproxy.Get()
    if err != nil {
        fmt.Println(err)
    } else {
        fmt.Println(proxy)
    }
}
```
在这个示例代码中，我们调用了 Gofreeproxy 库的 Get() 函数来随机获取一个可用代理。运行这段代码后，它会输出一个可用代理的地址。


更多项目详情请查看如下链接。

开源项目地址：https://github.com/ja9er/Gofreeproxy 

开源项目作者：ja9er

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=ja9er/Gofreeproxy)

