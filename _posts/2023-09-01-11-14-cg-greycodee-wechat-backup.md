---
layout: post
title: GitHub 开源项目 greycodee/wechat-backup 介绍，微信聊天记录持久化备份本地硬盘，释放手机存储空间。
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 greycodee/wechat-backup，该项目在 GitHub 有超过 2.3k Star，用一句话介绍该项目就是：“微信聊天记录持久化备份本地硬盘，释放手机存储空间。”。


![](https://raw.githubusercontent.com/greycodee/wechat-backup/master/./web.png)





背景介绍：
在日常生活中，我们经常使用微信进行各种沟通交流，而这些聊天记录中可能包含了许多重要的信息。然而，随着聊天记录的增多，手机的存储空间会被大量占用，而且微信自身并没有提供很好的聊天记录备份和查看功能，这就导致了我们无法有效地管理和查看这些聊天记录。这是一个让人头疼的问题，但是现在有了一个开源项目 "wechat-backup"，它可以帮助我们解决这个问题。

项目介绍：
"wechat-backup" 是一个开源项目，它的主要功能是将微信聊天记录持久化备份到本地硬盘，从而释放手机存储空间。项目的主要设计要点包括：收集微信聊天图片、语音、视频、头像、文件等数据，并将这些数据存放在同一个文件夹下；获取解密数据库的密钥，进行微信聊天数据数据库的解密；转换微信语音；运行程序，打开控制台输出的网址，就可以查看你的聊天记录了。

如何使用：
首先，你需要克隆这个项目到你的本地，然后进入项目目录，运行主程序，并将微信备份文件的路径作为参数传入。具体的命令如下：

```
$ git clone https://github.com/greycodee/wechat-backup.git
$ cd wechat-backup
$ go run main.go -f '[替换成你的微信备份文件路径]'
```

如果你的手机没有 ROOT 权限，你还可以通过手机自带的系统备份功能来获取数据。

项目推介：
虽然这个项目目前已经停止维护，但是它的功能强大，使用方便，可以帮助我们有效地管理和查看微信聊天记录，释放手机存储空间。如果你有一定的编程能力，你还可以根据自己的需求对这个项目进行二次开发。因此，我强烈推荐你试试这个项目。






以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=greycodee/wechat-backup&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/greycodee/wechat-backup 

开源项目作者：greycodee

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=greycodee/wechat-backup)

关注我们，一起探索有意思的开源项目。

