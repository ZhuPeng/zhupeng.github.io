---
layout: post
title: 用于生成 Go 测试数据的生成器推荐
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 go-faker/faker，该项目在 GitHub 有超过 200 Star，用一句话介绍该项目就是：“Go (Golang) Fake Data Generator for Struct”，用于生成 Go 测试数据的生成器。以下是具体的功能演示：

![Example to use Faker](https://cdn-images-1.medium.com/max/800/1*AkMbxngg7zfvtWiuvFb4Mg.gif)

faker 提供了生成伪数据的功能，这个库可以生成各种类型的伪数据，包括人名、地址、电话号码、电子邮件地址、银行账号等。这些数据可以用于测试、演示和开发等场景。

在使用 faker 库时，可以通过调用不同的函数来生成不同类型的伪数据，并可以通过设置配置参数来控制生成的数据的语言、地区、格式等。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=go-faker/faker&type=Timeline)

### 如何安装使用

1. 使用Go的包管理工具（例如`go mod`或`dep`）进行安装：
```
go get github.com/go-faker/faker
```
2. 或者手动下载源代码并编译安装：
```
git clone https://github.com/go-faker/faker.git
cd faker
go build
go install
```


### 使用示例 DEMO

```
package main

import (
	"fmt"
	"github.com/go-faker/faker"
)

type SomeStructWithTags struct {
	Latitude           float32           `faker:"lat"`
	Longitude          float32           `faker:"long"`
	RealAddress        faker.RealAddress `faker:"real_address"`
	CreditCardNumber   string            `faker:"cc_number"`
	CreditCardType     string            `faker:"cc_type"`
	Email              string            `faker:"email"`
	DomainName         string            `faker:"domain_name"`
	IPV4               string            `faker:"ipv4"`
	IPV6               string            `faker:"ipv6"`
}

func main() {
	a := SomeStructWithTags{}
	err := faker.FakeData(&a)
	if err != nil {
		fmt.Println(err)
	}
	fmt.Printf("%+v", a)
}
```
运行结果：
```json
{
			Latitude: 81.12195
			Longitude: -84.38158
			RealAddress: {Address:107 Guaymas Place City:Davis State:CA PostalCode:95616 Coordinates:{Latitude:38.567048 Longitude:-121.746046}}
			CreditCardType: American Express
			CreditCardNumber: 373641309057568
			Email: mJBJtbv@OSAaT.ru
			DomainName: FWZcaRE.ru,
			IPV4: 99.23.42.63
			IPV6: 975c:fb2c:2133:fbdd:beda:282e:1e0a:ec7d
}
```
只需要在定义的 Struct 上增加对应的标签即可迅速的生成的 Fake 数据，目前支持超过 60 种标签，以下是部分示例。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230514214040069.png)


更多项目详情请查看如下链接。

开源项目地址：https://github.com/go-faker/faker 

开源项目作者：go-faker

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=go-faker/faker)



关注我们，一起探索有意思的开源项目。
