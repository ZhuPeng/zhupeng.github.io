---
layout: post
title: 自动修复代码仓库中的错误配置和安全风险的工具推荐，越早用越好
tags: Go 安全
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 Legit-Labs/legitify，用一句话介绍该项目就是：“Detect and remediate misconfigurations and security risks across all your GitHub and GitLab assets”，自动对 GitHub 和 GitLab 代码资产中的错误配置和安全风险进行检测和修复。

![](https://user-images.githubusercontent.com/74864790/174815311-746a0c98-9a1f-44a9-808c-035788edfd4d.png)

legitify 支持如下检测类别，对于公开和私有仓库有部分的区分。从支持的类别看，如果你的代码仓库存在这些风险和错误配置还是非常值得修复的，毕竟任何的错误在仓库存在的时间越长，修复的代价就会越大，所以越早修复越好。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230218202454597.png)

以下是 legitify 使用 DEMO：

<iframe width="100%" height="400" src="https://user-images.githubusercontent.com/107790206/210602039-2d022692-87ea-4005-b9c6-f091158de3ce.mov" frameborder="0" allowfullscreen></iframe>

### 如何安装使用

legitify 项目使用 Go 开发，所以直接 clone 代码编译即可开始使用。

```bash
git clone git@github.com:Legit-Labs/legitify.git
go run main.go analyze ...
```


### 使用示例 DEMO

legitify 是一个命令行程序，因为要访问 GitHub 和 GitLab 的数据，所以唯一需要的就是对应的 GitHub 和 GitLab 的 API TOKEN。具体使用如下：

```bash
LEGITIFY_TOKEN=<your_token> legitify analyze
```

同时也可以设置需要扫描检测的仓库、组织等。

```bash
LEGITIFY_TOKEN=<your_token> legitify analyze --org org1,org2 --namespace organization,member
```

更多参数参考如下：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230218203216991.png)

分析的结果示例输出如下，最后会有一个总结性的表格。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230218203517545.png)

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230218203452186.png)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/Legit-Labs/legitify 

开源项目作者：Legit-Labs

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=Legit-Labs/legitify)



关注我们，一起探索有意思的开源项目。
