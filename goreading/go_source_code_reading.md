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

