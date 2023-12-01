---
layout: post
title: GitHub 开源项目 blakeblackshear/frigate 介绍，NVR with realtime local object detection for IP cameras
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 blakeblackshear/frigate，该项目在 GitHub 有超过 11.9k Star，用一句话介绍该项目就是：“NVR with realtime local object detection for IP cameras”。


![Events](https://raw.githubusercontent.com/blakeblackshear/frigate/master/docs/static/img/events-ui.png)
![](https://raw.githubusercontent.com/blakeblackshear/frigate/master/docs/static/img/frigate.png)
![](https://raw.githubusercontent.com/blakeblackshear/frigate/master/docs/static/img/media_browser.png)
![](https://raw.githubusercontent.com/blakeblackshear/frigate/master/docs/static/img/notification.png)
![](https://raw.githubusercontent.com/blakeblackshear/frigate/master/docs/static/img/home-ui.png)
![](https://raw.githubusercontent.com/blakeblackshear/frigate/master/docs/static/img/camera-ui.png)



背景介绍：
在智能家居领域，我们常常需要对 IP 监控摄像头的实时视频流进行目标检测。传统的解决方案往往会消耗大量的计算资源和易引发网络延迟问题，而且无法实现本地化的数据处理，给数据的安全性带来隐患。因此，我们需要一款不仅高效、快捷，而且能本地化处理数据的 NVR （网络视频录像机）项目来解决这个问题。

项目介绍：
Frigate 是一款为 [Home Assistant](https://www.home-assistant.io) 设计的本地化、完善的 NVR，配备有人工智能目标检测功能。它利用了 OpenCV 和 TensorFlow 来执行 IP 摄像机的实时本地目标检测。如果用户愿意，可以使用 [Google Coral Accelerator](https://coral.ai/products/) ，以获得较高的处理能力，并极大地减少处理负载。

Frigate 有以下几个主要优点和功能：
- 通过 [custom component](https://github.com/blakeblackshear/frigate-hass-integration) 与 Home Assistant 紧密集成；
- 通过只在必要的时候和地点寻找目标，实现资源使用最小化和性能最大化；
- 使用并行处理来处理大量的实时数据，强调实时性，而不是处理每一帧画面；
- 利用低开销的运动检测来决定在哪里运行目标检测；
- TensorFlow 运行在不同的进程中以实现最大 FPS；
- 利用 MQTT 进行通信，方便与其他系统集成；
- 根据检测到的对象对视频进行记录，设置保留时间；
- 24/7 录制，通过 RTSP 重新流式传输以减少对您的摄像头的连接数量；
- 支持 WebRTC 和 MSE，实现低延时直播视图。

如何使用：
可以通过查看 https://docs.frigate.video 中的文档来详细了解如何安装和使用 Frigate。

项目推介：
Frigate 是由 GitHub 用户 blakeblackshear 开发并维护的项目，开发活跃度极高，作者具有丰富的编程和项目经验，细节处理十分专业。由于 Frigate 的优秀性能和设计，已经吸引了众多的用户和爱好者的关注和使用，包括许多知名的智能家居用户和公司。为了支持项目的发展，你也可以通过 [Github Sponsors](https://github.com/sponsors/blakeblackshear) 对项目进行捐助。选择 Frigate，让您的智能家居系统拥有更快、更稳定的目标检测能力吧。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=blakeblackshear/frigate&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/blakeblackshear/frigate 

开源项目作者：blakeblackshear

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=blakeblackshear/frigate)

关注我们，一起探索有意思的开源项目。

