---
layout: post
title: 开源的企业级问答系统
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在当前大数据时代，充斥着海量的数据，当我们需要获取某些信息时，我们必须在多个不同的源头进行检索。这是一个非常耗时且低效的过程，使我们不得不将部分时间和精力用于查找信息，而非专注于解决实际问题。在这种情况下，我们需要一种工具，能够帮助我们针对性地获取数据，最好是能以人类的自然语言提问，内容源可以是我们日常工作中常用的私人资源，如 Slack、GitHub、Confluence 等。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240608221213237.png)

今天要给大家推荐一个 GitHub 开源项目 danswer，该项目在 GitHub 有超过 9.6k Star，一句话介绍该项目：Ask Questions in natural language and get Answers backed by private sources. Connects to tools like Slack, GitHub, Confluence, etc.


![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240608221646329.png)

###### 项目介绍

Danswer 是一个开源的企业级问答系统，用户可以用自然语言向系统提问，Danswer 会从你提供的私人数据源中查找答案。这些源头可以是 Slack、GitHub、Confluence 等多种常见的工具。项目提供了直接的 QA 功能以及由生成式 AI 模型为支撑的聊天功能。设计上，它采用最新的 NLP 模型实现智能文档检索，并有能力从自然语言中自动提取时间或资源过滤信息。

演示视频如下所示：

<video src="/Users/zhupeng/Downloads/292074827-563be14c-9304-47b5-bf0a-9049c2b6f410.mp4"></video>
目前支持如下数据源：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240125224557627.png)

###### 如何使用

Danswer 提供了完备的 Web UI，你还可以将 Danswer 插入到现有的 Slack 工作流中，更多的集成方式还在开发中。Danswer 支持本地测试和一键部署到虚拟机上的功能，只需要一个 `docker compose` 命令就可以完成部署。同时，项目也支持部署在 Kubernetes 上。

```bash
git clone https://github.com/danswer-ai/danswer.git
cd danswer/deployment/docker_compose
docker compose -f docker-compose.dev.yml -p danswer-stack up -d --pull always --force-recreate
```

启动后访问 localhost:3000 即可。

###### 项目推介

Danswer 项目目前正在积极的开发维护中，参与的开发者非常活跃，这就保证了项目的稳定性和前沿性。此外，Danswer 的这种将数据检索、问答、管理等一体化的设计，无疑是提高工作效率的一种极好方式。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240125224804246.png)


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=danswer-ai/danswer&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/danswer-ai/danswer 

开源项目作者：danswer-ai

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=danswer-ai/danswer)

关注我们，一起探索有意思的开源项目。

