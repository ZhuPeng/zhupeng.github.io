---
layout: post
title: 一款为微服务架构而设计的监控和故障排查工具
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 coroot/coroot，该项目在 GitHub 有超过 2.3k Star，用一句话介绍该项目就是：“A monitoring and troubleshooting tool for microservice architectures.”，一款为微服务架构而设计的监控和故障排查工具。

![](https://coroot.com/static/logo_u.png)

coroot 是一个由 Go 语言编写的开源项目，它提供了一种无需任何改动即可对微服务架构进行监控和故障排查的方法。通过借助 eBPF 实现了对服务间流量调用的监控，从而可以绘制出服务间的调用关系。

>eBPF 是一项革命性的技术，可以在 Linux 内核中运行沙盒程序，而无需更改内核源代码或加载内核模块。通过使 Linux 内核可编程，基础架构软件可以利用现有的层，从而使它们更加智能和功能丰富，而无需继续为系统增加额外的复杂性层。
>
>eBPF 导致了网络，安全性，应用程序配置/跟踪和性能故障排除等领域的新一代工具的开发，这些工具不再依赖现有的内核功能，而是在不影响执行效率或安全性的情况下主动重新编程运行时行为。

![](https://user-images.githubusercontent.com/194465/205605750-cb8da6f1-7388-4539-867c-2216f714cf66.gif)

目前主流的 7 层协议都是支持的，具体如下：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230325212459477.png)

同时 coroot 默认支持对调用的 SLO 进行追踪，同时也可以自己进行自定义，通过 Slack 等 IM 工具可以及时发送 SLO 不达标的告警。

![](https://user-images.githubusercontent.com/194465/205626385-076f2fcd-fd26-44e3-99ba-6c16ab738bb2.png)

除此之外，coroot 还支持很多的功能，比如日志分析、云拓扑自动感知、数据库可观测性、与已有监控系统的集成和内建的 Prometheus 缓存等，这里就不一一介绍了。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=coroot/coroot&type=Timeline)

### 如何安装使用

安装 coroot 项目可以通过 Helm 一站式安装，以下是安装命令：

```bash
helm repo add coroot https://coroot.github.io/helm-charts
helm repo update

helm install --namespace coroot --create-namespace coroot coroot/coroot
kubectl port-forward -n coroot service/coroot 8080:8080
```

访问 localhost:8080 即可，安装好后需要进行项目的创建，依次按提示操作即可。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230325213519795.png)


更多项目详情请查看如下链接。

开源项目地址：https://github.com/coroot/coroot 

开源项目作者：coroot

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=coroot/coroot)



关注我们，一起探索有意思的开源项目。
