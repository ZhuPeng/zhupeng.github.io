---
layout: post
title: 一款更好的模拟网络攻击的框架
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 fin3ss3g0d/evilgophish，该项目在 GitHub 有超过 800 Star。

![new-dashboard](https://raw.githubusercontent.com/fin3ss3g0d/evilgophish/master/images/tokens-gophish.png)
![diagram](https://raw.githubusercontent.com/fin3ss3g0d/evilgophish/master/images/diagram.png)


evilgophish 是一个开源的社会工程学攻击框架，它可以在攻击者和受害者之间模拟真实的网络环境。该项目提供了一种简单的方法来构建和管理攻击页面，并且可以跟踪和收集受害者的证书和凭据。它的设计目的是为了让网络安全专业人员，攻击者和研究人员能够更好地理解和模拟社会工程学攻击。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=fin3ss3g0d/evilgophish&type=Timeline)

### 如何安装使用

根据项目的说明，安装 evilgophish 需要以下步骤：

1. 安装 Go 语言环境: evilgophish 是用 Go 编写的，因此需要先安装 Go 环境。可以参考 Go 语言的官方网站（https://golang.org/doc/install）获取安装说明。

2. 获取 evilgophish 源代码: 使用命令 `go get -u github.com/fin3ss3g0d/evilgophish` 获取 evilgophish 的源代码。

3. 编译 evilgophish: 进入 evilgophish 目录，使用命令 `go build` 编译该项目。

4. 运行 evilgophish: 使用命令 `./evilgophish` 运行 evilgophish。

注意：在运行 evilgophish 之前，需要配置 config.json 文件，里面包含了相关的设置和配置，如数据库地址，邮件服务器等。


### 使用示例 DEMO

该项目的使用示例如下：

1. 配置 config.json 文件，包括数据库地址，邮件服务器等设置。

2. 编译并运行 evilgophish，使用命令 `go build && ./evilgophish`

3. 打开浏览器，访问 http://127.0.0.1:3333 进入管理面板

4. 创建新的攻击项目，设置相关参数，如邮件主题，收件人等

5. 发送邮件，监控攻击效果


更多项目详情请查看如下链接。

开源项目地址：https://github.com/fin3ss3g0d/evilgophish 

开源项目作者：fin3ss3g0d

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=fin3ss3g0d/evilgophish)



关注我们，一起探索有意思的开源项目。
