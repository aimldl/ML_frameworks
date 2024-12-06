





## Problem

Google search: No package 'opencv' found

* [Package opencv was not found in the pkg-config search path](https://stackoverflow.com/questions/15320267/package-opencv-was-not-found-in-the-pkg-config-search-path)

> ```
> After installing libopencv-dev in Ubuntu 20.04, the file opencv4.pc was already automatically present in /usr/local/lib/pkgconfig/. The only thing I had to do was to copy (symlink) this fie and cal it opencv.pc – fabian Nov 25 '20 at 18:11
> 
> $ cat /usr/lib64/pkgconfig/opencv.pc
> # Package Information for pkg-config
> 
> prefix=/usr
> exec_prefix=${prefix}
> libdir=${exec_prefix}/lib64
> includedir_old=${prefix}/include/opencv
> includedir_new=${prefix}/include
> 
> Name: OpenCV
> Description: Open Source Computer Vision Library
> Version: 3.1.0
> Libs: -L${exec_prefix}/lib64 -lopencv_shape -lopencv_stitching -lopencv_superres -lopencv_videostab -lopencv_aruco -lopencv_bgsegm -lopencv_bioinspired -lopencv_ccalib -lopencv_cvv -lopencv_dnn -lopencv_dpm -lopencv_fuzzy -lopencv_hdf -lopencv_line_descriptor -lopencv_optflow -lopencv_plot -lopencv_reg -lopencv_saliency -lopencv_stereo -lopencv_structured_light -lopencv_rgbd -lopencv_surface_matching -lopencv_tracking -lopencv_datasets -lopencv_text -lopencv_face -lopencv_video -lopencv_ximgproc -lopencv_calib3d -lopencv_features2d -lopencv_flann -lopencv_xobjdetect -lopencv_objdetect -lopencv_ml -lopencv_xphoto -lopencv_highgui -lopencv_videoio -lopencv_imgcodecs -lopencv_photo -lopencv_imgproc -lopencv_core
> Libs.private: -L/usr/lib64 -lQt5Test -lQt5Concurrent -lQt5OpenGL -L/lib64 -lwebp -lpng -ltiff -ljasper -ljpeg -lImath -lIlmImf -lIex -lHalf -lIlmThread -lgdal -lgstvideo-1.0 -lgstapp-1.0 -lgstbase-1.0 -lgstriff-1.0 -lgstpbutils-1.0 -lgstreamer-1.0 -lucil -lunicap -lpangoft2-1.0 -lpango-1.0 -lgobject-2.0 -lfontconfig -lfreetype -lglib-2.0 -ldc1394 -lv4l1 -lv4l2 -lgphoto2 -lgphoto2_port -lexif -lQt5Core -lQt5Gui -lQt5Widgets -lhdf5_hl -lhdf5 -lz -ldl -lm -ltesseract -llept -lpthread -lrt -lGLU -lGL
> Cflags: -I${includedir_old} -I${includedir_new}
> ```

`opencv.pc`를 `/usr/lib64/pkgconfig/`에 수동으로 만들어줬습니다.

```bash
After installing libopencv-dev in Ubuntu 20.04, the file opencv4.pc was already automatically present in /usr/local/lib/pkgconfig/. The only thing I had to do was to copy (symlink) this fie and cal it opencv.pc – fabian Nov 25 '20 at 18:11$ make
  ...
./src/image_opencv.cpp:5:10: fatal error: opencv2/opencv.hpp: No such file or directory
 #include "opencv2/opencv.hpp"
          ^~~~~~~~~~~~~~~~~~~~
compilation terminated.
Makefile:86: recipe for target 'obj/image_opencv.o' failed
make: *** [obj/image_opencv.o] Error 1
$
```

