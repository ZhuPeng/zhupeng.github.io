---
layout: post
title: Generative Models - 用生成模型处理图像和视频
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

当我们需要用到生成模型来创建新样本，处理图像，视频等数据，或要预测特定输入的可能输出时，那么 Generative Models by Stability AI 是您需要的解决方案。它是面向研究目的的创新开源工具，专注于图像和视频生成。

GitHub 开源项目 Stability-AI/generative-models 在 GitHub 有超过 12.7k Star。

![](https://raw.githubusercontent.com/Stability-AI/generative-models/master/assets/000.jpg)

###### 项目介绍

Stability AI 的生成模型提供了多种微调的模型供开发者选择。例如，在 2023 年 11 月 21 日发布的 Stable Video Diffusion 是一个图像到视频生成模型，它使用标准的图像编码器，但将解码器替换为时序感知的 `deflickering decoder`。此款模型可以以给定的同样尺寸的上下文帧为基准，生成分辨率为 576x1024 的 14 帧。对于需要生成 25 帧的需求，他们还有优化版本的 `SVD-XT` 模型。此外，他们还提供了供参考的 Streamlit demo（`scripts/demo/video_sampling.py`）和独立的 Python 脚本（`scripts/sampling/simple_video_sample.py`）。上述所有二者都可进行模型推断。

以下是对应生成的视频片段：

![](https://raw.githubusercontent.com/Stability-AI/generative-models/master/assets/tile.gif)

在设计上，这些模型都高度模块化，采用了 config-driven 的方法构建并组合子模块，并以 yaml 配置定义的对象调用 `instantiate_from_config()` 函数。同时，他们还使用了 PyTorch Lightning 进行训练，但若您喜欢使用其他训练包装器，也可以轻松地用在基础模块上。

###### 如何使用

以下为安装示例：

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

然后就可以根据自己的项目需求，参考其提供的代码和模型来开展相关的测试或者研究了。

```bash
streamlit run scripts/demo/sampling.py --server.port <your_port>
```

以上命令可以运行 streamlit 的 demo 代码。

![](https://raw.githubusercontent.com/Stability-AI/generative-models/master/assets/001_with_eval.png)

###### 项目推介

该项目更新频繁，可以看出开发者们投入了大量的精力，自 2023 年 6 月起持续发布新模型和技术报告，展现出活跃的开发状态和出色的研发能力。对于需要强大的生成模型来处理图像和视频等多媒体数据的机构或个人，该项目是一个有巨大潜力提高图像和视频处理效率的工具。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=Stability-AI/generative-models&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/Stability-AI/generative-models 

开源项目作者：Stability-AI

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=Stability-AI/generative-models)

关注我们，一起探索有意思的开源项目。

