---
layout: post
title: GitHub 开源项目 usememos/memos 介绍，An open source, lightweight note-taking service. Easily capture and share your great thoughts.
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 usememos/memos，该项目在 GitHub 有超过 21.3k Star，用一句话介绍该项目就是：“An open source, lightweight note-taking service. Easily capture and share your great thoughts.”。


![demo](https://www.usememos.com/demo.webp)
![](https://www.usememos.com/full-logo-landscape.png)
![](https://contri-graphy.yourselfhosted.com/graph?repo=usememos/memos&format=svg)



背景介绍：
在日常工作和生活中，我们时常有很多想法和灵感闪现，但由于各种原因（比如手头没纸笔、事后忘记等），这些灵感往往就像过眼云烟一样消失不见。另外在团队协作时，我们可能会感到交流和共享信息的方式过于繁琐。这里就存在一个需求，那就是一个开源、轻量级、注重隐私的，且容易分享的记事本服务。

项目介绍：
Memos 是一个注重隐私、轻量级的记事服务，它可以轻松捕获并分享你的好主意。项目主要的亮点包括：
- 开源且永久免费，解放创新未来，让创造力无界。
- 在几秒钟内通过 Docker 自我托管，给你拥有全方位数据控制权和隐私保障的自由。
- 支持纯文本和 Markdown，告别繁琐的富文本格式，欣赏简洁清晰的笔记。
- 方便地定制和分享你的笔记，在团队中无缝协作和分享你的思想。
- 提供 RESTful API 与第三方服务集成，创造出无限可能。

如何使用：
如果你已经安装了 Docker，那么在几秒钟内就可以部署 Memos ：
```bash
docker run -d --name memos -p 5230:5230 -v ~/.memos/:/var/opt/memos ghcr.io/usememos/memos:latest
```
在这条命令中，‘~/.memos/’ 是你在本地机器上的数据目录，‘/var/opt/memos’ 是 Docker 中的卷的目录，这一部分不应被修改。

项目推介：
Memos 的开发活跃，维护及时，得到了社区的积极响应和广泛应用，已经有很多第三方插件和应用集成该服务，如 iOS 和 Android 的第三方客户端 Moe Memos、Chrome 扩展、微信小程序、Telegram 机器人等，还有客户端适用于 MacOS 和 Windows。此外，项目已经在 GitHub 上获得了大量的 Star，赞美和支持的声音可见一斑。Memos 的丰富特性和活跃的社区使之在采用该项目时值得信赖。在此，我们鼓励并欢迎更多的开发者和用户加入到 Memos 项目的使用和贡献中来，它肯定会在你捕获和分享你的伟大思想中，起到不可或缺的作用。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=usememos/memos&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/usememos/memos 

开源项目作者：usememos

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=usememos/memos)

关注我们，一起探索有意思的开源项目。

