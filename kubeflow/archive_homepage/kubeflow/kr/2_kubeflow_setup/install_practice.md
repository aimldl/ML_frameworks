* Draft: 2020-07-13 (Mon)

# Kubeflow 설정 



```bash
$ kubectl version
Client Version: version.Info{Major:"1", Minor:"18", GitVersion:"v1.18.4", GitCommit:"c96aede7b5205121079932896c4ad89bb93260af", GitTreeState:"clean", BuildDate:"2020-06-17T11:41:22Z", GoVersion:"go1.13.9", Compiler:"gc", Platform:"linux/amd64"}
Server Version: version.Info{Major:"1", Minor:"18", GitVersion:"v1.18.5", GitCommit:"e6503f8d8f769ace2f338794c914a96fc335df0f", GitTreeState:"clean", BuildDate:"2020-06-26T03:39:24Z", GoVersion:"go1.13.9", Compiler:"gc", Platform:"linux/amd64"}
$
```

쿠버네티스 버전 1.18이 설치 되어 있습니다.

```bash
Client Version: version.Info{Major:"1", Minor:"18"
Server Version: version.Info{Major:"1", Minor:"18"
```

하지만 이 버전은 Kubeflow와 호환이 되지 않습니다. 쿠버네티스와 쿠브플로우의 버전은 아래 표에 정리되어 있습니다. 

> The recommended Kubernetes version is 1.14. Kubeflow has been validated and tested on Kubernetes 1.14.
>
> - Your cluster must run at least Kubernetes version 1.11.
> - Kubeflow **does not work** on Kubernetes 1.16.
> - Older versions of Kubernetes may not be compatible with the latest Kubeflow versions. The following matrix provides information about compatibility between Kubeflow and Kubernetes versions.

