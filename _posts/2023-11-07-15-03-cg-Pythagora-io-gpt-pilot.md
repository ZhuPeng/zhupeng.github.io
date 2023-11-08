---
layout: post
title: GitHub 开源项目 Pythagora-io/gpt-pilot 介绍，Dev tool that writes scalable apps from scratch while the developer oversees the implementation
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 Pythagora-io/gpt-pilot，该项目在 GitHub 有超过 14.6k Star，用一句话介绍该项目就是：“Dev tool that writes scalable apps from scratch while the developer oversees the implementation”。


![屏幕截图 2023-10-15 103907](https://github.com/Pythagora-io/gpt-pilot/assets/138990495/c3d08f21-7e3b-4ee4-981f-281d1c97149e)
![屏幕截图 2023-10-15 104120](https://github.com/Pythagora-io/gpt-pilot/assets/138990495/942cd1c9-b774-498e-b72a-677b01be1ac3)
![GPT Pilot workflow](https://github.com/Pythagora-io/gpt-pilot/assets/10895136/d89ba1d4-1208-4b7f-b3d4-76e3ccea584e)
![GPT Pilot Coding Workflow](https://github.com/Pythagora-io/gpt-pilot/assets/10895136/53ea246c-cefe-401c-8ba0-8e4dd49c987b)



# GPT Pilot：让开发人员20倍快速构建应用的开发工具

在开发应用程序时，我们往往会遇到许多重复且繁琐的工作，例如编写产品和技术需求、设置开发环境以及编码应用程序。GPT Pilot是一款旨在解决这些问题的开发工具，它可以以真实的开发流程逐步编写应用程序，让你作为技术领导进行开发过程的监督与审核。

## 背景介绍：
在构建应用程序时，AI可以自动生成大部分代码（可能达到95%），但在剩下的5%上，开发人员的参与是不可或缺的。GPT Pilot的目标就是研究如何最大限度地利用GPT-4来生成完全可用的、适合生产环境的应用程序。

GPT Pilot的设计理念以及它的工作原理都在以下博文中有详细解释：

- [【第一部分/共3部分】高级概念与GPT Pilot的工作流程](https://blog.pythagora.ai/2023/08/23/430/)
- [【第二部分/共3部分】GPT Pilot的编码工作流程](https://blog.pythagora.ai/2023/09/04/gpt-pilot-coding-workflow-part-2-3/)
- [【第三部分/共3部分】其他重要概念和未来计划（敬请期待）]

## 项目介绍：
GPT Pilot的核心目标是帮助开发人员以更高效的方式构建应用程序。它通过提供以下功能来实现这一目标：

- 提供多种应用程序模板，支持快速生成各种类型的应用程序
- 通过与开发人员交互，帮助生成产品需求和技术规格
- 自动设置开发环境，并逐步编写应用程序代码
- 在开发过程中，开发人员可以对每个任务进行审核和调试

此外，GPT Pilot还支持自定义设置，包括选择AI模型提供者（OpenAI/Azure/Openrouter）、添加API密钥以及选择数据库类型（默认为SQLite，也可选择PostgreSQL）。

## 如何使用：
要开始使用GPT Pilot，按照以下步骤进行操作：

1. 克隆仓库：`git clone https://github.com/Pythagora-io/gpt-pilot.git`
2. 进入项目目录：`cd gpt-pilot`
3. 创建虚拟环境：`python -m venv pilot-env`（激活虚拟环境：`source pilot-env/bin/activate`）
4. 安装依赖：`pip install -r requirements.txt`
5. 复制环境变量示例文件：`mv .env.example .env`
6. 在`.env`文件中进行相应配置，包括AI模型提供者、API密钥和数据库设置等。
7. 初始化数据库：`python db_init.py`
8. 启动GPT Pilot：`python main.py`

启动之后，按照终端中的说明操作即可。所有生成的代码将存储在`workspace`文件夹中，文件夹名称与输入的应用程序名称相对应。

如果你更喜欢使用Docker来运行GPT Pilot，可以按照以下步骤进行操作：

1. 克隆仓库：`git clone https://github.com/Pythagora-io/gpt-pilot.git`
2. 更新`docker-compose.yml`文件中的环境变量配置。
3. 默认情况下，GPT Pilot将读取和写入本地机器上的`~/gpt-pilot-workspace`文件夹，你也可以在`docker-compose.yml`中进行相应修改。
4. 构建容器：`docker compose build`
5. 启动GPT Pilot容器：`docker compose


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=Pythagora-io/gpt-pilot&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/Pythagora-io/gpt-pilot 

开源项目作者：Pythagora-io

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=Pythagora-io/gpt-pilot)

关注我们，一起探索有意思的开源项目。

