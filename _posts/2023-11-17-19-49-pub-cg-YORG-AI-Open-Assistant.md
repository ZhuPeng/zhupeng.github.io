---
layout: post
title: Open Assistant - 在强化的数据隐私保护下更好的使用大模型
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在开发过程中，我们常常需要和各种 AI 助手打交道，以实现各种复杂的任务。然而，许多现有的 AI 助手都有一个共同的问题，即它们都需要在线环境来完成代码执行，并且需要将我们的文件上传到 AI 提供商的服务器上。这样不仅带来了数据隐私、文件大小和数量限制以及基于云的费用等问题，而且在很大程度上限制了开发者的操作灵活性。

今天要给大家推荐一个 GitHub 开源项目 YORG-AI/Open-Assistant，该项目在 GitHub 有超过 1.2k Star，就是尝试更好的解决以上问题。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231217225329064.png)

###### 项目介绍

Open Assistant 项目基于 OpenAI 的助手 API 开发，其主要目标是帮助开发者在本地运行代码、从本地文件中检索知识（无需将其发送到 OpenAI）并提供更多的对开发者友好的工具。项目的核心优势包括强化的数据隐私保护，没有任何文件大小和数量的限制，能够降低使用基于云服务的成本，并提供使用你选择的大型语言模型（LLM）的灵活性。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231217225428827.png)

同时该项目还提供一个 Web 页面方便我们更好的使用：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231217225551356.png)

###### 如何使用

通过如下 pip 命令可以快速安装并使用。

```bash
pip install yorgassistant
```

开始使用之前，首先需要设置好 API Key 和需要使用到的工具，对应如下配置：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231217225846920.png)

对应的工具分为函数（Function）工具以及有状态（Stateful）的工具。都可以通过 Python  的装饰器很容易的进行创建，以下示例为一个 Function Tool ：

```bash
from yorgassistant.core.assistant.tools.tools import register_function_tool
@register_function_tool
def code_test(code: str):
    return {
        "type": "success",
        "content": {
            "result": "Hello, World!",
        },
    }
```

最后就可以开始使用了，以下是一段示例代码，仅供参考：

```python
import yorgassistant
yorgassistant.Threads.set_threads_yaml_path('data/threads.yaml')
yorgassistant.Assistants.set_assistants_yaml_path('data/assistants.yaml')
yorgassistant.Tools.set_tools_yaml_path('tools.yaml')
threads = yorgassistant.Threads.create()
print(threads.id)
assistant = yorgassistant.Assistants.create(name="Test Assistant", model="gpt-4-1106-preview", instructions="Use swe tool auto fix code files", tools=[{'type':'swe_tool'}])
print(assistant.id)

result = threads.run(assistant.id, "Use SoftWare Engineer Agent swe tool auto fix code files.")
print(result)

result = threads.run(assistant.id, "the repo url is https://github.com/YORG-AI/Open-Assistant",goto="stage_1")
print(result)

result = threads.run(assistant.id, "add helloworld feature to readme",  goto="stage_2")
print(result)

result = threads.run(assistant.id, "focus_files_name_list = [README.md]", goto="stage_3")
print(result)

result = threads.run(assistant.id, "action=3", goto="stage_4")
print(result)

result = threads.run(assistant.id, "", goto="stage_5")
print(result)

result = threads.run(assistant.id, "action=0,action_idx=0", goto="stage_6")
print(result)

result = threads.run(assistant.id, "", goto="finish")
print(result)
```

###### 项目推介

虽然项目尚处于早期阶段，但它的独特性和功能丰富性使得它得到了越来越多开发者的关注。如果你正在寻找一款可以强化你的数据隐私，完全控制代码执行环境，节省开发成本并提供丰富的开发工具的 AI 助手，那么 Open Assistant 是你的一个选择。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=YORG-AI/Open-Assistant&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/YORG-AI/Open-Assistant 

开源项目作者：YORG-AI

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=YORG-AI/Open-Assistant)

关注我们，一起探索有意思的开源项目。

