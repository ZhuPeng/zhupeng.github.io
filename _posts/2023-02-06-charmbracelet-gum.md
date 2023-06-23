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

![](https://camo.githubusercontent.com/91a2a754c42c4922be49ba009983e8734befd3ae1c415cfe17d0878cdea5b0f4/68747470733a2f2f73747566662e636861726d2e73682f67756d2f66696c7465722e676966)

2、确认按钮输入
![](https://camo.githubusercontent.com/e55a3f3371335e08446eac4192c9749f6f01eae9f30654360774e29b26705331/68747470733a2f2f73747566662e636861726d2e73682f67756d2f636f6d6d69745f322e676966)

3、支持文件夹浏览

![](https://camo.githubusercontent.com/596a0b5e2015dfec7a8ef761192a0297a13d653727760fcec6447df65460883f/68747470733a2f2f73747566662e636861726d2e73682f67756d2f66696c652e676966)

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

关注我们，一起探索有意思的开源项目。
