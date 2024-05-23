---
layout: post
title: GitHub 开源项目 prometheus/node_exporter 介绍，Exporter for machine metrics
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 prometheus/node_exporter，该项目在 GitHub 有超过 10.4k Star。

![](https://stats.deeptrain.net/repo/prometheus/node_exporter/?theme=light)

一句话介绍该项目：Exporter for machine metrics




![Docker Repository on Quay](https://quay.io/repository/prometheus/node-exporter/status)


###### 项目介绍

背景介绍：随着技术的不断进步，硬件和操作系统的性能监控变得尤为重要，但传统的监控工具往往面临着可扩展性差、无法适应不同环境、覆盖面窄等问题。尤其在多样化的 *NIX 环境下，需要一个能够提供丰富、准确的系统硬件及操作系统指标的工具，以帮助开发和运维团队有效地监控和分析系统状态。



![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-d2b4f65e131a21487c8589e352c0e5b9.png)

项目介绍：`Node exporter` 是 Prometheus 项目的一部分，专为 *NIX 内核设计，用于导出硬件和操作系统指标。它是用 Go 语言编写的，支持通过插件扩展其指标收集器。对于 Windows 用户，推荐使用 [Windows exporter](https://github.com/prometheus-community/windows_exporter)。而要暴露 NVIDIA GPU 指标，可以使用 [prometheus-dcgm](https://github.com/NVIDIA/dcgm-exporter)。`Node exporter` 的设计注重灵活性和扩展性，让用户可以根据自己的需求启用或禁用指标收集器，满足不同的监控需求。

如何使用：`Node exporter` 默认监听 HTTP 端口 9100，安装和使用都相对简单。可以通过 Docker 运行，也可使用 Ansible 进行自动化安装。例如，要通过 Docker 运行，可以使用以下命令：

```bash
docker run -d \
  --net="host" \
  --pid="host" \
  -v "/:/host:ro,rslave" \
  quay.io/prometheus/node-exporter:latest \
  --path.rootfs=/host
```

此命令会启动 `node_exporter`，并将其配置为访问宿主机的文件系统，以便监控宿主而不是容器内的系统指标。

项目推介：`Node exporter` 是 Prometheus 生态系统中的重要组成部分，因其强大的系统监控能力和灵活的配置选项，已经被全球数以千计的公司和组织采用。作为一个活跃的开源项目，它不仅拥有强大的社区支持，而且还持续更新，引入新功能和性能优化。无论是云基础设施、物理服务器，还是混合环境，`Node exporter` 都是监控系统健康状态不可或缺的工具。此外，其背后 Prometheus 项目的稳固和广泛使用，也进一步加强了用户对 `Node exporter` 的信心。无论你是开发人员、系统管理员还是 DevOps 工程师，`Node exporter` 都将是你日常工作中强大的助手。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=prometheus/node_exporter&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/prometheus/node_exporter 

开源项目作者：prometheus

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=prometheus/node_exporter)

关注我们，一起探索有意思的开源项目。

