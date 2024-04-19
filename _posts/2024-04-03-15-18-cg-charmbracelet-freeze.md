---
layout: post
title: GitHub 开源项目 charmbracelet/freeze 介绍，Generate images of code and terminal output 📸
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 charmbracelet/freeze，该项目在 GitHub 有超过 1.3k Star，一句话介绍该项目：Generate images of code and terminal output 📸




![](https://github.com/charmbracelet/freeze/assets/25087/de76b799-fa67-4b5b-8da2-d990ca5b4e06)

![](https://vhs.charm.sh/vhs-1C6z5SUKlTdqdj4KL1ADlH.gif)

![](https://raw.githubusercontent.com/charmbracelet/freeze/master/https://raw.githubusercontent.com/charmbracelet/freeze/master/./test/golden/svg/shadow.svg)

![](https://raw.githubusercontent.com/charmbracelet/freeze/master/./test/golden/svg/eza.svg)

![](https://vhs.charm.sh/vhs-1AGhIlc2Mtn9Ltc8vPtaAP.gif)

![](https://raw.githubusercontent.com/charmbracelet/freeze/master/./test/golden/svg/haskell.svg)

![](https://raw.githubusercontent.com/charmbracelet/freeze/master/./test/golden/svg/dracula.svg)

![](https://raw.githubusercontent.com/charmbracelet/freeze/master/./test/golden/svg/border-radius.svg)

![](https://raw.githubusercontent.com/charmbracelet/freeze/master/./test/golden/svg/window.svg)

![](https://raw.githubusercontent.com/charmbracelet/freeze/master/./test/golden/svg/border-width.svg)



首先，我们先介绍一些背景。在编程，教学或技术推广的过程中，我们经常会碰到需要展示代码或终端输出结果的情况。传统的做法是截屏或复制粘贴文本，但这样的效果往往并不理想，不仅因为所示的代码样式单一、不够美观，且根据不同的展示环境，效果展示不一，更重要的是这种方式无法定制优化，例如我们想更改代码的主题样式、字体大小，或者模拟终端的样式等等，这就使得我们的展示并不能达到最佳效果。

针对这个问题，我要为大家介绍一个 GitHub 上的优秀开源项目—— `Freeze`。Freeze 是一个完美解决上述问题的项目，它能够生成代码和终端输出的图片。与此同时，Freeze 支持生成 PNG，SVG 和 WebP 格式的图片，并且它还能捕获并生成终端的 ANSI 输出。更让人惊喜的是，Freeze 提供了高度的自定义能力以及一个可以进行简单且易操作的交互式 TUI，以便用户能够更方便地对生成的图片进行个性化定制。

关于如何使用 Freeze，我们可以通过很多种方式来进行安装，例如在 macOS 或 Linux 系统中我们可以通过 Homebrew 来安装，对于 Arch Linux 用户也可以通过 pacman 安装，对于使用 Nix 系统的用户也可以非常方便地进行安装。当然，还可以通过下载对应平台的程序包或者二进制文件进行安装，对于 Go 开发者，还可以直接通过 Go 来进行安装。在安装完成后，我们可以通过指令来生成代码或者终端输出的图片，如 `freeze artichoke.hs -o artichoke.png` 生成代码图片， `freeze --execute "eza -lah"` 捕获并生成终端的 ANSI 输出。

推荐这个项目的原因有两个，首先它解决了我们在展示代码或终端输出时常见的问题，提供了生成格式多样、且高度可定制的图片，大大增强了我们展示的能力。其次，项目的活跃度很高，作者对项目的维护热情很高，对 issues 和 PR 的响应也非常积极，这对于我们使用开源项目来说非常重要。结合这些特点，我们推荐大家尝试使用这个项目，相信它会有很大的帮助。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=charmbracelet/freeze&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/charmbracelet/freeze 

开源项目作者：charmbracelet

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=charmbracelet/freeze)

关注我们，一起探索有意思的开源项目。

