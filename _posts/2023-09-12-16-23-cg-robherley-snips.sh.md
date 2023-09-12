---
layout: post
title: GitHub 开源项目 robherley/snips.sh 介绍，✂️ passwordless, anonymous SSH-powered pastebin with a human-friendly TUI and web UI
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 robherley/snips.sh，该项目在 GitHub 有超过 774 Star，用一句话介绍该项目就是：“✂️ passwordless, anonymous SSH-powered pastebin with a human-friendly TUI and web UI”。


![](https://vhs.charm.sh/vhs-1MRS4DCN6XUpxzM2PrqCfL.gif)
![](https://vhs.charm.sh/vhs-2GYlJ8Fh4RYnYpN141jgtT.gif)
![](https://vhs.charm.sh/vhs-7j0LzNCGaBjF6v91QkXJgr.gif)
![](https://vhs.charm.sh/vhs-52eZOU1lp0y0ZwUFN6lkUm.gif)





背景介绍：在日常的开发工作中，我们经常需要分享代码片段，但是传统的方式如邮件、即时通讯工具等，不仅操作繁琐，而且无法保证代码的格式和高亮，给阅读带来困扰。同时，对于一些敏感信息，我们希望能有一种方式能够实现定时销毁，避免信息的泄露。

项目介绍：snips.sh 是一个 SSH 驱动的无密码、匿名的剪贴板，它具有人性化的 TUI 和 web UI。它的主要特点包括：无需安装，只需要有 SSH 客户端就可以使用；提供 Web UI，支持代码高亮、短链接和 markdown 渲染；提供 TUI，可以在终端中进行剪贴板管理和查看；无需密码，只需要 SSH 密钥；匿名使用，无需注册、登录和邮箱；支持时间限制的 URL，用于敏感信息的分享；可以自我托管，容器化并且资源占用少；智能识别源代码的语言。

如何使用：如果你有 SSH 密钥，你可以这样上传代码：

```
echo '{ "hello" : "world" }' | ssh snips.sh
```

如果你想访问 TUI，你可以这样操作：

```
ssh snips.sh
```

项目推介：snips.sh 是一个非常活跃的开源项目，作者 robherley 是一个有经验的开发者，他的其他项目也得到了广泛的关注和使用。snips.sh 的设计理念和实现方式都非常独特，它解决了开发者在代码分享中遇到的很多问题，是一个非常值得推荐的项目。



以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=robherley/snips.sh&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/robherley/snips.sh 

开源项目作者：robherley

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=robherley/snips.sh)

关注我们，一起探索有意思的开源项目。

