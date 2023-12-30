---
layout: post
title: Wails - 轻量级的 Electron 替代品，使用 Go 封装前端页面
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在日常开发中，我们常常会遇到需要使用 Go 语言开发桌面应用的需求，这时候就需要一个能够将 Go 代码和前端页面打包成一个二进制文件的工具。传统的方法是通过内置的 web 服务器为 Go 程序提供 web 接口，但这种方式并不是最佳解决方案。

今天要给大家推荐一个 GitHub 开源项目 wailsapp/wails，该项目在 GitHub 有超过 18.7k Star，用一句话介绍该项目就是：“Create beautiful applications using Go”。
![](https://raw.githubusercontent.com/wailsapp/wails/master/./assets/images/logo-universal.png)

###### 项目介绍

Wails 提供了一种新的方法：将 Go 代码和 web 前端封装成一个单一的二进制文件。它提供了一些工具，可以帮助你处理项目创建、编译和打包，让你只需要专注于创造性的工作。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231119160353765.png)

它的主要特点包括：

- 使用标准的 Go 作为后端
- 可以使用任何你已经熟悉的前端技术来构建 UI
- 使用预构建的模板快速创建丰富的前端
- 从 Javascript 轻松调用 Go 方法
- 为你的 Go 结构和方法自动生成 Typescript 定义
- 支持原生的对话框和菜单
- 支持原生的深色/浅色模式
- 支持现代的半透明和 "磨砂窗口" 效果
- 在 Go 和 Javascript 之间提供统一的事件系统
- 强大的命令行工具，可以快速生成和构建你的项目
- 多平台支持
- 使用原生的渲染引擎，不需要嵌入浏览器！

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231119160411164.png)

###### 如何使用

使用如下 Go 命令即可快速完成工具的安装。一旦安装完成，你就可以开始使用 Wails 来创建你的项目了。

```bash
go install github.com/wailsapp/wails/v2/cmd/wails@latest
```

首先，可以选择框架并进行项目初始化。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231119160619019.png)

生成的项目代码结构如下：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231119160652573.png)

在项目目录运行 wails dev 即可快速进行编译并运行代码。运行后将看到如下页面：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231119160806161.png)

###### 项目推介

Wails 的贡献者来自全球各地。如果你是 Go 程序员，并且希望为你的应用程序添加 HTML/JS/CSS 前端，而不想创建服务器并打开浏览器来查看它，那么 Wails 就是你的最佳选择。此外，Wails 还提供了原生的菜单和对话框，因此它可以被视为一个轻量级的 Electron 替代品。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=wailsapp/wails&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/wailsapp/wails 

开源项目作者：wailsapp

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=wailsapp/wails)

关注我们，一起探索有意思的开源项目。

