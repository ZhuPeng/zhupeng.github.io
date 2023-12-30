---
layout: post
title: XAgent - 大型语言模型（LLM）驱动的自主代理项目，旨在自动解决各种复杂任务
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在当前复杂的任务处理中，我们通常会遇到需要自动化处理各种各样任务的问题，这些问题可能涉及到任务的管理、求解方案、以及与工作环境的交互等，每一个环节分别需要不同的技术融合，在处理过程中需要耗费大量的人力和物力。这时，如果有一款能够安全、自动地进行各类任务处理的工具，无疑将会大大地提高工作的效率。 

今天要给大家推荐一个 GitHub 开源项目 OpenBMB/XAgent，该项目在 GitHub 有超过 5.2k Star，用一句话介绍该项目就是：“An Autonomous LLM Agent for Complex Task Solving”。

![](https://raw.githubusercontent.com/OpenBMB/XAgent/master/assets/readme/overview.png)

###### 项目介绍

XAgent 是一个开源的实验性大型语言模型（LLM）驱动的自主代理项目，能够自动解决各种任务。这个项目的主要设计目的是创建一种普适性的智能代理，能够应用于广泛的任务中。 

XAgent 主要有以下特点：

- 自主性：XAgent 能够在无人参与的情况下自行解决多种任务。
- 安全性：XAgent 被设计为在 docker 容器内运行，以此确保所有的动作都在安全的环境中进行，避免意外情况的发生。
- 可扩展性：XAgent 的设计具有很强的扩展性，可以轻松添加新工具，提升代理的能力，甚至添加新的代理。
- GUI：XAgent 为用户提供了用户友好的操作界面，用户也可以通过命令行接口来进行与代理的交互。
- 与人协作：XAgent 在遇到复杂任务时不仅能够按照你的指示来执行任务，而且在遇到困难的时候也可以向你寻求帮助。

以下是项目的一个使用 DEMO：

![](https://raw.githubusercontent.com/OpenBMB/XAgent/master/assets/readme/demo.gif)

大家可能会想到对标项目 AutoGPT，以下是两个项目的对比数据：

![](https://raw.githubusercontent.com/OpenBMB/XAgent/master/assets/readme/agent_comparison.png)

###### 如何使用

在使用 XAgent 之前，你首先需要安装 docker 和 docker-compose，然后构建 ToolServer 的 docker 镜像并运行该容器，运行命令如下：

```bash
docker-compose up --build
```

在启动 ToolServer 之后，接着就可以运行 XAgent。 按如下步骤进行：

1、安装需要的库文件(需要 Python 版本 >= 3.10)

```bash
pip install -r requirements.txt
```

2、配置 XAgent:
在 `assets/config.yml` 中对 XAgent 进行配置

3、运行 XAgent

```bash
python run.py --task "put your task here" --config_file "assets/config.yml"
```

以下是 XAgent 解决一个具体问题的大致处理流程：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231219214105363.png)

###### 项目推介

XAgent 所实现的自动处理任务是一大亮点，它体现了技术在智能任务处理方面的可能性。项目目前的状态是在积极的开发和改善中，其已经获得了一定的关注度。特别是这个项目的开发者 OpenBMB 在 GitHub 上是个非常活跃的开发者，他们有很多优秀的项目，在行业内也有一定的知名度。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231219214317497.png)


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=OpenBMB/XAgent&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/OpenBMB/XAgent 

开源项目作者：OpenBMB

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=OpenBMB/XAgent)

关注我们，一起探索有意思的开源项目。

