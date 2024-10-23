---
layout: post
title: Gin Web 框架默认的数据结构验证器
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在现代软件开发的实践中，确保数据的有效性和合法性是一个重要且常见的挑战。无论是处理来自用户输入的数据还是通过网络传输的数据，验证数据的准确性对于系统的安全性、稳定性与功能的正确实现至关重要。然而，数据验证的过程往往繁琐且易出错，特别是当牵涉到复杂的规则、跨字段的关系，或者需要对嵌套的数据结构进行深入验证时。没有一个有效、灵活且易于使用的验证工具，开发者可能需要编写大量的重复代码，不仅增加了开发的工作量，而且也增加了出错的风险。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-cba34cf9734902a2dae90c76bacccb48.png)

今天要给大家推荐一个 GitHub 开源项目 go validator，该项目在 GitHub 有超过 16.4k Star。

![](https://stats.deeptrain.net/repo/go-playground/validator/?theme=light)

一句话介绍该项目：Go Struct and Field validation, including Cross Field, Cross Struct, Map, Slice and Array diving


![](https://raw.githubusercontent.com/go-playground/validator/master/logo.png)


###### 项目介绍

validator 库一款用于 Go 语言的结构体和字段验证库，通过基于标签或自定义验证器实现交叉字段和交叉结构体验证、支持对切片、数组和映射的深入验证，以及映射键和值的验证等独特功能。它还支持处理类型接口、自定义字段类型，如 SQL 驱动的 `Valuer`，并支持别名验证标签、自定义字段名称提取，以及支持 i18n 的错误消息定制。该库也是 Gin Web框架的默认验证器。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241008230206380.png)

###### 如何使用

首先，使用 `go get` 命令安装 `validator`：

```bash
go get github.com/go-playground/validator/v10
```

然后，在你的代码中导入 `validator` ：

```go
import "github.com/go-playground/validator/v10"
```

使用 `validator` 进行数据验证的示例代码如下：

```go
package main

import (
    "fmt"
    "github.com/go-playground/validator/v10"
)

type User struct {
    Username string `validate:"required"`
    Age      int    `validate:"gte=0,lte=130"`
    Email    string `validate:"required,email"`
}

func main() {
    validate := validator.New()
    user := &User{
        Username: "John",
        Age:      35,
        Email:    "john@example.com",
    }

    err := validate.Struct(user)
    if err != nil {
        if validationErrors, ok := err.(validator.ValidationErrors); ok {
            fmt.Println(validationErrors)
        }
    } else {
        fmt.Println("Validation passed")
    }
}
```

###### 项目推介

`validator` 库是 Go 语言开发社区广泛认可和使用的项目，它不仅因为其强大的功能和灵活性受到推崇，也因为其活跃的开发和维护状态而备受信赖。除此之外，它还拥有一系列清晰的文档和使用示例，帮助开发者快速上手和解决问题。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=go-playground/validator&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/go-playground/validator 

开源项目作者：go-playground

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=go-playground/validator)

关注我们，一起探索有意思的开源项目。

