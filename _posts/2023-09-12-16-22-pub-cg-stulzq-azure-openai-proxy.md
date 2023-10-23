---
layout: post
title: azure-openai-proxy - 一个将 OpenAI 官方 API 转换为 Azure API 的代理工具
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在人工智能领域，我们常常需要使用 OpenAI 的官方 API 来进行模型调用，但是在某些情况下，我们可能需要将这些请求转发到 Azure OpenAI API。这样的需求可能源于各种原因，比如 Azure 的服务可能在特定地区有更好的访问速度，或者用户已经在 Azure 上有了大量的资源。这就需要我们有一个工具，能够将 OpenAI 的官方 API 请求转换为 Azure OpenAI API 请求。

今天要给大家推荐一个 GitHub 开源项目 stulzq/azure-openai-proxy，该项目在 GitHub 有超过 883 Star，用一句话介绍该项目就是：“Azure OpenAI Service Proxy. Convert OpenAI official API request to Azure OpenAI API request. Support GPT-4,Embeddings.”。

![](https://raw.githubusercontent.com/stulzq/azure-openai-proxy/master/assets/images/aoai-proxy.jpg)

###### 项目介绍

azure-openai-proxy 是一个能够将 OpenAI 官方 API 请求转换为 Azure OpenAI API 请求的服务代理。它支持所有的模型，包括 GPT-4 和 Embeddings，而且不需要做任何的改造工作。这个项目已经验证过可以支持的项目包括：chatgpt-web、chatbox、langchain 和 ChatGPT-Next-Web。

###### 如何使用

首先，你需要从 Azure OpenAI 获取一些必要的信息，包括 AZURE_OPENAI_ENDPOINT、AZURE_OPENAI_API_VER 和 AZURE_OPENAI_MODEL_MAPPER。然后，你可以使用 Docker 来运行这个项目，只需要设置好环境变量或者通过配置文件来设置这些参数即可。在运行起来之后，你就可以通过 POST 请求来调用 API 了。

Azure 获取 Key：

![](https://raw.githubusercontent.com/stulzq/azure-openai-proxy/master/assets/images/endpoint.png)

如果你想拿 ChatGPT-Next-Web 来做测试的话，以下是一个对应的 Docker Compose 启动配置。

````yaml
version: '3'

services:
  chatgpt-web:
    image: chenzhaoyu94/chatgpt-web
    ports:
      - 3002:3002
    environment:
      OPENAI_API_KEY: <Azure OpenAI API Key>
      OPENAI_API_BASE_URL: http://azure-openai:8080
      # OPENAI_API_MODEL: gpt-4
      AUTH_SECRET_KEY: ""
      MAX_REQUEST_PER_HOUR: 1000
      TIMEOUT_MS: 60000
    depends_on:
      - azure-openai
    links:
      - azure-openai
    networks:
      - chatgpt-ns

  azure-openai:
    image: stulzq/azure-openai-proxy
    ports:
      - 8080:8080
    environment:
      AZURE_OPENAI_ENDPOINT: <Azure OpenAI API Endpoint>
      AZURE_OPENAI_MODEL_MAPPER: <Azure OpenAI API Deployment Mapper>
      AZURE_OPENAI_API_VER: 2023-07-01-preview
    networks:
      - chatgpt-ns

networks:
  chatgpt-ns:
    driver: bridge
````

运行 docker compose up -d 之后，则可以访问到如下页面。

![](https://raw.githubusercontent.com/stulzq/azure-openai-proxy/master/assets/images/chatgpt-web.png)

###### 项目推介

azure-openai-proxy 是一个非常实用的工具，它可以帮助你更方便地在 Azure 上使用 OpenAI 的模型。项目的开发者 stulzq 是一个经验丰富的开发者，他在 GitHub 上有很多其他的开源项目，这个项目也是他的一次尝试，希望能够帮助更多的人。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231013222948961.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=stulzq/azure-openai-proxy&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/stulzq/azure-openai-proxy 

开源项目作者：stulzq

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=stulzq/azure-openai-proxy)

关注我们，一起探索有意思的开源项目。