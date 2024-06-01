---
layout: post
title: 具备任务拆解能力的终端 AI 编码引擎
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在今天这个快节奏、技术不断革新的时代，开发者在构建复杂且符合实际应用需求的软件时面临着巨大的挑战。其中一个核心痛点是：项目往往涉及多文件和多步骤的复杂任务，这不仅消耗大量时间，还需要紧跟技术的最新发展，即使是经验丰富的开发人员，也可能在新技术面前感到束手无策。此外，高效地管理上下文、迭代开发、以及优化开发流程以减少重复劳动，同样是他们面临的普遍问题。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-5e376d758e94aa64f9a360e18b59c2ce.png)

今天要给大家推荐一个 GitHub 开源项目 plandex，该项目在 GitHub 有超过 9.0k Star，一句话介绍该项目：An AI coding engine for building complex, real-world software with LLMs


![](https://raw.githubusercontent.com/plandex-ai/plandex/master/images/plandex-logo-dark-bg.png)


###### 项目介绍

**Plandex** 是一个开源的、基于终端的 AI 编码引擎，专为处理涉及多文件和多步骤的复杂任务而设计。它能够将大任务分解为更小的子任务，然后逐一实现，直到完成整个项目。Plandex 使用长时间运行的代理来实现这一点，帮助开发者高效地处理待办事项、使用不熟悉的技术、解决开发中遇到的难题，并减少在琐碎事务上的时间花费。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240510225439339.png)

###### 如何使用

使用如下命令可以快速安装：

```bash
curl -sL https://plandex.ai/install.sh | bash
```

或者，你也可以选择手动安装、从源代码构建，甚至在支持 WSL 的 Windows 系统上进行操作。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240510225537739.png)

下面介绍具体的使用步骤：

1、首先，如果你没有 OpenAI 账户，需要注册并生成一个 API 密钥。

2、设置环境变量，包括 `OPENAI_API_KEY` 以及其他可选的设置。

3、进入你的项目目录，运行 `plandex new` 开始一个新的计划。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240510225627296.png)

以下是一个具体的使用示例视频：

<video src="/Users/zhupeng/Downloads/Intro_to_Plandex-vimeo-926634577-hls-fastly_skyfire_sep-642.mp4"></video>
###### 项目推介

无论是个人开发者还是技术企业，都可以从 Plandex 的使用中获得显著的生产力提升，特别是在处理需要跨文件、多步骤的复杂软件开发任务时。同时，Plandex 对新技术的快速适配、对开发流程优化的深入思考，以及通过沙盒环境安全地积累更改，再加上其版本控制系统，都显示了该项目在实际应用中的高可靠性和实用性。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240510225741787.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=plandex-ai/plandex&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/plandex-ai/plandex 

开源项目作者：plandex-ai

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=plandex-ai/plandex)

关注我们，一起探索有意思的开源项目。

