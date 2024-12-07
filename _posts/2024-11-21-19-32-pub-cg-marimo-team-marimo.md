---
layout: post
title: 可替代 Jupyter 的 Python 编程环境
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在当今快速发展的数据科学和机器学习领域，开发人员和研究人员常常面临着代码复现和展示的挑战。传统的计算机笔记本工具，如 Jupyter Notebook，虽有广泛应用，但存在一些痛点：诸如代码依赖性管理不直观、笔记本难以版本控制、重复运行代码效率低下等问题。这些问题严重影响了实验的可重复性和代码的可维护性，阻碍了研究和开发的进程。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-eb72b4d774ad536a7660bcec7c58ff04.png)

今天要给大家推荐一个 GitHub 开源项目 marimo，该项目在 GitHub 有超过 8k Star。

![](https://stats.deeptrain.net/repo/marimo-team/marimo/?theme=light)

一句话介绍该项目：A reactive notebook for Python — run reproducible experiments, execute as a script, deploy as an app, and version with git. 

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241127231721000.png)

###### 项目介绍

marimo 是一个反应式 Python 笔记本项目，提供了一个可重复、易于版本控制、可部署为应用程序的编程环境。**marimo** 可以自动执行依赖项更改的单元格，并提供一个纯 Python 存储格式，无缝集成 Git 版本控制系统。此外，**marimo** 集成了包括 **Jupyter**、**Streamlit**、**Jupytext**、**Ipywidgets**、**Papermill** 等多个开源项目的功能。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241127231846856.png)

项目具有以下亮点：

1、功能齐全：一站式替代多个传统工具。

2、反应式编程：自动运行依赖单元格，确保代码与输出的一致性。

3、交互式操作：提供丰富的 UI 元素绑定，简化交互式编程。

4、可重复性：无隐藏状态，保证程序执行的确定性。

5、可执行性：支持作为 Python 脚本执行。

6、可分享性：可部署为交互式 Web 应用。

7、适用于数据处理：支持 SQL 查询和数据框操作。

8、Git 友好：笔记本以 `.py` 文件形式存储，便于版本控制。

9、现代化的编辑器：支持 GitHub Copilot、AI 辅助、Vim快捷键等。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241127232024728.png)

以下是一些使用示例：

![](https://raw.githubusercontent.com/marimo-team/marimo/main/docs/_static/reactive.gif)

![](https://raw.githubusercontent.com/marimo-team/marimo/main/docs/_static/readme-sql-cell.png)

![](https://raw.githubusercontent.com/marimo-team/marimo/main/docs/_static/embedding.gif)

###### 如何使用

执行如下命令安装：

```python
pip install marimo && marimo tutorial intro
```

创建与运行笔记本参考如下：

1、创建或编辑笔记本：`marimo edit`

2、以 Web 应用形式运行笔记本：`marimo run your_notebook.py`

3、作为脚本执行笔记本：`python your_notebook.py`

4、自动将 Jupyter 笔记本转换为 marimo 笔记本：`marimo convert your_notebook.ipynb > your_notebook.py`

###### 项目推介

marimo 自启动以来快速发展，已经吸引了大量开发者和数据科学家的关注。凭借其先进的反应式编程环境和兼具可重复性、易分享性的特点，**marimo** 成为了一个革新性的解决方案。无论是在学术研究、数据分析还是机器学习领域，**marimo** 都展现出了其强大的应用潜力。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241127232306671.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=marimo-team/marimo&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/marimo-team/marimo 

开源项目作者：marimo-team

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=marimo-team/marimo)

关注我们，一起探索有意思的开源项目。

