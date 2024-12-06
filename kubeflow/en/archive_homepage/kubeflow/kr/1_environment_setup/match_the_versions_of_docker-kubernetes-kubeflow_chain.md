* Draft: 2020-07-21 (Tue)

# Match the versions of Docker-Kubernetes-Kubeflow Chain

Google search: docker versions compatible with kubernetes

Every Kubernetes release has an External Dependencies section in the respective Changelog. E.g.:

[CHANGELOG-1.14:](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.14.md#external-dependencies)

The list of validated docker versions has changed. 1.11.1 and 1.12.1 have been removed. The current list is 1.13.1, 17.03, 17.06, 17.09, 18.06, 18.09.

[CHANGELOG-1.13:](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.13.md#external-dependencies)

The list of validated docker versions remain unchanged at 1.11.1, 1.12.1, 1.13.1, 17.03, 17.06, 17.09, 18.06 since Kubernetes 1.12.

[CHANGELOG-1.12:](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.12.md#external-dependencies)

The list of validated docker versions was updated to 1.11.1, 1.12.1, 1.13.1, 17.03, 17.06, 17.09, 18.06.

and so on...

[Docker and Kubernetes integrations compatibility matrix?](https://devops.stackexchange.com/questions/2691/docker-and-kubernetes-integrations-compatibility-matrix/6807)

Go to the link and find "dockver version"

For example, [kubernetes/CHANGELOG/CHANGELOG-1.14.md](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.14.md) > [External Dependencies](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.14.md#external-dependencies)
Find the following line with "docker version".

> The list of validated docker versions has changed. 1.11.1 and 1.12.1 have been removed.
> The current list is 1.13.1, 17.03, 17.06, 17.09, 18.06, 18.09. (#72823, #72831)

[kubernetes/CHANGELOG/CHANGELOG-1.15.md](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.15.md) > 

Find the following line with "docker version":
> * The list of validated docker versions remains unchanged.
>   * The current list is 1.13.1, 17.03, 17.06, 17.09, 18.06, 18.09. (#72823, #72831)


--kubernetes-version string     Default: "stable-1"
  Choose a specific Kubernetes version for the control plane.
  
[kubeadm init](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-init/)
