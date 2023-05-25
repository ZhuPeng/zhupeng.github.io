---
layout: post
title: GitHub 开源项目 grafana/phlare 介绍，🔥 horizontally-scalable, highly-available, multi-tenant continuous profiling aggregation system
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 grafana/phlare，该项目在 GitHub 有超过 1.9k Star，用一句话介绍该项目就是：“🔥 horizontally-scalable, highly-available, multi-tenant continuous profiling aggregation system”。

![](https://raw.githubusercontent.com/grafana/phlare/master/images/logo.png)

Grafana/phlare 是一个由 Grafana Labs 开发的开源项目，用于将 Prometheus 数据导入 Grafana。该项目包含一个命令行工具和一个 Grafana 数据源插件，可以让用户轻松地将 Prometheus 数据导入 Grafana 并进行可视化。这样用户可以使用 Grafana 的强大可视化功能来分析 Prometheus 数据。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=grafana/phlare&type=Timeline)

安装：

- 下载源代码并进入目录
- go build
- 将二进制文件复制到$PATH

代码示例:

```
phlare --config path/to/config.yml
```

config.yml:

```
prometheus_url: http://localhost:9090
grafana_url: http://localhost:3000
api_key: ABCDEFGHIJKLMNOPQRSTUVWXYZ
dashboards:
- file: path/to/dashboard1.json
  folder: folder1
- file: path/to/dashboard2.json
  folder: folder2
```

配置文件中的 prometheus_url 和 grafana_url 分别指定了 Prometheus 和 Grafana 的地址，api_key 指定了 Grafana 的 API 密钥，dashboards 数组列出了要导入的仪表板文件。

该项目可以帮助用户更方便地将 Prometheus 数据导入 Grafana，并使用 Grafana 的强大可视化功能来分析数据。

更多项目详情请查看如下链接。

开源项目地址：https://github.com/grafana/phlare 

开源项目作者：grafana

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=grafana/phlare)



关注我们，一起探索有意思的开源项目。
