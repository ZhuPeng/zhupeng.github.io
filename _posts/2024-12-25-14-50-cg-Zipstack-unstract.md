---
layout: post
title: GitHub 开源项目 Zipstack/unstract 介绍，No-code LLM Platform to launch APIs and ETL Pipelines to structure unstructured documents
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 Zipstack/unstract，该项目在 GitHub 有超过 3.2k Star。

![](https://stats.deeptrain.net/repo/Zipstack/unstract/?theme=light)

一句话介绍该项目：No-code LLM Platform to launch APIs and ETL Pipelines to structure unstructured documents




![img Prompt Studio](https://raw.githubusercontent.com/Zipstack/unstract/master/docs/assets/prompt_studio.png)

![img Using Unstract](https://raw.githubusercontent.com/Zipstack/unstract/master/docs/assets/Using_Unstract.png)

![](https://raw.githubusercontent.com/Zipstack/unstract/master/https://raw.githubusercontent.com/Zipstack/unstract/master/docs/assets/unstract_u_logo.png)

![](https://raw.githubusercontent.com/Zipstack/unstract/master/https://raw.githubusercontent.com/Zipstack/unstract/master/docs/assets/3rd_party/openai.png)

![](https://raw.githubusercontent.com/Zipstack/unstract/master/docs/assets/3rd_party/vertex_ai.png)

![](https://raw.githubusercontent.com/Zipstack/unstract/master/https://raw.githubusercontent.com/Zipstack/unstract/master/https://raw.githubusercontent.com/Zipstack/unstract/master/docs/assets/3rd_party/azure_openai.png)

![](https://raw.githubusercontent.com/Zipstack/unstract/master/docs/assets/3rd_party/anthropic.png)

![](https://raw.githubusercontent.com/Zipstack/unstract/master/https://raw.githubusercontent.com/Zipstack/unstract/master/docs/assets/3rd_party/ollama.png)

![](https://raw.githubusercontent.com/Zipstack/unstract/master/docs/assets/3rd_party/bedrock.png)

![](https://raw.githubusercontent.com/Zipstack/unstract/master/https://raw.githubusercontent.com/Zipstack/unstract/master/docs/assets/3rd_party/palm.png)


###### 项目介绍

### 背景介绍

在当今快速迭代的信息时代，处理文档已成为企业、开发者和数据分析师日常工作的一部分。然而，他们通常面临的一个主要挑战是如何有效地处理和提取非结构化文档中的信息。非结构化数据，如 PDFs、电子邮件、图片和文本文件，往往含有大量的重要信息，但由于缺乏标准化格式，使得数据提取变得复杂和耗时。传统的数据处理方法往往需要大量的手工劳动或复杂的编码工作。而且，随着数据量的增加，这些方法变得不再可行，从而迫切需要一种更高效、更智能的解决方案。

### 

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-81bd4aa72d1f485ad6ade20922dcbc78.png)

项目介绍

**Unstract** 是一个基于大型语言模型（LLM）的智能文档处理（IDP）2.0 平台，旨在无需编码即可启动 API 和 ETL 管道，以结构化非结构化文档。该项目提供了一个强大的 **Prompt Studio** 工具，允许用户高效地开发文档数据提取所需的提示，并享受快速开发和迭代的乐趣。同时，**Workflow Studio** 助力自动化涉及复杂文档的关键商业流程，超越传统的 RPA，利用大型语言模型的力量进一步简化处理过程。

- **主要功能**：通过简化的三步骤，用户可将文档添加到无码 **Prompt Studio**，进行提示工程以提取所需字段，然后配置并部署为结构化数据 API 或 ETL 管道。
- **设计要点**：项目支持 Linux 或 MacOS 系统，并依赖 Docker 容器化技术，确保了部署的灵活性和环境的一致性。

### 如何使用

1. 确保满足 **系统要求**：至少 8GB RAM，安装有 Linux 或 MacOS 系统。
2. 安装 **前提条件**：Docker、Docker Compose、Git。
3. 克隆仓库或下载发布版本，运行以下脚本以启动平台：
   ```bash
   ./run-platform.sh
   ```
4. 访问 [http://frontend.unstract.localhost](http://frontend.unstract.localhost) 并使用默认的用户名和密码（`unstract`）登录。
5. 参考用户指南和快速启动指南进行更进一步的配置和使用。

### 项目推介

**Unstract** 不仅是技术前沿的产物，而且是大型语言模型应用领域的一个里程碑。作为智能文档处理 2.0 的开创性平台，它为企业和开发者提供了前所未有的便利和效率，极大地简化了非结构化文档的处理工作。凭借对 OpenAI、Google VertexAI、Azure OpenAI 等多个 LLM 提供商的宽泛支持，以及对各种向量数据库和文本提取器的兼容，**Unstract** 完全符合当前数据处理的复杂需求。

项目的活跃开发状态、开放的社区支持和清晰的文档说明，使其成为希望探索和利用大型语言模型以结构化非结构化文档领域的人员和企业的理想选择。不管你是在寻求为自己的企业自动化解决方案，还是想要为客户提供更加高效的数据处理服务，**Unstract** 都值得你深入了解和使用。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=Zipstack/unstract&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/Zipstack/unstract 

开源项目作者：Zipstack

开源协议：GNU Affero General Public License v3.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=Zipstack/unstract)

关注我们，一起探索有意思的开源项目。

