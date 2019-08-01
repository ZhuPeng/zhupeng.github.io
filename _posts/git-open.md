经常使用命令行工具的同学，总是希望所有的操作都能使用命令行解决，比如提交代码后想看一下效果、提交完代码需要在页面提交 Pull Request。

今天要推荐的工具 git-open 能够将上面的流程一气呵成~ 目前支持了 GitHub, GitLab, Bitbucket 等平台。

![](https://user-images.githubusercontent.com/39191/33507513-f60041ae-d6a9-11e7-985c-ab296d6a5b0f.gif)

安装和使用方式：
```python
# 安装
$ npm install --global git-openstall --global git-openn

$ git open
# opens https://github.com/TRACKED_REMOTE_USER/CURRENT_REPO/tree/CURRENT_BRANCH

$ git open someremote
# opens https://github.com/PROVIDED_REMOTE_USER/CURRENT_REPO/tree/CURRENT_BRANCH

$ git open someremote somebranch
# opens https://github.com/PROVIDED_REMOTE_USER/CURRENT_REPO/tree/PROVIDED_BRANCH

$ git open --issue
# If branches use naming convention of issues/#123,
# opens https://github.com/TRACKED_REMOTE_USER/CURRENT_REPO/issues/123
```
每次能提升一点点效率，就会感到开心~

> 项目地址：https://github.com/paulirish/git-open
