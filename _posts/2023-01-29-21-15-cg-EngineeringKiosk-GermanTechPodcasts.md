---
layout: post
title: GitHub 开源项目 EngineeringKiosk/GermanTechPodcasts 介绍，A curated list of German Tech Podcasts 🇩🇪 🇦🇹 🇨🇭
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 EngineeringKiosk/GermanTechPodcasts，该项目在 GitHub 有超过 0.1k Star，用一句话介绍该项目就是：“A curated list of German Tech Podcasts 🇩🇪 🇦🇹 🇨🇭”。

GermanTechPodcasts 是一个 GitHub 开源项目，由 EngineeringKiosk 维护。该项目收集了一些德国科技类播客的相关信息，包括播客名称、简介、RSS 链接和更新时间等。这些信息可以帮助用户更好地了解德国科技领域的最新动态，并找到自己感兴趣的播客。项目使用 Python 编写，提供了爬虫脚本来爬取播客相关信息。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=EngineeringKiosk/GermanTechPodcasts&type=Timeline)

### 如何安装使用

该项目可以通过以下步骤安装：

1. 克隆该项目的代码库到本地：
```
git clone https://github.com/EngineeringKiosk/GermanTechPodcasts.git
```
2. 进入该项目目录，并使用 pip 安装依赖包
```
cd GermanTechPodcasts
pip install -r requirements.txt
```
3. 运行爬虫脚本来爬取播客相关信息
```
python main.py
```
安装完成后可以在项目目录下查看 data.json 文件,里面就是爬取的信息

注意：在安装之前需要确保你已经安装了 Python 环境。


### 使用示例 DEMO

以下是一个使用该项目爬取播客信息的示例代码：

```
import json

with open('data.json') as json_file:
    data = json.load(json_file)
    for p in data['podcasts']:
        print('Podcast name: ' + p['name'])
        print('Podcast url: ' + p['url'])
        print('Podcast description: ' + p['description'])
        print('Podcast language: ' + p['language'])
        print('Podcast category: ' + p['category'])
        print()
```

该代码首先打开 data.json 文件并将其加载到变量 data 中，然后使用 for 循环遍历 data 中的播客信息并打印出来。

请注意，这只是一个简单的示例，您可以根据需要修改代码来爬取更多的播客信息或将信息存储到其他位置。


更多项目详情请查看如下链接。

开源项目地址：https://github.com/EngineeringKiosk/GermanTechPodcasts 

开源项目作者：EngineeringKiosk

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=EngineeringKiosk/GermanTechPodcasts)

