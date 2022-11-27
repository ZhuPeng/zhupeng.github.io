---
layout: post
title: 又一个 SQLite 的增强扩展
tags: SQL
---

大家好。

SQLite 真的很强，轻量化、数据以文件形式存储，不需要单独的安装，同时又能使用强大的 SQL，所以只要我需要存储或者分析一些数据，我都会想到能否使用 SQLite 来存储和分析。比如 Excel 是否能够直接用 SQLite 来存储和分析呢？

今天要推荐的工具 xlite，就是一个可以将 Excel 表格文件导入 SQLite，并使用 SQL 进行查询的工具。xlite 以 SQLite 扩展的形式使用，在实际使用上，几乎跟 SQLite 内建的功能一样。以下就是具体的使用流程：

![image-20220828135625399](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220828135625399.png)

大致流程如下：

1、加载扩展，.load libxlite

2、创建虚拟表，从本地的 Excel 文件加载，并指定对应的列范围

3、使用 SQL 进行数据查找和分析

整体还是比较简单的，这样对 Excel 的支持简直太棒了，是重度使用 Excel 同学的福音。

xlite 使用 Rust 开发，目前在 GitHub 有超过 1K+ 的 Star，支持的 Excel 文件类型包括 .xlsx, .xls, .ods。目前 xlite 在支持数据的查找和分析，所以对应的变更操作（如 INSERT、UPDATE、DELETE）是不支持的，但是长期来看是否支持还不确定，如果能支持的话，也是一大利好。

更多项目详情请查看如下链接。

开源项目地址：https://github.com/x2bool/xlite

开源项目作者：[x2bool](https://github.com/x2bool)