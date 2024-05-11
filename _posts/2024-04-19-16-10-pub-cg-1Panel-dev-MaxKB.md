---
layout: post
title: 开箱即用，基于大模型的知识库问答系统
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在当今信息化迅速发展的社会，企业和个人面临的信息量越来越庞大，如何快速从这些信息中提取所需的知识变成了一个重大的挑战。特别是对于那些需要快速响应客户查询、提供在线帮助或内部知识共享的企业来说，有效管理和检索大量的文档信息成了他们亟待解决的痛点。传统的文档管理和检索系统往往无法有效处理自然语言查询，且难以灵活地整合到第三方业务系统中，从而影响了运营效率和用户体验。

今天要给大家推荐一个 GitHub 开源项目 1Panel-dev/MaxKB，该项目在 GitHub 有超过 2.8k Star，一句话介绍该项目：基于 LLM 大语言模型的知识库问答系统。开箱即用，支持快速嵌入到第三方业务系统，1Panel 官方出品。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240424225003111.png)

###### 项目介绍

MaxKB 是一个基于 LLM 大语言模型的知识库问答系统，由 1Panel 官方精心打造。它不仅支持开箱即用，快速嵌入到第三方业务系统中，还可以直接上传文档、自动爬取在线文档，并支持文本的自动拆分、向量化处理。MaxKB 的智能问答交互体验极佳，可以自然地理解用户的查询意图，快速从庞杂的信息中找到精确的答案。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240424225049070.png)

更值得一提的是，MaxKB 支持多种大模型，包括但不限于 Llama 2、Llama 3、Azure OpenAI、OpenAI 等，保证了其强大的语言处理能力。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240424225117594.png)

###### 如何使用

使用 MaxKB 非常简便。你可以通过 Docker 快速启动一个 MaxKB 实例：

```
docker run -d --name=maxkb -p 8080:8080 -v ~/.maxkb:/var/lib/postgresql/data 1panel/maxkb
```

启动后，使用默认的用户名(admin)和密码(MaxKB@123..)登录即可开始体验。此外，如果你希望基于本地大模型构建知识库问答系统，还可以通过 1Panel 应用商店快速部署 MaxKB 与 Ollama、Llama 2 的组合，30 分钟内即可上线并嵌入到第三方业务系统中。

###### 项目推介

目前，MaxKB 已经在 [DataEase 小助手](https://dataease.io/docs/v2/) 中得到应用，它基于 MaxKB 构建的智能问答系统已嵌入到 DataEase 产品及在线文档中，展示了 MaxKB 在实际业务中的强大应用能力。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=1Panel-dev/MaxKB&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/1Panel-dev/MaxKB 

开源项目作者：1Panel-dev

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=1Panel-dev/MaxKB)

关注我们，一起探索有意思的开源项目。

