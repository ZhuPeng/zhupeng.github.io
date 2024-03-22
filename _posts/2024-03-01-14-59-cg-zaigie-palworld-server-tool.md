---
layout: post
title: GitHub 开源项目 zaigie/palworld-server-tool 介绍，[中文|English|日本語]基于.sav存档解析和RCON优雅地用可视化界面管理幻兽帕鲁专用服务器。/ Through parse .sav and RCON, visual interface management PalWorld dedicated server.
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 zaigie/palworld-server-tool，该项目在 GitHub 有差不多 1000 Star，用一句话介绍该项目就是：“[中文|English|日本語]基于.sav存档解析和RCON优雅地用可视化界面管理幻兽帕鲁专用服务器。/ Through parse .sav and RCON, visual interface management PalWorld dedicated server.”。



![PC](https://raw.githubusercontent.com/zaigie/palworld-server-tool/master/./docs/img/pst-zh-1.png)
![加QQ群](https://raw.githubusercontent.com/zaigie/palworld-server-tool/master/./docs/img/add_group.jpg)
![](https://raw.githubusercontent.com/zaigie/palworld-server-tool/master/./docs/img/pst-zh-2.png)
![](https://raw.githubusercontent.com/zaigie/palworld-server-tool/master/./docs/img/pst-zh-3.png)
![](https://raw.githubusercontent.com/zaigie/palworld-server-tool/master/./docs/img/pst-zh-4.png)
![RCON](https://raw.githubusercontent.com/zaigie/palworld-server-tool/master/./docs/img/rcon.png)
![](https://raw.githubusercontent.com/labring-actions/templates/main/Deploy-on-Sealos.svg)
![](https://raw.githubusercontent.com/labring-actions/templates/main/Deploy-on-Sealos.svg)
![](https://pub.idqqimg.com/wpa/images/group.png)
![](https://raw.githubusercontent.com/zaigie/palworld-server-tool/master/./docs/img/pst-zh-m-1.png)



背景介绍：对于游戏服务器的管理，我们面临着繁琐低效的操作问题，例如无法实时获取玩家数据、无法快速对服务器进行一些如广播、封禁玩家等操作，甚至连服务器数据的备份都需要手动执行。同时，对于非技术背景的服务器管理员来说，这些问题更加困扰。于是，项目 "幻兽帕鲁服务器管理工具" 应运而生。

项目介绍： "幻兽帕鲁服务器管理工具" 是一个开源工具，它通过解析 '.sav' 存档文件和使用 RCON，给幻兽帕鲁专用服务器带来了一个可视化的管理界面。主要功能包括：

- 1、根据 'Level.sav' 存档文件解析显示完整的玩家数据、玩家幻兽数据、公会数据以及玩家背包物品数据。
- 2、利用 RCON 功能实现获取服务器信息、获得在线玩家列表、踢出/封禁玩家、游戏内广播以及平滑关闭服务器并广播消息等。
- 3、提供白名单管理和自定义 RCON 命令并执行等额外功能。

该工具使用 bbolt 单文件存储，通过定时任务获取 RCON 和 Level.sav 文件的数据并保存，以此提供一个简洁的可视化界面和 REST 接口，方便大家的管理与开发。

如何使用：安装使用该工具需要在游戏服务器上开启 RCON 功能，并对 'config.yaml' 文件进行相应的配置，包括 RCON 的地址和端口、RCON 的 AdminPassword、 RCON 通信超时时间和定时向 RCON 服务获取玩家在线情况的间隔等。然后，配置存档文件解析相关配置，包括存档文件路径、存档解析工具路径以及定时从存档获取数据的间隔等。最后，就可以运行 'pst' 来启动服务器管理工具，访问 http://{服务器 IP}:8080 就可以看到可视化界面。

项目推介：该项目是开发活跃的，主要由前端和后端工程师开发维护。虽然国际化的工作耗费了作者很多时间和精力，但工具已经支持 简体中文、英文、日文等多语言环境，值得大家去尝试使用。同时，作者还为工具提供了详细的使用文档，及时解决了用户在使用过程中可能遇到的问题。此外，该项目的管理员，zaigie，是一位优秀的计算机工程师，熟悉开源项目的运作，还为该项目开设了一个专门的讨论区，引导开发者和用户互动交流，提出改进建议，也热忱欢迎其他工程师为此项目提交 PR。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=zaigie/palworld-server-tool&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/zaigie/palworld-server-tool 

开源项目作者：zaigie

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=zaigie/palworld-server-tool)

关注我们，一起探索有意思的开源项目。

