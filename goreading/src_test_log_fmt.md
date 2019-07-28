# Go 源码阅读

## Go 源码结构

代码根目录主要 doc、lib、misc、src、test

* lib 中是 time 的 zoneinfo 包，干什么用的？
* misc 意思是大杂烩，大部分是各种编辑器的Go语言支持，还有cgo的例子等
* src 源码部分
* test 测试代码，声明是 package main，也就是这些代码可直接执行



FAQ：

Q: 单独的 test 目录测试代码和 _test.go 的优劣？

独立于 PKG 的 test 目录测试方式，可以提前定义好 PKG 的接口，针对接口进行测试，将代码实现和测试进行隔离

_test.go 形式与代码实现在一起，便于查看



## Go test 命令

源码位置：src/cmd/go/internal/test/test.go

```go
pkgs = load.PackagesForBuild(pkgArgs)

// translate C to runtime/cgo   Import C 就是 Import runtime/cgo
if deps["C"] {
    delete(deps, "C")
		deps["runtime/cgo"] = true
}
// Ignore pseudo-packages.   unsafe golang 的一个 pkg
delete(deps, "unsafe")   
```



FAQ：

Q: 为何要从 pkg deps 中删除 C 和 unsafe



## log 

```go
var std = New(os.Stderr, "", LstdFlags)  // 输出的标准错误

func (l *Logger) SetPrefix(prefix string)

func Fatal(v ...interface{}) {  
	std.Output(2, fmt.Sprint(v...))    // 为什么不直接调用 std.Fatal
	os.Exit(1)
}
```



FAQ：

Q: stderr、stdout 区别？

标准错误和标准输出，不同系统对应的输出可能不一样，可以屏蔽不同系统之间的差异

```bash
## mac
➜ ls -l /dev/std*
lr-xr-xr-x  1 root  wheel  0  5  8 18:00 /dev/stderr -> fd/2
lr-xr-xr-x  1 root  wheel  0  5  8 18:00 /dev/stdin -> fd/0
lr-xr-xr-x  1 root  wheel  0  5  8 18:00 /dev/stdout -> fd/1

➜ ./exe > a.log 2>&1 
# 2 => stderr, 1 => stdout, 0 => stdin, 将 2 的输出重定向到 1
```



Q: log 中包级别的方法包装存在重复

提交 PR 简化这部分代码：暂不提交，修改后单元测试不通过

```go
func Printf(format string, v ...interface{}) {
	std.Output(2, fmt.Sprintf(format, v...))  
  // std.Printf(format, v...)    // 使用 std.Printf 更简化
}

// 获取打印日志的文件和行号，如果在 std 增加了一层调用逻辑，获取的行号是不对的
_, file, line, ok = runtime.Caller(calldepth)

// 测试检查中把行号赋值为一个 Magic Number
Rline = `(57|59):` // must update if the calls to l.Printf / l.Print below move
```



Go 从 1.4 版本以后源码可以用 go 自举编译，需要设置 export GOROOT_BOOTSTRAP 源码tree

```bash
cd <source_code>/src
./make.bash  # 编译
./all.bash   # Test your changes
```



Q：PR 提交方式？

方式一：GitHub，Fork 仓库，新建分支，变更代码提交，在页面新建 PR，PR 会自动同步到 Go Gerrit 仓库。

方式二：直接向 Go Gerrit 仓库提交，需要工具 golang.org/x/review/git-codereview 、golang.org/x/tools/cmd/go-contrib-init

```bash
git codereview change   # 生成 gerrit 的 Change-Id?
git codereview sync  # 是不是 rebase master 代码？
```



## fmt

```go
// parsenum converts ASCII to integer.  num is 0 (and isnum is false) if no number present.
// 依次解析字符串中的数字
func parsenum(s string, start, end int) (num int, isnum bool, newi int) {
	if start >= end {
		return 0, false, end
	}
	for newi = start; newi < end && '0' <= s[newi] && s[newi] <= '9'; newi++ {
		if tooLarge(num) {
			return 0, false, end // Overflow; crazy long number most likely.
		}
		num = num*10 + int(s[newi]-'0')
		isnum = true
	}
	return
}
```

