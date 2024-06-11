---
layout: post
title: GitHub 开源项目 google/gvisor 介绍，Application Kernel for Containers
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 google/gvisor，该项目在 GitHub 有超过 15.2k Star。

![](https://stats.deeptrain.net/repo/google/gvisor/?theme=light)

一句话介绍该项目：Application Kernel for Containers




![gVisor](https://raw.githubusercontent.com/google/gvisor/master/g3doc/logo.png)


###### 项目介绍

背景介绍：
在当前技术架构中，容器技术已成为开发、打包和部署应用程序的革命性方法。然而，尽管容器技术带来了效率和性能上的巨大提升，但当我们利用它们运行不受信任或潜在恶意的代码时，其安全隐患不容忽视。传统容器直接利用宿主机的内核，一旦出现安全漏洞，整个系统的安全性便会遭受威胁。因此，在没有额外隔离措施的条件下，将容器作为安全沙箱来使用是不够理智的选择。



![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-71f6072d6f5eec896a31ff71b411d07b.png)

项目介绍：
**gVisor** 是一种应用程序内核，用 Go 语言编写，实现了 Linux 系统大部分的表面功能。它包含一个名为 `runsc` 的 [Open Container Initiative (OCI)][oci] 运行时，为应用程序和宿主机内核之间提供隔离边界。`runsc` 运行时能够与 Docker 和 Kubernetes 集成，简化了沙盒化容器的运行过程。与大多数内核不同，gVisor 不假定或要求一组固定的物理资源；相反，它利用现有宿主机内核功能并作为普通进程运行。换句话说，gVisor 是通过 Linux 来实现 Linux 的。

如何使用：
首先确保系统中已安装 Linux 4.14.77+ 和 Docker 版本 17.09.0 或更高版本。gVisor 的安装步骤如下：

1. 构建 `runsc` 二进制文件：
   ```sh
   mkdir -p bin
   make copy TARGETS=runsc DESTINATION=bin/
   sudo cp ./bin/runsc /usr/local/bin
   ```
   
2. 运行测试：
   可使用以下命令运行标准测试套件：
   ```sh
   make unit-tests
   make tests
   ```
   
另外，对于想要使用 `go get` 而非 bazel 的用户，可以通过以下步骤安装 `runsc`：
   ```sh
   echo "module runsc" > go.mod
   GO111MODULE=on go get gvisor.dev/gvisor/runsc@go
   CGO_ENABLED=0 GO111MODULE=on sudo -E go build -o /usr/local/bin/runsc gvisor.dev/gvisor/runsc
   ```

项目推介：
作为 Google 的一个开源项目，**gVisor** 在容器安全领域内提供了革命性的解决方案。其开发十分活跃，不只是因为其背后有 Google 的支持，更因为其创新的技术方案吸引了广泛的关注和参与。此外，gVisor 的集成能力使其能够轻松地与现有的 Docker 和 Kubernetes 生态系统结合使用，这大大降低了使用门槛，吸引了许多知名公司和用户的关注和采用。作为一个将 Linux 通过 Linux 实现的项目，gVisor 为容器安全提供了一种全新的视角，是值得每一位云计算和容器技术爱好者关注的重要项目。

[oci]: https://www.opencontainers.org

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=google/gvisor&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/google/gvisor 

开源项目作者：google

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=google/gvisor)

关注我们，一起探索有意思的开源项目。

