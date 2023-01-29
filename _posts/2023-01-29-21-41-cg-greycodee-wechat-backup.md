---
layout: post
title: GitHub 开源项目 greycodee/wechat-backup 介绍，微信聊天记录持久化备份本地硬盘，释放手机存储空间。
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 greycodee/wechat-backup，该项目在 GitHub 有超过 1.9k Star，用一句话介绍该项目就是：“微信聊天记录持久化备份本地硬盘，释放手机存储空间。”。

![](https://raw.githubusercontent.com/greycodee/wechat-backup/master/./web.png)

greycodee/wechat-backup 是一个基于 Python 的微信聊天记录备份工具。它可以将你的微信聊天记录导出到文本文件中，并支持导出多种格式，如 JSON、CSV 和 HTML。该项目还提供了一些额外的功能，如过滤聊天记录中的图片和语音消息。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=greycodee/wechat-backup&type=Timeline)

安装：

- 安装 python3
- 安装依赖库： wxpy、pandas、beautifulsoup4
- 下载源码并运行 python3 wechat_backup.py

用法：

- 扫码登录
- 输入好友昵称或备注
- 选择需要导出的格式
- 导出完成后会在当前目录生成文件

代码示例：

```
from wechat_backup import WeChatBackup

# 初始化
wechat_backup = WeChatBackup()

# 扫码登录
wechat_backup.login()

# 输入好友昵称或备注
friend_name = input("请输入好友昵称或备注：")

# 选择需要导出的格式
export_format = input("请选择需要导出的格式（json/csv/html）：")

# 导出聊天记录
wechat_backup.export_chat_history(friend_name, export_format)

# 导出完成
print("导出完成！")
```


更多项目详情请查看如下链接。

开源项目地址：https://github.com/greycodee/wechat-backup 

开源项目作者：greycodee

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=greycodee/wechat-backup)

