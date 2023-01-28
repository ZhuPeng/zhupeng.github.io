---
layout: post
title: GitHub 开源项目 thangchung/go-coffeeshop 介绍，☕ A practical event-driven microservices demo built with Golang. Nomad, Consul Connect, Vault, and Terraform for deployment
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 thangchung/go-coffeeshop，该项目在 GitHub 有超过 3.1k Star，用一句话介绍该项目就是：“☕ A practical event-driven microservices demo built with Golang. Nomad, Consul Connect, Vault, and Terraform for deployment”。

go-coffeeshop 是一个用 Go 语言编写的开源项目，它模拟了一个咖啡店的在线订单系统。它使用了 Go 的标准库以及第三方库，如 Gin 框架，GORM 数据库框架和 Redis 缓存数据库。 这个项目提供了一个简单的咖啡店订单系统的模型，演示了如何使用 Go 语言和相关框架来构建 Web 应用程序。它提供了一个可用的 RESTful API，用于订单的创建，查询，更新和删除。可以作为 Go 的入门级项目，也可以作为使用 Go 构建 Web 应用程序的参考。

### 如何安装使用

安装 go-coffeeshop 项目需要先安装 Go 语言环境和相关的依赖。

1. 安装 Go 语言：请参考 https://golang.org/doc/install 以获取最新的安装指南。

2. 克隆项目到本地：在终端中运行 `git clone https://github.com/thangchung/go-coffeeshop.git` 命令。

3. 安装依赖：进入项目目录，运行 `go mod download` 命令来安装依赖。

4. 启动项目：运行 `go run main.go` 命令来启动项目。

5. 访问项目：在浏览器中输入 http://localhost:8080 即可访问项目。

注意：在启动项目之前,需要本地有redis,并且需要更改配置文件config.toml的redis的地址和端口。


### 使用示例 DEMO

以下是使用 go-coffeeshop 项目的示例代码，可以用来创建一个新的订单：
```go
package main

import (
    "fmt"
    "net/http"
    "bytes"
    "io/ioutil"
    "encoding/json"
)

func main() {
    url := "http://localhost:8080/api/v1/orders"
    fmt.Println("URL:>", url)

    var jsonStr = []byte(`{"coffee_name":"Espresso","size":"small","milk_type":"whole","quantity":1}`)
    req, err := http.NewRequest("POST", url, bytes.NewBuffer(jsonStr))
    req.Header.Set("Content-Type", "application/json")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        panic(err)
    }
    defer resp.Body.Close()

    fmt.Println("response Status:", resp.Status)
    fmt.Println("response Headers:", resp.Header)
    body, _ := ioutil.ReadAll(resp.Body)
    fmt.Println("response Body:", string(body))

    var result map[string]interface{}
    json.Unmarshal([]byte(body), &result)
    fmt.Println("Order ID: ", result["id"])
}
```

这段代码使用了 Go 语言的 net/http 库发送了一个 HTTP POST 请求来创建一个新的订单。其中，jsonStr 变量包含了请求体，表示要创建的新订单的详细信息。最后的输出结果中包含了新创建的订单的 ID。

注意:该代码需要更改服务器地址为自己本地运行的地址。


更多项目详情请查看如下链接。

开源项目地址：https://github.com/thangchung/go-coffeeshop 

开源项目作者：thangchung

