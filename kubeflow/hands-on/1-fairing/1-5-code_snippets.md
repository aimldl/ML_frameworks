

fairing.config.set_preprocessor

* 이미지 생성 필요 정보를 정의

fairing.config.set_builder

* 컨테이너 이미지 빌드 

fairing.config.set_deployer

* 컨테이너 이미지 배포
* 배포자 타입
  * TfJob : Kubeflow의 TFJob 컴포넌트를 사용하여 텐서플로우 학습 작업을 시작
  * PyTorchJob : Kubeflow의 PyTorchJob 컴포넌트를 사용하여 PyTorch 학습 작업을 시작
  * Job : 쿠버네티스 Job 리소스를 사용하여 학습 작업을 시작
  * GCPJob : GCP에게 학습 작업 전달
  * Serving : 쿠버네티스의 디플로이먼트와 서비스를 사용하여, 예측(prediction) 엔드포인트를 서빙
  * KFServing : KFServing을 사용하여, 예측(prediction) 엔드포인트를 서빙

```python
fairing.config.set_preprocessor('python', command=command, path_prefix="/app", output_map=output_map)

fairing.config.set_builder(name='docker', registry=DOCKER_REGISTRY, image_name="mnist",
                           base_image="", dockerfile_path="Dockerfile")

fairing.config.set_deployer(name='tfjob', namespace=my_namespace, stream_log=False, 
                            job_name=tfjob_name,chief_count=num_chief, ps_count=num_ps, 
                            worker_count=num_workers,  
                            pod_spec_mutators=[mounting_pvc(pvc_name=pvc_name,
                                                            pvc_mount_path=model_dir),
                                               mounting_pvc(pvc_name=pvc_data_name,
                                                            pvc_mount_path=data_dir),
                                               get_resource_mutator(cpu=90, memory=600),
                                               get_resource_mutator(gpu=1, 
                                                                    gpu_vendor='nvidia')]
                           )
fairing.config.run()
```







- Step 3: Create a namespace to run the MNIST on-prem notebook
      [iap@iap01 ~]$ k get ns yoosung-jeon --show-labels | egrep serving.kubeflow.org/inferenceservice=enabled
      yoosung-jeon   Active   2d5h   ...,istio-injection=disabled,...,serving.kubeflow.org/inferenceservice=enabled
      [iap@iap01 ~]$



- Step 5: Configure kubernetes 
          
- 
          
- ​    Kubernetes TFJobs 리소스를 생성하기 위하여 kubernetes 환경 설정
          ​        Context: 권한을 제한하기 위하여 kubernetes-admin 대신 yoosung-jeon를 생성 
          ​        관련 API: fairing.config.set_deployer(name='tfjob',...)
          (mlpipeline) yoosungjeon@ysjeon-Dev ~ % vi ~/.kube/config
      apiVersion: v1
      clusters:
      
      - cluster:
          certificate-authority-data: LS0tLS1CRUdJTiBDRVJUSUZJQ0F...
          server: https://14.52.244.136:7443
        name: kubernetes
          contexts:
      - context:
          cluster: kubernetes
          user: default$ kubectl config get-contexts
          CURRENT   NAME                          CLUSTER      AUTHINFO           NAMESPACE
        *         kubernetes-admin@kubernetes   kubernetes   kubernetes-admin  
      - namespace: yoosung-jeon
          name: yoosung-jeon-context
          current-context: yoosung-jeon-context
          kind: Config
        preferences: {}
          users:
      - name: default
        user:
          token: eyJhbGciOiJSUzI1NiIsImtpZCI6Inl5dzc5RHpNZHJ5T3hrWHhsV1VoZm5...
        (base) yoosungjeon@ysjeon-Dev ~ % k config get-contexts
        CURRENT   NAME                   CLUSTER      AUTHINFO     NAMESPACE
      *         yoosung-jeon-context   kubernetes   default      yoosung-jeon
      (base) yoosungjeon@ysjeon-Dev ~ %



```bash
$ kubectl config get-contexts
CURRENT   NAME                          CLUSTER      AUTHINFO           NAMESPACE
*         kubernetes-admin@kubernetes   kubernetes   kubernetes-admin  
$
```

- Step 6: create PVs & Docker credential in Kubernetes

- - Kubernetes POD 생성시 사용할 Docker private registry의 credential 정보를 생성

​     [iap@iap01 ~]$ k create secret docker-registry agp-reg-cred -n yoosung-jeon \

​                 --docker-server=repo.acp.kt.co.kr --docker-username=agp --docker-password=Agp12345

