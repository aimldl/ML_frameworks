* Draft: 2020-04-16 (Thu)

# (kubeflow.error): Code 500 with message: Apply.Run  Error

## Problem

WARN[0095] Encountered error applying application cert-manager:  (kubeflow.error): Code 500 with message: Apply.Run  Error error when creating "/tmp/kout378745801": Internal error occurred: failed calling webhook "webhook.cert-manager.io": the server is currently unable to handle the request  filename="kustomize/kustomize.go:202"
WARN[0095] Will retry in 14 seconds.                     filename="kustomize/kustomize.go:203"
namespace/cert-manager unchanged
mutatingwebhookconfiguration.admissionregistration.k8s.io/cert-manager-webhook configured

  ...

INFO[0156] Applied the configuration Successfully!       filename="cmd/apply.go:72"
(kubeflow) aimldl@Home-Laptop:~/kubeflow/attractive-outfit-1587018718$ WARN[0095] Encountered error applying application cert-manager:  (kubeflow.error): Code 500 with message: Apply.Run  Error error when creating "/tmp/kout378745801": Internal error occurred: failed calling webhook "webhook.cert-manager.io": the server is currently unable to handle the request  filename="kustomize/kustomize.go:202"
bash: syntax error near unexpected token `('
(kubeflow) aimldl@Home-Laptop:~/kubeflow/attractive-outfit-1587018718$ WARN[0095] Will retry in 14 seconds.                     filename="kustomize/kustomize.go:203"
WARN[0095]: 명령을 찾을 수 없습니다
(kubeflow) aimldl@Home-Laptop:~/kubeflow/attractive-outfit-1587018718$ namespace/cert-manager unchanged
bash: namespace/cert-manager: 그런 파일이나 디렉터리가 없습니다
(kubeflow) aimldl@Home-Laptop:~/kubeflow/attractive-outfit-1587018718$ mutatingwebhookconfiguration.admissionregistration.k8s.io/cert-manager-webhook configured
bash: mutatingwebhookconfiguration.admissionregistration.k8s.io/cert-manager-webhook: 그런 파일이나 디렉터리가 없습니다
(kubeflow) aimldl@Home-Laptop:~/kubeflow/attractive-outfit-1587018718$ WARN[0095] Encountered error applying application cert-manager:  (kubeflow.error): Code 500 with message: Apply.Run  Error error when creating "/tmp/kout378745801": Internal error occurred: failed calling webhook "webhook.cert-manager.io": the server is currently unable to handle the request  filename="kustomize/kustomize.go:202"
bash: syntax error near unexpected token `('
(kubeflow) aimldl@Home-Laptop:~/kubeflow/attractive-outfit-1587018718$ WARN[0095] Will retry in 14 seconds.                     filename="kustomize/kustomize.go:203"
WARN[0095]: 명령을 찾을 수 없습니다
(kubeflow) aimldl@Home-Laptop:~/kubeflow/attractive-outfit-1587018718$ namespace/cert-manager unchanged
bash: namespace/cert-manager: 그런 파일이나 디렉터리가 없습니다
(kubeflow) aimldl@Home-Laptop:~/kubeflow/attractive-outfit-1587018718$ mutatingwebhookconfiguration.admissionregistration.k8s.io/cert-manager-webhook configured
bash: mutatingwebhookconfiguration.admissionregistration.k8s.io/cert-manager-webhook: 그런 파일이나 디렉터리가 없습니다



### Solution

Adding "export AWS_REGION=us-west-2" solved the problem.

```bash
$ export AWS_REGION=us-west-2
$ export AWS_SDK_LOAD_CONFIG=1
$ kfctl apply -V -f kfctl_aws.yaml
```