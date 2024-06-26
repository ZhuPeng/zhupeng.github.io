---
layout: post
title: GitHub 新项目！快速生成接口文档和模拟数据，开发联调效率杠杠滴
tags: 投稿
---

说起前后端，避免不了一系列的协作问题，包括但不限于接口没有及时给出、文档没有及时编写、接口写好后又时好时坏、系统未完成造数据困难……

## 先评估现在常见的解决方案
直接在用到的地方写死数据。例如直接把数据写到模版上，或者变量值的声明位置，或者一个 json 文件。
- 优点
  - 简单
  - 见效快
- 缺点
  - 死数据，编写麻烦
  - 可维护性差
  - 造成大量冗余代码

项目代码内分模块编写 mock 代码。例如创建专门的 mock 目录，使用 mockjs 进入 ajax 拦截实现接口和数据模拟。要对于上一个方案而言，造数据容易得多，并且减少了代码入侵。
- 优点
  - 外置依赖最小
- 缺点
  - 解耦性差
  - 浏览器看不见请求
  - 不支持文件流

自己实现一个服务端。例如使用 express 这些接口库，专门开一个项目来做接口模拟，这要求有一定的额外知识储备。
- 优点
  - 定制性最强
- 缺点
  - 需要额外维护一个项目
  - 需要自己开发对应的数据生成及其他功能

使用在线的模拟平台，例如一些在线 mock 服务。
- 优点
  - 交互良好，多人协作
- 缺点
  -  api 路径定制性差
  -  或有数据敏感风险
  -  不支持离线开发
  -  不支持文件流
  
## 关于 mockm 能给到的
- 小巧易用
  - 安装包 430KB，解包大小 1.79 MB
  - npm 一键安装，跨平台使用
  - 支持 UI 界面操作

- 接口自动创建
  - 支持 Restful API，给一个对象即可生成增删改查一系列接口
  - 支持 WebSocket 实时通讯
  - 支持文件流，例如上传，下载
  
- 数据生成
  - 支持使用 Mockjs 语法
  - 经过增强和优化的 Mockjs 语法
  - 支持使用原生 js 写数据 (数据类型选择为 eval 即可)
  - 支持批量自动翻译和转换
  - 支持声明类型和描述
  
- 辅助调试
  - 支持保存请求记录
  - 支持请求重放，编辑
  - 支持精简版 postman
  - 自动带参调试，无需登录
  - 支持自动允许跨域
  - 支持 api 拦截，注入，响应修改
  - 支持远程调试，一个属性完成内网穿透，无需花生壳，nginx，无需注册账号
  
- 辅助开发
  - 开源免费
  - 高可定制
  - 开放配置，直接支持 nodejs 相关生态
  - 修改实时生效
  
- 辅助部署
  - 数据和配置可移植
  - 自带进程守护

看起来比较抽象，简单来说 mockm 是一个跨平台，前后端可用的接口工具，类似一个便捷的服务端模拟服务，然后附带一些联调接口时会用到的功能，例如精简版 postman，可以自动带 token 调试接口，无需担心帐号被挤，请求信息可重放和可查阅。

由于是一个服务端的实现，支持更多的模拟场景，例如文件的上传下载、静态资源访问、WebSocket实时通讯，接口代理和拦截……经过封装，很简单就能实现所要模拟的接口。

以下是一些示例。

## 创建 API
``` js
api: {
  // 创建一个不区分 http 方法的接口，返回 hello
  '/api/1': `hello`,
  // 创建一个 post 方法的接口, 并返回接收到的值
  'post /api/2' (req, res) {
    res.json({desc: `你传入的值`, data: req.query}) // req.query 是 url 上的查询参数
  },
  // 创建一个 websocket 接口，并返回收到的消息
  'ws /api/3' (ws) {
    ws.on('message', msg => ws.send(msg))
  }
},
```

## 从文本批量转换为接口和数据

为了方便快速造数据，可以 `从文本批量转换为接口和数据`，假设有这样一个接口: `/api/user`，只需给出以下格式的内容:

```
昵称
邮箱
头像
孩子
- 年龄
- 出生日期
- 手机号
```

会自动转换为：

![文档](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_y4FYWt.png)

然后访问接口返回：

![响应](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_y4kTHg.png)

当然，响应的格式是完全可以自定义的。如果觉得这个功能比较鸡肋，也可以看看其他功能。

## 快速生成 Restful API
假设我要写一个博客文章的列表，并且要实现添加文章、查询文章、分页、模糊搜索、删除、修改等各种功能的接口。那么只需添加以下内容：

``` js
module.exports = {
  db: {
    'blogs': [
      {
        id: 1,
        content: `mockm 是一款便于使用，功能灵活的接口工具. 看起来不错~`,
        title: `认识 mockm 的第一天`,
      },
    ],
  },
}

```

这时候上面要实现的所有接口已经实现了。
这里我用 http 作为请求工具简单表示几个功能，你可以使用你喜欢的工具发送请求。

``` sh
# 查看 id 为 1 的博文详情
http :9000/blogs/1

# 创建一篇关于同事的文章
http post :9000/blogs title=同事的一天 content=今天他的生活还是同样的苦涩

# 获取所有文章
http :9000/blogs

# 查询所有含有 `苦涩` 的文章
http :9000/blogs?q=苦涩

# 更多示例省略...
```

## 附
- GitHub：https://github.com/wll8/mockm
- 文档：https://hongqiye.com/doc/mockm
