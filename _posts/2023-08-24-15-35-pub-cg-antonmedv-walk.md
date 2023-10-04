---
layout: post
title: Walk - 一个简单好用的终端文件管理器
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在终端中进行文件管理时，我们通常需要频繁使用 cd 和 ls 命令来进行文件夹的切换和查看，但是这种方式不够直观，也不够快捷。因此，对于一个命令行工具的爱好者来说，需要一个更加简单和极简的终端文件管理器来帮助我们更快速地进行文件管理。

今天要给大家推荐一个 GitHub 开源项目 antonmedv/walk，该项目在 GitHub 有超过 2.1k Star，以下是该工具的使用示例：

![](https://raw.githubusercontent.com/antonmedv/walk/master/.github/images/demo.gif)

###### 项目介绍

Walk 是一个终端文件管理器，它可以帮助我们更快速地进行文件管理。它提供了模糊搜索功能，可以快速定位到我们需要的文件夹，同时也可以直接在终端中打开 vim 编辑器。Walk 的设计非常简单，只提供了必要的功能，让我们可以更加专注于文件管理本身。要开始使用需要先掌握一些快捷命令。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230826201413835.png)

以下列举了部分功能的使用。

1、文件内容预览功能：在浏览文件目录树时进行文件内容的预览

![](https://raw.githubusercontent.com/antonmedv/walk/master/.github/images/preview-mode.gif)

2、删除文件或文件夹：输入快捷命令 dd 进行文件或者文件夹删除

![](https://raw.githubusercontent.com/antonmedv/walk/master/.github/images/rm-demo.gif)

3、目录树增加前置的 icon 图标

![](https://raw.githubusercontent.com/antonmedv/walk/master/.github/images/demo-icons.gif)

###### 如何安装使用

Walk 的安装非常简单，参考如下方式执行命令即可。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230826201601684.png)

下载好后需要将 walk 命令配置在你的 shell 可访问的路径上，以下是设置 lk 别名触发文件管理命令，针对  Bash/Zsh、Fish、PowerShell 配置略有不同。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230826201714931.png)

###### 项目推介

Walk是一个非常简单和实用的终端文件管理器，它的开发者也非常活跃，不断地更新和维护这个项目。同时，Walk 也得到了很多用户的好评和推荐，可以帮助我们更加高效地进行文件管理。

如果你正在寻找一款简单而实用的终端文件管理器，那么 Walk 绝对是一个不错的选择。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=antonmedv/walk&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/antonmedv/walk 

开源项目作者：antonmedv

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=antonmedv/walk)

关注我们，一起探索有意思的开源项目。

