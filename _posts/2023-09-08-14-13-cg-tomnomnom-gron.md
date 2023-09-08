---
layout: post
title: GitHub 开源项目 tomnomnom/gron 介绍，Make JSON greppable!
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 tomnomnom/gron，该项目在 GitHub 有超过 12.4k Star，用一句话介绍该项目就是：“Make JSON greppable!”。





1、背景介绍：
在我们日常的开发工作中，经常会遇到需要处理 JSON 数据的情况。JSON 数据的优点是结构清晰，易于理解，但是当我们需要在大量的 JSON 数据中寻找特定的信息时，就会感到非常困扰。传统的 grep 命令虽然可以在文本中搜索特定的字符串，但是对于 JSON 数据的搜索并不友好。这就是我们需要 " gron " 这个项目的原因。

2、项目介绍：
" gron " 是一个开源项目，它的主要功能是将 JSON 数据转化为离散的赋值语句，使得我们可以更容易地使用 grep 命令来搜索我们需要的信息。同时，它还可以显示信息的绝对 '路径' ，使得我们可以更快地定位到信息的位置。此外，" gron " 还可以反向工作，即将过滤后的数据重新转化为 JSON 格式。这对于处理大量的 JSON 数据非常有帮助。

3、如何使用：
" gron " 的安装非常简单，它没有运行时依赖。你可以直接下载 Linux、Mac、Windows 或 FreeBSD 的二进制文件并运行。将二进制文件放在你的 $PATH (例如在 /usr/local/bin) 中，就可以很方便地使用了。如果你是 Mac 用户，你还可以通过 brew 命令来安装 " gron " ：

▶ brew install gron

如果你是 Go 用户，你可以使用 go install 命令来安装：

▶ go install github.com/tomnomnom/gron@latest

使用 " gron " 非常简单，你只需要将 JSON 数据作为输入，然后使用 grep 命令来搜索你需要的信息。例如：

▶ gron "https://api.github.com/repos/tomnomnom/gron/commits?per_page=1" | fgrep "commit.author"

4、项目推介：
" gron " 是一个非常活跃的开源项目，它的作者 Tom Hudson 是一个非常知名的开发者。项目的代码质量非常高，已经有很多知名的公司和开发者在使用。如果你在处理 JSON 数据时遇到了困扰，我强烈推荐你试试 " gron " ，它一定会给你带来很大的帮助。






以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=tomnomnom/gron&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/tomnomnom/gron 

开源项目作者：tomnomnom

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=tomnomnom/gron)

关注我们，一起探索有意思的开源项目。

