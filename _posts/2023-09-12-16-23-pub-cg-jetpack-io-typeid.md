---
layout: post
title: TypeID - 一个受 Stripe IDs 启发的类型安全、K-可排序、全局唯一标识符生成工具
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在进行大型项目开发时，我们经常会遇到需要对各种类型的数据进行唯一标识的问题。传统的 UUIDv4 虽然可以提供全局唯一的标识，但是它完全随机的特性使得在数据库中的排序性能较差，且无法直观地理解其代表的实体类型。这就需要我们寻找一个既能提供全局唯一标识，又具有良好的排序性能和类型安全性的解决方案。

今天要给大家推荐一个 GitHub 开源项目 jetpack-io/typeid，该项目在 GitHub 有超过 2.3k Star，用一句话介绍该项目就是：“Type-safe, K-sortable, globally unique identifier inspired by Stripe IDs”。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231019203100795.png)

###### 项目介绍

TypeID 是一个受 Stripe IDs 启发的类型安全、K-可排序、全局唯一标识符。它是 UUIDv7 的现代、类型安全的扩展。TypeID 由三部分组成：类型前缀、下划线分隔符和一个使用修改过的 base32 编码的 128 位 UUIDv7。例如，一个类型为 user 的 TypeID 可能如下所示：

      user_2x4y6z8a0b1c2d3e4f5g6h7j8k
      └──┘ └────────────────────────┘
      类型    uuid 后缀 (base32)

TypeID 的优点包括：
- 类型安全：你不能在需要 post ID 的地方误用 user ID。在调试时，你可以立即理解一个 TypeID 引用的实体类型是什么，这得益于类型前缀。
- 与 UUID 兼容：TypeID 是 UUID 的超集。它们基于即将出现的 UUIDv7 标准。如果你解码 TypeID 并删除类型信息，你会得到一个有效的 UUIDv7。
- K-可排序：TypeID 是 K-可排序的，可以用作数据库的主键，同时保证良好的局部性。相比于完全随机的全局 id，如 UUIDv4，TypeID 的数据库局部性更好。
- 深思熟虑的编码：base32 编码是 URL 安全的，不区分大小写，避免了模糊字符，可以通过双击选择复制，且比 UUID 使用的传统十六进制编码更紧凑（26 个字符 vs 36 个字符）。

###### 如何使用

TypeID 项目已经提供了 Go、SQL 和 TypeScript 的官方实现，同时也有来自社区的多种语言实现，包括 C#、Elixir、Haskell、Java、PHP、Python 和 Ruby。你可以根据自己的需要选择合适的实现进行使用。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231019203231262.png)

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231019203258111.png)

同时你也可以使用如下命令行，进行相关的测试。

```bash
curl -fsSL https://get.jetpack.io/typeid | bash
```

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231019203405526.png)

###### 项目推介

TypeID 项目由 jetpack.io 开发和维护，该团队在开源社区中有很高的活跃度和影响力。项目的开发活跃，社区反馈积极，已经有多个知名的开源项目和公司在使用。如果你在寻找一个类型安全、K-可排序、全局唯一的标识符解决方案，TypeID 无疑是一个值得你关注和尝试的项目。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=jetpack-io/typeid&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/jetpack-io/typeid 

开源项目作者：jetpack-io

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=jetpack-io/typeid)

关注我们，一起探索有意思的开源项目。

