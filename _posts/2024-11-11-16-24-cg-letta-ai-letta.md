---
layout: post
title: GitHub 开源项目 letta-ai/letta 介绍，Letta (formerly MemGPT) is a framework for creating LLM services with memory.
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 letta-ai/letta，该项目在 GitHub 有超过 12.5k Star。

![](https://stats.deeptrain.net/repo/letta-ai/letta/?theme=light)

一句话介绍该项目：Letta (formerly MemGPT) is a framework for creating LLM services with memory.




![](https://raw.githubusercontent.com/letta-ai/letta/master/assets/Letta-logo-RGB_GreyonOffBlack_cropped_small.png)

![](https://raw.githubusercontent.com/letta-ai/letta/master/assets/letta_ade_screenshot.png)


###### 项目介绍

### **Letta （前身为 MemGPT）：构建具备记忆能力的 LLM 服务的开源框架**

在日益增长的人工智能领域，智能代理的建立和管理已经变得至关重要。然而，当前大多数的语言模型（LLM）和 AI 服务面临着一个共同的挑战——状态不持续性和记忆缺失。这意味着 AI 在进行复杂交互或需要基于历史信息做出决策时往往表现不佳。这不仅限制了 AI 应用的复杂度，而且在用户体验上也造成了明显的断层。

此背景下，**Letta** 应运而生。作为一个开源框架，Letta 专注于构建具备状态和记忆能力的语言模型（LLM）应用。这不仅提高了智能代理的交互质量，还大幅增强了它们的推理能力和信息处理能力，让它们能更加自然地与用户交流，记住并利用以往的交流内容。

#### **核心功能及设计亮点**

- **状态性和记忆能力**：Letta 的最大特色在于打造了具有长期记忆和透明记忆能力的状态性代理。
- **白盒框架**：Letta 是一个模型不可知的白盒框架，带来更高的自定义性和透明度。
- **适应性强**：支持多种数据库后端，如 SQLite 和 Postgres，为开发者提供灵活的选择。
- **简易上手**：提供了快速安装和运行的指引，通过 `pip` 或 Docker 都可轻松部署。

#### **如何使用 Letta**

1. 通过 `pip` 安装 Letta：
    ```sh
    $ pip install -U letta
    ```

2. 设置环境变量，例如为 OpenAI 或其他 LLM / 嵌入式提供商：
    ```sh
    $ export OPENAI_API_KEY=sk-...
    ```

3. 运行 Letta CLI，创建并与智能代理进行对话：
    ```sh
    $ letta run
    ```

4. 启动 Letta 服务器：
    ```sh
    $ letta server
    ```

#### **为什么选择 Letta**

Letta 不仅是一个技术进步的展示，它的创建和维护也展示了一个积极的开源社区参与实践。由超过一百名贡献者共同构建，跨越了学术和工业界的界限，Letta 得到了来自不同领域专家的测试和验证。无论是开发人员寻找构建复杂、记忆性强的 LL 系统的解决方案，还是研究人员探索语言理解的新领域，Letta 都提供了强大工具和活跃的社区支持。

此外，Letta 的文档详尽、上手指南完善，并提供了灵活的部署选项，无论是面对个人项目还是企业级应用，Letta 都能提供所需的支持和灵活性。考虑到其开放性、扩展性以及在前沿技术领域的应用潜力，Letta 确实是一个值得关注和参与的开源项目。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=letta-ai/letta&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/letta-ai/letta 

开源项目作者：letta-ai

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=letta-ai/letta)

关注我们，一起探索有意思的开源项目。

