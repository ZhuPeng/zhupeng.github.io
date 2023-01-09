---
layout: post
title: GitHub 精选开源项目周刊第4期
tags: 每周精选
---

大家好，我是你们的章鱼猫。今天推送的是 GitHub 精选开源项目推荐周刊第 4 期，周刊内推荐的项目来自 GitHub 精选公众号粉丝的自荐，我们希望能够帮助更多的同学更好的开发和推广开源项目。

## 快点查查——微信小程序
**项目介绍：**

该小程序借助了腾讯位置、高德地图、和风天气、一言等提供的 API 服务。通过这类第三方服务接口，来为用户快速定位附近的公交、地铁、公厕、学校、景点、美食等任何关键信息，同时提供了天气查询、天气舒适度建议。另外附加了一点文学气息：页面刷新会显示随机经典古诗句哦！

**功能描述:**

1.快速定位附近的公交、地铁、公厕、学校、景点、美食、网咖等信息，并且提供文字导航和语音导航

2.实时查询当前位置的天气情况，并且提供穿衣指南、健身指南等温馨提示

3.页面刷新后会随机显示景点古诗词，还可以用来涨知识呢

扫描如下二维码试用

![image.png](https://cdn.nlark.com/yuque/0/2020/png/1285468/1590833904221-2385f9a7-5b53-45a5-9c9b-3c5ead9d105c.png)

**项目地址：**https://github.com/tomato-cc/wxmap

**项目作者：**https://github.com/tomato-cc

## react-visual-editor 可视化拖拽工具

**项目介绍：**

项目基于 React 组件之间的原始约束设计，不会添加多余 dom 节点，以组件可视化拖拽，嵌套形式，完全还原真实开发中页面代码的实现过程，组件可以自由拖拽嵌套，配合dom树与设计面板的实时交互，实现组件实时追踪，使设计面板快速响应你对组件的操作，所见即所得，可以完美还原 UI 设计搞，并支持多款型号手机（可配置），和 PC 效果展示，模板功能可以使你分享你的页面或者页面中局部任何部分组件组合，减少相似页面的重复操作，可以选择以 React 源码生成的形式生成页面代码，也可以以 JSON 动态更新的形式实现 noCode。

**功能描述：**

项目支持的功能特别多和全面。

- 现有功能描述

- - **任意拖拽嵌套**：通过组件预览面板拖拽组件，到设计面板实现任意嵌套，或者拖拽到DomTree中指定容器节点，DomTree与设计面板中的组件也可随意拖拽嵌套
  - **实时预览**：设计面板中会实时展示组件的属性效果和样式效果，并且与真实页面无异，所见即所得
  - **DomTree展示**：页面组件dom树的展示并实现组件dom实时追踪
  - **可视化属性配置**：结合React 特性和JS语法定制了可视化的组件属性配置，实现复杂数据结构的可视化配置
  - **可视化样式配置**：通过样式配置面板修改样式，实时在页面中显示样式效果
  - **模板功能**：可以选中局部或者整个页面做为可复用的模板，提高页面配置效率减少重复工作
  - **组件约束**：根据组件特性，可以配置组件的父组件约束与子组件约束，解决组件间的错误嵌套和报错
  - **预览与代码生成**：可随时预览页面的真实效果，和页面的jsx代码与样式代码
  - **多平台支持** ：支持PC与移动端多型号设配切换展示
  - **组件库替换**：通过简单的配置可以对接任何React组件库

- 新版功能(增加功能)

- - 组件调用方式：新版重构为react组件，可以简单的集成到任何项目中
  - **辅助线展示**：添加辅助线展示方便查看组件位置
  - **边距查看**：选中组件与hover组件之间各边的距离实时展示，方便UI还原
  - **选中组件拖拉改变大小**：选中的组件支持拖拉修改组件的宽高
  - **可视化样式配置**：通过样式配置面板修改样式，实时在页面中显示样式效果

![brickd1.gif](https://cdn.nlark.com/yuque/0/2020/gif/596944/1592617052301-897e982f-c7b5-4b50-a370-0cb9f14a66e2.gif)

![brickd1.gif](https://cdn.nlark.com/yuque/0/2020/gif/596944/1592617052301-897e982f-c7b5-4b50-a370-0cb9f14a66e2.gif)

![brickd3.gif](https://cdn.nlark.com/yuque/0/2020/gif/596944/1592617158295-32555724-d1ee-477e-b967-df74696fd7a9.gif)

**项目地址：**https://github.com/brick-design/react-visual-editor

**项目作者：**https://github.com/brick-design



## 通过程序生成中国山水画

**项目介绍：**

看看效果就知道牛不牛了~

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_shanshui-screen001.jpg)

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_shanshui-screen002.jpg)

**功能描述：**

通过程序生成可无限滚动的中国山水画，所有代码是通过 JavaScript 编写的，最终生成的山水画是 SVG 格式，非常清晰。

在线体验地址：http://shan-shui-inf.lingdong.works/

**项目地址：**https://github.com/LingDong-/shan-shui-inf

**项目作者：**https://github.com/LingDong-

## 桌面定时提醒开源软件
**项目介绍：**

程序员普遍有久坐的习惯，但是久坐有很多的不好的地方，具体哪里不好你懂得。所以定时的多走动走动是很有必要的，那么在电脑安装一个定时提醒软件就是一个不错的方法。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_stretchly-microbreak.png)

**功能描述：**

软件支持多个平台，比如 Mac、Windows。功能上支持设置提醒时长，暂时暂停当前提醒等。

**项目地址：**https://github.com/hovancik/stretchly

**项目作者：**https://github.com/hovancik

以上就是本次推荐的全部项目。GitHub精选 公众号致力于为大家分享和宣传优质的开源项目，让更多的人了解和知道，乃至去使用大家的开源项目，一方面可以帮助大家提高影响力，另外一方面还有助于大家收获更多粉丝的支持。如果你有开项目需要分享，欢迎点击 [共享文档](https://www.yuque.com/g/loonggg/febxd7/wvs0z6/collaborator/join?token=bVhhgBw5Rw0xM0Qj) 或底部阅读原文直接投稿分享。

**上期推荐：**

[GitHub 精选开源项目周刊第 3 期](https://mp.weixin.qq.com/s?__biz=MzA3MzE4ODY0Mg==&mid=2455985231&idx=1&sn=4a18dcb642075508eaac5a203ad90d63&chksm=88852802bff2a114d2007ae9b7e346c16b988d39c6d4491c3e2bd00b9aee9980bf655bc995bb&token=759885314&lang=zh_CN#rd)

[GitHub 精选开源项目周刊第 2 期](https://mp.weixin.qq.com/s?__biz=MzA3MzE4ODY0Mg==&mid=2455985136&idx=1&sn=2374645d303295d4802e1f9ed6444ad5&chksm=88852fbdbff2a6abb8820c84534103e05300b7f3449e89e983842c7455c85cc0ea16ed3d7d43&token=759885314&lang=zh_CN#rd)

[GitHub 精选开源项目周刊第 1 期](https://mp.weixin.qq.com/s?__biz=MzA3MzE4ODY0Mg==&mid=2455984989&idx=1&sn=aaec500b7374fd6dca20c539f0d6a8b7&chksm=88852f10bff2a606fd3da4bc6e177d4b02b1f8033adfd9a88ce718163947a0f576d2ffe7450a&token=148059737&lang=zh_CN#rd)

[GitHub 精选开源项目周刊第 0 期](https://mp.weixin.qq.com/s?__biz=MzA3MzE4ODY0Mg==&mid=2455984989&idx=2&sn=ff43140e282ebe3640d713113fabfa3e&chksm=88852f10bff2a60671b08bcec38f406e5cd7ce029f3b57b5af2abcaffb3ea8f0fa2d2bc609be&token=148059737&lang=zh_CN#rd)
