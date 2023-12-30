---
layout: post
title: Oapi-codegen - 适配 OpenAPI 3.0 的 Go 语言模板代码生成器 
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在日常的开发工作中，我们通常会使用 OpenAPI 3.0 进行 API 的设计和开发。OpenAPI 3.0 是一种用于定义 API 的详细描述的规范，被广泛用于各式各样的现代 web 服务。然而，当我们要与服务端进行交互的时候，尤其是在编写 Go 语言的服务端和客户端时，我们通常需要编写大量的模板代码以确保我们的 Go 语言模型精确地对应于 OpenAPI 规范。这无疑是一件非常繁琐和消耗时间的工作。

今天要给大家推荐一个 GitHub 开源项目 deepmap/oapi-codegen，该项目在 GitHub 有超过 4.4k Star，用一句话介绍该项目就是：“Generate Go client and server boilerplate from OpenAPI 3 specifications”。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231203180248975.png)

###### 项目介绍

Oapi-codegen 是一个 Go 语言模板代码生成器，其主要功能是根据 OpenAPI 3.0 API 定义生成 Go 语言的模板代码，缩减了我们编写 Go 模型的工作量。

设计上，Oapi-codegen 默认使用 Echo 作为其 HTTP 路由引擎，但同时也支持 Chi、Gin、gorilla/mux、Fiber、Iris 等其他路由引擎。这个开源项目试图保持简洁而非过于通用，因为我们无法为所有可能的 OpenAPI 方案生成强类型的 Go 代码，如果可以通过实用程序代码或反射来实现某件事，那么这可能是优于代码生成的更好的方式。

类型定义：

```yaml
NewPet:
  required:
    - name
  properties:
    name:
      type: string
    tag:
      type: string
  additionalProperties:
    type: string
```

以下对应生成的 Server 的示例代码：

```go
// NewPet defines model for NewPet.
type NewPet struct {
	Name                 string            `json:"name"`
	Tag                  *string           `json:"tag,omitempty"`
	AdditionalProperties map[string]string `json:"-"`
}

// Getter for additional properties for NewPet. Returns the specified
// element and whether it was found
func (a NewPet) Get(fieldName string) (value string, found bool) {...}

// Setter for additional properties for NewPet
func (a *NewPet) Set(fieldName string, value string) {...}

// Override default JSON handling for NewPet to handle additionalProperties
func (a *NewPet) UnmarshalJSON(b []byte) error {...}

// Override default JSON handling for NewPet to handle additionalProperties
func (a NewPet) MarshalJSON() ([]byte, error) {...}w
```

###### 如何使用

使用 Oapi-codegen 非常简单，在你的控制台上运行以下命令即可：

```
go install github.com/deepmap/oapi-codegen/v2/cmd/oapi-codegen@latest
oapi-codegen -package petstore petstore-expanded.yaml > petstore.gen.go
```
以上代码将会根据 petstore-expanded.yaml 文件生成一个名为 petstore.gen.go 的 Go 语言文件。

###### 项目推荐

Oapi-codegen 对于那些希望快速部署服务，同时减少模板代码编写工作量的用户来说，是一个非常不错的选择，也许会为你节省大量的时间！


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=deepmap/oapi-codegen&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/deepmap/oapi-codegen 

开源项目作者：deepmap

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=deepmap/oapi-codegen)

关注我们，一起探索有意思的开源项目。

