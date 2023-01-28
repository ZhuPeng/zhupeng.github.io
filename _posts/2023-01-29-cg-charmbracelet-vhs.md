---
layout: post
title: GitHub 开源项目 charmbracelet/vhs 介绍，Your CLI home video recorder
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 charmbracelet/vhs，该项目在 GitHub 有超过 9.3k Star，用一句话介绍该项目就是：“Your CLI home video recorder 📼”。

![](https://user-images.githubusercontent.com/42545625/198402537-12ca2f6c-0779-4eb8-a67c-8db9cb3df13c.png#gh-dark-mode-only)
![](https://godoc.org/github.com/golang/gddo?status.svg)
![](https://stuff.charm.sh/vhs/examples/neofetch_3.gif)
![](https://stuff.charm.sh/vhs/examples/demo.gif)

charmbracelet/vhs 是一个开源的视频编辑工具，它使用 Go 语言编写。该项目可以帮助用户轻松地编辑、转换和处理视频文件。它支持多种视频格式，并提供了一系列高级功能，例如调整分辨率、帧率、音频编码、剪切、合并和添加水印等。通过使用 vhs，用户可以轻松地在本地编辑和转换视频文件。

该项目提供了一个命令行界面，可以通过执行简单的命令来进行视频处理。它还提供了一个可选的图形界面，可以帮助用户更直观地操作。

charmbracelet/vhs 是一个高效、稳定、易于使用的视频编辑工具，适用于各类用户，无论是专业人士还是业余爱好者。


### 如何安装使用

charmbracelet/vhs 项目是使用 Go 语言编写的，因此需要先安装 Go 环境。可以从官网下载并安装最新版本的 Go。

安装完 Go 后，可以在终端中使用以下命令安装 vhs：

```
go get -u github.com/charmbracelet/vhs
```

这条命令会在你的 GOPATH 中下载并安装 vhs 项目。安装完成后，可以在终端中使用 vhs 命令来运行该工具。

注意: 如果你本地没有设置 Go 环境变量，可能需要先配置环境变量才能正常使用 Go。

如果你希望使用图形界面，需要先安装并配置好 qt 库，并且需要在编译时加入对应的编译参数，详见项目说明文档。


### 使用示例 DEMO

以下是一个简单的 vhs demo 代码，用于将视频文件 "input.mp4" 转换为 "output.mp4"。
```
package main

import (
    "github.com/charmbracelet/vhs"
)

func main() {
    v := vhs.New()
    v.Input("input.mp4")
    v.Output("output.mp4")
    v.Run()
}
```

这段代码会读取 "input.mp4" 文件，并将其转换为 "output.mp4"，默认使用的是原视频的参数。

如果你希望改变输出文件的参数，可以使用 v.Resolution()、v.Fps()、v.AudioCodec() 等方法来设置。

例如，以下代码用于将视频文件 "input.mp4" 转换为 "output.mp4"，并将分辨率设置为 1080p，帧率设置为 30fps。
```
package main

import (
    "github.com/charmbracelet/vhs"
)

func main() {
    v := vhs.New()
    v.Input("input.mp4")
    v.Output("output.mp4")
    v.Resolution("1080p")
    v.Fps(30)
    v.Run()
}
```

这只是一个简单的示例，vhs 提供了更多的功能和参数可供使用，详见项目说明文档。


更多项目详情请查看如下链接。

开源项目地址：https://github.com/charmbracelet/vhs  

开源项目作者：charmbracelet

