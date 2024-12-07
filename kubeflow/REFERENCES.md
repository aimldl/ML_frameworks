* Draft: 2020-04-17 (Fri)

# References

[Kubeflow on AWS](https://www.kubeflow.org/docs/aws/) & [AWS for Kubeflow](https://www.kubeflow.org/docs/started/cloud/getting-started-aws/), Kubeflow Official Website

* [Deployment](https://www.kubeflow.org/docs/aws/deploy/): Instructions for deploying Kubeflow on AWS

  * ##### [Install Kubeflow](https://www.kubeflow.org/docs/aws/deploy/install-kubeflow/)

  * ##### [Uninstall Kubeflow](https://www.kubeflow.org/docs/aws/deploy/uninstall-kubeflow/)

[eksctl 명령줄 유틸리티](https://docs.aws.amazon.com/ko_kr/eks/latest/userguide/eksctl.html)

* [Kubeflow on Amazon EKS](https://aws.amazon.com/ko/blogs/opensource/kubeflow-amazon-eks/), Eng-Hwa Tan and Arun Gupta, 30 SEP 2018
*  This blog post is out-dated which means not all the lines may work.
* In actuality,
  * https://raw.githubusercontent.com/NVIDIA/k8s-device-plugin/v1.10/nvidia-device-plugin.yml
  * `404: Not Found` error occurs.
  * 

[How to setup Kubeflow in AWS](https://medium.com/@vvalouch/how-to-setup-kubeflow-in-aws-a0946f618469)

* This article shares various challenges in the process of installing Kubeflow. I've experienced some of them, but having more items in the list may be helpful in the future.

Found on 2020-04-24 (Fri), Google search: kubeflow how to check the cluster name

* I found this article three days after successfully installing Kubeflow on AWS. Among many fixes I've made, the last piece of puzzle was to use Kubernetes 1.14, not Kubernetes 1.15. In the official website, Kubeflow is compatible with Kubernetes 1.15, but it's actually not! The installation was successful, but Jupyter Server failed to create the "CONNECT" link. I found a work-around and fixed this issue, but another problem came up. I found Kubernetes 1.14 is tested and verified in the same page where the compatibility matrix exists. 
* If I found this article earlier, the installation process might have gone easier for me because the following is mentioned.

> This article assumes the existing AWS account, uses Kubernetes 1.14 and Kubeflow 1.0.

* This sentence might have given me a hint and got me escape from the abyss of debugging something not working well. I might not have tried out all possible ways to fix the issue until I reached the conclusion that Kubernetes 1.15 may not be the wise choice for Kubeflow at this stage.
* Installing Kubeflow on AWS required me the spirit of "not giving up" and "going deeper into the abyss" as well as the general ability to solve problems and debug errors. I thanked I've studied three text books on debugging back in 2011-ish. Making it work all alone was difficult and painful steps.
* To sum, the process of installing Kubeflow was time-consuming and not pleasant experience. I do wish I found this article earlier.

##### [Customizing Kubeflow on AWS](https://www.kubeflow.org/docs/aws/customizing-aws/): Tailoring a AWS deployment of Kubeflow

##### [AWS IAM Role for Service Account](https://www.kubeflow.org/docs/aws/iam-for-sa/)

Setup up IAM Role for Service Account to get fine-grained access control to AWS services

##### [Logging](https://www.kubeflow.org/docs/aws/logging/)

Add logging support for kubeflow

##### [Private Access](https://www.kubeflow.org/docs/aws/private-access/)

How to create private EKS clusters

##### [Authentication and Authorization](https://www.kubeflow.org/docs/aws/authentication/)

Authentication and authorization support for Kubeflow in AWS

##### [Authentication using OIDC](https://www.kubeflow.org/docs/aws/authentication-oidc/)

Authentication and authorization support through OIDC for Kubeflow in AWS

##### [Configure Kubeflow Pipelines on AWS](https://www.kubeflow.org/docs/aws/pipeline/)

Customize Kubeflow Pipelines to use AWS Services

##### [Custom Domain](https://www.kubeflow.org/docs/aws/custom-domain/)

Use a custom domain for Kubeflow on AWS

##### [Storage Options](https://www.kubeflow.org/docs/aws/storage/)

Using EFS and FSx for Lustre with Kubeflow

##### [Troubleshooting Deployments on Amazon EKS](https://www.kubeflow.org/docs/aws/troubleshooting-aws/)

Help diagnose and fix issues you may encounter in your Kubeflow deployment

##### [Kubeflow on AWS Features](https://www.kubeflow.org/docs/aws/features/)

##### [End-to-end Kubeflow on AWS](https://www.kubeflow.org/docs/aws/aws-e2e/)

Running Kubeflow using AWS services



[mojokb/kubeflow-book](https://github.com/mojokb/kubeflow-book)



Jupyter Notebook

[Recommender example for kubeflow](https://github.com/lightbend/kubeflow-recommender)

* An end-to-end example showing how to use Kubeflow for both machine learning and model serving.
* Using [Collaborative filtering](https://en.wikipedia.org/wiki/Collaborative_filtering) to recommend products to the user based on the purchsing history

[Kubeflow – Jupyter Notebooks 살펴보기](https://www.kangwoo.kr/2020/03/08/kubeflow-jupyter-notebooks/), 2020-03-08, [Kim Kangwoo](https://www.kangwoo.kr/)



Google search: reissued from pod/my-first-notebook 1 insufficient cpu 2 insufficient pods

[Documentation](https://www.kubeflow.org/docs/) /  [Jupyter Notebooks](https://www.kubeflow.org/docs/notebooks/)

* ##### [Overview of Jupyter Notebooks in Kubeflow](https://www.kubeflow.org/docs/notebooks/why-use-jupyter-notebook/)

* [Set Up Your Notebooks](https://www.kubeflow.org/docs/notebooks/setup/)

## To-Read List
* [Industrializing AI & Machine Learning Applications with Kubeflow](https://towardsdatascience.com/industrializing-ai-machine-learning-applications-with-kubeflow-5687bf56153f), 2019-09-09, Tianxiang (Ivan) Liu
