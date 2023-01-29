---
layout: post
title: GitHub 开源项目 apache/skywalking-rover 介绍，Metrics collector and profiler powered by eBPF to diagnose CPU and network performance.
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 apache/skywalking-rover，该项目在 GitHub 有超过 0.1k Star，用一句话介绍该项目就是：“Metrics collector and profiler powered by eBPF to diagnose CPU and network performance.”。

![](http://skywalking.apache.org/assets/logo.svg)

Apache Skywalking-Rover是一个开源项目，它可以帮助您在本地运行和调试Skywalking服务端。它可以模拟Skywalking服务端的功能，并将收集到的数据存储在本地磁盘上。这对于开发和测试Skywalking应用程序非常有用。该项目基于Apache Skywalking项目开发，并遵循Apache许可协议。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=apache/skywalking-rover&type=Timeline)

### 如何安装使用

Apache Skywalking Rover 是 Apache Skywalking 的一个子项目。它是一个用来采集应用程序运行时信息的工具。

安装步骤如下：

1. 下载最新版本的 Rover 压缩包，并解压。
2. 在解压后的目录中，执行 ```./bin/rover.sh``` 或 ```./bin/rover.bat``` 来启动 Rover。
3. 在配置文件 ```config/application.yml``` 中配置连接信息，包括 Skywalking 服务器地址和端口、应用程序名称等。
4. 通过 JAVA_OPTS 参数配置 JVM 参数，例如内存和线程等。
5. 在 Rover 启动时，它会自动检测并采集应用程序运行时信息。

注意: 此项目需要jdk1.8及以上版本


### 使用示例 DEMO

Apache Skywalking Rover 是一个开源项目，它是 Apache Skywalking 的一个子项目。它提供了一种用于在应用程序运行时收集和上报应用程序性能数据的方法。

安装步骤：

1. 下载并安装 Java 8 或更高版本
2. 下载最新版本的 Apache Skywalking Rover 包
3. 解压并进入解压目录
4. 修改 config/application.yml 中的配置参数，如服务端地址等
5. 运行 bin/startup.sh (Unix/Linux) 或 bin/startup.bat (Windows)

示例代码：

```
public class MyApplication {
    public static void main(String[] args) {
        // 使用 Skywalking Rover 进行性能监控
        SkywalkingAgent.init();
        // 应用程序代码
        // ...
        // 结束 Skywalking Rover 监控
        SkywalkingAgent.destroy();
    }
}
```

在你的应用程序中，只需要在启动时调用 SkywalkingAgent.init() 和结束时调用 SkywalkingAgent.destroy() 即可。这样就可以在运行时收集并上报应用程序的性能数据。

注意：在使用这个代码之前，请确保已经安装并配置好 Apache Skywalking Rover 并且已经启动。


更多项目详情请查看如下链接。

开源项目地址：https://github.com/apache/skywalking-rover 

开源项目作者：apache

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=apache/skywalking-rover)

