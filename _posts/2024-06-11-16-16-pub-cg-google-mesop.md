---
layout: post
title: 轻松上手构建 Web 应用的工具
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

构建一个具有吸引力的 Web 应用变得越来越重要。然而，对于许多开发者来说，传统的 Web 开发需要深入了解多种语言如 HTML、CSS 和 JavaScript，这无疑增加了学习成本和开发难度。特别是对于那些精通 Python 但对前端技术不太熟悉的开发者而言，这成为了一个不小的挑战。他们急需一个既能利用 Python 的强大功能，又能快速、简便地创建漂亮 Web 应用的工具。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-5ffc827bbd73c9160c0c5c0f0e3c70b0.png)

今天要给大家推荐一个 GitHub 开源项目 mesop，该项目在 GitHub 有超过 4k Star。

![](https://stats.deeptrain.net/repo/google/mesop/?theme=light)

一句话介绍该项目：Build delightful web apps quickly in Python

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240630215011386.png)

###### 项目介绍

Mesop 是 Google 推出的一个 Python 编写的 UI 框架，它允许开发者快速构建如可演示的 Web 应用和内部工具。Mesop 的核心优势在于它的直观性和开发流程的丝滑：开发者可以使用习惯的 Python 代码编写 UI，遵循易于理解的反应式 UI 范例，并利用丰富的已有组件。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240630215142470.png)

更重要的是，Mesop 提供了热重载功能和强大的 IDE 支持，极大地提升了开发效率。另外，通过 Mesop，开发者可以不写任何 JavaScript/CSS/HTML 代码而构建自定义 UI，真正做到了快速开发和创新。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240630215155425.png)

###### 如何使用

首先，通过简单的命令安装 Mesop：

```sh
$ pip install mesop
```
接着，将提供的代码示例复制到 `main.py` 文件中。

```python
import mesop as me
import mesop.labs as mel


@me.page(
  security_policy=me.SecurityPolicy(
    allowed_iframe_parents=["https://google.github.io"]
  ),
  path="/text_to_image",
  title="Text to Image Example",
)
def app():
  mel.text_to_image(
    generate_image,
    title="Text to Image Example",
  )


def generate_image(prompt: str):
  return "https://www.google.com/logos/doodles/2024/earth-day-2024-6753651837110453-2xa.gif"
```

之后，通过以下命令运行应用：

```sh
$ mesop main.py
```
通过上述几步，你即可启动并运行一个简单的 Mesop 应用，示例页面如下。完整的上手指南请参见 Getting Started。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240630215643066.png)

###### 项目推介

Mesop 是由 Google 开发并使用于其内部的快速应用开发工作，它尽管不是 Google 官方支持的产品，但其背后的技术实力和在 Google 的实际应用经验赋予了它极高的可靠性和实用价值。此外，其丰富的文档、示例和入门教程，使得即便是 UI 开发新手也能轻松上手。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240630220233692.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=google/mesop&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/google/mesop 

开源项目作者：google

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=google/mesop)

关注我们，一起探索有意思的开源项目。

