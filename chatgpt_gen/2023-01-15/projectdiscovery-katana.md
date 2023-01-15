
大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 projectdiscovery/katana，该项目在 GitHub 有超过 5.3k Star，用一句话介绍该项目就是：“A next-generation crawling and spidering framework.”。

![image](https://user-images.githubusercontent.com/8293321/199371558-daba03b6-bf9c-4883-8506-76497c6c3a44.png)
![](https://user-images.githubusercontent.com/8293321/196779266-421c79d4-643a-4f73-9b54-3da379bbac09.png)
![](https://goreportcard.com/badge/github.com/projectdiscovery/katana)
![](https://raw.githubusercontent.com/projectdiscovery/nuclei-burp-plugin/main/static/join-discord.png)

projectdiscovery/katana 是一个开源的网络安全工具，可以帮助用户进行子域枚举、端口扫描、资产发现等操作。该工具基于 Python 开发，具有简单易用的用户界面，易于集成到其它渗透测试工具中。它支持多种数据源，包括 DNSdumpster、Crtsh、Bufferover、Rapid7 等，可以有效地帮助用户发现网络漏洞。



### 如何安装使用

要安装 projectdiscovery/katana，您需要先安装 Python 3.7 或更高版本。然后，您可以使用以下命令在终端中安装该项目:
```
pip3 install katana
```
在安装之后，您可以使用以下命令来运行 katana:
```
katana -h
```
这将显示所有可用的命令行选项和用法。如果在安装过程中遇到问题，请查看项目的 GitHub 页面以获取更多帮助。


### 使用示例 DEMO

这里是一个使用 projectdiscovery/katana 进行子域枚举的示例代码:
```
from katana.utils.request import make_request
from katana.manager.scan_manager import ScanManager

# Initialize the scan manager
scan_manager = ScanManager()

# Add a target to scan
scan_manager.add_target("example.com")

# Add subdomain enum module
scan_manager.add_module("subdomain_enum")

# Start the scan
scan_manager.start_scan()

# Get the scan results
scan_results = scan_manager.get_scan_results()

# Print the results
for result in scan_results:
    print(result)
```
这段代码会对 example.com 进行子域枚举，并打印出所有发现的子域。除此之外，还可以使用端口扫描和资产发现等其他模块。详细使用说明请参考项目的 GitHub 页面.


更多项目详情请查看如下链接。

开源项目地址：https://github.com/projectdiscovery/katana  (文末可点击阅读原文)

开源项目作者：katana

