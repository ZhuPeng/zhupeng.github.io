---
layout: post
title: 推荐一个邮箱检测工具，功能非常多
tags: 其他
---

大家好。

虽然我们现在很多的场合都在使用实时通信工具，但是电子邮箱依然在非常多的场合下使用，比如资讯订阅、找回密码、验证信息、正式的网络通信等。

今天要推荐的工具 check-if-email-exists 能够检测一个电子邮箱是否存在、是否可发送、是否设置了头像、是否泄露过密码等多项检测，而且检测是不需要前置去实际发送邮件的。以下是目前支持的检测功能：

![image-20220123203137730](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220123203137730.png)

check-if-email-exists 工具不管你是单独使用，还是集成到你的产品中都非常的方便。

1、单独使用：下载命令行工具

![image-20220123203255688](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220123203255688.png)

2、产品集成：导入 Rust 库

![image-20220123203315149](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220123203315149.png)

3、如果不想单独自己开发，也可以使用官方提供的 SaaS 服务，当然是需要付费的（每月 50 次的免费额度）

如果你的产品需要批量的去给客户发送电子邮件，前置对邮件进行必要的检测，能够尽早的发现电子邮箱上的问题，避免邮件发出之后的风险，尤其对于对方邮件密码是否泄露，涉及很多的安全问题。

更多项目详情请查看如下链接。

开源项目地址：https://github.com/reacherhq/check-if-email-exists
