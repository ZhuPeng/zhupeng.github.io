---
layout: post
title: GitHub 开源项目 trzsz/trzsz-ssh 介绍，支持 trzsz 的 ssh 客户端，支持搜索和选择服务器进行批量登录，支持记住密码。   An ssh client that supports trzsz, supports searching and selecting servers for batch login.
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 trzsz/trzsz-ssh，该项目在 GitHub 有差不多 1000 Star，用一句话介绍该项目就是：“支持 trzsz 的 ssh 客户端，支持搜索和选择服务器进行批量登录，支持记住密码。   An ssh client that supports trzsz, supports searching and selecting servers for batch login.”。

![tssh登录演示](https://trzsz.github.io/images/tssh.gif)
![tssh批量执行](https://trzsz.github.io/images/batch_ssh.gif)









背景介绍：
在日常的服务器管理工作中，我们常常会遇到一些问题，比如需要批量登录到多台服务器进行操作，但是每次都需要手动输入密码，这无疑增加了我们的工作负担。同时，我们可能还需要在服务器之间传输文件，但是传统的 ssh 文件传输工具速度较慢，无法满足我们的需求。这时候，我们就需要一个能够解决这些问题的工具，而 "trzsz-ssh"（tssh）就是为此而生。

项目介绍：
"trzsz-ssh"（tssh）是一个支持 trzsz 的 ssh 客户端，它不仅支持搜索和选择服务器进行批量登录，还支持记住密码，大大提高了我们的工作效率。此外，tssh 还支持一次选择多台服务器，批量登录，并支持批量执行预先指定的命令，方便我们快速完成批量服务器操作。最重要的是，tssh 内置支持 trzsz 文件传输工具，解决了 Windows 中使用 trzsz ssh 上传速度很慢的问题。在作者的 MacOS 上，使用 trzsz ssh 的上传速度在 10 MB/s 左右，而使用 tssh 可以到 80 MB/s 以上。

如何使用：
tssh 提供了多种安装方式，包括 Windows、MacOS、Ubuntu、Debian、Linux 和 ArchLinux 等操作系统都可以方便地安装 tssh。例如，对于 Windows 用户，可以通过 scoop、winget 或 choco 进行安装，命令如下：
```
scoop install tssh
winget install tssh
choco install tssh
```
对于 MacOS 用户，可以通过 homebrew 进行安装，命令如下：
```
brew update
brew install trzsz-ssh
```
安装完成后，我们就可以享受 tssh 带来的便利了。

项目推介：
"trzsz-ssh"（tssh）是一个非常活跃的开源项目，其作者是一位热衷于开源的程序员，他的其他项目也都得到了广泛的关注和好评。tssh 不仅解决了我们在服务器管理中遇到的问题，还提供了非常高的文件传输速度，这无疑是我们在日常工作中的一个强大助手。因此，我强烈推荐大家试试这个项目，我相信它一定能给你带来惊喜。






以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=trzsz/trzsz-ssh&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/trzsz/trzsz-ssh 

开源项目作者：trzsz

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=trzsz/trzsz-ssh)

关注我们，一起探索有意思的开源项目。

