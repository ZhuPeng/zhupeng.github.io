---
layout: post
title: ChatGPT 都能智能回答问题了，问答社区还需要吗？
tags: 问答
---

大家好，又见面了，我是 GitHub 精选君！

问答社区还需不需要呢？我觉得还是需要存在的，毕竟 ChatGPT 语言模型的训练数据很多就来自问答社区，所以数据源头还是很重要的。

今天要给大家推荐一个 GitHub 开源项目 answerdev/answer，该项目在 GitHub 有超过 6.0k Star，用一句话介绍该项目就是：“An open-source knowledge-based community software. You can use it quickly to build Q&A community for your products, customers, teams, and more.”，支持快速构建问答社区网站的开源工具。以下是对应的 UI 界面：

![](https://raw.githubusercontent.com/answerdev/answer/master/docs/img/logo.svg)

![](https://raw.githubusercontent.com/answerdev/answer/main/docs/img/screenshot.png)

answer 是一个开源的问答系统。它基于 Go 开发，使用了机器学习技术来匹配问题和答案。

这个系统可以帮助你快速构建一个问答系统，用于提供客户服务、知识库管理等场景。系统支持多种输入输出方式，包括命令行、HTTP API、自然语言处理等，可以方便地集成到各种应用中。以下是 answer 项目的核心卖点，包括：平台化、组织、集成等特点。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230212193910846.png)

### 如何安装使用

answer 有众多的依赖，推荐使用 docker-compose 启动，使用如下命令即可：

```bash
curl -fsSL https://raw.githubusercontent.com/answerdev/answer/main/docker-compose.yaml | docker compose -p answer -f - up
```

应用启动后根据页面的提示进行配置即可完成安装，其中包括：1、选择语言；2、配置数据库；3、创建配置文件；4、填写应用的基础信息等。


更多项目详情请查看如下链接。

开源项目地址：https://github.com/answerdev/answer  (文末可点击阅读原文)

开源项目作者：answer

