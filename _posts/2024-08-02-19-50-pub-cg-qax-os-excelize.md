---
layout: post
title: 纯 Go 编写的 Excel 工具库
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

无论是财务报表、数据分析、还是日常的信息记录，Excel 都扮演着不可或缺的角色，而且 Excel 成为企业和个人管理数据的首选工具之一。然而，随着大数据和自动化的兴起，手动操作 Excel 文件已经远远无法满足高效、动态的数据处理需求。开发者和数据分析师们迫切需要一种高效的方式来程序化地读写 Excel 文件，尤其是在服务器端或者是没有安装 Microsoft Excel 的环境中。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-007c6f7feb2f79e13ed24d93eb762183.png)

今天要给大家推荐一个 GitHub 开源项目 excelize，该项目在 GitHub 有超过 17.8k Star。

![](https://stats.deeptrain.net/repo/qax-os/excelize/?theme=light)

一句话介绍该项目：Go language library for reading and writing Microsoft Excel™ (XLAM / XLSM / XLSX / XLTM / XLTX) spreadsheets

![](https://raw.githubusercontent.com/qax-os/excelize/master/./excelize.svg)

###### 项目介绍

Excelize 是一个用纯 Go 语言编写的库，它为读写 Microsoft Excel (XLAM / XLSM / XLSX / XLTM / XLTX) 文件提供了一套功能丰富的 API。

![](https://raw.githubusercontent.com/qax-os/excelize/master/./test/images/chart.png)

该库支持 Microsoft Excel 2007 及更高版本生成的电子表格文档，并且提供了高兼容性以支持复杂组件，这使得 Excelize 成为处理大量数据的强大工具。通过这个库，开发者可以高效地在服务端生成、编辑、格式化 Excel 文件，从而实现数据报告和分析的自动化。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240815213425387.png)

###### 如何使用

首先需要确保你的开发环境已经安装了 Go 语言环境，并且版本在 1.18 或以上。通过下面的命令，你可以轻松地安装 Excelize：

```bash
go get github.com/xuri/excelize/v2
```

创建一个新的 Excel 文件非常简单：

```go
package main

import (
    "fmt"
    "github.com/xuri/excelize/v2"
)

func main() {
    f := excelize.NewFile()
    index, err := f.NewSheet("Sheet2")
    f.SetCellValue("Sheet2", "A2", "Hello world.")
    f.SetActiveSheet(index)
    if err := f.SaveAs("Book1.xlsx"); err != nil {
        fmt.Println(err)
    }
}
```

读取现有 Excel 文件同样容易：

```go
package main

import (
    "fmt"
    "github.com/xuri/excelize/v2"
)

func main() {
    f, err := excelize.OpenFile("Book1.xlsx")
    cell, err := f.GetCellValue("Sheet1", "B2")
    fmt.Println(cell)
}
```

###### 项目推介

Excelize 由于其强大的功能、高效的性能以及易用的 API，已经在全球范围内被许多知名公司和组织所采用，包括但不限于金融、电信、制造业等领域。该项目的 GitHub 页面显示，它拥有稳定而活跃的开发维护状态，并且汇集了大量的 star 和贡献者。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=qax-os/excelize&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/qax-os/excelize 

开源项目作者：qax-os

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=qax-os/excelize)

关注我们，一起探索有意思的开源项目。

