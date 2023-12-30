---
layout: post
title: Waveny - 专为模拟吉他而设计的放大器和效果器
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在现今的音乐创作环节中，吉他音色和效果器的应用极大的丰富了音乐表达的形式和内容。然而，实际录音环境及设备对于大多数创作者来说无疑增加了创作难度和成本，如何在不影响音效质量的前提下，实现更便携、更低成本的吉他效果，你有什么办法没有？

今天要给大家推荐一个 GitHub 开源项目 nlpodyssey/waveny，该项目在 GitHub 有差不多 1000 Star，用一句话介绍该项目就是：“Emulate guitar amps and pedals with deep learning, in Go.”。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231217221507606.png)

###### 项目介绍

Waveny 是一个用 Go 语言编写的库和命令行工具，专为模拟吉他放大器和效果器，项目是通过深度学习模型来实现的。项目的设计灵感来源于 Neural Amp Modeler（NAM），并将其相关库进行了改编。Waveny 目前主要功能为通过深度学习模型实现吉他音箱和效果器的模拟输出，功能强大但使用简便。

###### 如何使用

可以直接通过 `go build ./cmd/waveny` 或 `go run ./cmd/waveny` 构建和运行列出的命令，然后按照 `waveny COMMAND [arguments...]` 的格式进行具体的操作。例如，你可以通过命令 `waveny train -config path/to/wavenet.json -input path/to/v3_0_0.wav -target path/to/v3_0_0_reamped.wav -out path/to/output-folder/` 来训练新的 WaveNet 模型。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231217221738744.png)

###### 项目推介

Waveny 的开发进度虽然正处于早期阶段，但已经有明确的发展规划，这个项目是由 Go 语言实现的对吉他效果器和音箱的深度学习模拟，这在技术上具有一定的难度，但由于其对音质处理的优秀特性，已经探索出其在音乐创作领域中的可能。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=nlpodyssey/waveny&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/nlpodyssey/waveny 

开源项目作者：nlpodyssey

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=nlpodyssey/waveny)

关注我们，一起探索有意思的开源项目。

