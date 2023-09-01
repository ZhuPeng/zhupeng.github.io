---
layout: post
title: GitHub 开源项目 aandrew-me/tgpt 介绍，ChatGPT in terminal without needing API keys
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 aandrew-me/tgpt，该项目在 GitHub 有超过 625 Star，用一句话介绍该项目就是：“ChatGPT in terminal without needing API keys”。


![demo](https://user-images.githubusercontent.com/66430340/233759296-c4cf8cf2-0cab-48aa-9e84-40765b823282.gif)
![](https://raw.githubusercontent.com/aandrew-me/tgpt/master/tgpt.svg)





背景介绍：
在日常工作或学习中，我们经常需要使用聊天机器人进行对话，但是往往需要 API 密钥才能使用，这对很多用户来说是一个难题。此外，我们也希望能够在终端环境中直接使用聊天机器人，而不需要通过复杂的界面操作。

项目介绍：
Terminal GPT (tgpt) 是一个跨平台的命令行界面 (CLI) 工具，它允许你在终端中使用 ChatGPT 3.5，而无需 API 密钥。tgpt 提供了多种实用的功能，如生成和执行 shell 命令、生成代码等，同时还支持多行交互模式，可以满足不同用户的需求。tgpt 的设计理念是简洁、高效，让用户可以在终端环境中轻松使用聊天机器人。

如何使用：
tgpt 的安装非常简单，支持多种操作系统。对于 GNU/Linux 或 MacOS 用户，可以通过以下命令进行安装：

    curl -sSL https://raw.githubusercontent.com/aandrew-me/tgpt/main/install | bash -s /usr/local/bin

对于 Arch Linux 用户，可以通过 paru 或 yay 进行安装：

    paru -S tgpt-bin
    yay -S tgpt-bin

对于 Go 用户，可以通过以下命令进行安装：

    go install github.com/aandrew-me/tgpt@latest

对于 Windows 用户，可以通过 Chocolatey 或 Scoop 进行安装：

    choco install tgpt
    scoop install https://raw.githubusercontent.com/aandrew-me/tgpt/main/tgpt.json

使用 tgpt 也非常简单，例如，你可以通过以下命令查询互联网的定义：

    tgpt "What is internet?"

项目推介：
tgpt 是一个活跃的开源项目，已经得到了很多用户的认可和使用。它的设计理念和强大的功能使得它在聊天机器人领域中独树一帜。如果你在寻找一个可以在终端环境中使用的聊天机器人，那么 tgpt 将是你的最佳选择。






以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=aandrew-me/tgpt&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/aandrew-me/tgpt 

开源项目作者：aandrew-me

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=aandrew-me/tgpt)

关注我们，一起探索有意思的开源项目。

