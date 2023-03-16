---
layout: post
title: 使用 Golang 开发的事件驱动的微服务示例
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 thangchung/go-coffeeshop，该项目在 GitHub 有超过 3.1k Star，用一句话介绍该项目就是：“☕ A practical event-driven microservices demo built with Golang.”，使用 Golang 开发的事件驱动的微服务示例。

![](https://github.com/thangchung/go-coffeeshop/raw/main/docs/home_screen.png)

go-coffeeshop 是一个用 Go 语言编写的开源项目，它模拟了一个咖啡店的在线订单系统。它使用了 Go 的标准库以及第三方库，如 Gin 框架，GORM 数据库框架和 Redis 缓存数据库。 这个项目提供了一个简单的咖啡店订单系统的模型，演示了如何使用 Go 语言和相关框架来构建 Web 应用程序。它提供了一个可用的 RESTful API，用于订单的创建，查询，更新和删除。可以作为 Go 的入门级项目，也可以作为使用 Go 构建 Web 应用程序的参考。

![](https://github.com/thangchung/go-coffeeshop/raw/main/docs/coffeeshop.svg)

### 如何安装使用

因为 go-coffeeshop 包含多个服务，要一步一步运行起来还是比较困难的，所以 go-coffeeshop 使用 docker compose 进行管理，只需要在仓库目录运行 make docker-compose 即可启动如下服务。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230305191904315.png)


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


更多项目详情请查看如下链接。

开源项目地址：https://github.com/thangchung/go-coffeeshop 

开源项目作者：thangchung

