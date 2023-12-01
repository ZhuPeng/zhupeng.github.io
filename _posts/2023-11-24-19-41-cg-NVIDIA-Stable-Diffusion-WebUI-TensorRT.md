---
layout: post
title: GitHub 开源项目 NVIDIA/Stable-Diffusion-WebUI-TensorRT 介绍，TensorRT Extension for Stable Diffusion Web UI
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 NVIDIA/Stable-Diffusion-WebUI-TensorRT，该项目在 GitHub 有超过 1.0k Star，用一句话介绍该项目就是：“TensorRT Extension for Stable Diffusion Web UI”。





背景介绍：在图像生成技术领域，稳定扩散（Stable Diffusion）是一种新型的方法，它提供了在保证图像质量的同时实现更高效生成图像的能力。然而，由于种种原因，直接使用稳定扩散技术在某些应用场景下可能无法满足效能需求。特别是在是 NVIDIA RTX GPUs 硬件环境下，虽然这款硬件具有强大的计算能力，但没有针对稳定扩散技术优化的工具，导致不能充分发挥其性能和效率。

项目介绍：为了解决上述问题，"TensorRT Extension for Stable Diffusion Web UI" 这个项目应运而生。该项目是 NVIDIA 推出的一款针对稳定扩散的 TensorRT 扩展工具，可以有效提升在 RTX GPUs 上进行稳定扩散的性能。除了基本的引擎优化外，该项目还支持为特定的分辨率和批次大小生成优化引擎，并且可以在导出默认引擎的情况下进行扩展，提供了相当强大的定制性。

如何使用：使用该项目非常简单，您只需要按照以下步骤操作：首先，启动 webui.bat；在扩展选项卡中选择 "Install from URL"；复制项目仓库链接并粘贴至 "URL for extension's git repository"；点击 "Install" 完成安装；安装完成后，点击 "Generate Default Engines" 按钮，然后根据提示进行操作，即可开始生成由 TRT 加速的图像。

项目推介：目前，该项目在 GitHub 上唤起了很多用户的关注，并收到了许多积极的反馈。尤其对于从事图像生成技术的开发者，这是一个非常值得关注的项目。其发布者 NVIDIA 是全球知名的 AI 计算公司，拥有先进的技术和色强大的研发团队，对此类项目的维护和更新都非常到位，因此在使用过程中即使遇到了问题，也能得到及时的解决。同时，该项目的部署和使用语义都非常清晰，无论你是初学者还是有经验的开发者，都能够快速上手。对于希望提升在 NVIDIA RTX GPUs 上稳定扩散性能的开发者来说，这个项目无疑是一个极佳的选择。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=NVIDIA/Stable-Diffusion-WebUI-TensorRT&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/NVIDIA/Stable-Diffusion-WebUI-TensorRT 

开源项目作者：NVIDIA

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=NVIDIA/Stable-Diffusion-WebUI-TensorRT)

关注我们，一起探索有意思的开源项目。

