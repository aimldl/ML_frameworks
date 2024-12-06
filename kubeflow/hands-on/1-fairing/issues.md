ImagePushSecrets



- Step 6: create PVs & Docker credential in Kubernetes

- - Kubernetes POD 생성시 사용할 Docker private registry의 credential 정보를 생성

​     [iap@iap01 ~]$ k create secret docker-registry agp-reg-cred -n yoosung-jeon \

​                 --docker-server=repo.acp.kt.co.kr --docker-username=agp --docker-password=Agp12345

​     [iap@iap01 ~]$ k patch serviceaccount default -n yoosung-jeon -p "{\"imagePullSecrets\": [{\"name\": \"agp-reg-cred\"}]}"



Fairing

Python library 만들어서 run하도록 만들면 될 듯...

KT Fairing API library

제일 앞서나가고 있다.

Harbor가 쓰기 좋다.

- docker, Helm chart가 지원된다.

Nexus보다... Repo. 

Nexus에서 Public repo 관리가 유료

Chelsea Nexus repo



Helm을 왜 쓰나?

k8s 

Helm chart는 



Harbor에 올릴 때 diff만 하나?

