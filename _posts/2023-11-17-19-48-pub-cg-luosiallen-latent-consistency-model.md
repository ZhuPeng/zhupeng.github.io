---
layout: post
title: LatentConsistencyModels - 通过少量步骤生成高分辨率图像的强大工具
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在很多应用场景中，例如游戏开发、电影特效制作等，我们通常需要根据一些以文本形式给出的场景描述，生成对应的高分辨率图像。然而，由于语言与视觉信息之间的复杂关系，这是一个非常具有挑战性的任务。许多现有的模型需要大量的计算资源，且常常需要经过大量的迭代和优化才能生成满意的结果。在这种情况下，Latent Consistency Models （潜在一致模型）应运而生，这是一个能够快速生成高分辨率图像的模型。

GitHub 开源项目 luosiallen/latent-consistency-model 在 GitHub 有超过 2.1k Star，用一句话介绍该项目就是：“Latent Consistency Models: Synthesizing High-Resolution Images with Few-Step Inference”。
![](https://raw.githubusercontent.com/luosiallen/latent-consistency-model/master/./lcm_logo.png)

以下是使用以上项目，对图片加文字生成新的图片的示例：

![](https://raw.githubusercontent.com/luosiallen/latent-consistency-model/master//img2img_demo/taylor.png)
![](https://raw.githubusercontent.com/luosiallen/latent-consistency-model/master//img2img_demo/elon.png)

###### 项目介绍

Latent Consistency Models 是一个旨在通过少量步骤就能生成高分辨率图像的强大工具。它提供了三个版本的 LCM-LoRA （潜在一致模型 - 洛拉）模型，用以适应不同的需求。此外，该项目还发布了两个全参数优化的 LCM，以进一步提高图像生成的效果。所有的模型和工具对开发者和研究人员都是完全开放的。

以下是经过多步推理的效果差异展示：

![](https://raw.githubusercontent.com/luosiallen/latent-consistency-model/master/teaser.png)

在最新的更新中，作者提供了 LCM 的训练脚本，用户可以更容易地定制和优化模型。同时，项目也加入了 LCM-LoRA，一种新的无训练加速模块。这个功能提供了技术报告和 Hugging Face 博客以供用户参考。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231217224300925.png)

###### 如何使用

对于代码类相关的项目，项目的 Github 主页上提供了详细的代码使用示例。你可以根据说明进行安装和使用，并且该项目还有许多 Demo 供你参考。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231217224441965.png)

你需要首先通过 pip 安装依赖库，然后通过执行 app.py 启动 Gradio。使用浏览器打开`http://localhost:7860`即可查看模型的生成结果。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231217224356682.png)

如果你想自己直接通过代码使用模型，也可以参考如下代码：

```python
from diffusers import DiffusionPipeline
import torch

pipe = DiffusionPipeline.from_pretrained("SimianLuo/LCM_Dreamshaper_v7")

# To save GPU memory, torch.float16 can be used, but it may compromise image quality.
pipe.to(torch_device="cuda", torch_dtype=torch.float32)

prompt = "Self-portrait oil painting, a beautiful cyborg with golden hair, 8k"

# Can be set to 1~50 steps. LCM support fast inference even <= 4 steps. Recommend: 1~8 steps.
num_inference_steps = 4 

images = pipe(prompt=prompt, num_inference_steps=num_inference_steps, guidance_scale=8.0, lcm_origin_steps=50, output_type="pil").images
```

###### 项目推介

该项目由经验丰富的计算机科学家 Sialuo Luo 创建和维护。至今，它已经受到了许多开发者和研究人员的广泛关注和使用。尽管该项目仍在持续更新和改进中，但其已经展现出强大的功能和实用性。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231217224729440.png)


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=luosiallen/latent-consistency-model&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/luosiallen/latent-consistency-model 

开源项目作者：luosiallen

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=luosiallen/latent-consistency-model)

关注我们，一起探索有意思的开源项目。

