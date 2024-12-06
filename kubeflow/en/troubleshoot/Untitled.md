* Draft: 2020-04-20 (Mon)

An error occurred on Amazon EC2 instance (bitnami)

But it looks like this is fine the next time I ran the installation script again.

```
$ ./install_kubeflow
  ...
Requirement already satisfied, skipping upgrade: six>=1.5 in /usr/lib/python2.7/dist-packages (from python-dateutil<3.0.0,>=2.1->botocore==1.15.41->awscli) (1.5.2)
ERROR: boto3 1.9.67 has requirement botocore<1.13.0,>=1.12.67, but you'll have botocore 1.15.41 which is incompatible.
ERROR: boto3 1.9.67 has requirement s3transfer<0.2.0,>=0.1.10, but you'll have s3transfer 0.3.3 which is incompatible.
Installing collected packages: botocore, s3transfer, awscli
  Found existing installation: botocore 1.12.67
    Uninstalling botocore-1.12.67:
      Successfully uninstalled botocore-1.12.67
  Found existing installation: s3transfer 0.1.13
    Uninstalling s3transfer-0.1.13:
      Successfully uninstalled s3transfer-0.1.13
Successfully installed awscli-1.18.41 botocore-1.15.41 s3transfer-0.3.3
  ...
^C
$
```

