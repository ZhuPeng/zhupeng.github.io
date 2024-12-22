---
layout: post
title: 简洁的网页健康监控仪表盘
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在软件开发和维护上，确保在线服务的持续可用性和健康状态成为了每个开发者和企业不可回避的挑战。当面对服务中断或性能下降的问题时，快速定位并解决问题是至关重要的。然而，服务健康监控和故障警报的设置往往既复杂又耗时，尤其是当需要跨多个服务和平台进行时。这就需要一个简单而强大的解决方案，来帮助开发者专注于他们真正重要的事情——构建和优化他们的应用。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-695311a46095790685cde6408e03c7e2.png)

今天要给大家推荐一个 GitHub 开源项目 gatus，该项目在 GitHub 有超过 6.7k Star。

![](https://stats.deeptrain.net/repo/TwiN/gatus/?theme=light)

一句话介绍该项目：⛑ Automated developer-oriented status page

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241216233652015.png)

###### 项目介绍

Gatus 是一个为开发者设计的自动化健康仪表板，提供 HTTP、ICMP、TCP 以及 DNS 查询等多种方式来监控你的服务，并通过一系列条件对查询结果进行评估，诸如状态码、响应时间、证书到期时间、响应体等。最为醒目的功能是，每个健康检查都可以与 Slack、Teams、PagerDuty、Discord、Twilio 等多种警报方式进行配对。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241216233759286.png)

以下是一些示例的页面：

![](https://raw.githubusercontent.com/TwiN/gatus/master/.github/assets/dashboard-dark.png)



![](https://raw.githubusercontent.com/TwiN/gatus/master/.github/assets/github-alerts.png)



![](https://raw.githubusercontent.com/TwiN/gatus/master/.github/assets/gotify-alerts.png)

###### 如何使用

可以通过 Docker 快速使用 Gatus：

```console
docker run -p 8080:8080 --name gatus twinproduction/gatus
```

下图是一个简单的配置及对应的监控页面：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241216234046010.png)

###### 项目推介

Gatus 已经被许多开发者和组织广泛使用，其简便的设定和强大的功能集是其受欢迎的主要原因。作者 TwiN 本人就亲自在 Kubernetes 集群中部署使用 Gatus 来监控他的核心应用，项目网站为 https://status.twin.sh/。这不仅展示了 Gatus 的实战用途，也证明了其稳定和可靠性。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=TwiN/gatus&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/TwiN/gatus 

开源项目作者：TwiN

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=TwiN/gatus)

关注我们，一起探索有意思的开源项目。

