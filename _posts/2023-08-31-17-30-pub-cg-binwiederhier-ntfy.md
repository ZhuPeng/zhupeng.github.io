---
layout: post
title: ntfy - 一个基于 HTTP 的简单发布订阅通知服务
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在我们的日常编程工作中，经常会遇到需要及时获取信息的情况，比如需要追踪某个任务的完成情况，或者需要及时获取某个事件的通知。然而，传统的通知方式往往需要我们去主动查询，或者需要通过电子邮件、短信等方式接收，这些方式不仅效率低下，而且可能会被各种信息淹没。这个时候，我们就需要一个能够主动推送通知到我们手机或者桌面的服务。

今天要给大家推荐一个 GitHub 开源项目 binwiederhier/ntfy，该项目在 GitHub 有超过 12.0k Star，用一句话介绍该项目就是：“Send push notifications to your phone or desktop using PUT/POST”。

![](https://raw.githubusercontent.com/binwiederhier/ntfy/master/web/public/static/images/ntfy.png)

![](https://raw.githubusercontent.com/binwiederhier/ntfy/master/.github/images/screenshot-curl.png)

###### 项目介绍

ntfy 是一个基于 HTTP 的简单发布订阅通知服务，你可以通过任何计算机的脚本发送通知到你的手机或桌面，而无需注册或支付任何费用。ntfy 是开源的，如果你想运行自己的服务实例，可以很容易地做到。你可以在 ntfy.sh 上访问 ntfy 的免费版本，如果你不想自己进行服务搭建，也有收费版本可以选择。此外，还有开源的 Android 和 iOS 应用可以在 Google Play 和 App Store 上获取。

以下是一些通知的推送示例：

![](https://raw.githubusercontent.com/binwiederhier/ntfy/master/.github/images/screenshot-web-detail.png)

![](https://raw.githubusercontent.com/binwiederhier/ntfy/master/.github/images/screenshot-phone-main.jpg)

![](https://raw.githubusercontent.com/binwiederhier/ntfy/master/.github/images/screenshot-phone-detail.jpg)
![](https://raw.githubusercontent.com/binwiederhier/ntfy/master/.github/images/screenshot-phone-notification.jpg)

以下是该项目支持各国语言的情况：

![](https://hosted.weblate.org/widgets/ntfy/-/multi-blue.svg)

###### 如何使用

你可以通过 HTTP 的 PUT/POST 方法发送通知到 ntfy，然后 ntfy 会将这些通知推送到你的手机或桌面。以下是一个安卓 APP 的使用示例：

视频地址：https://docs.ntfy.sh/static/img/android-video-overview.mp4

###### 项目推介

ntfy 项目的维护者不仅提供了详细的文档，还设立了多种方式供用户交流和反馈问题，包括 Discord 服务器，Matrix 房间，Lemmy 讨论板，以及 GitHub issues。此外，项目还提供了付费计划，你可以通过购买付费计划来支持 ntfy 的开发。如果你在寻找一个能够方便地发送推送通知的服务，那么 ntfy 是一个非常好的选择。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=binwiederhier/ntfy&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/binwiederhier/ntfy 

开源项目作者：binwiederhier

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=binwiederhier/ntfy)

关注我们，一起探索有意思的开源项目。

