---
layout: post
title: GitHub 开源项目 chatchat-space/Langchain-Chatchat 介绍，Langchain-Chatchat（原Langchain-ChatGLM）基于 Langchain 与 ChatGLM 等语言模型的本地知识库问答 | Langchain-Chatchat (formerly langchain-ChatGLM), local knowledge based LLM (like ChatGLM) QA app with langchain 
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 chatchat-space/Langchain-Chatchat，该项目在 GitHub 有超过 18.7k Star，用一句话介绍该项目就是：“Langchain-Chatchat（原Langchain-ChatGLM）基于 Langchain 与 ChatGLM 等语言模型的本地知识库问答 | Langchain-Chatchat (formerly langchain-ChatGLM), local knowledge based LLM (like ChatGLM) QA app with langchain ”。


![](https://raw.githubusercontent.com/chatchat-space/Langchain-Chatchat/master/img/logo-long-chatchat-trans-v2.png)
![实现原理图](https://raw.githubusercontent.com/chatchat-space/Langchain-Chatchat/master/img/langchain+chatglm.png)
![实现原理图2](https://raw.githubusercontent.com/chatchat-space/Langchain-Chatchat/master/img/langchain+chatglm2.png)
![](https://raw.githubusercontent.com/chatchat-space/Langchain-Chatchat/master/img/fastapi_docs_026.png)
![img](https://raw.githubusercontent.com/chatchat-space/Langchain-Chatchat/master/img/LLM_success.png)
![](https://raw.githubusercontent.com/chatchat-space/Langchain-Chatchat/master/img/init_knowledge_base.jpg)
![](https://raw.githubusercontent.com/chatchat-space/Langchain-Chatchat/master/img/qr_code_74.jpg)
![](https://raw.githubusercontent.com/chatchat-space/Langchain-Chatchat/master/img/official_wechat_mp_account.png)



一、背景介绍

随着现代科技的发展，人们对信息的需求日益增长，然而却面临着信息检索和处理的困境。含有关键信息的文件，如各类文档、论文、手册等，数量庞大，内容漫溢，使得寻找特定信息成为一项繁重且耗时的任务。需要一个解决方案，能以大模型的方式，快速、准确实现全文信息检索，并能进行增强生成(RAG)对知识库内容进行处理。同时，出于数据安全和隐私保护的考虑，这个解决方案还需要有完全本地化推理和私域化部署的能力，以保护企业的私有数据和知识产权。

二、项目介绍

GitHub 开源项目 "Langchain-Chatchat" 正是为解决上述问题而设计。它基于TechBotAI的大语言模型和本地知识库技术 Langchain 开发，是一款可以实现完全本地推理的知识库增强生成项目。这款项目的设计初衷，是为了构建一套中文环境友好、可以脱线运行的知识库问答解决方案。
 
Langchain-Chatchat 使用 Langchain 实现了一种基于本地知识库的问答应用。具体来讲，系统的流程包括加载文件，读取文本，对文本进行分割和向量化，对问句进行向量化，然后在文本向量中匹配出与问句向量最相似的 `top k`个，将匹配出的文本作为上下文和问题一起添加到 `prompt`中，提交给大语言模型生成回答，以此实现检索增强生成(RAG)。

它所能够解决的痛点包括：数据的安全保护，私域化部署的需求，以及冗杂文件搜寻的困扰，帮助用户省时省力。

三、如何使用

在使用 Langchain-Chatchat 之前，你需要拥有 Python 3.8 - 3.10 的环境，然后将本项目仓库拉取到本地，并安装所有的依赖。

然后进行模型的下载，例如。默认使用的 LLM 模型为 [THUDM/ChatGLM2-6B](https://huggingface.co/THUDM/chatglm2-6b) ，Embedding 模型为 [moka-ai/m3e-base](https://huggingface.co/moka-ai/m3e-base) 。下载好的模型需要先安装 Git LFS 。然后进行初始化知识库和配置文件，最后执行命令启动项目。

四、项目推介

目前，Langchain-Chatchat 是一个新兴的开源项目，由一支热情高涨的开发团队共同打造，项目开发活跃，且代码高质。项目获得了开源社区的高度关注和积极反响，已经有一大批用户或公司争相尝试，对于特定需求的解决效果很好。
如你关心数据的安全问题，需要大规模数据检索和处理，或者你是需要私域化部署的企业，这款开源项目会是你的理想之选。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=chatchat-space/Langchain-Chatchat&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/chatchat-space/Langchain-Chatchat 

开源项目作者：chatchat-space

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=chatchat-space/Langchain-Chatchat)

关注我们，一起探索有意思的开源项目。

