兼容 Redis 的高性能数据库 KeyDB



大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 Snapchat/KeyDB，该项目在 GitHub 有超过 6.5k Star，用一句话介绍该项目就是：“A Multithreaded Fork of Redis”。

KeyDB 是一个开源的，高性能的，多线程的内存键值存储。它是流行的 Redis 数据库的分支版本，完全兼容 Redis 命令和数据类型。KeyDB 提供了很多的高级功能，如 Lua 脚本，LRU 淘汰和命令的并行执行。它是为企业环境构建的，提供高可用性和集群支持。KeyDB 也针对速度进行了优化，基准测试表明它是可用的键值存储之一。总的来说，KeyDB 是内存数据存储需求的强大和可靠的选择。

以下是 KeyDB 与 Redis 的性能对比，可以看出优势非常明显。

![](https://docs.keydb.dev/img/blog/2020-09-15/ops_comparison.png)


### 如何安装使用

KeyDB 可以通过下载源代码并编译来安装，同时也可以使用第三方包管理器（如 apt 或 yum）安装预编译的二进制文件。

1、源代码编译

```bash
git clone https://github.com/snapchat/KeyDB  # 可更换成 ssh 协议
cd KeyDB
make 
sudo make install
keydb-server  # 启动 KeyDB 服务器
```

2、第三方包管理器安装

```bash
sudo apt-get install keydb
sudo yum install keydb
```

以上安装只是简单步骤的介绍，实际情况可能根据不同系统会有不同，可根据错误提示逐步修改调整，推荐使用包管理的方式安装。

### 使用示例 DEMO

如果你使用 Python 的话，可以使用如下简单示例代码跟 KeyDB 进行交互。

```python
# Import the KeyDB library
import keydb

# Connect to KeyDB server running on localhost
client = keydb.Client()

# Set a key-value pair
client.set("mykey", "myvalue")

# Get the value of a key
value = client.get("mykey")
print(value)

```

这只是 KeyDB 的一个基本示例，KeyDB 还支持许多其他命令，如 HGET，HSET，LPUSH 等。 更多命令请参考 KeyDB 官网文档（https://keydb.dev/documentation/index.html）。

更多项目详情请查看如下链接。

开源项目地址：https://github.com/Snapchat/KeyDB   (文末可点击阅读原文)

开源项目作者：KeyDB

