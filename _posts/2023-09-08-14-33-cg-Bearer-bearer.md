---
layout: post
title: GitHub 开源项目 Bearer/bearer 介绍，Code security scanning tool (SAST) to discover, filter and prioritize security and privacy risks.
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 Bearer/bearer，该项目在 GitHub 有超过 1.3k Star，用一句话介绍该项目就是：“Code security scanning tool (SAST) to discover, filter and prioritize security and privacy risks.”。


![](https://raw.githubusercontent.com/Bearer/bearer/master/./docs/assets/img/bearer-logo-light.svg)





背景介绍：
在当今的互联网时代，数据安全和隐私保护的重要性不言而喻。然而，随着开发语言和框架的多样化，开发者在编写代码时可能会无意中引入安全风险和隐私泄露的问题，如路径遍历、开放重定向、敏感信息暴露、SQL 注入、输入验证、XSS、XPath 等问题。这些问题可能会导致严重的数据泄露和系统安全风险。

项目介绍：
Bearer CLI 是一个静态应用安全测试（SAST）工具，它可以扫描你的源代码，分析你的数据流，以发现、过滤和优先处理安全和隐私风险。目前支持 JavaScript、TypeScript、Ruby 和 Java 技术栈，PHP 的 Beta 版本也即将推出。

Bearer CLI 可以扫描你的源代码以发现：
- 使用内置规则覆盖 OWASP Top 10 和 CWE Top 25 的安全风险和漏洞，例如：访问控制、加密失败、注入、设计、安全配置错误、身份验证和认证失败、数据完整性失败、安全日志和监控失败、服务器端请求伪造（SSRF）等。
- 具有检测敏感数据流的能力，例如你的应用中的 PII、PHI 的使用，以及处理敏感数据的组件（例如 pgSQL 数据库，第三方 API 如 OpenAI、Sentry 等）。这有助于生成与隐私影响评估（PIA）、数据保护影响评估（DPIA）、GDPR 合规报告的处理活动记录（RoPA）输入相关的隐私报告。

如何使用：
安装 Bearer CLI 的最快方式是使用安装脚本，它会自动选择最适合你的架构的构建。默认安装到 ./bin 并使用最新的发布版本：curl -sfL https://raw.githubusercontent.com/Bearer/bearer/

项目推介：
Bearer CLI 项目开发活跃，作者具有丰富的安全领域经验。它不仅可以帮助开发者提前发现和修复代码中的安全风险，还能帮助企业更好地满足数据隐私保护的合规要求。如果你是一名关注代码安全和隐私保护的开发者，或者你的公司需要一个强大的代码安全扫描工具，那么 Bearer CLI 无疑是一个值得你关注和尝试的项目。



以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=Bearer/bearer&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/Bearer/bearer 

开源项目作者：Bearer

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=Bearer/bearer)

关注我们，一起探索有意思的开源项目。