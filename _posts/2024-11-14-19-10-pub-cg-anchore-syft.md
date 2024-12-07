---
layout: post
title: 专注于容器镜像安全的工具
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在今天的软件开发领域，安全和合规性是绕不开的议题。软件供应链安全已然成为企业关注的热点，特别是当涉及到容器化技术和微服务架构时。随着依赖库和第三方组件的使用越来越广，了解和管理这些组件变得日益困难，而这些组件潜在的安全漏洞和许可证问题也随之而来。作为开发者或运维人员，如何快速准确地了解到你的容器镜像或文件系统中究竟包含了什么软件包和依赖，成为了一项挑战。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241118223847305.png)

今天要给大家推荐一个 GitHub 开源项目 syft，该项目在 GitHub 有超过 6.3k Star。

![](https://stats.deeptrain.net/repo/anchore/syft/?theme=light)

一句话介绍该项目：CLI tool and library for generating a Software Bill of Materials from container images and filesystems

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241118223800443.png)


###### 项目介绍

**Syft** 是一个开源的 CLI 工具和 Go 语言库，专门用于从容器镜像和文件系统生成软件物料清单（Software Bill of Materials，简称 **SBOM**）。通过 **Syft**，你可以获得一个清晰的软件包和依赖关系视图，这样不仅可以帮助你高效地管理软件许可证，还可以和诸如 [Grype](https://github.com/anchore/grype) 这样的扫描工具搭配使用，以便进行漏洞检测和软件供应链风险管理。

以下是一个使用示例：

![](https://user-images.githubusercontent.com/590471/90277200-2a253000-de33-11ea-893f-32c219eea11a.gif)

主要功能介绍如下：

1、支持生成容器镜像、文件系统、档案等的 SBOM

2、支持 OCI、Docker 和 [Singularity](https://github.com/sylabs/singularity) 镜像格式

3、能够识别 Linux 发行版

4、与 [Grype](https://github.com/anchore/grype) 紧密集成，提供快速现代的漏洞扫描能力

5、支持创建符合 [in-toto spec](https://github.com/in-toto/attestation/blob/main/spec/README.md) 的 SBOM 签名声明

6、支持多种 SBOM 格式之间的转换，包括 CycloneDX、SPDX 和 Syft 自有格式

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241118224038274.png)

###### 如何使用

对于 Linux、macOS 和 Windows 用户，可以通过以下方式安装 **Syft**：

```bash
curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | sh -s -- -b /usr/local/bin
```

也可以通过 **Homebrew**、**Scoop**、**Chocolatey** 或 **Nix** 进行安装，具体命令请参照项目 README。

具体的使用方式举例如下：

1、生成 SBOM

为了生成容器镜像的 SBOM，执行：

```bash
syft <image-name>
```

如果想要包含所有镜像层中的软件，而不仅是最终镜像中的，提供 `--scope all-layers` 选项：

```bash
syft <image-name> --scope all-layers
```

2、输出格式:

通过 `-o` 或 `--output` 选项，可以配置 Syft 的输出格式，例如：

```bash
syft <image-name> -o <format>
```

支持的格式有 `syft-json`、`syft-table`、`cyclonedx-xml`、`spdx-tag-value` 等，详细信息可参考项目文档。

###### 项目推介

随着软件供应链安全的关注度不断攀升，类似 **Syft** 这样能够提供清晰、详细 SBOM 的工具变得异常重要。**Syft** 的开发活跃，由拥有广泛认可的安全企业 Anchore 赞助。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241118224229211.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=anchore/syft&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/anchore/syft 

开源项目作者：anchore

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=anchore/syft)

关注我们，一起探索有意思的开源项目。

