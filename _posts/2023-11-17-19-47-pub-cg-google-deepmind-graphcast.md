---
layout: post
title: GraphCast - Google DeepMind 开源的气象预测模型，专为全球中远期天气预测设计
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在气候预测和研究中，我们经常遇到的一个问题是对全球气候变化的中远期预测。由于气候系统的复杂性和数据的大量性，我们通常依赖复杂的数值气候模型来进行预测。然而，这些模型不仅需要大量的计算资源，而且在预测中也可能存在误差，使得我们的预测结果可能偏离实际情况。鉴于此，我们急需一个高效且准确的气候预测工具，用以解决目前的痛点。

今天要给大家推荐一个 GitHub 开源项目 google-deepmind/graphcast，该项目在 GitHub 有超过 1.6k Star，该项目就是尝试解决以上问题。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231217222915205.png)

###### 项目介绍

来自 Google DeepMind 的开源项目 GraphCast 是一个基于图神经网络的气象预测模型，专为全球中远期天气预测设计。项目提供了三个预训练模型，分别为 `GraphCast`、`GraphCast_small` 和 `GraphCast_operational`，均使用 ERA5 数据进行训练。模型权重、规范化统计和样本输入等均可从 [Google Cloud Bucket](https://console.cloud.google.com/storage/browser/dm_graphcast) 下载。

GraphCast 使用了多种图神经网络（GNN）技术，并对网格和三角形网格进行转换，可以有效地从输入的网格数据中生成节点和边向量特征，并将节点输出向量返回到多级网格数据。所有这些特性让 GraphCast 成为一种高效且富有创新的气候预测工具。

###### 如何使用

首先，需要下载或克隆项目代码。然后，下载所需的 ERA5 数据集。在 Python 环境中，首先导入相关的库，然后依照 `graphcast_demo.ipynb` 笔记本文件的说明加载数据，生成或加载预训练模型，生成预测结果，计算损失和梯度等操作。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231217223237129.png)

更多示例代码请通过 GitHub 查看。

###### 项目推介

GraphCast 是由 Google DeepMind 团队开发的开源项目，其开发团队有着丰富的人工智能及机器学习经验，积累的优秀项目和研究为他们的专业能力和创新能力提供了有力的证明。项目采用先进的图神经网络技术，使得其在全球中远期天气预测方面具有显著的优势。而且，项目的算法和代码都是公开的，允许研究人员对其进行修改和优化，以满足更多的应用需求。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=google-deepmind/graphcast&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/google-deepmind/graphcast 

开源项目作者：google-deepmind

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=google-deepmind/graphcast)

关注我们，一起探索有意思的开源项目。

