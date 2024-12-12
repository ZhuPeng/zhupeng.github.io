---
layout: post
title: GitHub 开源项目 aquasecurity/kube-bench 介绍，Checks whether Kubernetes is deployed according to security best practices as defined in the CIS Kubernetes Benchmark
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 aquasecurity/kube-bench，该项目在 GitHub 有超过 7.1k Star。

![](https://stats.deeptrain.net/repo/aquasecurity/kube-bench/?theme=light)

一句话介绍该项目：Checks whether Kubernetes is deployed according to security best practices as defined in the CIS Kubernetes Benchmark




![Kubernetes Bench for Security](https://raw.githubusercontent.com/aquasecurity/kube-bench/master//docs/images/output.png "Kubernetes Bench for Security")

![](https://raw.githubusercontent.com/aquasecurity/kube-bench/master/docs/images/kube-bench.png)


###### 项目介绍

### 背景介绍

随着 Kubernetes 成为当代云原生应用的标准部署环境，其安全性也越来越受到企业和开发者的重视。但是，如何确保在持续迅速发展的 Kubernetes 生态中遵循最佳安全实践，是一个普遍面临的挑战。在此背景下，遵守像 CIS (Center for Internet Security) Kubernetes 基准这样的标准成为了验证 Kubernetes 集群配置安全性的重要手段。CIS Kubernetes 基准提供了一系列强有力的安全配置检查指南，但手动验证这些指南既耗时又容易出错。

### 

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-92446082c58936fc87e7ce99f744898f.png)

项目介绍

`kube-bench` 是一个开源工具，旨在自动化检查 Kubernetes 的部署是否遵循了 CIS Kubernetes 基准中定义的安全最佳实践。这个工具通过运行 YAML 文件中配置的测试来实现，使得随着测试规范的发展，更新这个工具变得轻而易举。此外，`kube-bench` 也是 [`Trivy`](https://github.com/aquasecurity/trivy)——一款云原生安全扫描器——的组成部分，支持 CIS Kubernetes 基准扫描，以及作为 Kubernetes 操作员部署。

### 如何使用

使用 `kube-bench` 极其简便。若要在您的 Kubernetes 集群中运行 `kube-bench`，您可以使用附带的 `job.yaml` 文件来创建一个 Job，运行测试。具体操作如下：

```bash
$ kubectl apply -f job.yaml
job.batch/kube-bench 创建成功

# 使用 kubectl 查看 pods 状态
$ kubectl get pods
NAME                      READY   STATUS      RESTARTS   AGE
kube-bench-j76s9   0/1     Completed   0          11s

# 测试完成后，查看日志以获取结果
kubectl logs kube-bench-j76s9
[INFO] 1 Master Node Security Configuration
[INFO] 1.1 API Server
...
```

更多信息和不同的运行方式，请参见 [文档](https://github.com/aquasecurity/kube-bench/docs/running.md)。

### 项目推介

`kube-bench` 是由 Aqua Security 维护的一个项目，该团队在云原生安全领域拥有广泛的经验和知名度。截至目前，`kube-bench` 已在 GitHub 上获得了大量 Star 并不断更新，显示了其活跃的开发状态和社区支持的强度。它被多家知名公司和组织用于确保他们的 Kubernetes 集群配置达到安全标准。

除了在 GitHub 上的活跃度外，`kube-bench` 也易于与其他安全工具集成，比如与 Aqua Security 的 Trivy 扫描器结合使用，提供了一站式的云原生安全方案。无论是 Kubernetes 的开发者还是安全专家，都能从 `kube-bench` 中获益，确保他们的集群安全、稳定。

结合其持续更新以支持最新版的 CIS Kubernetes 基准，`kube-bench` 成为了 Kubernetes 集群安全配置不可或缺的工具之一。不论您是刚接入 Kubernetes 的新手，还是经验丰富的专家，`kube-bench` 都是确保集群安全的强大助手。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=aquasecurity/kube-bench&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/aquasecurity/kube-bench 

开源项目作者：aquasecurity

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=aquasecurity/kube-bench)

关注我们，一起探索有意思的开源项目。

