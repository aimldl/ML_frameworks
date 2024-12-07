Q: Is EKS CLUSTER NAME different from AWS_CLUSTER_NAME?

Q: Should I use /opt?

A: Permission denied.

$ mkdir -p ${KF_DIR}
mkdir: `/opt//adorable-lagomorph' 디렉토리를 만들 수 없습니다: 허가 거부

### Choosing the Right Configuration for YouYAML File

There are two options for AWS: the standard setup and authentication. 

| Deployment platform         | Manifest                                                     |
| --------------------------- | ------------------------------------------------------------ |
| AWS with the standard setup | [kfctl_aws.v1.0.1.yaml](https://raw.githubusercontent.com/kubeflow/manifests/v1.0-branch/kfdef/kfctl_aws.v1.0.1.yaml) |
| AWS with authentication     | [kfctl_aws_cognito.v1.0.1.yaml](https://raw.githubusercontent.com/kubeflow/manifests/v1.0-branch/kfdef/kfctl_aws_cognito.v1.0.1.yaml) |

For the full list of platforms and the corresponding manifest files, refer to [Configuration quick reference](https://www.kubeflow.org/docs/started/getting-started/#configuration-quick-reference).

I would go with the standard setup and then switch to the authentication setup because the former is relatively easier than the latter. From the configuration point of view, the authentication setup requires more information in the later step. For example, the following information needs to be filled in after looking up the information here and there. This adds additional steps and complexity.

```
  plugins:
  - kind: KfAwsPlugin
    metadata:
      name: aws
    spec:
      auth:
        cognito:
          certArn: arn:aws:acm:us-west-2:xxxxx:certificate/xxxxxxxxxxxxx-xxxx
          cognitoAppClientId: xxxxxbxxxxxx
          cognitoUserPoolArn: arn:aws:cognito-idp:us-west-2:xxxxx:userpool/us-west-2_xxxxxx
          cognitoUserPoolDomain: your-user-pool
      region: us-west-2
      roles:
      - eksctl-kubeflow-aws-nodegroup-ng-a2-NodeInstanceRole-xxxxx

