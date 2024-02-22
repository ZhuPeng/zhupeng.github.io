---
layout: post
title: GitHub 开源项目 AbanteAI/rawdog 介绍，Generate and auto-execute Python scripts in the cli
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 AbanteAI/rawdog，该项目在 GitHub 有差不多 1000 Star，用一句话介绍该项目就是：“Generate and auto-execute Python scripts in the cli”。





背景介绍：为我们的日常工作带来便利是开源项目的重要意义之一。每个人都会遇到需要繁琐手动操作的问题，比如统计和绘制家目录中Git仓库的数量和磁盘占用，查看某个文件夹中所有CSV文件的pd.describe()结果，查询当前活动的端口以及属于Google的端口，并关闭它们等等。这些看似琐碎的任务耗费了我们大量的时间和精力。

项目介绍：基于这些需求，作者开发了名为 "Rawdog" （Recursive Augmentation With Deterministic Output Generations）的开源项目。这是一个命令行助手，它可以自动生成并自动执行Python脚本来解决上述问题，只需要你提供相应的命令。它能自我选择上下文，通过运行脚本打印信息，将输出增添至对话中，然后再次调用自己。并且它也可以按照README文件中的指示来设定仓库，或检查所有的CSV文件是否能合并，以及原因等。该工具强大实用，但请注意按照指示操作，以防意外情况的发生。

如何使用：要使用Rawdog，你只需通过 pip 进行安装：
```
pip install rawdog-ai
```
然后，选择一种交互模式，如果没有找到 API 密钥，你将被提示输入：
- 直接模式：执行单个提醒并关闭
```
rawdog Plot the size of all the files and directories in cwd
```
- 对话模式：进行反复交互，直至你关闭。Rawdog 可以看到它的脚本和输出。
```
rawdog
>>> What can I do for you? (Ctrl-C to exit)
>>> > |
```
如果你希望在执行每个脚本前手动确认，可以使用 `--dry-run` 参数。

模型选择：Rawdog 使用 'gpt-4' 作为默认的 `litellm` 补全模型，你可以修改 `~/.rawdog/config.yaml` 来调整模型或指向其他提供者。

项目推介：Rawdog 是非常活跃的开源项目，它的作者AbanteAI在 AI 和编程社区中也享有很高的声望，这一项目的优秀品质得到了业内广泛认可。你可以通过访问 [discord 联系作者](https://discord.gg/zbvd9qx9Pb)获取更多帮助，来尽快地开始在你的日常工作中使用 Rawdog 来提高效率。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=AbanteAI/rawdog&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/AbanteAI/rawdog 

开源项目作者：AbanteAI

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=AbanteAI/rawdog)

关注我们，一起探索有意思的开源项目。

