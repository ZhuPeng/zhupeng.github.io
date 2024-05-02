---
layout: post
title: 开源 RAG 引擎，大模型应用开发必备框架
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在当今信息爆炸的社会，大量的数据充斥着我们的生活。每天都有海量的资料以各种格式生成，如 Word、slides、excel、txt、图片、扫描件、结构化数据、网页等。这些文档在大多数情况下具有复杂并且不规则的格式，使得从中提取关键信息变得极其困难。这种情况下，一个能深入理解文档并提供真实问答能力的系统就显得非常必要。

今天要给大家推荐一个 GitHub 开源项目 infiniflow/ragflow，该项目在 GitHub 有超过 1.2k Star，一句话介绍该项目：RAGFlow is an open-source RAG (Retrieval-Augmented Generation) engine based on deep document understanding.

![](https://raw.githubusercontent.com/infiniflow/ragflow/master/web/src/assets/logo-with-text.png)

###### 项目介绍

[RAGFlow](https://demo.ragflow.io) 是一个开源的基于深入文档理解的 RAG (Retrieval-Augmented Generation) 引擎。它提供了一种简洁的 RAG 工作流，适用于任何规模的业务，结合了大型语言模型 (LLM)，能够提供基于多种复杂格式数据的真实问答能力。

RAGFlow 的主要特点包括：

1、深入理解基于复杂格式的非结构化数据的知识提取，能“在无限令牌的数据海洋中找到针”。

2、提供了丰富且智能的模板选择，支持基于模板的文档切割。

3、通过文本切割的可视化减少错觉，可以快速查看关键引用，支持有依据的答案。

4、兼容多种数据源，包括 Word、slides、excel、txt、图片、扫描件、结构化数据、网页等。

5、提供了自动化和快速上手的 RAG 工作流程，包括可配置的 LLM 和嵌入模型，多种 recall 和融合重排等。

![](https://github.com/infiniflow/ragflow/assets/12318111/d6ac5664-c237-4200-a7c2-a4a00691b485)

###### 如何使用

RAGFlow 的使用主要依赖于 Docker，用户需要首先确认安装了 Docker。在安装好 Docker 后，需要设置 `vm.max_map_count` 的值大于 65535，然后通过克隆项目 url 获取项目源码，并构建预制的 Docker 镜像启动服务器。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240423224852028.png)

服务器成功启动后，通过浏览器输入服务器的 IP 地址即可登录 RAGFlow。此外，用户还可以在 `service_conf.yaml` 中选择需要的 LLM 工厂，并用相应的 API 密钥更新 `API_KEY` 字段。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240423224914401.png)

###### 项目推介

RAGFlow 提供了一种创新的解决方案，用于解决我们在面对海量复杂格式的数据时的问题。RAGFlow 不仅提供了一个强大的问答系统，而且其设计的核心是以人为本，注重用户的使用体验。其智能的设计，如模板的选择，或者可视化的文本切割，都使得用户可以更轻松地从复杂的文档中获取信息。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=infiniflow/ragflow&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/infiniflow/ragflow 

开源项目作者：infiniflow

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=infiniflow/ragflow)

关注我们，一起探索有意思的开源项目。

