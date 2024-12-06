* Draft: 2021-01-31 (Sun)

# `No package 'opencv' found`

## Problem

After changing `Makefile` in the `darknet` directory

```bash
$ nano Makefile
```

from the default settings in the top 3 rows

```makefile
GPU=0
CUDNN=0
OPENCV=0
```

to

```makefile
GPU=0
CUDNN=0
OPENCV=1
```

the following errors are observed.

* `No package 'opencv' found`

```bash
$ make
make
gcc -Iinclude/ -Isrc/ -DOPENCV `pkg-config --cflags opencv`  -Wall -Wno-unused-result -Wno-unknown-pragmas -Wfatal-errors -fPIC -Ofast -DOPENCV -c ./src/gemm.c -o obj/gemm.o
Package opencv was not found in the pkg-config search path.
Perhaps you should add the directory containing `opencv.pc'
to the PKG_CONFIG_PATH environment variable
No package 'opencv' found
  ...
^Cmake: *** [Makefile:89: obj/lstm_layer.o] Interrupt
$
```

Obviously, `darknet` won't compile correctly to use OpenCV.

## Hint

