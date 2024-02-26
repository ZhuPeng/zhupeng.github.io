---
layout: post
title: 一套 SDK 无缝适配上百种大模型平台
tags: 
---

大家好，又见面了，我是 GitHub 精选君！

###### 项目背景

在繁琐的开发过程中，我们经常会遇到大量不同的 LLM API 调用需求，例如我们需要在 Bedrock、Azure、OpenAI、Cohere、Anthropic、Ollama、Sagemaker、HuggingFace、Replicate 等 100 多个 LLM 平台之间进行切换，而这些 LLM 开放的 API 可能是完全不同的。对于每个不同的平台，都需要进行额外的 API 输出转换、异常处理和负载均衡等额外操作，不仅消耗了我们大量的时间，而且这无疑给我们的开发过程增加了不必要的复杂性。

今天要给大家推荐一个 GitHub 开源项目 litellm，该项目在 GitHub 有超过 3.9k Star，用一句话介绍该项目就是：“Call all LLM APIs using the OpenAI format. Use Bedrock, Azure, OpenAI, Cohere, Anthropic, Ollama, Sagemaker, HuggingFace, Replicate (100+ LLMs)”。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240202152454618.png)

###### 项目介绍

LiteLLM 提供了统一的 OpenAI 格式，可以让您轻松调用所有的 LLM API。无论您是使用什么平台，LiteLLM 都可以帮到您。它不仅可以翻译输入到提供商的 `completion` 和 `embedding` 端点，还可以确保一致的输出，文本响应将始终在 `['choices'][0]['message']['content']` 处可用。此外，LiteLLM 还能够映射所有提供商常见的异常，这样我们就可以只关心软件构造，而不必为不同平台的异常类型头疼了。另外，LiteLLM 还支持负载均衡，对于多个部署（比如 Azure/OpenAI），项目的 `Router` 可以处理 1k+ 请求/秒，极大地提高了我们的工作效率。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240202152957739.png)

如何使用：

输入以下代码即可快速安装使用：

```bash
pip install litellm
```
然后在 python 代码中引入 LiteLLM，设置 ENV 变量，即可无缝调用不同的 LLM 平台。以下是一个示例：
```python
from litellm import completion
import os

## set ENV variables 
os.environ["OPENAI_API_KEY"] = "your-openai-key" 
os.environ["COHERE_API_KEY"] = "your-cohere-key" 

messages = [{ "content": "Hello, how are you?","role": "user"}]

# openai call
response = completion(model="gpt-3.5-turbo", messages=messages)

# cohere call
response = completion(model="command-nightly", messages=messages)
print(response)
```

###### 项目推介

LiteLLM 适用于各种使用多种 LLM 平台进行开发的场景，可以为你节省宝贵的时间，减轻切换不同 LLM 平台的压力。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=BerriAI/litellm&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/BerriAI/litellm 

开源项目作者：BerriAI

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=BerriAI/litellm)

关注我们，一起探索有意思的开源项目。

