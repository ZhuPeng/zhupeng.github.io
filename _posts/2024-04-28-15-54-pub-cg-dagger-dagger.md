---
layout: post
title: 现代化的 API 和跨语言脚本引擎，更好的支撑 CICD
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在快速发展的软件行业，应用程序的交付速度和质量成为衡量成功的关键因素。然而，开发团队常常面临建立和维护复杂的部署脚本的挑战，这些脚本往往依赖于特定的环境、语言或平台，导致”手工“式的脚本管理过程低效、易出错。随着项目规模的扩大和技术栈的变化，这一问题更是成为开发和运维团队的核心痛点，急需一种解决方案来简化和标准化应用程序的交付过程。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240818195338663.png)

今天要给大家推荐一个 GitHub 开源项目 dagger，该项目在 GitHub 有超过 10.8k Star，一句话介绍该项目：Application Delivery as Code that Runs Anywhere

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240502221026794.png)

###### 项目介绍

**Dagger** 是一个开创性的开源工具，旨在通过提供一个现代化的 API 和跨语言脚本引擎，来替换软件项目中的传统部署脚本。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240502221140773.png)

通过 Dagger，开发者可以将项目中的任务和工作流封装成简单的函数，并使用自己喜欢的编程语言来编写。这些函数随后被打包成一个定制的 GraphQL API，可以从命令行界面、语言解释器或自定义 HTTP 客户端运行。此外，Dagger 允许开发者将这些函数打包成模块，以便于在下一个项目中复用或与社区共享。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240502221156532.png)

###### 如何使用

获取并开始使用 Dagger 是一个简单直接的过程。以下是基础的安装和使用步骤：

1、安装：首先，访问 Dagger 官方文档页面查看安装指南，根据您的操作系统进行安装。

```bash
# Website-> https://docs.dagger.io/install
# Mac
brew install dagger/tap/dagger

# Mac or Linux
curl -L https://dl.dagger.io/dagger/install.sh | BIN_DIR=$HOME/.local/bin sh
```

2、定义和封装函数：按照您项目的需求，使用您选择的编程语言定义必要的任务和工作流函数。

```go
package main

import (
	"context"
	"fmt"
	"math"
	"math/rand"
)

type Example struct{}

// Build and publish a project using a Wolfi container
func (m *Example) BuildAndPublish(ctx context.Context, buildSrc *Directory, buildArgs []string) (string, error) {
	ctr := dag.Wolfi().Container()

	return dag.
		Golang().
		BuildContainer(GolangBuildContainerOpts{Source: buildSrc, Args: buildArgs, Base: ctr}).
		Publish(ctx, fmt.Sprintf("ttl.sh/my-hello-container-%.0f", math.Floor(rand.Float64()*10000000))) //#nosec
}
```

3、通过 CLI 运行函数：完成函数定义后，可以直接通过命令行界面执行这些函数，为开发带来便利。

```bash
dagger call build-and-publish \
  --build-src=. \
  --build-args="-C","./hello"
```

###### 项目推介

Dagger 已经成为数以百计的开发团队选择的应用程序交付工具，尤其是对于追求开发与运维一体化（DevOps）和持续集成/持续部署（CI/CD）的团队来说，是一个不可或缺的工具。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240502221834512.png)

此外，Dagger 以其创新的使用 GraphQL 来声明和执行部署任务，为应用交付带来前所未有的灵活性和速度，大大优化了开发流程，减少了开发和部署的时间和成本。不论是刚刚起步的小型项目还是需要高度定制化交付流程的大型企业，Dagger 都能提供强大支持，是值得信赖和投入的开源项目。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240502221810939.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=dagger/dagger&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/dagger/dagger 

开源项目作者：dagger

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=dagger/dagger)

关注我们，一起探索有意思的开源项目。

