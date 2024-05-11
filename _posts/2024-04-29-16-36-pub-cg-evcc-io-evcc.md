---
layout: post
title: 一个电动车充电治理与家庭能源管理系统
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在全球范围内，电动汽车（EV）的快速增长与普及，为家庭充电和能源管理带来了前所未有的挑战和需求。用户经常面对的问题包括但不限于：如何有效管理电动车的充电以最大化利用家庭内部的太阳能电力、如何在电网负荷较低时优先充电以减少能源成本、同时如何确保充电过程的安全性和效率等。针对这些日益复杂的需求，一个能够综合解决上述问题的系统应运而生。

今天要给大家推荐一个 GitHub 开源项目 evcc-io/evcc，该项目在 GitHub 有超过 2.6k Star，一个电动车充电治理与家庭能源管理系统。


![](https://raw.githubusercontent.com/evcc-io/evcc/master/docs/logo.png)


###### 项目介绍

[evcc](https://github.com/evcc-io/evcc) 是一个可扩展的电动汽车（EV）充电控制器和家庭能源管理系统。该项目以其简洁清晰的用户界面，广泛支持的充电器品牌和型号，以及整合各类电表（包括电网、太阳能、电池和充电器的电表），电动汽车（包括状态监测、远程充电、电池和预调节状态）等特点，在 [PV magazine](https://www.pv-magazine.de/2021/01/15/selbst-ist-der-groeoenlandhof-wallbox-ladesteuerung-selbst-gebaut/) 上受到了特别报道。

![](https://raw.githubusercontent.com/evcc-io/evcc/master/docs/screenshot.png)

除此之外，evcc 还提供了丰富的插件系统、状态通知、日志记录、精细的充电功率控制以及与家庭自动化系统集成的 API。

![](https://hosted.weblate.org/widgets/evcc/-/evcc/multi-auto.svg)

###### 如何使用

要开始使用 evcc，首先需要确保您的系统中安装了 [Go][1] 1.22 和 [Node][2] 18。接下来，通过以下命令构建并运行 Go 后端，用户界面将在 http://127.0.0.1:7070/ 可用：

```sh
make install-ui
make ui
make install
make
./evcc
```
此外，项目还支持跨平台编译和前端开发模式。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240504223118181.png)

###### 项目推介

evcc 项目从小型家庭用户到大型组织，都在使用 evcc 来优化他们的电动车充电和能源管理需求。凭借其强大的功能和灵活的扩展性，无论您是对电动汽车充电有基础需求的用户，还是需要高级家庭能源管理功能的高端用户，evcc 都能提供满足您需求的解决方案。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240504223246193.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=evcc-io/evcc&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/evcc-io/evcc 

开源项目作者：evcc-io

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=evcc-io/evcc)

关注我们，一起探索有意思的开源项目。

