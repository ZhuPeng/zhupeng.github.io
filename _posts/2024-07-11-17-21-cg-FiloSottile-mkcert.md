---
layout: post
title: GitHub 开源项目 FiloSottile/mkcert 介绍，A simple zero-config tool to make locally trusted development certificates with any names you'd like.
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 FiloSottile/mkcert，该项目在 GitHub 有超过 47.2k Star。

![](https://stats.deeptrain.net/repo/FiloSottile/mkcert/?theme=light)

一句话介绍该项目：A simple zero-config tool to make locally trusted development certificates with any names you'd like.




![](https://user-images.githubusercontent.com/1225294/51066373-96d4aa80-15be-11e9-91e2-f4e44a3a4458.png)


###### 项目介绍

背景介绍：
在当今快速发展的互联网时代，Web 开发几乎已成为编程领域中不可或缺的一部分。开发人员在本地测试网站时，常常需要确保与线上环境一致的安全连接（HTTPS）。然而，使用真正的证书颁发机构（CA）颁发的证书来进行本地开发不仅存在安全隐患，而且对于一些特殊域名（比如 `example.test`、`localhost` 或 `127.0.0.1`）来说，甚至是不可能的。尽管自签名证书可以作为一种替代方案，但它经常会引起浏览器的不信任错误。自己管理 CA 可以说是一种最好的解决方案，但这通常涉及复杂的命令、专业知识和手动操作，对于大多数开发人员来说，这是一项艰巨的任务。



![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-6e75d82cb07dc3cc66542361db88af1c.png)

项目介绍：
在这样的背景下，`mkcert` 应运而生。`mkcert` 是一个简单的零配置工具，用于生成本地受信任的开发证书，可以自定义任意名称。`mkcert` 自动在系统根存储中创建并安装本地 CA，并生成本地受信任的证书。这意味着开发人员可以轻松地在本地开发环境中使用 HTTPS，而无需担心安全警告或配置复杂性的问题。`mkcert` 支持主流操作系统及浏览器，包括 macOS、Linux、Windows，以及 Firefox、Chrome 和 Java 环境。

如何使用：
安装 `mkcert` 极其简单。以 macOS 为例：

1. 使用 Homebrew 安装：
```
brew install mkcert
brew install nss # 如果使用 Firefox
```

生成证书:
```
$ mkcert -install
创建了一个新的本地 CA 💥
本地 CA 现已安装在系统信任库中！⚡️

$ mkcert example.com "*.example.com" example.test localhost 127.0.0.1 ::1
为以下名称创建了有效的新证书 📜
 - "example.com"
 - "*.example.com"
 - "example.test"
 - "localhost"
 - "127.0.0.1"
 - "::1"
证书位于 "./example.com+5.pem"，密钥位于 "./example.com+5-key.pem" ✅
```

对于 Linux、Windows 用户，安装方式类似，可以通过包管理器或者直接从源代码编译。更多系统的安装指导，请参考项目 README。

项目推介：
`mkcert` 不仅因其简单易用而备受开发人员的欢迎，它的作者 FiloSottile 也是一个在安全和加密领域有着广泛贡献的知名开发者。这保证了项目的高质量和持续更新。截至目前，该项目在 GitHub 上拥有超过 30k 的星标，足以证明其广泛的受欢迎程度和社区信任度。无论你是独立开发者还是企业用户，`mkcert` 都能为你解决本地 HTTPS 部署的痛点。无论你在开发现代 Web 应用、APIs 还是进行其他需要本地 HTTPS 的开发工作，`mkcert` 都是一个不可或缺的工具。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=FiloSottile/mkcert&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/FiloSottile/mkcert 

开源项目作者：FiloSottile

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=FiloSottile/mkcert)

关注我们，一起探索有意思的开源项目。

