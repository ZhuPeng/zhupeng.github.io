---
layout: post
title: GitHub 开源项目 graphdeco-inria/gaussian-splatting 介绍，Original reference implementation of "3D Gaussian Splatting for Real-Time Radiance Field Rendering"
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 graphdeco-inria/gaussian-splatting，该项目在 GitHub 有超过 7.7k Star，用一句话介绍该项目就是：“Original reference implementation of "3D Gaussian Splatting for Real-Time Radiance Field Rendering"”。


![Teaser image](https://raw.githubusercontent.com/graphdeco-inria/gaussian-splatting/master/assets/teaser.png)
![Teaser image](https://raw.githubusercontent.com/graphdeco-inria/gaussian-splatting/master/assets/select.png)
![Default learning rate result](https://raw.githubusercontent.com/graphdeco-inria/gaussian-splatting/master/assets/worse.png "title-1")
![Reduced learning rate result](https://raw.githubusercontent.com/graphdeco-inria/gaussian-splatting/master/assets/better.png "title-2")
![](https://raw.githubusercontent.com/graphdeco-inria/gaussian-splatting/master/assets/logo_inria.png)
![](https://raw.githubusercontent.com/graphdeco-inria/gaussian-splatting/master/assets/logo_uca.png)
![](https://raw.githubusercontent.com/graphdeco-inria/gaussian-splatting/master/assets/logo_mpi.png)
![](https://raw.githubusercontent.com/graphdeco-inria/gaussian-splatting/master/assets/logo_graphdeco.png)



背景介绍：
在实时的光照场渲染领域，我们经常会遇到若干痛点问题。首先，为了实现高质量的视觉呈现，我们需要使用一些复杂昂贵的神经网络进行训练和渲染，而近期的更快方法则不可避免地牺牲了质量以换取速度。其次，无论是对于无边界的也好，还是完整场景（而不是孤立的物体）来说，或者是 1080p 分辨率的渲染来说，没有当前的方法能够达到实时的显示速度。因此，我们迫切需要一种能在保持训练时间争议、允许高质量实时（≥ 30 fps）新视图合成的同时，也能实现最先进的视觉质量的方法。

项目介绍：
我们的开源项目 "3D Gaussian Splatting for Real-Time Radiance Field Rendering" 是一种具有重要意义的实时光照场渲染方法。我们主要引入了三个关键要素以实现上述目标：首先，我们利用在相机校准过程中产生的稀疏点，用 3D 高斯来表示场景，这为场景优化保留了连续的体积光照场的有益属性，同时避免了在空白空间中进行不必要的计算；其次，我们对 3D 高斯进行了交叉优化/密度控制，特别是优化了各向异性协方差，以实现场景的精确表示；最后，我们开发了一种快速的可见度感知渲染算法，支持各向异性分割，并加快了训练，实现了实时渲染。我们在多个已建立的数据集上证明了这种方法可以实现最先进的视觉质量和实时渲染。

如何使用：
我们的项目基于原生 Python，以及 PyTorch 和 CUDA 拓展。使用我们的项目，首先你需要有具备 Compute Capability 7.0+ 的 CUDA-ready GPU，以及 24 GB 的显存（为了达到论文评估质量）。接着，你需要通过在终端运行以下指令进行项目的克隆：
```shell
# SSH
git clone git@github.com:graphdeco-inria/gaussian-splatting.git --recursive
```
或者
```shell
# HTTPS
git clone https://github.com/graphdeco-inria/gaussian-splatting --recursive
```

项目推介：
该项目在实时光照场领域已经展现出了其卓越的表现，它由 INRIA（法国国家计算机与自动化研究所）的团队进行研发，团队有数位在图形学领域有着深厚技术积累的研究者，他们的研究果实有着广泛的影响，也荣誉累累。此外，此项目的教程已经由 Jonathan Stephens 所制作，更方便初学者进行项目的学习和使用。无论是对图形学领域有追求，还是在需要快速、高质量实时光照场渲染的工作者，都应当关注和尝试使用该项目。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=graphdeco-inria/gaussian-splatting&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/graphdeco-inria/gaussian-splatting 

开源项目作者：graphdeco-inria

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=graphdeco-inria/gaussian-splatting)

关注我们，一起探索有意思的开源项目。

