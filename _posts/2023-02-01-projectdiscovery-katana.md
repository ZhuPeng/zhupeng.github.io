
大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 projectdiscovery/katana，该项目在 GitHub 有超过 5.3k Star，用一句话介绍该项目就是：“A next-generation crawling and spidering framework.”，下一代爬虫框架。

![](https://user-images.githubusercontent.com/8293321/196779266-421c79d4-643a-4f73-9b54-3da379bbac09.png)

![image](https://user-images.githubusercontent.com/8293321/199371558-daba03b6-bf9c-4883-8506-76497c6c3a44.png)

katana 是一个爬虫工具，具备如下功能，能够高度配置化进行网页抓取，同时支持无浏览器方式的抓取，且对命令行的支持友好，支持通过管道进行输入输出的控制。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230201222704205.png)

katana 使用 Go 开发，并且可通过命令行和工具库引入的方式使用，通过如下命令即可安装使用。

```bash
go install github.com/projectdiscovery/katana/cmd/katana@latest
```

安装好后，如果通过命令使用，有非常多的参数的支持。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230201223000574.png)

以下是一个使用示例，默认会对目标网站进行子链接的解析。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230201223036208.png)

也可以通过包引入的方式进行定制化的开发，但是我觉得 katana 的亮点就是命令行支持的友好。


更多项目详情请查看如下链接。

开源项目地址：https://github.com/projectdiscovery/katana  (文末可点击阅读原文)

开源项目作者：katana



关注我们，一起探索有意思的开源项目。
