---
layout: post
title: 大模型加持的浏览器自动化工具，抢茅台也是可以的
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 项目背景

在当今的信息化社会，我们经常需要通过浏览器进行各种网页操作，同时我们也会遇到网页上的一些操作流程繁琐、耗时久的问题。而传统的浏览器自动化工具需要针对每个网站编写定制的脚本，这种方法依赖于网页的 DOM 解析和 XPath 交互，一旦网站布局发生变化，原先的自动化流程就可能出现问题。因此，我们需要一种能适应网站变化，同时能解决这些问题的工具。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240626232401377.png)

今天要给大家推荐一个 GitHub 开源项目 skyvern，该项目在 GitHub 有超过 5.3k Star，一句话介绍该项目：Automate browser-based workflows with LLMs and Computer Vision

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240418224042583.png)

###### 项目介绍

Skyvern 利用了大语言模型（LLMs）和计算机视觉技术来自动化浏览器操作流程。Skyvern 不仅能解析实时视窗中的项目，创建互动方式，并进行交互，而且可以在从未见过的网站上运行，通过将视觉元素映射到完成工作流所需的操作，无需任何定制代码。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240629190348182.png)

更重要的是，Skyvern 遇到页面布局变化时，不会像传统的自动化工具那样出现问题，因为它没有预设的 XPaths 或者寻找页面导航需要的其他选择器。Skyvern 通过 LLMs 处理交互来应对更复杂的情况，并且对于网页变化及时准确反应。

![](https://raw.githubusercontent.com/Skyvern-AI/skyvern/master/docs/images/finditparts_recording_crop.gif)

###### 如何使用

在本地机器上运行 Skyvern，首先需要确保你已经正确安装了 Python3.11、Brew（如果你是 Mac 用户）和 Poetry。然后按照以下步骤进行：

1、克隆仓库并导航至根目录；

2、运行安装脚本以安装必要的依赖项并设置环境；

3、启动服务器；

4、启动 UI；

5、在浏览器中导航至 localhost:8501 使用 UI。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240418224333753.png)

以下是对应的任务配置页面：

![](https://raw.githubusercontent.com/Skyvern-AI/skyvern/master/docs/images/skyvern_visualizer_run_task.png)

###### 项目推介

Skyvern 使用了现在最新的大语言模型和计算机视觉技术以实现稳定及可靠的浏览器自动化流程。虽然现在这个项目还在开发阶段，但是根据目前的进展，我相信 Skyvern 在未来会更加强大和便利。并且 Skyvern 也提供了一个线上的版本，如果你希望无需管理基础设施就可以运行 Skyvern，你可以考虑试用这个版本。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=Skyvern-AI/skyvern&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/Skyvern-AI/skyvern 

开源项目作者：Skyvern-AI

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=Skyvern-AI/skyvern)

关注我们，一起探索有意思的开源项目。

