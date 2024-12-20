---
layout: post
title: GitHub 开源项目 XiaoMi/ha_xiaomi_home 介绍，Xiaomi Home Integration for Home Assistant
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 XiaoMi/ha_xiaomi_home，该项目在 GitHub 有超过 12.7k Star。

![](https://stats.deeptrain.net/repo/XiaoMi/ha_xiaomi_home/?theme=light)

一句话介绍该项目：Xiaomi Home Integration for Home Assistant




![](https://raw.githubusercontent.com/XiaoMi/ha_xiaomi_home/master/./doc/images/cloud_control.jpg)

![](https://raw.githubusercontent.com/XiaoMi/ha_xiaomi_home/master/./doc/images/local_control.jpg)


###### 项目介绍

### 背景介绍

随着智能家居设备的普及，我们的生活正在变得更智能、更便捷。小米作为智能家居设备的主要提供商之一，拥有广泛的产品线，覆盖了从灯泡、插座到空气净化器等众多家用电器。然而，对于想要实现更个性化智能家居自动化的用户来说，仅依赖于小米自家的米家应用显然是不够的。这是因为，用户可能还想要将小米智能家居设备和其他品牌的智能家居设备进行集成，或者实现更加复杂的自动化场景。此时，一个支持多品牌设备且开源的智能家居管理平台——Home Assistant，就成了用户的理想选择。然而，如何将小米的智能家居设备无缝集成到 Home Assistant 中，成了一个技术挑战。

### 

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-80c210eacfea37dd15517e24990b60b2.png)

项目介绍

Xiaomi Home Integration for Home Assistant 是一个由小米官方支持的集成组件，解决了小米 IoT 智能设备与 Home Assistant 无缝集成的问题。该项目使得用户可以在 Home Assistant 平台上使用小米 IoT 智能家居设备，实现更复杂、更个性化的智能家居自动化场景。主要功能包括登录小米账户、添加小米智能家居设备至 Home Assistant、支持多用户登录和设备管理等。此项目的推出极大地扩展了 Home Assistant 的设备支持范围，提高了小米智能家居产品的可玩性和自动化程度。

### 如何使用

安装此集成的方法主要有三种：

1. **通过 Git 克隆**：这是推荐的安装方法，因为它方便在更新 `xiaomi_home` 至某一特定版本时切换至相应的标签（Tag）。

    ```bash
    cd config
    git clone https://github.com/XiaoMi/ha_xiaomi_home.git
    cd ha_xiaomi_home
    ./install.sh /config
    ```

2. **通过 HACS**：虽然 Xiaomi Home 尚未作为默认集成添加到 HACS 商店中，但通过添加自定义仓库的方式可以进行安装。

3. **手动安装**：通过 Samba 或 FTPS 手动下载并复制 `custom_components/xiaomi_home` 文件夹至 Home Assistant 的 `config/custom_components` 文件夹下。

使用后，需要登录小米账户并根据指南添加 MIoT 设备，即可在 Home Assistant 中控制和管理小米智能家居设备。

### 项目推介

Xiaomi Home Integration for Home Assistant 为小米及 Home Assistant 用户带来了极大的便利，它不但得到了小米的官方支持，而且还可以实现多用户设备的集中管理，非常适合拥有多个小米智能设备的家庭使用。当前，它已经支持了大部分小米智能家居产品的类别，尽管还有少数类别的设备暂不支持，但考虑到其持续更新与官方背书的事实，这个项目无疑是连接小米智能设备与 Home Assistant 的最佳桥梁。此外，随着智能家居市场的快速增长，能够将不同品牌的智能设备集成到同一个平台上管理将成为趋势，而 Xiaomi Home Integration 无疑在这方面起到了先锋作用。预计随着项目的发展和小米智能家居设备种类的

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=XiaoMi/ha_xiaomi_home&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/XiaoMi/ha_xiaomi_home 

开源项目作者：XiaoMi

开源协议：Other

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=XiaoMi/ha_xiaomi_home)

关注我们，一起探索有意思的开源项目。

