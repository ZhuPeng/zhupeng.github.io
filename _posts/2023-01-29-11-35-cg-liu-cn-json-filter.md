---
layout: post
title: Go 语言 JSON 过滤器，让结构体中的数据字段按需使用
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 liu-cn/json-filter，该项目在 GitHub 有超过 100 Star，用一句话介绍该项目就是：Golang 的 JSON 字段过滤器，随意选择你想要输出为 JSON 的结构体字段，让 Go 拥有动态语言般的 JSON 处理能力。

json-filter 是一个用于过滤、查询和操作 JSON 数据的库。该库提供了一种类似于 SQL 的语法来查询 JSON 数据，可以帮助开发人员轻松地提取和操作 JSON 数据。它提供了一组简单易用的函数，可以帮助开发人员在 JSON 数据中进行筛选和选择。

在实际编程开发过程中，往往一个结构体会被多个使用场景引用，但是不同场景暴露的数据字段又不太一样，为了不重复定义多个数据结构增加维护成本，同时又不想在不同场景暴露出其他不需要的字段，那有什么好办法吗？如果你也有以上问题，或许可以尝试用 json-filter 的过滤器来过滤你想要的字段吧， 不仅简单，更重要的是很强大，很复杂的结构体也可以过滤出你想要的字段。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=liu-cn/json-filter&type=Timeline)

### 如何安装使用

liu-cn/json-filter 作为一个 Go 语言开发的库，可以通过 go get 命令安装。

在命令行中输入以下命令，即可安装 json-filter 库：

```
go get -u github.com/liu-cn/json-filter
```

这样就可以在你的项目中引用 json-filter 库了。在代码中导入：
```
import "github.com/liu-cn/json-filter"
```

接下来可以使用 json-filter 库中提供的函数和方法来处理 JSON 数据。


### 使用示例 DEMO

这是一个使用 json-filter 库来过滤 JSON 数据的示例代码：

```go
package main

import (
	"encoding/json"
	"fmt"
	"time"

	"github.com/liu-cn/json-filter/filter"
)

//同一个结构体，你可能想要在article 接口下只返回UID Avatar Nickname这三个字段就够了，其他字段不想要暴露
//另外你还想在profile 接口下返回 Nickname Sex VipEndTime Price 这四个字段，其他字段不想暴露
//这样的情况有很多，想要复用一个结构体来随心所欲的构造自己想要的json数据结构，可以看一个简单的demo

type User struct {
	UID    uint   `json:"uid,select(article)"`    //select中表示选中的场景(该字段将会使用到的场景)
	Avatar string `json:"avatar,select(article)"` //和上面一样此字段在article接口时才会解析该字段

	Nickname string `json:"nickname,select(article|profile)"` //"｜"表示有多个场景都需要这个字段 article接口需要 profile接口也需要

	Sex        int       `json:"sex,select(profile)"`          //该字段是仅仅profile才使用
	VipEndTime time.Time `json:"vip_end_time,select(profile)"` //同上
	Price      string    `json:"price,select(profile)"`        //同上
}

func main() {

	user := User{
		UID:        1,
		Nickname:   "boyan",
		Avatar:     "avatar",
		Sex:        1,
		VipEndTime: time.Now().Add(time.Hour * 24 * 365),
		Price:      "999.9",
	}

	marshal, err := json.Marshal(user)
	if err != nil {
		panic(err)
	}
	fmt.Println(string(marshal)) //以下是官方的json解析输出结果：可以看到所有的字段都被解析了出来
	//{"uid":1,"nickname":"boyan","avatar":"avatar","sex":1,"vip_end_time":"2023-03-06T23:11:22.622693+08:00","price":"999.9"}

	//用法：filter.Select("select里的一个场景",这里可以是slice/array/struct/pointer/map)
	article:=filter.Select("article", user)
	articleBytes, _ := json.Marshal(article)
	fmt.Println(string(articleBytes)) //以下是通过json-filter 过滤后的json，此输出是article接口下的json
	//{"avatar":"avatar","nickname":"boyan","uid":1}
	
  //filter.Select fmt打印的时候会自动打印过滤后的json字符串
	fmt.Println(filter.Select("article", user)) //以下是通过json-filter 过滤后的json，此输出是article接口下的json
	//{"avatar":"avatar","nickname":"boyan","uid":1}

	fmt.Println(filter.Select("profile", user)) //profile接口下
	//{"nickname":"boyan","price":"999.9","sex":1,"vip_end_time":"2023-03-06T23:31:28.636529+08:00"}
}
```


更多项目详情请查看如下链接。

开源项目地址：https://github.com/liu-cn/json-filter 

开源项目作者：liu-cn

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=liu-cn/json-filter)

