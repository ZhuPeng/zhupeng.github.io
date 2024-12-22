---
layout: post
title: 一个工具库无缝切换多种大模型提供商
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在当今快速发展的人工智能领域，生成式AI（Generative AI）技术的应用范围不断扩大，从文本生成、代码辅助，到多媒体内容创作等，其潜力几乎无所不包。然而，开发者在尝试利用这些先进技术时，常常面临一个核心问题：不同的生成式AI提供商（如OpenAI、Google等）提供的接口各不相同，这不仅大大增加了学习和适应的成本，还使得切换供应商或者对比不同供应商的结果变得异常困难。这种碎片化对于寻求最佳解决方案的开发者来说是一个巨大的障碍。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241219213823088.png)

今天要给大家推荐一个 GitHub 开源项目 aisuite，该项目在 GitHub 有超过 8.9k Star。

![](https://stats.deeptrain.net/repo/andrewyng/aisuite/?theme=light)

一句话介绍该项目：Simple, unified interface to multiple Generative AI providers 

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241219213011124.png)

###### 项目介绍

aisuite 是一个简单、统一的接口，支持多个生成式 AI 提供商。它旨在为开发者提供一个标准化的交互方式，使得与最受欢迎的大型语言模型（LLM）进行互动和对比成为可能。通过像 OpenAI 那样的接口设计，`aisuite` 让开发者可以轻松切换不同的 LLM 提供商而无需更改代码，将各个提供商的 python 客户端库封装在一个简单的接口之下。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241219213621559.png)

主要特点与功能如下：

1、简化了与多个 LLM 提供商对接的过程：目前支持 OpenAI、Anthropic、Azure、Google、AWS 等主要供应商。

2、易于安装和配置：通过几条简单的命令即可安装和配置 `aisuite`，支持安装特定供应商的扩展包。

3、灵活的 API 密钥管理：允许通过环境变量或直接在构造函数中传递配置来管理 API 密钥。

4、开放式贡献模式：鼓励社区贡献，易于添加新的供应商支持。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241219213314141.png)

###### 如何使用

通过 pip 即可安装：

```shell
pip install aisuite
```

若需要安装特定提供商的库，可以通过以下命令实现：

```shell
pip install 'aisuite[anthropic]'
```

设置 API 密钥，然后就可以开始使用了。以下是一个简单的例子：

```python
import aisuite as ai

client = ai.Client()
models = ["openai:gpt-4o", "anthropic:claude-3-5-sonnet-20240620"]
messages = [
    {"role": "system", "content": "Respond in Pirate English."},
    {"role": "user", "content": "Tell me a joke."},
]

for model in models:
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.75
    )
    print(response.choices[0].message.content)
```

###### 项目推介

aisuite 的代码库被积极维护，不断更新，以支持更多的 LLM 提供商和功能。对于要在项目中使用生成式 AI 的开发者来说，`aisuite` 大大简化了代码的复杂性，使得切换和对比不同的 AI 提供者变得非常简单。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=andrewyng/aisuite&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/andrewyng/aisuite 

开源项目作者：andrewyng

开源协议：MIT License

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=andrewyng/aisuite)

关注我们，一起探索有意思的开源项目。

