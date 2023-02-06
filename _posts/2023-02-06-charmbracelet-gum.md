---
layout: post
title: 用于构建优雅命令行程序的工具推荐
tags: Go&命令行
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 charmbracelet/gum，该项目在 GitHub 有超过 12.0k Star，用一句话介绍该项目就是：“A tool for glamorous shell scripts 🎀”，用于构建优雅命令行程序的工具。

![](https://stuff.charm.sh/gum/gum.png)

可能大家不太能理解优雅的命令行程序怎么样的，我们来看几个例子：

1、从命令获取输入，同时有好的交互

![](https://stuff.charm.sh/gum/demo.gif)

2、根据需要生成匹配格式的 commit 信息

![](https://stuff.charm.sh/gum/commit_2.gif)

以上是两个示例，而 gum 就是一个可以方便构建如上命令行程序的工具。在我的初步使用上了解到，gum 核心就是如何从命令行中获取输入，而输入的方式包括直接输入、选择输入、文件输入等，而程序可以利用输入进行特殊的执行逻辑，从而实现操作的自动化。

我们来多看几个示例，你就能更多的感受 gum 的强大之处了。

1、支持搜索过滤并将结果写入文件

![](/Users/zhupeng/Downloads/filter.gif)

2、确认按钮输入
![](/Users/zhupeng/Downloads/confirm_2.gif)

3、支持文件夹浏览

![](/Users/zhupeng/Downloads/file.gif)

而要实现以上任何示例都是比较的简单的，如果你喜欢使用命令行，gum 一定是一个你喜欢的工具。

### 如何安装使用

以下有很多安装 gum 的方式，大家可任选其一：

```bash
# macOS or Linux
brew install gum

# Arch Linux (btw)
pacman -S gum

# Nix
nix-env -iA nixpkgs.gum
# Or, with flakes
nix run "github:charmbracelet/gum" -- --help

# Debian/Ubuntu
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://repo.charm.sh/apt/gpg.key | sudo gpg --dearmor -o /etc/apt/keyrings/charm.gpg
echo "deb [signed-by=/etc/apt/keyrings/charm.gpg] https://repo.charm.sh/apt/ * *" | sudo tee /etc/apt/sources.list.d/charm.list
sudo apt update && sudo apt install gum

# Fedora/RHEL
echo '[charm]
name=Charm
baseurl=https://repo.charm.sh/yum/
enabled=1
gpgcheck=1
gpgkey=https://repo.charm.sh/yum/gpg.key' | sudo tee /etc/yum.repos.d/charm.repo
sudo yum install gum

# Alpine
apk add gum

# Android (via termux)
pkg install gum

# Windows (via Scoop)
scoop install charm-gum
```

gum 还支持很多的语法，更多项目详情请查看如下链接。

开源项目地址：https://github.com/charmbracelet/gum  (文末可点击阅读原文)

开源项目作者：gum

