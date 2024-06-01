---
layout: post
title: 教你从零开始学习 Jenkins 的开源项目
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在现代化的软件开发过程中，我们常常需要通过持续集成（CI）和持续部署（CD）流程，来确保我们的应用程序可以快速且自动化地从开发阶段转变到运行阶段。这其中，如何迅速有效地部署 Jenkins，是一个常见的挑战。同时，如何配置 Docker 作为从节点（Slave），如何在 GitOps 方式中使用 Argo CD 将应用程序部署到 k8s，都是我们日常工作中需要处理的问题。

今天要给大家推荐一个 GitHub 开源项目 Jenkins-Zero-To-Hero，该项目在 GitHub 有超过 5.1k Star，一句话介绍该项目：Install Jenkins, configure Docker as slave, set up cicd, deploy applications to k8s using Argo CD in GitOps way.

![](https://user-images.githubusercontent.com/43399466/216040281-6c8b89c3-8c22-4620-ad1c-8edd78eb31ae.png)

###### 项目介绍
项目 Jenkins-Zero-To-Hero 是一个专注于教你从零开始学习 Jenkins 的开源项目。它不仅可以帮助你安装和配置 Jenkins，还可以指导你配置 Docker 作为 Jenkins 的从节点（Slave），设置 CI/CD，以及使用 Argo CD 在 GitOps 方式下部署应用程序到 Kubernetes。

![](https://user-images.githubusercontent.com/43399466/215974891-196abfe9-ace0-407b-abd2-adcffe218e3f.png)

除此之外，它还提供了详细的 Jenkins 插件安装教程，教你如何在 Jenkins 中安装 "Docker Pipeline" 插件；如何为 Jenkins 和 Ubuntu 用户授予对 Docker 守护进程的操作权限，以及如何在 AWS EC2 实例上安装和配置 Jenkins。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240523000248377.png)

![](https://user-images.githubusercontent.com/43399466/215959008-3ebca431-1f14-4d81-9f12-6bb232bfbee3.png)

###### 如何使用

项目 README 文档中已经详细描述了如何在 AWS EC2 实例上安装和配置 Jenkins，具体步骤包括：

1、安装 Java

2、安装 Jenkins

3、配置 Jenkins 的入站流量规则以使其可以在外部访问

4、登陆到 Jenkins，并使用 Admin 密码

5、安装 Jenkins 提议的插件

6、安装 Docker，配置 Docker 作为 Jenkins 的从节点

7、为 Jenkins 和 Ubuntu 用户授予对 Docker 守护进程的操作权限

项目中提供了详细的命令行代码，你可以直接复制粘贴到你的命令行窗口中进行操作。

![](https://user-images.githubusercontent.com/43399466/215973898-7c366525-15db-4876-bd71-49522ecb267d.png)

###### 项目推介
项目还比较年轻，但是它的核心价值——解决软件开发人员在实际工作中遇到的一些常见问题，已经非常明显。这个项目是一个不错的学习资源，它可以帮助你从零开始，一步步成为 Jenkins 的专家。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=iam-veeramalla/Jenkins-Zero-To-Hero&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/iam-veeramalla/Jenkins-Zero-To-Hero 

开源项目作者：iam-veeramalla

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=iam-veeramalla/Jenkins-Zero-To-Hero)

关注我们，一起探索有意思的开源项目。

