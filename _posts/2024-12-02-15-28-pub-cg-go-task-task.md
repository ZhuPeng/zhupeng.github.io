---
layout: post
title: 比肩 Make 的通用构建工具
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在软件开发过程中，自动化成为了提升效率和确保一致性的关键。无论是编译代码、运行测试、打包软件，还是部署应用，自动化任务都扮演着不可或缺的角色。然而，传统的自动化工具如 GNU Make 虽然功能强大，但对于新手来说，学习成本相对较高，而且在跨平台使用时可能会遇到一些兼容性问题。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-0d1377bccdd5b10416ddbd83c1bea269.png)

今天要给大家推荐一个 GitHub 开源项目 go-task，该项目在 GitHub 有超过 11.6k Star。

![](https://stats.deeptrain.net/repo/go-task/task/?theme=light)

一句话介绍该项目：A task runner / simpler Make alternative written in Go

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241207224855361.png)


###### 项目介绍

Task 是一个用 Go 语言编写的任务运行器、构建工具，旨在提供比 GNU Make 更简单、更易用的用户体验。通过 Task，用户可以轻松定义和执行自动化任务，在提升开发效率的同时，降低学习成本和操作复杂度。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241207225011378.png)

Task 的主要功能和设计要点包括：

1、简洁易懂的任务定义：使用 YAML 文件来定义任务，结构清晰，易于理解和修改。

2、跨平台兼容：无论是在 Linux、macOS 还是 Windows 上，Task 都能够无缝运行，免除了传统工具的平台限制。

3、并行任务执行：Task 支持并行执行多个任务，大幅提升了构建和部署的效率。

4、灵活的任务依赖管理：可以轻松定义任务间的依赖关系，保证复杂工作流程的顺畅执行。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241207225056435.png)

###### 如何使用

可以通过包管理工具，或者预编译的二进制文件直接下载使用

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241207225207832.png)

或者若你已经安装了 Go 环境，可以使用以下命令安装：

```sh
go install github.com/go-task/task/v3/cmd/task@latest
```

使用 Task 定义并运行任务也非常直观。首先，创建一个名为 `Taskfile.yml` 的文件，在其中定义你的任务：

```yaml
version: '3'

tasks:
  build:
    cmds:
      - go build -v -i main.go

  assets:
    cmds:
      - esbuild --bundle --minify css/index.css > public/bundle.css
```

然后，通过运行以下命令执行任务：

```sh
task assets build
```

会先执行 esbuild 的构建，然后进行 Go 应用的构建打包。

###### 项目推介

Task 因其简洁易用且功能强大为众多开发者所喜爱。凭借积极的开发态度和稳定的更新，Task 获得了 GitHub 上的高星标记，聚集了大量的开发者社区参与贡献和反馈。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=go-task/task&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/go-task/task 

开源项目作者：go-task

开源协议：MIT License

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=go-task/task)

关注我们，一起探索有意思的开源项目。

