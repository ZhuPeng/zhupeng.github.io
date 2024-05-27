---
layout: post
title: 可在手机端部署的大模型
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在自然语言处理领域，语言模型是一个重要的维度，它是理解和生成人类自然语言的关键工具。然而，目前的大部分语言模型都存在着计算量大、存储空间需求高和部署困难等问题。这在一定程度上限制了语言模型的应用范围和效果，特别是对于端侧设备，这些问题更加突出。

今天要给大家推荐一个 GitHub 开源项目 MiniCPM，该项目在 GitHub 有超过 3.9k Star

![image-20240515232903859](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240515232903859.png)

用一句话介绍该项目就是：MiniCPM-2B: An end-side LLM outperforms Llama2-13B.
![](https://raw.githubusercontent.com/OpenBMB/MiniCPM/master/./assets/creation.case1.png)

![](https://raw.githubusercontent.com/OpenBMB/MiniCPM/master/./assets/code.case1.gif)

###### 项目介绍

MiniCPM 是面壁智能与清华大学自然语言处理实验室共同开源的系列端侧大模型。MiniCPM 是一个有 24 亿非词嵌入参数量的大型语言模型，具有出色的性能表现。通过 SFT 与 DPO 的优化，MiniCPM 在各种公开的评测集上，包括 MTBench 等，都展现出优秀的性能，甚至超越了 Llama2-13B、MPT-30B、Falcon-40B 等现有的模型。值得一提的是，MiniCPM 还能以 Int4 的形式进行量化，准确率损失较小，既降低了存储和计算的成本，还使得模型能在手机等端侧设备上顺利部署，实现实时推理。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240515222433571.png)

但是小模型也是有一定的局限性的，参考如下：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240320223510217.png)

###### 如何使用

如果想要使用 MiniCPM，只需安装 transformers 库和 accelerate 库，然后通过 AutoModelForCausalLM 和 AutoTokenizer 从网络云服务中即时地获取模型和字典。例如:

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

torch.manual_seed(0)
path = 'openbmb/MiniCPM-2B-dpo-bf16'
tokenizer = AutoTokenizer.from_pretrained(path)
model = AutoModelForCausalLM.from_pretrained(path)
responds, history = model.chat(tokenizer, "山东省最高的山是哪座山, 它比黄山高还是矮？差距多少？")
print(responds)
```
在这个例子中，我们使用了预先训练好的 MiniCPM-2B 模型，然后直接利用 chat 方法进行交互式对话。

###### 项目推介

MiniCPM 不仅在公开评测中显示出了优秀的性能，还继承了面壁智能长期以来对于开放性技术的理念，提供了全面的开源代码和模型，并且会不定期进行更新优化，供广大开发者和研究者进行使用和二次开发。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240320223651775.png)


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=OpenBMB/MiniCPM&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/OpenBMB/MiniCPM 

开源项目作者：OpenBMB

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=OpenBMB/MiniCPM)

关注我们，一起探索有意思的开源项目。

