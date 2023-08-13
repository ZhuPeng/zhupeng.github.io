---
layout: post
title: 可本地搭建的 Stable Diffusion Web 应用
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

在处理图像和文本时，我们经常面临着各种挑战，例如图像修复、图像上采样、文本生成等。这些问题需要强大而高效的工具来解决，Stable Diffusion 可以很好的解决以上问题，但是要想自己本地使用 Stable Diffusion，还是有一定的门槛的。Stable Diffusion Web UI 项目正是为了应对这些挑战而诞生的。

今天要给大家推荐一个 GitHub 开源项目 AUTOMATIC1111/stable-diffusion-webui，该项目在 GitHub 有超过 79.4k Star，用一句话介绍该项目就是：“Stable Diffusion web UI”。


![](https://raw.githubusercontent.com/AUTOMATIC1111/stable-diffusion-webui/master/screenshot.png)

#### 项目介绍
Stable Diffusion Web UI 是基于 Gradio 库的浏览器界面，用于使用 Stable Diffusion 进行图像和文本处理。该项目旨在提供一个用户友好的界面，使用户能够轻松地使用Stable Diffusion的功能。主要特点包括：
- 原始的文本转图像和图像转图像模式
- 一键安装和运行脚本（但您仍需安装Python和Git）
- 图像修复、图像补全、彩色素描等功能
- 提示矩阵，指定模型应该更关注的文本部分
- 稳定扩散放大，用于图像的高清放大
- 注意力控制，可以针对特定文本部分增加注意力
- 循环处理，多次运行图像处理
- X/Y/Z绘图，可绘制具有不同参数的图像的三维图
- 文本反转，可以使用多个嵌入和自定义名称进行文本反转
- 额外选项标签，包括各种神经网络工具，如面部修复、图像上采样等
- 图像尺寸调整选项
- 采样方法选择和噪声设置选项
- 随时中断处理过程
- 支持4GB显卡等功能

#### 如何使用
要使用Stable Diffusion Web UI项目，您需要按照以下步骤进行安装和配置：
1. 克隆代码仓库。
2. 运行一键安装和运行脚本 webui.sh，确保已安装 Python3 和 Git。
3. 打开浏览器，访问 Stable Diffusion Web UI的界面。
4. 在界面上选择所需的功能和参数，上传图像或输入文本。
5. 启动处理过程，并根据需要进行调整和控制。
6. 在处理完成后，查看结果并下载或保存图像。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=AUTOMATIC1111/stable-diffusion-webui&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/AUTOMATIC1111/stable-diffusion-webui 

开源项目作者：AUTOMATIC1111

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=AUTOMATIC1111/stable-diffusion-webui)

关注我们，一起探索有意思的开源项目。