​     [iap@iap01 ~]$ k patch serviceaccount default -n yoosung-jeon -p "{\"imagePullSecrets\": [{\"name\": \"agp-reg-cred\"}]}"





```bash
$ kubectl create secret docker-registry agp-reg-cred -n admin --docker-server=repo.acp.kt.co.kr --docker-username=agp --docker-password=Agp12345
secret/agp-reg-cred created
$
```



Check

```bash
$ kubectl get secret
NAME                  TYPE                                  DATA   AGE
default-token-hfht7   kubernetes.io/service-account-token   3      321d
istio.default         istio.io/key-and-cert                 3      49d
my-harbor             kubernetes.io/dockerconfigjson        1      200d
mypriregistry         kubernetes.io/dockerconfigjson        1      212d
mysql-pass            Opaque                                1      200d
mysql-password        Opaque                                1      212d
$
```



```bash
$ kubectl get secret -n admin
NAME                         TYPE                                  DATA   AGE
agp-reg-cred                 kubernetes.io/dockerconfigjson        1      45s
default-editor-token-8mqzw   kubernetes.io/service-account-token   3      36d
default-token-fw2dh          kubernetes.io/service-account-token   3      36d
default-viewer-token-n5sjd   kubernetes.io/service-account-token   3      36d
istio.default                istio.io/key-and-cert                 3      36d
istio.default-editor         istio.io/key-and-cert                 3      36d
istio.default-viewer         istio.io/key-and-cert                 3      36d
mlpipeline-minio-artifact    Opaque                                2      36d
$
```





```bash
$ kubectl patch serviceaccount default -n admin -p "{\"imagePullSecrets\": [{\"name\": \"agp-reg-cred\"}]}"
serviceaccount/default patched
$
```

Q: 확인?

```
$ kubectl edit serviceaccount default -n admin
```



```yaml
imagePullSecrets:
- name: agp-reg-cred
```



```yaml
# Please edit the object below. Lines beginning with a '#' will be ignored,
# and an empty file will abort the edit. If an error occurs while saving this file will be
# reopened with the relevant failures.
#
apiVersion: v1
imagePullSecrets:
- name: agp-reg-cred
kind: ServiceAccount
metadata:
  creationTimestamp: "2021-05-17T01:00:12Z"
  name: default
  namespace: admin
  resourceVersion: "431393541"
  selfLink: /api/v1/namespaces/admin/serviceaccounts/default
  uid: dac0df8b-8596-420b-b365-61f535231aa7
secrets:
- name: default-token-fw2dh
```



- - mnist 어플리케이션에서 사용할 Physical Volume과 학습/검증 데이터 생성

```bash
$ cat mnist-pvc-nfs.yaml
```



```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
name: mnist-pvc
namespace: yoosung-jeon
spec:
accessModes:
- ReadWriteMany
resources:
requests:
storage: 1Gi
storageClassName: nfs-sc-iap
```







```bash
$ cat mnist-data-pvc-nfs.yaml
```



```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
name: mnist-data-pvc
namespace: yoosung-jeon
spec:
accessModes:
- ReadWriteMany
resources:
requests:
storage: 1Gi
storageClassName: nfs-sc-iap
```



```bash
$ k apply -f mnist-data-pvc-nfs.yaml
$ k apply -f mnist-pvc-nfs.yaml
```



```bash
$ kubectl apply -f mnist-data-pvc-nfs.yaml
error: error validating "mnist-data-pvc-nfs.yaml": error validating data: [ValidationError(PersistentVolumeClaim): unknown field "accessModes" in io.k8s.api.core.v1.PersistentVolumeClaim, ValidationError(PersistentVolumeClaim): unknown field "name" in io.k8s.api.core.v1.PersistentVolumeClaim, ValidationError(PersistentVolumeClaim): unknown field "namespace" in io.k8s.api.core.v1.PersistentVolumeClaim, ValidationError(PersistentVolumeClaim): unknown field "storage" in io.k8s.api.core.v1.PersistentVolumeClaim, ValidationError(PersistentVolumeClaim): unknown field "storageClassName" in io.k8s.api.core.v1.PersistentVolumeClaim]; if you choose to ignore these errors, turn validation off with --validate=false
$
```



```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: mnist-data-pvc
  namespace: yoosung-jeon
spec:
  accessModes:
  - ReadWriteMany
  resources:
    requests:
      storage: 1Gi
  storageClassName: nfs-sc-iap
```





```bash
$ kubectl apply -f mnist-data-pvc-nfs.yaml
error: error parsing mnist-data-pvc-nfs.yaml: error converting YAML to JSON: yaml: line 9: could not find expected ':'
$
```



