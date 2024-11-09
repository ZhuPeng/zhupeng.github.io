---
layout: post
title: 为微控制器打造的 Go 编译器
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

随着物联网 (IoT) 和边缘计算的发展，越来越多的微型设备需要运行高效能、低功耗的应用程序。传统的编程语言编译器往往不适合这些资源受限的环境，因为它们生成的二进制文件过大，运行时占用的内存过多。此外，想要在浏览器端运行高效的应用程序，同时保持快速响应和低资源消耗，对传统的 WebAssembly 编译器也是一大挑战。这就需要一种新的编程语言编译器来解决这些痛点。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-208f8e946e5971c4a1cafc843f8f1303.png)

今天要给大家推荐一个 GitHub 开源项目 tinygo，该项目在 GitHub 有超过 15.4k Star。

![](https://stats.deeptrain.net/repo/tinygo-org/tinygo/?theme=light)

一句话介绍该项目：Go compiler for small places. Microcontrollers, WebAssembly (WASM/WASI), and command-line tools. Based on LLVM.

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240913211643969.png)

###### 项目介绍

TinyGo 是一个专为小型设备如微控制器、WebAssembly (wasm/wasi) 和命令行工具设计的 Go 语言编译器。它基于 LLVM，能够提供与 Go 语标准工具链不同的编译方式。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240913211814124.png)

TinyGo 的目标是生成非常小的二进制文件，只包括程序实际使用到的部分，极大地减小了资源占用。TinyGo 支持绝大多数 Go 语言标准库，可以编译大多数不做改动的 Go 代码。此外，TinyGo 特别适合嵌入式开发和 WebAssembly 应用，支持超过 94 种不同的微控制器板，并且提供对 WASM 和 WASI 的优秀支持。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240913212022723.png)

###### 如何使用

可以访问TinyGo 官方开始指南 [QuickStart](https://tinygo.org/getting-started/) 完成安装。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240913211935232.png)

安装成功后，可以使用下面的代码编译和运行一个在内置 LED 上闪烁的示例程序，该程序适用于任何带有内置 LED 的支持板：

```go
package main

import (
    "machine"
    "time"
)

func main() {
    led := machine.LED
    led.Configure(machine.PinConfig{Mode: machine.PinOutput})
    for {
        led.Low()
        time.Sleep(time.Millisecond * 1000)

        led.High()
        time.Sleep(time.Millisecond * 1000)
    }
}
```
通过以下命令编译并闪写到 Arduino Uno：
```shell
tinygo flash -target arduino examples/blinky1
```
对于 WebAssembly 应用，也可以轻松编译：
```shell
tinygo build -o main.wasm -target=wasip1 main.go
```

###### 项目推介

TinyGo 活跃的开发社区、持续增长的支持硬件列表以及与 LLVM 的紧密集成保证了其前景和稳定性。TinyGo 已被 Fastly Compute、Fermyon Spin、wazero 等知名 WebAssembly 运行时采用，展现了其在现代 Web 应用程序中的实际价值。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240913212128159.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=tinygo-org/tinygo&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/tinygo-org/tinygo 

开源项目作者：tinygo-org

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=tinygo-org/tinygo)

关注我们，一起探索有意思的开源项目。

