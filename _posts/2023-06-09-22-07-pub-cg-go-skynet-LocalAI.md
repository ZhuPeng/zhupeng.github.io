---
layout: post
title: LocalAI: 自托管、社区驱动的本地 OpenAI API 兼容替代方案
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

**1. 背景介绍**

在我们的日常工作中，我们常常遇到需要使用强大的自然语言处理和生成能力的场景，然而，传统的云端 API 服务不仅价格昂贵，而且需要稳定的互联网连接。此外，运行大型语言模型通常需要昂贵的 GPU 资源。针对这些问题，今天推荐开源项目LocalAI。

LocalAI 的目标是提供一个自托管的、社区驱动的本地 OpenAI 兼容 API。我们的解决方案不仅免费开源，而且不需要 GPU，并且可以在消费级硬件上运行。我们致力于将 AI 能力普惠化，让每个人都能轻松地获得强大的语言模型。

![](https://user-images.githubusercontent.com/2420543/233147843-88697415-6dbf-4368-a862-ab217f9f7342.jpeg)

**2. 项目介绍**

LocalAI 在 GitHub 有超过 6.5k Star，LocalAI 是一个满足 OpenAI API 规范的本地推理 REST API。它允许你在本地或本地部署的消费级硬件上运行 LLMs（不仅限于此），支持多个与 ggml 格式兼容的模型系列。与传统的云端 API 不同，LocalAI 不需要 GPU，也不需要互联网连接。

LocalAI 支持多种模型系列，包括音频转录、使用 GPT 进行文本生成以及使用稳定扩散算法进行图像生成（实验性功能）。在首次加载模型后，它将保持模型在内存中，以实现更快的推理速度。

LocalAI 不使用外部命令，而是利用 C++ 绑定进行推理，从而实现更快的速度和更好的性能。

![](https://user-images.githubusercontent.com/2420543/234715439-98d12e03-d3ce-4f94-ab54-2b256808e05e.png)

**3. 如何使用**

安装和使用 LocalAI 非常简单。我们提供了详细的安装指南：https://localai.io/basics/build/index.html，以帮助你快速上手。同时还提供了相关的代码示例供参考：

````bash
git clone https://github.com/go-skynet/LocalAI

cd LocalAI

# (optional) Checkout a specific LocalAI tag
# git checkout -b build <TAG>

# copy your models to models/
cp your-model.bin models/

# (optional) Edit the .env file to set things like context size and threads
# vim .env

# start with docker-compose
docker-compose up -d --pull always
# or you can build the images with:
# docker-compose up -d --build

# Now API is accessible at localhost:8080
curl http://localhost:8080/v1/models
# {"object":"list","data":[{"id":"your-model.bin","object":"model"}]}

curl http://localhost:8080/v1/completions -H "Content-Type: application/json" -d '{
     "model": "your-model.bin",            
     "prompt": "A long time ago in a galaxy far, far away",
     "temperature": 0.7
   }'
````

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=go-skynet/LocalAI&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/go-skynet/LocalAI 

开源项目作者：go-skynet

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=go-skynet/LocalAI)

关注我们，一起探索有意思的开源项目。

