---
layout: post
title: GitHub 开源项目 WuKongIM/WuKongIM 介绍，8年积累，沉淀出来的高性能通用实时通讯服务，支持即时通讯（聊天软件）(IM)(Chat)，消息推送，消息中台，音视频信令，直播弹幕，客服系统，AI通讯，即时社区等场景
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 WuKongIM/WuKongIM，该项目在 GitHub 有超过 864 Star，用一句话介绍该项目就是：“8年积累，沉淀出来的高性能通用实时通讯服务，支持即时通讯（聊天软件）(IM)(Chat)，消息推送，消息中台，音视频信令，直播弹幕，客服系统，AI通讯，即时社区等场景”。


![image](https://raw.githubusercontent.com/WuKongIM/WuKongIM/master/./docs/demo.gif)
![image](https://raw.githubusercontent.com/WuKongIM/WuKongIM/master/./docs/architecture/architecture2.png)
![image](https://raw.githubusercontent.com/WuKongIM/WuKongIM/master/./docs/业务系统对接图.png)
![image](https://raw.githubusercontent.com/WuKongIM/WuKongIM/master/./docs/webhook.png)
![image](https://raw.githubusercontent.com/WuKongIM/WuKongIM/master/./docs/screen1.png)
![image](https://raw.githubusercontent.com/WuKongIM/WuKongIM/master/./docs/screen2.png)
![image](https://raw.githubusercontent.com/WuKongIM/WuKongIM/master/./docs/screen3.png)
![image](https://raw.githubusercontent.com/WuKongIM/WuKongIM/master/./docs/screen4.png)
![image](https://raw.githubusercontent.com/WuKongIM/WuKongIM/master/./docs/screen5.png)
![image](https://raw.githubusercontent.com/WuKongIM/WuKongIM/master/./wechat.jpg)



背景介绍：
在当今信息爆炸的时代，实时通讯服务的需求日益增长。无论是即时通讯（聊天软件）、消息推送、音视频信令、直播弹幕、客服系统，还是 AI 通讯等场景，都离不开高效、稳定、安全的通讯服务支持。然而，市面上的通讯服务产品或多或少存在一些问题，如性能瓶颈、依赖复杂、安全性不足等，这给开发者带来了很大的困扰。

项目介绍：
"WuKongIM" 是一款经过 8 年积累沉淀出来的高性能通用实时通讯服务，它支持即时通讯（聊天软件）(IM)(Chat)、消息推送、消息中台、音视频信令、直播弹幕、客服系统、AI通讯、即时社区等场景。WuKongIM 使用自研的消息数据库、二进制协议和网络库，支持自定义协议。它能够处理百万级在线用户，每秒可处理 160,000 条消息（包括数据库操作），且无任何第三方依赖，部署简单。同时，WuKongIM 对消息通道和消息内容进行加密，防止中间人攻击和消息篡改。此外，WuKongIM 采用基于通道的设计，目前支持群组和点对点通道，可以扩展支持自定义通道，适用于聊天机器人和客服等用例。

如何使用：
首先，你需要在 go1.20.0 或更高版本的环境中编译此项目。具体操作如下：
```shell
git clone https://github.com/WuKongIM/WuKongIM.git
cd WuKongIM
go run main.go --config config/wk.yaml
```
然后，你可以通过访问 http://127.0.0.1:5001/varz 来查看系统信息。

项目推介：
WuKongIM 是一个活跃的开源项目，其背后的开发团队积极响应社区反馈，持续进行优化和更新。此外，WuKongIM 已经在 TangSengDaoDao（基于 WuKongIM 的通讯层）等实际项目中得到应用，表现出色。如果你正在寻找一个高性能、易部署、安全可靠的通讯服务，那么 WuKongIM 绝对值得你一试。




以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=WuKongIM/WuKongIM&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/WuKongIM/WuKongIM 

开源项目作者：WuKongIM

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=WuKongIM/WuKongIM)

关注我们，一起探索有意思的开源项目。

