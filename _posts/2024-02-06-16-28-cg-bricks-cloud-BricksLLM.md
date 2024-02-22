---
layout: post
title: GitHub 开源项目 bricks-cloud/BricksLLM 介绍，Enterprise grade API infrastructure that helps you access control and mange spend across OpenAI, Azure OpenAI and Anthropic. 
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 bricks-cloud/BricksLLM，该项目在 GitHub 有差不多 1000 Star，用一句话介绍该项目就是：“Enterprise grade API infrastructure that helps you access control and mange spend across OpenAI, Azure OpenAI and Anthropic. ”。



![](https://raw.githubusercontent.com/bricks-cloud/BricksLLM/master/./assets/bricks-logo.png)



` | optional | Timeout for proxing requets to the foundational model provider endpoint | `10s`
> | `STATSD_HOST`         | optional | Host for statsd | `localhost` 
> | `STATSD_PORT`         | optional | The port that statsd runs on | `8125`
> | `LOGGING_PROVIDER`         | optional | This value can only be stdout | `stdout`
> | `LOGGING_LEVEL`         | optional | Log level (panic, fatal, error, warn, info, debug, trace)  | `info` 

1、背景介绍：

在现实生活中，我们通常会遇到调用 AI 网关的问题，例如你需要调用 OpenAI，Azure OpenAI 或者 Anthropic 进行特定的开发工作，但是这些 AI 服务提供商并没有提供细粒度的访问控制，这里的访问控制包括：访问的频率限制、花费限制以及会话的存在时间限制等。如果不加以控制，这可能会导致服务调用成本无法控制，甚至有数据安全风险。

2、项目介绍：

BricksLLM 是一个用 Go 语言编写的云原生 AI 网关。它支持 OpenAI、Anthropic 和 Azure OpenAI，并且，BricksLLM 提供创建 API 密钥的功能，这些密钥具有速率限制、成本限制和 TTL。这些 API 密钥可以同时用于开发和生产，以达到精细的访问控制。这个代理的设计目标是与现有 SDK 100% 兼容。

BricksLLM 的主要功能包括：速率限制、成本控制、成本分析、请求分析、Cache、请求重试、服务降级等。同时，它还对所有 OpenAI 端点、Anthropic 和 Azure OpenAI 提供了原生支持，并且允许集成自定义模型，支持 Datadog 集成，具有日志保护隐私控制功能。

3、如何使用：

BricksLLM 安装和使用的最简单方法是通过 [BricksLLM-Docker](https://github.com/bricks-cloud/BricksLLM-Docker)。首先克隆 `BricksLLM-Docker` 仓库，然后切换到 `BricksLLM-Docker` 目录，之后本地部署 `BricksLLM`，`Postgresql` 和 `Redis`。之后是创建提供商设置和 `Bricks API key`。然后，你就可以像平常那样使用 `OpenAI`，将你的请求引向 `BricksLLM`.

这个过程涉及代码操作如下：

```bash
git clone https://github.com/bricks-cloud/BricksLLM-Docker
cd BricksLLM-Docker
docker-compose up
curl -X PUT http://localhost:8001/api/provider-settings \
   -H "Content-Type: application/json" \
   -d '{
          "provider":"openai",
          "setting": {
             "apikey": "YOUR_OPENAI_KEY"
          }
      }'   
curl -X PUT http://localhost:8001/api/key-management/keys \
   -H "Content-Type: application/json" \
   -d '{
	      "name": "My Secret Key",
	      "key": "my-secret-key",
	      "tags": ["mykey"],
        "settingIds": ["ID_FROM_STEP_FOUR"],
        "rateLimitOverTime": 2,
        "rateLimitUnit": "m",
        "costLimitInUsd": 0.25
      }' 
```
当然，如果你需要更新当前版本的话，可以直接通过命令 `docker pull luyuanxin1995/bricksllm:latest` 来完成。

4、项目推介：

BricksLLM 对于需要使用 AI 服务提供商如 OpenAI，Azure OpenAI 或者 Anthropic 的开发者来说是一个非常有用的工具。它弥补了这些 AI 服务提供商没有详细访问控制的缺陷，塑造了一个安全、可控的环境，使


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=bricks-cloud/BricksLLM&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/bricks-cloud/BricksLLM 

开源项目作者：bricks-cloud

开源协议：MIT License

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=bricks-cloud/BricksLLM)

关注我们，一起探索有意思的开源项目。

