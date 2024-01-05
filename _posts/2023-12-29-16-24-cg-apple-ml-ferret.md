---
layout: post
title: GitHub 开源项目 apple/ml-ferret 介绍，None
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 apple/ml-ferret，该项目在 GitHub 有超过 5.0k Star，用一句话介绍该项目就是：“None”。


![](https://raw.githubusercontent.com/apple/ml-ferret/master/figs/ferret_icon.png)
![](https://raw.githubusercontent.com/apple/ml-ferret/master/figs/ferret_fig_diagram_v2.png)
![](https://raw.githubusercontent.com/apple/ml-ferret/master/figs/ferret_demo.png)



背景介绍：在日常工作中，我们可能需要对一些指定的图像元素进行精准指引和锚定，这样有利于更加深入地从宏观和微观的角度理解图像内容和结构。然而，现有的技术在处理用户语言输入时，无法准确理解和定位对象，也无法在详细级别上提供精准的分析和锚定。比如，我们可能希望机器能更准确地理解如“左上角的绿色苹果”这样的描述，并精准锚定到指定对象上。这就涉及到模型理解语言描述并锚定图像元素的能力，既是精准识别对象，又要保证对语言的准确理解。

项目介绍：Ferret 就是为解决上述问题而生的开源项目。Ferret 是一款端对端的机器学习语言模型，它能对任何形式的引用进行处理，并在响应中锚定任何内容。它包含了混合区域表示和空间感知视觉采样的 Ferret 模型。此外，它还发布了一个大规模、有层级结构且坚韧性强的针对指令调整的数据集 GRIT。在设计上，Ferret 引入了空间感知的视觉采样器和混合区域表示来实现更加精细和开放词汇的引用和定位。同时，该项目使用了多模态评估基准 Ferret-Bench，需要引用/定位，语义，知识和推理的联合要求。

如何使用：首先，你需要克隆 Ferret 项目到你的本地，然后安装所需的库。如果你要进行训练，还需要安装额外的训练用包。你可以调整`per_device_train_batch_size`和`gradient_accumulation_steps`的数值以适应你的 GPU。另外，记住训练时总是要保持全局批量大小一致。项目还提供了训练所需的脚本。在评估阶段，你可以查看项目的文档以获取详细操作。在进行项目的演示时，你需要本地训练 Ferret 并使用 checkpoints，之后，你可以按照给出的命令步骤依次运行。

项目推介：Ferret 是 Apple 公司开展的开源项目，这是一个在机器学习领域颇有影响力的名字。Ferret 设计理念上的突破能够在很大程度上提升计算机对描绘对象的理解和锚定能力，对于图像分析、人工智能交互等应用场景具有很高的价值。而且，Ferret 项目目前已经开源，甚至你可以完全按照提供的步骤，进行本地演示。让你有机会亲手操作这个由 Apple 制作的前沿研究项目，这是一个非常难得的机会。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=apple/ml-ferret&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/apple/ml-ferret 

开源项目作者：apple

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=apple/ml-ferret)

关注我们，一起探索有意思的开源项目。

