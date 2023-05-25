---
layout: post
title: 支持快速生成干净且隔离的开发环境的提效工具
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 jetpack-io/devbox，该项目在 GitHub 有超过 4.8k Star，用一句话介绍该项目就是：“Instant, easy, and predictable development environments”，支持快速生成干净且隔离的开发环境。

devbox 是一个由 jetpack-io 开发的开源项目，它是一个用于提高开发效率的工具。通过使用 devbox，开发人员可以在本地快速构建一个完整且隔离的开发环境，并使用各种工具和技术来开发和测试应用程序。以下是具体的一个使用示例：

![](https://user-images.githubusercontent.com/279789/186491771-6b910175-18ec-4c65-92b0-ed1a91bb15ed.svg)

![](https://mmbiz.qpic.cn/mmbiz_png/zRiam9B2qkhQCRORTWf890g6pXvgweRmGVtVqHTGtuJerdG2G2Sy038pDcfgt8jvqcUGIELwgOTHzshc6bxVWFg/0?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/zRiam9B2qkhQCRORTWf890g6pXvgweRmGCM7QbYpkr4mEplXicbL2Iasqozk7v1suEibGricHSZWdD4EvUeq3ibY9uA/0?wx_fmt=png)

在本地电脑上通过 devbox 来管理依赖的工具有很多的好处，比如可以保证团队内使用统一的开发环境、使用更新的工具版本时可以不污染当前的环境、devbox 相比其他工具安装会更快速。以下是官方整理的使用 devbox 的优点：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230409201554852.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=jetpack-io/devbox&type=Timeline)

### 如何安装使用

通过如下命令即可安装 devbox

```bash
curl -fsSL https://get.jetpack.io/devbox | bash
```

安装好后依次通过如下步骤接口进行初始化并使用。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230409201724222.png)

初始化 devbox 并增加 python3 依赖工具。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230409201759425.png)

使用 devbox shell 即可进入刚才定义的环境，进入后查看 python --version 可以看到是刚才定义的版本。


devbox 使用起来还是比较简单的。更多项目详情请查看如下链接。

开源项目地址：https://github.com/jetpack-io/devbox 

开源项目作者：jetpack-io

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=jetpack-io/devbox)



关注我们，一起探索有意思的开源项目。
