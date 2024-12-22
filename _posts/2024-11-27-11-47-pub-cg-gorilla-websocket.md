---
layout: post
title: 为 Go 开发的 WebSocket 库
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在现代的 Web 开发中，实时性是一个不可或缺的要求，无论是在线聊天应用、实时通知系统还是多人在线游戏，它们都需要一种能够快速、高效地进行客户端与服务器之间数据交换的技术。这就是 WebSocket 协议发挥作用的地方。但是，在具体的实现过程中，开发者往往会面临诸多挑战，例如如何处理各种不同的网络环境、如何确保数据传输的安全性以及如何提高传输效率等。很多时候，这些挑战会极大地增加开发的复杂度和时间成本。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-f9b5c0ecd0bb9a02425fe9a8118527ee.png)

今天要给大家推荐一个 GitHub 开源项目 websocket，该项目在 GitHub 有超过 22.7k Star。

![](https://stats.deeptrain.net/repo/gorilla/websocket/?theme=light)

一句话介绍该项目：Package gorilla/websocket is a fast, well-tested and widely used WebSocket implementation for Go.

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241201213934843.png)

###### 项目介绍

`Gorilla WebSocket` 是一个为 Go 语言开发的 WebSocket 的实现库，它旨在提供一个快速、经过严格测试且广为使用的 WebSocket 实现。该项目遵循 WebSocket 协议（RFC 6455）的响应式编程要求，为 Go 开发者提供了一个稳定、高效的 WebSocket 通信解决方案。它不仅包含了完整的协议实现，还通过提供丰富的示例代码，使得开发者能够快速掌握如何使用该库来构建实时应用。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241201214017465.png)

###### 如何使用

安装只需要运行下面的命令：

```
go get github.com/gorilla/websocket
```

以下是一个简单的使用示例，展示了如何创建一个 WebSocket 服务器和客户端：

服务器端示例如下：

```go
package main

import (
    "net/http"
    "github.com/gorilla/websocket"
)

var upgrader = websocket.Upgrader{
    ReadBufferSize:  1024,
    WriteBufferSize: 1024,
}

func handler(w http.ResponseWriter, r *http.Request) {
    conn, _ := upgrader.Upgrade(w, r, nil) // error ignored for simplicity
    defer conn.Close()
    for {
        messageType, p, _ := conn.ReadMessage() // error ignored for simplicity
        if err := conn.WriteMessage(messageType, p); err != nil {
            return
        }
    }
}

func main() {
    http.HandleFunc("/echo", handler)
    http.ListenAndServe(":8080", nil)
}
```

客户端示例如下：

```go
package main

import (
    "github.com/gorilla/websocket"
    "log"
    "net/url"
)

func main() {
    u := url.URL{Scheme: "ws", Host: "localhost:8080", Path: "/echo"}
    c, _, err := websocket.DefaultDialer.Dial(u.String(), nil)
    if err != nil {
        log.Fatal("dial:", err)
    }
    defer c.Close()

    err = c.WriteMessage(websocket.TextMessage, []byte("hello"))
    if err != nil {
        log.Println("write:", err)
        return
    }
    _, message, err := c.ReadMessage()
    if err != nil {
        log.Println("read:", err)
        return
    }
    log.Printf("received: %s", message)
}
```

###### 项目推介

`Gorilla WebSocket` 已经通过了 [Autobahn Test Suite](https://github.com/crossbario/autobahn-testsuite) 的服务器测试，这证明了其协议实现的完整性和稳定性。此外，它还提供了丰富的示例代码，帮助开发者快速掌握如何进行 WebSocket 开发。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241201214235682.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=gorilla/websocket&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/gorilla/websocket 

开源项目作者：gorilla

开源协议：BSD 2-Clause "Simplified" License

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=gorilla/websocket)

关注我们，一起探索有意思的开源项目。

