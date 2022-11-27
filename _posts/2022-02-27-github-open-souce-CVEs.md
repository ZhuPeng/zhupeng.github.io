---
layout: post
title: GitHub 开源自建的安全漏洞修复建议数据库
tags: GitHub，安全
---

大家好。

log4j 的漏洞大家还记得么，其实近些年来，针对开源软件的漏洞频发，各大科技公司也都在对自身的软件供应链安全上下功夫，毕竟安全问题无小事，出了问题可能公司就倒闭了。

另外如果你在 GitHub 上开源过代码，如果代码里面有漏洞或者风险的话，会有一个 GitHub 官方的机器人 dependabot 自动创建 PR 来帮助你修复漏洞。

![image-20220227205003364](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220227205003364.png)

那 GitHub 是如何做到的呢？当然 GitHub 会扫描所有的开源代码仓库，找到有漏洞的代码，但是应该如何给出升级或者改进的建议呢？

其实 GitHub 一直很关注开源软件的安全问题，所以内部也一直有全职的安全团队在应对这样或者那样的开源漏洞，并给出相应的修复建议，通过不断的积累就会变成一个大规模的数据集，之后通过和 dependabot 的结合帮助开源软件的维护人快速的修复漏洞。

今天要介绍的开源项目 advisory-database（开源漏洞建议数据库），来自 GitHub 公司的开源项目，希望更进一步的帮助开源软件的漏洞修复。

![image-20220227205333758](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220227205333758.png)

advisory-database 开源有三个目标：将过往 GitHub 公司内部积累的经验开放；赋能社区中各领域有经验的开发者建设漏洞建议社区；采用机器可读的漏洞数据库组织形式，方便其他软件或者公司集成。

除此之外，GitHub 还专门定制了展示页面，方便大家浏览和反馈漏洞的修复建议。

![image-20220227205807903](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220227205807903.png)

网站地址：https://github.com/advisories

如果你的公司也在关注开源软件的安全问题，不妨和 GitHub 一起共同建设。更多项目详情请查看如下链接。

开源项目地址：https://github.com/github/advisory-database
