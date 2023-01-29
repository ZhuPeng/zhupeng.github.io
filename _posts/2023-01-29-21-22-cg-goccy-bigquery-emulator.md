---
layout: post
title: GitHub 开源项目 goccy/bigquery-emulator 介绍，BigQuery emulator server implemented in Go
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 goccy/bigquery-emulator，该项目在 GitHub 有超过 0.3k Star，用一句话介绍该项目就是：“BigQuery emulator server implemented in Go”。

![](https://user-images.githubusercontent.com/209884/196145011-e35c2df4-5f5d-43ce-b7df-08cd130b5d31.png)
![](https://user-images.githubusercontent.com/209884/196145033-aa032878-7e01-4ec7-9a23-b174b87e1a24.png)

goccy/bigquery-emulator 是一个用于模拟 Google BigQuery 的开源项目。它可以在本地运行 BigQuery 语句，无需连接到云端服务。这对于开发和测试来说非常方便，可以减少费用和网络延迟。该项目基于 Go 语言开发，可以轻松安装和使用。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=goccy/bigquery-emulator&type=Timeline)

### 如何安装使用

goccy/bigquery-emulator 项目通过使用 Go 语言编写，因此可以通过以下步骤安装：
1. 确保已安装 Go 环境
2. 使用 go get 命令安装项目：`go get -u github.com/goccy/bigquery-emulator`
3. 在工程中导入项目包：`import "github.com/goccy/bigquery-emulator"`
4. 使用 go build 命令编译工程
5. 运行生成的可执行文件即可使用该项目。


### 使用示例 DEMO

下面是一份 demo 代码，它将启动 bigquery-emulator 并在本地端口 9090 上进行监听，并使用默认配置创建一个名为 "myproject" 的项目：

```
package main

import (
    "context"
    "log"

    "github.com/goccy/bigquery-emulator/bigquery"
)

func main() {
    // 创建一个默认配置的 bigquery-emulator
    emu, err := bigquery.NewEmulator(bigquery.WithAddr(":9090"), bigquery.WithProjectID("myproject"))
    if err != nil {
        log.Fatal(err)
    }
    defer emu.Close()

    // 启动 bigquery-emulator
    if err := emu.Run(context.Background()); err != nil {
        log.Fatal(err)
    }
}
```

使用 bigquery 客户端连接到 bigquery-emulator 时，请将 bigquery.ClientOption.Endpoint 设置为 "http://localhost:9090"。


更多项目详情请查看如下链接。

开源项目地址：https://github.com/goccy/bigquery-emulator 

开源项目作者：goccy

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=goccy/bigquery-emulator)

