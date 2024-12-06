

* Rev.1: 2020-12-17 (Thu)

## 쿠브플로 설치하기 (Installing Kubeflow)

## 코멘트

> In my case, I installed Kubeflow on AWS and this path was a bumpy road. I had to fix many things to make the my-first-notebook work. I had to write a Bash script automating the installation process because I had to try this and that over and over for weeks. The official installation documentation is confusing at first. Some parts are inaccurate and outdated. To make the installation itself successfully, well, I had to collect the correct information piece-by-piece and move forward little by little.

Kubeflow의 설치 과정은 아직까지 상당히 힘듭니다. (2020년 중반을 기준으로) 이유는

* (영문) 공식 설치문서가 완전하지 않아서, 기술적인 문제해결 능력이 요구됩니다. 
* AWS에 설치하는 경우 아직 버그가 리포팅 되고 있어서 난관을 넘어야 합니다. 

웹 상에 있는 많은 문서는 오래 되서 참고 시 큰 도움이 안 됐습니다. 제가 설치할 때 주로 참고한 문서는

* [Installing Kubeflow](https://www.kubeflow.org/docs/started/getting-started/)
* The official installation manual "[Instructions for deploying Kubeflow on AWS with the shell](https://www.kubeflow.org/docs/aws/deploy/install-kubeflow/)"has a couple of defects. Check [troubleshoot/MissingRegion could not find region configuration.md](troubleshoot/MissingRegion could not find region configuration.md) if you encounter MissingRegion error after running:

와 같습니다.

기본적으로 쿠버네티스를 설치한 후에, `kfctl`를 설치해서 YAML파일인 `CONFIG_FILE`을 통해 설치가 진행됩니다.

```
$ kfctl apply -V -f ${CONFIG_FILE}
```

## 퍼블릭 크라우드에 설치하기

AWS (Amazon Web Service)에 설치하는 과정은 [AWS에 Kubeflow 설치하기](INSTALL-AWS.md)를 참고하세요.

## 로컬머신에 쿠브플로 설치하기





## 다음

* [쿠브플로 대쉬보드 소개](how_to/introducing_kubeflow_central_dashboard.md)

* [k9s 설치하기](INSTALL k9s.md)