---
layout: post
title: GitHub 开源项目 Stability-AI/generative-models 介绍，Generative Models by Stability AI
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 Stability-AI/generative-models，该项目在 GitHub 有超过 12.7k Star，用一句话介绍该项目就是：“Generative Models by Stability AI”。


![sample1](https://raw.githubusercontent.com/Stability-AI/generative-models/master/assets/000.jpg)
![tile](https://raw.githubusercontent.com/Stability-AI/generative-models/master/assets/tile.gif)
![sample2](https://raw.githubusercontent.com/Stability-AI/generative-models/master/assets/001_with_eval.png)



1、背景介绍：
当我们需要用到生成模型来创建新样本，处理图像，视频等数据，或要预测特定输入的可能输出时，那么 “Generative Models by Stability AI” 是您需要的解决方案。它是面向研究目的的创新开源工具，专注于图像和视频生成。

2、项目介绍：
根据其 README 文件，Stability AI 的生成模型提供了多种微调的模型供开发者选择。例如，其在 2023 年 11 月 21 日发布的 “Stable Video Diffusion” 是一个图像到视频生成模型，它使用标准的图像编码器，但将解码器替换为时序感知的 `deflickering decoder`。此款模型可以以给定的同样尺寸的上下文帧为准，生成分辨率为 576x1024 的 14 帧。对于需要生成 25 帧的需求，他们还有优化版本的 `SVD-XT` 模型。此外，他们还提供了供参考的 Streamlit demo（`scripts/demo/video_sampling.py`）和独立的 Python 脚本（`scripts/sampling/simple_video_sample.py`）。上述所有二者都可进行模型推断。

在设计上，这些模型都高度模块化，采用了 config-driven 的方法构建并组合子模块，并以 yaml 配置定义的对象调用 `instantiate_from_config()` 函数。同时，他们还使用了 PyTorch Lightning 进行训练，但若您喜欢使用其他训练包装器，也可以轻松地用在基础模块上。

3、如何使用：
对于代码类项目，我们需要先安装相关的环境，以下为安装示例：
```shell
# 克隆项目代码库
git clone git@github.com:Stability-AI/generative-models.git
cd generative-models

# 设置虚拟环境
python3 -m venv .pt2
source .pt2/bin/activate

# 安装依赖
pip3 install -r requirements/pt2.txt

# 安装项目拓展
pip3 install .

# 安装 sdata for training
pip3 install -e git+https://github.com/Stability-AI/datapipelines.git@main#egg=sdata

```
然后就可以根据自己的项目需求，参考其提供的代码和模型来开展相关的研究。

4、项目推介：
该项目更新频繁，可以看出开发者们投入了大量的精力，自 2023 年 6 月起持续发布新模型和技术报告，展现出活跃的开发状态和出色的研发能力。尽管该项目相对较新，但由于其高质量的内容和创新的设计思路，已经获得了很多用户的关注和使用。尤其是对于需要强大的生成模型来处理图像和视频等多媒体数据的机构或个人，该项目无疑将是一大福音。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=Stability-AI/generative-models&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/Stability-AI/generative-models 

开源项目作者：Stability-AI

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=Stability-AI/generative-models)

关注我们，一起探索有意思的开源项目。

