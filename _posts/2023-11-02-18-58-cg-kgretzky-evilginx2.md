---
layout: post
title: GitHub 开源项目 kgretzky/evilginx2 介绍，Standalone man-in-the-middle attack framework used for phishing login credentials along with session cookies, allowing for the bypass of 2-factor authentication
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 kgretzky/evilginx2，该项目在 GitHub 有超过 8.6k Star，用一句话介绍该项目就是：“Standalone man-in-the-middle attack framework used for phishing login credentials along with session cookies, allowing for the bypass of 2-factor authentication”。


![](https://raw.githubusercontent.com/kgretzky/evilginx2/master/media/img/evilginx2-logo-512.png)
![](https://raw.githubusercontent.com/kgretzky/evilginx2/master/media/img/evilginx2-title-black-512.png)
![](https://raw.githubusercontent.com/kgretzky/evilginx2/master/media/img/screen.png)
![](https://raw.githubusercontent.com/kgretzky/evilginx2/master/media/img/evilginx_mastery.jpg)







背景介绍：
在网络安全领域，钓鱼攻击一直是一个棘手的问题。攻击者通过伪造网站，诱导用户输入登录凭证，从而窃取用户信息。尽管现在大多数网站都采用了两步验证（2-factor authentication）的方式来提高安全性，但是这并不能完全阻止钓鱼攻击。因为攻击者可以通过中间人攻击（Man-in-the-middle attack）的方式，获取到用户的登录凭证和会话cookie，从而绕过两步验证。这就是我们需要关注的核心问题。

项目介绍：
Evilginx 是一个独立的中间人攻击框架，主要用于钓鱼攻击，可以窃取用户的登录凭证和会话cookie，从而绕过两步验证。该项目是 2017 年发布的 Evilginx 的继任者，原版本使用定制的 nginx HTTP 服务器提供中间人功能，作为浏览器和被钓鱼网站之间的代理。现在的版本完全用 GO 语言编写，实现了自己的 HTTP 和 DNS 服务器，使得设置和使用变得极其简单。

如何使用：
Evilginx 的安装和使用可以参考在线文档：https://help.evilginx.com。在这里，你可以找到详细的安装和使用教程。

项目推介：
Evilginx 是由知名开发者 Kuba Gretzky (@mrgretzky) 开发并维护的，项目活跃，代码质量高，已经获得了广大开发者的认可。虽然该工具可能被用于恶意目的，但其真正的价值在于提醒我们，作为防御者，需要考虑到这种攻击方式，并找到保护用户免受此类钓鱼攻击的方法。因此，Evilginx 只应在获得被钓鱼方书面许可的合法渗透测试任务中使用。如果你对反向代理钓鱼有兴趣，还可以查看作者的 Evilginx Mastery 课程，学习最新的钓鱼方法，以及如何使用 Evilginx 进行攻击。







以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=kgretzky/evilginx2&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/kgretzky/evilginx2 

开源项目作者：kgretzky

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=kgretzky/evilginx2)

关注我们，一起探索有意思的开源项目。

