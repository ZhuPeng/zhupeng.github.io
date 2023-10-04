---
layout: post
title: Zep - 一个为大模型/聊天应用程序提供长期存储的项目
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在构建LLM / Chatbot应用程序时，我们需要一个长期存储的解决方案，以便存储相关文档、聊天历史记录和丰富的用户数据，以便在应用程序的提示中使用。然而，当前市场上的解决方案大多数都是基于内存的，无法满足长期存储的需求，因此Zep 项目应运而生。

Zep 在 GitHub 有 1k 左右 Star，用一句话介绍该项目就是：“Zep: A long-term memory store for LLM / Chatbot applications”。


![](https://github.com/getzep/zep/blob/main/assets/zep-bot-square-200x200.png?raw=true)

###### 项目介绍

Zep 是一个为 LLM 应用程序设计的长期存储解决方案，它不仅可以存储文本和嵌入式信息，还可以存储聊天消息、角色和用户元数据。Zep 还提供了向量数据库和混合搜索功能，可以快速检索相关文档和聊天历史记录。此外，Zep 还提供了嵌入式和丰富功能，可以自动嵌入文本和消息，并使用先进的开源模型、OpenAI 或自定义向量进行丰富。Zep 还支持 Python 和TypeScript / JS SDK，可以轻松集成到您的LLM应用程序中。

###### 如何使用

您可以通过Docker或云部署来快速启动Zep，并使用 Python和TypeScript / JS SDK进行集成。Zep还提供了丰富的API和示例代码，以帮助您更好地了解如何使用Zep。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230819215515548.png)

以下是两个 Python 的使用示例。

1、embedding 向量搜素

```Python
# Search by embedding vector, rather than text query
# embedding is a list of floats
results = collection.search(
    embedding=embedding, limit=5
)
```

2、将聊天历史进行持久化

```python
session_id = "2a2a2a" 

history = [
     { role: "human", content: "Who was Octavia Butler?" },
     {
        role: "ai",
        content:
           "Octavia Estelle Butler (June 22, 1947 – February 24, 2006) was an American" +
           " science fiction author.",
     },
     {
        role: "human",
        content: "Which books of hers were made into movies?",
        metadata={"foo": "bar"},
     }
]


 messages = [Message(role=m.role, content=m.content) for m in history]
 memory = Memory(messages=messages)
 result = await client.aadd_memory(session_id, memory)
```


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=getzep/zep&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/getzep/zep 

开源项目作者：getzep

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=getzep/zep)

关注我们，一起探索有意思的开源项目。

