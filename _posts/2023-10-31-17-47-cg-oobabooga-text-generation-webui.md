---
layout: post
title: GitHub 开源项目 oobabooga/text-generation-webui 介绍，A Gradio web UI for Large Language Models. Supports transformers, GPTQ, AWQ, EXL2, llama.cpp (GGUF), Llama models.
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 oobabooga/text-generation-webui，该项目在 GitHub 有超过 26.0k Star，用一句话介绍该项目就是：“A Gradio web UI for Large Language Models. Supports transformers, GPTQ, AWQ, EXL2, llama.cpp (GGUF), Llama models.”。


![Image1](https://github.com/oobabooga/screenshots/raw/main/print_instruct.png)
![Image2](https://github.com/oobabooga/screenshots/raw/main/print_chat.png)
![Image1](https://github.com/oobabooga/screenshots/raw/main/print_default.png)
![Image2](https://github.com/oobabooga/screenshots/raw/main/print_parameters.png)
![Image3](https://github.com/oobabooga/screenshots/raw/main/gpt4chan.png)





背景介绍：
在大型语言模型的研究和应用中，我们经常会遇到如何方便快捷地进行模型交互、模型切换、模型训练等问题。同时，对于不同的模型，我们可能需要不同的界面模式进行交互，如默认模式、笔记本模式和聊天模式等。这些问题的存在，使得我们在进行大型语言模型的研究和应用时，需要花费大量的时间和精力在模型交互和管理上。

项目介绍：
"Text generation web UI" 是一个基于 Gradio 的大型语言模型的 Web UI，它的目标是成为文本生成的 AUTOMATIC1111/stable-diffusion-webui。它具有以下特点：
- 支持三种界面模式：默认（两列）、笔记本和聊天
- 支持多种模型后端：transformers、llama.cpp、ExLlama、ExLlamaV2、AutoGPTQ、GPTQ-for-LLaMa、CTransformers、AutoAWQ
- 提供下拉菜单快速切换不同模型
- LoRA：即时加载和卸载 LoRAs，使用 QLoRA 训练新的 LoRA
- 提供精确的聊天模式指令模板，包括 Llama-2-chat、Alpaca、Vicuna、WizardLM、StableLM 等
- 通过 transformers 库实现 4-bit、8-bit 和 CPU 推理
- 使用 transformers 采样器的 llama.cpp 模型（llamacpp_HF loader）
- 支持多模态管道，包括 LLaVA 和 MiniGPT-4
- 扩展框架
- 自定义聊天角色
- 高效的文本流
- 支持 Markdown 输出和 LaTeX 渲染，例如与 GALACTICA 一起使用
- 包括 websocket 流的端点在内的 API

如何使用：
1）克隆或下载仓库。
2）根据您的操作系统运行 start_linux.sh、start_windows.bat、start_macos.sh 或 start_wsl.bat 脚本。
3）在询问时选择您的 GPU 供应商。
4）尽情享受吧！

项目推介：
该项目的开发活跃，作者是知名的开源贡献者，项目已经在多个知名公司和机构中得到应用。同时，该项目的文档齐全，易于上手，对于大型语言模型的研究和应用具有很高的参考价值。因此，我强烈推荐大家关注和使用这个项目。






以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=oobabooga/text-generation-webui&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/oobabooga/text-generation-webui 

开源项目作者：oobabooga

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=oobabooga/text-generation-webui)

关注我们，一起探索有意思的开源项目。

