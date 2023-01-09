---
layout: post
title: 支持本地搭建的个人相册应用
tags: 相册
---

大家好。

使用智能相机这么多年了，相信大家肯定有不少照片吧，尤其是还玩摄影的肯定更加的多。这些照片是不是都是放在某个硬盘里面，很少会再去翻看了，有很大一部分原因是查看起来非常的不方便。对我来说，有两个问题：1、照片普遍都比较大，系统默认预览看起来非常的慢；2、照片只有时间信息，缺少一些照片的元信息，查找起来非常的麻烦。

今天要推荐的开源项目 PhotoView，是一款能够在本地自己搭建的个人相册，PhotoView 会基于你硬盘中的照片，自动生成缩略图，让你浏览起来非常的快速。除此之外，PhotoView 还会基于图片的信息，自动生成基于时间、地点、人物对照片进行聚合，其中基于人物的聚合非常有意思，意味着可以找到照片中相同人脸的照片，虽然准确率可能不太高，但是也非常的有用了。

接下来我们简单看看 PhotoView 的使用界面。

基于时间线聚合图片：

![image-20220313205849577](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220313205849577.png)

基于地点聚合图片：

![image-20220313205927254](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220313205927254.png)

基于人物信息聚合图片：

![image-20220313205938516](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220313205938516.png)

小编本人在本地尝试安装和启动 PhotoView，由于 PhotoView 涉及前后端和数据库 MySQL，完全本地安装还是比较难的。但是项目提供了使用 Docker 和 docker-compose 启动的方式，让整体的难度降低了不少。

![image-20220313211417386](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220313211417386.png)

使用 docker-compose 还是很方便的。

![image-20220313213022433](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220313213022433.png)

从我个人的使用来看，比本地文件系统预览要好用太多了，只是在最开始使用的时候因为要生成缩略图，会需要一些时间，之后的浏览就非常的迅速了。

更多项目详情请查看如下链接。

开源项目地址：https://github.com/photoview/photoview
