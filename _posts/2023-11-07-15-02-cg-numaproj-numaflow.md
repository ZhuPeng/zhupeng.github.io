---
layout: post
title: GitHub 开源项目 numaproj/numaflow 介绍，Kubernetes-native platform to run massively parallel data/streaming jobs
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 numaproj/numaflow，该项目在 GitHub 有差不多 1000 Star，用一句话介绍该项目就是：“Kubernetes-native platform to run massively parallel data/streaming jobs”。


![Numaflow Demo](https://img.youtube.com/vi/hJS714arX6Q/0.jpg)



# 背景介绍

在处理大规模并行数据/流处理作业时，我们常常面临着一些挑战。首先，要将数据处理分布到多个节点上，需要创建复杂的作业调度和管理机制。其次，在数据处理过程中，我们需要确保数据的完整性和准确性。此外，还需要对作业执行进行监视和调优，以保证高效和稳定的运行。针对这些问题，我们推荐使用 GitHub 开源项目 [Numaflow](https://github.com/numaproj/numaflow)。

# 项目介绍

Numaflow 是一个基于 Kubernetes 的平台，用于运行大规模并行的数据/流处理作业。使用 Numaflow，您可以将作业的各个组件以顶点的形式定义为 Kubernetes 自定义资源。每个作业由一个或多个源顶点、数据处理顶点和汇聚顶点组成。Numaflow 的设计采用 Kubernetes-native 理念，因此如果您熟悉 Kubernetes，就已经了解了如何使用 Numaflow。

Numaflow 还提供了一些核心功能，包括使用您喜欢的编程语言、保证输入数据的 Exactly-Once 语义、自动扩缩容以及具备后压控制能力等。此外，Numaflow 还提供了开发人员友好的用户界面，帮助您更便捷地管理和监视作业的执行状态。

# 如何使用

想要使用 Numaflow，您只需按照项目的[快速入门指南](https://github.com/numaproj/numaflow/blob/main/docs/quick-start.md)进行安装和配置。在安装完成后，您可以根据[示例](https://github.com/numaproj/numaflow/tree/main/examples)来创建自己的作业，也可以参考项目的[开发文档](https://github.com/numaproj/numaflow/blob/main/docs/development/development.md)来了解更多详细信息。如果您遇到任何问题或想要为项目做出贡献，可以查看[贡献指南](https://github.com/numaproj/numaproj/blob/main/CONTRIBUTING.md)。

以下是一个使用 Python 编写的 Numaflow 作业的代码示例：

```
from numaflow import NumaflowJob, Vertex

source_vertex = Vertex(name="source", ...)
processing_vertex = Vertex(name="processing", ...)
sink_vertex = Vertex(name="sink", ...)

with NumaflowJob(name="my-job") as job:
    job.add_vertex(source_vertex)
    job.add_vertex(processing_vertex)
    job.add_vertex(sink_vertex)

job.deploy()
```

通过以上代码示例，您可以轻松地创建一个包含源、数据处理和汇聚的 Numaflow 作业，并将其部署到 Kubernetes 集群中。

# 项目推介

作为一个开发活跃的开源项目，Numaflow 在解决大规模并行数据/流处理需求方面具有很高的实用性和可靠性。无论是实时数据分析应用、事件驱动应用、流式应用还是基于流处理的工作流，Numaflow 都能为您提供强大的支持。

Numaflow 的核心设计理念与 Kubernetes 兼容，并且支持多种编程语言。此外，Numaflow 还获得了[Core Infrastructure Initiative Best Practices](https://bestpractices.coreinfrastructure.org/projects/6078)的认可，可见其在安全性和可靠性方面的优秀表现。

很多知名用户和公司已经在使用 Numaflow，证明了其在实际应用环境中的可靠性和稳定性。此外，Numaflow 也受到了业内知名人士的推荐和好评。

因此，我们推荐关注并使用 Numaflow，以更高效和简


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=numaproj/numaflow&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/numaproj/numaflow 

开源项目作者：numaproj

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=numaproj/numaflow)

关注我们，一起探索有意思的开源项目。

