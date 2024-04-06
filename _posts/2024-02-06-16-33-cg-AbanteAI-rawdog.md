---
layout: post
title: 基于自然语言描述的命令行运维工具
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

为我们的日常工作带来便利是开源项目的重要意义之一。每个人都会遇到需要繁琐手动操作的问题，比如统计 Home 目录中Git 仓库的数量和磁盘占用，查看某个文件夹中所有 CSV 文件的 pd.describe() 结果，查询当前活动的端口以及属于 Google 的端口，并关闭它们等等。这些看似琐碎的任务如果都需要手动去写命令需要耗费不少时间。

今天要给大家推荐一个 GitHub 开源项目 AbanteAI/rawdog，该项目在 GitHub 有超过 1.7k Star，一句话介绍该项目：Generate and auto-execute Python scripts in the cli.

<video src="/Users/zhupeng/Downloads/301779248-1417a927-58c1-424f-90a8-e8e63875dcda.mp4"></video>

###### 项目介绍

Rawdog（Recursive Augmentation With Deterministic Output Generations）是一个命令行助手，它可以自动生成自然语言描述的命令相关的 Python 脚本，并自动执行。它能自我选择上下文，通过运行脚本打印信息，将输出增添至对话中，然后再次调用自己。并且它也可以按照 README 文件中的指示来设定仓库，或检查所有的 CSV 文件是否能合并等。该工具强大实用，但请注意按照指示操作，以防意外情况的发生。

###### 如何使用

要使用 Rawdog，你只需通过 pip 进行安装：

```
pip install rawdog-ai
```
如果没有找到 API 密钥，你将被提示输入。然后，选择一种交互模式，以下是两种交互模式：

1、直接模式：执行单个提醒并关闭

```
rawdog Plot the size of all the files and directories in cwd
```
2、对话模式：进行反复交互，直至你关闭。Rawdog 可以看到它的脚本和输出。

```
rawdog
>>> What can I do for you? (Ctrl-C to exit)
>>> > |
```
模型选择：Rawdog 使用 gpt-4 作为默认的 `litellm` 补全模型，你可以修改 `~/.rawdog/config.yaml` 来调整模型或指向其他提供者。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=AbanteAI/rawdog&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/AbanteAI/rawdog 

开源项目作者：AbanteAI

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=AbanteAI/rawdog)

关注我们，一起探索有意思的开源项目。

