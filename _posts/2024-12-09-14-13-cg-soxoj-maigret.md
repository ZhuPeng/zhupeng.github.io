---
layout: post
title: GitHub 开源项目 soxoj/maigret 介绍，🕵️‍♂️ Collect a dossier on a person by username from thousands of sites
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 soxoj/maigret，该项目在 GitHub 有超过 11.3k Star。

![](https://stats.deeptrain.net/repo/soxoj/maigret/?theme=light)

一句话介绍该项目：🕵️‍♂️ Collect a dossier on a person by username from thousands of sites




![Open in Cloud Shell](https://user-images.githubusercontent.com/27065646/92304704-8d146d80-ef80-11ea-8c29-0deaabb1c702.png)

![HTML report screenshot](https://raw.githubusercontent.com/soxoj/maigret/main/static/report_alexaimephotography_html_screenshot.png)

![XMind 8 report screenshot](https://raw.githubusercontent.com/soxoj/maigret/main/static/report_alexaimephotography_xmind_screenshot.png)

![](https://komarev.com/ghpvc/?username=maigret&color=brightgreen&label=views&style=flat-square)

![](https://raw.githubusercontent.com/soxoj/maigret/main/static/maigret.png)

![](https://asciinema.org/a/Ao0y7N0TTxpS0pisoprQJdylZ.svg)


###### 项目介绍

在当今信息爆炸的时代，知识和数据遍布互联网的每一个角落。在这样一个信息高度集成的时代，我们时常会面临一个问题，即如何在成千上万的网站中找到某个人的详细信息。这可能是出于各种目的，例如背景调查、网络安全分析、社交媒体调研等。然而，这项任务常常显得繁重而困难，尤其是对于没有相应工具的人来说。此时，一个功能强大、使用方便的工具就显得尤为重要。

**Maigret** 项目正是在这样的背景下应运而生。这个项目以虚构的法国警探 Jules Maigret 为灵感，开发了一个通过仅需一个用户名，就能在超过 3000 个网站中搜集个人档案的工具。Maigret 能够解析个人资料页面，提取个人信息、链接到其他资料等。其强大之处在于，它不仅支持对 Tor 和 I2P 网站的检查，还能进行域名解析，而所有这些功能都无需 API 密钥。此外，Maigret 还支持标签搜索、检测审查和验证码，并且能够进行请求重试，保证了搜索的全面性和深度。

要使用 **Maigret**，用户有多种安装选项，包括直接从 PyPI 安装、通过 Docker 运行，或者克隆仓库后在本地安装。其中，最简单的安装方法是通过 pip：

```bash
pip3 install maigret
```

安装完成后，使用也非常简单。例如，要生成某个用户名的 HTML、PDF 和 Xmind8 报告，用户仅需执行以下命令：

```bash
maigret 用户名 --html
maigret 用户名 --pdf
maigret 用户名 --xmind #Output not compatible with xmind 2022+
```

Maigret 不仅提供了强大的功能，而且还保持了活跃的开发状态。项目的源代码是开放的，这意味着任何人都可以参与贡献，无论是添加新的网站、改进代码，还是修复 bug。此外，作为 Sherlock 项目的一个分支，Maigret 也继承了其可靠性和强大的社区支持。

在推荐这个项目时，有几点值得一提。首先，考虑到其背后的开发者社区和积极性，用户可以期待 Maigret 进行持续的改进和更新。其次，该工具已有多个案例证明其有效性，无论是对个人或公司来说，都是强有力的网络信息搜集工具。最后，Maigret 项目完全开源，采用 MIT 许可证，用户可以自由地使用和分发。

总之，对于需要在互联网上搜集个人信息的用户来说，Maigret 提供了一个快速、全面、且易于使用的解决方案。无论是网络安全专家、数据分析师，还是普通的调查人员，都可以从这个工具中受益。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=soxoj/maigret&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/soxoj/maigret 

开源项目作者：soxoj

开源协议：MIT License

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=soxoj/maigret)

关注我们，一起探索有意思的开源项目。

