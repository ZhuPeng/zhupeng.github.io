---
layout: post
title: 用于快速搭建通知中心的开源基础设施
tags: 前端
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 novuhq/novu，该项目在 GitHub 有超过 17.0k Star，用一句话介绍该项目就是：“The open-source notification infrastructure for products. Add a notification center for your React, Vue and Angular apps 🚀”，用于快速搭建通知中心的开源基础设施。

![](https://user-images.githubusercontent.com/8872447/165779274-22a190da-3284-487e-bd1e-14983df12cbb.png)

novuhq/novu 是一个基于 JavaScript 的开源项目，它提供了一种简单而强大的方式来构建和管理现代 Web 应用程序。它使用了最新的 Web 技术，如 React 和 GraphQL，并结合了简单的命令行界面，使得开发人员能够快速上手并开始构建应用程序。项目提供了丰富的文档和示例，帮助开发人员了解如何使用它的各种功能。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230201214147501.png)

novu 提供了很多丰富的功能，上手也非常的简单。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230201214339878.png)

通过如下简单的示例就可以实现一个简单的消息通知。

安装：

```bash
npx novu init
npm install @novu/node
```

示例代码：

```javascript
import { Novu } from '@novu/node';

const novu = new Novu(process.env.NOVU_API_KEY);

await novu.trigger('<TRIGGER_NAME>', {
  to: [
    {
      subscriberId: '<UNIQUE_IDENTIFIER>',
      email: 'john1@doemail.com',
      firstName: 'John',
      lastName: 'Doe',
    },
  ],
  payload: {
    name: 'Hello World',
    organization: {
      logo: 'https://happycorp.com/logo.png',
    },
  },
});
```


更多项目详情请查看如下链接。

开源项目地址：https://github.com/novuhq/novu  (文末可点击阅读原文)

开源项目作者：novu

非常多的开源作者参与其中：

![](https://contributors-img.web.app/image?repo=novuhq/novu)



关注我们，一起探索有意思的开源项目。
