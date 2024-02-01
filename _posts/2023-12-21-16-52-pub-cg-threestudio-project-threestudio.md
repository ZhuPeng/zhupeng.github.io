---
layout: post
title: 生成 3D 画面原来可以这么简单
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在现代数字艺术领域，3D 内容生成是一个重要且具有挑战性的课题。要真正实现精细的、高质量的 3D 模型创建，艺术家需要花费大量时间，并具备高级的技术技能和创新想象力。而且，从 2D 文本或图像生成 3D 内容常常需要各种类型的复杂和专业的工具，这在很大程度上限定了使用 3D 的用户数量。

今天要给大家推荐一个 GitHub 开源项目 threestudio-project/threestudio，该项目在 GitHub 有超过 4.5k Star，用一句话介绍该项目就是：“A unified framework for 3D content generation.”。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240126230912371.png)

###### 项目介绍

ThreeStudio 是一个从文本提示、单个图像和少量图像生成 3D 内容的统一框架。通过提升 2D 文本到图像生成模型，为 3D 内容生成带来新的可能性。

该项目的优点有很多，以下是其中一些介绍：

1、同一框架下支持多种生成模式，从文本到 3D，图片到 3D，几乎无所不能；

2、强大的扩展性，以扩展系统为基础，您可以添加自己的扩展，丰富框架的多样性和功能性；

3、持续激活的更新，作者经常会对新的推理和开源项目进行适配，让框架始终保持最前沿的状态。

以下是一些生成效果：

![](https://github.com/threestudio-project/threestudio/assets/22424247/bf2d2213-5027-489c-a6ba-1c56c14ee8b7)

![](https://github.com/threestudio-project/threestudio/assets/19284678/1dbdebab-43d5-4830-872c-66b38d9fda92)
![](https://github.com/threestudio-project/threestudio/assets/19284678/437b4044-142c-4e5d-a406-4d9bad0205e1)
![](https://github.com/threestudio-project/threestudio/assets/19284678/4f4d62c5-2304-4e20-b632-afe6d144a203)
![](https://github.com/threestudio-project/threestudio/assets/19284678/2f36ddbd-e3cf-4431-b269-47a9cb3d6e6e)

###### 如何使用

以下是一个在 Ubuntu20.04 系统中测试过可行的安装步骤（其他系统也可根据该步骤试一试）：

1、确保你拥有至少 6GB 显存的 NVIDIA 显卡并已安装 CUDA。

2、安装 `Python>=3.8`。

3、（可选）创建虚拟环境并激活。

4、安装 `PyTorch>=1.12`。

5、安装 ninja 来加快编译 CUDA 扩展的速度。

6、使用`pip install -r requirements.txt`来安装依赖项。

具体的使用示例可参考项目 README，比如如果要按一个图片生成 3D 效果，大致代码如下：

```bash
python launch.py --config configs/stable-zero123.yaml --train --gpu 0 data.image_path=./load/images/2d_image.png
```

###### 项目推介

ThreeStudio 是跟进各种最新技术趋势并快速应用到框架中的开源项目，其成功地为广大从事 3D 内容创作的工程师、艺术家提供了一个一站式解决方案。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=threestudio-project/threestudio&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/threestudio-project/threestudio 

开源项目作者：threestudio-project

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=threestudio-project/threestudio)

关注我们，一起探索有意思的开源项目。

