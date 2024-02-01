---
layout: post
title: DB-GPT - 一个用于数据库领域的大型语言模型开源框架
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在数据 3.0 的时代，全球都在积极寻求利用大型语言模型（LLMs）来改善现有的工作流程，而软件工程是其中最为火热的一个领域。在软件研发过程中，数据库是最经常使用并且开发人员需要经常与之交互的工具，如何使得开发人员能够更快更好的与数据进行交互和数据分析，能够极大的提升软件研发的效率。但这一过程往往需要大量的代码编写和系统优化，在这个背景下，如何借助大语言模型的优势，使用最少的代码实现和数据库之间的高效互动应用成为了一大探索方向。

今天要给大家推荐一个 GitHub 开源项目 eosphoros-ai/DB-GPT，该项目在 GitHub 有超过 8.3k Star，用一句话介绍该项目就是：“Revolutionizing Database Interactions with Private LLM Technology”。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240108223822616.png)

![](https://github.com/eosphoros-ai/DB-GPT/assets/13723926/1f77079e-d018-4eee-982b-9b6a66bf1063)

###### 项目介绍

DB-GPT 是一个用于数据库领域的大型语言模型开源框架，包括 SMMF (服务导向的多模型管理框架)， Text2SQL 微调技术，RAG 框架及其优化技术，数据驱动的代理框架协作以及生成式商业智能等技术。DB-GPT 简化了基于大语言模型和数据库的各种应用程序的创建，使企业和开发者可以以最少的编码创建定制的应用程序，充分利用大型语言模型以及数据库的优势。

以下是 DB-GPT 项目的架构图：

![](https://raw.githubusercontent.com/eosphoros-ai/DB-GPT/master/./assets/DB-GPT.png)

以下是 DB-GPT 的一个使用 DEMO：

![](https://github.com/eosphoros-ai/DB-GPT/assets/13723926/3044e83b-a71e-41fe-a1e2-98e479e0ab59)

###### 如何使用

你需要查看**使用教程** (http://docs.dbgpt.site/docs/overview) 来了解如何进行安装和初次使用。然后，你还可以了解一下应用案例和调试方案，来进一步了解如何使用 DB-GPT。这里我给你简单介绍一下安装的步骤，具体安装介绍请点击链接**Install** (http://docs.dbgpt.site/docs/installation) 来进行查看。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240108224350875.png)

我们来看下最简单的安装方式，docker-compose，在代码仓库里面能够查看到配置文件如下：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240108224617122.png)

运行 docker compose up -d 即可快速启动，然后通过 docker logs db-gpt-webserver-1 -f 查看日志。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240108224640601.png)

###### 项目推介

DB-GPT 项目是一个非常活跃的开源项目，由 Eosphoros AI 团队开发并维护。DB-GPT 支持比较多的 LLM 模型，包括开源和 API 代理的 LLMs，如 LLaMA/LLaMA2、Baichuan、ChatGLM、Wenxin 等，同时，DB-GPT 项目还有一系列高效的数据处理和问答系统，可以平滑地对接多种数据源，从而提高开发和查询效率。因此，我非常推荐你们尝试使用 DB-GPT。以下是项目的 RoadMap：

![](https://raw.githubusercontent.com/eosphoros-ai/DB-GPT/master/./assets/roadmap.jpg)


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=eosphoros-ai/DB-GPT&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/eosphoros-ai/DB-GPT 

开源项目作者：eosphoros-ai

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=eosphoros-ai/DB-GPT)

关注我们，一起探索有意思的开源项目。

