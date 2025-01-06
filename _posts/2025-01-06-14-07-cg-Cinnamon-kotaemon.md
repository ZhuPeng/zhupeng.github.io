---
layout: post
title: GitHub 开源项目 Cinnamon/kotaemon 介绍，An open-source RAG-based tool for chatting with your documents.
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 Cinnamon/kotaemon，该项目在 GitHub 有超过 19.5k Star。

![](https://stats.deeptrain.net/repo/Cinnamon/kotaemon/?theme=light)

一句话介绍该项目：An open-source RAG-based tool for chatting with your documents.




![Preview](https://raw.githubusercontent.com/Cinnamon/kotaemon/main/docs/images/preview-graph.png)

![Preview](https://raw.githubusercontent.com/Cinnamon/kotaemon/main/docs/images/preview.png)

![Chat tab](https://raw.githubusercontent.com/Cinnamon/kotaemon/main/docs/images/chat-tab.png)

![Models](https://raw.githubusercontent.com/Cinnamon/kotaemon/main/docs/images/models.png)

![](https://abroad.hellogithub.com/v1/widgets/recommend.svg?rid=d3141471a0244d5798bc654982b263eb&claim_uid=RLiD9UZ1rEHNaMf&theme=small)

![](https://raw.githubusercontent.com/Cinnamon/kotaemon/main/docs/images/pdf-viewer-setup.png)


###### 项目介绍

在当今的信息爆炸时代，获取、理解和利用大量文档成了一个普遍而又头疼的问题。我们经常发现自己淹没在海量的报告、文章和手册中，试图从这些文档中找到我们需要的答案。这不仅仅是一个查找的问题，更是一个怎样高效地理解和利用这些文档的信息的难题。面对这个挑战，一个能够简化并加速这个过程的工具显得十分必要。

这就是 `kotaemon` 项目发挥作用的地方。“An open-source RAG-based tool for chatting with your documents.”，`kotaemon` 是一个基于开源的、可清洁和可定制的 RAG 用户界面，旨在与您的文档对话。对于想对他们的文档进行问答（QA）的终端用户来说，以及想要构建自己的 RAG 流水线的开发者而言，都是一个非常实用的工具。

### 项目亮点：
- 对于终端用户，`kotaemon` 提供了一个干净且极简的用户界面，支持多种大型语言模型（LLMs），如 OpenAI, AzureOpenAI, Cohere 等，且安装简单易行。
- 对于开发者而言，提供了一套工具来构建您自己的基于 RAG 的文档 QA 流水线，同时支持自定义 UI，使您能直观地看到 RAG 流水线的运行情况，并利用 Gradio 推出的主题进行开发。
- 支持托管您自己的文档 QA (RAG) 网页 UI，支持多用户登录，私有/公开的文件集合组织，协作和共享您喜爱的对话。
- 通过默认系统提供详细的引用来确保 LLM 答案的正确性，且可以直接在浏览器的 PDF 查看器中查看引用（包括相关分数）和高亮显示。

### 安装使用：
项目提供了基于 Docker 的安装方法，推荐使用 Docker 进行安装和部署。您可以选择 `lite` 或 `full` 版本的 Docker 镜像，对于大多数用户来说，`lite` 版本已经足够使用。安装步骤如下：

```bash
docker run \
-e GRADIO_SERVER_NAME=0.0.0.0 \
-e GRADIO_SERVER_PORT=7860 \
-p 7860:7860 -it --rm \
ghcr.io/cinnamon/kotaemon:main-lite
```
对于需要处理更多文件类型（如 `.doc`, `.docx` 等）的用户，可以选择 `full` 版本。

### 项目推介：
截至目前，`kotaemon` 项目已经得到了社区的广泛关注和积极的反馈。其背后的开发团队 Cinnamon 是在人工智能领域享有盛誉的团队，其为本项目的可靠性和未来的发展提供了强有力的保障。此外，项目已与多个知名的语言模型 API 提供商（如 OpenAI 等）实现了兼容，确保了其广泛的应用场景和实用性。无论您是想快速对文档进行问答，还是想构建并定制自己的 RAG 流水线，`kotaemon` 都是一个值得尝试的项目。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=Cinnamon/kotaemon&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/Cinnamon/kotaemon 

开源项目作者：Cinnamon

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=Cinnamon/kotaemon)

关注我们，一起探索有意思的开源项目。

