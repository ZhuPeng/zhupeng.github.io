---
layout: post
title: GitHub 开源项目 ultralytics/ultralytics 介绍，NEW - YOLOv8 🚀 in PyTorch > ONNX > OpenVINO > CoreML > TFLite
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 ultralytics/ultralytics，该项目在 GitHub 有超过 17.2k Star，用一句话介绍该项目就是：“NEW - YOLOv8 🚀 in PyTorch > ONNX > OpenVINO > CoreML > TFLite”。


![](https://raw.githubusercontent.com/ultralytics/assets/main/im/banner-yolo-vision-2023.png)
![](https://kaggle.com/static/images/open-in-kaggle.svg)
![](https://raw.githubusercontent.com/ultralytics/assets/main/yolov8/yolo-comparison-plots.png)
![](https://github.com/ultralytics/assets/raw/main/social/logo-social-github.png)
![](https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png)
![](https://github.com/ultralytics/assets/raw/main/social/logo-social-linkedin.png)
![](https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png)
![](https://github.com/ultralytics/assets/raw/main/social/logo-social-twitter.png)
![](https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png)
![](https://github.com/ultralytics/assets/raw/main/social/logo-social-youtube.png)



          | 1.95                                | 36.1               | 90.4              |
| [YOLOv8xl](https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8xl.pt) | 640                   | 52.1                 | 467.7                          | 2.71                                | 141.8              | 354.3             |

见 [YOLOv8 Models](https://github.com/ultralytics/ultralytics/tree/main/ultralytics/cfg/models) 获取完整模型列表。

**背景介绍：**

在快速发展的 AI 领域中，无论是图像识别、目标检测还是人体姿态估计等任务，都需要准确、高效的模型才能应对实际需求。随着技术不断进步，目标检测模型也迎来了新一代的升级与优化，而 Ultralytics 的 YOLOv8 正是一款全新的目标识别模型，它在前一代模型的基础上，加入了若干创新技术，使得检测速度、准确度获得了进一步的提升。

**项目介绍：**

Ultralytics YOLOv8（链接：https://github.com/ultralytics/ultralytics ）是一款优秀的目标检测开源项目，主要基于 PyTorch、ONNX、CoreML 和 TFLite 等技术实现。项目主要提供 Detect、Segment、Pose 三种预训练模型，并且也可以在 ImageNet 数据集上进行类别识别任务。相比前一代，YOLOv8 模型在速度、准确度以及易用性上都做了大幅度的优化和提升。此外，YOLOv8 还提供了完善的使用文档，对于新手来说十分友好。

**如何使用：**

首先，你需要在支持 Python>=3.8 和 PyTorch>=1.8 的环境中，通过 pip 安装 Ultralytics 包及其相关依赖：

```bash
pip install ultralytics
```

接着，你可以通过命令行或者 Python 脚本来进行模型的预测、训练等操作。例如，使用 Python，你可以通过以下代码来使用模型进行预测：

```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.pt")

# Use the model
results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image
```

**项目推介：**

目前，Ultralytics YOLOv8 项目在 GitHub 上更新非常活跃，且作者非常积极回复用户的问题和反馈。项目有着详细完善的文档和示例，对开发者十分友好。不仅如此，该项目引入了一系列先进的模型优化技术，使得检测速度及准确度得到了显著提升，且可以支持在多种设备上运行，包括 CPU、GPU、移动设备等。包括爱奇艺、京东等一些知名电商和媒体公司在内的用户正在使用此项目。因此，无论你是机器学习的研究者，还是想要尝试最新图像处理技术的开发者，Ultralytics YOLOv8 都是你的最佳选择。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=ultralytics/ultralytics&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/ultralytics/ultralytics 

开源项目作者：ultralytics

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=ultralytics/ultralytics)

关注我们，一起探索有意思的开源项目。

