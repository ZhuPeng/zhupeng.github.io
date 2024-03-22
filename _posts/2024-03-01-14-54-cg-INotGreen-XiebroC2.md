---
layout: post
title: GitHub 开源项目 INotGreen/XiebroC2 介绍，一款支持多人协作的渗透测试图形化框架、支持lua插件扩展、域前置/CDN上线、自定义多个模块、自定义shellcode、文件管理、进程管理、内存加载、反向代理等功能
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 INotGreen/XiebroC2，该项目在 GitHub 有差不多 1000 Star，用一句话介绍该项目就是：“一款支持多人协作的渗透测试图形化框架、支持lua插件扩展、域前置/CDN上线、自定义多个模块、自定义shellcode、文件管理、进程管理、内存加载、反向代理等功能”。



![](https://raw.githubusercontent.com/INotGreen/XiebroC2/master/Image\Image.jpg)



背景介绍：
在面临日益复杂的网络安全挑战时，多人协作成为了实现有效渗透测试的关键。同时，对于更为复杂的系统如 CDN 和自定义模块的渗透测试也变得越来越重要。然而，如何在这样的大规模，多平台的环境中有效地组织和执行渗透测试是一项巨大的挑战，这就是 XiebroC2 开源项目希望解决的问题。

项目介绍：
XiebroC2 是一款支持多人协作的渗透测试图形化框架，它支持 Lua 插件扩展、域前置/CDN 上线、自定义多个模块、自定义 shellcode、文件管理、进程管理、内存加载、反向代理等功能。该项目的控制端客户端由 Golang 编写，兼容 Windows、Linux 和 MacOS。团队服务器则由.net 8.0 编写，设计为内存占用低，无需安装任何依赖，几乎可以兼容全平台系统。其中，控制端在设计时考虑到了用户交互，支持了反弹 shell、文件管理、进程管理、网络流量监控、内存加载、自定义 UI 背景色等功能。

如何使用：
安装和使用 XiebroC2 很简单。通过以下链接使用 curl 截取项目文件：
```bash
curl -o XiebroC2-v3.1.7z https://github.com/INotGreen/XiebroC2/releases/download/XieBroC2-v3.1/Xiebro-v3.1.7z
```
确保控制端运行在 .Net Framework4.8 以上的环境，修改 TeamServerIP 和 TeamServerPort 为你的 VPS 的 IP 和端口，然后保存为 profile.json。运行服务器命令：
```bash
Teamserver.exe -c profile.json
```

项目推介：
XiebroC2 项目目前开发活跃，它已经被多家知名的安全公司及安全团队使用，并得到了良好的反馈。同时，该项目保持活跃更新，最新版本 3.1 已经修复了一些已知 bug，并增加了对 Websocket 通信协议的支持。作者是一位在 Github 社区中有一定影响力的开发者，项目质量和后续支持有保障。如果你正在寻找一款功能强大、简单易用的渗透测试框架，XiebroC2 无疑是一个值得推荐的选择。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=INotGreen/XiebroC2&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/INotGreen/XiebroC2 

开源项目作者：INotGreen

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=INotGreen/XiebroC2)

关注我们，一起探索有意思的开源项目。

