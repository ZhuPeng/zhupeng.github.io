---
layout: post
title: GitHub 开源项目 stretchr/testify 介绍，A toolkit with common assertions and mocks that plays nicely with the standard library
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 stretchr/testify，该项目在 GitHub 有超过 22.7k Star。

![](https://stats.deeptrain.net/repo/stretchr/testify/?theme=light)

一句话介绍该项目：A toolkit with common assertions and mocks that plays nicely with the standard library





###### 项目介绍

背景介绍：在软件开发过程中，确保代码质量是每个开发者的首要任务。无论是新功能的开发还是现有功能的维护，编写可靠、易于维护的单元测试都是实现这一目标不可或缺的一步。然而，Go 语言的标准库虽然提供了基础的测试框架，但在进行更复杂的断言或模拟外部依赖时，开发者可能会发现自己需要编写大量模板代码。这不仅耗时而且降低了测试代码的可读性和易用性，是许多 Go 开发者面临的核心痛点。



![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-ddc4920b76bdab84ed7a4ec278ddb1ba.png)

项目介绍：为了解决上述问题，《Testify》应运而生。这是一个为 Go 语言设计的测试工具包，它与标准库无缝集成，旨在简化测试过程。该项目提供了一系列功能强大的工具，包括但不限于易于使用的断言、高效的模拟机制和全面的测试套件接口。通过使用《Testify》，开发者可以轻松编写更加清晰、精确的测试代码，提高测试覆盖率，同时降低测试代码的维护成本。此外，《Testify》还支持友好的失败描述输出，使得测试结果更易于理解。

如何使用：安装《Testify》极其简单，只需一行命令即可：

```shell
go get github.com/stretchr/testify
```

使用《Testify》的断言功能进行测试示例：

```go
package yours

import (
  "testing"
  "github.com/stretchr/testify/assert"
)

func TestSomething(t *testing.T) {
  // 使用 assert 进行不同类型的断言
  assert.Equal(t, 123, 123, "they should be equal")
  assert.NotEqual(t, 123, 456, "they should not be equal")
  assert.Nil(t, nil)
  if assert.NotNil(t, t) {
    assert.Equal(t, "Something", "Something")
  }
}
```

若需要使用模拟功能，可参考以下示例：

```go
package yours

import (
  "testing"
  "github.com/stretchr/testify/mock"
)

// MyMockedObject 是一个模拟对象示例
type MyMockedObject struct{
  mock.Mock
}

func (m *MyMockedObject) DoSomething(number int) (bool, error) {
  args := m.Called(number)
  return args.Bool(0), args.Error(1)
}

func TestSomething(t *testing.T) {
  testObj := new(MyMockedObject)
  testObj.On("DoSomething", 123).Return(true, nil)
  
  // 调用测试代码
  // targetFuncThatDoesSomethingWithObj(testObj)
  
  testObj.AssertExpectations(t)
}
```

项目推介：自从《Testify》项目发布以来，其以其强大的功能、易用性以及高效的性能，迅速在 Go 社区中获得了广泛的认可和好评。该项目目前在 GitHub 上拥有众多星标，社区活跃，定期发布更新，保证了工具的先进性和稳定性。无论是个人开发者还是大型企业，都可以从《Testify》中受益。其中，知名公司如 Google、Amazon 等都在其项目中使用了《Testify》。如果你在寻找一个强大而且高效的 Go 语言测试工具，《Testify》无疑是你的首选。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=stretchr/testify&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/stretchr/testify 

开源项目作者：stretchr

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=stretchr/testify)

关注我们，一起探索有意思的开源项目。

