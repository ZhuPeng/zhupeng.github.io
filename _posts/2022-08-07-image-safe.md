---
layout: post
title: 镜像部署越来越广泛使用，但镜像安全你了解吗？
tags: 安全
---

大家好。

现在越来越多的公司的服务部署都使用镜像部署了，使用镜像部署有很多的好处，比如不需要做工具的安装、服务的启动环境是干净的、弹性扩缩容也变得容易等等。但是使用镜像同样会面临安全相关的问题，你知道吗？

使用镜像进行容器部署，提倡的就是以最小化的镜像去运行服务，如非必要都不需要打包到镜像里面。这样其实也能在你的服务被其他不法侵入之后，降低被攻击的风险。

今天要推荐的一款工具集 veinmind-tools，一款容器安全开源工具集，支持检测容器镜像安全风险。veinmind-tools 以容器镜像资源为中心，针对恶意文件、敏感配置、入侵攻击等严重安全问题，在镜像 pull-build-push 阶段提供安全检测，从生产环境的容器的供应链源头解决安全风险，降低安全风险点，同时维护容器安全交流社群，建立容器安全学习交流良好氛围。

以下是项目的主要功能及亮点：

![image-20220807210310352](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220807210310352.png)

通过如下命令就可以直接开始使用：

![image-20220807210631173](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220807210631173.png)

对于要单独扫描一个镜像参考如下命令，其中可以看到扫面出来了几个比较敏感的文件，涉及 .git、config.ini 配置文件、ssh key 等，这些都可能造成更广范围的安全问题，是非常值得去修复并提高安全等级的。

![img](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_scan_image.png)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/chaitin/veinmind-tools

开源项目作者：[chaitin](https://github.com/chaitin)

关注我们，一起探索有意思的开源项目。
