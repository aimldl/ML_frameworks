

* Draft: 2020-04-13 (Mon)

## 로컬 환경에 Fairing 설치하기



## AWS CLI 버전 업그레이드 하기

```bash
$ pip install awscli --upgrade --user
```

자세한 내용은 [AWS CLI 설치 및 설정하기](../../aws/cli/INSTALL.md)를 참고하세요.

## Fairing 설치하기

```bash
$ pip install kubeflow-fairing
```

## 에러

fairing을 설치했을 때 버전 이슈로 에러가 발생했습니다.

```bash
$ pip install kubeflow-fairing
Collecting kubeflow-fairing
  ...
ERROR: awscli 1.18.36 has requirement botocore==1.15.36, but you'll have botocore 1.15.39 which is incompatible.
  ...
$
```

설치 후 확인해보니 현재 AWS CLI 버전이 1.18.36인데, 설치된 botocore 1.15.39는 호환이 안 된다는 내용입니다. 8일 전에 AWS CLI를 업데이트를 했지만, 그 사이에 새로운 버전이 나와서 아래처럼 에러가 발생했네요.

```bash
$ aws --version
aws-cli/1.18.36 Python/3.7.7 Linux/4.15.0-96-generic botocore/1.15.39
$
```

AWS CLI의 버전을 업데이트 하면

```bash
$ pip install awscli --upgrade --user
```

aws-cli와 botocore의 버전이 모두 1.15.39로 호환이 되게 되었습니다.

```bash
$ aws --version
aws-cli/1.18.39 Python/3.7.7 Linux/4.15.0-96-generic botocore/1.15.39
$
```

