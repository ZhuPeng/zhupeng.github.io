---
layout: post
title: 一个简单易用的动态域名解析工具
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在数字化时代中，动态域名解析 (DDNS) 成为了维持网络服务持续在线的关键技术，尤其对于依赖动态 IP 地址的小型企业和个人用户而言。随着 IP 地址频繁变动，手动更新域名解析配置显得繁琐且容易出错。市场上虽有多种 DDNS 解决方案，但复杂的配置流程、有限的服务商支持、缺乏灵活性和安全性顾虑常常让人望而却步。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-0f8b153c160a902b0903d187bbae2519.png)

今天要给大家推荐一个 GitHub 开源项目 jeessy2/ddns-go，该项目在 GitHub 有超过 9.7k Star。

![](https://stats.deeptrain.net/repo/jeessy2/ddns-go)

一句话介绍该项目：Simple and easy to use DDNS. Support Aliyun, Tencent Cloud, Dnspod, Cloudflare, Callback, Huawei Cloud, Baidu Cloud, Porkbun, GoDaddy, Namecheap, NameSilo...


![screenshots](https://raw.githubusercontent.com/jeessy2/ddns-go/master/ddns-web.png)


###### 项目介绍

**ddns-go** 是一个简单易用的 DDNS 工具，支持众多域名服务商，包括 `阿里云`、`腾讯云`、`Dnspod`、`Cloudflare`、`华为云`、`Callback`、`百度云`、`Porkbun`、`GoDaddy`、`Namecheap`、`NameSilo` 等。项目特别适合需要动态 IP 解析的用户和小型企业，通过自动获取公网 IPv4 或 IPv6 地址，并解析到对应的域名服务上，极大地简化了动态域名解析的流程。

ddns-go 的设计特点包括：

1、支持 macOS、Windows、Linux 系统，适应 ARM、x86 等架构

2、多域名服务商支持，满足不同用户需求

3、支持接口、网卡、命令行方式获取 IP 地址

4、简洁的网页配置界面，方便快捷地查看日志和配置

5、支持 Webhook、TTL 设置及自定义参数传递，增强了使用的灵活性和功能丰富性

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240519230817401.png)

###### 如何使用

**系统中使用：**

简单三步让你的 ddns-go 服务运行起来：

1、从 [GitHub Releases](https://github.com/jeessy2/ddns-go/releases) 下载对应系统版本的 ddns-go 并解压。

2、安装服务：

​	2.1、对于 macOS/Linux：在终端运行 `sudo ./ddns-go -s install`。

​	2.2、对于 Windows：以管理员身份打开命令行，运行 `./ddns-go.exe -s install`。

3、在浏览器中打开 `http://主机IP:9876`，按照指引完成配置。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240519231008207.png)

**Docker 中使用：**

```bash
docker run -d --name ddns-go --restart=always --net=host -v /opt/ddns-go:/root jeessy/ddns-go
```

这条命令会将 ddns-go 以容器形式运行，并将配置文件存放在主机的 `/opt/ddns-go` 目录下。

###### 项目推介

ddns-go 因为其简化了 DDNS 的配置流程，提高了解析的效率，也因为项目持续维护更新，社区活跃，为用户提供稳定可靠的动态域名解析服务。无论是个人博客、小企业内网还是其他需要远程访问的场合，ddns-go 都能提供及时、高效的解决方案。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=jeessy2/ddns-go&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/jeessy2/ddns-go 

开源项目作者：jeessy2

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=jeessy2/ddns-go)

关注我们，一起探索有意思的开源项目。

