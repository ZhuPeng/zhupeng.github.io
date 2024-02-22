---
layout: post
title: GitHub 开源项目 Calcium-Ion/new-api 介绍，基于One API的二次开发版本，仅供个人管理渠道使用，请勿用于商业API分发！
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 Calcium-Ion/new-api，该项目在 GitHub 有差不多 1000 Star，用一句话介绍该项目就是：“基于One API的二次开发版本，仅供个人管理渠道使用，请勿用于商业API分发！”。



![image](https://github.com/Calcium-Ion/new-api/assets/61247483/ad0e7aae-0203-471c-9716-2d83768927d4)
![image](https://github.com/Calcium-Ion/new-api/assets/61247483/d1ac216e-0804-4105-9fdc-66b35022d861)
![image](https://github.com/Calcium-Ion/new-api/assets/61247483/3ca0b282-00ff-4c96-bf9d-e29ef615c605)
![image](https://github.com/Calcium-Ion/new-api/assets/61247483/f4f40ed4-8ccb-43d7-a580-90677827646d)
![image](https://github.com/Calcium-Ion/new-api/assets/61247483/90d7d763-6a77-4b36-9f76-2bb30f18583d)
![image](https://github.com/Calcium-Ion/new-api/assets/61247483/e414228a-3c35-429a-b298-6451d76d9032)
![image](https://github.com/Calcium-Ion/new-api/assets/61247483/1c66b593-bb9e-4757-9720-ff2759539242)
![image](https://github.com/Calcium-Ion/new-api/assets/61247483/5b3228e8-2556-44f7-97d6-4f8d8ee6effa)
![image](https://github.com/Calcium-Ion/new-api/assets/61247483/af9a07ee-5101-4b3d-8bd9-ae21a4fd7e9e)
![](https://github.com/Calcium-Ion/new-api/assets/61247483/de536a8a-0161-47a7-a0a2-66ef6de81266)



一、背景介绍：
在开发过程中，我们经常会遇到需要二次开发，以适应更复杂的功能需求的问题。这就需要我们具备扩展和修改现有开源项目的能力。然而，这并不是一件容易的事，其中的难题可能包括但不限于接口兼容性、数据一致性、新功能开发和旧功能保留等问题。而这个开源项目 "New API" 让这些问题变得更简单。

二、项目介绍：
"https://github.com/Calcium-Ion/new-api" 这是一个基于 "One API" 的二次开发项目。它拥有全新的 UI 界面，支持 Midjourney-Proxy 接口，还增加了在线充值和用 key 查询使用额度的功能，以便于二次分销。该项目还提供了渠道显示已使用额度，支持指定组织访问的功能，以及支持各种不同类型的模型选择和调用，在解决数据一致性问题上有了全新突破。同时，项目也增加了数据看板，提供了对数据进行实时监控的功能。

三、如何使用：
安装和使用项目非常简单，以下是使用 Docker 进行部署的命令：
```shell
# 使用 SQLite 的部署命令：
docker run --name new-api -d --restart always -p 3000:3000 -e TZ=Asia/Shanghai -v /home/ubuntu/data/new-api:/data calciumion/new-api:latest

# 使用 MySQL 的部署命令，在上面的基础上添加 `-e SQL_DSN="root:123456@tcp(localhost:3306)/oneapi"`，请自行修改数据库连接参数。例如：
docker run --name new-api -d --restart always -p 3000:3000 -e SQL_DSN="root:123456@tcp(localhost:3306)/oneapi" -e TZ=Asia/Shanghai -v /home/ubuntu/data/new-api:/data calciumion/new-api:latest
```
四、项目推介：
New API 在继承 One API 的优秀特性的同时，也在功能上做了许多有意义的扩展，比如充值系统、数据监控、模型调用和权重随机等，这些功能在实际开发中都有极大的实用价值。作者也提供了具体的接口文档和使用指南，方便二次开发。项目更新活跃，所以如果你正在寻找一个可以立即投入使用，同时又有一定扩展性的项目，New API 无疑是一个不错的选择。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=Calcium-Ion/new-api&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/Calcium-Ion/new-api 

开源项目作者：Calcium-Ion

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=Calcium-Ion/new-api)

关注我们，一起探索有意思的开源项目。

