---
layout: post
title: 可以本地运行的命令行 AI 工具
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在我们进行编程的过程中，可能会遇到各种问题，比如对于某些命令行的使用不熟悉，或是在编码过程中需要生成某种复杂的一行代码，这些过程都需要我们花费大量的时间与精力。而随着大模型的出现，我们希望通过智能化的方式，解决这些问题，提升我们的编程效率。

今天要给大家推荐一个 GitHub 开源项目 yusufcanb/tlm，该项目在 GitHub 有差不多 1000 Star，一句话介绍该项目：Local CLI Copilot, powered by CodeLLaMa.

![](https://raw.githubusercontent.com/yusufcanb/tlm/master/./assets/suggest.gif)

###### 项目介绍

tlm 是一个本地的命令行界面 ( CLI ) 工具，它依托于强大的 [CodeLLaMa](https://ai.meta.com/blog/code-llama-large-language-model-coding/) ，无需 API Key（订阅），不需要网络连接，只需你的本地电脑就可以给你提供最佳的命令行建议。其主要特性包括：跨平台兼容，可在 macOS、Linux 和 Windows 上运行；支持自动检测 shell；能生成一行简洁代码以及命令的说明。

![](https://raw.githubusercontent.com/yusufcanb/tlm/master/./assets/explain.gif)

###### 如何使用

首先，需要安装 [Ollama](https://ollama.com/) 下载必需的模型。然后，项目提供了两种实现方式：通过安装脚本或是直接通过 Go 命令进行安装。以 Linux 和 macOS 为例，可以通过以下命令进行安装：

```bash
curl -fsSL https://raw.githubusercontent.com/yusufcanb/tlm/release/1.1/install.sh | sudo bash -E
```

安装完成后，可以运行 `tlm help` 命令来确认是否安装成功。

###### 项目推介

tlm 项目解决了开发者在编程过程中面临的一些挑战，使命令行的使用变得更为便捷。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=yusufcanb/tlm&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/yusufcanb/tlm 

开源项目作者：yusufcanb

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=yusufcanb/tlm)

关注我们，一起探索有意思的开源项目。

