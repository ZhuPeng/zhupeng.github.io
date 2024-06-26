---
layout: post
title: PMail - 一种快速、简单、安全搭建私人邮件服务器的解决方案
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在现代社会，电子邮件已经成为人们日常生活和工作中必不可少的一部分。然而，使用第三方邮件服务商的安全性和隐私性存在一定的风险。因此，许多人希望能够拥有自己的私人邮件服务器，但是搭建私人邮件服务器需要一定的技术知识和时间成本。而 PMail 项目的出现，为用户提供了一种快速、简单、安全的搭建私人邮件服务器的解决方案。

PMail 在 GitHub 有 498 Star，用一句话介绍该项目就是：“Private EMail Server”。


![](https://raw.githubusercontent.com/Jinnrry/PMail/master/./docs/en.gif)

###### 项目介绍

PMail 是一个个人邮件服务器，追求最小化的部署过程和极低的资源消耗。它运行在单个文件上，包含完整的发送/接收邮件服务和网页端邮件管理功能。只需要一个服务器、一个域名、一行代码、一分钟的部署时间，您就能够建立自己的域名邮箱。PMail具有单文件操作和易于部署的特点，二进制文件仅为15MB，在运行期间占用不到10M的内存。它支持dkim、spf校验，如果正确配置，可以得到10分的邮件测试分数。PMail实现了ACME协议，程序将自动获取和更新Let's Encrypt证书。默认情况下，为Web服务生成了一个SSL证书，允许页面使用https协议。如果您有自己的网关或不需要https，请在配置文件中将use_https设置为false，以便Web服务不使用https。（注意：即使您不需要https，请确保SSL证书文件的路径是正确的，虽然Web服务不再使用证书，但smtp协议仍需要证书）。

当然因为追求最小化，PMail 同样舍弃了一些东西，比如目前只有核心功能是比较完整的，其他还有比较多的缺失，比如权限，还有 UI 是比较丑的。

###### 如何使用

您可以通过以下步骤来使用PMail：

1、下载：点击链接下载适合您的程序文件，或使用Docker。

````bash
# 下载链接：https://github.com/Jinnrry/PMail/releases

docker pull ghcr.io/jinnrry/pmail:latest
````

2、运行：运行程序文件或使用Docker。

3、配置：在浏览器中打开 127.0.0.1 按照提示进行配置。

4、邮件测试：检查您的邮箱是否完成了所有的安全配置。建议使用 https://www.mail-tester.com/ 进行检查。

5、微信消息推送：打开运行目录中的 config.json 文件，在开头编辑几个配置项，然后重新启动服务。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=Jinnrry/PMail&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/Jinnrry/PMail 

开源项目作者：Jinnrry

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=Jinnrry/PMail)

关注我们，一起探索有意思的开源项目。

