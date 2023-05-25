---
layout: post
title: 支持模拟成千上万个 Kubelet 节点的效率工具
tags: 云原生
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 kubernetes-sigs/kwok，该项目在 GitHub 有超过 0.4k Star，用一句话介绍该项目就是：“Kubernetes WithOut Kubelet -  Simulates thousands of Nodes and Clusters.”，支持模拟成千上万个 Kubelet 节点。

![](https://raw.githubusercontent.com/kubernetes-sigs/kwok/master/./logo/kwok.svg)

使用动图：https://raw.githubusercontent.com/kubernetes-sigs/kwok/master/demo/manage-clusters.svg

Kwok 是一个用于开发 Kubernetes 并提高效率的工具。它可以帮助用户快速在本地计算机上模拟成千上万个跟 Kubelet 行为一致的节点，从而方便用户做各种形式的测试，这对 Kubernetes 的性能优化帮助很大。

### 如何安装使用

Kwok 有多种安装方式，推荐使用 brew install kwok。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230212195503014.png)

以下是项目的系统支持状态：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230212195320048.png)


### 使用示例 DEMO

安装 kwok 后，使用如下命令即可启动一个本地的 Kubernetes 集群：

```bash
kwok \
  --kubeconfig=~/.kube/config \
  --manage-all-nodes=false \
  --manage-nodes-with-annotation-selector=kwok.x-k8s.io/node=fake \
  --manage-nodes-with-label-selector= \
  --disregard-status-with-annotation-selector=kwok.x-k8s.io/status=custom \
  --disregard-status-with-label-selector= \
  --cidr=10.0.0.1/24 \
  --node-ip=10.0.0.1
```

对应的也可以使用 kwokctl 来创建和管理集群：

```bash
$ kwokctl create cluster --name=kwok
kwokctl create cluster
Creating cluster "kwok-kwok"
Starting cluster "kwok-kwok"
Cluster "kwok-kwok" is ready
You can now use your cluster with:

    kubectl config use-context kwok-kwok

Thanks for using kwok!

$ kubectl config use-context kwok-kwok

$ kwokctl get clusters
kwok

$ kwokctl delete cluster --name=kwok
Stopping cluster "kwok-kwok"
Deleting cluster "kwok-kwok"
Cluster "kwok-kwok" deleted
```

有了集群后，可以使用 Kubectl 创建 v1.Node 资源来新增虚拟的 Node 节点，执行以上 yaml 配置后，会生成如下 node 节点：

```bash
$ kubectl get node -o wide
NAME          STATUS   ROLES   AGE   VERSION   INTERNAL-IP   EXTERNAL-IP   OS-IMAGE    KERNEL-VERSION   CONTAINER-RUNTIME
kwok-node-0   Ready    agent   5s    fake      196.168.0.1   <none>        <unknown>   <unknown>        <unknown>
```

这样你可以像正常使用 k8s 一样在上面创建 pod。

更多项目详情请查看如下链接。

开源项目地址：https://github.com/kubernetes-sigs/kwok  (文末可点击阅读原文)

开源项目作者：kwok



关注我们，一起探索有意思的开源项目。
