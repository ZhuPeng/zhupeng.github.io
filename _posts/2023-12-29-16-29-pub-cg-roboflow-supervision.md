---
layout: post
title: 频繁用到的计算机视觉工具集合
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在视觉相关工程师的日常工作中，需要大量时间书写计算机视觉工具，但这类工具往往存在重复的问题。为了解决这个问题，我们往往会对现有的代码进行修改或重用，但这可能会带来新的问题，例如缺乏高度的定制化、代码结构混乱导致后期难以维护、或者无法适应新的数据集。这些问题都让我们非常苦恼。

今天要给大家推荐一个 GitHub 开源项目 roboflow/supervision，该项目在 GitHub 有超过 8.1k Star，用一句话介绍该项目就是：“We write your reusable computer vision tools. 💜”。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240220232038487.png)

###### 项目介绍

Supervision 项目的主旨就是为你书写可重用的计算机视觉工具。不论你需要从硬盘加载数据集，还是在图像或视频上绘制侦测，或者计算一个区域内有多少侦测，你都可以依赖这个项目。而且，Supervision 更是被设计为模型不可知的。只要将分类、检测、分割模型插入即可。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240220232145488.png)

项目还提供了各种广泛且高度可定制的标记器，让你能够将者最佳的可视化用于自己的使用场景中。此外，引用该项目库，你还可以借助一套工具，用于加载、分割、合并和保存数据集。

除此之外，该项目还提供了一些相关的教程：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240220232222991.png)

###### 如何使用

在 Python>=3.8 的环境下，你可以通过以下命令安装这个包：

```bash
pip install supervision
```
然后，你就可以使用任何分类、检测或分割模型了。如果你需要使用我们为最流行的库创建的连接器，比如 Ultralytics，Transformers，或者 MMDetection ，你可以参考以下代码：
```python
>>> import cv2
>>> import supervision as sv
>>> from ultralytics import YOLO

>>> image = cv2.imread(...)
>>> model = YOLO('yolov8s.pt')
>>> result = model(image)[0]
>>> detections = sv.Detections.from_ultralytics(result)

>>> len(detections)
5
```


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=roboflow/supervision&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/roboflow/supervision 

开源项目作者：roboflow

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=roboflow/supervision)

关注我们，一起探索有意思的开源项目。

