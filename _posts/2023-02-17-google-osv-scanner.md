---
layout: post
title: 一款使用 Go 开发的漏洞扫描工具
tags: 安全扫描
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 google/osv-scanner，该项目在 GitHub 有超过 4.3k Star，用一句话介绍该项目就是：“Vulnerability scanner written in Go which uses the data provided by https://osv.dev”，一款使用 Go 开发的漏洞扫描工具。

osv-scanner 是一个由 Google 开源的应用程序安全性扫描器。它可以自动扫描应用程序代码以查找常见的安全漏洞，并生成漏洞报告。该项目基于 Go 开发，可以运行在 Linux, MacOS 和 Windows 系统上。

osv-scanner 支持扫描多种编程语言，包括 Java, Python, C/C++, C#, Go, Ruby, JavaScript 等。它提供了大量的规则来检测常见的漏洞，如 SQL 注入，跨站脚本（XSS）漏洞，路径遍历漏洞，以及许多其他类型的漏洞。这个项目可以帮助您更快，更准确地发现应用程序中的安全漏洞，并可以帮助开发人员更早地修复这些问题。

以下是 osv-scanner 项目的 Star 趋势：

![Stargazers over time](https://starchart.cc/google/osv-scanner.svg)


### 如何安装使用

要安装 osv-scanner 项目，可以使用如下几种方式：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230212185810075.png)


### 使用示例 DEMO

以下是一个简单的示例使用 osv-scanner 扫描本地目录中的代码文件：

```Bash
osv-scanner -r /path/to/your/dir
```

如果需要在扫描时对特定的版本依赖进行扫描，可以在参数加上 --lockfile，比如如下是针对 node 和 python 项目的。

```bash
osv-scanner --lockfile=/path/to/your/package-lock.json --lockfile=/path/to/another/Cargo.lock
# Python
osv-scanner --lockfile 'requirements.txt:/path/to/your/extra-requirements.txt'
```


更多项目详情请查看如下链接。

开源项目地址：https://github.com/google/osv-scanner  (文末可点击阅读原文)

开源项目作者：osv-scanner

