---
layout: post
title: 本地运行和管理大模型的工具
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 项目背景

在当前具有高速发展的人工智能和机器学习领域，语言模型正朝着更大、更复杂的方向发展。然而，随着模型规模的不断扩大，这样的模型往往需要大量的计算资源来运行，并且需要专业化的技术知识来进行管理和维护。这使得很多开发者或研究者面临困扰，如何在本地运行和管理这些大型语言模型呢？

今天要给大家推荐一个 GitHub 开源项目 ollama/ollama，该项目在 GitHub 有超过 34.7k Star，用一句话介绍该项目就是：Get up and running with Llama 2, Mistral, and other large language models locally.


![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240311224833584.png)

###### 项目介绍

Ollama 是一个用于在本地运行和管理大型语言模型的开源项目，Ollama 提供了一整套简洁易用的 API ，用于创建、运行和管理各种语言模型。同时，提供了一系列预构建的模型库，这些模型可以被直接下载并运行，覆盖了从 Llama 到 Mistral 的各种语言模型。不管你是想使用诸如 Llama 2, Mistral 这样的顶级模型，还是希望快速部署和测试自己的模型，Ollama 都能提供方便的支持。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240311224954972.png)

###### 如何使用

安装 Ollama 非常简单，只需要使用下列命令即可在 macOS，Linux 或者是 Windows 中安装：`curl -fsSL https://ollama.ai/install.sh | sh` 。同时，Ollama 还支持 Docker 镜像的方式安装和使用。

要运行预构建的模型，只需要输入 `ollama run llama2` 即可。Ollama 还支持模型的导入，只需要创建一个 `Modelfile` 文件并按照规定格式描述模型，就可以使用 `ollama create model_name -f Modelfile` 将你的模型导入至 Ollama 中，并用 `ollama run model_name` 运行你的模型。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240311225214641.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=ollama/ollama&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/ollama/ollama 

开源项目作者：ollama

开源协议：MIT License

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=ollama/ollama)

关注我们，一起探索有意思的开源项目。

