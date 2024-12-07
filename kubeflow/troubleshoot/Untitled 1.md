* Draft: 2020-04-20 (Mon)

I can't run eksctl on Amazon EC2 instance (bitnami)



```
$ ./install_kubeflow
  ...
---------------
  EKS cluster  
---------------
grep: /home/bitnami/.kube/config: No such file or directory
There is an existing Amazon EKS cluster: 
Create a new cluster ([y]/n)?y
Creating a new EKS cluster takes 10~15+ minutes.
For details, refer to https://eksctl.io/
Specifically, https://eksctl.io/usage/creating-and-managing-clusters/
[ℹ]  eksctl version 0.17.0
[ℹ]  using region us-west-2
Error: getting availability zones: getting availability zones for us-west-2: UnauthorizedOperation: You are not authorized to perform this operation.
	status code: 403, request id: d362c7e5-6885-41cf-bca0-38440706668c
grep: /home/bitnami/.kube/config: No such file or directory
 is created
  ...
$
```

