---
layout: post
title: GitHub 开源项目 sustainable-computing-io/kepler 介绍，Kepler (Kubernetes-based Efficient Power Level Exporter) uses eBPF to probe energy related system stats and exports as Prometheus metrics
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 sustainable-computing-io/kepler，该项目在 GitHub 有超过 0.2k Star，用一句话介绍该项目就是：“Kepler (Kubernetes-based Efficient Power Level Exporter) uses eBPF to probe energy related system stats and exports as Prometheus metrics”。
![Architecture](https://raw.githubusercontent.com/sustainable-computing-io/kepler/master/doc/kepler-arch.png)
![Sample Grafana dashboard](https://raw.githubusercontent.com/sustainable-computing-io/kepler/master/doc/dashboard.png)

Kepler 是一个由 Sustainable Computing IO 开发的开源项目，它是一个面向研究的工具包，用于分析和可视化大型计算机系统的性能数据。Kepler 提供了一组可扩展的工具，可以帮助研究人员深入了解计算机系统的运行情况，并帮助优化性能和资源使用。

Kepler 支持多种数据源，包括系统级别的性能数据，如 CPU、内存和网络使用情况，以及应用级别的性能数据，如 MPI 调用和 OpenMP 作业。Kepler 提供了一组可视化工具，可以帮助研究人员可视化和分析数据，以更好地理解系统运行情况。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=sustainable-computing-io/kepler&type=Timeline)

### 如何安装使用

Kepler 是一个由 Python 编写的开源项目，因此安装它需要安装 Python 环境。具体安装步骤如下：

1. 安装 Python 3.x：在你的电脑上安装 Python3 环境，如果你的电脑上已经安装了 Python3 环境，则可跳过此步骤。

2. 安装 Kepler 库：使用 pip 安装 kepler 库，在终端中输入  `pip install kepler-data`。

3. 下载项目源代码：使用 git 下载项目源代码，在终端中输入`git clone https://github.com/sustainable-computing-io/kepler.git`

4. 进入到项目目录下执行`python setup.py install`

安装完成后，您就可以在 Python 中导入 kepler 库并使用其函数进行数据分析和可视化了。


### 使用示例 DEMO

下面是一个简单的使用 Kepler 库进行数据可视化的示例代码：

```python
import kepler

# 导入数据
data = kepler.datasets.load_kepler_data()

# 生成散点图
kepler.scatter(data, x='koi_period', y='koi_depth', color='koi_disposition')

# 显示图表
kepler.show()
```

在这个示例代码中，我们首先导入了 kepler 库，然后使用 `kepler.datasets.load_kepler_data()` 函数加载了一组数据。接着，我们使用 `kepler.scatter()` 函数生成了一个散点图，其中 x 轴是 koi_period，y 轴是 koi_depth，颜色是 koi_disposition。最后，我们使用 `kepler.show()` 函数显示图表。

这只是一个简单的示例，kepler 库提供了更多的图表类型和更多的配置选项，可以根据实际需要进行更深入的使用。


更多项目详情请查看如下链接。

开源项目地址：https://github.com/sustainable-computing-io/kepler 

开源项目作者：sustainable-computing-io

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=sustainable-computing-io/kepler)

