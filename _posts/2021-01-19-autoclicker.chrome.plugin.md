---
layout: post
title: 超级易用，可自由定制的浏览器自动化插件
tags: 插件
---

今天给大家推荐一个超级牛逼的浏览器自动化插件 autoclicker，从我的体验来看，这个插件做的非常的易用。

简单介绍一下 autoclicker，它是通过 xpath 来定位浏览器中的按钮、输入框等元素，通过自动化的方式串联操作，实现超级简单易用的自动化。

autoclicker 是一个 Chrome 插件，安装完成之后，打开任意网页，可在你需要自动点击的地方右键会弹出 Auto Click / Auto Fill 选项。如下图：

![image-20210119122202606](https://7465-test-3c9b5e-books-1301492295.tcb.qcloud.la/images/compress_image-20210119122202606.png)

选择如上选项之后就会自动重定向到配置页。

![image-20210119122258003](https://7465-test-3c9b5e-books-1301492295.tcb.qcloud.la/images/compress_image-20210119122258003.png)

配置页会自动提取右键点击后的 xpath 并自动填充到 Action 配置中。之后刷新之前的网页，就会自动定位到 xpath 的元素并点击，从而实现了自动化。

从我自己的使用来看，因为我需要批量处理某个网页中的操作，所以涉及配置中的 Batch 操作，这时候需要打开右上角的 PRO 开关，batch 才能配置，否则配置项是置灰的。作者可能是希望这个工具能被更多的小白使用，从而对应这些 batch 的操作定义为 PRO，才会有这样的设定吧。

![image-20210119122530402](https://7465-test-3c9b5e-books-1301492295.tcb.qcloud.la/images/compress_image-20210119122530402.png)

其中参数 Init Wait 对应是网页加载后等待的时间，Repeat 为重复 Action 的次数，R-Interval 对应每次 Action 的间隔时间。

另外工具自动生成的 xpath 不是很智能，如果你懂一点 xpath 的知识的话，会让你更好的使用这个工具。

Chrome 插件安装地址：https://chrome.google.com/webstore/detail/auto-clicker-autofill/iapifmceeokikomajpccajhjpacjmibe?utm_source=chrome-ntp-icon

