---
layout: post
title: Go 实现的 llama 模型调试与推理库
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

大家都喜欢大而复杂的模型，如 GPT，但是这些模型大多需要 GPU 集群来完成运算，花费不菲。而且，在编程语言方面，我们经常需要在高性能和易用性之间作出取舍，例如 C++ 具有高性能，但其底层性质使其难以推广。如果你也在烦恼这样的问题，那么 Llama.go 项目或许会是你的选择。

今天要给大家推荐一个 GitHub 开源项目 gotzmann/llama.go，该项目在 GitHub 有超过 1.1k Star，用一句话介绍该项目就是：“llama.go is like llama.cpp in pure Golang!”。


![](https://raw.githubusercontent.com/gotzmann/llama.go/master/./assets/images/terminal.png?raw=true)

###### 项目介绍

Llama.go 是基于 Go 语言的开源项目，它与 llama.cpp 有相同的设计理念，关注性能和优雅性，同样以 Go 语言重新实现。相比于 C++ ， Go 语言更易理解和使用。在 Llama.go 中，你不需要拥有繁多的硬件就可以在本地实现对大型 GPT 模型的理解和模拟。此外，它还充分利用 Go 语言的多线程和消息传递特性来提高性能。

Llama.go 项目还规划了很多功能特性，包括对多种操作系统的兼容性，提供稳定版本供 ML 极客使用，内存使用和 GC 优化，服务器模式的引入以及开箱即用的模型等。此外，对于进一步的功能开发，如支持更大的模型，对于流行 LLaMA 家族模型的支持，支持开放式的模型等，也在其开发路径中。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240306224304339.png)

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240306224324795.png)

###### 如何使用

首先，下载模型：
LLaMA-7B: llama-7b-fp32.bin  https://nogpu.com/llama-7b-fp32.bin
LLaMA-13B: llama-13b-fp32.bin   https://nogpu.com/llama-13b-fp32.bin

接着，可以自己编译生成二进制文件，或者可以根据系统不同下载已经生成的文件。然后你可以运行以下命令测试：

```shell
llama-go-v1.4.0-macos \
    --model ~/models/llama-7b-fp32.bin \
    --prompt "Why Golang is so popular?" \
```

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240306224504398.png)


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=gotzmann/llama.go&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/gotzmann/llama.go 

开源项目作者：gotzmann

开源协议：Other

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=gotzmann/llama.go)

关注我们，一起探索有意思的开源项目。

