---
layout: post
title: pix2tex - 通过 OCR 将数学公式的图像转换为相应的 LaTeX 代码
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在数学领域，将手写公式转换为 LaTeX 代码是一个常见的需求。然而，手动转换费时费力且容易出错。为解决这一问题，pix2tex 项目应运而生。该项目旨在创建一个基于学习的系统，可以接收数学公式的图像并返回相应的 LaTeX 代码。

GitHub 开源项目 lukas-blecher/LaTeX-OCR，该项目在 GitHub 有超过 6.1k Star，用一句话介绍该项目就是：“pix2tex: Using a ViT to convert images of equations into LaTeX code.”。

![](https://user-images.githubusercontent.com/55287601/117812740-77b7b780-b262-11eb-81f6-fc19766ae2ae.gif)

###### 项目介绍

pix2tex 是一个基于 ViT (Vision Transformer) 的 OCR 项目，使用深度学习模型将数学公式的图像转换为相应的 LaTeX 代码。项目主要包括以下功能：

1、通过使用命令行工具，可从磁盘上的已有图像或剪贴板中解析并获取 LaTeX 代码。

2、提供了一个用户界面，可通过截图方式快速获取模型预测的 LaTeX 代码，并使用 MathJax 渲染并复制到剪贴板。

3、可通过 API 使用，提供一个 Streamlit 演示页面。

![](https://user-images.githubusercontent.com/55287601/109183599-69431f00-778e-11eb-9809-d42b9451e018.png)

该模型在处理小分辨率图像时效果最佳，因此在预处理阶段，使用另一个神经网络预测输入图像的最佳分辨率，并自动将图像调整为最符合训练数据的大小，从而提高性能。然而，仍然不完美，对于超大的图像可能无法进行最佳处理，因此在拍摄之前不要太过放大图像。 同时，始终要仔细检查结果的准确性，如果答案错误，可以尝试使用其他分辨率重新进行预测。

###### 如何使用

要使用该项目，您需要安装 Python 3.7+ 和 PyTorch。接下来，按照以下步骤安装并运行项目：

1、安装pix2tex库：`pip install "pix2tex[gui]"`

2、下载模型检查点

3、通过以下三种方式之一获取图像的预测结果：

- 使用命令行工具`pix2tex`，您可以从磁盘上的已有图像或剪贴板中解析并获取 LaTeX 代码。
- 使用提供的用户界面`latexocr`，通过截图方式快速获取模型预测的 LaTeX 代码，并通过 MathJax 渲染并复制到剪贴板。
- 使用 API，您可以通过安装相关依赖并运行 API 进行连接，或使用提供的 Docker 镜像。

如果您希望在自己的Python代码中使用该项目，可以按照以下示例进行调用：

```python
from PIL import Image
from pix2tex.cli import LatexOCR
    
img = Image.open('path/to/image.png')
model = LatexOCR()
print(model(img))
```

###### 项目推介

pix2tex 的作者在深度学习领域有丰富的经验，该项目提供了详细的文档以及各种示例和演示。如果您对数学公式的 LaTeX 转换感兴趣，那么 pix2tex 是您的不二选择！

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231129224825053.png)


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=lukas-blecher/LaTeX-OCR&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/lukas-blecher/LaTeX-OCR 

开源项目作者：lukas-blecher

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=lukas-blecher/LaTeX-OCR)

关注我们，一起探索有意思的开源项目。

