* Draft: 2020-08-10 (Mon)

# 1.1. Python 설치하기
Ubuntu Linux에는 Python 2.0 버전이 설치됩니다.

## Python 2.0 버전 제거하기
만약 2.0 버전이 설치되어 있다면 `python --version` 명령어로 확인할 수 있습니다.
```bash
$ python --version
Python 2.7.17
$
```

아래의 2개 명령어로 Python 2.0과 Dependencies를 제거합니다.
```bash
$ sudo apt purge python-dev python-pip 
[sudo] h2o의 암호: 
패키지 목록을 읽는 중입니다... 완료
의존성 트리를 만드는 중입니다       
상태 정보를 읽는 중입니다... 완료
다음 패키지가 자동으로 설치되었지만 더 이상 필요하지 않습니다:
  libpython-all-dev libpython-dev libpython-stdlib libpython2.7-dev python python-all
  python-asn1crypto python-cffi-backend python-crypto python-cryptography python-dbus python-enum34
  python-gi python-idna python-ipaddress python-keyring python-keyrings.alt python-minimal
  python-pkg-resources python-secretstorage python-setuptools python-six python-wheel python-xdg
  python2.7 python2.7-dev python2.7-minimal
Use 'sudo apt autoremove' to remove them.
다음 패키지를 지울 것입니다:
  python-all-dev* python-dev* python-pip*
  ...
$
```

```bash
$ sudo apt autoremove
패키지 목록을 읽는 중입니다... 완료
의존성 트리를 만드는 중입니다       
상태 정보를 읽는 중입니다... 완료
다음 패키지를 지울 것입니다:
  libpython-all-dev libpython-dev libpython-stdlib libpython2.7-dev python python-all
  python-asn1crypto python-cffi-backend python-crypto python-cryptography python-dbus python-enum34
  python-gi python-idna python-ipaddress python-keyring python-keyrings.alt python-minimal
  python-pkg-resources python-secretstorage python-setuptools python-six python-wheel python-xdg
  python2.7 python2.7-dev python2.7-minimal
0개 업그레이드, 0개 새로 설치, 27개 제거 및 0개 업그레이드 안 함.
이 작업 후 54.9 M바이트의 디스크 공간이 비워집니다.
계속 하시겠습니까? [Y/n] y
  ...
$
```

제거된 후에는 다음과 같은 메세지를 출력합니다.

```bash
$ python --version

sudo apt install python3       
sudo apt install python        
sudo apt install python-minimal

You also have python3 installed, you can run 'python3' instead.

$
```

## Python3 실행하기
python3가 있을 경우에
```bash
$ which python3
/usr/bin/python3
```
`python3`명령어를 실행합니다.

```bash
$ python3
Python 3.6.9 (default, Jul 17 2020, 12:50:27) 
[GCC 8.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
$
