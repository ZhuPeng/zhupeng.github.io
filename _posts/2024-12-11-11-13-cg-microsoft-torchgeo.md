---
layout: post
title: GitHub 开源项目 microsoft/torchgeo 介绍，TorchGeo: datasets, samplers, transforms, and pre-trained models for geospatial data
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 microsoft/torchgeo，该项目在 GitHub 有超过 3.0k Star。

![](https://stats.deeptrain.net/repo/microsoft/torchgeo/?theme=light)

一句话介绍该项目：TorchGeo: datasets, samplers, transforms, and pre-trained models for geospatial data




![](https://raw.githubusercontent.com/microsoft/torchgeo/main/logo/logo-color.svg)

![](https://img.youtube.com/vi/ET8Hb_HqNJQ/0.jpg)

![](https://img.youtube.com/vi/R_FhY8aq708/0.jpg)

![](https://raw.githubusercontent.com/microsoft/torchgeo/main/images/geodataset.png)

![](https://raw.githubusercontent.com/microsoft/torchgeo/main/images/vhr10.png)

![](https://raw.githubusercontent.com/microsoft/torchgeo/main/images/inria.png)


###### 项目介绍

**背景介绍**

在处理与地理空间数据相关的项目时，无论是从事遥感数据分析的专家还是机器学习领域的研究者，都面临着相同的难题：如何有效地处理和分析这些大规模、多维度、不同坐标参照系统的数据。地理空间数据具有其特殊性，包括但不限于大范围的地理覆盖、不同的空间分辨率、多光谱波段，以及复杂的数据格式。这些问题直接影响到数据处理的效率和模型训练的可行性，是地理空间数据应用领域的核心痛点。

**

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-793c961f395fd8f14148f5e11210113c.png)

项目介绍**

为解决上述问题，[TorchGeo](https://github.com/microsoft/torchgeo) 应运而生。这是一个基于 [PyTorch](https://pytorch.org/) 的地理空间数据领域库，类似于 torchvision，提供了专门针对地理空间数据的数据集、采样器、转换方法和预训练模型。TorchGeo 的目标是简化机器学习专家处理地理空间数据的难度，并帮助遥感领域的专家探索机器学习解决方案。它不仅包含了多种地理空间数据集的处理和采样器（例如 Landsat 7 和 8 卫星数据，CDL 数据等），还提供了数据的转换、叠加且易于与 PyTorch 数据加载器结合使用的功能。

**如何使用**

安装 TorchGeo 推荐使用 pip：

```console
$ pip install torchgeo
```

对于需要使用 conda 或 spack 的用户，可以参照官方文档中的安装指令。[安装指南](https://torchgeo.readthedocs.io/en/stable/user/installation.html) 提供了更多详情。

使用 TorchGeo 可以非常简单地处理地理空间数据：

```python
from torch.utils.data import DataLoader
from torchgeo.datamodules import InriaAerialImageLabelingDataModule
from torchgeo.datasets import CDL, Landsat7, Landsat8, stack_samples
from torchgeo.samplers import RandomGeoSampler

# 假设你已经下载了 Landsat 7 和 8 的数据
landsat7 = Landsat7(paths="...", bands=["B1", ..., "B7"])
landsat8 = Landsat8(paths="...", bands=["B2", ..., "B8"])
landsat = landsat7 | landsat8
cdl = CDL(paths="...", download=True, checksum=True)
dataset = landsat & cdl

sampler = RandomGeoSampler(dataset, size=256, length=10000)
dataloader = DataLoader(dataset, batch_size=128, sampler=sampler, collate_fn=stack_samples)

for batch in dataloader:
    image = batch["image"]
    mask = batch["mask"]
    # 使用模型训练或者预测
```

**项目推介**

TorchGeo 由微软支持并维护，自发布以来，一直活跃在开发和更新中，保证了其技术的前沿性和实用性。它的官方文档详尽，提供了丰富的 API 文档、贡献指南和多个教程，帮助用户快速上手。此外，它的实用性不限于学术研究，多个知名机构和公司也在各自的遥感数据处理和分析项目中应用了 TorchGeo，这充分证明了其在业界的广泛认可和高效能力。无论是刚入门的学者还是资深的遥感数据分析师，TorchGeo 都是一个值得推荐和尝试的工具库。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=microsoft/torchgeo&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/microsoft/torchgeo 

开源项目作者：microsoft

开源协议：MIT License

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=microsoft/torchgeo)

关注我们，一起探索有意思的开源项目。

