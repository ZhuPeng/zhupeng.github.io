
大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 novuhq/novu，该项目在 GitHub 有超过 17.0k Star，用一句话介绍该项目就是：“The open-source notification infrastructure for products. Add a notification center for your React, Vue and Angular apps 🚀”。

![](https://user-images.githubusercontent.com/8872447/165779274-22a190da-3284-487e-bd1e-14983df12cbb.png)
![](https://user-images.githubusercontent.com/80174214/193887395-f1c95042-b4e6-480e-a89c-a78aa247fa90.gif)
![](https://contributors-img.web.app/image?repo=novuhq/novu)

novuhq/novu 是一个基于 JavaScript 的开源项目，它提供了一种简单而强大的方式来构建和管理现代 Web 应用程序。它使用了最新的 Web 技术，如 React 和 GraphQL，并结合了简单的命令行界面，使得开发人员能够快速上手并开始构建应用程序。项目提供了丰富的文档和示例，帮助开发人员了解如何使用它的各种功能。



### 如何安装使用

要安装 novuhq/novu 项目，您需要先确保安装了 Node.js 和 npm (Node.js 的包管理器)。然后，您可以在命令行中使用以下命令来安装 novu：
```
npm install -g @novu/cli
```
这将在全局安装 novu 命令行工具。

然后，您可以在任意文件夹中使用以下命令来创建一个新的 novu 项目：
```
novu create my-project
```
这将在当前文件夹中创建一个名为 "my-project" 的新项目。

安装完成后, 您可以通过运行以下命令来启动项目：
```
cd my-project
novu start
```
这将启动一个开发服务器，您可以在浏览器中访问 http://localhost:3000 来查看项目。


### 使用示例 DEMO

下面是一个简单的 novuhq/novu 项目示例，它展示了如何使用 React 和 GraphQL 构建一个简单的应用程序。

首先，使用以下命令来创建一个新的 novu 项目:
```
novu create my-project
```

然后，在项目目录中，您可以找到一个名为 `src` 的文件夹，这里存放着应用程序的源代码。

接下来，您可以在 `src` 文件夹中创建一个名为 `pages` 的文件夹，并在其中创建一个名为 `Home.js` 的文件。这个文件将是我们的主页组件.

```javascript
import React from 'react';

const Home = () => {
    return (
        <div>
            <h1>Welcome to my Novu Project!</h1>
        </div>
    );
};

export default Home;
```

最后，您可以在 `src/routes.js` 中导入并渲染 `Home` 组件。

```javascript
import React from 'react';
import { Router } from '@novu/router';
import Home from './pages/Home';

const routes = [
    {
        path: '/',
        component: Home,
        exact: true,
    },
];

export default function App() {
    return <Router routes={routes} />;
}
```

启动项目，在浏览器中访问 http://localhost:3000，您将会看到 "Welcome to my Novu Project!" 的文本.

这只是 novuhq/novu 的一个简单示例，它具有更多的功能，如支持 GraphQL, 路由, 状态管理等。最好的方法是查看官方文档以了解更多的细节.


更多项目详情请查看如下链接。

开源项目地址：https://github.com/novuhq/novu  (文末可点击阅读原文)

开源项目作者：novu

