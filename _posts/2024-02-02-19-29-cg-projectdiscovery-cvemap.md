---
layout: post
title: GitHub 开源项目 projectdiscovery/cvemap 介绍，Navigate the CVE jungle with ease.
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 projectdiscovery/cvemap，该项目在 GitHub 有差不多 1000 Star，用一句话介绍该项目就是：“Navigate the CVE jungle with ease.”。


![image](https://raw.githubusercontent.com/projectdiscovery/cvemap/master/static/cvemap.png)
![](https://raw.githubusercontent.com/projectdiscovery/nuclei-burp-plugin/main/static/join-discord.png)



背景介绍：
在信息安全的领域，常见的一个难题就是如何有效、便利的获取及管理广大如森林的漏洞库呢？为了应对大量的CVE（公共漏洞和披露），通常会花费大量的时间和精力去遍历多个漏洞数据库，如国家漏洞数据库 (NVD)，已知的被利用的漏洞目录 (KEV)，黑客攻击预测评分系统 (EPSS)，以及各种出现在Github上面的漏洞验证模板和已公开的漏洞代码的库。每当新的漏洞出现，即使是有经验的开发者也需要花费大量的时间去收集和阅读相关信息。这样一来，无论我们是要针对应用程序和系统进行安全分析，还是只是想跟踪和管理已知漏洞，都会感到力不从心。

项目介绍：
综合以上痛点，我向您介绍 Github 上的开源项目 " CVEMAP "。根据项目的一句话介绍 " Navigate the CVE jungle with ease. "，我们可以获知：CVEMAP 是一个命令行工具，它旨在提供一种结构化且易于导航的界面，以便访问各种漏洞数据库。CVEMAP 的主要功能包括：CVE 数据集搜索和查询、CVE 到 EPSS 映射、CVE 到 KEV 映射、CVE 到 CPE 映射、CVE 到 GitHub 公开 POCs 的映射、CVE 到 Nuclei 模板的映射、CVE 到 HackerOne 报告的映射，可以在 CVE 数据上应用自定义过滤器，使用 STDIN 输入 / JSONL 输出。

如何使用：
CVEMAP 需要 Go 1.21 才能成功安装。要安装，请运行以下命令：

```console
go install github.com/projectdiscovery/cvemap/cmd/cvemap@latest
```

CVEMAP 的使用非常简单，只需在命令行输入 ' cvemap -h '，即可显示此工具支持的所有开关。

CVEMAP CLI 基于 CVEMap API 构建，要求有来自 ProjectDiscovery Cloud Platform 的API Token，可以通过名为 `PDCP_API_KEY` 的环境变量或使用交互式 `-auth` 选项进行配置。

项目推介：
目前，CVEMAP 是由知名的安全团队 projectdiscovery 维护更新的。项目往往每 6 小时更新一次漏洞数据集，可以看出项目的活跃度和维护者的用心程度。由于其强大的功能和方便的操作，这个工具得到了很多开发者的喜爱和使用。如果你也在与漏洞数据库的海洋进行斗争，那 CVEMAP 是你不能错过的一款强大工具。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=projectdiscovery/cvemap&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/projectdiscovery/cvemap 

开源项目作者：projectdiscovery

开源协议：MIT License

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=projectdiscovery/cvemap)

关注我们，一起探索有意思的开源项目。

