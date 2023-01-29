---
layout: post
title: GitHub 开源项目 projectdiscovery/asnmap 介绍，Go CLI and Library for quickly mapping organization network ranges using ASN information.
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 projectdiscovery/asnmap，该项目在 GitHub 有超过 0.3k Star，用一句话介绍该项目就是：“Go CLI and Library for quickly mapping organization network ranges using ASN information.”。

![](https://user-images.githubusercontent.com/8293321/192910103-a5945f2c-fa82-45e1-8568-1e46898ff6c5.png)

![image](https://user-images.githubusercontent.com/8293321/192092220-5d734305-fd3e-43fb-919a-91ff5296dfd2.png)

ASNMap是一个开源项目，可以帮助用户快速和方便地查询和枚举自己或其他组织的Autonomous System Number（ASN）信息。ASN是一种在路由器之间分配的编号，用于管理Internet上的路由器。该项目使用whois协议来收集ASN信息，并且支持多种输出格式，如JSON和CSV。

ASNMap是一个非常实用的工具，可用于网络安全研究、渗透测试和数据分析等多种场景。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=projectdiscovery/asnmap&type=Timeline)

### 如何安装使用

安装ASNMap可以使用go get命令进行安装。具体方法是在命令行中输入:
```
go get -u -v github.com/projectdiscovery/asnmap
```
这将在你的本地go环境中安装ASNMap项目。

安装完成后，你可以在命令行中使用“asnmap”命令来运行该项目。

注意: 你需要安装Go语言环境。


### 使用示例 DEMO

这是一个使用ASNMap进行ASN查询的示例代码：
```
package main

import (
    "fmt"
    "github.com/projectdiscovery/asnmap"
)

func main() {
    // create a new asnmap client
    client := asnmap.NewASNMap()

    // lookup the ASN for the IP address
    asn, _ := client.LookupASN("8.8.8.8")
    fmt.Printf("ASN for 8.8.8.8: %d\n", asn)
}
```

这段代码中，我们首先导入了fmt和asnmap包。然后我们创建了一个新的asnmap客户端，使用它来查询IP地址8.8.8.8的ASN。查询结果被打印出来。

这只是一个简单的示例，ASNMap还提供了更多的功能供你使用，比如:
- 查询某个ASN所属公司的信息
- 查询某个IP地址所属的地理位置
- 查询某个域名所属的ASN等

你可以在官方文档或者项目的github页面上查看更多的使用示例。


更多项目详情请查看如下链接。

开源项目地址：https://github.com/projectdiscovery/asnmap 

开源项目作者：projectdiscovery

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=projectdiscovery/asnmap)

