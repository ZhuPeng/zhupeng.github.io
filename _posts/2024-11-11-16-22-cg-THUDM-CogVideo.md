---
layout: post
title: GitHub 开源项目 THUDM/CogVideo 介绍，text and image to video generation: CogVideoX (2024) and CogVideo (ICLR 2023)
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 THUDM/CogVideo，该项目在 GitHub 有超过 8.9k Star。

![](https://stats.deeptrain.net/repo/THUDM/CogVideo/?theme=light)

一句话介绍该项目：text and image to video generation: CogVideoX (2024) and CogVideo (ICLR 2023)




![High-frame-rate sample](https://raw.githubusercontent.com/THUDM/CogVideo/CogVideo/assets/appendix-sample-highframerate.png)

![Intro images](https://raw.githubusercontent.com/THUDM/CogVideo/CogVideo/assets/intro-image.png)

![](https://raw.githubusercontent.com/THUDM/CogVideo/master/resources/web_demo.png)


###### 项目介绍

### 背景介绍

在数字内容创造的时代，视频内容因其丰富的信息量和强大的表达力，越来越受到人们的青睐。然而，创造高质量的视频内容往往需要大量的时间、专业的软件技能和丰富的创意。对于非专业人士而言，这构成了一个巨大的挑战。尤其是在想要快速将文本或者图像内容转化为视频的场景中，技术和创意的门槛显得尤为突出。如何降低这一门槛，使得更多的人能够轻松创造出高质量的视频内容，成为了业界探索的问题。

### 

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-094708bf237c4ffa1b88c69f597ef34d.png)

项目介绍

**CogVideo & CogVideoX** 项目应运而生，旨在通过先进的深度学习技术，解决从文本和图像到视频生成的问题。该项目基于大规模 Transformer 模型，能够理解文本描述，并将之转化为高质量的视频内容。CogVideoX 更是在此基础上进行了升级，推出了 CogVideoX - 5B 模型，不仅支持更高分辨率的视频生成，还增加了从图像到视频的生成能力，极大的拓宽了应用场景。

此外，该项目还考虑了模型训练和推理过程中的成本问题，发布了一套更为经济的 fine-tuning 框架，使得单卡 4090 GPU 也可以进行模型的微调，进一步降低了使用门槛。

### 如何使用

安装 CogVideoX，首先确保您的 Python 版本在 3.10 到 3.12 之间。然后，通过以下简单的命令安装所需的依赖项：

```
pip install -r requirements.txt
```

使用 CogVideoX 生成视频内容，可以参考 [sat_demo](sat/README.md) 来了解如何使用 SAT 权重进行推理和 fine-tuning。此外，还可以查看 [diffusers_demo](inference/cli_demo.py) 获取更详尽的推理代码说明。

### 项目推介

CogVideo & CogVideoX 项目自开源以来，受到了广泛的关注和好评。尤其是在 ICLR 2023上的展示，进一步证明了其在文本和图像到视频生成领域的领先地位。该项目不仅得到了研究界的认可，同时也吸引了大量的技术爱好者和内容创作者的尝试。通过简单的指令，用户就能够生成与自己想法相匹配的视频内容，极大的释放了创造力。

该项目的活跃开发状态、开源社区的积极参与以及不断增加的功能特性，使其成为了当前最值得关注的开源项目之一。无论是对于研究人员、开发者还是内容创作者来说，CogVideo & CogVideoX 都提供了一个强大的工具，以更低的成本创造出高质量的视频内容。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=THUDM/CogVideo&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/THUDM/CogVideo 

开源项目作者：THUDM

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=THUDM/CogVideo)

关注我们，一起探索有意思的开源项目。

