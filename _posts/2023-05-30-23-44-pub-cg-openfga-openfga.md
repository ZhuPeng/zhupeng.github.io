---
layout: post
title: 受 Google Zanzibar 启发，一个为开发人员构建的高性能、灵活的授权/权限引擎
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

## 背景介绍

在开发过程中，我们经常会遇到权限管理的问题。而这个问题正是 OpenFGA 项目正在解决的。OpenFGA 旨在为开发人员提供一种简单的方式来建模应用程序权限，并将细粒度的授权集成到应用程序中。它能够快速进行内存数据存储以支持快速开发，并提供可插拔的数据库模块。目前，它支持 PostgreSQL 14 和 MySQL 8 两种数据库。

该项目在 GitHub 有超过 1.1k Star，用一句话介绍该项目就是：“A high performance and flexible authorization/permission engine built for developers and inspired by Google Zanzibar”，一个为开发人员构建的高性能、灵活的授权/权限引擎，受 Google Zanzibar 启发。

## 项目介绍

OpenFGA 提供了以下主要功能和设计要点：

- 高性能和灵活的授权/权限引擎。
- 受 Google Zanzibar 启发，为开发人员提供模型化应用程序权限的简便方式。
- 支持内存数据存储和可插拔的数据库模块。
- 提供 HTTP API 和 gRPC API 接口。
- 提供多种语言的 SDK，包括 Node.js/JavaScript、GoLang、Python 和 .NET。，请查看社区项目 https://github.com/openfga/community#community-projects 了解更多第三方 SDK 和工具。

## 示例代码

您可以参考以下代码示例来使用 OpenFGA：

```python
import openfga_sdk
from openfga_sdk.client import OpenFgaClient


async def main():
    configuration = openfga_sdk.ClientConfiguration(
        api_scheme = OPENFGA_API_SCHEME, # optional, defaults to "https"
        api_host = OPENFGA_API_HOST, # required, define without the scheme (e.g. api.fga.example instead of https://api.fga.example)
        store_id = OPENFGA_STORE_ID, # optional, not needed when calling `CreateStore` or `ListStores`
        authorization_model_id = OPENFGA_AUTHORIZATION_MODEL_ID, # Optional, can be overridden per request
    )
    # Enter a context with an instance of the OpenFgaClient
    async with OpenFgaClient(configuration) as fga_client:
        api_response = await fga_client.read_authorization_models()
        await fga_client.close()

```

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=openfga/openfga&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/openfga/openfga 

开源项目作者：openfga

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=openfga/openfga)

关注我们，一起探索有意思的开源项目。