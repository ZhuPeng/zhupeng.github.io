---
layout: post
title: GitHub 开源项目 gradio-app/gradio 介绍，Build and share delightful machine learning apps, all in Python. 🌟 Star to support our work!
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 gradio-app/gradio，该项目在 GitHub 有超过 27.2k Star，一句话介绍该项目：Build and share delightful machine learning apps, all in Python. 🌟 Star to support our work!




![`hello_world_4` demo](https://raw.githubusercontent.com/gradio-app/gradio/master/demo/hello_world_4/screenshot.gif)

![](https://raw.githubusercontent.com/gradio-app/gradio/master/readme_files/gradio.svg)

![](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/gradio-guides/lcm-screenshot-3.gif)

![](https://raw.githubusercontent.com/gradio-app/gradio/master/readme_files/huggingface_mini.svg)

![](https://raw.githubusercontent.com/gradio-app/gradio/master/readme_files/python.svg)

![](https://raw.githubusercontent.com/gradio-app/gradio/master/readme_files/fastapi.svg)

![](https://raw.githubusercontent.com/gradio-app/gradio/master/readme_files/encode.svg)

![](https://raw.githubusercontent.com/gradio-app/gradio/master/readme_files/svelte.svg)

![](https://raw.githubusercontent.com/gradio-app/gradio/master/readme_files/vite.svg)

![](https://raw.githubusercontent.com/gradio-app/gradio/master/readme_files/pnpm.svg)



背景介绍：
在机器学习开发过程中，我们经常会需要将模型、API 或任何 Arbitrary Python 函数以应用的形式展示给他人，但是编写 web 应用并显示我们的模型结果通常需要 JavaScript， CSS 和 web 托管的复杂技能。有没有一种方式可以快速、无需编程和托管知识就可以将我们的 Python 模型转变成一个应用，并且方便的分享出去呢？Gradio 就是为了解决这个困扰我们的问题而生的。

项目介绍：
Gradio 是一个开源的 Python 包，旨在让开发者可以轻松快速的创建一个 web 应用，展示你的机器学习模型，API 或任何 Arbitrary Python 函数，并且能够快速通过 Gradio 的分享功能分享你的应用，不需要任何 JavaScript，CSS 或者 web 托管的知识。

如何使用：
在 Python 3.8 或者更新的版本上，你可以使用 pip 来安装 Gradio。运行以下命令即可：
```bash
pip install gradio
```
你可以在任何写 Python 的地方运行 Gradio，包括你的代码编辑器， Jupyter notebook， Google Colab 等。从以下的 Gradio app 开始：
```python
import gradio as gr

def greet(name, intensity):
    return "Hello " * intensity + name + "!"

demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"],
)

demo.launch()
```
然后执行你的代码。如果你将 Python 代码写在了例如 `app.py` 的文件里，你可以在终端运行 `python app.py`。 

项目推介：
你可以将你的 Gradio app 共享，而不需要担心 web 服务器的繁琐问题。只需要在 `launch()` 中设置 `share=True`，就能为你的演示创建一个公共可访问的 URL。Gradio 项目持续活跃并更新，具有很好的社区活力和影响力，如果你在机器学习或者 Python 上编程，这是一个值得一试的工具。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=gradio-app/gradio&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/gradio-app/gradio 

开源项目作者：gradio-app

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=gradio-app/gradio)

关注我们，一起探索有意思的开源项目。

