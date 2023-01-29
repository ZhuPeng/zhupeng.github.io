---
layout: post
title: GitHub 开源项目 keyval-dev/odigos 介绍，Instant distributed traces without code changes. 🚀 Boost existing monitoring tools with higher-quality data
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 keyval-dev/odigos，该项目在 GitHub 有超过 0.8k Star，用一句话介绍该项目就是：“Instant distributed traces without code changes. 🚀 Boost existing monitoring tools with higher-quality data”。

![Supported Destinations](https://raw.githubusercontent.com/keyval-dev/odigos/master/assets/dests.png)
![](https://raw.githubusercontent.com/keyval-dev/odigos/master/assets/odigos.gif)

keyval-dev/odigos 是一个开源的、跨平台的、高性能的、简单易用的对象存储库。它提供了对象存储的基本功能，如上传、下载、删除等，并支持多种存储后端，如 Amazon S3、Google Cloud Storage、Minio 等。同时还可以使用自定义存储后端，支持跨平台。该项目使用简单易用的API,可以方便的使用对象存储功能。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=keyval-dev/odigos&type=Timeline)

### 如何安装使用

安装 keyval-dev/odigos 项目可以通过以下几种方式进行:

1. 通过 PIP 安装，使用命令 "pip install odigos" 安装。

2. 通过源码编译安装，在 GitHub 上下载源码并使用编译器进行编译安装。

3. 通过下载二进制文件安装，下载对应的二进制文件并执行安装。

在安装过程中还需要确保你已经安装了Python并且已经将Python加入了环境变量。

在使用这个库之前需要获取对应存储后端的凭证，配置信息请参考项目的文档。


### 使用示例 DEMO

以下是一份使用 keyval-dev/odigos 库上传文件到 Amazon S3 的示例代码：

```python
from odigo import S3, S3Client

# 设置Amazon S3凭证
access_key = '<your access key>'
secret_key = '<your secret key>'

# 创建S3客户端
s3 = S3Client(S3, access_key=access_key, secret_key=secret_key)

# 上传文件
s3.put_object(bucket='<your bucket>', key='<object key>', data=b'Hello World!')

# 下载文件
data = s3.get_object(bucket='<your bucket>', key='<object key>')
print(data)

# 删除文件
s3.delete_object(bucket='<your bucket>', key='<object key>')
```
请注意，您需要替换示例代码中的“<your access key>”，“<your secret key>”，“<your bucket>”和“<object key>”为您的凭证和实际的存储桶和对象键。

还可以查看项目文档中的其他使用示例，如上传流，文件和字符串，等。


更多项目详情请查看如下链接。

开源项目地址：https://github.com/keyval-dev/odigos 

开源项目作者：keyval-dev

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=keyval-dev/odigos)

