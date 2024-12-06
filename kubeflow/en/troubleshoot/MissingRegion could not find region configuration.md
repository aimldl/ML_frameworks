##### aimldl/computing_environments/kubeflow/troubleshoot/MissingRegion could not find region configuration.md

* Draft: 2020-04-13 (Mon)

# MissingRegion: could not find region configuration

## Problem

Could not determinte it's EKS cluster MissingRegion: could not find region configuration

```bash
$ echo $CONFIG_FILE
/home/aimldl/kubeflow//adorable-lagomorph-2020-04-13/kfctl_aws.yaml
$ kfctl apply -V -f ${CONFIG_FILE}
  ...
INFO[0001] You already have cluster setup. Skip creating new eks cluster.   filename="aws/eks.go:95"
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

## Hint

Google search: "Could not determinte it's EKS cluster MissingRegion: could not find region configuration"

[Could not determinte it's EKS cluster MissingRegion: could not find region configuration #4854](https://github.com/kubeflow/kubeflow/issues/4854) by [kubeflow](https://github.com/kubeflow)/**[kubeflow](https://github.com/kubeflow/kubeflow)**

> [PatrickXYS](https://github.com/PatrickXYS)
>
> a quick workaround for this issue is:
>
> ```
> export AWS_SDK_LOAD_CONFIG=1 
> ```
>
> This can make session read configuration information from config file (`~/.aws/config`).

> [@apryiomka](https://github.com/apryiomka) Since according to the [AWS SDK Go doc](https://docs.aws.amazon.com/es_es/sdk-for-go/v1/developer-guide/configuring-sdk.html), we should set the region with
>
> ```
> export AWS_REGION=us-west-2
> ```
>
> For reference:
> [![image](https://user-images.githubusercontent.com/23116624/76907782-562c8d00-6864-11ea-9844-a4bc74390142.png)](https://user-images.githubusercontent.com/23116624/76907782-562c8d00-6864-11ea-9844-a4bc74390142.png)
>
> But this is just for workaround, I'll fix it in the PR and you can see it in the next patch revision of `kfctl`.

## Solution

```bash
$ aws configure set default.region us-west-2
$ export AWS_SDK_LOAD_CONFIG=1
$ kfctl apply -V -f kfctl_aws.yaml
  ...
INFO[0098] Applied the configuration Successfully!       filename="cmd/apply.go:72"
$
```

  or

```bash
$ export AWS_REGION=us-west-2
$ export AWS_SDK_LOAD_CONFIG=1
$ kfctl apply -V -f kfctl_aws.yaml
  ...
INFO[0098] Applied the configuration Successfully!       filename="cmd/apply.go:72"
$
```

