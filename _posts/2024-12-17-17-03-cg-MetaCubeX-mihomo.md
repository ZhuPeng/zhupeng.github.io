---
layout: post
title: GitHub 开源项目 MetaCubeX/mihomo 介绍，A simple Python Pydantic model for Honkai: Star Rail parsed data from the Mihomo API.
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 MetaCubeX/mihomo，该项目在 GitHub 有超过 17.3k Star。

![](https://stats.deeptrain.net/repo/MetaCubeX/mihomo/?theme=light)

一句话介绍该项目：A simple Python Pydantic model for Honkai: Star Rail parsed data from the Mihomo API.





###### 项目介绍

### **背景介绍**

在当前的游戏生态中，游戏数据的分析和共享变得越来越重要。以 "崩坏：星穹铁道" 为例，玩家经常需要查询自己的角色数据，对战绩、角色等级及稀有度等信息进行分析，以便更好地规划游戏策略。然而，由于数据散布在不同的平台和接口，这通常需要大量的手动操作和时间成本，增加了玩家的负担。

### **

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-ff01342c3b3e364427d07384870c31bb.png)

项目介绍**

在这种背景下， `mihomo` 项目应运而生。它是一个基于 Python 和 Pydantic 的轻量级工具，旨在为 "崩坏：星穹铁道" 的玩家提供一个简单高效的方式来解析和使用来自 Mihomo API 的数据。通过提供类型提示和自动完成支持，该项目大大提升了代码的可读性和易用性，为游戏数据分析提供了强力工具。

项目主要功能有：

- 支持两种数据格式（V1 和 V2）的解析及获取
- 提供简单的客户端 API 调用示例，包括如何获取玩家信息、角色数据等
- 工具集的使用，包含去重与合并角色数据的方法，方便对游戏角色进行管理
- 支持数据持久化，包括 pickle 和 json 格式，便于数据存储和分享

### **如何使用**

要使用 `mihomo`，首先需要安装该工具库：

```shell
pip install -U git+https://github.com/KT-Yeh/mihomo.git
```

下面是两个版本数据获取的代码示例：

```python
import asyncio
from mihomo import Language, MihomoAPI
from mihomo.models import StarrailInfoParsed
from mihomo.models.v1 import StarrailInfoParsedV1

client = MihomoAPI(language=Language.EN)

async def main():
    # 获取 V1 格式数据
    data_v1: StarrailInfoParsedV1 = await client.fetch_user_v1(800333171)
    # 处理和展示 V1 数据...

    # 获取 V2 格式数据，并替换 icon 名称为真实 url
    data_v2: StarrailInfoParsed = await client.fetch_user(800333171, replace_icon_name_with_url=True)
    # 处理和展示 V2 数据...

asyncio.run(main())
```

### **项目推介**

自从 `mihomo` 项目发布以来，它受到了众多 "崩坏：星穹铁道" 玩家和数据分析师的欢迎。凭借其简单而强大的功能，该项目不仅帮助玩家节省了大量处理数据的时间，还提升了游戏策略的制定效率。

此外，该项目的持续更新和活跃的社区支持确保了其功能的持续优化和扩展，使其成为游戏玩家和开发者的首选工具之一。如果你也是 "崩坏：星穹铁道" 的粉丝，或者对游戏数据分析有兴趣，`mihomo` 绝对值得一试！

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=MetaCubeX/mihomo&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/MetaCubeX/mihomo 

开源项目作者：MetaCubeX

开源协议：MIT License

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=MetaCubeX/mihomo)

关注我们，一起探索有意思的开源项目。

