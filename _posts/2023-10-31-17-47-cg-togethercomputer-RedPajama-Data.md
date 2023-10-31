---
layout: post
title: GitHub 开源项目 togethercomputer/RedPajama-Data 介绍，The RedPajama-Data repository contains code for preparing large datasets for training large language models.
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 togethercomputer/RedPajama-Data，该项目在 GitHub 有超过 3.7k Star，用一句话介绍该项目就是：“The RedPajama-Data repository contains code for preparing large datasets for training large language models.”。


![](https://raw.githubusercontent.com/togethercomputer/RedPajama-Data/master/docs/rpv2.png)







背景介绍：在大规模语言模型的训练过程中，我们常常会遇到如何准备大量数据集的问题。这个问题的核心痛点在于，如何从海量的文本文档中筛选出高质量的数据，并进行去重处理，以便于训练出更准确的语言模型。

项目介绍：" RedPajama-Data " 是一个开源项目，专门用于准备训练大型语言模型的大数据集。该项目包含了超过 1000 亿份来自 84 个 CommonCrawl 快照的文本文档，这些文档都经过了 CCNet 管道的处理。在这些文档中，有 300 亿份文档附带有质量信号，还有 200 亿份文档经过了去重处理。该项目支持多种语言，包括英语、德语、法语、意大利语和西班牙语。

如何使用：首先，需要将配置文件 " configs/rp_v2.0.conf " 复制到例如 " configs/default.conf "，并配置环境变量。然后，构建 Docker 镜像，具体命令如下：

```
. configs/default.conf
cd app
docker build -t "${DOCKER_REPO}:" .
```

确保你已经安装了 s5cmd，并且已经配置了你的 S3 个人资料，这样你就可以从 S3 桶中拉取数据了。然后，你可以运行管道的步骤，包括准备工件、计算质量信号和去重。

项目推介：" RedPajama-Data " 项目是一个非常活跃的开源项目，作者是知名的开发者。该项目已经在 HuggingFace 上可用，得到了业内人士的广泛关注和推荐。如果你正在寻找一个用于准备大规模语言模型训练数据集的工具，那么 " RedPajama-Data " 项目将是你的不二之选。






以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=togethercomputer/RedPajama-Data&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/togethercomputer/RedPajama-Data 

开源项目作者：togethercomputer

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=togethercomputer/RedPajama-Data)

关注我们，一起探索有意思的开源项目。

