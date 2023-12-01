---
layout: post
title: GitHub 开源项目 Ma-Lab-Berkeley/CRATE 介绍，Code for CRATE (Coding RAte reduction TransformEr).
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 Ma-Lab-Berkeley/CRATE，该项目在 GitHub 有差不多 1000 Star，用一句话介绍该项目就是：“Code for CRATE (Coding RAte reduction TransformEr).”。


![](https://raw.githubusercontent.com/Ma-Lab-Berkeley/CRATE/master/figs/fig_objective.png)
![](https://raw.githubusercontent.com/Ma-Lab-Berkeley/CRATE/master/figs/fig1.png)
![](https://raw.githubusercontent.com/Ma-Lab-Berkeley/CRATE/master/figs/fig_arch.png)
![](https://raw.githubusercontent.com/Ma-Lab-Berkeley/CRATE/master/figs/fig3.png)
![](https://raw.githubusercontent.com/Ma-Lab-Berkeley/CRATE/master/figs/fig_seg.png)
![](https://raw.githubusercontent.com/Ma-Lab-Berkeley/CRATE/master/figs/fig5.png)



//arxiv.org/abs/2308.16271) and the [crate NeurIPS-processed paper](https://openreview.net/forum?id=THfl8hdVxH#). 

## Citation
If you find the CRATE useful for your research, please consider citing our work:
```bibtex
@article{CRATE,
  author    = {Yaodong Yu, Shengbang Tong, Tianzhe Chu, Ziyang Wu, Druv Pai, Sam Buchanan, Benjamin D Haeffele, and Yi Ma},
  title     = {White-Box Transformers via Sparse Rate Reduction},
  journal   = {NeurIPS},
  year      = {2023},
}
```

```
背景介绍：
在现今计算机视觉领域，我们决胜的挑战是如何简化处理并优化模型性能。处理数据的速度和效率是关键，并且数据稀疏性是一种解决这一问题的重要方式。数据稀疏性不仅可以提升处理速度，还能通过使用更少的参数，简化数据结构，减少模型大小，便于存储和传输。CRATE 项目就是专门为解决这个问题而创建的。

项目介绍：
CRATE (Coding RAte reduction TransformEr) 是一个白箱（可解析）变压器架构，每一层执行一个交替最小化算法的单步，以优化稀疏率减少目标。CRATE 的优点主要在于白箱性的构建，以及其具济白箱化转换，可以有效地解决数据稀疏性问题。其中的 MSSA（Multi-Head Subspace Self-Attention）块和 ISTA（Iterative Shrinkage-Thresholding Algorithms）块，可以进行单步间的转换，实现对链路的优化。

如何使用：
对于代码使用，提供了相应的代码示例，可据此进行安装和使用。CRATE 模型可以使用以下代码定义：
```python
from model.crate import CRATE
dim = 384
n_heads = 6
depth = 12
model = CRATE(image_size=224,
              patch_size=16,
              num_classes=1000,
              dim=dim,
              depth=depth,
              heads=n_heads,
              dim_head=dim // n_heads)
```
此外，CRATE 项目还提供了与图像识别的训练代码和模型微调，可根据实际场合进行调整。

项目推介：
CRATE 是 MAlab-Berkeley 团队的一项开源项目，该团队在机器学习和人工智能方面有着深厚的研究基础，以及丰富的项目实施经验。该项目已经也在 NeurIPS-2023 年会议上被讨论提到，并获得了相应的认可并且使用。此外，这个项目也被其他人用作实际项目，以适应各种环境和场合。如果你对数据稀疏化有需要，不妨试试这个项目。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=Ma-Lab-Berkeley/CRATE&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/Ma-Lab-Berkeley/CRATE 

开源项目作者：Ma-Lab-Berkeley

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=Ma-Lab-Berkeley/CRATE)

关注我们，一起探索有意思的开源项目。

