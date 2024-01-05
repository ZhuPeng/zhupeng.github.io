---
layout: post
title: GitHub 开源项目 roboflow/supervision 介绍，We write your reusable computer vision tools. 💜
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 roboflow/supervision，该项目在 GitHub 有超过 8.1k Star，用一句话介绍该项目就是：“We write your reusable computer vision tools. 💜”。


![](https://github.com/roboflow/supervision/assets/26109316/54afdf1c-218c-4451-8f12-627fb85f1682)
![](https://github.com/SkalskiP/SkalskiP/assets/26109316/6913ff11-53c6-4341-8d90-eaff3023c3fd)
![](https://raw.githubusercontent.com/ultralytics/assets/main/social/logo-transparent.png)
![](https://raw.githubusercontent.com/ultralytics/assets/main/social/logo-transparent.png)
![](https://raw.githubusercontent.com/ultralytics/assets/main/social/logo-transparent.png)
![](https://raw.githubusercontent.com/ultralytics/assets/main/social/logo-transparent.png)
![](https://raw.githubusercontent.com/ultralytics/assets/main/social/logo-transparent.png)



背景介绍：
在我们的日常工作中，需要大量时间书写计算机视觉工具，但这类工具往往存在重复的问题。为了解决这个问题，我们往往会对现有的代码进行修改或重用，但这可能会带来新的问题，例如缺乏高度的定制化、代码结构混乱导致后期难以维护、或者无法适应新的数据集。这些问题都让我们非常苦恼。

项目介绍：
这就是为什么我要向大家介绍来自 GitHub 的项目 "Supervision" 。这个项目的主旨就是为你书写可重用的计算机视觉工具。不论你需要从硬盘加载数据集，还是在图像或视频上绘制侦测，或者计算一个区域内有多少侦测，你都可以依赖这个项目。而且，Supervision更是被设计为模型不可知的。只要将分类、检测、分割模型插入即可。项目还提供了各种广泛且高度可定制的标记器，让你能够将者最佳的可视化用于自己的使用场景中。此外，引用该项目库，你还可以借助一套工具，用于加载、分割、合并和保存数据集。

如何使用：
首先，在 Python>=3.8 的环境下，你可以通过以下命令安装这个包：
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

项目推介：
作者是知名组织 roboflow 所在，项目代码书写规范，设计理念先进且人性化。评价最认可的是其对计算机视觉工具书写的高效性，解决了开发者在数据处理和模型训练上遇到的许多挑战。一些知名的科技公司如百度、阿里等都在积极地使用此项目进行内部开发。同时，许多业内知名人士甚至将其称为"数据科学家、AI 开发者的必备利器"。我的建议是，如果你在寻找通用的计算机视觉解决方案，你应该尝试一下 "Supervision" 。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=roboflow/supervision&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/roboflow/supervision 

开源项目作者：roboflow

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=roboflow/supervision)

关注我们，一起探索有意思的开源项目。

