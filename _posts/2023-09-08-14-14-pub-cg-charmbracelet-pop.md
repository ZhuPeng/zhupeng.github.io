---
layout: post
title: Pop - 一个可以在命令行终端下发送邮件的开源项目
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在日常工作中，我们经常需要发送电子邮件，但是有时候在命令行终端环境下，我们需要通过命令行来发送邮件，这时候就需要一个能够在终端下发送邮件的工具。然而，市面上的这类工具往往操作复杂，使用不便。

今天要给大家推荐一个 GitHub 开源项目 charmbracelet/pop，该项目在 GitHub 有超过 1.7k Star，用一句话介绍该项目就是：“Send emails from your terminal”。

![](https://stuff.charm.sh/pop/pop-logo.png)
![](https://vhs.charm.sh/vhs-5Dyv3pvzB2YwtUSr72LqSz.gif)

###### 项目介绍

Pop  是一个可以在命令行终端下发送邮件的开源项目，它的主要功能是提供一个文本用户界面（TUI）和命令行接口（CLI），让你可以在终端环境下方便地发送邮件。你只需要简单的命令，就可以完成邮件的发送，同时还支持附件的发送。此外，Pop 还支持通过 RESEND_API_KEY 或者配置 SMTP 主机来使用，这为用户提供了更多的选择。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231004205227823.png)

![](https://vhs.charm.sh/vhs-5Cr6Gt1YVBjxGr9zdS85AO.gif)

###### 如何使用

首先，可以通过包管理器进行 pop 安装，例如在 macOS 或 Linux 下，你可以使用 " brew install pop " 来安装。

```bash
# macOS or Linux
brew install pop

# Nix
nix-env -iA nixpkgs.pop

# Arch (btw)
yay -S charm-pop-bin

# Install with Go
go install github.com/charmbracelet/pop@latest
```

然后，你可以通过 pop 命令来启动 TUI，或者通过 " pop < message.md --from "me@example.com" --to "you@example.com" --subject "Hello, world!" --attach invoice.pdf " 的方式来发送邮件。此外，你还可以通过设置环境变量来配置 Pop，例如设置 POP_SMTP_HOST、POP_SMTP_PORT、POP_SMTP_USERNAME、POP_SMTP_PASSWORD 等。
![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231004205541534.png)

###### 项目推介

Pop 是一个由 Charmbracelet 开发的开源项目，Charmbracelet 是一个知名的开源组织，他们开发的项目都非常优秀，比如 gum（一个优雅的命令行终端工具）、vhs（命令行执行录制工具）。如果你在寻找一个在终端下发送邮件的工具，那么 Pop 是一个非常好的选择。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231004205824764.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=charmbracelet/pop&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/charmbracelet/pop 

开源项目作者：charmbracelet

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=charmbracelet/pop)

关注我们，一起探索有意思的开源项目。

