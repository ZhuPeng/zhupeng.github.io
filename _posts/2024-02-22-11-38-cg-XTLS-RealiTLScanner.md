---
layout: post
title: GitHub 开源项目 XTLS/RealiTLScanner 介绍，A TLS server scanner for Reality
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 XTLS/RealiTLScanner，该项目在 GitHub 有差不多 1000 Star，用一句话介绍该项目就是：“A TLS server scanner for Reality”。





背景介绍：在日常的安全测试和网络监控工作中，TLS 服务器的扫描是难以回避的操作。然而，我们可能会面临一些问题，比如效率低下、输出内容混乱、扫描结果准确性差、缺少地理位置信息等问题。实际工作中，我们需要一个可以快速准确进行TLS 服务器扫描、支持多线程、结构化输出结果以便后续分析，且支持PGP 的工具。

项目介绍： RealiTLScanner 是一个适合现实情况的 TLS 服务器扫描器，它是在 Go 1.21+ 环境下构建的。RealiTLScanner 能扫描指定 IP, IP CIDR 或域名，支持默认端口443 及自定义端口，支持多线程扫描和每个扫描任务的超时设置，可以将扫描结果保存为 CSV 格式，支持 Verbose 输出模式，它支持从 URL 爬取域名并进行扫描，还能从文件中批量读取目标列表进行扫描，这些都大大提高了扫描的效率。另外，只需要在执行文件夹内放置 MaxMind GeoLite2/GeoIP2 的国家数据库文件 `Country.mmdb`，即可启用地理 IP 信息功能，便于我们分析服务器的地理位置。

如何使用：安装和使用 RealiTLScanner 是非常简单的过程。首先我们需要进行构建，只需要在命令行中输入 `go build` 即可。扫描时只需运行 `./RealiTLScanner -addr 1.2.3.4` 即可直接进行扫描。扫描结果会显示出连接情况、目标 IP、是否支持 TLS、ALPN 协议，证书颁发者等详细信息。如果想进行更复杂的操作，比如改变扫描端口、设置线程数量、设置超时时间、保存结果到文件等，也只需添加对应的参数即可。

项目推介：作为一个开源项目，RealiTLScanner 社区活跃、开发状态稳定，作者团队由一组热爱开源、熟知网络安全的工程师构成，且长期在维护和优化这个项目，所以你在使用过程中遇到任何问题都可以得到及时的解答。更重要的是，它在实际使用中获得了非常好的效果，被网络安全工程师们广泛应用。所以，如果你对网络安全扫描感兴趣，RealiTLScanner 绝对是你不可错过的工具。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=XTLS/RealiTLScanner&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/XTLS/RealiTLScanner 

开源项目作者：XTLS

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=XTLS/RealiTLScanner)

关注我们，一起探索有意思的开源项目。

