---
layout: post
title: GitHub 开源项目 aaamoon/copilot-gpt4-service 介绍，Convert Github Copilot to ChatGPT
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 aaamoon/copilot-gpt4-service，该项目在 GitHub 有超过 8.1k Star，用一句话介绍该项目就是：“Convert Github Copilot to ChatGPT”。





背景介绍：
在进行联机聊天或语言理解的过程中，我们往往需要一种技术可以将接收明确指令的程序自然地转化为可以接收特定要求的人工智能。然而传统的技术处理起来过于复杂，可能会存在兼容性问题，且对输入类型的需求过于苛刻，即使是一些乱序的字符串或数字都可能导致程序错误。这就是我们为什么需要 "Copilot-GPT4-Service" 项目。

项目介绍：
"Copilot-GPT4-Service" 开源项目的目标是将 GitHub Copilot 转化为 ChatGPT，让你可以更自由地在各种平台上进行交互。项目所支持的 API 包括获取首页，健康检查，获取模型列表，聊天 API，以及用于嵌入的 API。最值得注意的是，和 OpenAI API 不同的是，这个服务只接受前两种类型以及包含字符串的数组数组。

如何使用：
首先，你需要安装并启动 copilot-gpt4-service，例如，在本地启动后，API 的默认地址是：`http://127.0.0.1:8080`；然后，获取你的 GitHub 账户的 GitHub Copilot 插件 Token；最后，安装第三方客户端，例如，[ChatGPT-Next-Web](https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web)，并在设置中填入 copilot-gpt4-service 的 API 地址和 GitHub Copilot 插件 Token，就可以使用 GPT-4 模型进行对话了。

项目推介：
"copilot-gpt4-service" 是 Github Copilot 和 ChatGPT 的成功融合，它让你可以使用 GPT-4 模型在各种平台上进行自由对话。考虑到部署和安全因素，项目有一套详细的部署方法和注意事项，并且也列出了不被推荐的部署方法，避免因为违反 GitHub Copilot 的规定而被封禁。它的独特之处在于，你完全可以自己定义独立的 token 来访问服务，保证了服务的安全性。这个项目最近在开源社区中的活跃度非常高，并且已经有很多知名的开源项目采用了它，如：[Chatbox](https://github.com/Bin-Huang/chatbox)，[OpenCat APP](https://opencat.app/)，[ChatX APP](https://apps.apple.com/us/app/chatx-ai-chat-client/id6446304087)。总的来说，无论你是希望为个人用途还是为公共场合提供强大的聊天功能，"copilot-gpt4-service" 都是你最佳的选择。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=aaamoon/copilot-gpt4-service&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/aaamoon/copilot-gpt4-service 

开源项目作者：aaamoon

开源协议：MIT License

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=aaamoon/copilot-gpt4-service)

关注我们，一起探索有意思的开源项目。

