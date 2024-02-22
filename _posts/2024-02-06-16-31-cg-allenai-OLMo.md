---
layout: post
title: GitHub 开源项目 allenai/OLMo 介绍，Modeling, training, eval, and inference code for OLMo
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 allenai/OLMo，该项目在 GitHub 有超过 2.5k Star，用一句话介绍该项目就是：“Modeling, training, eval, and inference code for OLMo”。



![](https://github.com/allenai/OLMo/assets/8812459/774ac485-a535-4768-8f7c-db7be20f5cc3)
![](https://allenai.org/olmo/olmo-7b-animation.gif)



背景介绍：

在计算机语言学领域，我们经常会面临需要准确、快速地训练和应用语言模型的问题。传统的方法往往无法满足日常生产中对于模型质量和运行速度的高要求，而且模型的训练和应用过程繁琐，效率较低。对于科研人员和开发者来说，如何得到一个易于安装、使用并且具有高质量的语言模型一直是一个磨人的问题。

项目介绍：

针对上述问题，AllenAI团队开发了 OLMo（Open Language Model）开源项目（https://github.com/allenai/OLMo）来解决各类难题。此项目主要是用于训练和使用 AI2 的开放语言模型。项目中包含了 OLMo 1B、OLMo 7B 和 OLMo 7B Twin 2T 三种主要模型，它们都是在 Dolma 数据集上进行训练的。

OLMo 项目设计的核心亮点在于提供了一个对于语言模型训练细节的全面管理，不仅让模型训练和应用过程变得更加简洁高效，而且通过封装 PyTorch 不同版本的版本特性，让用户无需过多关注底层细节，只需几行代码就可以轻松上手。

如何使用：

OLMo 项目的安装和使用非常简单。首先需要安装 PyTorch，然后选择从源码安装或者通过 PyPi 安装 OLMo 代码库。以下是从源码安装的步骤：

```bash
git clone https://github.com/allenai/OLMo.git
cd OLMo
pip install -e .[all]
```

如果你想直接通过 PyPi 安装：

```bash
pip install ai2-olmo
```

在项目代码中提供了如何进行模型推理的详细说明和代码示例，例如，下面的代码展示了如何在 Hugging Face 上运行模型推理：

```python
from hf_olmo import * # registers the Auto* classes

from transformers import AutoModelForCausalLM, AutoTokenizer

olmo = AutoModelForCausalLM.from_pretrained("allenai/OLMo-7B")
tokenizer = AutoTokenizer.from_pretrained("allenai/OLMo-7B")

message = ["Language modeling is "]
inputs = tokenizer(message, return_tensors='pt', return_token_type_ids=False)
response = olmo.generate(**inputs, max_new_tokens=100, do_sample=True, top_k=50, top_p=0.95)
print(tokenizer.batch_decode(response, skip_special_tokens=True)[0])
```

项目推介：

此项目由知名的 AI 研究团队 AllenAI 开发和维护，其严苛的代码和模型质量控制让人对此项目深具信心。无论是对于想要深入研究自然语言处理领域的科研人员，还是想要在业务项目中应用语言模型的工程师们，OLMo 都提供了一个可靠的解决方案。推荐大家亲自尝试，体验其技术的深度和广度。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=allenai/OLMo&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/allenai/OLMo 

开源项目作者：allenai

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=allenai/OLMo)

关注我们，一起探索有意思的开源项目。