```yaml
$ kubectl apply -f mnist-data-pvc-nfs.yaml
error: error validating "mnist-data-pvc-nfs.yaml": error validating data: [ValidationError(PersistentVolumeClaim): unknown field "\u00a0 accessModes" in io.k8s.api.core.v1.PersistentVolumeClaim, ValidationError(PersistentVolumeClaim): unknown field "\u00a0 name" in io.k8s.api.core.v1.PersistentVolumeClaim, ValidationError(PersistentVolumeClaim): unknown field "\u00a0 namespace" in io.k8s.api.core.v1.PersistentVolumeClaim, ValidationError(PersistentVolumeClaim): unknown field "\u00a0 storageClassName" in io.k8s.api.core.v1.PersistentVolumeClaim, ValidationError(PersistentVolumeClaim): unknown field "\u00a0 \u00a0 \u00a0 storage" in io.k8s.api.core.v1.PersistentVolumeClaim]; if you choose to ignore these errors, turn validation off with --validate=false
$
```





```bash
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: mnist-data-pvc
  namespace: yoosung-jeon
spec:
  accessModes: ReadWriteMany
  resources:
    requests:
      storage: 1Gi
  storageClassName: nfs-sc-iap
```



https://kubernetes.io/docs/concepts/storage/persistent-volumes/

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: mnist-data-pvc
  namespace: admin
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
  storageClassName: nfs-sc-iap
```



```bash
$ kubectl apply -f mnist-data-pvc-nfs.yaml 
error: error validating "mnist-data-pvc-nfs.yaml": error validating data: [ValidationError(PersistentVolumeClaim): unknown field "\u00a0 name" in io.k8s.api.core.v1.PersistentVolumeClaim, ValidationError(PersistentVolumeClaim): unknown field "\u00a0 namespace" in io.k8s.api.core.v1.PersistentVolumeClaim]; if you choose to ignore these errors, turn validation off with --validate=false
$
```



```bash
$ kubectl apply -f mnist-data-pvc-nfs.yaml 
persistentvolumeclaim/mnist-data-pvc created
$
```



```bash
$ kubectl get persistentvolumeclaim -n admin
NAME              STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
mnist-data-pvc    Bound    pvc-93b47a74-33ff-487b-bcdb-fc301ace6775   1Gi        RWO            nfs-sc-iap     57s
workspace-study   Bound    pvc-5fd6093e-fb62-498a-95c9-dc11a6b59eb3   10Gi       RWO            nfs-sc-iap     3h2m
$
```



```bash
$ k apply -f mnist-pvc-nfs.yaml
```



```bash
$ kubectl apply -f mnist-pvc-nfs.yaml
persistentvolumeclaim/mnist-pvc created
(base) aimldl@aimldl-homelaptop:~/다운로드/kubeflow_fairing$ kubectl get pvc -n admin
NAME              STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
mnist-data-pvc    Bound    pvc-93b47a74-33ff-487b-bcdb-fc301ace6775   1Gi        RWO            nfs-sc-iap     16m
mnist-pvc         Bound    pvc-f73761fd-372d-4662-93d4-b229d50b3687   1Gi        RWX            nfs-sc-iap     15s
$
```



```bash
$ kubectl get pvc -n admin | egrep mnist
mnist-data-pvc    Bound    pvc-93b47a74-33ff-487b-bcdb-fc301ace6775   1Gi        RWO            nfs-sc-iap     17m
mnist-pvc         Bound    pvc-f73761fd-372d-4662-93d4-b229d50b3687   1Gi        RWX            nfs-sc-iap     62s
$
```



```bash
$ docker login repo.acp.kt.co.kr
Authenticating with existing credentials...
WARNING! Your password will be stored unencrypted in /home/aimldl/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
(base) aimldl@aimldl-homelaptop:~/다운로드/kubeflow_fairing$ kubectl create secret --help
Create a secret using specified subcommand.

Available Commands:
  docker-registry Create a secret for use with a Docker registry
  generic         Create a secret from a local file, directory or literal value
  tls             Create a TLS secret

Usage:
  kubectl create secret [flags] [options]

Use "kubectl <command> --help" for more information about a given command.
Use "kubectl options" for a list of global command-line options (applies to all commands).
(base) aimldl@aimldl-homelaptop:~/다운로드/kubeflow_fairing$ cat /home/aimldl/.docker/config.json
{
	"auths": {
		"repo.acp.kt.co.kr": {
			"auth": "YWdwOkFncDEyMzQ1"
		}
	}
}(base) aimldl@aimldl-homelaptop:~/다운로드/kubeflow_fairing$ 

```