```



The difference in the manifest files between two setups is compared below. A lot more items are common in both files.

| kfctl_aws.v1.0.1.yaml                                        | kfctl_aws_cognito.v1.0.1.yaml                                |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| - kustomizeConfig:   parameters:   - name: clusterRbacConfig    value: 'OFF'   repoRef:     name: manifests    path: istio/istio  name: istio | - kustomizeConfig:   parameters:   - name: clusterRbacConfig    value: 'ON'   repoRef:    name: manifests    path: istio/istio  name: istio |
| - kustomizeConfig:   parameters:   - name: namespace    value: istio-system   repoRef:    name: manifests    path: istio/add-anonymous-user-filter  name: add-anonymous-user-filter | - kustomizeConfig:                                           |
| - kustomizeConfig:   overlays:   - istio   - application     repoRef:    name: manifests    path: common/centraldashboard  name: centraldashboard | - kustomizeConfig:   overlays:   - istio   - application   parameters:   - name: userid-header    value: kubeflow-userid   repoRef:    name: manifests    path: common/centraldashboard  name: centraldashboard |
| - kustomizeConfig:   overlays:   - application   parameters:    - name: minioPvcName    value: minio-pv-claim   repoRef:    name: manifests    path: pipeline/minio  name: minio | - kustomizeConfig:   overlays:   - application   parameters:   - name: minioPvName    value: minio-pv   - name: minioPvcName    value: minio-pv-claim   repoRef:    name: manifests    path: pipeline/minio  name: minio |
| - kustomizeConfig:   overlays:   - application   parameters:            - name: mysqlPvcName    value: mysql-pv-claim   repoRef:    name: manifests    path: pipeline/mysql  name: mysql | - kustomizeConfig:   overlays:   - application   parameters:   - name: mysqlPvName    value: mysql-pv   - name: mysqlPvcName    value: mysql-pv-claim   repoRef:    name: manifests    path: pipeline/mysql  name: mysql |
| - kustomizeConfig:   overlays:   - application   - istio     repoRef:    name: manifests    path: profiles  name: profiles | - kustomizeConfig:   overlays:   - application   - istio   parameters:   - name: userid-header    value: kubeflow-userid   repoRef:    name: manifests    path: profiles  name: profiles |
|                                                              | - kustomizeConfig:   overlays:   - cognito   parameters:   - name: namespace    value: istio-system   repoRef:    name: manifests    path: aws/istio-ingress  name: istio-ingress |
|                                                              | - kustomizeConfig:   overlays:   - application   parameters:    - name: namespace    value: istio-system   - name: origin-header    value: x-amzn-oidc-data   - name: custom-header    value: kubeflow-userid   repoRef:    name: manifests    path: aws/aws-istio-authz-adaptor  name: aws-istio-authz-adaptor |
| plugins: - kind: KfAwsPlugin  metadata:   name: aws  spec:   auth:    basicAuth:     password:      name: password     username: admin    region: us-west-2   roles:   - eksctl-kubeflow-aws-nodegroup-ng-a2-NodeInstanceRole-xxxxxxx | plugins: - kind: KfAwsPlugin  metadata:   name: aws  spec:   auth:    cognito:     certArn: arn:aws:acm:us-west-2:xxxxx:certificate/xxxxxxxxxxxxx-xxxx     cognitoAppClientId: xxxxxbxxxxxx     cognitoUserPoolArn: arn:aws:cognito-idp:us-west-2:xxxxx:userpool/us-west-2_xxxxxx     cognitoUserPoolDomain: your-user-pool   region: us-west-2   roles:   - eksctl-kubeflow-aws-nodegroup-ng-a2-NodeInstanceRole-xxxxx |

### Set up your Kubeflow configuration

```
$ mkdir -p ${KF_DIR}
$ cd && tree kubeflow/
kubeflow/
└── adorable-lagomorph

1 directory, 0 files
$ cd ${KF_DIR}
$ wget -O kfctl_aws.yaml $CONFIG_URI
--2020-04-08 13:41:17--  https://raw.githubusercontent.com/kubeflow/manifests/v1.0-branch/kfdef/kfctl_aws_cognito.v1.0.1.yaml
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 151.101.228.133
접속 raw.githubusercontent.com (raw.githubusercontent.com)|151.101.228.133|:443... 접속됨.
HTTP request sent, awaiting response... 200 OK
Length: 8803 (8.6K) [text/plain]
Saving to: ‘kfctl_aws.yaml’

kfctl_aws.yaml           100%[==================================>]   8.60K  --.-KB/s    in 0.06s   

2020-04-08 13:41:18 (145 KB/s) - ‘kfctl_aws.yaml’ saved [8803/8803]

$ export CONFIG_FILE=${KF_DIR}/kfctl_aws.yaml
$
```

### Configure Kubeflow

> In v1.0.1, Kubeflow supports to use [AWS IAM Roles for Service Account](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html) to fine grain control AWS service access. kfctl will create two roles `kf-admin-${cluster_name}` and `kf-user-${cluster_name}` and Kubernetes service account `kf-admin` and `kf-user` under kubeflow namespace. `kf-admin-${cluster_name}` will be assumed by components like `alb-ingress-controller`, `profile-controller` or any Kubeflow control plane components which need to talk to AWS services. `kf-user-${cluster_name}` can be used by user’s application.

kfctl will create two roles and Kubernetes service account under kubeflow namespace.

* Roles: `kf-admin-${cluster_name}`, `kf-user-${cluster_name}` 
* Kubernetes service account: `kf-admin`, `kf-user` 

`kf-admin-${cluster_name}` is assumed by any Kubeflow control plane components which need to talk to AWS services. Examples include `albingress-controller` and `profile-controller`. 

`kf-user-${cluster_name}` is used by user's application.

##### Option 1: Use AWS IAM for Service Account

> `kfctl` will help create or reuse IAM OIDC Identity Provider, create role and handle trust relationship binding with Kubernetes Service Accounts. For details, refer to [AWS IAM Role for Service Account](https://www.kubeflow.org/docs/aws/iam-for-sa/).

Step 1. Change the region to your EKS cluster is located.

```
$ kubectl config view
  ...
      - --region
      - ap-northeast-2
  ...
