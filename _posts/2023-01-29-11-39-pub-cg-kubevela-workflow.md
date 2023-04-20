---
layout: post
title: 可独立运行的 KubeVela 声明式工作流引擎
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 kubevela/workflow，该项目在 GitHub 有 100 Star，用一句话介绍该项目就是：“Declarative Workflow of KubeVela which can run as standalone.”，可独立运行的 KubeVela 声明式工作流引擎。

![](https://static.kubevela.net/images/1.6/workflow-arch.png)

kubevela/workflow 是一个开源的 Kubernetes 工作流编排工具。它可以帮助用户在 Kubernetes 集群中管理和调度工作流。该项目提供了一组灵活的 API 和命令行工具，可以轻松地编排、部署和管理工作流。

它还提供了一个可视化的 Web 界面，可以帮助用户直观地了解工作流的运行状态和历史记录。

kubevela/workflow 可以通过 kubectl 插件的形式集成到 Kubernetes 集群中，并支持多种工作流语言，如 YAML、JSON、HCL 和 JSONnet。

另外你可以直接使用 kubevela/workflow 或者通过 SDK 的方式按 IaC 的方式进行使用。以下是更详细的功能介绍：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230325214151759.png)


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=kubevela/workflow&type=Timeline)

### 如何安装使用

kubevela/workflow 可以通过两种方式安装:

1、KubeVela 插件

如果你已经安装了 KubeVela，可以直接通过 addon 安装

```bash
vela addon enable vela-workflow
```

2、使用 Helm 安装:

```bash
helm repo add kubevela https://kubevela.github.io/charts
helm repo update
helm install --create-namespace -n vela-system vela-workflow kubevela/vela-workflow
```


### 使用示例 DEMO

以下是一个使用 kubevela/workflow 创建一个简单工作流的示例代码：

```yaml
apiVersion: core.oam.dev/v1alpha1
kind: WorkflowRun
metadata:
  name: build-push-image
  namespace: default
spec:
  workflowSpec:
   steps:
   # or use kubectl create secret generic git-token --from-literal='GIT_TOKEN=<your-token>'
    - name: create-git-secret
      type: export2secret
      properties:
        secretName: git-secret
        data:
          token: <git token>
    # or use kubectl create secret docker-registry docker-regcred \
    # --docker-server=https://index.docker.io/v1/ \
    # --docker-username=<your-username> \
    # --docker-password=<your-password> 
    - name: create-image-secret
      type: export2secret
      properties:
        secretName: image-secret
        kind: docker-registry
        dockerRegistry:
          username: <docker username>
          password: <docker password>
    - name: build-push
      type: build-push-image
      properties:
        # use your kaniko executor image like below, if not set, it will use default image oamdev/kaniko-executor:v1.9.1
        # kanikoExecutor: gcr.io/kaniko-project/executor:latest
        # you can use context with git and branch or directly specify the context, please refer to https://github.com/GoogleContainerTools/kaniko#kaniko-build-contexts
        context:
          git: github.com/FogDong/simple-web-demo
          branch: main
        image: fogdong/simple-web-demo:v1
        # specify your dockerfile, if not set, it will use default dockerfile ./Dockerfile
        # dockerfile: ./Dockerfile
        credentials:
          image:
            name: image-secret
        # buildArgs:
        #   - key="value"
        # platform: linux/arm
    - name: apply-deploy
      type: apply-deployment
      properties:
        image: fogdong/simple-web-demo:v1
```

以上代码定义了多个工作流步骤，包括导入秘钥（包括 Git、镜像仓库）、build-push、apply-deploy。

可以使用 kubectl apply 命令将该工作流部署到 Kubernetes 集群中:
```bash
$ kubectl apply -f workflow.yaml
```

然后使用 kubectl get 命令查看工作流的状态:
```bash
$ kubectl get wf
```

您也可以使用 kubectl logs 命令查看工作流的日志:
```bash
$ kubectl logs -f <workflow-name> -n <namespace>
```

请注意，您需要替换 <workflow-name> 和 <namespace> 为实际的值。


更多项目详情请查看如下链接。

开源项目地址：https://github.com/kubevela/workflow 

开源项目作者：kubevela

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=kubevela/workflow)



关注我们，一起探索有意思的开源项目。
