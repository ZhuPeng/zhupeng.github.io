---
layout: post
title: Mods - 一个基于命令行专为管道设计的人工智能工具
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在我们的日常工作中，我们经常会使用命令行来执行各种操作，但是有时候我们可能会遇到一些问题，比如如何解析命令的输出，如何将这些输出以友好的方式展示出来，或者如何在命令行中使用人工智能等。这些问题可能会让我们的工作变得复杂和困难。

今天要给大家推荐一个 GitHub 开源项目 charmbracelet/mods，该项目在 GitHub 有超过 1.7k Star，用一句话介绍该项目就是：“AI on the command line”。

![](https://github.com/charmbracelet/mods/assets/25087/5442bf46-b908-47af-bf4e-60f7c38951c4)

###### 项目介绍

Mods 是一个基于命令行的人工智能工具，专为管道设计。它能够非常好地解析命令的输出，并以 CLI 友好的文本格式（如 Markdown）返回结果。Mods 是一个简单的工具，使在命令行和管道中使用人工智能变得非常容易。Mods 与 OpenAI 和 LocalAI 兼容。Mods 的功能包括读取标准输入并用在 Mods 参数中提供的提示前置它，然后将输入文本发送到 LLM 并打印出结果，可选择要求 LLM 将响应格式化为 Markdown。Mods 提供了一种可以针对上一个管道命令输出再二次进行大模型查询的能力，Mods 也可以单独在标准输入或参数提供的提示上工作。

以下是一个使用示例，根据 curl 输出在通过大模型执行相关命令

![](https://vhs.charm.sh/vhs-5Uyj0U6Hlqi1LVIIRyYKM5.gif)

###### 如何使用

首先，你需要安装 Mods，然后查看一些下面的示例。由于 Mods 内置了 Markdown 格式化，你可能还想获取 Glow 以使输出更具吸引力。Mods 支持 OpenAI 兼容的端点。默认情况下，Mods 配置为支持 OpenAI 的官方 API 和在端口 8080 上运行的 LocalAI 安装。你可以通过运行 mods --settings 在你的设置文件中配置额外的端点。

安装 Mods 的方法如下：

```bash
# macOS 或 Linux
brew install charmbracelet/tap/mods

# Arch Linux
yay -S mods

# Debian/Ubuntu
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://repo.charm.sh/apt/gpg.key | sudo gpg --dearmor -o /etc/apt/keyrings/charm.gpg
echo "deb [signed-by=/etc/apt/keyrings/charm.gpg] https://repo.charm.sh/apt/ * *" | sudo tee /etc/apt/sources.list.d/charm.list
sudo apt update && sudo apt install mods

# Fedora/RHEL
echo '[charm]
name=Charm
baseurl=https://repo.charm.sh/yum/
enabled=1
gpgcheck=1
gpgkey=https://repo.charm.sh/yum/gpg.key' | sudo tee /etc/yum.repos.d/charm.repo
sudo yum install mods
```

###### 项目推介

Mods 是一个活跃的开源项目，由 Charmbracelet 团队开发。这个团队以开发高质量的开源项目而闻名。Mods 的设计理念和功能都非常出色，它不仅解决了命令行操作中的一些常见问题，还提供了一种全新的方式来使用人工智能。如果你是一个喜欢在命令行中工作的开发者，或者你正在寻找一种在命令行中使用人工智能的方法，那么 Mods 绝对值得你试试。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231029192504149.png)


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=charmbracelet/mods&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/charmbracelet/mods 

开源项目作者：charmbracelet

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=charmbracelet/mods)

关注我们，一起探索有意思的开源项目。

