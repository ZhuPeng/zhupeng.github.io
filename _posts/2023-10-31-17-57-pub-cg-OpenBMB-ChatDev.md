---
layout: post
title: ChatDev - 一个基于大型语言模型 (LLMs) 的虚拟软件公司
tags: 
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在当今的软件开发过程中，我们经常会遇到各种问题，如需求分析、设计、编码、测试、文档编写等环节的复杂性和繁琐性，这些问题往往会影响到软件开发的效率和质量。同时，我们也期望能有一种方式，能够通过自然语言的方式，快速地生成定制化的软件。这就是我们今天要介绍的开源项目 ChatDev 要解决的问题。

GitHub 开源项目 OpenBMB/ChatDev 在 GitHub 有超过 16.0k Star，用一句话介绍该项目就是：“Create Customized Software using Natural Language Idea (through LLM-powered Multi-Agent Collaboration)”。

![](https://github.com/OpenBMB/ChatDev/raw/main/misc/logo1.png)

![](https://raw.githubusercontent.com/OpenBMB/ChatDev/master/misc/intro.png)

###### 项目介绍

ChatDev 是一个基于大型语言模型 (LLMs) 的虚拟软件公司，通过多个智能代理（包括首席执行官、首席产品官、首席技术官、程序员、审查员、测试员、艺术设计师等角色）的协作，实现了一种全新的软件开发方式。

![](https://raw.githubusercontent.com/OpenBMB/ChatDev/master/misc/agentverse.png)

这些代理形成了一个多代理组织结构，他们通过参与专门的功能研讨会，包括设计、编码、测试和文档编写等任务，共同完成软件开发。ChatDev 的主要目标是提供一个易于使用、高度可定制和可扩展的框架，这是研究集体智能的理想场景。

DEMO 视频地址：https://user-images.githubusercontent.com/11889052/263643733-80d01d2f-677b-4399-ad8b-f7af9bb62b72.mp4

###### 如何使用

首先，你需要克隆 GitHub 仓库，命令如下：

```bash
git clone https://github.com/OpenBMB/ChatDev.git
```
然后，确保你有 3.9 或更高版本的 Python 环境。你可以使用以下命令创建并激活此环境，将 ChatDev_conda_env 替换为任意你喜欢的环境名称：
```bash
conda create -n ChatDev_conda_env python=3.9 -y
conda activate ChatDev_conda_env
```
接着，进入到项目目录，安装依赖项即可。

```bash
cd ChatDev
pip3 install -r requirements.txt
```

后续还需要设置 OpenAI 的 API Key 即可开始开发你的软件了。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231111212909368.png)

###### 项目推介

ChatDev 其作者是知名的开源社区 OpenBMB。该项目已经在 2023 年 8 月 17 日发布了 v1.0.0 版本。此外，该项目还支持 Docker 安全执行，支持 Git 版本控制，支持人机交互模式，支持艺术模式等多种功能。如果你是一个对新技术感兴趣的开发者，或者是一个希望提高软件开发效率的团队，我强烈推荐你尝试使用 ChatDev。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231111213142618.png)


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=OpenBMB/ChatDev&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/OpenBMB/ChatDev 

开源项目作者：OpenBMB

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=OpenBMB/ChatDev)

关注我们，一起探索有意思的开源项目。

