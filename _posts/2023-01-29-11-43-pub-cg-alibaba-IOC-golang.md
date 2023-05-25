---
layout: post
title: Golang 依赖注入框架，帮助开发者构建 Go 应用
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 alibaba/IOC-golang，该项目在 GitHub 有超过 1k Star，用一句话介绍该项目就是：“一款服务于 Go 开发者的依赖注入框架，方便搭建任何 Go 应用。 A Golang depenedency injection framework, helps developers to build any go application.”。

![](https://raw.githubusercontent.com/ioc-golang/ioc-golang-website/main/resources/video/ioc-golang-demo.gif)

IOC-golang 是一个由阿里巴巴开源的 Go 语言实现的 Inversion of Control (IoC) 容器。该项目提供了一种简单的方法来管理依赖关系，使得应用程序的组件之间能够更加松耦合。它主要支持构造函数注入和 setter 注入两种方式，支持单例和多实例，支持依赖循环解决。通过使用 IOC-golang，可以使代码更加结构化，提高代码的可维护性和可测试性。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=alibaba/IOC-golang&type=Timeline)

### 如何安装使用

IOC-golang 是阿里巴巴开源的一个基于反射机制的 Golang 控制反转 (IOC) 容器，它支持构造函数注入和属性注入。

安装方式：

1. 使用 go get 命令安装：
```bash
go get -u github.com/alibaba/IOC-golang
```

2. 使用 go mod 安装：
```bash
require github.com/alibaba/IOC-golang v1.2.0
```

3. 使用 dep 安装：
```bash
dep ensure -add github.com/alibaba/IOC-golang
```

安装完成后，就可以在代码中通过 import 引入并使用该项目了。


### 使用示例 DEMO

以下是一个简单的 demo 代码，用于展示如何使用 IOC-golang 来管理依赖关系：

![](https://raw.githubusercontent.com/ioc-golang/ioc-golang-website/main/resources/img/ioc-golang-quickstart-structure.png)

对应代码如下：

```go
package main

import (
	"fmt"
	"time"

	"github.com/alibaba/ioc-golang"
)

// +ioc:autowire=true
// +ioc:autowire:type=singleton

type App struct {
	// inject main.ServiceImpl1 pointer to Service interface with proxy wrapper
	ServiceImpl1 Service `singleton:"main.ServiceImpl1"`

	// inject main.ServiceImpl2 pointer to Service interface with proxy wrapper
	ServiceImpl2 Service `singleton:"main.ServiceImpl2"`

	// inject ServiceImpl1 pointer to Service1 's own interface with proxy wrapper
	// this interface belongs to ServiceImpl1, there is no need to mark 'main.ServiceImpl1' in tag
	Service1OwnInterface ServiceImpl1IOCInterface `singleton:""`

	// inject ServiceStruct struct pointer
	ServiceStruct *ServiceStruct `singleton:""`
}

func (a *App) Run() {
	for {
		time.Sleep(time.Second * 3)
		fmt.Println(a.ServiceImpl1.GetHelloString("laurence"))
		fmt.Println(a.ServiceImpl2.GetHelloString("laurence"))

		fmt.Println(a.Service1OwnInterface.GetHelloString("laurence"))
		
		fmt.Println(a.ServiceStruct.GetString("laurence"))
	}
}

type Service interface {
	GetHelloString(string) string
}

// +ioc:autowire=true
// +ioc:autowire:type=singleton

type ServiceImpl1 struct {
}

func (s *ServiceImpl1) GetHelloString(name string) string {
	return fmt.Sprintf("This is ServiceImpl1, hello %s", name)
}

// +ioc:autowire=true
// +ioc:autowire:type=singleton

type ServiceImpl2 struct {
}

func (s *ServiceImpl2) GetHelloString(name string) string {
	return fmt.Sprintf("This is ServiceImpl2, hello %s", name)
}

// +ioc:autowire=true
// +ioc:autowire:type=singleton

type ServiceStruct struct {
}

func (s *ServiceStruct) GetString(name string) string {
	return fmt.Sprintf("This is ServiceStruct, hello %s", name)
}

func main() {
	// start to load all structs
	if err := ioc.Load(); err != nil {
		panic(err)
	}

	// Get Struct
	app, err := GetAppSingleton()
	if err != nil {
		panic(err)
	}
	app.Run()
}
```

通过如下方式运行代码：

```bash
% go mod init ioc-golang-demo
% export GOPROXY="https://goproxy.cn"
% go mod tidy
% go get github.com/alibaba/ioc-golang@master
% sudo iocli gen
```

会在当前目录生成：zz_generated.ioc.go，开发者无需关心这一文件，这一文件中就包含了上面使用的 GetAppSingleton 方法。执行程序后控制台打印输出如下，可看到，依赖注入成功，程序正常运行。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230401221542117.png)


更多项目详情请查看如下链接。

开源项目地址：https://github.com/alibaba/IOC-golang 

开源项目作者：alibaba

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=alibaba/IOC-golang)



关注我们，一起探索有意思的开源项目。
