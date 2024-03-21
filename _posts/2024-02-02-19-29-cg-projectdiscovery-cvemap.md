---
layout: post
title: 方便访问安全漏洞数据库的工具
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在信息安全的领域，常见的一个难题就是如何有效、便利的获取及管理广大的漏洞库？为了应对大量的 CVE（公共漏洞和披露），通常会花费大量的时间和精力去遍历多个漏洞数据库，如国家漏洞数据库 (NVD)，已知的被利用的漏洞目录 (KEV)，黑客攻击预测评分系统 (EPSS)，以及各种出现在 GitHub 上面的漏洞验证模板和已公开的漏洞代码的库。每当新的漏洞出现，即使是有经验的开发者也需要花费大量的时间去收集和阅读相关信息。这样一来，无论我们是要针对应用程序和系统进行安全分析，还是只是想跟踪和管理已知漏洞，都会感到力不从心。

今天要给大家推荐一个 GitHub 开源项目 projectdiscovery/cvemap，该项目在 GitHub 有差不多 1000 Star，用一句话介绍该项目就是：Navigate the CVE jungle with ease.

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240311225418221.png)

###### 项目介绍

CVEMAP 是一个命令行工具，它旨在提供一种结构化且易于导航的界面，以便访问各种漏洞数据库。CVEMAP 的主要功能包括：CVE 数据集搜索和查询、CVE 到 EPSS 映射、CVE 到 KEV 映射、CVE 到 CPE 映射、CVE 到 GitHub 公开 POCs 的映射、CVE 到 Nuclei 模板的映射、CVE 到 HackerOne 报告的映射，可以在 CVE 数据上应用自定义过滤器，使用 STDIN 输入 / JSONL 输出。

以下是一个使用示例：

![](https://raw.githubusercontent.com/projectdiscovery/cvemap/master/static/cvemap.png)

###### 如何使用

CVEMAP 需要 Go 1.21 才能成功安装。安装运行以下命令：

```console
go install github.com/projectdiscovery/cvemap/cmd/cvemap@latest
```

在命令行输入 cvemap -h ，即可显示此工具支持的所有参数。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240311225612444.png)

CVEMAP CLI 基于 CVEMap API 构建，要求有来自 ProjectDiscovery Cloud Platform 的 API Token，可以通过名为 `PDCP_API_KEY` 的环境变量或使用交互式 `-auth` 选项进行配置。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240311225649723.png)

###### 项目推介

目前，CVEMAP 是由知名的安全团队 projectdiscovery 维护更新的。项目往往每 6 小时更新一次漏洞数据集，可以看出项目的活跃度和维护者的用心程度。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240311225810752.png)


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=projectdiscovery/cvemap&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/projectdiscovery/cvemap 

开源项目作者：projectdiscovery

开源协议：MIT License

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=projectdiscovery/cvemap)

关注我们，一起探索有意思的开源项目。

