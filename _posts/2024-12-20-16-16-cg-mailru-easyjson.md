---
layout: post
title: GitHub 开源项目 mailru/easyjson 介绍，Fast JSON serializer for golang.
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 mailru/easyjson，该项目在 GitHub 有超过 4.5k Star。

![](https://stats.deeptrain.net/repo/mailru/easyjson/?theme=light)

一句话介绍该项目：Fast JSON serializer for golang.





###### 项目介绍

### 背景介绍
在现代软件开发中，JSON 已成为跨平台、跨语言数据交换的标准格式之一。无论是微服务之间的通信、浏览器与服务器的数据传输，还是配置文件的编写，JSON 都扮演着重要的角色。然而，在使用 Go 语言处理 JSON 数据时，标准的 `encoding/json` 包虽然功能强大，却因反射（reflection）的使用而在性能上存在不足。尤其是在高并发场景或数据密集型应用中，这种性能瓶颈会成为开发者难以忽略的核心痛点。

### 

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-4bd55b1cf7f3fa27370b0ad221eecbd0.png)

项目介绍
`easyjson` 是为 Go 语言设计的一个快速 JSON 序列化工具，它通过避免使用反射的方式，实现了从 Go 结构体到 JSON 数据以及反向转换的快速编解码。性能测试显示，`easyjson` 的速度比标准 `encoding/json` 包快 4-5 倍，比其他 JSON 编码库快 2-3 倍。

`easyjson` 生成的 Go 代码结构简单，便于开发者进行优化或修正。它还提供了一些标准 `encoding/json` 包中不可用的选项，例如默认生成 "snake_case" 命名或启用 `omitempty` 行为，使开发者能够根据需要定制生成的代码。

### 如何使用
安装 `easyjson` 很简单，可以根据 Go 的版本选择适当的安装命令。对于 Go 1.17 以上的版本，可以使用以下命令：

```sh
go get github.com/mailru/easyjson && go install github.com/mailru/easyjson/...@latest
```

安装后，通过简单的命令就可以为 `.go` 文件中的所有结构体生成相应的 marshaller 和 unmarshaller 函数：

```sh
easyjson -all .go
```

使用 `easyjson` 进行 JSON 的序列化（Serialize）和反序列化（Deserialize）也极为便捷：

```go
someStruct := &SomeStruct{Field1: "val1", Field2: "val2"}
rawBytes, err := easyjson.Marshal(someStruct)

someStruct := &SomeStruct{}
err := easyjson.Unmarshal(rawBytes, someStruct)
```

更多使用说明和功能，请参考 [GoDoc 文档](https://godoc.org/github.com/mailru/easyjson)。

### 项目推介
`easyjson` 由 Mail.Ru Group 的团队开发和维护，这保证了项目的专业性和可靠性。项目自发布以来，因其出色的性能和易用性，已被许多知名项目和公司采用。活跃的开发状态、持续的维护更新以及这些实际应用案例，都是选择 `easyjson` 的有力理由。

无论你是在开发高性能的 Web 应用、微服务，还是简单需要在 Go 中高效处理 JSON 数据的场景，`easyjson` 都能为你提供强大的支持。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=mailru/easyjson&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/mailru/easyjson 

开源项目作者：mailru

开源协议：MIT License

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=mailru/easyjson)

关注我们，一起探索有意思的开源项目。

