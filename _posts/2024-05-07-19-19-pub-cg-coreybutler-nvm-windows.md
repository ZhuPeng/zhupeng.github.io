---
layout: post
title: 开发者首选的 Node 版本管理工具
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在当今多变的软件开发领域，开发者经常需要在不同版本的开发环境中切换以保证项目的兼容性和稳定性。特别是对于 Node.js 开发者来说，面对 Node.js 的快速迭代和版本众多，如何有效地管理和切换不同版本的 Node.js 成为了一个普遍而又繁琐的问题。而 Windows 用户更是因为操作系统的限制和特性，找不到一个既方便又有效的版本管理工具，这直接影响了他们的开发效率和体验。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-9951d738133eccc0600fd122e27346f4.png)

今天要给大家推荐一个 GitHub 开源项目 nvm-windows，该项目在 GitHub 有超过 36.7k Star，一句话介绍该项目：A node.js version management utility for Windows. Ironically written in Go.

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240511231420733.png)


###### 项目介绍

`NVM for Windows` 是一个专为 Windows 用户设计的 Node.js 版本管理工具，其核心目的是简化和优化在 Windows 系统上管理和切换 Node.js 版本的过程。该项目采用了 Go 语言开发，适配 Windows 操作系统的特性，提供了一个简易、直观且高效的解决方案。与原生 `nvm`（主要面向 Mac/Linux 用户）不同，`NVM for Windows` 针对 Windows 系统进行了专门的设计和优化，使其成为 Microsoft、npm 和 Google 推荐的 Windows 下的 Node.js 版本管理工具。

![](https://github.com/coreybutler/staticassets/raw/master/images/nvm-1.1.8-screenshot.jpg)

主要特点包括：

1、支持管理多个 Node.js 版本

2、独特的安装策略，避免与现有 Node.js 安装冲突

![](https://github.com/coreybutler/staticassets/raw/master/images/nvm-usage-highlighted.jpg)

3、简化安装和升级过程

4、提供图形用户界面安装程序，便于使用

![](https://github.com/coreybutler/staticassets/raw/master/images/nvm-installer.jpg)

###### 如何使用

1、在安装 `NVM for Windows` 之前，建议先卸载任何存在的 Node.js 版本，以避免潜在的路径冲突。

2、通过最新的安装程序 [Download Releases](https://github.com/coreybutler/nvm-windows/releases) 安装 `NVM for Windows`。

3、安装完成后，打开终端或 PowerShell，使用 `nvm install` 命令安装所需的 Node.js 版本，例如 `nvm install 14.0.0`。

4、使用 `nvm use` 命令切换 Node.js 版本，例如 `nvm use 14.0.0`。

5、若需要为特定的 Node.js 版本安装全局工具（如 yarn），只需在切换至该版本后执行相应的 npm 安装命令。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240511231815980.png)

###### 项目推介

`NVM for Windows` 已经成为 Windows 上众多 Node.js 开发者的首选版本管理工具。不仅如此，多家知名公司和组织已经开始在其开发流程中采用 `NVM for Windows` 来管理 Node.js 环境，极大地提升了开发效率和流程的灵活性。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240511231914082.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=coreybutler/nvm-windows&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/coreybutler/nvm-windows 

开源项目作者：coreybutler

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=coreybutler/nvm-windows)

关注我们，一起探索有意思的开源项目。

