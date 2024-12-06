

## 비디오로 다크넷 성능을 테스트

## 명령어

다크넷에서 아래의 명령어를 써서 비디오 파일을 실행할 수 있습니다.

```bash
$ ./darknet detector demo cfg/coco.data cfg/yolov3.cfg yolov3.weights <video file>
```

## Problem

도커 컨테이너에서 OpenCV를 컴파일한 다음 아래처럼 에러가 발생합니다.

```bash
$ ./darknet detector demo cfg/coco.data cfg/yolov3.cfg yolov3.weights kt_data/seoul.mp4 
Demo needs OpenCV for webcam images.
$
```

`OpenCV`가 있는지 확인해보겠습니다.

```bash
# python -c 'import cv2; print(cv2.__version__)'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ImportError: No module named cv2
#
```

## Action

```bash
# apt install -y libopencv-dev
  ...
Configuring tzdata
------------------

Please select the geographic area in which you live. Subsequent configuration questions will narrow
this down by presenting a list of cities, representing the time zones in which they are located.

  1. Africa   3. Antarctica  5. Arctic  7. Atlantic  9. Indian    11. SystemV  13. Etc
  2. America  4. Australia   6. Asia    8. Europe    10. Pacific  12. US
Geographic area: 6

Please select the city or region corresponding to your time zone.

  1. Aden         19. Chongqing    37. Jerusalem     55. Novokuznetsk   73. Taipei
  2. Almaty       20. Colombo      38. Kabul         56. Novosibirsk    74. Tashkent
  3. Amman        21. Damascus     39. Kamchatka     57. Omsk           75. Tbilisi
  4. Anadyr       22. Dhaka        40. Karachi       58. Oral           76. Tehran
  5. Aqtau        23. Dili         41. Kashgar       59. Phnom_Penh     77. Tel_Aviv
  6. Aqtobe       24. Dubai        42. Kathmandu     60. Pontianak      78. Thimphu
  7. Ashgabat     25. Dushanbe     43. Khandyga      61. Pyongyang      79. Tokyo
  8. Atyrau       26. Famagusta    44. Kolkata       62. Qatar          80. Tomsk
  9. Baghdad      27. Gaza         45. Krasnoyarsk   63. Qostanay       81. Ujung_Pandang
  10. Bahrain     28. Harbin       46. Kuala_Lumpur  64. Qyzylorda      82. Ulaanbaatar
  11. Baku        29. Hebron       47. Kuching       65. Rangoon        83. Urumqi
  12. Bangkok     30. Ho_Chi_Minh  48. Kuwait        66. Riyadh         84. Ust-Nera
  13. Barnaul     31. Hong_Kong    49. Macau         67. Sakhalin       85. Vientiane
  14. Beirut      32. Hovd         50. Magadan       68. Samarkand      86. Vladivostok
  15. Bishkek     33. Irkutsk      51. Makassar      69. Seoul          87. Yakutsk
  16. Brunei      34. Istanbul     52. Manila        70. Shanghai       88. Yangon
  17. Chita       35. Jakarta      53. Muscat        71. Singapore      89. Yekaterinburg
  18. Choibalsan  36. Jayapura     54. Nicosia       72. Srednekolymsk  90. Yerevan
Time zone: 69
  ...
#
```

## 확인

```bash
# python -c 'import cv2; print(cv2.__version__)'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ImportError: No module named cv2
#
```

```bash
# python3 -c 'import cv2; print(cv2.__version__)'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ModuleNotFoundError: No module named 'cv2'
#
```

```bash
# pkg-config --modversion opencv
3.2.0
#
```

## Problem2

```bash
# ./darknet detector demo cfg/coco.data cfg/yolov3.cfg yolov3.weights ../etri_videos/seoul.mp4 
  ...
Loading weights from yolov3.weights...Done!
video file: ../etri_videos/seoul.mp4
Unable to init server: Could not connect: Connection refused

(Demo:2022): Gtk-WARNING **: 14:41:30.319: cannot open display: 
#
```

## Hint

X를 쓸 수 있도록 변경해보겠습니다.

```bash
root@228b2e12fee0:/home/user/darknet# apt-get install -y x11-apps            CREATED             STATUS              PORTS               
root@228b2e12fee0:/home/user/darknet# read escape sequence
$ 

```

```bash
$ docker ps
CONTAINER ID  IMAGE                                    COMMAND ...  NAMES
228b2e12fee0  aimldl/darknet:gpu_cudnn_opencv_version  "bash"  ...  affectionate_shirley
$ docker commit affectionate_shirley aimldl/darknet:gpu_cudnn_opencv_ver0.2
sha256:aa867e60ecefcc77ca5daa5d4c80bfa58b2305dc5d1f51f6bab9fa0b1146784b
$ 
```

```bash
$ docker run -it --gpus all -e DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix --user="$(id --user):$(id --group)" aimldl/darknet:gpu_cudnn_opencv_ver0.2 bash
groups: cannot find name for group ID 1000
I have no name!@ee3df7915268:/$ 
```

이 상황에서 `xclock`을 실행하면

```bash
# xclock
```

실행이 잘 됩니다. 비디오도 잘 실행이 됩니다.

```bash
$ cd /home/user/darknet/
$ ./darknet detector demo cfg/coco.data cfg/yolov3.cfg yolov3.weights ../etri_videos/seoul.mp4

```

## Problem3

문제는 프롬프트가 루트의 `#` 대신 `$`로 된다는 것입니다.

```bash
I have no name!@ee3df7915268:/home/user/darknet$
```

```bash
$ id --user
1000
$ id --group
1000
$
```





```bash
# ./darknet detector demo cfg/coco.data cfg/yolov3.cfg yolov3.weights ../etri_videos/seoul.mp4 > darknet-2021-02-15_mon.log
#
```

