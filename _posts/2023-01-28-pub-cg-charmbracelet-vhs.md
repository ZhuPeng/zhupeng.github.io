---
layout: post
title: 命令行演示 DEMO 视频生成工具
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 charmbracelet/vhs，该项目在 GitHub 有超过 9.3k Star，用一句话介绍该项目就是：“Your CLI home video recorder”，命令行演示 DEMO 视频生成工具。

![](https://user-images.githubusercontent.com/42545625/198402537-12ca2f6c-0779-4eb8-a67c-8db9cb3df13c.png#gh-dark-mode-only)
![](https://stuff.charm.sh/vhs/examples/neofetch_3.gif)

vhs 能够通过写代码的方式生成命令行工具的使用和演示 DEMO，可以是视频也可以是动图。我们先来看一下例子。

![](https://stuff.charm.sh/vhs/examples/demo.gif)

要生成如上效果的代码如下，代码还是非常容易理解的，而且 vhs 支持很多的展示效果，以下也只是做了最基础的展示：

```bash
# Where should we write the GIF?
Output demo.gif

# Set up a 1200x600 terminal with 46px font.
Set FontSize 46
Set Width 1200
Set Height 600

# Type a command in the terminal.
Type "echo 'Welcome to VHS!'"

# Pause for dramatic effect...
Sleep 500ms

# Run the command by pressing enter.
Enter

# Admire the output for a bit.
Sleep 5s
```


### 如何安装使用

vhs 项目是使用 Go 语言编写的，除了使用 Go 原生命令安装意外，还支持非常多的包管理工具进行安装。

```bash
go install github.com/charmbracelet/vhs@latest
```

包管理工具安装，推荐使用 brew install。

```bash
# macOS or Linux
brew install vhs

# macOS (via MacPorts)
sudo port install vhs

# Arch Linux (btw)
pacman -S vhs

# Nix
nix-env -iA nixpkgs.vhs

# Debian/Ubuntu
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://repo.charm.sh/apt/gpg.key | sudo gpg --dearmor -o /etc/apt/keyrings/charm.gpg
echo "deb [signed-by=/etc/apt/keyrings/charm.gpg] https://repo.charm.sh/apt/ * *" | sudo tee /etc/apt/sources.list.d/charm.list
# Install ttyd from https://github.com/tsl0922/ttyd/releases
sudo apt update && sudo apt install vhs ffmpeg

# Fedora/RHEL
echo '[charm]
name=Charm
baseurl=https://repo.charm.sh/yum/
enabled=1
gpgcheck=1
gpgkey=https://repo.charm.sh/yum/gpg.key' | sudo tee /etc/yum.repos.d/charm.repo
# Install ttyd from https://github.com/tsl0922/ttyd/releases
sudo yum install vhs ffmpeg

# Void Linux
sudo xbps-install vhs

# Windows
scoop install vhs
```


### 使用示例 DEMO

安装 vhs 以后，具体的使用非常简单，以下是一个基本流程。

1、新建视频脚本的文件

```bash
vhs new demo.tape
```

2、编辑文件进行流程创作

```bash
# demo.tape 是纯文本文件，可以直接编辑
vim demo.tape
```

以下是一个简单的 DEMO，会在视频中显示 "echo 'Welcome to VHS!'"。

```bash
# Where should we write the GIF?
Output demo.gif

# Set up a 1200x600 terminal with 46px font.
Set FontSize 46
Set Width 1200
Set Height 600

# Type a command in the terminal.
Type "echo 'Welcome to VHS!'"

# Pause for dramatic effect...
Sleep 500ms

# Run the command by pressing enter.
Enter

# Admire the output for a bit.
Sleep 5s
```

3、效果渲染

```bash
vhs < demo.tape
```

vhs 支持了非常多的视频效果，更多请参考 vhs 的 GitHub 项目页面。


如果你是一个命令行工具的开发者或者是需要给其他展示某个命令行工具的使用，非常推荐你使用 vhs 来制作视频。更多项目详情请查看如下链接。

开源项目地址：https://github.com/charmbracelet/vhs  

开源项目作者：charmbracelet



关注我们，一起探索有意思的开源项目。
