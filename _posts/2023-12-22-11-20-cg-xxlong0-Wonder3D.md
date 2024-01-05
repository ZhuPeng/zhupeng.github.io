---
layout: post
title: GitHub 开源项目 xxlong0/Wonder3D 介绍，Single Image to 3D using Cross-Domain Diffusion
tags: 
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 xxlong0/Wonder3D，该项目在 GitHub 有超过 3.5k Star，用一句话介绍该项目就是：“Single Image to 3D using Cross-Domain Diffusion”。


![](https://raw.githubusercontent.com/xxlong0/Wonder3D/master/assets/fig_teaser.png)



背景介绍：
在虚拟实境（VR）、增强实境（AR）和计算机图形领域，3D 模型是重要的元素。但制作质量高、细节丰富的 3D 模型需要专业知识和大量时间。对于那些希望快速、方便地生成 3D 模型的个人或团队，这就成了挑战。我们需要一个解决方案，可以基于单一视图图像快速生成高质量的 3D 模型。

项目介绍：
这就是我们介绍的开源项目 Wonder3D 的作用。在只需 2 ~ 3 分钟的时间内，项目可以从单视图图像重建具有高度详细纹理的 3D 网格模型。Wonder3D 首先利用跨域扩散模型生成一致的多视图法线图与对应的颜色图像，然后使用创新的法线融合方法实现快速、高质量的重建。它简化了 3D 模型的创建过程，满足了高效快速的需求。

如何使用：
首先，你需要下载并安装 Wonder3D 的源代码。源代码里的用法详细写出了如何使用 Wonder3D。这是一个典型的使用案例:

```bash
# 首先克隆仓库，然后使用仓库中的命令

#...这里是一些代码...

pipeline = load_wonder3d_pipeline()

# 下载一个示例图像.
cond = Image.open(requests.get("https://d.skis.ltd/nrp/sample-data/lysol.png", stream=True).raw)

# 运行管道！
images = pipeline(cond, num_inference_steps=20, output_type='pt', guidance_scale=1.0).images

result = make_grid(images, nrow=6, ncol=2, padding=0, value_range=(0, 1))

save_image(result, 'result.png')
```

项目推介：
该项目目前在 Github 上活跃开发，作者 xxlong0 一直在更新和优化项目，例如近期添加了 GUI 演示和 Windows 支持。根据我们的了解，作者同时也是香港大学的研究者，有着丰富的机器学习、计算机图形学和 3D 重建的经验。以他的背景和此项目的高质量来看，我们有理由相信 Wonder3D 将有一个美好的未来。如果你是一个有热情的开发者，热衷于 3D AIGC 的速度、质量和实惠等领域，或者是在寻找一个能够快速从图片生成 3D 模型的解决方案，我们强烈推荐你使用和参与这个项目。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=xxlong0/Wonder3D&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/xxlong0/Wonder3D 

开源项目作者：xxlong0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=xxlong0/Wonder3D)

关注我们，一起探索有意思的开源项目。

