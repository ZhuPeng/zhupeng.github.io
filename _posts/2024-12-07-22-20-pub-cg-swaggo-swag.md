---
layout: post
title: 自动生成项目的 API 文档
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在构建 Web 应用程序时，创建和维护 API 文档是一个既耗时又复杂的任务。随着应用程序迭代和功能的增加，手动更新文档更是一个挑战。如果文档与实际 API 不同步，就会给前后端的交互和第三方使用带来错误和混淆。这种情况下，开发者需要一个能够自动化生成和更新 API 文档的工具，以提高开发效率，并确保文档的准确性和实时性。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-897aa9b0952792833b78bd0ea324f93b.png)

今天要给大家推荐一个 GitHub 开源项目 swag，该项目在 GitHub 有超过 11k Star

![](https://stats.deeptrain.net/repo/swaggo/swag/?theme=light)

一句话介绍该项目：Automatically generate RESTful API documentation with Swagger 2.0 for Go.

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241207230817349.png)


###### 项目介绍

Swag 是一个由 Go 语言编写的开源项目，旨在自动根据 Go 代码中的注释生成符合 Swagger 2.0 规范的 RESTful API 文档。Swag 能够简化 API 文档的生成和维护工作，让开发者专注于代码逻辑的实现，而无需担心文档的准确性和更新问题。项目支持多个流行的 Go Web 框架，并且提供了多种插件，使得在现有的 Go 项目中集成 Swagger UI 变得非常容易和快捷。

![](https://raw.githubusercontent.com/swaggo/swag/master/assets/swagger-image.png)

主要功能和设计要点包括：

1、注释格式化：通过一套声明性的注释格式，简化 API 文档的编写。

2、框架支持：提供了对多个 Go Web 框架的支持，包括但不限于 Gin。

3、灵活的集成：支持通过命令行工具 `swag` 初始化和格式化文档，灵活适用于不同项目的需求。

4、强大的自定义能力：支持自定义类型、枚举描述、安全注释等高级功能。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241207230958492.png)

###### 如何使用

1、通过以下命令安装 `swag`：

```sh
go install github.com/swaggo/swag/cmd/swag@latest
```

2、在你的 Go API 源代码中添加必要的注释，参见项目的声明性注释格式

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241207231232924.png)

3、在包含 `main.go` 的项目根目录下运行：

```sh
swag init
```
该命令将解析你的注释并生成 `docs` 文件夹及 `docs/docs.go`。

4、在你的代码中导入生成的 `docs/docs.go`，以初始化你的 Swagger 文档配置。

```go
import _ "example-module-name/docs"
```

###### 项目推介

**Swag** 由于其能够极大简化文档的生成流程和提高 API 文档的准确性与实用性，已经在 GitHub 上获得了不少星标。它不仅适合个人开发者，也被包括多家知名企业在内的组织所采用。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241207231313892.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=swaggo/swag&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/swaggo/swag 

开源项目作者：swaggo

开源协议：MIT License

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=swaggo/swag)

关注我们，一起探索有意思的开源项目。

