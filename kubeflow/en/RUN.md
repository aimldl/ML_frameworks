* Rev. 1: 2020-12-17 (Thu)

# 쿠브플로 실행하기

쿠브플로 설치 완료 후, 쿠브플로를 실행하기 위한 가장 간단한 방법은 `쿠브플로 대쉬보드`로 접속하는 것입니다. `쿠브플로 대쉬보드`는 `Kubeflow UI`라고 불리기도 합니다. 우선 `쿠브플로 대쉬보드`서버를 실행한 후, 클라이언트 프로그램으로 웹브라우저를 통해 접속할 수 있습니다. 아래에 소개되는 내용보다 자세한 사항은 [쿠브플로 대쉬보드 소개](how_to/introducing_kubeflow_central_dashboard.md)를 참고하세요.

## 요약

```bash
$ kfui
```

혹은

```bash
$ kubectl port-forward -n istio-system svc/istio-ingressgateway 8080:80
```

## 쿠브플로 대쉬보드 혹은 Kubeflow UI 서버 실행하기

리눅스 터미널에서 

```bash
$ kubectl port-forward -n istio-system svc/istio-ingressgateway 8080:80
```

를 실행하면 `쿠브플로 대쉬보드`서버가 로컬호스트로 실행됩니다. 로컬호스트의 IP주소는 `127.0.0.1`, URL은 `localhost`입니다. 

```bash
$ kubectl port-forward -n istio-system svc/istio-ingressgateway 8080:80
Forwarding from 127.0.0.1:8080 -> 80
Forwarding from [::1]:8080 -> 80
```

결과 메세지는 8080포트를 80포트로 포워딩 했다는 것을 의미합니다.

## 웹브라우저로 `쿠브플로 대쉬보드`에 접속하기

웹브라우저 주소창에

> http://localhost:8080/

를 입력하면 아래와 같이 `쿠브플로 대쉬보드`, 줄여서 `대쉬보드`에 접속할 수 있습니다. 보다 자세한 내용은 [쿠브플로 대쉬보드 소개](how_to/introducing_kubeflow_central_dashboard.md)를 참고하세요.

<img src="images/kubeflow-dashboard-4.png">

## 실행명령어를 `kfui` alias로 지정하기

`쿠브플로 대쉬보드`를 실행하는 명령어는 길고 복잡하므로 매번 입력하기는 불편합니다.  아래처럼 `kfui`로 alias로 지정하여

```bash
$ alias kfui="kubectl port-forward -n istio-system svc/istio-ingressgateway 8080:80"
```

`kfui` 명령어를 실행하는 것이 더 편리합니다. 

```bash
$ kfui
Forwarding from 127.0.0.1:8080 -> 80
Forwarding from [::1]:8080 -> 80
```

`kubectl port-forward ...`로 시작하는 전체 명령어를 입력한 것과 동일한 결과 메세지를 얻을 수 있습니다. 전체 명령어가 `kfui`명령어로 alias되어도 8080포트가 80포트로 포워딩 되었음을 알 수 있습니다.

## 다음

[쿠브플로우 대쉬보드 소개](how_to/introducing_kubeflow_central_dashboard.md)