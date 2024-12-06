

## Hint

> Kubeflow doesn't work on 1.16 yet.
>
> Source: [Error: couldn't apply KfApp: (kubeflow.error): Code 500 with message: kfApp Apply failed for kustomize: (kubeflow.error): Code 500 with message: couldn't create resources from istio-install Error: Timeout: request did not complete within requested timeout 30s #4212](https://github.com/kubeflow/kubeflow/issues/4212)

### [Overview of Deployment on Existing Clusters](https://www.kubeflow.org/docs/started/k8s/overview/)

#### Minimum system requirements

* at least one worker node with a minimum of:
  * 4 CPU
  * 50 GB storage
  * 12 GB memory

The recommended Kubernetes version is 1.14. 

* Kubeflow has been validated and tested on Kubernetes 1.14.
* Your cluster must run at least Kubernetes version 1.11.
* Kubeflow does not work on Kubernetes 1.16.

#### Compatibility between Kubeflow and Kubernetes versions

<img src="images/kubeflow-overview-compatibility_between_kubeflow_and_kubernetes versions-.png">

## Actions

Let's check the Kubernetes version of Amazon EKS.

> Kubernetes version 1.15
>
> **Amazon EKS** now supports **Kubernetes version** 1.15. **Amazon** Elastic **Kubernetes** Service (**EKS**) now supports **Kubernetes version** 1.15 for all clusters. **Kubernetes** is rapidly evolving, with frequent feature releases and bug fixes. The **Kubernetes** 1.15 **release** focuses on stability and maturity of the core feature set.Mar 10, 2020
>
> [Amazon EKS now supports Kubernetes version 1.15](https://aws.amazon.com/about-aws/whats-new/2020/03/amazon-eks-now-supports-kubernetes-version-1-15/?nc1=h_ls)

> ## Available Amazon EKS Kubernetes versions
>
> The following Kubernetes versions are currently available for new clusters in Amazon EKS:
>
> - 1.15.11
> - 1.14.9
> - 1.13.12
> - 1.12.10
>
> [Amazon EKS Kubernetes versions](https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html)

> EKS supports versions `1.12`, `1.13`, `1.14` and `1.15` (default). With `eksctl` you can deploy any of the supported versions by passing `--version`.
>
> ```
> eksctl create cluster --version=1.14
> ```

## Solution

I switched back to version 1.14 for Kubernetes and this problem has been solved! My Kubernetes version was 1.15 (default) which is supported, but not validated and tested by Kubeflow 1.0. 

<img src="images/kubeflow-dashboard-notebook_servers-my-first-notebook-connect_successfully.png">

I've reached this far, but previously "CONNECT" link fails to work.

Tada~ It's successful at this time. I'm so happy because I can move forward.

<img src="images/kubeflow-dashboard-notebook_servers-my-first-notebook-first_success.png">