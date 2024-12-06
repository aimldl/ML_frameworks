







## Problem



```bash
# make
  ...
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
#
```