> | Kubernetes Versions | Kubeflow 0.4   | Kubeflow 0.5   | Kubeflow 0.6   | Kubeflow 0.7   | Kubeflow 1.0        |
> | ------------------- | -------------- | -------------- | -------------- | -------------- | ------------------- |
> | 1.11                | **compatible** | **compatible** | incompatible   | incompatible   | incompatible        |
> | 1.12                | **compatible** | **compatible** | incompatible   | incompatible   | incompatible        |
> | 1.13                | **compatible** | **compatible** | incompatible   | incompatible   | incompatible        |
> | 1.14                | **compatible** | **compatible** | **compatible** | **compatible** | **compatible**      |
> | 1.15                | incompatible   | **compatible** | **compatible** | **compatible** | **compatible**      |
> | 1.16                | incompatible   | incompatible   | incompatible   | incompatible   | **no known issues** |
> | 1.17                | incompatible   | incompatible   | incompatible   | incompatible   | **no known issues** |
> | 1.18                | incompatible   | incompatible   | incompatible   | incompatible   | **no known issues** |
>
> - **incompatible**: the combination does not work at all
> - **compatible**: all Kubeflow features have been tested and verified for the Kubernetes version
> - **no known issues**: the combination has not been fully tested but there are no repoted issues
>
> 출처: [ Overview of Deployment on Existing Clusters > Minimum system requirements](https://www.kubeflow.org/docs/started/k8s/overview/#minimum-system-requirements)

쿠버네티스 1.14를 추천하므로 쿠버네티스 재설치를 진행합니다.



## ubeadm, kubelet, kubectl 설치하기

모든 컴퓨터에 kubeadm, kubelet, kubectl를 설치합니다. 

```bash
$ sudo apt-get update && sudo apt-get install -y apt-transport-https curl
$ curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
$ cat <<EOF | sudo tee /etc/apt/sources.list.d/kubernetes.list
deb https://apt.kubernetes.io/ kubernetes-xenial main
EOF
$ sudo apt-get update
$ sudo apt-get install -y kubelet kubeadm kubectl
$ sudo apt-mark hold kubelet kubeadm kubectl
```

The kubelet is now restarting every few seconds, as it waits in a crashloop for kubeadm to tell it what to do.



Google search: uninstall kubernetes

[Kubernetes completely uninstall](https://medium.com/@meysam1369/kubernetes-completely-uninstall-3f2a83dd985d), 2018-08-07, Medium

```bash
$ sudo -i
[sudo] password for k8smaster: 
root@k8smaster-gpu-desktop:~# kubeadm reset
[reset] Reading configuration from the cluster...
#
```

If the cluster is node, First delete it from master

```bash
# kubectl drain <node name> — delete-local-data — force — ignore-daemonsets
# kubectl delete node <node name>
```

> Then remove **kubeadm** completely
>
> ```bash
> kubeadm reset 
> # on debian base 
> sudo apt-get purge kubeadm kubectl kubelet kubernetes-cni kube* 
> #on centos base
> sudo yum remove kubeadm kubectl kubelet kubernetes-cni kube*# on debian base
> sudo apt-get autoremove
> #on centos base
> sudo yum autoremove
>  
> sudo rm -rf ~/.kube
> ```

```bash
# kubeadm reset
# apt-get purge kubeadm kubectl kubelet kubernetes-cni kube*
  ...
# apt-get autoremove
# rm -rf ~/.kube
```



```bash
# kubeadm reset
[reset] Reading configuration from the cluster...
[reset] FYI: You can look at this config file with 'kubectl -n kube-system get cm kubeadm-config -oyaml'
[reset] WARNING: Changes made to this host by 'kubeadm init' or 'kubeadm join' will be reverted.
[reset] Are you sure you want to proceed? [y/N]: y
[preflight] Running pre-flight checks
[reset] Removing info for node "k8smaster-gpu-desktop" from the ConfigMap "kubeadm-config" in the "kube-system" Namespace
{"level":"warn","ts":"2020-07-13T17:16:12.214+0900","caller":"clientv3/retry_interceptor.go:61","msg":"retrying of unary invoker failed","target":"endpoint://client-f2d8c4d4-b080-4b76-a4e4-67d56576d2ac/192.168.0.109:2379","attempt":0,"error":"rpc error: code = Unknown desc = etcdserver: re-configuration failed due to not enough started members"}
{"level":"warn","ts":"2020-07-13T17:16:12.269+0900","caller":"clientv3/retry_interceptor.go:61","msg":"retrying of unary invoker failed","target":"endpoint://client-f2d8c4d4-b080-4b76-a4e4-67d56576d2ac/192.168.0.109:2379","attempt":0,"error":"rpc error: code = Unknown desc = etcdserver: re-configuration failed due to not enough started members"}
{"level":"warn","ts":"2020-07-13T17:16:12.380+0900","caller":"clientv3/retry_interceptor.go:61","msg":"retrying of unary invoker failed","target":"endpoint://client-f2d8c4d4-b080-4b76-a4e4-67d56576d2ac/192.168.0.109:2379","attempt":0,"error":"rpc error: code = Unknown desc = etcdserver: re-configuration failed due to not enough started members"}
{"level":"warn","ts":"2020-07-13T17:16:12.594+0900","caller":"clientv3/retry_interceptor.go:61","msg":"retrying of unary invoker failed","target":"endpoint://client-f2d8c4d4-b080-4b76-a4e4-67d56576d2ac/192.168.0.109:2379","attempt":0,"error":"rpc error: code = Unknown desc = etcdserver: re-configuration failed due to not enough started members"}
{"level":"warn","ts":"2020-07-13T17:16:13.013+0900","caller":"clientv3/retry_interceptor.go:61","msg":"retrying of unary invoker failed","target":"endpoint://client-f2d8c4d4-b080-4b76-a4e4-67d56576d2ac/192.168.0.109:2379","attempt":0,"error":"rpc error: code = Unknown desc = etcdserver: re-configuration failed due to not enough started members"}
{"level":"warn","ts":"2020-07-13T17:16:13.849+0900","caller":"clientv3/retry_interceptor.go:61","msg":"retrying of unary invoker failed","target":"endpoint://client-f2d8c4d4-b080-4b76-a4e4-67d56576d2ac/192.168.0.109:2379","attempt":0,"error":"rpc error: code = Unknown desc = etcdserver: re-configuration failed due to not enough started members"}
{"level":"warn","ts":"2020-07-13T17:16:15.561+0900","caller":"clientv3/retry_interceptor.go:61","msg":"retrying of unary invoker failed","target":"endpoint://client-f2d8c4d4-b080-4b76-a4e4-67d56576d2ac/192.168.0.109:2379","attempt":0,"error":"rpc error: code = Unknown desc = etcdserver: re-configuration failed due to not enough started members"}
{"level":"warn","ts":"2020-07-13T17:16:18.783+0900","caller":"clientv3/retry_interceptor.go:61","msg":"retrying of unary invoker failed","target":"endpoint://client-f2d8c4d4-b080-4b76-a4e4-67d56576d2ac/192.168.0.109:2379","attempt":0,"error":"rpc error: code = Unknown desc = etcdserver: re-configuration failed due to not enough started members"}
{"level":"warn","ts":"2020-07-13T17:16:25.285+0900","caller":"clientv3/retry_interceptor.go:61","msg":"retrying of unary invoker failed","target":"endpoint://client-f2d8c4d4-b080-4b76-a4e4-67d56576d2ac/192.168.0.109:2379","attempt":0,"error":"rpc error: code = Unknown desc = etcdserver: re-configuration failed due to not enough started members"}
{"level":"warn","ts":"2020-07-13T17:16:38.210+0900","caller":"clientv3/retry_interceptor.go:61","msg":"retrying of unary invoker failed","target":"endpoint://client-f2d8c4d4-b080-4b76-a4e4-67d56576d2ac/192.168.0.109:2379","attempt":0,"error":"rpc error: code = Unknown desc = etcdserver: re-configuration failed due to not enough started members"}
{"level":"warn","ts":"2020-07-13T17:17:04.582+0900","caller":"clientv3/retry_interceptor.go:61","msg":"retrying of unary invoker failed","target":"endpoint://client-f2d8c4d4-b080-4b76-a4e4-67d56576d2ac/192.168.0.109:2379","attempt":0,"error":"rpc error: code = Unknown desc = etcdserver: re-configuration failed due to not enough started members"}
W0713 17:17:04.583134     830 removeetcdmember.go:61] [reset] failed to remove etcd member: etcdserver: re-configuration failed due to not enough started members
.Please manually remove this etcd member using etcdctl
[reset] Stopping the kubelet service
[reset] Unmounting mounted directories in "/var/lib/kubelet"
[reset] Deleting contents of config directories: [/etc/kubernetes/manifests /etc/kubernetes/pki]
[reset] Deleting files: [/etc/kubernetes/admin.conf /etc/kubernetes/kubelet.conf /etc/kubernetes/bootstrap-kubelet.conf /etc/kubernetes/controller-manager.conf /etc/kubernetes/scheduler.conf]
[reset] Deleting contents of stateful directories: [/var/lib/etcd /var/lib/kubelet /var/lib/dockershim /var/run/kubernetes /var/lib/cni]

The reset process does not clean CNI configuration. To do so, you must remove /etc/cni/net.d

The reset process does not reset or clean up iptables rules or IPVS tables.
If you wish to reset iptables, you must do so manually by using the "iptables" command.

If your cluster was setup to utilize IPVS, run ipvsadm --clear (or similar)
to reset your system's IPVS tables.

The reset process does not clean your kubeconfig files and you must remove them manually.
Please, check the contents of the $HOME/.kube/config file.

#
```

## 계정 리셋하기

### 마스터용 컴퓨터

Fresh start를 위해서 계정을 리셋하겠습니다. 삭제 전에 필요한 데이터를 백업합니다.

참고: [How to Add and Delete Users on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-add-and-delete-users-on-ubuntu-16-04) > How To Delete a User

#### 기존 k8smaster 계정 삭제

##### Step 1. 루트 계정으로 변환합니다.

```bash
$ sudo -i
[sudo] password for aimldl: 
#
```

##### Step 2. `deluser`명령어로 계정을 삭제합니다.

```bash
# deluser k8smaster
Removing user `k8smaster' ...
Warning: group `k8smaster' has no more members.
Done.
#
```

##### Step 3. 사용자의 홈 디렉토리를 삭제합니다.

계정의 이름이 `k8smaster`이므로 `/home/k8smaster` 디렉토리가 남아있습니다. 이 디렉토리를 수동으로 삭제합니다. 이때 `rm -rf *` 명령어는 디렉토리 밑의 모든 파일을 강제로 삭제하므로 사용 시 각별한 주의가 필요합니다. 실행 전에 원하는 디렉토리가 맞는지 재확인하세요.

```bash
# cd home/
# ls
aimldl  git  k8smaster
# cd k8smaster/
# ls
Desktop    Music     Templates         github     temp4zoom
Documents  Pictures  Videos            snap
Downloads  Public    examples.desktop  temp-soho
# rm -rf *
# ls -al
total 108
drwxr-xr-x 15 1002 1002 4096  7월 14 11:11 .
drwxr-xr-x  5 root root 4096  6월 30 17:46 ..
-rw-------  1 1002 1002  720  7월 10 09:29 .ICEauthority
-rw-------  1 1002 1002  122  7월 13 18:05 .Xauthority
  ...
-rw-------  1 1002 1002 3744  6월 30 18:01 .xsession-errors.old
# rm -rf .*
rm: refusing to remove '.' or '..' directory: skipping '.'
rm: refusing to remove '.' or '..' directory: skipping '..'
# ls -al
total 8
drwxr-xr-x 2 1002 1002 4096  7월 14 11:11 .
drwxr-xr-x 5 root root 4096  6월 30 17:46 ..
# cd ..
# rmdir k8smaster/
# ls
aimldl  git
#
```

#### 신규 k8smaster 계정 생성