---
layout: post
title: 全面、高效、可复用的 Go 工具库
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在日常的开发工作中，开发人员经常会遇到各种数据操作的需求，包括但不限于字符串处理、时间日期格式化、加密解密、数据结构操作等。然而，Go 语言的标准库尽管功能强大，但在某些方面依然存在使用上的不便，例如高效地处理字符串、切片操作或是复杂的数据结构处理等。这导致开发人员不得不重复造轮子，或是寻找第三方库来满足需求。而在寻找第三方库时，又常常面临文档不全、维护更新慢、依赖繁杂等问题。这些问题严重影响了开发效率和项目的可维护性。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-89cddebf233a4dd3b8b0f7807d7a56e0.png)

今天要给大家推荐一个 GitHub 开源项目 lancet，该项目在 GitHub 有超过 4.7k Star。

![](https://stats.deeptrain.net/repo/duke-git/lancet/?theme=light)

一句话介绍该项目：A comprehensive, efficient, and reusable util function library of Go.


![](https://raw.githubusercontent.com/duke-git/lancet/master/./logo.png)


###### 项目介绍

Lancet 是一个全面、高效、可复用的 Go 语言工具函数库，灵感来自 Java 的 apache common 包和 lodash.js。Lancet 提供了 600 多个 Go 语言的实用函数

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240911225051745.png)

支持字符串、切片、日期时间、网络、加密等多种操作，且仅依赖 Go 标准库和 golang.org/x 库，保证了项目的轻量级和高效性。每个导出的函数都配备了单元测试，确保了库的稳定性和可靠性。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240911225106719.png)

###### 如何使用

对于使用 Go 1.18 及以上版本的用户，建议安装 Lancet v2.x.x 版本，因为在这个版本中所有函数都采用了 Go 1.18 的泛型进行重写。对于使用 Go 1.18 以下版本的用户，则应安装 v1.x.x 版本。

```bash
go get github.com/duke-git/lancet/v2 // will install latest version of v2.x.x

go get github.com/duke-git/lancet // below go1.18, install latest version of v1.x.x
```

以下是使用字符串反转功能的示例：

```go
package main

import (
    "fmt"
    "github.com/duke-git/lancet/v2/strutil"
)

func main() {
    s := "hello"
    rs := strutil.Reverse(s)
    fmt.Println(rs) //Output：olleh
}
```

###### 项目推介

Lancet 自发布以来，已在 GitHub 上获得了良好的关注度和积极的反馈。项目维护活跃，定期更新，确保了其稳定性和时效性。其简洁而全面的设计理念，让开发人员能够迅速提高开发效率，减少不必要的工作量。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=duke-git/lancet&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/duke-git/lancet 

开源项目作者：duke-git

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=duke-git/lancet)

关注我们，一起探索有意思的开源项目。

