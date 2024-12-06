* Draft: 2021-02-03 (Wed)

# darknet make 명령어 실행 후 pkg-config: not found 에러

## Problem

```bash
# make
mkdir -p obj
mkdir -p backup
mkdir -p results
gcc -Iinclude/ -Isrc/ -DOPENCV `pkg-config --cflags opencv`  -DGPU -I/usr/local/cuda/include/ -Wall -Wno-unused-result -Wno-unknown-pragmas -Wfatal-errors -fPIC -Ofast -DOPENCV -DGPU -c ./src/gemm.c -o obj/gemm.o
/bin/sh: 1: pkg-config: not found
In file included from ./src/utils.h:5:0,
                 from ./src/gemm.c:2:
include/darknet.h:11:14: fatal error: cuda_runtime.h: No such file or directory
     #include "cuda_runtime.h"
              ^~~~~~~~~~~~~~~~
compilation terminated.
Makefile:89: recipe for target 'obj/gemm.o' failed
make: *** [obj/gemm.o] Error 1
#
```

## Solution

```bash
# apt install -y pkg-cfg
```



