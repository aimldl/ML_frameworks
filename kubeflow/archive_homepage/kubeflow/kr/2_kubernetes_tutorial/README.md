* Rev.1: 2020-07-21 (Tue)
* Draft: 2020

# Kubernetes Tutorial


```bash
$ kubeadm version
kubeadm version: &version.Info{Major:"1", Minor:"18", GitVersion:"v1.18.6", GitCommit:"dff82dc0de47299ab66c83c626e08b245ab19037", GitTreeState:"clean", BuildDate:"2020-07-15T16:56:34Z", GoVersion:"go1.13.9", Compiler:"gc", Platform:"linux/amd64"}

$ kubectl version
Client Version: version.Info{Major:"1", Minor:"18", GitVersion:"v1.18.6", GitCommit:"dff82dc0de47299ab66c83c626e08b245ab19037", GitTreeState:"clean", BuildDate:"2020-07-15T16:58:53Z", GoVersion:"go1.13.9", Compiler:"gc", Platform:"linux/amd64"}
Server Version: version.Info{Major:"1", Minor:"18", GitVersion:"v1.18.6", GitCommit:"dff82dc0de47299ab66c83c626e08b245ab19037", GitTreeState:"clean", BuildDate:"2020-07-15T16:51:04Z", GoVersion:"go1.13.9", Compiler:"gc", Platform:"linux/amd64"}

$ kubectl cluster-info
Kubernetes master is running at https://192.168.0.109:6443
KubeDNS is running at https://192.168.0.109:6443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.

$ kubectl get nodes
NAME                            STATUS   ROLES    AGE     VERSION
k8smaster-alienware-aurora-r6   Ready    master   6h36m   v1.18.6

$ kubectl get nodes
NAME                             STATUS   ROLES    AGE    VERSION
k8smaster-alienware-aurora-r6    Ready    master   7h4m   v1.18.6
k8snode-01-alienware-aurora-r7   Ready    <none>   93s    v1.18.6
$
```

While the `minikube start` command launches the virtual kubernetes server environment, there is no such a thing as `kubeadm start`.
```bash
$ kubeadm start
unknown command "start" for "kubeadm"
To see the stack trace of this error execute with --v=5 or higher
$
```

* [Tutorials](https://kubernetes.io/docs/tutorials/)
  * [Learn Kubernetes Basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/)
  * [Using kubectl to Create a Deployment](https://kubernetes.io/docs/tutorials/kubernetes-basics/deploy-app/deploy-intro/)
  * [Viewing Pods and Nodes](https://kubernetes.io/docs/tutorials/kubernetes-basics/explore/explore-intro/)
  * [Interactive Tutorial - Exploring Your App](https://kubernetes.io/docs/tutorials/kubernetes-basics/explore/explore-interactive/)
  
  
