---
layout: post
title: GitHub 开源项目 WongKinYiu/yolov9 介绍，Implementation of paper - YOLOv9: Learning What You Want to Learn Using Programmable Gradient Information
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 WongKinYiu/yolov9，该项目在 GitHub 有超过 5.8k Star，用一句话介绍该项目就是：“Implementation of paper - YOLOv9: Learning What You Want to Learn Using Programmable Gradient Information”。



![](https://raw.githubusercontent.com/WongKinYiu/yolov9/master/./figure/performance.png)



背景介绍：
在计算机视觉领域，物体检测已经成为了一个核心的问题。传统的检测方法存在诸多限制，例如需要大量计算资源，精度不高，适应性差等。有很多试图解决这个问题的项目，其中 YOLO （You Only Look Once）系列算法是最为人所熟知的之一。然而，当我们需要进行定制化地、灵活地学习时，传统的 YOLO 也会显得力不从心。此时，如何使我们能够按照自己的目标进行训练，并获得高质量的模型就成为了一个新的挑战。

项目介绍：
项目链接为：https://github.com/WongKinYiu/yolov9 ，这是一个基于论文 "YOLOv9: Learning What You Want to Learn Using Programmable Gradient Information" 的实现。YOLOv9 是 YOLO 系列算法的新成员，它采用了可以编程的梯度信息来帮助我们实现可以自我学习的能力。在无数的实验中，YOLOv9 展示出了极高的效果。相比于以前的 YOLO 系列模型，YOLOv9 具备更高的精度和更少的参数数量。这些设计使得它在各种任务中，如训练自定义对象检测，人脸检测，物体跟踪等等有着出色的表现。

如何使用：
项目使用 Docker 进行环境的构建与管理。首先，我们需要创建一个 Docker 容器。在你的代码终端中，输入以下命令：
``` shell
nvidia-docker run --name yolov9 -it -v your_coco_path/:/coco/ -v your_code_path/:/yolov9 --shm-size=64g nvcr.io/nvidia/pytorch:21.11-py3
```
然后，我们需要安装以下所需的软件包：
``` shell
apt update
apt install -y zip htop screen libgl1-mesa-glx
pip install seaborn thop
```
最后，进入 "/yolov9" 目录并使用提供的预训练模型来进行评估。详细的使用命令可以在项目的 README 文档中找到。

项目推介：
YOLOv9 项目得到了广泛的关注与应用。不仅开发活跃，而且已经有许多公司和研究机构使用 YOLOv9 进行客户实景训练并取得了良好的效果。它能够满足多任务检测的需求，并在调优和训练过程中展示出优秀的性能。如果你正在寻找一个具有高度灵活性和优秀性能的新颖对象检测模型，那么 YOLOv9 将是一个不可多得的选择。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=WongKinYiu/yolov9&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/WongKinYiu/yolov9 

开源项目作者：WongKinYiu

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=WongKinYiu/yolov9)

关注我们，一起探索有意思的开源项目。

