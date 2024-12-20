---
layout: post
title: GitHub 开源项目 facebookresearch/AnimatedDrawings 介绍，Code to accompany "A Method for Animating Children's Drawings of the Human Figure"
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 facebookresearch/AnimatedDrawings，该项目在 GitHub 有超过 11.6k Star。

![](https://stats.deeptrain.net/repo/facebookresearch/AnimatedDrawings/?theme=light)

一句话介绍该项目：Code to accompany "A Method for Animating Children's Drawings of the Human Figure"




![Sequence 02](https://user-images.githubusercontent.com/6675724/219223438-2c93f9cb-d4b5-45e9-a433-149ed76affa6.gif)

![Sequence 01](https://user-images.githubusercontent.com/6675724/233157474-1506d219-c085-49f9-a537-43d6c1bae93a.gif)


###### 项目介绍

背景介绍：
在数字艺术和计算机图形学领域，将孩子们天马行空的画作转化成活泼生动的动画，不仅仅是一种技术挑战，更是一种创造力的展现。孩子的绘画往往包含着纯真和创意，但传统动画的制作流程复杂且耗时，普通家庭往往难以承受这样的成本和技术门槛。因此，存在着一个核心痛点：如何快速、低成本地将孩子的手绘作品转化为动画，让这些美好的想象力跃然屏幕上？



![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-6232e073dcc1e82f9ffc99584a77ec16.png)

项目介绍：
《Animated Drawings》是一个由 Facebook Research 团队开发的开源项目，基于他们在论文 "A Method for Animating Children's Drawings of the Human Figure" 中描述的算法实现。该项目的核心目的在于将孩子们的人物画作动画化。用户可以将自己或孩子的绘画作品导入此工具中，通过算法处理后生成动画，为创意注入生命。项目既强大又灵活，支持多种动画输出格式（如 MP4 视频、透明 GIF 等），并提供了一系列配置文件，让用户按需调整动画风格和参数。此外，通过 Docker 容器，项目还简化了机器学习模型的使用，自动识别绘画中的人物姿态，并生成所需的注解文件，从而实现快速动画生成。

如何使用：
1. 首先，在 macOS Ventura 13.2.1 和 Ubuntu 18.04 环境下安装该项目；
2. 使用 Conda 创建一个 Python 虚拟环境，然后将项目克隆到本地，并通过 pip 安装；
3. 使用提供的 Python 代码段启动一个交互式窗口，或者导出 MP4 视频和 GIF 文件；
4. 对于想要让自己绘画作品动画化的用户，项目还提供了 Docker 方案，通过 TorchServe 运行机器学习模型，自动化生成注解文件的过程。

项目推介：
《Animated Drawings》项目得到了业内人士的广泛关注和认可，项目的 Video Overview 已在 YouTube 上发布，详细介绍了其背后的技术和使用方法。Facebook Research 团队本身就是技术领域的佼佼者，他们长期致力于将前沿的研究成果实用化。此项目是为了帮助用户，特别是非专业用户，轻松将孩子的绘画作品动画化而设计的。它不仅有助于促进亲子互动，而且提供了一个新颖的方法来探索和实现创意想法。随着项目的不断发展，相信未来会有更多家庭和创意工作者受益于此。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=facebookresearch/AnimatedDrawings&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/facebookresearch/AnimatedDrawings 

开源项目作者：facebookresearch

开源协议：MIT License

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=facebookresearch/AnimatedDrawings)

关注我们，一起探索有意思的开源项目。

