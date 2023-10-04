---
layout: post
title: GPT Engineer - AI 工程师大行其道，自己动手写代码
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在软件开发过程中，经常需要根据需求编写代码。然而，编写代码是一个耗时且繁琐的任务。GPT Engineer 项目旨在解决这个问题，它基于用户的需求生成完整的代码库。您只需指定您想要构建的内容，AI 会向您询问细节，并最终生成相应的代码。

今天要给大家推荐一个 GitHub 开源项目 AntonOsika/gpt-engineer，该项目在 GitHub 有超过 36.4k Star，用一句话介绍该项目就是：“Specify what you want it to build, the AI asks for clarification, and then builds it.”。

###### 项目介绍

GPT Engineer 项目旨在提供一个易于适应、扩展和让您的代理程序学习您期望的代码外观的工具。它根据提示生成整个代码库。

以下是该项目的设计哲学：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230814225633668.png)

简单概括如下：

- 简单易用
- 灵活且易于添加自定义的 "AI 步骤"，详见 `steps.py`
- 渐进式地构建用户体验，包括：
  1. 高级提示
  2. 向 AI 提供会长期记忆的反馈
- AI 和人类之间快速交互
- 简洁性，所有计算都可以中断并保存到文件系统中

以下是项目的演示视频：Downloads/gpt-engier.mp4

###### 如何使用

选择 **稳定版** 或 **开发版**。

对于 **稳定版** 发行版：
- `pip install gpt-engineer`

对于 **开发版**：
- `git clone https://github.com/AntonOsika/gpt-engineer.git`
- `cd gpt-engineer`
- `pip install -e .`
  - （或者：对于虚拟环境，可以运行 `make install && source venv/bin/activate`）

**另外需要按如下步骤进行设置**

使用 OpenAI API 密钥（最好是具有 GPT-4 访问权限），运行：
- `export OPENAI_API_KEY=[您的 API 密钥]`

Windows 系统的备选设置方法：
- 在命令行中执行 `set OPENAI_API_KEY=[您的 API 密钥]`
- 在 PowerShell 中执行 `$env:OPENAI_API_KEY="[您的 API 密钥]"`

**运行**

- 创建一个空文件夹。如果在存储库内部，可以运行：
  - `cp -r projects/example/ projects/my-new-project`
- 在新文件夹中填写 `prompt` 文件
- 运行 `gpt-engineer projects/my-new-project`
  - （注意，通过 `gpt-engineer --help` 命令可以查看所有可用选项。例如，使用 `--steps use_feedback` 可以改进/修复项目中的代码）

**结果**

检查在 `projects/my-new-project/workspace` 文件夹中生成的文件。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=AntonOsika/gpt-engineer&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/AntonOsika/gpt-engineer 

开源项目作者：AntonOsika

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=AntonOsika/gpt-engineer)

关注我们，一起探索有意思的开源项目。

