---
layout: post
title: GitHub 开源项目 kubernetes/ingress-nginx 介绍，Ingress NGINX Controller for Kubernetes
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 kubernetes/ingress-nginx，该项目在 GitHub 有超过 17.6k Star。

![](https://stats.deeptrain.net/repo/kubernetes/ingress-nginx/?theme=light)

一句话介绍该项目：Ingress NGINX Controller for Kubernetes





###### 项目介绍

背景介绍：在现代的云原生应用部署中，Kubernetes 已经成为了事实上的标准。然而，在 Kubernetes 集群中部署和管理应用时，我们经常面临着如何有效地管理、路由外部流量到集群内部服务的挑战。尤其是在处理动态伸缩、服务发现等复杂场景时，传统的方法往往显得力不从心，这时就需要一个可靠、高效的反向代理和负载均衡器来保证应用的高可用和高性能。



![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-f388f0818c437c54c0b3b706333720a3.png)

项目介绍：Ingress NGINX Controller 便是为解决上述问题而生。它是一个基于 NGINX 的 Kubernetes Ingress 控制器，利用 NGINX 的强大功能作为反向代理和负载均衡器，为 Kubernetes 集群提供了一种高效的方式来管理外部访问到集群内服务的流量。该项目支持多种配置选项，可以满足复杂的路由需求，还包括 SSL/TLS 终端解析、支持 WebSocket、HTTP/2 等。通过高度优化的配置和性能，Ingress NGINX Controller 能够保证在大规模集群环境下的高效运行。

如何使用：要开始使用 Ingress NGINX Controller，首先需要在你的 Kubernetes 集群上部署它。可以通过官方的 [Getting Started](https://kubernetes.github.io/ingress-nginx/deploy/) 指南来进行部署，该指南提供了不同 Kubernetes 环境下的详细部署步骤。一旦部署完成，你就可以开始配置 Ingress 资源来管理流量了。例如，一个基本的 Ingress 资源配置可能如下所示：

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: example-ingress
  annotations:
    kubernetes.io/ingress.class: nginx
spec:
  rules:
  - host: www.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: example-service
            port:
              number: 80
```

这个示例配置了一个简单的路由规则，将对 `www.example.com` 的访问路由到 `example-service` 服务上。

项目推介：Ingress NGINX Controller 是由 Kubernetes 官方支持和维护的项目，拥有广泛的社区支持和活跃的开发维护。它已经通过了严格的 E2E 测试，确保了与多个 Kubernetes 版本的兼容性。由于使用了 NGINX 这一广泛认可的高性能反向代理，它在业内享有盛誉。此外，许多世界知名的企业和组织已经在生产环境中使用 Ingress NGINX Controller，体现了其高度的可靠性和性能。不论是开发者还是企业，如果你正在寻找一种稳定、高效的方式来管理你的 Kubernetes 集群流量，Ingress NGINX Controller 是你的理想选择。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=kubernetes/ingress-nginx&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/kubernetes/ingress-nginx 

开源项目作者：kubernetes

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=kubernetes/ingress-nginx)

关注我们，一起探索有意思的开源项目。

