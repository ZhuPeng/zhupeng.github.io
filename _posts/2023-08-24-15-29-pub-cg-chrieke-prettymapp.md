---
layout: post
title: 一个创建个性化地图展示的工具
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在我们的日常生活中，我们经常需要查看地图来获取位置信息或者规划路线。然而，传统的地图界面可能显得单调乏味，难以满足用户的审美需求。此时，prettymapp 这个开源项目就能派上用场了。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_macau.png)

prettymapp 项目在 GitHub 有超过 2.2k Star。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240508225231380.png)

一句话介绍该项目：“Create beautiful maps from OpenStreetMap data in a streamlit webapp”。以下是一些创建的示例：

![](https://raw.githubusercontent.com/chrieke/prettymapp/master/streamlit-prettymapp/example_prints/demo.gif)

###### 项目介绍

 prettymapp 是一个基于 OpenStreetMap 数据创建美观地图的 Python 包和 Web 应用程序。它通过重新设计 prettymaps 项目，提高了速度和简化了配置界面，同时增加了streamlit webapp 组件。prettymapp 提供了多种预设的地图样式，用户可以根据自己的需求进行自定义配置，从而创建出美观的地图。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_barcelona.png)

###### 如何使用

用户可以直接在 streamlit webapp 上使用 prettymapp，也可以在 Python 中直接调用 prettymapp 包进行自定义配置。在使用 prettymapp 包时，用户可以通过设置不同的参数来实现地图的自定义配置，同时也可以参考 prettymapp 提供的预设样式进行配置。此外，prettymapp 还提供了代码示例，方便用户快速上手。

本地运行代码：

```bash
git clone https://github.com/chrieke/prettymapp.git
cd prettymapp
pip install -r streamlit-prettymapp/requirements.txt
streamlit run streamlit-prettymapp/app.py
```

使用 Python 调用，安装命令如下：

```bash
pip install prettymapp
```

Python 的示例代码如下，定义区域并下载数据进行渲染。

```python
from prettymapp.geo import get_aoi
from prettymapp.osm import get_osm_geometries
from prettymapp.plotting import Plot
from prettymapp.settings import STYLES

aoi = get_aoi(address="Praça Ferreira do Amaral, Macau", radius=1100, rectangular=False)
df = get_osm_geometries(aoi=aoi)

fig = Plot(
    df=df,
    aoi_bounds=aoi.bounds,
    draw_settings=STYLES["Peach"]
).plot_all()

fig.savefig("map.jpg")
```


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=chrieke/prettymapp&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/chrieke/prettymapp 

开源项目作者：chrieke

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=chrieke/prettymapp)

关注我们，一起探索有意思的开源项目。

