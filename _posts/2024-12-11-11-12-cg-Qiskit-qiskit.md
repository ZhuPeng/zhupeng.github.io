---
layout: post
title: GitHub 开源项目 Qiskit/qiskit 介绍，Qiskit is an open-source SDK for working with quantum computers at the level of extended quantum circuits, operators, and primitives.
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 Qiskit/qiskit，该项目在 GitHub 有超过 5.4k Star。

![](https://stats.deeptrain.net/repo/Qiskit/qiskit/?theme=light)

一句话介绍该项目：Qiskit is an open-source SDK for working with quantum computers at the level of extended quantum circuits, operators, and primitives.





###### 项目介绍

### 背景介绍

随着量子计算的飞速发展，越来越多的科学家、工程师和爱好者对探索量子世界充满了兴趣。但是，量子计算的复杂性及其与传统计算机体系结构的巨大差异，使得在此领域内的研究和实验面临着巨大的技术壁垒。其中，核心的痛点在于如何将抽象的量子计算理论与具体的量子硬件设备相结合，以及如何优化和模拟量子电路等。为了降低这些技术壁垒，需要一个强大且易于使用的工具来辅助量子计算的研究和开发。

### 

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-1a4b5e3b6a5c156c4c27ed00786ea0a4.png)

项目介绍

**Qiskit** 是一个开源的量子计算软件开发工具包 (SDK)，专注于以扩展量子电路、运算符和基元的层面与量子计算机进行交互。该项目主要解决了创建和优化量子电路、模拟量子算法的实际操作问题，并且提供了一个量子信息工具箱来构建高级运算符。Qiskit 包含的量子电路转换器支持优化量子电路，而且提供了基本函数（Sampler 和 Estimator）来完成测量和估算。

Qiskit 的设计要点在于其模块化的架构，旨在易用性和可扩展性之间找到平衡。它为研究人员、开发人员提供了强大的接口去快速实验和实施量子算法，同时保持与量子硬件的兼容性。

### 如何使用

安装 **Qiskit** 非常简单，推荐通过 `pip` 安装：

```bash
pip install qiskit
```

安装后，您可以迅速开始您的第一个量子程序。例如，创建和执行一个简单的量子电路：

```python
import numpy as np
from qiskit import QuantumCircuit

# 创建量子电路
qc_example = QuantumCircuit(3)
qc_example.h(0)          # 生成超位置态
qc_example.p(np.pi/2,0)  # 添加量子相位
qc_example.cx(0,1)       # 控制非门
qc_example.cx(0,2)       

# 使用 Sampler 测量全部量子位
from qiskit.primitives import StatevectorSampler
qc_measured = qc_example.measure_all(inplace=False)
sampler = StatevectorSampler()
job = sampler.run([qc_measured], shots=1000)
result = job.result()
```

此外，Qiskit 还提供了多种优化和模拟量子电路的高级工具，如转换器（transpiler）和量子信息工具箱。

### 项目推介

**Qiskit** 是由 IBM 主导开发的，拥有活跃的开发社区和丰富的学习资源。它支持 IBM 的量子硬件，对初学者和研究人员都非常友好。项目自诞生以来，已经吸引了包括谷歌、微软等在内的众多科技巨头和研究机构的关注和使用。

该项目不仅活跃在开发者社区，还定期更新和发布新版本，确保功能的先进性和稳定性。由于 Qiskit 的通用性和易用性，许多重要的量子计算研究和创新都是基于这个平台进行的。无论您是量子计算的学生、研究者还是爱好者，Qiskit 都能为您的研究和开发工作提供强大的支持和便利。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=Qiskit/qiskit&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/Qiskit/qiskit 

开源项目作者：Qiskit

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=Qiskit/qiskit)

关注我们，一起探索有意思的开源项目。

