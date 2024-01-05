---
layout: post
title: GitHub 开源项目 OpenAccess-AI-Collective/axolotl 介绍，Go ahead and axolotl questions
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 OpenAccess-AI-Collective/axolotl，该项目在 GitHub 有超过 2.8k Star，用一句话介绍该项目就是：“Go ahead and axolotl questions”。


![](https://raw.githubusercontent.com/OpenAccess-AI-Collective/axolotl/master/image/axolotl.png)



背景介绍

在人工智能(AI)模型的开发过程中，通常需要对模型进行微调以适应特定任务和数据集。然而，各种模型的微调过程和配置各不相同，差异很大，涉及到的参数众多，微小的改变可能导致模型的性能有显著的差距。这使得微调成为一项耗时耗力却又关键至极的过程。如何用更少的时间和更低的复杂度细调模型，并在多个配置和架构中流畅无阻，是 AI 开发者一直在探索和实践的问题。

项目介绍

[ Axolotl ](https://github.com/OpenAccess-AI-Collective/axolotl)是一款强大的工具，能帮你轻松地微调各种 AI 模型，无论是各种 `Huggingface` 模型，如 `llama`，`pythia`，`falcon`，`mpt`，还是其他一些主流架构如 `lora`、`qlora`、`relora`、`gptq`，Axolotl 都能提供全面的支持。你可以通过简易的 `yaml` 文件或者命令行覆写来定制配置，支持加载不同的数据集格式，甚至可以携带自定义的分词数据集。Axolotl 还与 `xformer`，`flash attention`，`rope scaling`，`multipacking` 等强大功能集成，无论是使用单个 `GPU` 还是通过 `FSDP` 或 `Deepspeed` 使用多个 `GPU`，Axolotl 都能处理。其过程可以轻松地在本地或云端通过 `Docker` 运行，并且你还可以将结果以及可选的检查点记录到 `wandb`。

如何使用

安装 Axolotl 非常简单，你只需要拥有Python 3.9 或以上版本以及 Pytorch 2.0 或以上版本。你可以直接从Github源代码运行install命令，或者在项目目录文件夹下通过PIP运行install命令。详细的代码示例请参见项目README给出的示例。

如果你是开发者，还可以通过`git`命令把项目克隆到本地，然后再运行相关安装命令。配置完成后，你就可以开始进行微调操作了，无论是训练、推理还是其他操作，只需要一行命令，轻松完成。

项目推介

作为一个正在积极开发和更新的项目，Axolotl 吸引了大量的开发者参与和贡献，项目活跃度非常高。项目的开发团队来自 OpenAccess AI Collective，这是一个主张AI开放的团体。Axolotl已经成功服务于众多知名的企业和团队，并有一队长期维护并保障其运行稳定和功能更新的工程师团队，也深受业内专家和研究者的好评。你无需担心项目的维护和更新问题，并可以享受到这个开源项目带来的所有优点。如果你正在寻找一款实用的，能帮助你轻松细调 AI 模型的工具，Axolotl 将会是你的首选。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=OpenAccess-AI-Collective/axolotl&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/OpenAccess-AI-Collective/axolotl 

开源项目作者：OpenAccess-AI-Collective

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=OpenAccess-AI-Collective/axolotl)

关注我们，一起探索有意思的开源项目。

