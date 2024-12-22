---
layout: post
title: 一款简单易用的 json 解析库
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在快节奏的开发工作中，处理 json 数据是一项常见但往往耗时的任务。无论是解析复杂的 json 结构，还是需要在没有固定模式的大型 json 文件中查找特定的信息，开发者都面临着效率问题。特别是在 Go 语言中，尽管其标准库提供了强大的 json 支持，但在处理复杂或大型 json 文档时，依旧可能感到不够灵活和高效。关键的痛点包括如下：

1、路径检索复杂性：需要在嵌套的 json 结构中快速定位和检索数据，使用传统方法时往往要写大量的代码。

2、效率问题：在大型 json 文件中查找特定信息时，性能可能成为瓶颈。

3、代码复杂度：实现复杂的 json 数据检索和操作可能使代码变得难以维护和理解。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-3f6338302471222cf5f5e15a78f767ef.png)

今天要给大家推荐一个 GitHub 开源项目 gjson，该项目在 GitHub 有超过 14.5k Star。

![](https://stats.deeptrain.net/repo/tidwall/gjson/?theme=light)

一句话介绍该项目：Get json values quickly - json parser for Go

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241125224045997.png)


###### 项目介绍

`Gjson` 是一个为 Go 语言设计的开源包，它通过提供快速简单的方式从 json 中获取值来解决上述问题。其特点包括：

1、一行检索：能够通过简单的路径语法，实现对嵌套 json 数据的快速访问。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241125224314473.png)

2、点符号路径：支持直观的点符号来定位 json 结构中的元素。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241125224325765.png)

3、迭代和解析 json 行：简化了遍历 json 对象或数组，以及解析多行 json 数据的过程。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241125224349548.png)

此外，`Gjson` 还与 `Sjson` 和 `JJ` 命令行工具配合使用，分别提供了修改 json 数据和命令行交互功能，进一步增加了开发者操作 json 的灵活性。

###### 如何使用

运行以下命令安装：

```sh
$ go get -u github.com/tidwall/gjson
```

下面是一个简单的使用例子，展示了如何从 json 字符串中检索特定字段的值：

```go
package main

import "github.com/tidwall/gjson"

const json = `{"name":{"first":"Janet","last":"Prichard"},"age":47}`

func main() {
	value := gjson.Get(json, "name.last")
	println(value.String()) // 输出 "Prichard"
}
```

###### 项目推介

`Gjson` 目前是一个活跃的开源项目，它的优势不仅在于其简单、高效的 API，而且因为它为许多工作和项目节约了大量的时间和劳动。由于其卓越的性能和易用性，`Gjson` 已经被多家知名公司和许多个人项目采用。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241125224504385.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=tidwall/gjson&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/tidwall/gjson 

开源项目作者：tidwall

开源协议：MIT License

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=tidwall/gjson)

关注我们，一起探索有意思的开源项目。

