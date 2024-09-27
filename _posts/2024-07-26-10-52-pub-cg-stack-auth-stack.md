---
layout: post
title: 面向开发者的全面身份验证解决方案
tags: 
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

无论是小团队还是大型企业，在开发新的应用程序时都会遇到一个普遍但却棘手的问题：**用户认证与管理**。这个看似简单的需求，实际上包含了大量的挑战，比如安全的用户数据存储、第三方登录集成（如 Google、Facebook 或 GitHub）、用户权限管理等。这不仅耗费开发资源，也显著增加了项目的初期投入。对于许多团队来说，如何快速、高效地解决这个问题成为了能否顺利推进项目的关键。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-59e5e4344ed1502df298d523b0f682c3.png)

今天要给大家推荐一个 GitHub 开源项目 stack-auth，该项目在 GitHub 有超过 3.1k Star。

![](https://stats.deeptrain.net/repo/stack-auth/stack/?theme=light)

一句话介绍该项目：Open-source Clerk/Auth0 alternative

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240804213821668.png)


###### 项目介绍

Stack 是一个开源、自托管且高度可定制的身份验证和用户管理系统，提供了一套完整的前后端解决方案，特别适合 Next.js、React 和 JavaScript 项目。通过 Stack，开发者可以在不到一分钟的时间内搭建起一个功能强大的认证系统，轻松实现如 OAuth 第三方登录、邮箱链接和密码登录认证等常见需求，同时还支持用户管理、团队权限设置以及深度自定义界面，支持暗黑模式/明亮模式等多种现代网页设计要求。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240804213935611.png)

###### 如何使用

Stack 的安装过程极为简单。首先，确保你的项目是基于 Next.js：

1、创建一个 Next.js 项目（如果尚未创建）:

```bash
npx create-next-app your-project-name
cd your-project-name
```

2、安装 Stack：

```bash
npm install @stackframe/stack
```

安装命令执行后，你将被引导完成安装过程。进一步的配置和使用，可以参考官方文档 [Document](https://docs.stack-auth.com)。

3、开始使用 Stack 构建你的应用程序，享受快速、灵活的开发体验。

```javascript
// stack.ts
import "server-only";
import { StackServerApp } from "@stackframe/stack";

export const stackServerApp = new StackServerApp({
  tokenStore: "nextjs-cookie", // storing auth tokens in cookies
  //there is other parameter named "urls" which is covered later in the docs
});

// page.tsx
import { StackHandler } from "@stackframe/stack";
import { stackServerApp } from "@/stack";

export default function Handler(props: any) {
  return <StackHandler fullPage app={stackServerApp} {...props} />;
}
```

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240804214230095.png)

###### 项目推介

**Stack** 正因其开源、高度可定制的特点，以及快速部署的能力，受到了众多开发者的青睐。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240804214355665.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=stack-auth/stack&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/stack-auth/stack 

开源项目作者：stack-auth

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=stack-auth/stack)

关注我们，一起探索有意思的开源项目。

