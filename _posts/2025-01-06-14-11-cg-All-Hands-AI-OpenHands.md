---
layout: post
title: GitHub 开源项目 All-Hands-AI/OpenHands 介绍，🙌 OpenHands: Code Less, Make More
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 All-Hands-AI/OpenHands，该项目在 GitHub 有超过 40.6k Star。

![](https://stats.deeptrain.net/repo/All-Hands-AI/OpenHands/?theme=light)

一句话介绍该项目：🙌 OpenHands: Code Less, Make More




![App screenshot](https://raw.githubusercontent.com/All-Hands-AI/OpenHands/master/./docs/static/img/screenshot.png)

![](https://raw.githubusercontent.com/All-Hands-AI/OpenHands/master/./docs/static/img/logo.png)


###### 项目介绍

在当今快速演变的软件开发领域中，开发者面临着代码编写、调试、集成新技术等方面的重大挑战。这些挑战常常导致效率下降，创新受阻。在这样的背景下，一个能够大幅提高开发者生产力、简化软件开发过程的开源工具，显得尤为宝贵。🙌 OpenHands 就是针对这一需求应运而生的项目。

🙌 OpenHands 是一个由人工智能驱动的软件开发助手平台。它致力于通过自动化常见的开发任务，如修改代码、运行命令、浏览网页、调用 API 甚至从 StackOverflow 复制代码片段，来帮助开发者 "Code Less, Make More"。用户可以通过 Docker 容器非常轻松地启用和运行 OpenHands，可见其启动过程与使用门槛都被大大简化。

### 如何使用：

安装 OpenHands 的最快方式是通过 Docker。只需要按照以下步骤执行：

```bash
docker pull docker.all-hands.dev/all-hands-ai/runtime:0.18-nikolaik

docker run -it --rm --pull=always \
    -e SANDBOX_RUNTIME_CONTAINER_IMAGE=docker.all-hands.dev/all-hands-ai/runtime:0.18-nikolaik \
    -e LOG_ALL_EVENTS=true \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v ~/.openhands-state:/.openhands-state \
    -p 3000:3000 \
    --add-host host.docker.internal:host-gateway \
    --name openhands-app \
    docker.all-hands.dev/all-hands-ai/openhands:0.18
```

运行后，OpenHands 将在 [http://localhost:3000](http://localhost:3000) 上启动可供使用。

### 项目推介：

自项目启动以来，🙌 OpenHands 经过社区的不断贡献与完善，已展现出强大的生命力。由于其面向未来的设计，即使在极其竞争激烈的开源社区中，它依然保持着活跃的开发状态。该项目不仅吸引了众多开发者的兴趣，也受到了行业内知名人士的高度评价。更重要的是，它利用最前沿的人工智能技术，真正为软件开发领域带来了翻天覆地的变革。

OpenHands 不仅是一个工具，它代表了一个广泛的、活跃的社区，这个社区致力于分享知识、经验和代码，以推动软件开发领域的进步。该项目的设计哲学、用户体验设计以及对未来软件开发形态的预见，都显示了其作为开源项目的独特价值和重要性。

加入到 OpenHands 社区，无论是通过 Slack、Discord 还是 GitHub 进行交流，都将使你与志同道合的开发者相聚，不断探索 OpenHands 带来的无限可能。无论你是想对代码进行微小的更改，还是希望参与到项目的核心开发中，OpenHands 社区都将为你提供一个支持和成长的平台。

在使用开源项目时，常常担心项目的持续维护与更新。但对于 OpenHands 而言，其背后强大的社区支持、活跃的开发进展以及开放的沟通渠道，都保证了这一项目不仅能够持续进步，还能够不断适应行业的新需求、新挑战。通过 OpenHands，我们可以真正实

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=All-Hands-AI/OpenHands&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/All-Hands-AI/OpenHands 

开源项目作者：All-Hands-AI

开源协议：MIT License

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=All-Hands-AI/OpenHands)

关注我们，一起探索有意思的开源项目。

