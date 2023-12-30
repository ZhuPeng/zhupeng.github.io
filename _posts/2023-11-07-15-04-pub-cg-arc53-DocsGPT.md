---
layout: post
title: DocsGPT - 旨在简化项目文档搜索体验
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在开发过程中，经常会遇到需要查找项目文档中的信息的问题。但是，手动搜索文档耗时且不高效。针对这个问题，项目 DocsGPT 应运而生。DocsGPT 是一个开源的文档助手，通过集成强大的 GPT 模型，开发人员可以轻松地在项目中提问，并获取准确的回答。让我们告别繁琐的手动搜索，让 DocsGPT 帮助您快速找到所需的信息。尝试一下，看看它如何革新您的项目文档体验。

GitHub 开源项目 arc53/DocsGPT 在 GitHub 有超过 13.1k Star，用一句话介绍该项目就是：“GPT-powered chat for documentation, chat with your documents”。

![](https://d3dg1063dc54p9.cloudfront.net/videos/demov3.gif)

###### 项目介绍

DocsGPT 是一款前沿的开源解决方案，旨在简化在项目文档中查找信息的流程。它集成了强大的 GPT 模型，可以帮助开发人员轻松提问关于项目的问题，并获得准确的答案。DocsGPT 解决了传统手动搜索文档耗时且不高效的问题，使得开发人员能够更快地获取所需的信息。

![](https://user-images.githubusercontent.com/17906039/220427472-2644cff4-7666-46a5-819f-fc4a521f63c7.png)

主要设计要点：

- 集成强大的 GPT 模型，确保准确的答案。
- 使用先进的自然语言处理技术，提供智能的文档搜索功能。
- 使用可扩展的架构，方便与其他工具和系统集成。

目前主要优化的开源模型如下：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231202231102145.png)

###### 如何使用

1、安装：

- 在您的计算机上安装 Docker。
- 克隆项目仓库：`git clone https://github.com/arc53/DocsGPT.git`
- 创建 `.env` 文件，并设置环境变量 `API_KEY` 和 `VITE_API_STREAMING`。API_KEY 是您的 OpenAI API 密钥，VITE_API_STREAMING 可以设置为 true 或 false，取决于您是否希望进行流式回答。
- 运行 `./setup.sh` 脚本，安装所有依赖项并下载本地模型或使用 OpenAI。

2、使用：

- 运行 ./run-with-docker-compose.sh
- 在浏览器中访问 http://localhost:5173/。
- 输入您的项目问题，DocsGPT 将返回准确的答案。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=arc53/DocsGPT&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/arc53/DocsGPT 

开源项目作者：arc53

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=arc53/DocsGPT)

关注我们，一起探索有意思的开源项目。

