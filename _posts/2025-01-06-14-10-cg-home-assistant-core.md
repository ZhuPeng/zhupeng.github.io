---
layout: post
title: GitHub 开源项目 home-assistant/core 介绍，:house_with_garden: Open source home automation that puts local control and privacy first.
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 home-assistant/core，该项目在 GitHub 有超过 75.4k Star。

![](https://stats.deeptrain.net/repo/home-assistant/core/?theme=light)

一句话介绍该项目：:house_with_garden: Open source home automation that puts local control and privacy first.





###### 项目介绍

背景介绍：
在这个智能家居设备遍地开花的时代，我们渴望构建一个中心化且自私有化的智能家居环境，确保数据隐私在本地控制。尽管智能家居设备给生活带来了便利，但同时它们各自为营的生态系统、对数据隐私的不同处理方式，以及不断增长的第三方云依赖，暴露出了一系列问题：数据存储位置不透明、设备间互联互通困难、用户对自己数据的掌控度低。因此，一款能够提供统一接口，确保数据安全且支持广泛设备的开源智能家居平台变得尤为重要。



![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-508473b8d1f2d168c39af1e2dccc565a.png)

项目介绍：
Home Assistant 是一个以 :house_with_garden: 家庭自动化为核心，将本地控制和隐私放在首位的开源项目。它支持数以千计的智能家居设备，无论是知名品牌还是小众设备，提供一个统一的配置和控制平台。核心特点包括自动化规则引擎、物联网集成、以及丰富的可视化界面。通过 Home Assistant，用户可以在一个平台上监视、控制并自动化他们所有的智能设备，而无需依赖外部云服务。该平台的设计理念围绕着模块化、易用性和扩展性，且有一个活跃的社区支持不断地进行功能更新和设备支持。

如何使用：
Home Assistant 可以在多种硬件上安装，包括 Raspberry Pi、智能家居网关、甚至是旧的PC或Mac。安装过程简单，只需几个步骤：

1. 从 https://www.home-assistant.io/getting-started/ 访问官方指南并选择合适的安装方式。
2. 根据选择的安装方式，下载相应的镜像并闪存到 SD 卡或硬盘中。
3. 插入装有 Home Assistant 的存储设备，开启设备电源开始安装。
4. 完成安装并通过浏览器访问 Home Assistant 面板，开始添加和配置你的智能设备。

代码示例（将某个设备添加到自动化规则）：
```yaml
automation:
  - alias: "Turn on lights when it gets dark"
    trigger:
      - platform: sun
        event: sunset
    action:
      - service: light.turn_on
        entity_id: light.living_room
```

项目推介：
Home Assistant 在家庭自动化领域是一颗正在崛起的明星。它由一个在业内极具影响力的开发团队维护，社区活跃，持续更新频繁，反映出了良好的项目活力。而且，由于它强调隐私和本地控制，受到了那些注重数据隐私的用户的青睐。目前，包括一些创业公司和技术爱好者在内的多种用户群体已经在使用 Home Assistant 来构建他们的智能家居系统。此外，数不尽的教程、插件和集成保证了新用户可以相对容易地入门和扩展自己的系统。随着智能家居设备的日益普及，像 Home Assistant 这样的项目无疑是构建开放、可控与私有的智能家庭生态系统的最佳选择之一。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=home-assistant/core&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/home-assistant/core 

开源项目作者：home-assistant

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=home-assistant/core)

关注我们，一起探索有意思的开源项目。

