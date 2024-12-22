---
layout: post
title: 可独立部署的健身饮食管理应用
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在现代社会，人们越来越注重健康与健身，但与此同时，管理个人的健身计划、饮食和体重变化往往充满挑战。对许多人而言，找到一个既能够全面覆盖健身管理各个方面，又能提供个性化设置的工具是非常困难的。此外，对于健身房的经营者来说，有效地管理会员、跟踪他们的进度同样也是一项挑战。大多数现有的解决方案要么功能不足以满足需求，要么是封闭源代码且价格昂贵的应用程序，限制了用户的选择和灵活性。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-6ab360547b649ca7d34b8ae51383e341.png)

今天要给大家推荐一个 GitHub 开源项目 wger，该项目在 GitHub 有超过 3.3k Star。

![](https://stats.deeptrain.net/repo/wger-project/wger/?theme=light)

一句话介绍该项目：Self hosted FLOSS fitness/workout, nutrition and weight tracker

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241219215530796.png)


###### 项目介绍

wger 是一个免费的开源网络应用程序，致力于帮助用户管理个人健身、体重和饮食计划，同时也可以作为一个简易的健身房管理工具。wger 提供了一个 REST API，方便与其他项目和工具的集成。它的独特之处在于，所有的功能都是基于社区的反馈和需求持续开发的，确保了其实用性和有效性。

![](https://raw.githubusercontent.com/wger-project/wger/master/wger/software/static/images/screens-3.png)

该项目不仅包括了工作计划和饮食计划的创建和管理，还允许用户跟踪体重变化，并包含一个数据库来存储和查找训练动作。此外，它还是一款开源项目，这意味着用户可以根据自己的需求，自由地定制和扩展应用。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241219215638844.png)

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241219215647936.png)

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241219215659035.png)

###### 如何使用

wger 可以通过 Docker 来安装，对于想要自己托管实例的用户，可以参考提供的 docker compose 文件。如果只是想尝试一下，可以使用以下命令运行一个演示实例：

```shell script
docker run -ti --name wger.demo --publish 8000:80 wger/demo
```

打开浏览器并以 **admin** 用户登录，密码为 adminadmin

###### 项目推介

wger 的开源特性吸引了一大批开发者和健身爱好者的共同参与，不断提升和优化。wger 不仅适用于个人用户，也能为健身房运营者提供强大的管理工具。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241219215901667.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=wger-project/wger&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/wger-project/wger 

开源项目作者：wger-project

开源协议：GNU Affero General Public License v3.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=wger-project/wger)

关注我们，一起探索有意思的开源项目。

