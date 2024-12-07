---
layout: post
title: 支持PDF/网页/多格式电子书的数据提取工具
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

数据的采集与分析成为了各行各业关注的焦点。然而，在信息提取过程中，我们经常面临多种挑战，尤其是从非结构化数据源如 PDF 文档、网页以及电子书中提取高质量数据。这些文件往往包含大量的文本、图表、公式和图片，手动提取既耗时又低效，而且可能因格式不统一、布局复杂等问题而造成信息转录的错误和遗漏，从而影响数据分析的精确度和效率。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-ca6f64d28d9f33b0ffc96bdf7b8a41ac.png)

今天要给大家推荐一个 GitHub 开源项目 MinerU，该项目在 GitHub 有超过 17.6k Star。

![](https://stats.deeptrain.net/repo/opendatalab/MinerU/?theme=light)

一句话介绍该项目：A one-stop, open-source, high-quality data extraction tool, supports PDF/webpage/e-book extraction. 一站式开源高质量数据提取工具，支持PDF/网页/多格式电子书提取。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241119224104797.png)


###### 项目介绍

MinerU 是一个开源高质量数据提取工具，支持从 PDF、网页、电子书等多种格式进行数据提取。项目在 InternLM 的预训练过程中被开发和完善，专注于解决科学文献和技术文件中的符号转换问题，致力于推动大模型时代的技术发展。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241119224206713.png)

`MinerU` 的主要功能包括：

1、自动移除页眉、页脚、脚注、页码等，确保语义连贯。

2、按人类可读的顺序输出文本，适应单列、多列及复杂布局。

3、保留原始文档结构，包括标题、段落、列表等。

4、提取图片、图片描述、表格、表标题和脚注。

5、自动识别并将文档中的公式转换为 LaTeX 格式。

6、自动识别并将表格转换为 LaTeX 或 HTML 格式。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241119224245620.png)

###### 如何使用

首先确保已安装 Python 环境，然后通过 pip 安装 magic-pdf：

```bash
pip install -U magic-pdf[full] --extra-index-url https://wheels.myhloli.com
```

具体的命令行参数参考如下：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241119224448683.png)

###### 项目推介

项目自开源以来，一直致力于优化性能、扩展功能和简化使用流程，如在最新版本中整合了高精度的表格识别模型、提供了对 84 种语言的 OCR 支持，并大幅优化了内存占用。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241119224551023.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=opendatalab/MinerU&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/opendatalab/MinerU 

开源项目作者：opendatalab

开源协议：GNU Affero General Public License v3.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=opendatalab/MinerU)

关注我们，一起探索有意思的开源项目。

