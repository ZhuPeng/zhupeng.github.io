---
layout: post
title: 用 Go  编写的 PDF 处理库
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

PDF 文件因其跨平台、格式统一的特性被广泛应用于文档分享、工作报告、学术论文等领域。然而，随着使用场景的不断扩展，用户对 PDF 文件的处理需求也越来越多样化，包括但不限于合并、分割、加密、解密、压缩、优化、添加水印、创建表单等。尽管市场上存在诸多 PDF 处理工具，但它们或是功能有限，或是操作复杂，或是需要付费使用。特别是对于开发者而言，一个易于集成、功能全面、性能稳定的 PDF 处理库尤为重要，以便快速实现后端系统中对 PDF 文件的各种操作需求。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-a0b85cb869d1f0b2498b47f23ecffa4e.png)

今天要给大家推荐一个 GitHub 开源项目 pdfcpu，该项目在 GitHub 有超过 6.8k Star。

![](https://stats.deeptrain.net/repo/pdfcpu/pdfcpu/?theme=light)

一句话介绍该项目：A PDF processor written in Go.

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241015230640767.png)

###### 项目介绍

pdfcpu  是一个用 Go  编写的 PDF 处理库，它不仅支持 PDF 文档的加密和解密，还提供了一个全面的命令行界面（CLI），兼容所有版本的 PDF 文件，并对 PDF 2.0 (ISO-32000-2) 提供了基本支持及持续改进。

![](https://raw.githubusercontent.com/pdfcpu/pdfcpu/master/resources/demo.png)

此库通过其命令集，针对批处理和脚本处理提供强大的支持，并通过提供多样化的命令，简化了将 PDF 处理集成到基于 Go 的后端系统中。其命令集涵盖从注释、附件处理、创建书签、裁剪、解密加密，到合并、分割、水印、优化等几乎所有常见的 PDF 处理功能。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241015230855484.png)

###### 如何使用

要安装 pdfcpu，用户可以直接下载最新的二进制文件，或者通过 Go 模块进行安装：

```bash
$ git clone https://github.com/pdfcpu/pdfcpu
$ cd pdfcpu/cmd/pdfcpu
$ go install
$ pdfcpu version
```

或者直接通过 Go 安装：

```bash
$ go install github.com/pdfcpu/pdfcpu/cmd/pdfcpu@latest
```

对于 macOS 用户，还可以通过 Homebrew 进行安装：

```bash
$ brew install pdfcpu
$ pdfcpu version
```

此外，pdfcpu 也支持在 Docker 容器内运行，提供了 Dockerfile 用于构建镜像。

以下是 pdfcpu 支持的部分命令列表：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241015231014070.png)

###### 项目推介

pdfcpu 项目仍处于 *Alpha* 阶段，并不断进行着改进和更新，但它已经表现出相当的稳定性和可靠性。项目的活跃开发态势、响应社区反馈的积极性，以及持续增加的功能特性，使得 pdfcpu 成为了处理 PDF 文件的首选库之一。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=pdfcpu/pdfcpu&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/pdfcpu/pdfcpu 

开源项目作者：pdfcpu

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=pdfcpu/pdfcpu)

关注我们，一起探索有意思的开源项目。

