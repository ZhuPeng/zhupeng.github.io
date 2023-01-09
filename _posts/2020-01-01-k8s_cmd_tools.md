---
layout: post
title: Kubernetes 命令行工具系列一
tags: Go相关
---

如今容器已经无处不在，而 Kubernetes 作为容器的调度引擎，已经被业界公认为标准，而围绕 Kubernetes 开源社区有着众多的小工具来方便我们更好的管理和使用 k8s 集群。



* top for k8s

就像 Linux 的 top 命令一样，可以方便的查看 k8s 集群内容器的运行时情况。

![](https://user-images.githubusercontent.com/6745370/57700251-8891ba80-7694-11e9-8074-af95782479e1.gif)

> 项目地址：<https://github.com/ynqa/ktop>



* kube-hunter

Hunter，就如工具的名字一样，作用是发现 k8s 集群的安全漏洞。

> 项目地址：<https://github.com/aquasecurity/kube-hunter>



* Kubernetes Operator Pythonic Framework

Operator 是 k8s 的第三方资源扩展的概念，平时我们的运维操作都是对一些资源进行对应的管控，例如增加实例数、备份数据等，Operator 就是基于 k8s 的基础将这些操作进行固化，且可以方便的使用声明式的方式管理。k8s 是使用 Go 编写的，该 Python 框架基于 k8s kapi 只需要很少的代码就能实现预期目标。

> 项目地址：<https://github.com/zalando-incubator/kopf>



* 命令行提示符

如果你是一个 k8s 的集群管理员，需要频繁的切换多个集群或者 namespace，拥有可视化的命令行提示符将会提高你的效率，同时减少出错的概率。

![](<https://raw.githubusercontent.com/jonmosco/kube-ps1/master/img/screenshot2.png>)

![](<https://raw.githubusercontent.com/jonmosco/kube-ps1/master/img/screenshot-sol-light.png>)

![](<https://raw.githubusercontent.com/jonmosco/kube-ps1/master/img/screenshot-img.png>)

![](<https://raw.githubusercontent.com/jonmosco/kube-ps1/master/img/kube-ps1.gif>)

> 项目地址：<https://github.com/jonmosco/kube-ps1>

