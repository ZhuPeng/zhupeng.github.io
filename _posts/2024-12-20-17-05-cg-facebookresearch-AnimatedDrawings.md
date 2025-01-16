---
layout: post
title: 将儿童人物画作动画化的有趣项目
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在数字艺术和计算机图形学领域，将孩子们天马行空的画转化成活泼生动的动画，不仅仅是一种技术挑战，更是一种创造力的展现。孩子的绘画往往包含着纯真和创意，但传统动画的制作流程复杂且耗时，普通家庭往往难以承受这样的成本和技术门槛。因此，如何快速、低成本地将孩子的手绘作品转化为动画，让这些美好的想象力跃然屏幕上，是一个很有趣的方向。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-6232e073dcc1e82f9ffc99584a77ec16.png)

今天要给大家推荐一个 GitHub 开源项目 AnimatedDrawings，该项目在 GitHub 有超过 12.1k Star。

![](https://stats.deeptrain.net/repo/facebookresearch/AnimatedDrawings/?theme=light)

一句话介绍该项目：Code to accompany "A Method for Animating Children's Drawings of the Human Figure"


![](https://user-images.githubusercontent.com/6675724/219223438-2c93f9cb-d4b5-45e9-a433-149ed76affa6.gif)


###### 项目介绍

Animated Drawings 是一个由 Facebook Research 团队开发的开源项目，基于他们在论文 A Method for Animating Children's Drawings of the Human Figure 中描述的算法实现。该项目的核心目的在于将孩子们的人物画作动画化。用户可以将自己或孩子的绘画作品导入此工具中，通过算法处理后生成动画，为创意注入生命。项目既强大又灵活，支持多种动画输出格式（如 MP4 视频、透明 GIF 等），并提供了一系列配置文件，让用户按需调整动画风格和参数。

![](https://raw.githubusercontent.com/facebookresearch/AnimatedDrawings/main/media/interactive_window_example.gif)

###### 如何使用

当前项目仅在 macOS Ventura 13.2.1 和 Ubuntu 18.04 环境下经过了测试，如果是其他系统可能碰到未知问题。然后可按如下流程安装使用：

1、使用 Conda 创建一个 Python 虚拟环境，然后将项目克隆到本地，并通过 pip 安装

```bash
# create and activate the virtual environment
conda create --name animated_drawings python=3.8.13
conda activate animated_drawings

# clone AnimatedDrawings and use pip to install
git clone https://github.com/facebookresearch/AnimatedDrawings.git
cd AnimatedDrawings
pip install -e .
```

2、然后激活 conda 环境，使用如下命令来生成导出 MP4 视频和 GIF 文件

![](/Users/zhupeng/Work/git/zhupeng.github.io/images/image-20250104224754019.png)

###### 项目推介

Facebook Research 团队本身就是技术领域的佼佼者，他们长期致力于将前沿的研究成果实用化。此项目是为了帮助用户，特别是非专业用户，轻松将孩子的绘画作品动画化而设计的。它不仅有助于促进亲子互动，而且提供了一个新颖的方法来探索和实现创意想法。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=facebookresearch/AnimatedDrawings&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/facebookresearch/AnimatedDrawings 

开源项目作者：facebookresearch

开源协议：MIT License

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=facebookresearch/AnimatedDrawings)

关注我们，一起探索有意思的开源项目。

