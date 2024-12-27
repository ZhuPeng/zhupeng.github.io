---
layout: post
title: GitHub 开源项目 getomni-ai/zerox 介绍，PDF to Markdown with vision models
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 getomni-ai/zerox，该项目在 GitHub 有超过 7.2k Star。

![](https://stats.deeptrain.net/repo/getomni-ai/zerox/?theme=light)

一句话介绍该项目：PDF to Markdown with vision models




![Hero Image](https://raw.githubusercontent.com/getomni-ai/zerox/master/./examples/heroImage.png)

![](https://github.com/user-attachments/assets/cccc0e9a-e3b2-425e-9b54-e5024681b129)


###### 项目介绍

背景介绍：
在数字化时代，无数的 PDF 文件和文档被每天创造和分享，而它们的内容往往需要被进一步处理或分析。例如，学术研究、商务报告或法律文件等，都需要被精确地转换成可编辑的格式来进行内容分析或数据提取。然而，PDF 文件本身的复杂布局、表格、图表等元素，使得这一过程充满了挑战。这些文件的内容经常无法通过传统的文本提取工具准确地转换，造成信息的丢失或误读，严重影响了工作效率和数据分析的准确性。



![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-86b0ba962ecb7b61a3239945fff5b54c.png)

项目介绍：
针对上述挑战，Zerox OCR 项目应运而生。它是一个开源项目，主要利用先进的视觉模型来实现 PDF 到 Markdown 的转换。该项目通过将文件（如 PDF ， DOCX ，图片等）转换为一系列图片，再将每张图片提交给 GPT 模型进行处理，最后聚合回传的结果，输出为 Markdown 格式。这个过程不仅保留了文件的原始视觉布局，还大大提高了转换的准确性和效率。零代码的接口设计也让使用者无需复杂的配置即可快速上手。

如何使用：
Zerox 可以作为 Node 和 Python 包使用。

Node.js 用户：
```sh
npm install zerox
```
需要安装 `graphicsmagick` 和 `ghostscript`，Linux 用户可以使用以下命令：
```sh
sudo apt-get update
sudo apt-get install -y graphicsmagick
```
示例代码（从文件 URL 使用）：
```ts
import { zerox } from "zerox";

const result = await zerox({
  filePath: "https://omni-demo-data.s3.amazonaws.com/test/cs101.pdf",
  openaiAPIKey: process.env.OPENAI_API_KEY,
});
```

Python 用户：
```sh
pip install py-zerox
```
同样，Python 版本的 Zerox 支持使用多种视觉模型进行 OCR 处理。确保设置了环境变量及模型供应商信息后，可通过以下方式使用：
```python
from pyzerox import zerox
import asyncio

async def main():
    # 输入文件路径和必要的模型信息
    result = await zerox(filePath="path/to/your/file.pdf", openaiAPIKey="your_openai_api_key")
    print(result)

asyncio.run(main())
```

项目推介：
Zerox OCR 是一个高度活跃和不断更新的项目，背后由一支专业的团队所支持。它的主要优势在于利用最新的视觉模型技术，能够处理复杂的文档布局和元素，保证转换结果的精确度和一致性，这使其在众多的文档处理工具中脱颖而出。目前，已经有多家知名企业和机构采用这一技术来改进他们的数据处理和分析流程。另外，它作为开源工具，意味着拥有强大的社区支持，用户可以根据自身需求进行定制和优化。无论是开发者还是非技术用户，都可以轻松上手，将它集成到自己的工作流程中，提升文档处理的效率和质量。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=getomni-ai/zerox&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/getomni-ai/zerox 

开源项目作者：getomni-ai

开源协议：MIT License

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=getomni-ai/zerox)

关注我们，一起探索有意思的开源项目。

