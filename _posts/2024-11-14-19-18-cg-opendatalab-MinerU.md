---
layout: post
title: GitHub 开源项目 opendatalab/MinerU 介绍，A one-stop, open-source, high-quality data extraction tool, supports PDF/webpage/e-book extraction.一站式开源高质量数据提取工具，支持PDF/网页/多格式电子书提取。
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 opendatalab/MinerU，该项目在 GitHub 有超过 14.6k Star。

![](https://stats.deeptrain.net/repo/opendatalab/MinerU/?theme=light)

一句话介绍该项目：A one-stop, open-source, high-quality data extraction tool, supports PDF/webpage/e-book extraction.一站式开源高质量数据提取工具，支持PDF/网页/多格式电子书提取。




![](https://raw.githubusercontent.com/opendatalab/MinerU/master/docs/images/MinerU-logo.png)


###### 项目介绍

### 背景介绍

在日益进入大数据和信息化时代的今天，数据的采集与分析成为了各行各业关注的焦点。然而，在信息提取过程中，我们经常面临多种挑战，尤其是从非结构化数据源如 PDF 文档、网页以及电子书中提取高质量数据。这些文件往往包含大量的文本、图表、公式和图片，手动提取既耗时又低效，而且可能因格式不统一、布局复杂等问题而造成信息转录的错误和遗漏，从而影响数据分析的精确度和效率。

### 

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-ca6f64d28d9f33b0ffc96bdf7b8a41ac.png)

项目介绍

针对上述问题， [`MinerU`](https://github.com/opendatalab/MinerU) 的诞生提供了一站式的解决方案。`MinerU` 是一个开源高质量数据提取工具，支持从 PDF、网页、电子书等多种格式进行数据提取。项目在 [InternLM](https://github.com/InternLM/InternLM) 的预训练过程中被开发和完善，专注于解决科学文献和技术文件中的符号转换问题，致力于推动大模型时代的技术发展。

`MinerU` 的主要功能包括：

- 自动移除页眉、页脚、脚注、页码等，确保语义连贯。
- 按人类可读的顺序输出文本，适应单列、多列及复杂布局。
- 保留原始文档结构，包括标题、段落、列表等。
- 提取图片、图片描述、表格、表标题和脚注。
- 自动识别并将文档中的公式转换为 LaTeX 格式。
- 自动识别并将表格转换为 LaTeX 或 HTML 格式。

### 如何使用

使用 `MinerU` 非常简单。首先确保已安装 Python 环境，然后通过 pip 安装 `MinerU`：

```bash
pip install mineru
```

之后，你可以通过命令行或 API的方式来使用 `MinerU` 进行数据提取。例如，从 PDF 中提取数据到 Markdown 格式：

```bash
mineru pdf2md your_file.pdf -o output.md
```

或者，使用 Python API 进行更灵活的控制：

```python
from mineru import PDFExtractor

extractor = PDFExtractor()
result = extractor.extract("your_file.pdf")
print(result)
```

### 项目推介

`MinerU` 从 2022 年初开始开源，尽管相对于一些商业产品来说仍然年轻，但它在开源社区已经表现出了强劲的发展潜力和活动状态。项目自开源以来，一直致力于优化性能、扩展功能和简化使用流程，如在最新版本中整合了高精度的表格识别模型、提供了对 84 种语言的 OCR 支持，并大幅优化了内存占用。

此外，`MinerU` 已经在多个科研项目和技术文档处理任务中得到应用，得到了用户的广泛认可。对于寻求高效、灵活且成本友好的数据提取解决方案的开发者、数据分析师和科研工作者来说，`MinerU` 无疑是一个值得尝试的优秀工具。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=opendatalab/MinerU&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/opendatalab/MinerU 

开源项目作者：opendatalab

开源协议：GNU Affero General Public License v3.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=opendatalab/MinerU)

关注我们，一起探索有意思的开源项目。

