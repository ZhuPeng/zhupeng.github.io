---
layout: post
title: loom - 一个基于树形结构的写作界面
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在人工智能与人类的协同创作中，如何有效地处理文本内容，同时提供一个交互性强、用户体验良好的界面，一直是一个主要的挑战。

今天要给大家推荐一个 GitHub 开源项目 socketteer/loom，该项目在 GitHub 有差不多 1000 Star，用一句话介绍该项目就是：“Multiversal tree writing interface for human-AI collaboration”。

DEMO 参考如下：

![](https://raw.githubusercontent.com/socketteer/loom/master/static/readme/read-view.png)

###### 项目介绍

开源项目 loom 是一个基于树形结构的写作界面，专为 GPT-3 设计。这个项目现在还处于积极开发的阶段，虽然文档可能还不完善，但功能并不显得稀疏。loom 具备强大的操作性，包括线性故事查看、树形导航栏、编辑模式；你可以在树形视图下用鼠标探索、展开和折叠节点，调整树形结构，甚至进行就地节点编辑。另外，这个项目对于文件的输入和输出也进行了优化，支持以JSON格式打开和保存树，同时在多个标签页中处理树。

更多示例页面参考如下：

![](https://raw.githubusercontent.com/socketteer/loom/master/static/readme/read-view-light.png)

![](https://raw.githubusercontent.com/socketteer/loom/master/static/readme/tree-view.png)

![](https://raw.githubusercontent.com/socketteer/loom/master/static/readme/tree-view-light.png)

![](https://raw.githubusercontent.com/socketteer/loom/master/static/readme/metadata-light.png)

![](https://raw.githubusercontent.com/socketteer/loom/master/static/readme/block-multiverse.png)

###### 如何使用

你可以通过 Python 环境或者 Docker 来运行这个项目。首先，确保你的系统已经安装了 tkinter 和 Python 环境（版本需大于等于 3.9.13），接下来通过 pip 安装需要的依赖：`pip install -r requirements.txt`。建议设置环境变量`OPENAI_API_KEY`，`GOOSEAI_API_KEY`，`AI21_API_KEY`，当然你也可以在设置选项中直接使用它们。最后，运行main.py 并加载一个 json 树，就可以直接查看效果了。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231224224848314.png)

对于 Docker 的使用同样简单，只需编辑 Makefile 以添加你的 API 密钥（或在设置选项中使用），然后按照 Makefile 的指示操作即可。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231224224912120.png)

###### 项目推介

尽管这个项目目前还处于开发阶段，但它的概念是非常吸引人的，并有可能改变我们对于树形文本处理的常规理解。而且，该项目在 GitHub 上的活跃状态表明它在不断改进和更新，也就意味着你可以期待即将到来的新功能和更多的稳定性。如果你在寻找一个能够处理大量文本，特别是与人工智能协作时的文本的工具，那么 loom 项目值得你一试。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=socketteer/loom&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/socketteer/loom 

开源项目作者：socketteer

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=socketteer/loom)

关注我们，一起探索有意思的开源项目。

