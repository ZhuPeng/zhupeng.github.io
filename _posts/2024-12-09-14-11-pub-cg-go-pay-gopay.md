---
layout: post
title: 极简、易用的聚合支付 SDK
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

从电商交易到个人转账，数字支付无处不在，成为了我们日常生活的一部分。随着支付方式的多样化，开发者面临着如何快速集成多种支付平台的挑战，如微信、支付宝、PayPal 等。这不仅需要处理不同支付平台的接入问题，还要面对 API 接口变更、数据安全、支付效率等一系列挑战，大大增加了开发的复杂度和维护的工作量。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-56f98c9ab3f133097146cd9b78b9c149.png)

今天要给大家推荐一个 GitHub 开源项目 gopay，该项目在 GitHub 有超过 4.3k Star。

![](https://stats.deeptrain.net/repo/go-pay/gopay/?theme=light)

一句话介绍该项目：微信、支付宝、通联支付、拉卡拉、PayPal、Apple 的Go版本SDK。


![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241209230555338.png)


###### 项目介绍

GoPay 是一个使用 Go 语言开发的聚合支付 SDK，包括微信、支付宝、QQ、通联支付、拉卡拉、PayPal、Apple 等多种支付方式。提供了一套统一、简化的接口来处理各种支付需求，有效降低了开发者在支付功能集成上的工作难度。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241209230703122.png)

该项目主要突出以下特点：

1、多支付平台支持：简化了多个主流支付平台的集成流程。

2、极简接入体验：通过详尽的文档和示例代码，开发者可以快速实现支付功能的集成。

3、高度可定制：允许通过自定义`Logger`来满足不同的日志记录需求，同时通过查看具体支付方式的`xxx_test.go`代码，开发者可以理解如何针对不同的支付场景使用 SDK。

4、持续更新和优化：跟随各大支付平台的API变更同步更新，保持功能的前沿性和稳定性。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241209230804730.png)

###### 如何使用

执行以下命令安装：
```bash
go get -u github.com/go-pay/gopay
```

然后，通过以下示例代码来查看 GoPay 的版本，以开始接入支付功能：
```go
import (
    "github.com/go-pay/gopay"
    "github.com/go-pay/xlog"
)

func main() {
    xlog.Info("GoPay Version: ", gopay.Version)
}
```

更详细的支付方式接入可参考项目文档。

###### 项目推介

无论是开发新的电商平台、实现跨境支付、还是简化现有系统的支付处理，**GoPay** 都提供了一套完善的解决方案。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=go-pay/gopay&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/go-pay/gopay 

开源项目作者：go-pay

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=go-pay/gopay)

关注我们，一起探索有意思的开源项目。

