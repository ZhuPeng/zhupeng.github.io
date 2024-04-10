---
layout: post
title: 在博客文章嵌入交互式代码片段的平台
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

我们在编写文档、开发在线课程或者撰写技术博客时，经常需要插入一些代码片段来解释具体概念或者演示算法运行效果。然而，普通的书写工具并不能很好的支持代码片段的排版和交互操作，用户无法直接在文中运行和修改代码。这种沟通方式的单向性和僵化性，显著降低了文档的可读性和用户的学习效率。

今天要给大家推荐一个 GitHub 开源项目 nalgeon/codapi，该项目在 GitHub 有差不多 1000 Star，一句话介绍该项目：Interactive code examples for documentation, education and fun.

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240330202532492.png)

###### 项目介绍

Codapi 是一个为产品文档、在线课程或者博客文章嵌入交互式代码片段的开源平台。通过 Codapi，静态的代码示例可以被自动转换成 Playground，随意修改和实时运行。Codapi 提供了隔离的执行环境和对这些环境中代码执行的 API，再配合 JavaScript 小部件 [codapi-js](https://github.com/nalgeon/codapi-js) ，进行更方便的集成。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240330202631174.png)

支持超多编程语言：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240330202654276.png)

###### 如何使用

主要通过 `/v1/exec` 接口运行代码，具体示例如下：

```http
POST https://api.codapi.org/v1/exec
content-type: application/json

{
    "sandbox": "python",
    "command": "run",
    "files": {
        "": "print('hello world')"
    }
}
```
此时 `sandbox` 是预先设定好的沙箱名称，`command` 是通过这个沙箱支持的命令名称。

另外，你可以在 [codapi-js](https://github.com/nalgeon/codapi-js) 页面了解如何在网页中嵌入 JavaScript 小部件。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240330202751650.png)

###### 项目推介

Codapi 是一个优秀的开源项目，它之所以值得推荐，主要因为它在以下几个方面有出色的表现：首先，它为我们开发文档提供了一种新颖有趣的形式，使之更具互动性，从而提升读者的体验。其次，Codapi 提供了适用于任何编程语言、数据库或软件的沙箱，并且项目使用了非常宽松的 Apache-2.0 许可证。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=nalgeon/codapi&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/nalgeon/codapi 

开源项目作者：nalgeon

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=nalgeon/codapi)

关注我们，一起探索有意思的开源项目。

