* Draft: 2021-02-09 (Tue)

# 다크넷을 위한 도커 환경 만드는 방법







```bash
root@0f849469a8df:/home/user/darknet# python -c 'import cv2; print(cv2.__version__)'
bash: python: command not found
root@0f849469a8df:/home/user/darknet# which python
root@0f849469a8df:/home/user/darknet# apt-get install -y python3-dev

...

root@0f849469a8df:/home/user# cd darknet/
root@0f849469a8df:/home/user/darknet# make
gcc -Iinclude/ -Isrc/ -DOPENCV `pkg-config --cflags opencv`  -DGPU -I/usr/local/cuda/include/ -Wall -Wno-unused-result -Wno-unknown-pragmas -Wfatal-errors -fPIC -Ofast -DOPENCV -DGPU -c ./src/gemm.c -o obj/gemm.o
Package opencv was not found in the pkg-config search path.
Perhaps you should add the directory containing `opencv.pc'
to the PKG_CONFIG_PATH environment variable
No package 'opencv' found
In file included from ./src/utils.h:5:0,
                 from ./src/gemm.c:2:
include/darknet.h:11:14: fatal error: cuda_runtime.h: No such file or directory
     #include "cuda_runtime.h"
              ^~~~~~~~~~~~~~~~
compilation terminated.
Makefile:89: recipe for target 'obj/gemm.o' failed
make: *** [obj/gemm.o] Error 1
root@0f849469a8df:/home/user/darknet# nvcc --version
bash: nvcc: command not found
root@0f849469a8df:/home/user/darknet# 
```

