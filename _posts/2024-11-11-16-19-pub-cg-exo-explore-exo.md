---
layout: post
title: 用日常设备运行自己的 AI 集群
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

AI 作为当下最引人注目的技术之一，其应用场景日益广泛，从自动化家居到智能办公，再到高级研究领域。然而，AI 模型的训练和推理通常需要强大的计算能力，对硬件的要求极高。对于大多数个人用户而言，高价的专业 GPU 往往是难以承受的；同时，随手可得的设备如智能手机、平板电脑、笔记本电脑等，虽然众多但往往未能充分利用。这一切，都在等待一个能够改变现状的解决方案。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241207223337261.png)

今天要给大家推荐一个 GitHub 开源项目 exo-explore，该项目在 GitHub 有超过 17k Star。

![](https://stats.deeptrain.net/repo/exo-explore/exo/?theme=light)

一句话介绍该项目：Run your own AI cluster at home with everyday devices

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241113233759131.png)


###### 项目介绍

**exo** 让人们可以在家中用日常设备运行自己的 AI 集群。忘掉昂贵的 NVIDIA GPU，利用你现有的设备组建一个强大的 GPU 集群：iPhone、iPad、Android、Mac、Linux，几乎任何设备！exo 的这一理念，为广大技术爱好者、研究人员、小型团队提供了前所未有的机会，让他们可以利用手头上看似普通的设备，完成复杂的 AI 模型运行任务。

![](https://github.com/exo-explore/exo/raw/main/docs/exo-screenshot.png)

**exo 的主要功能包括：**

1、广泛的模型支持：支持多种模型，包括 LLaMA、Mistral、LlaVA、Qwen 和 Deepseek 等。

2、动态模型分区：根据当前网络拓扑和可用设备资源，优化模型的分配。

3、自动设备发现：零手动配置，自动发现其他设备。

4、与 ChatGPT 兼容的 API：提供一行代码改变，即可在自己的硬件上运行模型。

5、设备平等：不使用主-从架构，设备之间点对点连接。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241113233920470.png)

###### 如何使用

首先，确保你的设备上安装有 Python>=3.12.0，并根据你的操作系统配置好相应的环境（在 Linux 上可能需要 NVIDIA 驱动、CUDA 和 cuDNN）。

```sh
git clone https://github.com/exo-explore/exo.git
cd exo
pip install -e .
# alternatively, with venv
source install.sh
```

然后，在所有想要参与集群的设备上运行 exo 即可，无需额外配置，设备间会进行自动发现。

```sh
# Device 1
exo

# Device 2
exo
```

###### 项目推介

1、创新：exo 利用现有设备创建 AI 集群的理念，在节省成本的同时提升了设备的利用率。

2、实验性质：虽然 exo 目前仍处于实验阶段，但它展示了一种全新的、低成本参与 AI 计算的可能性。

3、社区支持：由 exo labs 维护，有机会参与早期的问题修复和功能贡献，加入一个正在成长的社区。

exo 开启了一扇门，让每个人都有可能参与到 AI 的革命中来，无论他们手头上拥有什么样的设备。在资源有限的情况下，exo 提供了一种独特而强大的解决方案，让 AI 的探索和应用变得更加民主化、普及化。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=exo-explore/exo&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/exo-explore/exo 

开源项目作者：exo-explore

开源协议：GNU General Public License v3.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=exo-explore/exo)

关注我们，一起探索有意思的开源项目。

