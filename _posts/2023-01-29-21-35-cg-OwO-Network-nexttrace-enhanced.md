---
layout: post
title: GitHub 开源项目 OwO-Network/nexttrace-enhanced 介绍，An open source visual route tracking CLI tool (Enhanced Edition)
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 OwO-Network/nexttrace-enhanced，该项目在 GitHub 有超过 0.4k Star，用一句话介绍该项目就是：“An open source visual route tracking CLI tool (Enhanced Edition)”。

![](https://raw.githubusercontent.com/OwO-Network/nexttrace-enhanced/master/asset/logo.png)

![image](https://user-images.githubusercontent.com/13616352/186600128-5985e713-502b-4382-b6cf-cc279904e31b.png)
![NextTrace Web Screenshot](https://raw.githubusercontent.com/OwO-Network/nexttrace-enhanced/master/asset/screenshot-web.png)
![NextTrace traceMap Screenshot](https://raw.githubusercontent.com/OwO-Network/nexttrace-enhanced/master/asset/screenshot-traceMap.png)

OwO-Network/nexttrace-enhanced 是一个基于 nexttrace 的增强版本。nexttrace 是一个用于跟踪 Linux 系统调用的工具。增强版本添加了更多功能，如自定义规则和更好的可读性输出。该项目基于 Golang 开发，可以在 Linux 和 macOS 上运行。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=OwO-Network/nexttrace-enhanced&type=Timeline)

安装方式:

1. 首先需要安装 Go 环境, 可以参考官网 https://golang.org/doc/install
2. 通过 go get 命令安装: 

```
go get -u github.com/OwO-Network/nexttrace-enhanced
```

3. 运行命令:

```
nexttrace-enhanced
```

示例代码:

```
package main

import (
    "github.com/OwO-Network/nexttrace-enhanced"
)

func main() {
    nexttrace.Trace()
}
```

可以通过运行该程序并在终端进行操作来查看系统调用详情.


更多项目详情请查看如下链接。

开源项目地址：https://github.com/OwO-Network/nexttrace-enhanced 

开源项目作者：OwO-Network

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=OwO-Network/nexttrace-enhanced)

