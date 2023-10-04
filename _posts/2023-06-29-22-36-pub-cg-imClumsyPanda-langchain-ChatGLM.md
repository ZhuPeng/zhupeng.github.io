---
layout: post
title: langchain-ChatGLM - 基于本地知识库的 ChatGLM 问答
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在开发过程中，我们经常会遇到需要构建基于本地知识库的问答系统的问题。这种系统需要能够根据用户提供的问题，在本地的知识库中查找并返回相关答案。然而，要实现这样的功能并不容易，涉及到语言模型的选择、知识库的管理以及问答的匹配和检索等核心问题。

今天要给大家推荐一个 GitHub 开源项目 imClumsyPanda/langchain-ChatGLM，该项目在 GitHub 有超过 13.5k Star，用一句话介绍该项目就是：“langchain-ChatGLM, local knowledge based ChatGLM with langchain ｜ 基于本地知识库的 ChatGLM 问答”。

![](https://raw.githubusercontent.com/imClumsyPanda/langchain-ChatGLM/master/img/langchain+chatglm.png)

###### 项目介绍

langchain-ChatGLM 提供了一种基于本地知识库的 ChatGLM（Chat with Generative Language Model）问答系统。该项目结合了langchain和ChatGLM-6B模型的思想，旨在构建一个可灵活应用于中文场景的开源问答系统。通过langchain-ChatGLM，我们可以轻松地将开源的语言模型与本地知识库相结合，实现对中文问答的支持。

![](https://raw.githubusercontent.com/imClumsyPanda/langchain-ChatGLM/master/img/langchain+chatglm2.png)

langchain-ChatGLM的主要功能包括：
- 基于本地知识库的问答：系统可以根据用户的提问，在本地的知识库中进行搜索，并返回相关的答案。
- 多模型支持：项目支持使用不同的语言模型，可以根据需求选择合适的模型进行使用。
- 离线私有化：可以将该问答系统部署在本地环境中，确保数据的安全性和隐私性。

![](https://github.com/chatchat-space/langchain-ChatGLM/raw/master/img/webui_0915_0.png)

WebUI 知识库管理页面：

![](https://github.com/chatchat-space/langchain-ChatGLM/raw/master/img/webui_0915_1.png)

###### 如何使用

要使用langchain-ChatGLM，您可以按照以下步骤进行安装和配置：

1. 克隆或下载项目的代码库。
2. 根据项目README提供的指南，安装必要的依赖项和语言模型。
3. 配置本地知识库，将您的知识数据添加到系统中。
4. 运行项目，并通过提问测试系统的问答功能。

如果您正在寻找一种灵活且功能强大的基于本地知识库的问答系统，langchain-ChatGLM 值得选择。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=imClumsyPanda/langchain-ChatGLM&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/imClumsyPanda/langchain-ChatGLM 

开源项目作者：imClumsyPanda

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=imClumsyPanda/langchain-ChatGLM)

关注我们，一起探索有意思的开源项目。

