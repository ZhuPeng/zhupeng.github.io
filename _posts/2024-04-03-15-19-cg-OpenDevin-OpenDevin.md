---
layout: post
title: GitHub 开源项目 OpenDevin/OpenDevin 介绍，🐚 OpenDevin: Code Less, Make More
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 OpenDevin/OpenDevin，该项目在 GitHub 有超过 16.7k Star，一句话介绍该项目：🐚 OpenDevin: Code Less, Make More




![](https://raw.githubusercontent.com/OpenDevin/OpenDevin/master/./logo.png)



背景介绍：在过去的几年里，我们在职业编程环境中遇到了很多问题。工作的复杂性增加，编程任务变得更加复杂，而且需要长时间的专注和仔细的细节管理。我们时常涉足于代码编写、代码审查、代码调试和运行测试等多个步骤，这无疑增加了我们的工作强度。而且，我们通常需要在 shell、代码编辑器和网络浏览器等不同的工具之间切换，这使得任务变得极为繁琐。若能有个工具帮助我们解决一些看似复杂的编程任务，那将对我们大有裨益。

项目介绍：OpenDevin 是一个开源项目，其目标是复制和改进 Devin，一个能够执行复杂工程任务并能够与用户积极协作的自主 AI 软件工程师。Devin 利用 shell、代码编辑器和网络浏览器等工具，展示了 LLM(长期记忆模型)在软件开发中的潜力。我们的目标是探索和扩展 Devin 的能力，确定优点和改进空间，以推动开放源代码模型的进步。项目目前的几个主要工作方向包括：
1. UI：开发用户友好的界面，包括聊天界面，显示命令的 shell 和网络浏览器。
2. 架构：构建出稳定的框架，强壮的后端能够读取、写入和运行简单的命令。
3. Agent 的能力：提升 Agent 的生成 bash 脚本、运行测试和执行其他软件工程任务的能力。
4. 评估：建立符合 Devin 评估准则的最小化评估管道。

如何使用：首先，您需要满足以下系统需求：Linux，Mac OS 或 Windows 上的 WSL、Docker、Python 3.11或更高版本、NodeJS 14.8 或更高版本。其次，用以下命令构建项目：

```bash
make build
```
然后，设置环境：

```bash
make setup-config
```
最后，运行应用：

```bash
make run
```
如果您需要，在后端和前端之间单独运行，那么可以使用以下命令：
```bash
make start-backend
make start-frontend
```
更多的帮助命令可以如下操作：
```bash
make help
```

项目推介：OpenDevin 是一个活跃的开源项目，它旨在开源社区的支持下，复制、增强和超越原始的 Devin 模型。项目团队正在积极开展工作，提供友好的用户界面，稳定的框架，提升 Agent 的能力，建立评估管道等。您可以通过访问项目主页浏览我们的进度，并且项目已经发布了 alpha 版本供用户体验。从长期来看，我们相信这个项目会对我们的编程环境产生显著影响，并可能开创出新的编程范式。如果您对此有兴趣，那么请加入我们的社区，一起参与这个项目，我们期待看到您的贡献！


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=OpenDevin/OpenDevin&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/OpenDevin/OpenDevin 

开源项目作者：OpenDevin

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=OpenDevin/OpenDevin)

关注我们，一起探索有意思的开源项目。

