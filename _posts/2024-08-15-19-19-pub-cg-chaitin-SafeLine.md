---
layout: post
title: 一个自托管网站应用防攻击防火墙
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

随着网络攻击技术的不断进步，网络安全面临着前所未有的挑战，从 SQL 注入、XSS 攻击到更为复杂的 RCE 和 SSRF 攻击，网站和 Web 应用程序的安全防护变得越来越困难。这些攻击不仅威胁到个人和企业的敏感数据，还可能对品牌声誉造成长期的负面影响。在这样的背景下，如何有效地保护我们的 Web 应用程序，确保它们免受网络攻击和利用，成为了每个组织都必须面对的重要问题。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240917204424167.png)

今天要给大家推荐一个 GitHub 开源项目 SafeLine，该项目在 GitHub 有超过 11.9k Star。

![](https://stats.deeptrain.net/repo/chaitin/SafeLine/?theme=light)

一句话介绍该项目：serve as a reverse proxy to protect your web services from attacks and exploits.

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240831225604984.png)


###### 项目介绍

SafeLine 是一个自托管的 WAF(Web Application Firewall)，旨在保护你的 Web 应用免受攻击和利用。SafeLine 通过在 Web 应用和互联网之间部署一个过滤和监控 HTTP 流量的防火墙，保护 Web 应用不受诸如 SQL 注入、XSS、代码注入、操作系统命令注入等攻击的侵害。作为一种反向代理，SafeLine 在客户端与服务器之间建立了一个保护屏障，防止恶意客户端直接接触到后端服务器。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240831225648839.png)

主要功能包括：

1、防御各种 web 攻击

2、主动防御机器人滥用

3、HTML 和 JS 代码加密

4、基于 IP 的速率限制

5、Web 访问控制列表

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240831225816068.png)

###### 如何使用

安装 SafeLine 的具体信息可以在安装指南 [Install](https://docs.waf.chaitin.com/en/tutorials/install) 中找到。

保护 Web 应用的配置和使用指南详见配置指南 [Configuration](https://docs.waf.chaitin.com/en/tutorials/Configuration)。

以下是一些具体的系统页面示例：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240831225944283.png)

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240831225955624.png)

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240831230004986.png)

###### 项目推介

SafeLine 已经证明是一款生产就绪的解决方案，全球安装超过 20 万次，保护超过 100 万个网站，每天处理超过 300 百亿个 HTTP 请求。无论是新手还是有经验的开发人员，都可以轻松部署和使用 SafeLine，以提高其 web 应用程序的安全性。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240831230100696.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=chaitin/SafeLine&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/chaitin/SafeLine 

开源项目作者：chaitin

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=chaitin/SafeLine)

关注我们，一起探索有意思的开源项目。

