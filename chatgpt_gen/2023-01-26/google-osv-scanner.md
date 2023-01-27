
大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 google/osv-scanner，该项目在 GitHub 有超过 4.3k Star，用一句话介绍该项目就是：“Vulnerability scanner written in Go which uses the data provided by https://osv.dev”。

![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/google/osv-scanner/badge)
![Packaging status](https://repology.org/badge/vertical-allrepos/osv-scanner.svg)
![Stargazers over time](https://starchart.cc/google/osv-scanner.svg)

"google/osv-scanner" 是一个由 Google 开源的应用程序安全性扫描器。它可以自动扫描应用程序代码以查找常见的安全漏洞，并生成漏洞报告。该项目基于 Python 开发，可以运行在 Linux, MacOS 和 Windows 系统上。

它支持扫描多种编程语言，包括Java, Python, C/C++, C#, Go, Ruby, JavaScript 等。
它提供了大量的规则来检测常见的漏洞，如 SQL 注入，跨站脚本（XSS）漏洞，路径遍历漏洞，以及许多其他类型的漏洞。

这个项目可以帮助您更快，更准确地发现应用程序中的安全漏洞，并可以帮助开发人员更早地修复这些问题。

如果你需要在应用程序开发过程中保证应用程序安全性，那么这个项目将会对你


### 如何安装使用

要安装 "google/osv-scanner" 项目，您需要执行以下步骤:

1. 克隆项目到本地：`git clone https://github.com/google/osv-scanner.git`

2. 进入到项目目录下: `cd osv-scanner`

3. 安装项目依赖: `pip install -r requirements.txt`

4. 扫描文件：`python osv-scanner.py <path_to_code>`

请注意,需要本地安装python环境，并且是3.6以上版本.
如果需要扫描特定语言的代码，需要安装对应语言的编译器.

项目扫描完成后会在根目录下生成scan_result.json文件
可以使用osv-scanner-report.py 生成漏洞报告


### 使用示例 DEMO

以下是一个简单的示例代码，演示了如何使用 "google/osv-scanner" 扫描本地目录中的代码文件：

```
import os

# 设置要扫描的代码目录
code_dir = 'path/to/code'

# 执行扫描
os.system(f'python osv-scanner.py {code_dir}')

# 生成扫描结果报告
os.system(f'python osv-scanner-report.py -i scan_result.json -o scan_result.html')

# 打开报告
os.system(f'open scan_result.html')
```

这段代码首先将要扫描的代码目录路径设置为 `code_dir` 变量，然后执行 `os.system(f'python osv-scanner.py {code_dir}')` 命令来扫描目录中的代码。
扫描完成后,会在根目录下生成scan_result.json文件,之后使用 `os.system(f'python osv-scanner-report.py -i scan_result.json -o scan_result.html')` 生成漏洞报告。
最后使用 `os.system(f'open scan_result.html')`打开报告.

请注意，上面的代码仅用于演示目的，在实际使用中需要根据您的实际情况进行修改。


更多项目详情请查看如下链接。

开源项目地址：https://github.com/google/osv-scanner  (文末可点击阅读原文)

开源项目作者：osv-scanner

