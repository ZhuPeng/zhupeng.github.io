---
layout: post
title: GitHub 开源项目 mudler/LocalAI 介绍，:robot: The free, Open Source OpenAI alternative. Self-hosted, community-driven and local-first. Drop-in replacement for OpenAI running on consumer-grade hardware. No GPU required. Runs ggml, gguf, GPTQ, onnx, TF compatible models: llama, llama2, rwkv, whisper, vicuna, koala, cerebras, falcon, dolly, starcoder, and many others
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 mudler/LocalAI，该项目在 GitHub 有超过 13.0k Star，用一句话介绍该项目就是：“:robot: The free, Open Source OpenAI alternative. Self-hosted, community-driven and local-first. Drop-in replacement for OpenAI running on consumer-grade hardware. No GPU required. Runs ggml, gguf, GPTQ, onnx, TF compatible models: llama, llama2, rwkv, whisper, vicuna, koala, cerebras, falcon, dolly, starcoder, and many others”。


![Spectro Cloud logo_600x600px_transparent bg](https://github.com/go-skynet/LocalAI/assets/2420543/68a6f3cb-8a65-4a4d-99b5-6417a8905512)
![](https://github.com/go-skynet/LocalAI/assets/2420543/0966aa2a-166e-4f99-a3e5-6c915fc997dd)
![](https://cdn.buymeacoffee.com/buttons/default-orange.png)



背景介绍：
在 AI 领域的开发中，我们经常会碰到一个问题，即我们需要执行大量的数据推断，但由于缺乏相应的设备和算力，我们无法在本地完成。此外，使用网络服务可能会涉及到数据安全性和隐私性的问题。为了解决这些问题，一个能够在消费级硬件上运行并提供 REST API 的 OpenAI 替代方案出现了，即 LocalAI。

项目介绍：
LocalAI 是一个开源的 OpenAI 替代方案，它可以在本地或企业环境中进行推断，并且只需要消费级硬件。LocalAI 支持多种模型，包括 ggml ，pytorch 等，并且无需 GPU。LocalAI 提供了文本生成（使用 GPT 们）、文本转音频、音频转文本（使用 whisper.cpp），图片生成（使用稳定扩散算法）、OpenAI 函数以及生成用于向量数据库的嵌入等功能。值得一提的是，一旦模型第一次加载后，它会保持在内存中以便进行更快的推断。

如何使用：
关于如何安装和使用 LocalAI，可以参考官方提供的 [“Getting started”](https://localai.io/basics/getting_started/index.html)。此外，还提供了一些使用示例，如使用 Luna-AI Llama 模型。更多的资源，如在 Kubernetes 中安装 LocalAI 和整合 LocalAI 的项目等，也可以在其官方网站上找到。

项目推介：
LocalAI 是由 [Ettore Di Giacinto](https://github.com/mudler/) 创建并维护的，是一个社区驱动的项目，致力于让 AI 更加容易接触和使用，欢迎任何形式的贡献、反馈和合并请求。该项目已经在企业和开源社区中得到了许多实际使用，并已经有一些知名的用户和公司正在使用。例如，在 [“Create a slackbot for teams and OSS projects that answer to documentation”](https://mudler.pm/posts/smart-slackbot-for-teams/) 一文中，作者分享了如何使用 LocalAI 来创建一个能在 Slack 上回答各种文档问题的机器人。在 YouTube 上，还有使用 LocalAI 进行的 [“LocalAI meets k8sgpt”](https://www.youtube.com/watch?v=PKrDNuJ_dfE) 教程。对于关注 AI 领域，或者需要 OpenAI 解决方案的用户来说，LocalAI 是一个值得关注的项目。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=mudler/LocalAI&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/mudler/LocalAI 

开源项目作者：mudler

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=mudler/LocalAI)

关注我们，一起探索有意思的开源项目。

