---
layout: post
title: ComfyUI - 模块化的 stable diffusion 流程化编排界面
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在处理图像、视频或其它 stable diffusion 数据过程中，我们需要设计和执行复杂的 stable diffusion 流程。然而由于它的复杂性，我们可能需要编写大量的代码来实现。更为麻烦的是，应对不同数据或不同类型的流程，我们又要做出相应的调整或重头编写。那么，有没有一种方法，既能简化这种复杂的流程设计，又能根据不同的需求轻松调整流程呢？

今天要给大家推荐一个 GitHub 开源项目 comfyanonymous/ComfyUI，该项目在 GitHub 有超过 15.5k Star，用一句话介绍该项目就是：“The most powerful and modular stable diffusion GUI with a graph/nodes interface.”。


![](https://raw.githubusercontent.com/comfyanonymous/ComfyUI/master/comfyui_screenshot.png)

###### 项目介绍

ComfyUI 提供了一种非常强大的、模块化的 stable diffusion GUI，使用图/节点/流程图界面，设计和执行高级 stable diffusion 流程，无需编写任何代码。它支持 SD1.x，SD2.x，SDXL 和 stable 视频扩散，还有许多特性需要注意，如千差万别的优化、异步队列系统、低显存选项、CPU 模式、多种模型或检查点加载方式、多种复杂流程设计和操作，同时还有丰富示例供学习和参考。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231224225356876.png)

###### 如何使用

使用 ComfyUI 很简单，你可以先访问 GitHub 项目链接，点击右上角的 "Code" 按钮，然后选择 "Download ZIP"，下载项目到本地，解压后运行 python main.py 即可，当然可能你使用的系统有差别，在参数上会有不同，具体可参考 GitHub README 介绍。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231224225801618.png)

然后通过图/节点/流程图界面设计和执行你想要的稳定扩散流程。如果遇到问题，你可以查阅项目提供的各种教程例子 https://comfyanonymous.github.io/ComfyUI_examples/。

以下是一个图片转化图片（img2img）的示例：

![](https://comfyanonymous.github.io/ComfyUI_examples/img2img/img2img_workflow.png)

###### 项目推介

虽然这个项目是最近才发布，但它的功能强大，设计灵活，非常适合处理图像、视频或其它稳定扩散数据。项目作者积极响应用户反馈，更新代码，一直在为 ComfyUI 加入更多的功能和例子。就目前来看，项目维护的活跃，已经有不少人在此基础上延伸应用。对于想通过简单、灵活、高效的方式处理稳定扩散数据的朋友来说，这是一个值得一试的项目。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231224225929416.png)


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=comfyanonymous/ComfyUI&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/comfyanonymous/ComfyUI 

开源项目作者：comfyanonymous

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=comfyanonymous/ComfyUI)

关注我们，一起探索有意思的开源项目。

