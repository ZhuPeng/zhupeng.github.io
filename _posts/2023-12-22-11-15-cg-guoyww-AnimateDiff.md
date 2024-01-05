---
layout: post
title: GitHub 开源项目 guoyww/AnimateDiff 介绍，Official implementation of AnimateDiff.
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 guoyww/AnimateDiff，该项目在 GitHub 有超过 6.6k Star，用一句话介绍该项目就是：“Official implementation of AnimateDiff.”。


![Open in OpenXLab](https://cdn-static.openxlab.org.cn/app-center/openxlab_app.svg)
![](https://raw.githubusercontent.com/guoyww/AnimateDiff/master/__assets__/figs/adapter_explain.png)
![](https://raw.githubusercontent.com/guoyww/AnimateDiff/master/__assets__/demos/image/RealisticVision_firework.png)
![](https://raw.githubusercontent.com/guoyww/AnimateDiff/master/__assets__/animations/v3/animation_fireworks.gif)
![](https://raw.githubusercontent.com/guoyww/AnimateDiff/master/__assets__/demos/image/RealisticVision_sunset.png)
![](https://raw.githubusercontent.com/guoyww/AnimateDiff/master/__assets__/animations/v3/animation_sunset.gif)
![](https://raw.githubusercontent.com/guoyww/AnimateDiff/master/__assets__/demos/scribble/scribble_1.png)
![](https://raw.githubusercontent.com/guoyww/AnimateDiff/master/__assets__/animations/v3/sketch_boy.gif)
![](https://raw.githubusercontent.com/guoyww/AnimateDiff/master/__assets__/demos/scribble/scribble_2_readme.png)
![](https://raw.githubusercontent.com/guoyww/AnimateDiff/master/__assets__/animations/v3/sketch_city.gif)



背景介绍：随着计算机视觉技术的发展，图像生成的技术和应用也在日益广泛地被采用。然而，许多社区模型在生成动画方面仍缺乏足够的效果，这将需要额外的训练和优化，耗费了大量的时间和资源。

项目介绍：AnimateDiff 是在这样的背景下诞生的，该项目官方基于 Arxiv 上的 [AnimateDiff](https://arxiv.org/abs/2307.04725) 文章进行了实现，它是一个插件式的模块，能够在没有新增训练的情况下，将多数社区模型转变成动画生成器。实际上，AnimateDiff 开发了四个版本，分别是 `v1`、`v2` 、`v3` 和 `sdxl-beta`，它们分别适用于 [Stable Diffusion V1.5](https://huggingface.co/runwayml/stable-diffusion-v1-5) 和 [Stable Diffusion XL](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) 。此外，项目 GALLERY 提供了一些社区贡献的结果展示。

如何使用:在准备环境的过程中，需要首先克隆设计库和创建 conda 环境，然后下载 Stable Diffusion V1.5。再然后，手动下载社区`.safetensors`模型，并将它们保存在 `models/DreamBooth_LoRA`。最后，手动下载 AnimateDiff 模块，并将模块保存在 `models/Motion_Module`。具体代码如下：
```
git clone https://github.com/guoyww/AnimateDiff.git
cd AnimateDiff
conda env create -f environment.yaml
conda activate animatediff
git lfs install
git clone https://huggingface.co/runwayml/stable-diffusion-v1-5 models/StableDiffusion/
```
项目推介：AnimateDiff 项目的开发者具有丰富的经验，包括 [Yuwei Guo](https://guoyww.github.io/) 等，他们在其它相关领域也有深入的研究和积累。目前，该项目正处在活跃开发状态，且已在社区合作的过程中逐步得到了优化和完善。人们通过使用 AnimateDiff 已经达到了一些令人瞩目的结果，不仅大大加快了动画生成的速度，还显著提高了生成效果的质量。如果你在寻找一个能够快速、高效地将模型转变成动画生成器的项目，AnimateDiff 绝对值得你一试。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=guoyww/AnimateDiff&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/guoyww/AnimateDiff 

开源项目作者：guoyww

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=guoyww/AnimateDiff)

关注我们，一起探索有意思的开源项目。

