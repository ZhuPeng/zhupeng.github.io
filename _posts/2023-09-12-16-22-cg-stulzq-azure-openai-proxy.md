---
layout: post
title: GitHub 开源项目 stulzq/azure-openai-proxy 介绍，Azure OpenAI Service Proxy. Convert OpenAI official API request to Azure OpenAI API request. Support GPT-4,Embeddings.
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 stulzq/azure-openai-proxy，该项目在 GitHub 有超过 883 Star，用一句话介绍该项目就是：“Azure OpenAI Service Proxy. Convert OpenAI official API request to Azure OpenAI API request. Support GPT-4,Embeddings.”。


![aoai-proxy.jpg](https://raw.githubusercontent.com/stulzq/azure-openai-proxy/master/assets/images/aoai-proxy.jpg)
![Screenshot of the overview UI for an OpenAI Resource in the Azure portal with the endpoint & access keys location circled in red.](https://raw.githubusercontent.com/stulzq/azure-openai-proxy/master/assets/images/endpoint.png)
![chatgpt-web](https://raw.githubusercontent.com/stulzq/azure-openai-proxy/master/assets/images/chatgpt-web.png)









背景介绍：
在人工智能领域，我们常常需要使用 OpenAI 的官方 API 来进行模型调用，但是在某些情况下，我们可能需要将这些请求转发到 Azure OpenAI API。这样的需求可能源于各种原因，比如 Azure 的服务可能在特定地区有更好的访问速度，或者用户已经在 Azure 上有了大量的资源。这就需要我们有一个工具，能够将 OpenAI 的官方 API 请求转换为 Azure OpenAI API 请求。

项目介绍：
"azure-openai-proxy" 是一个能够将 OpenAI 官方 API 请求转换为 Azure OpenAI API 请求的服务代理。它支持所有的模型，包括 GPT-4 和 Embeddings。这个项目已经验证过可以支持的项目包括：chatgpt-web、chatbox 和 langchain。

如何使用：
首先，你需要从 Azure OpenAI 获取一些必要的信息，包括 AZURE_OPENAI_ENDPOINT、AZURE_OPENAI_API_VER 和 AZURE_OPENAI_MODEL_MAPPER。然后，你可以使用 Docker 来运行这个项目，只需要设置好环境变量或者通过配置文件来设置这些参数即可。在运行起来之后，你就可以通过 POST 请求来调用 API 了。

项目推介：
"azure-openai-proxy" 是一个非常实用的工具，它可以帮助你更方便地在 Azure 上使用 OpenAI 的模型。项目的开发者 stulzq 是一个经验丰富的开发者，他在 GitHub 上有很多其他的开源项目，这个项目也是他的一次尝试，希望能够帮助更多的人。虽然这个项目目前还在开发中，但是已经有一些项目已经验证过可以使用，所以你完全可以放心地使用。如果你在使用过程中遇到任何问题，也可以通过 GitHub 提交问题，开发者会在第一时间进行回应。







以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=stulzq/azure-openai-proxy&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/stulzq/azure-openai-proxy 

开源项目作者：stulzq

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=stulzq/azure-openai-proxy)

关注我们，一起探索有意思的开源项目。