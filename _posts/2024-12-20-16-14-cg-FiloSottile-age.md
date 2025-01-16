---
layout: post
title: 小巧简单的文件加密工具
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

数据安全性成为了许多组织和个人面临的主要挑战之一。随着云计算和远程工作模式的普及，对文件进行安全、高效的加密变得尤为重要。然而，许多加密工具要么过于复杂，充斥着各种配置选项，要么安全性不足，不能有效地保护敏感数据免受未经授权的访问。此外，许多工具缺乏跨平台支持和易用性，使得用户在不同环境下难以保持数据的加密解密一致性。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-45b7152238aecfcb3433ee8e3cbb7366.png)

今天要给大家推荐一个 GitHub 开源项目 age，该项目在 GitHub 有超过 17.7k Star。

![](https://stats.deeptrain.net/repo/FiloSottile/age/?theme=light)

一句话介绍该项目：A simple, modern and secure encryption tool (and Go library) with small explicit keys, no config options, and UNIX-style composability.

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241223223316302.png)


###### 项目介绍

`age` 是一个简单、现代且安全的文件加密工具及 Go 语言库，设计理念围绕着小巧明确的密钥、零配置选项以及 UNIX 风格的组合性，旨在为用户提供一个直观、易于使用的加密解决方案。`age` 支持通过小而明确的公钥进行加密，或者选择使用口令加密，更贴合不同用户的需求场景。此外，它还支持硬件 PIV 令牌如 YubiKeys，通过插件扩展其功能。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241223223647487.png)

###### 如何使用

用户可以通过多种途径在不同的操作系统上安装 `age`

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241223223914599.png)

安装后使用方式参考如下：

1、生成密钥

```bash
$ age-keygen -o key.txt
```

2、加密文件（假设已有公钥）

```bash
$ tar cvz ~/data | age -r [public-secrets] > data.tar.gz.age
```

2、解密文件

```bash
$ age --decrypt -i key.txt data.tar.gz.age > data.tar.gz
```

###### 项目推介

`age` 由知名的安全专家 Filippo Valsorda 设计，并且得到了社区的广泛认可和支持。age 有强大的跨平台支持和易用性，不论是个人用户还是企业，都可以轻松地将其集成到现有的安全体系中。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=FiloSottile/age&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/FiloSottile/age 

开源项目作者：FiloSottile

开源协议：BSD 3-Clause "New" or "Revised" License

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=FiloSottile/age)

关注我们，一起探索有意思的开源项目。

