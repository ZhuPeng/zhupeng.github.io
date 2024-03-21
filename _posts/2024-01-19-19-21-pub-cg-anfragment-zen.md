---
layout: post
title: 系统级别的广告屏蔽应用，不只是浏览器
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

近年来，随着网络技术的广泛应用，网络广告已成为我们日常生活中无法忽视的一部分，然而过滤网络广告却是我们常常头疼的问题。同时，网络隐私泄露问题也令我们烦恼不已。除了浏览器内的广告和跟踪，还有一些桌面应用和操作系统组件等都可能存在广告和隐私跟踪问题，虽然市面已经有一些浏览器插件能够解决部分问题，但是这些问题有的不在浏览器上操作，对应的插件也无法起作用。因此，我们需要一款更全面、更有效的广告屏蔽和隐私保护工具。

今天要给大家推荐一个 GitHub 开源项目 anfragment/zen，该项目在 GitHub 有超过 1.6k Star，用一句话介绍该项目就是：“Simple, free and efficient ad-blocker and privacy guard for Windows, macOS and Linux”。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240303203341619.png)

###### 项目介绍

Zen 是一款面向 Windows、macOS 及 Linux 平台的开源系统级别广告屏蔽和隐私保护应用。它的工作原理是建立一个代理服务器，拦截所有应用的 HTTP 请求，并屏蔽那些提供广告、跟踪代码，以及其它不想看到的内容。通过在系统级别运行，Zen 能解决浏览器插件无法处理的问题，例如嵌入在桌面应用和操作系统组件的跟踪器。Zen 自带许多预装的过滤器，同时也允许您通过添加 hosts 文件和 EasyList 样式的过滤器来定制您的保护设置。

![](https://github.com/anfragment/zen/blob/master/assets/screenshots/main-window.png?raw=true)
![](https://github.com/anfragment/zen/blob/master/assets/screenshots/filter-lists.png?raw=true)

###### 如何使用

使用 `wails build` 可以构建 Zen，使用 `wails dev` 可以在开发模式下运行它。

首次运行 Zen 时，会提示您安装一个根证书，这是为了能够拦截和修改 HTTPS 请求而必需的。此证书在本地生成，永远不会离开您的设备。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240303203440662.png)

###### 项目推介

Zen 的广告屏蔽技术和隐私保护技术也在业内得到了高度认可， 是你必不可少的隐私防护工具。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=anfragment/zen&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/anfragment/zen 

开源项目作者：anfragment

开源协议：MIT License

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=anfragment/zen)

关注我们，一起探索有意思的开源项目。

