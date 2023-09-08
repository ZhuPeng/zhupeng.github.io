---
layout: post
title: GitHub 开源项目 acheong08/obi-sync 介绍，Reverse engineering of the native Obsidian sync and publish server
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 acheong08/obi-sync，该项目在 GitHub 有超过 789 Star，用一句话介绍该项目就是：“Reverse engineering of the native Obsidian sync and publish server”。







背景介绍：
在我们日常的工作和学习中，经常会遇到需要在不同设备之间同步文件的需求，而 Obsidian 是一款非常受欢迎的知识管理工具，但是其原生的同步和发布服务器的功能有时并不能满足我们的需求。这时候，我们就需要一个可以实现反向工程的 Obsidian 同步和发布服务器，帮助我们更好地管理和同步我们的文件。

项目介绍：
" Rev Obsidian Sync " 是一个反向工程的 Obsidian 同步和发布服务器，这个项目并非官方版本，但是它提供了一些非常实用的功能。首先，它可以实现端到端的加密，保证了我们文件的安全性。其次，它支持实时同步，无论你是在 IOS、Android、Linux、MacOS 还是 Windows 上，都可以通过插件实现文件的实时同步。此外，它还支持文件历史记录、恢复和快照，以及保险库分享和发布（目前只支持 markdown，暂时还不支持渲染）。这些功能都可以帮助我们更好地管理和同步我们的文件。

如何使用：
你可以通过 Docker 快速启动这个项目，首先你需要设置一些环境变量，比如你的服务器的域名或 IP 地址（如果不是在 80 或 433 端口，需要包含端口）。然后，你可以通过以下命令来构建和运行这个项目：
- git clone https://github.com/acheong08/obsidian-sync
- cd obsidian-sync
- go run cmd/obsidian-sync/main.go
最后，你需要安装和配置插件，就可以开始使用这个项目了。

项目推介：
这个项目目前正在积极开发中，作者是一个非常有经验的开发者，他对这个项目的维护非常用心。虽然这个项目还在开发阶段，但是已经有很多人开始关注和使用这个项目了。如果你也是 Obsidian 的用户，希望能够更好地管理和同步你的文件，那么这个项目绝对值得你一试。







以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=acheong08/obi-sync&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/acheong08/obi-sync 

开源项目作者：acheong08

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=acheong08/obi-sync)

关注我们，一起探索有意思的开源项目。

