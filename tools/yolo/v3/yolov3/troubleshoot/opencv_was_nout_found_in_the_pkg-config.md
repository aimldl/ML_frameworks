

* Draft: 2021-02-02 (Tue)

> # [opencv was not found in the pkg-config](https://askubuntu.com/questions/1289550/opencv-was-not-found-in-the-pkg-config)
>
> Using `cmake` and `cuda` i create `opencv` , the file was saved in
>
> ```
> /usr/local/lib/python3.8/dist-packages/cv2/python-3.8/cv2.so
> ```
>
> now i'm trying to install `darknet` but i got this error
>
> Package `opencv` was not found in the `pkg-config` search path.
>
> Perhaps you should add the directory containing `opencv.pc` to the `PKG_CONFIG_PATH` environment variable
>
> ```
> No package 'opencv' found
> ```
>
> Beca0use, you installed it manually from source. It should declared `.pc` file in one of the directories or through environment variable.
>
> ```
> man pkg-config
> pkg-config retrieves information about packages from  special  metadata
>        files.  These  files  are named after the package, and has a .pc exten‐
>        sion.   On  most  systems,  pkg-config  looks  in   /usr/lib/pkgconfig,
>        /usr/share/pkgconfig,     /usr/local/lib/pkgconfig     and     /usr/lo‐
>        cal/share/pkgconfig for these files.  It will additionally look in  the
>        colon-separated  (on  Windows, semicolon-separated) list of directories
>        specified by the PKG_CONFIG_PATH environment variable.
> ```
>
> Just make sure you have installed opencv not just copied its shared lib to python. I expect default installation put `.pc` file in `/usr/local/lib/pkgconfig/`
>
> 
>
> answered Nov 4 '20 at 13:57
>
> - i didn't found opencv.pc in any directory but i wrote a simple code to make sure that opencv is working and it run fine python3 import cv2 cv2.__version__ 4.5.0 – [M.Akyuzlu](https://askubuntu.com/users/1144726/m-akyuzlu) [Nov 5 '20 at 2:55](https://askubuntu.com/questions/1289550/opencv-was-not-found-in-the-pkg-config#comment2189527_1289577) 
> - what i did simply is install ubuntu 20.04 , cuda , cudnn ,cmake and pulled a opencv repo and its examps and make it . – [M.Akyuzlu](https://askubuntu.com/users/1144726/m-akyuzlu) [Nov 5 '20 at 2:59](https://askubuntu.com/questions/1289550/opencv-was-not-found-in-the-pkg-config#comment2189528_1289577) 