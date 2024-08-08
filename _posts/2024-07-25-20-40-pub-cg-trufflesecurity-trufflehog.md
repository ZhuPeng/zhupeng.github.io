---
layout: post
title: 敏感信息泄露自动化扫描工具
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

企业和个人越来越依赖于各种在线平台来存储和管理数据，其中包括敏感信息。然而，这些敏感信息（比如凭证、密钥和访问令牌）时常因疏忽而被泄露到公共仓库如 GitHub 上。一旦这些敏感信息被恶意用户发现，便可能对公司或个人造成巨大的安全威胁和财务损失。因此，检测和预防敏感信息泄露成为了企业和开发者亟需解决的问题。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-30a455b9ea08b1527edfa9d28e60c305.png)

今天要给大家推荐一个 GitHub 开源项目 trufflehog，该项目在 GitHub 有超过 14.6k Star。

![](https://stats.deeptrain.net/repo/trufflesecurity/trufflehog/?theme=light)

一句话介绍该项目：Find and verify secrets

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240801220638406.png)

###### 项目介绍

TruffleHog 专注于发现和验证 Git 仓库中泄露的凭证和敏感信息。通过深度扫描代码历史记录和实时监测，TruffleHog 能够有效地识别出各类编码格式中的秘密信息，包括简单文本、散列值和令牌。它支持多种扫描模式，包括对指定仓库的扫描、组织层面的扫描，以及输出扫描结果为 JSON 格式等。此外，TruffleHog 能够只筛选出已验证的秘密，有效减少误报。通过这些功能，开发者和企业可以大大降低潜在的信息安全风险。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240801220737579.png)

###### 如何使用

1、安装 TruffleHog

MacOS 用户：
```bash
brew install trufflehog
```

使用 Docker：
```bash
docker run --rm -it -v "$PWD:/pwd" trufflesecurity/trufflehog:latest github --repo https://github.com/trufflesecurity/test_keys
```

源码编译：
```bash
git clone https://github.com/trufflesecurity/trufflehog.git
cd trufflehog; go install
```

2、快速开始

扫描一个仓库以寻找已验证的秘密：
```bash
trufflehog git https://github.com/trufflesecurity/test_keys --only-verified
```

![](https://storage.googleapis.com/truffle-demos/non-interactive.svg)

###### 项目推介

TruffleHog 是由专注于安全工具开发的 **Truffle Security** 团队创建和维护的。自从项目启动以来，它已经受到了开发社区的广泛认可和使用，包括一些知名公司和组织。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240801220916960.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=trufflesecurity/trufflehog&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/trufflesecurity/trufflehog 

开源项目作者：trufflesecurity

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=trufflesecurity/trufflehog)

关注我们，一起探索有意思的开源项目。

