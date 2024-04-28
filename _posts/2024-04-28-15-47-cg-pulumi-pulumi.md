---
layout: post
title: GitHub 开源项目 pulumi/pulumi 介绍，Pulumi - Infrastructure as Code in any programming language. Build infrastructure intuitively on any cloud using familiar languages 🚀
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 pulumi/pulumi，该项目在 GitHub 有超过 19.8k Star，一句话介绍该项目：Pulumi - Infrastructure as Code in any programming language. Build infrastructure intuitively on any cloud using familiar languages 🚀




![Watch the video](https://raw.githubusercontent.com/pulumi/pulumi/master//youtube_preview_image.png)

![](https://www.pulumi.com/images/logo/logo-on-white-box.svg?)

![](https://www.pulumi.com/images/get-started.svg?)

![](https://www.pulumi.com/images/docs/quickstart/console.png)

![](https://www.pulumi.com/logos/tech/logo-js.png)

![](https://www.pulumi.com/logos/tech/logo-ts.png)

![](https://www.pulumi.com/logos/tech/logo-python.svg)

![](https://www.pulumi.com/logos/tech/logo-golang.png)

![](https://www.pulumi.com/logos/tech/dotnet.svg)

![](https://www.pulumi.com/logos/tech/java.svg)


###### 项目介绍

### 背景介绍

在当今这个数字化飞速发展的时代，快速部署和管理复杂的云基础设施成了许多组织面临的一大挑战。随着云服务提供商的种类和服务的增多，如何有效地管理这些资源，同时确保开发效率和资源配置的灵活性，成为了企业云战略中的一项核心议题。大多数现有的工具要么与特定云平台强绑定，要么语法过于繁琐，不利于快速迭代和交叉团队的合作。因此，一个能够跨平台、易于使用，支持多种编程语言的云基础设施即代码（IaC）工具，便成了行业内急需解决的问题。

### 

![](https://dalleprodsec.blob.core.windows.net/private/images/813a8abe-2ee6-4350-a6eb-0672c9f26286/generated_00.png?se=2024-04-29T07%3A46%3A59Z&sig=KIRBVhkbOOPWA%2BOtfbq3w5WbgmLPb9wPvjSpXCMkhMg%3D&ske=2024-05-05T04%3A19%3A15Z&skoid=e52d5ed7-0657-4f62-bc12-7e5dbb260a96&sks=b&skt=2024-04-28T04%3A19%3A15Z&sktid=33e01921-4d64-4f8c-a055-5bdaffd5e33d&skv=2020-10-02&sp=r&spr=https&sr=b&sv=2020-10-02)

项目介绍

[Pulumi](https://github.com/pulumi/pulumi) 是一个开源项目，旨在通过在任何云上使用熟悉的语言来直观地构建基础设施，提供了一种全新的云基础设施即代码（IaC）解决方案。该项目允许开发者使用其熟悉的编程语言来定义和部署云服务资源，支持包括 AWS、Azure、Google Cloud Platform 和 Kubernetes 在内的 120 多个提供商。更令人兴奋的是，Pulumi 摆脱了传统 IaC 工具依赖于 YAML 或特定声明性语法的限制，让开发者可以利用循环、函数、类和包管理等标准语言特性，实现更加直观和灵活的基础设施管理方案。

### 如何使用

首先，需要安装 Pulumi。在终端中运行以下命令即可：

```bash
$ curl -fsSL https://get.pulumi.com/ | sh
```

接下来，可以创建一个新项目，开始你的 Pulumi 之旅：

```bash
$ mkdir pulumi-demo && cd pulumi-demo
$ pulumi new hello-aws-javascript
```
以 TypeScript 为例，创建三个 Web 服务器的简单例子：

```typescript
const aws = require("@pulumi/aws");
const sg = new aws.ec2.SecurityGroup("web-sg", {
    ingress: [{ protocol: "tcp", fromPort: 80, toPort: 80, cidrBlocks: ["0.0.0.0/0"] }],
});
for (let i = 0; i < 3; i++) {
    new aws.ec2.Instance(`web-${i}`, {
        ami: "ami-7172b611",
        instanceType: "t2.micro",
        vpcSecurityGroupIds: [sg.id],
        userData: `#!/bin/bash
            echo "Hello, World!" > index.html
            nohup python -m SimpleHTTPServer 80 &`,
    });
}
```

又或者是构建一个简单的无服务器定时器，每天早上 8:30 归档 Hacker News：

```typescript
const aws = require("@pulumi/aws");

const snapshots = new aws.dynamodb.Table("snapshots", {
    attributes: [{ name: "id", type: "S", }],
    hashKey: "id", billingMode: "PAY_PER_REQUEST",
});

aws.cloudwatch.onSchedule("daily-yc-snapshot", "cron(30 8 * * ? *)", () => {
    require("https").get("https://news.ycombinator.com", res => {
        let content = "";
        res.setEncoding("utf8");
        res.on("data", chunk => content += chunk);
        res.on("end", () => new aws.sdk.DynamoDB.DocumentClient().put({
            TableName: snapshots.name.get(),
            Item: { date: Date.now(), content },
        }).promise());
    }).end();
});
```

### 项目推介

Pulumi 是开源项目，遵循 Apache 2.0 许可协议，它的开发活跃，社区支持度高。项目不仅支持多种语言（例如 TypeScript、JavaScript、Python

###### 如何使用

###### 项目推介

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=pulumi/pulumi&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/pulumi/pulumi 

开源项目作者：pulumi

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=pulumi/pulumi)

关注我们，一起探索有意思的开源项目。

