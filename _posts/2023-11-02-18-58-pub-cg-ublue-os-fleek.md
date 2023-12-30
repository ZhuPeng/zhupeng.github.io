---
layout: post
title: Fleek - 一个全能的电脑 Home 环境管理系统，适配主流操作系统
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在我们的日常编程工作中，我们常常需要在不同的电脑设备上进行操作，常见的比如工作和家庭电脑的切换，但是每次更换设备时，我们都需要重新配置我们的工作环境，这无疑增加了我们的工作负担。同时，我们可能还需要安装各种各样的软件和工具，但是在不同的操作系统中，这些软件和工具的安装过程可能会有所不同，这也给我们带来了一定的困扰。这时候，我们就需要一个能够帮助我们快速搭建工作环境，同时支持各种软件和工具安装的工具。

今天要给大家推荐一个 GitHub 开源项目 ublue-os/fleek，该项目在 GitHub 有差不多 1000 Star，用一句话介绍该项目就是：“Own your $HOME”。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231119155305879.png)

###### 项目介绍

Fleek 是一个全能的电脑 Home 环境管理系统，它可以帮助你在电脑上快速搭建起一个高效的工作环境。无论你是使用全新的 M2 MacBook Air，还是使用经久耐用的运行 Linux 的 ThinkPad，甚至是使用带有 WSL 的 Windows，Fleek 都能让你在任何地方都能拥有相同的环境、工具和配置。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231119155750101.png)

Fleek 提供了一套丰富的程序和包，无论你需要安装新的编程语言工具集，还是最新的社交媒体应用，Fleek 都能为你提供支持。只需要在你的 .fleek.yml 文件中添加一行代码，然后运行 fleek apply，你就可以自由地安装你需要的软件和工具。

安装新工具：

![](https://raw.githubusercontent.com/ublue-os/fleek/master/fleek-add.gif)

搜索 ruby 并安装：

![](https://raw.githubusercontent.com/ublue-os/fleek/master/fleek-search.gif)

###### 如何使用

首先，你需要按照 Fleek 的安装指南进行安装。需要先安装 Nix，再做相应的初始化即可，参考如下：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231119155842166.png)

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231119155900441.png)

然后，在你的 .fleek.yml 文件中添加你需要的软件和工具，例如：

```
packages:
    - helix
    - go
    - gcc
    - nodejs
    - yarn
    - rustup
    - vhs
    - rnix-lsp
    - duf
```

然后运行 fleek apply，你就可以安装你需要的软件和工具了。如果你想要更多的自由度，你可以使用 fleek eject 来手动管理你的配置。

###### 项目推介

Fleek 项目目前处于 BETA 阶段，但是它已经能够提供强大的功能，并且有着良好的稳定性。Fleek 是基于 Nix 和 Nix Home Manager 构建的，但是 Fleek 提供了一个用户友好的命令行接口，隐藏了所有的复杂性。无论你是一个经验丰富的开发者，还是一个初学者，Fleek 都能为你提供强大的支持。所以，我强烈推荐你试试 Fleek，它会给你带来全新的体验。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=ublue-os/fleek&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/ublue-os/fleek 

开源项目作者：ublue-os

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=ublue-os/fleek)

关注我们，一起探索有意思的开源项目。