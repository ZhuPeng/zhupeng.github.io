---
layout: post
title: GitHub 开源项目 TEN-framework/TEN-Agent 介绍，TEN Agent is a conversational AI powered by TEN, integrating Gemini 2.0 Multimodal Live API, OpenAI Realtime API, RTC, and more. It offers real-time capabilities to see, hear, and speak, along with advanced tools like weather checks, web search, and RAG.
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 TEN-framework/TEN-Agent，该项目在 GitHub 有超过 3.2k Star。

![](https://stats.deeptrain.net/repo/TEN-framework/TEN-Agent/?theme=light)

一句话介绍该项目：TEN Agent is a conversational AI powered by TEN, integrating Gemini 2.0 Multimodal Live API, OpenAI Realtime API, RTC, and more. It offers real-time capabilities to see, hear, and speak, along with advanced tools like weather checks, web search, and RAG.




![TEN Agent banner](https://github.com/TEN-framework/docs/blob/main/assets/jpg/banner.jpg?raw=true)

![Usecases](https://github.com/TEN-framework/docs/blob/main/assets/jpg/gemini-with-ten.jpg?raw=true)

![Usecases](https://github.com/TEN-framework/docs/blob/main/assets/gif/gemini.gif?raw=true)

![Usecases](https://github.com/TEN-framework/docs/blob/main/assets/jpg/usecases.jpg?raw=true)

![Ready-to-use Extensions](https://github.com/TEN-framework/docs/blob/main/assets/jpg/extensions.jpg?raw=true)

![Docker Setting](https://github.com/TEN-framework/docs/blob/main/assets/gif/docker_setting.gif?raw=true)

![Module Example](https://github.com/TEN-framework/docs/blob/main/assets/gif/module-example.gif?raw=true)

![Gemini Realtime Playground](https://github.com/TEN-framework/docs/blob/main/assets/gif/gemini-playground.gif?raw=true)

![Components Diagram](https://github.com/TEN-framework/docs/blob/main/assets/jpg/diagram.jpg?raw=true)

![TEN star us gif](https://github.com/TEN-framework/docs/blob/main/assets/gif/star_us_2.gif?raw=true)


###### 项目介绍

### **背景介绍**

在数字化时代，人工智能 (AI) 聊天代理的需求日益增长，它们不仅能够提升用户体验、增强客户服务质量，还能在数据分析、即时信息检索等领域发挥巨大作用。然而，创建一个功能强大的AI聊天代理面临着种种挑战：如何集成多种API实现多模态交互、确保实时响应、并且提高用户交互的自然性和准确性。这些问题是建立有效AI聊天系统的核心痛点。

### **

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-3bdafd170d85efb14177219648e1ed0e.png)

项目介绍**

**TEN Agent** 是一个由 **TEN** 框架支持的会话 AI，它集成了 **Gemini 2.0 Multimodal Live API**、**OpenAI Realtime API**、实时通信 (RTC) 等先进技术。该项目旨在提供实时的看、听和说的能力，配备了高级工具比如天气检查、网页搜索和 RAG 。通过融合多种API和功能，**TEN Agent** 能够处理复杂的情景并提供多模态的交互体验。

### **如何使用**

**安装步骤**:

1. 确保你的系统满足最低要求：CPU >= 2核，RAM >= 4GB。
2. 安装 **Docker** / **Docker Compose** 和 **Node.js(LTS) v18**。
3. 克隆 Repo 并创建 `.env` 文件：

```bash
cp ./.env.example ./.env
```

4. 在 `.env` 文件中配置 Agora App ID 和 App Certificate 。

```bash
AGORA_APP_ID=
AGORA_APP_CERTIFICATE=
```

5. 启动代理开发容器：

```bash
docker compose up -d
```

6. 进入容器，构建代理并启动web服务：

```bash
docker exec -it ten_agent_dev bash
task use
task run
```

7. 在浏览器中打开 [localhost:3000](http://localhost:3000)，配置你的代理。

**示例代码**: (如何运行 Gemini 实时扩展)

- 选择 voice_assistant_realtime 图。
- 选择 Gemini Realtime 模块。
- 选择 v2v 扩展并输入 Gemini API密钥。

### **项目推介**

**TEN Agent** 是一个活跃发展中的项目，具备了强大的多模态AI交互能力。它不仅集成了高级实时API，如 **OpenAI** 和 **Gemini 2.0**，还提供了开箱即用的扩展，如天气检查和Web搜素等。该项目由 **TEN-framework** 维护，这是一个在开源社区享有盛誉的团队，其对于项目的持续投入保证了技术的前沿性和稳定性。

目前，**TEN Agent** 已经吸引了大量开发者的关注，其社区活跃且不断扩大，为用户提供了丰富的交流和协作平台，如 Discord 服务器和 GitHub 讨论区。不管是企业还是个人开发者，都可以通过 **TEN Agent** 构建高效、智能的AI聊天体验，提升服务质量和用户互动。

此外，该项目遵循Apache 2.0许可证，确保了良好的开源生态和使用灵活性。无论是在技术还是社区方面，**TEN Agent** 都展现出巨大的潜力和价值，强烈推荐给所有寻求构建高级AI聊天代理的开发者和团队。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=TEN-framework/TEN-Agent&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/TEN-framework/TEN-Agent 

开源项目作者：TEN-framework

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=TEN-framework/TEN-Agent)

关注我们，一起探索有意思的开源项目。

