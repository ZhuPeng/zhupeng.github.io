---
layout: post
title: GitHub 开源项目 projectdiscovery/subfinder 介绍，Fast passive subdomain enumeration tool.
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 projectdiscovery/subfinder，该项目在 GitHub 有超过 10.4k Star。

![](https://stats.deeptrain.net/repo/projectdiscovery/subfinder/?theme=light)

一句话介绍该项目：Fast passive subdomain enumeration tool.




![](https://raw.githubusercontent.com/projectdiscovery/subfinder/master/static/subfinder-logo.png)

![](https://raw.githubusercontent.com/projectdiscovery/subfinder/master/static/subfinder-run.png)


###### 项目介绍

**介绍 `Subfinder`：快速而强大的被动子域名发现工具**

### 背景介绍

在网络安全和信息收集的领域中，探索与目标网站相关联的各个子域名是一项基础而关键的任务。这不仅有助于渗透测试人员和漏洞悬赏猎人理解目标网站的网络架构，还能揭示潜在的安全隐患点。然而，手工搜索子域名极为耗时且低效，且容易遗漏关键信息。因此，一个自动化、快速且准确的子域名枚举工具就显得非常必要。

### 

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-7d8a726c81ed9edd82ae87360909eb9b.png)

项目介绍

`Subfinder` 是一个快速的被动子域名枚举工具，它使用被动在线资源返回网站的有效子域名。项目特点包括简洁的模块化架构，以及对速度的优化，专注于一件事情 - 被动子域名枚举，并且做得非常好。`Subfinder` 遵守所有被用到的被动资源许可和使用限制，其被动模式保证了速度和隐秘性，适合渗透测试人员和漏洞悬赏猎人使用。

**主要特点：**

- 快速且强大的解析和通配符消除模块
- 精选的被动资源以最大化结果
- 支持多种输出格式（JSON，文件，标准输出）
- 优化速度，对资源消耗轻
- 支持 **STDIN/OUT**，便于集成到工作流中

### 如何使用

首先，需要安装 `Go 1.21` 或更高版本：

```sh
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
```

使用示例：

```sh
subfinder -d example.com
```

上述命令将为 `example.com` 寻找子域名。更详细的使用说明和选项可以通过 `subfinder -h` 命令查看。

### 项目推介

`Subfinder` 由 **projectdiscovery** 团队用心打造，得益于社区的贡献而不断进化。它不仅被安全社区的成员广泛使用，也是许多企业安全工作流程中不可或缺的一部分。`Subfinder` 的开发活跃，持续更新以适应新的网络环境和挑战。无论是开发者、渗透测试人员还是安全爱好者，都会发现 `Subfinder` 是探索子域名的强大工具。加入它的 Discord 群组，可以更快地获得支持和与其他用户交流的机会。

总的来说，如果你在寻找一个高效、快速且用户友好的子域名枚举工具，`Subfinder` 绝对值得一试。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=projectdiscovery/subfinder&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/projectdiscovery/subfinder 

开源项目作者：projectdiscovery

开源协议：MIT License

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=projectdiscovery/subfinder)

关注我们，一起探索有意思的开源项目。

