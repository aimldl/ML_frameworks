* Draft: 2021-01-31 (Sun)

# fatal error: cuda_runtime.h: No such file or directory

## Problem

After changing `Makefile` in the `darknet` directory

```bash
$ nano Makefile
```

from the default settings in the top 5 rows

```makefile
GPU=0
CUDNN=0
OPENCV=0
OPENMP=0
DEBUG=0
```

to

```makefile
GPU=1
CUDNN=0
OPENCV=0
OPENMP=0
DEBUG=0
```

the following errors are observed.

* `include/darknet.h:11:14: fatal error: cuda_runtime.h: No such file or directory`

```bash
$ make
gcc -Iinclude/ -Isrc/ -DGPU -I/usr/local/cuda/include/ -Wall -Wno-unused-result -Wno-unknown-pragmas -Wfatal-errors -fPIC -Ofast -DGPU -c ./src/gemm.c -o obj/gemm.o
In file included from ./src/utils.h:5,
                 from ./src/gemm.c:2:
include/darknet.h:11:14: fatal error: cuda_runtime.h: No such file or directory
   11 |     #include "cuda_runtime.h"
      |              ^~~~~~~~~~~~~~~~
compilation terminated.
make: *** [Makefile:89: obj/gemm.o] Error 1

$
```

Obviously, `darknet` won't compile correctly to use GPU.

## Hint





## Action

```bash
$ docker attach stupefied_cori
root@c0bffd73888a:/# apt install nvidia-driver-455
  ...
debconf: unable to initialize frontend: Dialog
debconf: (No usable dialog-like program is installed, so the dialog based frontend cannot be used. at /usr/share/perl5/Debconf/FrontEnd/Dialog.pm line 76.)
debconf: falling back to frontend: Readline
  ...
Configuring keyboard-configuration
----------------------------------

The layout of keyboards varies per country, with some countries having multiple common layouts. Please select the country of origin for the keyboard of this computer.

  1. Afghani                   21. Danish                                     41. French (Togo)                       61. Lao                            81. Slovak
  2. Albanian                  22. Dhivehi                                    42. Georgian                            62. Latvian                        82. Slovenian
  3. Amharic                   23. Dutch                                      43. German                              63. Lithuanian                     83. Spanish
  4. Arabic                    24. Dzongkha                                   44. German (Austria)                    64. Macedonian                     84. Spanish (Latin American)
  5. Arabic (Morocco)          25. English (Australian)                       45. Greek                               65. Malay (Jawi, Arabic Keyboard)  85. Swahili (Kenya)
  6. Arabic (Syria)            26. English (Cameroon)                         46. Hebrew                              66. Maltese                        86. Swahili (Tanzania)
  7. Armenian                  27. English (Ghana)                            47. Hungarian                           67. Maori                          87. Swedish
  8. Azerbaijani               28. English (Nigeria)                          48. Icelandic                           68. Moldavian                      88. Switzerland
  9. Bambara                   29. English (South Africa)                     49. Indian                              69. Mongolian                      89. Taiwanese
  10. Bangla                   30. English (UK)                               50. Indonesian (Arab Melayu, phonetic)  70. Montenegrin                    90. Tajik
  11. Belarusian               31. English (US)                               51. Indonesian (Javanese)               71. Nepali                         91. Thai
  12. Belgian                  32. Esperanto                                  52. Iraqi                               72. Norwegian                      92. Tswana
  13. Berber (Algeria, Latin)  33. Estonian                                   53. Irish                               73. Persian                        93. Turkish
  14. Bosnian                  34. Faroese                                    54. Italian                             74. Polish                         94. Turkmen
  15. Braille                  35. Filipino                                   55. Japanese                            75. Portuguese                     95. Ukrainian
  16. Bulgarian                36. Finnish                                    56. Japanese (PC-98)                    76. Portuguese (Brazil)            96. Urdu (Pakistan)
  17. Burmese                  37. French                                     57. Kazakh                              77. Romanian                       97. Uzbek
  18. Chinese                  38. French (Canada)                            58. Khmer (Cambodia)                    78. Russian                        98. Vietnamese
  19. Croatian                 39. French (Democratic Republic of the Congo)  59. Korean                              79. Serbian                        99. Wolof
  20. Czech                    40. French (Guinea)                            60. Kyrgyz                              80. Sinhala (phonetic)
Country of origin for the keyboard: 59

Please select the layout matching the keyboard for this machine.

  1. Korean  2. Korean - Korean (101/104 key compatible)
Keyboard layout: 1
  ...
A new initrd image has also been created. To revert, please regenerate your
initrd by running the following command after deleting the modprobe.d file:
`/usr/sbin/initramfs -u`
*****************************************************************************
*** Reboot your computer and verify that the NVIDIA graphics driver can   ***
*** be loaded.                                                            ***
*****************************************************************************
  ...
root@c0bffd73888a:/#
```

An error message occurs after installing the driver.

```bash
root@c0bffd73888a:/# nvidia-smi
Failed to initialize NVML: Unknown Error
root@c0bffd73888a:/#
```

I was hoping to reboot the system, but this is a container. If rebooted, what is stored in the container will be reset. So I have used a trick to create a new image and run the container.

```bash
root@c0bffd73888a:/# exit
$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
$ docker images
REPOSITORY          TAG                    IMAGE ID            CREATED             SIZE
nvidia/cuda         11.0-base-driver-455   0f98611c048c        4 minutes ago       3.26GB
  ...
$ docker run -it nvidia/cuda:11.0-base-driver-455 bash
root@95f9ff464d33:/# ls
bin  boot  dev  etc  home  lib  lib32  lib64  libx32  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@95f9ff464d33:/# nvidia-smi
Failed to initialize NVML: Unknown Error
root@95f9ff464d33:/#
```

Unfortunately, the error still remains.





