---
layout: post
title: 一款全能型内网安全扫描工具
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

随着信息技术的快速发展，企业内网的复杂程度日益增加，面对潜在的安全威胁，安全检测成为维护内网安全的重要手段。然而，传统的安全检测工具或服务往往仅覆盖有限的范围，无法全面评估和应对内网潜在的安全风险。特别是在大型网络环境中，信息搜集、漏洞扫描、服务爆破等多个阶段的工作量庞大，且极易漏掉部分工作令人头疼。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-496cbf55824923fcc20e0888cf8f0fcf.png)

今天要给大家推荐一个 GitHub 开源项目 fscan，该项目在 GitHub 有超过 9.8k Star。

![](https://stats.deeptrain.net/repo/shadow1ng/fscan/?theme=light)

一句话介绍该项目：一款内网综合扫描工具，方便一键自动化、全方位漏洞扫描。

![](https://raw.githubusercontent.com/shadow1ng/fscan/master/image/1.png)


###### 项目介绍

fscan 是一款强大的内网综合扫描工具，旨在为安全工程师提供一键自动化、全方位的漏洞扫描功能。该工具支持主机存活探测、端口扫描、常见服务的爆破、高危漏洞扫描如 ms17010、Redis 批量写公钥、计划任务反弹 shell、读取 Windows 网卡信息、Web 指纹识别、Web 漏洞扫描等功能，基本覆盖了内网安全检测的各个方面。此外，fscan 的设计理念注重易用性和效率，大大减轻了安全专家的工作负担。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240725220846904.png)

###### 如何使用

fscan 的安装和使用相当简单，用户可以直接在 GitHub Release 上获取最新的可执行程序。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240725220928819.png)

以下是一些基本用法和示例：

1、简单用法，使用全部模块扫描

```bash
fscan.exe -h 192.168.1.1/24 
```

![](https://raw.githubusercontent.com/shadow1ng/fscan/master/image/4.png)

2、Redis 写公钥和计划任务反弹 shell：

```bash
# Redis rsa
fscan.exe -h 192.168.1.1/24 -rf id_rsa.pub 
```

![](https://raw.githubusercontent.com/shadow1ng/fscan/master/image/2.png)

###### 项目推介

凭借着强大的功能、简便的操作和活跃的社区支持，fscan 已经获得了广泛的认可和好评，无论是对于安全新手还是老手来说，都是一个值得尝试和长期关注的工具。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240725221346472.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=shadow1ng/fscan&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/shadow1ng/fscan 

开源项目作者：shadow1ng

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=shadow1ng/fscan)

关注我们，一起探索有意思的开源项目。

