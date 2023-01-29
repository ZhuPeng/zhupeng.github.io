---
layout: post
title: GitHub 开源项目 sari3l/Poc-Monitor 介绍，🔍 Github CVE POC 信息监控推送 🚀
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 sari3l/Poc-Monitor，该项目在 GitHub 有超过 0.0k Star，用一句话介绍该项目就是：“🔍 Github CVE POC 信息监控推送 🚀”。

![](https://user-images.githubusercontent.com/45752995/179657618-4b42753b-4344-4cdd-a068-79bd33d2b33f.jpeg)

Poc-Monitor 是一个用于检测漏洞状态变化的开源项目。它能够定期自动扫描给定的 URL 列表，并在检测到漏洞状态变化时发送通知。该项目使用 Go 语言编写，支持多种通知方式，如邮件、微信、Telegram 等。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=sari3l/Poc-Monitor&type=Timeline)

安装方法:

1. 下载源码：`git clone https://github.com/sari3l/Poc-Monitor.git`
2. 安装依赖：`go mod download`
3. 编译程序：`go build`
4. 运行程序：`./Poc-Monitor -c config.yml`

示例配置文件:

```
scan:
  schedule: "*/5 * * * *"
  urls:
  - "http://example.com/1"
  - "http://example.com/2"
notify:
  mail:
    enable: true
    host: "smtp.example.com"
    port: 587
    username: "notify@example.com"
    password: "password"
    from: "notify@example.com"
    to:
    - "admin@example.com"
    subject: "[Poc-Monitor] 漏洞状态变化"
```

这是一个简单的配置示例，它会在每 5 分钟扫描 "http://example.com/1" 和 "http://example.com/2"，并在检测到漏洞状态变化时发送邮件通知给 "admin@example.com"。

更多项目详情请查看如下链接。

开源项目地址：https://github.com/sari3l/Poc-Monitor 

开源项目作者：sari3l

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=sari3l/Poc-Monitor)

