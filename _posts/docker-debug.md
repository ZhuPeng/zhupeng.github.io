这些年 Docker 的快速发展，已经成为了很多公司的标配，也不再是一个只能在开发阶段使用的玩具了。作为在生产环境中广泛应用的产品，Docker 有着非常成熟的社区以及大量的使用者，代码库中的内容也变得非常庞大。

Docker 打包的镜像的时候会将需要发布的包加载进去，而对于一些常用的运维、Debug 工具则根据不同的公司的策略会略有不同，比如"富容器"就是按照虚拟机的配置来打包镜像，但是按照 Docker 的理念，镜像的大小越小肯定是越利于分发的。今天要介绍的两个工具是在不忘镜像里面打包过多的工具的情况下，也能很好的去做到容器的故障排查。

1. Kubectl debug

Kubernetes 已经被很多公司用来作为容器的调度系统了，可以说是当今事实上的标准了。`kubectl-debug` 是一个简单的 kubectl 插件，能够帮助你便捷地进行 Kubernetes 上的 Pod 排障诊断。背后做的事情很简单: 在运行中的 Pod 上额外起一个新容器，并将新容器加入到目标容器的 `pid`, `network`, `user` 以及 `ipc` namespace 中，这时我们就可以在新容器中直接用 `netstat`, `tcpdump` 这些熟悉的工具来解决问题了, 而旧容器可以保持最小化，不需要预装任何额外的排障工具。

![](https://raw.githubusercontent.com/aylei/kubectl-debug/master/docs/kube-debug.gif)

> 项目地址：[<https://github.com/aylei/kubectl-debug>](<https://github.com/aylei/kubectl-debug>)



2. Docker-debug

`docker-debug` 的想法是来源于 Kubectl debug，如果你没有使用 Kubernetes，可以使用 Docker-debug，毕竟都是容器。

![](https://7465-test-3c9b5e-1258459492.tcb.qcloud.la/GitHub%E7%B2%BE%E9%80%89/docker-debug.png)

> 项目地址：[https://github.com/zeromake/docker-debug](<https://github.com/zeromake/docker-debug>)

***