$
```

Step 2. Add `enablePodIamPolicy: true` in the `${CONFIG_FILE}` file.

Step 3. Delete the key-value of `roles`.

```
      roles:
      - eksctl-kubeflow-aws-nodegroup-ng-a2-NodeInstanceRole-xxxxxxx
```

Before

```
      region: us-west-2
      roles:
      - eksctl-kubeflow-aws-nodegroup-ng-a2-NodeInstanceRole-xxxxxxx
```

<img src="/home/aimldl/github/computing_environments/kubeflow/images/kubeflow-installation-configure_kubeflow-use_iam_for_service_account.png">

After

```
      region: ap-northeast-2
      enablePodIamPolicy: true
```

<img src="/home/aimldl/github/computing_environments/kubeflow/images/kubeflow-installation-configure_kubeflow-use_iam_for_service_account-after.png">

1. I like the default cluster name `kubeflow-aws`. So let's not change it.

```
$ sudo apt install jq
$ aws iam list-roles | jq -r ".Roles[] | select(.RoleName | startswith(\"eksctl\") and contains(\"NodeInstanceRole\")) \
    .RoleName"
eksctl-adorable-creature-15860772-NodeInstanceRole-AIX9FFX3BHVH
eksctl-ridiculous-painting-158609-NodeInstanceRole-XSZPUWSD2JWR
$ 
```

There is not output with`startswith(\"eksctl-$AWS_CLUSTER_NAME\") ` . So it is changed to `startswith(\"eksctl\")`. 

3 can be done. I may use

```
roles:
- eksctl-adorable-creature-15860772-NodeInstanceRole-AIX9FFX3BHVH
```



> ### Option 2: Use Node Group Role
>
> 1. Replace the AWS cluster name in your `${CONFIG_FILE}` file, by changing the value `kubeflow-aws` to `${AWS_CLUSTER_NAME}` in multiple locations in the file. For example, use this `sed` command:
>
>    ```
>    sed -i'.bak' -e 's/kubeflow-aws/'"$AWS_CLUSTER_NAME"'/' ${CONFIG_FILE}
>    ```
>
> 2. Retrieve the AWS Region and IAM role name for your worker nodes. To get the IAM role name for your Amazon EKS worker node, run the following command:
>
>    ```
>    aws iam list-roles \
>        | jq -r ".Roles[] \
>        | select(.RoleName \
>        | startswith(\"eksctl-$AWS_CLUSTER_NAME\") and contains(\"NodeInstanceRole\")) \
>        .RoleName"
>    
>    eksctl-kubeflow-example-nodegroup-ng-185-NodeInstanceRole-1DDJJXQBG9EM6
>    ```
>
>    Note: The above command assumes that you used `eksctl` to create your cluster. If you use other provisioning tools to create your worker node groups, find the role that is associated with your worker nodes in the Amazon EC2 console.
>
> 3. Change cluster region and worker role names in your `${CONFIG_FILE}` file:
>
>    ```
>    region: us-west-2
>    roles:
>    - eksctl-kubeflow-example-nodegroup-ng-185-NodeInstanceRole-1DDJJXQBG9EM6
>    ```
>
> If you have multiple node groups, you will see corresponding number of node group roles. In that case, please provide the role names as an array.

### Deploy Kubeflow

```
$ cd ${KF_DIR}
$ kfctl apply -V -f ${CONFIG_FILE}
```

An error occurs

```
$ kfctl apply -V -f ${CONFIG_FILE}
INFO[0000] No name specified in KfDef.Metadata.Name; defaulting to adorable-lagomorph based on location of config file: /home/aimldl/kubeflow/adorable-lagomorph/kfctl_aws.yaml.  filename="coordinator/coordinator.go:202"
  ...
INFO[0003] You already have cluster setup. Skip creating new eks cluster.   filename="aws/eks.go:95"
Error: failed to apply:  (kubeflow.error): Code 500 with message: coordinator Apply failed for aws:  (kubeflow.error): Code 400 with message: Could not determinte it's EKS cluster MissingRegion: could not find region configuration
Usage:
  kfctl apply -f ${CONFIG} [flags]

Flags:
  -f, --file string   Static config file to use. Can be either a local path:
                      		export CONFIG=./kfctl_gcp_iap.yaml
                      	or a URL:
                      		export CONFIG=https://raw.githubusercontent.com/kubeflow/manifests/v1.0-branch/kfdef/kfctl_gcp_iap.v1.0.0.yaml
                      		export CONFIG=https://raw.githubusercontent.com/kubeflow/manifests/v1.0-branch/kfdef/kfctl_istio_dex.v1.0.0.yaml
                      		export CONFIG=https://raw.githubusercontent.com/kubeflow/manifests/v1.0-branch/kfdef/kfctl_aws.v1.0.0.yaml
                      		export CONFIG=https://raw.githubusercontent.com/kubeflow/manifests/v1.0-branch/kfdef/kfctl_k8s_istio.v1.0.0.yaml
                      	kfctl apply -V --file=${CONFIG}
  -h, --help          help for apply
  -V, --verbose       verbose output default is false

failed to apply:  (kubeflow.error): Code 500 with message: coordinator Apply failed for aws:  (kubeflow.error): Code 400 with message: Could not determinte it's EKS cluster MissingRegion: could not find region configuration
$
```

The following two lines in `ktctl_aws.yaml` are switched after applying it.

Before

```
      region: ap-northeast-2
      enablePodIamPolicy: true
```

After

```
      enablePodIamPolicy: true
      region: ap-northeast-2
```

Run the command to deploy Kubeflow again.

```
$ cd ${KF_DIR}
$ kfctl apply -V -f ${CONFIG_FILE}
```

This didn't work.



```
$ bash echo_env_variables 
  ...
The following two names are supposed to be the same.
AWS_CLUSTER_NAME=adorable-creature-1586077260
KF_NAME =adorable-lagomorph
  ...
$
```



> *Important!!!* By default, these scripts create an AWS Application Load Balancer for Kubeflow that is open to public. This is good for development testing and for short term use, but we do not recommend that you use this configuration for production workloads.
>
> To secure your installation, Follow the [instructions](https://www.kubeflow.org/docs/aws/authentication) to add authentication and authorization.

> Wait for all the resources to become ready in the kubeflow namespace.

```
$ kubectl -n kubeflow get all
```

https://www.kubeflow.org/docs/aws/deploy/install-kubeflow/



TODO: Update the document above

$ export AWS_CLUSTER_NAME="adorable-creature-1234567890"
$ export BASE_DIR=~/kubeflow/
$ export KF_NAME="adorable-lagomorph"

export KF_NAME=${AWS_CLUSTER_NAME}
export KF_DIR=${BASE_DIR}/${KF_NAME}

updated
$ bash echo_env_variables 
PATH=/home/aimldl/anaconda3/bin:/home/aimldl/anaconda3/condabin:/home/aimldl/.local/bin:/home/aimldl/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/usr/lib/jvm/java-12-oracle/bin:/usr/lib/jvm/java-12-oracle/db/bin:/home/aimldl/bin:/home/aimldl/bin
CONFIG_URI=https://raw.githubusercontent.com/kubeflow/manifests/v1.0-branch/kfdef/kfctl_aws.v1.0.1.yaml
The following two names are supposed to be the same.
AWS_CLUSTER_NAME=adorable-creature-1586077260
KF_NAME =adorable-creature-1586077260
BASE_DIR=/home/aimldl/kubeflow/
KF_DIR =KF_DIR

