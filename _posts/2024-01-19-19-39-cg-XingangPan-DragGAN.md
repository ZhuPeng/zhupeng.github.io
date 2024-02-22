---
layout: post
title: GitHub 开源项目 XingangPan/DragGAN 介绍，Official Code for DragGAN (SIGGRAPH 2023)
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 XingangPan/DragGAN，该项目在 GitHub 有超过 34.3k Star，用一句话介绍该项目就是：“Official Code for DragGAN (SIGGRAPH 2023)”。


![Open in OpenXLab](https://cdn-static.openxlab.org.cn/app-center/openxlab_app.svg)
![](https://raw.githubusercontent.com/XingangPan/DragGAN/master/DragGAN.gif)



背景介绍：在我们实际应用中，大部分的生成对抗网络（GAN）使用模型的潜在空间进行图像生成，这个潜在空间是连续的，我们可以对这个空间进行控制以生成我们想要的图像，但是，如何精细地控制生成效果，或者是与图像进行互动，都是我们目前需要解决的问题。正是这种需求和问题给予了 `DragGAN` 原理和的生命力。

项目介绍：`DragGAN` 是一个开源的项目，其在 SIGGRAPH 2023 上公开，项目的核心理念是：通过对潜在空间进行控制和调整，以达到更好的生成效果，提供了一种新的使用 GAN 的交互式操作方式。除此之外，该项目还提供了丰富的解决方案来解决创作过程中的被动感，如何更自由的创作出我们想要的图像，打开了使用生成对抗网络的新领域。

如何使用：首先在有 CUDA 图形卡的情况下，遵循 [NVlabs/stylegan3](https://github.com/NVlabs/stylegan3#requirements) 的要求进行安装。然后使用下面的命令进行项目的安装，包括创建环境、安装包等：

```
conda env create -f environment.yml
conda activate stylegan3
pip install -r requirements.txt
```

使用 `python scripts/download_model.py` 下载训练好的权重，并且提供了使用 Docker 进行操作的选择，使用 `docker build . -t draggan:latest  ` 和 `docker run -p 7860:7860 -v "$PWD":/workspace/src -it draggan:latest bash` 进行 Docker 的构建和启动。使用 `sh scripts/gui.sh` 启动 `DragGAN` 的图形用户界面，然后你就可以进行交互式操作了。

项目推介：从交互式生成对抗网络的新颖性可看出，`DragGAN` 的价值和影响力不容忽视，这是未来 GAN 网络发展的一种可能走向。项目目前维护活跃，研究者来自计算机图形学的重要会议 ACM SIGGRAPH，背景强大；由于项目刚刚公布，目前已经有大量的开发者对此表示关注。我强烈建议有 GAN 应用需求的人关注和试用该开源项目。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=XingangPan/DragGAN&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/XingangPan/DragGAN 

开源项目作者：XingangPan

开源协议：Other

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=XingangPan/DragGAN)

关注我们，一起探索有意思的开源项目。

