---
layout: post
title: 现代化工作流引擎，写脚本即可生成工作流程和用户界面
tags: 
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

公司内部团队经常需要构建和管理复杂的内部工具，比如 API 网关、后台作业、工作流程以及用户界面。如果都单独开发，这些任务需要大量的开发时间来集成和维护。尤其是在数据流程和自动化方面，找到一个既灵活又能提供足够控制权的平台一直是开发者的一大挑战。而现有的第三方解决方案，如 Retool 和 Airflow，虽然功能强大，但通常涉及昂贵的订阅费用，对于想要完全控制和自定义工作流的团队来说，它们的功能可能仍显不足。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-2af2ff8c6290021f78ce7bf081633216.png)

今天要给大家推荐一个 GitHub 开源项目 windmill，该项目在 GitHub 有超过 10.1k Star。

![](https://stats.deeptrain.net/repo/windmill-labs/windmill/?theme=light)

一句话介绍该项目：Open-source developer platform to turn scripts into workflows and UIs. Fastest workflow engine (5x vs Airflow). Open-source alternative to Airplane and Retool.

![](https://raw.githubusercontent.com/windmill-labs/windmill/master/./imgs/windmill-banner.png)

###### 项目介绍

Windmill 提供了一种革新性的解决方案，实现了脚本到工作流程和用户界面（UI）的转换，是 Retool、Airplane 等商业工具的开源替代品。通过 Windmill，您可以将简单的脚本自动转换为可分享的 UI，便于团队成员之间的协作和共享。它支持多种脚本语言，包括 Python、TypeScript、Go、Bash、SQL 和 GraphQL，几乎不设限地为您提供灵活性。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241106000705684.png)

Windmill 设计的关键优点在于它的自动生成 UI 和定制 UI 功能，这允许用户以极低的代码量构建复杂的应用程序。此外，其基于 Rust 的后端、Svelte 的前端和先进的沙盒执行机制确保了应用的高性能和安全性。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240911224402295.png)

其主张的最快自托管工作流引擎更是在性能比较中超越了 Airflow 等方案。

![](https://raw.githubusercontent.com/windmill-labs/windmill/master/imgs/fastest.png)

###### 如何使用

通过 Docker compose、Kubernetes 或直接从二进制文件运行 Windmill 来轻松地在本地或服务器上进行自托管。

```bash
curl https://raw.githubusercontent.com/windmill-labs/windmill/main/docker-compose.yml -o docker-compose.yml
curl https://raw.githubusercontent.com/windmill-labs/windmill/main/Caddyfile -o Caddyfile
curl https://raw.githubusercontent.com/windmill-labs/windmill/main/.env -o .env

docker compose up -d
```

Windmill 提供了强大的 CLI 工具，支持从本地文件、GitHub 存储库同步脚本，并且可以从本地命令运行脚本和工作流。以下是一个使用 TypeScript 编写的脚本示例：

```typescript
//import any dependency from npm
import * as wmill from "windmill-client"
import * as cowsay from 'cowsay@1.5.0';

export async function main( a: number, b: "my" | "enum", c: Postgresql, d = "default string", e = { nested: "object" } ) {
  const email = process.env["WM_EMAIL"];
  console.log(cowsay.say({ text: "hello " + email }));
  return { foo: d };
}
```

以下是一个 Workflow 示例：

![](https://raw.githubusercontent.com/windmill-labs/windmill/master/./imgs/windmill-flow.png)

###### 项目推介

Windmill 以其创新的解决方案和卓越的性能，已经在开源社区中获得了显著的认可。对于希望构建和管理内部工具的团队来说，Windmill 提供了一个与众不同的选择，既可以减少开发和维护成本，也能提高工作效率。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240911224809959.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=windmill-labs/windmill&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/windmill-labs/windmill 

开源项目作者：windmill-labs

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=windmill-labs/windmill)

关注我们，一起探索有意思的开源项目。

