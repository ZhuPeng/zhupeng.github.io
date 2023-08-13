---
layout: post
title: Mailpit - 为开发者提供的电子邮件和SMTP测试工具
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

在开发过程中，我们常常会面临测试电子邮件和 SMTP 功能的需求。然而，手动测试这些功能通常很麻烦且耗时，特别是需要频繁发送和接收大量电子邮件的情况下。这正是 Mailpit 项目所解决的核心问题。

今天要给大家推荐一个 GitHub 开源项目 axllent/mailpit，该项目在 GitHub 有超过 1.1k Star，用一句话介绍该项目就是：“An email and SMTP testing tool with API for developers”。


![](https://raw.githubusercontent.com/axllent/mailpit/develop/docs/screenshot.png)

## 项目介绍

Mailpit 是一个面向开发者的多平台电子邮件测试工具和API。它同时充当SMTP服务器和提供Web界面以查看所有捕获的电子邮件。

与 [MailHog](#why-rewrite-mailhog) 相比，Mailpit的速度更快，极大地提高了测试效率。

主要功能包括：
- 单个可执行文件即可运行，无需安装
- SMTP服务器（默认为 `0.0.0.0:1025`）
- Web界面查看电子邮件（支持格式化HTML、高亮HTML源码、纯文本、标头、原始源码以及包含图像缩略图的MIME附件）
- 在桌面模式下，可切换至移动设备和平板电脑的HTML预览
- 高级邮件搜索（详见Wiki：https://github.com/axllent/mailpit/wiki/Mail-search）
- 消息标记（详见 Wiki：https://github.com/axllent/mailpit/wiki/Tagging）
- 使用Web套接字实时更新Web界面的新邮件
- 支持浏览器通知新邮件提醒（仅限HTTPS和`localhost`）
- 可配置的自动电子邮件修剪功能（默认保留最近的500封邮件）
- 电子邮件存储可选择在临时或持久化数据库中（详见Wiki：https://github.com/axllent/mailpit/wiki/Email-storage）
- 快速的SMTP处理和存储速度 - 根据CPU、网络速度和电子邮件大小，每秒处理约70-100封电子邮件，轻松处理成千上万封邮件
- SMTP中继/消息发布 - 通过不同的SMTP服务器中继消息，包括可选的接受列表

## 如何使用

你可以按照以下步骤安装和使用 Mailpit：
1. 在 项目链接 https://github.com/axllent/mailpit 中找到并下载最新的可执行文件。
2. 根据你的操作系统和需求，配置 Mailpit 的设置文件。
3. 运行 Mailpit 可执行文件启动SMTP服务器和Web界面。
4. 在Web界面中，你可以查看所有捕获的电子邮件，并使用高级搜索功能来查找特定的邮件。
5. 如果你是开发者，可以使用 Mailpit 的API来集成和测试电子邮件功能。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=axllent/mailpit&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/axllent/mailpit 

开源项目作者：axllent

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=axllent/mailpit)

关注我们，一起探索有意思的开源项目。

