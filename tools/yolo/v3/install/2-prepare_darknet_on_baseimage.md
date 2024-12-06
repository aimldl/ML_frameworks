





베이스 이미지를 생성합니다.



```bash
$
  ...
Successfully built 3d0a19184aa9
Successfully tagged baseimage-darknet:latest
root@f508e9cee903:/#
```

root@f508e9cee903:/home/user/darknet# nvidia-smi
bash: nvidia-smi: command not found
root@f508e9cee903:/home/user/darknet# 

`user` 디렉토리를 생성합니다.

```bash
root@f508e9cee903:/# ls    
bin   dev  home  lib64  mnt  proc  run   srv  tmp  var
boot  etc  lib   media  opt  root  sbin  sys  usr
root@f508e9cee903:/# cd home/
root@f508e9cee903:/home# ls
root@f508e9cee903:/home# mkdir user
root@f508e9cee903:/home# ls
user
root@f508e9cee903:/home# cd user/
root@f508e9cee903:/home/user# ls
root@f508e9cee903:/home/user#
```

이제부터 본격적인 설치를 위해 필요한 기본 프로그램을 깝니다.

```bash
/home/user# apt update
# apt install -y git
```

CPU only  버전을 컴파일합니다.

 ```bash
root@f508e9cee903:/home/user# git clone https://github.com/pjreddie/darknet.git
root@f508e9cee903:/home/user# cd darknet/
root@f508e9cee903:/home/user/darknet# ls
LICENSE       LICENSE.gen  LICENSE.meta  LICENSE.v1  README.md  data      include  scripts
LICENSE.fuck  LICENSE.gpl  LICENSE.mit   Makefile    cfg        examples  python   src
root@f508e9cee903:/home/user/darknet# make
  ...
nter.o obj/darknet.o libdarknet.a -o darknet -lm -pthread  libdarknet.a
root@f508e9cee903:/home/user/darknet# ls
LICENSE       LICENSE.gpl   LICENSE.v1  backup   data      libdarknet.a   python   src
LICENSE.fuck  LICENSE.meta  Makefile    cfg      examples  libdarknet.so  results
LICENSE.gen   LICENSE.mit   README.md   darknet  include   obj            scripts
root@f508e9cee903:/home/user/darknet#

 ```

`darknet`명령어가 생겼음을 확인할 수 있습니다.



CPU 버전이 돌아가는 것을 확인하기 위해서 웨이츠 파일이 필요합니다. 이미 다운로드 받아놓은 것을 

```bash
$ docker cp yolov3.weights vibrant_jang:/home/user/darknet
$
```

`docker attach`로 돌아갑니다.

```bash
$ docker attach vibrant_jang
root@f508e9cee903:/home/user/darknet# ls
LICENSE       LICENSE.gpl   LICENSE.v1  backup   data      libdarknet.a   python   src
LICENSE.fuck  LICENSE.meta  Makefile    cfg      examples  libdarknet.so  results  yolov3.weights
LICENSE.gen   LICENSE.mit   README.md   darknet  include   obj            scripts
root@f508e9cee903:/home/user/darknet# 
```

실행합니다.

```bash
root@f508e9cee903:/home/user/darknet# ./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg
  ...
Loading weights from yolov3.weights...Done!
data/dog.jpg: Predicted in 15.464110 seconds.
dog: 100%
truck: 92%
bicycle: 99%
root@f508e9cee903:/home/user/darknet# 
```

결과적으로 15.46초 정도가 걸렸습니다.

