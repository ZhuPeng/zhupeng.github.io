---
layout: post
title: GitHub 开源项目 GaiZhenbiao/ChuanhuChatGPT 介绍，GUI for ChatGPT API and many LLMs. Supports agents, file-based QA, GPT finetuning and query with web search. All with a neat UI.
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 GaiZhenbiao/ChuanhuChatGPT，该项目在 GitHub 有超过 13.2k Star，用一句话介绍该项目就是：“GUI for ChatGPT API and many LLMs. Supports agents, file-based QA, GPT finetuning and query with web search. All with a neat UI.”。


![Video Title](https://github.com/GaiZhenbiao/ChuanhuChatGPT/assets/51039745/0eee1598-c2fd-41c6-bda9-7b059a3ce6e7.jpg)
![ChuanhuChat5更新](https://github.com/GaiZhenbiao/ChuanhuChatGPT/assets/70903329/f2c2be3a-ea93-4edf-8221-94eddd4a0178)
![](https://github.com/GaiZhenbiao/ChuanhuChatGPT/assets/70903329/aca3a7ec-4f1d-4667-890c-a6f47bf08f63)
![](https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=&slug=ChuanhuChat&button_colour=219d53&font_colour=ffffff&font_family=Poppins&outline_colour=ffffff&coffee_colour=FFDD00)
![](https://user-images.githubusercontent.com/51039745/226920291-e8ec0b0a-400f-4c20-ac13-dafac0c3aeeb.JPG)



1、背景介绍：在了解大型语言模型 (LLM) 和 ChatGPT 相关的众多项目中，通常我们会面临以下问题。第一，使用这些语言模型需要获取 API，并且可能需要面对较复杂的编程控制，难以直接与语言模型进行互动。第二，很多时候我们只是希望进行简单的疑问，而并不需要获取全部的聊天记录。第三，我们可能需要离线或者本地部署语言模型，但很多现有的语言模型接口都只提供在线调用，如何进行本地部署并使用成为一大难题。第四，我们可能需要将 ChatGPT 与网络搜索等工具结合使用，这样即使 ChatGPT 的数据太旧，也可以获取最新的搜索结果。

2、项目介绍：为解决以上问题，" 川虎 ChatGPT " 这个项目应运而生。该项目创建了一个界面优美、用户友好的 Web 图形用户界面，使得使用者无需编程知识即可更便捷、更深入地与多种语言模型，如 ChatGPT、Azure OpenAI、Google PaLM 等模型进行互动。其主要功能包括，支持文件问答，基于 Agent 助理，支持 LLM 的本地部署，联网搜索，GPT fine-tuning 等。此外，项目还支持在线搜索，知识库等功能，且支持本地部署 LLM，使得无需网络连接也可以使用。最后，该项目目前已适配了多个不同的语言模型 API 调用和本地部署，且提供了多种可调整的参数，为 LLN 的调试和优化提供了更大的空间。

3、如何使用：
通过以下步骤，你就可以轻松安装并开始使用这个项目：
```shell
git clone https://github.com/GaiZhenbiao/ChuanhuChatGPT.git
cd ChuanhuChatGPT
pip install -r requirements.txt
```
然后，在项目文件夹中复制一份 `config_example.json`，并将其重命名为 `config.json`，在其中填入 `API-Key` 等设置。完成后运行以下命令，一个浏览器窗口将会自动打开，此时您将可以使用 " 川虎 Chat " 与ChatGPT或其他模型进行对话。
```shell
python ChuanhuChatbot.py
```

4、项目推介：目前，到 Github 的 star 折线图显示，" 川虎 ChatGPT " 项目目前处于活跃开发状态，在社区中也广受好评。项目作者在代码质量、设计思路以及文档完备程度上都做得非常出色，这使得该项目不仅易于使用，而且易于扩展和开发。近期，该项目的版本更新也相当频繁，持续对优化和完善。因此，我强烈推荐关注和使用这个项目，尤其对于在聊天机器人、自然语言处理等领域有研究或应用需求的人士。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=GaiZhenbiao/ChuanhuChatGPT&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/GaiZhenbiao/ChuanhuChatGPT 

开源项目作者：GaiZhenbiao

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=GaiZhenbiao/ChuanhuChatGPT)

关注我们，一起探索有意思的开源项目。

