## runtime

包含 go 里面原生支持的类型，如 chan

* chan

详细介绍：<https://draveness.me/golang/concurrency/golang-channel.html>

```go
// 跳过 buf 直接发送给 receiver
if sg := c.recvq.dequeue(); sg != nil {
		// Found a waiting receiver. We pass the value we want to send
		// directly to the receiver, bypassing the channel buffer (if any).
		send(c, sg, ep, func() { unlock(&c.lock) }, 3)
		return true
}
```

buf => 循环数组