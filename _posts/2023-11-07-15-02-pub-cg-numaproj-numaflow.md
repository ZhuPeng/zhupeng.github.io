---
layout: post
title: Numaflow - 基于 Kubernetes 的平台，用于运行大规模并行的数据/流处理作业平台
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在处理大规模并行数据/流处理作业时，我们常常面临着一些挑战。首先，要将数据处理分布到多个节点上，需要创建复杂的作业调度和管理机制。其次，在数据处理过程中，我们需要确保数据的完整性和准确性。此外，还需要对作业执行进行监视和调优，以保证高效和稳定的运行。以上问题如果要自己去解决，有不小的开发成本。

今天要给大家推荐一个 GitHub 开源项目 numaproj/numaflow，该项目在 GitHub 有差不多 1000 Star，用一句话介绍该项目就是：“Kubernetes-native platform to run massively parallel data/streaming jobs”。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231126182555962.png)

###### 项目介绍

Numaflow 是一个基于 Kubernetes 的平台，用于运行大规模并行的数据/流处理作业。使用 Numaflow，您可以将作业的各个组件以顶点的形式定义为 Kubernetes 自定义资源（CRD）。每个作业由一个或多个源顶点、数据处理顶点和汇聚顶点组成。Numaflow 的设计采用 Kubernetes-native 理念，因此如果您熟悉 Kubernetes，就已经了解了如何使用 Numaflow。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231126182755324.png)

Numaflow 还提供了一些核心功能，包括使用您喜欢的编程语言、保证输入数据的 Exactly-Once 语义、自动扩缩容以及具备后压控制能力等。此外，Numaflow 还提供了开发人员友好的用户界面，帮助您更便捷地管理和监视作业的执行状态。

![](https://numaflow.numaproj.io/assets/numaflow-ui-advanced-pipeline.png)

###### 如何使用

想要使用 Numaflow，使用如下 kubectl 命令即可快速安装。

```bash
kubectl create ns numaflow-system
kubectl apply -n numaflow-system -f https://raw.githubusercontent.com/numaproj/numaflow/stable/config/install.yaml
kubectl apply -f https://raw.githubusercontent.com/numaproj/numaflow/stable/examples/0-isbsvc-jetstream.yaml
```

安装好后即可开始使用，首先创建对应的数据处理流水线，以下为官方提供的示例：

```
kubectl apply -f https://raw.githubusercontent.com/numaproj/numaflow/stable/examples/1-simple-pipeline.yaml

kubectl get pipeline # or "pl" as a short name

```

对应的 Pipeline 配置如下：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231126183409295.png)

对应的页面效果如下：

![](https://github.com/numaproj/numaflow/raw/main/docs/assets/numaflow-ui-simple-pipeline.png)

更多其他更复杂流水线设置可以参考项目官方介绍。

###### 项目推介

Numaflow 在解决大规模并行数据/流处理需求方面具有很高的实用性和可靠性。无论是实时数据分析应用、事件驱动应用、流式应用还是基于流处理的工作流，Numaflow 都能为您提供强大的支持。Numaflow 的核心设计理念与 Kubernetes 兼容，并且支持多种编程语言。此外，Numaflow 还获得了 [Core Infrastructure Initiative Best Practices ](https://bestpractices.coreinfrastructure.org/projects/6078)的认可，可见其在安全性和可靠性方面的优秀表现。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231126183742084.png)


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=numaproj/numaflow&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/numaproj/numaflow 

开源项目作者：numaproj

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=numaproj/numaflow)

关注我们，一起探索有意思的开源项目。

