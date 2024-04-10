---
layout: post
title: 快速将数据和 AI 算法转化为生产就绪的 Web 应用程序
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在当前数据化、算法化的环境中，有很多场景会碰到需要将数据和 AI 算法转化为生产就绪的网络应用程序的情况。这需要你既要有较强的数据和算法能力，同时还要有全栈开发的技巧。然而对于大部分数据科学家和机器学习工程师来说，他们的专长并不在后端开发和前端设计上，这使得他们无法有效地推广他们的算法。为了能更好地让数据和 AI 算法应用于实际，这就需要一个可以简化开发和部署过程的工具。

今天要给大家推荐一个 GitHub 开源项目 Avaiga/taipy，该项目在 GitHub 有超过 6.6k Star，一句话介绍该项目：Turns Data and AI algorithms into production-ready web applications in no time.

![](https://raw.githubusercontent.com/Avaiga/taipy/master/readme_img/gui_creation.webp)

###### 项目介绍

Taipy 是一个面向数据科学家和机器学习工程师开发的开源 Python 库，可以方便地将数据和 AI 算法转化为生产就绪的 Web 应用程序。Taipy 具有如下几个主要特点：

1、它是基于 Python 的 UI 框架，可以让你在不需要学习其他像 HTML、CSS 或者 JavaScript 这样的前端技术的情况下，就能开发全栈应用。

2、内置了很多可以处理数据流水线的功能，例如可视化和管理工具。

3、Taipy 提供了丰富的业务场景和数据管理特性，可以灵活地处理像需求预测、生产规划这样的应用场景。

4、还包含了版本管理和流水线管控的功能，可以更好地适应多用户环境。

![](https://raw.githubusercontent.com/Avaiga/taipy/master/readme_img/scenario_and_data_mgt.gif)

###### 如何使用

在使用 Taipy 之前，首先需要通过 pip 来安装 Taipy：

```bash
pip install taipy
```

使用 Taipy 你可以完全用 Python 的方式来编写你的网应用程序，以下是一个代码的示例以及对应的 UI 交互。

```python
import taipy as tp
import pandas as pd
from taipy import Config, Scope, Gui

# Taipy Scenario & Data Management

# Filtering function - task
def filter_genre(initial_dataset: pd.DataFrame, selected_genre):
    filtered_dataset = initial_dataset[initial_dataset["genres"].str.contains(selected_genre)]
    filtered_data = filtered_dataset.nlargest(7, "Popularity %")
    return filtered_data

# Load the configuration made with Taipy Studio
Config.load("config.toml")
scenario_cfg = Config.scenarios["scenario"]

# Start Taipy Core service
tp.Core().run()

# Create a scenario
scenario = tp.create_scenario(scenario_cfg)


# Taipy User Interface
# Let's add a GUI to our Scenario Management for a full application

# Callback definition - submits scenario with genre selection
def on_genre_selected(state):
    scenario.selected_genre_node.write(state.selected_genre)
    tp.submit(scenario)
    state.df = scenario.filtered_data.read()

# Get list of genres
genres = [
    "Action", "Adventure", "Animation", "Children", "Comedy", "Fantasy", "IMAX"
    "Romance","Sci-FI", "Western", "Crime", "Mystery", "Drama", "Horror", "Thriller", "Film-Noir","War", "Musical", "Documentary"
    ]

# Initialization of variables
df = pd.DataFrame(columns=["Title", "Popularity %"])
selected_genre = "Action"

## Set initial value to Action
def on_init(state):
    on_genre_selected(state)

# User interface definition
my_page = """
# Film recommendation

## Choose your favorite genre
<|{selected_genre}|selector|lov={genres}|on_change=on_genre_selected|dropdown|>

## Here are the top seven picks by popularity
<|{df}|chart|x=Title|y=Popularity %|type=bar|title=Film Popularity|>
"""

Gui(page=my_page).run()
```

![](https://raw.githubusercontent.com/Avaiga/taipy/master/readme_img/readme_app.gif)

###### 项目推介

Taipy 是一个正在持续开发维护的开源项目，特别是对于那些专业方向偏向于数据和算法但又需要开发网络应用程序的数据科学家和机器学习工程师来说，Taipy 极大的简化了他们的开发和部署过程，使得他们可以将更多的时间放在数据和算法的设计上。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=Avaiga/taipy&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/Avaiga/taipy 

开源项目作者：Avaiga

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=Avaiga/taipy)

关注我们，一起探索有意思的开源项目。

