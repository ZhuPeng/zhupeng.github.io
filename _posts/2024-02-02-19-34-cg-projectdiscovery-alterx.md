---
layout: post
title: GitHub 开源项目 projectdiscovery/alterx 介绍，Fast and customizable subdomain wordlist generator using DSL
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 projectdiscovery/alterx，该项目在 GitHub 有差不多 1000 Star，用一句话介绍该项目就是：“Fast and customizable subdomain wordlist generator using DSL”。


![image](https://user-images.githubusercontent.com/8293321/229380735-140d3f25-d0cb-461d-8c49-4c1eff43d1f4.png)
![](https://raw.githubusercontent.com/projectdiscovery/nuclei-burp-plugin/main/static/join-discord.png)



背景介绍：在网络安全领域，子域名枚举是一种常见的信息收集技术，越来越多的黑客和渗透测试人员用其寻找潜在的安全漏洞。然而，传统的子域名枚举工具存在两个核心问题：一是生成的子域名列表泛滥，并不能有效增加找到真实子域名的可能性；二是处理速度慢且无法定制，往往不能满足实战需求。

项目介绍：AlterX 是一个快速且可定制的子域名词表生成工具，利用 Domain Specific Language (DSL，领域特定语言) 进行自定义配对。相比其他子域名枚举工具如 `goaltdns` ，AlterX 带来的独一无二的特性在于它的 `scripting` 功能，AlterX 基于输入模式生成子域名排列词表，同理，这也是 [nuclei](https://github.com/projectdiscovery/nuclei) 以 [fuzzing-templates](https://github.com/projectdiscovery/fuzzing-templates) 的方式工作的原理。AlterX 具备自动词汇补充、预设变量、可配置样式等特点，它能从传入的子域名中提取变量，并据此应用预设模板生成更有效的排列组合。

如何使用：安装 AlterX 需要在系统中已经安装了 Golang 1.19 ，Golang 可以从[这里](https://go.dev/doc/install)下载。安装 Golang 后，使用以下命令安装 AlterX ：

```bash
go install github.com/projectdiscovery/alterx/cmd/alterx@latest
```

你可以运行 `./alterx [flags]` 来查看可用的标志和选项。

项目推介：AlterX 是一款由 ProjectDiscovery 团队开发的开源工具，这个团队在信息安全社区享有较高的知名度，已经开发出多款优秀的安全工具如 Nuclei、httpx、dnsx 等。AlterX 项目活跃，更新迭代速度快，指标显示，该项目正在得到越来越多的用户关注和使用，其快速、可定制的特性也得到了用户们的一致好评。无论你是安全研究人员，还是渗透测试员，AlterX 都能帮助你在子域名枚举环节大幅提高效率。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=projectdiscovery/alterx&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/projectdiscovery/alterx 

开源项目作者：projectdiscovery

开源协议：MIT License

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=projectdiscovery/alterx)

关注我们，一起探索有意思的开源项目。

