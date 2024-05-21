---
layout: post
title: GitHub 开源项目 SawyerHood/draw-a-ui 介绍，Draw a mockup and generate html for it
tags: 
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 SawyerHood/draw-a-ui，该项目在 GitHub 有超过 12.9k Star。

![](https://stats.deeptrain.net/repo/SawyerHood/draw-a-ui/?theme=light)

一句话介绍该项目：Draw a mockup and generate html for it




![A demo of the app](https://raw.githubusercontent.com/SawyerHood/draw-a-ui/master/./demo.gif)


###### 项目介绍

### **背景介绍**
在当今快速发展的互联网时代，网页设计和开发是一个不断进化的领域。设计师和前端开发者们经常面临一个共同的挑战：如何快速、高效地将概念化的设计草图转化为实际可用的 HTML 代码。这一过程不仅耗时而且容易出错，尤其是在将复杂的设计想法具体实现时。在初步设计阶段，往往需要频繁地修改和调整，如果每一次修改都需要手动编写代码，无疑会大大拖慢项目的进度，增加项目成本。

### **

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-c3923a4aac1989a0f69ff35d2f3c79b1.png)

项目介绍**
面对上述挑战，[draw-a-ui](https://github.com/SawyerHood/draw-a-ui) 应用应运而生。这个项目基于 tldraw 和 gpt-4-vision api，旨在通过用户绘制的线框图自动生成 HTML 代码。用户只需绘制一个模拟界面的草图，`draw-a-ui` 就能将其转换为配备 Tailwind CSS 的 HTML 文件，极大缩短从设计到开发的时间。项目目前尚处于开发阶段，但核心功能——将绘图画布的 SVG 转换为 PNG，再将该 PNG 传送给 gpt-4-vision 以指令形式返回单个 HTML 文件——已经完善并开源。

### **如何使用**
首先，您需要有一个 OpenAI API 密钥，并确保它有访问 GPT-4 Vision API 的权限。只需按照以下步骤操作即可轻松设置和运行 `draw-a-ui`:

1. 克隆项目到本地
2. 在项目的根目录下创建 `.env.local` 文件，并添加您的 OpenAI API 密钥，如下所示：
   ```bash
   echo "OPENAI_API_KEY=sk-your-key" > .env.local
   ```
3. 安装依赖并启动项目：
   ```bash
   npm install
   npm run dev
   ```
4. 通过浏览器打开 [http://localhost:3000](http://localhost:3000) 查看结果。

### **项目推介**
尽管目前 `draw-a-ui` 项目标注为演示用途，并不建议在生产环境中直接使用，但其背后的理念和技术实现无疑展现了未来开发的趋势。该项目利用最新的人工智能技术（如 GPT-4），为前端开发带来了革命性的工作模式改变。

目前，该项目的作者正在开发一个托管版，并鼓励用户加入等待列表，表明了其未来商用的可能性和潜力。虽然 `draw-a-ui` 目前尚处于早期阶段，但它为设计和开发工作流程提供了一个全新的视角，特别适合那些愿意尝试新技术、寻找提升工作效率方法的开发者和设计师。

此外，考虑到项目采用的开源模式，它也提供了一个很好的学习平台，让感兴趣的开发者可以深入了解如何将先进的人工智能技术应用到实际项目中。无论是作为技术研究，还是作为提升个人和团队开发效率的工具，`draw-a-ui` 都值得关注和尝试。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=SawyerHood/draw-a-ui&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/SawyerHood/draw-a-ui 

开源项目作者：SawyerHood

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=SawyerHood/draw-a-ui)

关注我们，一起探索有意思的开源项目。

