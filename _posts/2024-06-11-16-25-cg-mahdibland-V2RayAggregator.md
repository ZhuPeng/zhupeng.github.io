---
layout: post
title: GitHub 开源项目 mahdibland/V2RayAggregator 介绍，Collect Lots of Shadowsocks, ShadowsocksR, Trojan, Vmess from Public Sources & Filter Best Nodes By Speed
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 mahdibland/V2RayAggregator，该项目在 GitHub 有超过 2.3k Star。

![](https://stats.deeptrain.net/repo/mahdibland/V2RayAggregator/?theme=light)

一句话介绍该项目：Collect Lots of Shadowsocks, ShadowsocksR, Trojan, Vmess from Public Sources & Filter Best Nodes By Speed




![](https://i.ibb.co/g32RmJy/netlify.png)

![](https://i.ibb.co/g32RmJy/netlify.png)


###### 项目介绍

### 背景介绍
在网络自由度日益成为全球关注焦点的今天，通过安全、可靠的网络连接访问全球信息成为许多用户的迫切需求。Shadowsocks、ShadowsocksR、Trojan 和 Vmess 等代理技术，作为网络隐私保护和反审查的重要工具，其重要性不言而喻。然而，寻找稳定且速度快的免费代理节点成为用户的一大挑战。许多公开的代理源质量参差不齐，且经常面临失效的问题，这大大影响了用户体验。

### 

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-f53c3c8fe970d6deceff582f62852d5e.png)

项目介绍
**V2RayAggregator** 是一个开源项目，目标是从公开来源收集大量的 Shadowsocks、ShadowsocksR、Trojan、Vmess 代理节点，并通过速度测试筛选出最佳节点。该项目利用 `GitHub Actions` 自动化实现测试和筛选过程，确保提供的节点既稳定又快速。项目特色包括：

- 来源广泛：集成多个免费代理源，确保节点的多样性。
- 去重机制：自动去除重复的节点，保证节点列表的精简。
- 格式兼容：提供包括 YAML、clash、v2ray、base64 等多种格式，一键导入到各类客户端。
- 速度排序：通过速度测试，确保用户可以获得最优质的代理服务。

此外，项目还提供了日志可视化服务，方便用户查看和选择节点。

### 如何使用
用户可以根据自己的需求选择两种节点方案：公开节点和免费机场。公开节点更新频率为每 12 小时一次，适用于对稳定性需求较高的用户；免费机场节点每 2 小时更新一次，更适合追求速度和最新资源的用户。

#### 导入节点：
- 导入操作简单，只需选择对应格式的订阅链接，即可一键导入到支持 ss、ssr、vmess、trojan 的客户端。

#### 节点链接示例（200 个筛选节点）：
- **公开节点（Group 1）**：
  - Base64: [链接](https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/Eternity)
  - Mixed: [链接](https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/Eternity.txt)
  - Clash: [链接](https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/Eternity.yml)

- **免费机场（Group 2）**：
  - Base64: [链接](https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/EternityAir)
  - Mixed: [链接](https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/EternityAir.txt)
  - Clash: [链接](https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/EternityAir.yml)

### 项目推介
**V2RayAggregator** 项目自推出以来，已经成为许多追求网络自由和隐私保护用户的首选工具。项目的开源性质和活跃的开发维护状态，保证了其源源不断的更新和改进。虽然项目目前还在持续优化中，但凭借其提供的高速、稳定节点，已经受到众多用户的广泛好评和推荐。无论您是寻找稳定的网络代理服务，还是对开放源码技术感兴趣，**V2RayAggregator** 都值得您的关注和试用。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=mahdibland/V2RayAggregator&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/mahdibland/V2RayAggregator 

开源项目作者：mahdibland

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=mahdibland/V2RayAggregator)

关注我们，一起探索有意思的开源项目。

