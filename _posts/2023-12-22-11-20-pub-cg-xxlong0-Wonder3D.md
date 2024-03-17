---
layout: post
title: 只需 2 ~ 3 分钟从图像重建详细纹理的 3D 模型
tags: 
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在虚拟实境（VR）、增强实境（AR）和计算机图形领域，3D 模型是重要的元素。但制作质量高、细节丰富的 3D 模型需要专业知识和大量时间。对于那些希望快速、方便地生成 3D 模型的个人或团队，这就成了挑战。我们需要一个解决方案，可以基于单一视图图像快速生成高质量的 3D 模型。

今天要给大家推荐一个 GitHub 开源项目 Wonder3D，该项目在 GitHub 有超过 3.5k Star，用一句话介绍该项目就是：“Single Image to 3D using Cross-Domain Diffusion”。以下是一些生成的示例：


![](https://raw.githubusercontent.com/xxlong0/Wonder3D/master/assets/fig_teaser.png)

###### 项目介绍

Wonder3D 在只需 2 ~ 3 分钟的时间内，项目可以从单视图图像重建具有高度详细纹理的 3D 网格模型。Wonder3D 首先利用跨域扩散模型生成一致的多视图法线图与对应的颜色图像，然后使用创新的法线融合方法实现快速、高质量的重建。它简化了 3D 模型的创建过程，满足了高效快速的需求。

以下是对应的论文链接：https://arxiv.org/abs/2310.15008

![](https://www.xxlong.site/Wonder3D/assets/pipeline.png)

###### 如何使用

首先，你需要下载并安装 Wonder3D 的源代码。源代码里的用法详细写出了如何使用 Wonder3D。这是一个典型的使用案例:

```python
# First clone the repo, and use the commands in the repo
import torch
import requests
from PIL import Image
import numpy as np
from torchvision.utils import make_grid, save_image
from diffusers import DiffusionPipeline  # only tested on diffusers[torch]==0.19.3, may have conflicts with newer versions of diffusers

def load_wonder3d_pipeline():

    pipeline = DiffusionPipeline.from_pretrained(
    'flamehaze1115/wonder3d-v1.0', # or use local checkpoint './ckpts'
    custom_pipeline='flamehaze1115/wonder3d-pipeline',
    torch_dtype=torch.float16
    )

    # enable xformers
    pipeline.unet.enable_xformers_memory_efficient_attention()

    if torch.cuda.is_available():
        pipeline.to('cuda:0')
    return pipeline

pipeline = load_wonder3d_pipeline()

# Download an example image.
cond = Image.open(requests.get("https://d.skis.ltd/nrp/sample-data/lysol.png", stream=True).raw)

# The object should be located in the center and resized to 80% of image height.
cond = Image.fromarray(np.array(cond)[:, :, :3])

# Run the pipeline!
images = pipeline(cond, num_inference_steps=20, output_type='pt', guidance_scale=1.0).images

result = make_grid(images, nrow=6, ncol=2, padding=0, value_range=(0, 1))

save_image(result, 'result.png')
```

###### 项目推介

该项目目前在 Github 上活跃开发，作者 xxlong0 一直在更新和优化项目，例如近期添加了 GUI 演示和 Windows 支持。根据我们的了解，作者同时也是香港大学的研究者，有着丰富的机器学习、计算机图形学和 3D 重建的经验。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=xxlong0/Wonder3D&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/xxlong0/Wonder3D 

开源项目作者：xxlong0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=xxlong0/Wonder3D)

关注我们，一起探索有意思的开源项目。

