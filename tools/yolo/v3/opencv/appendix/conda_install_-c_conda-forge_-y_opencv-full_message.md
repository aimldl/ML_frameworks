* Draft: 2021-01-27 (Wed)

# `conda-forge`를 통해 OpenCV 설치하기

## 관련 문서 검색

Google search: anaconda how to install opencv on ubuntu

[[Python] OpenCV 설치 with Anaconda](https://m.blog.naver.com/PostView.nhn?blogId=jooostory&logNo=221196559703&proxyReferer=https:%2F%2Fwww.google.com%2F), 2018-01-30

Google search: conda install opencv

* [conda-forge opencv - :: Anaconda Cloud](https://anaconda.org/conda-forge/opencv)

  ```bash
  $ conda install -c conda-forge opencv
  ```

```bash
## Assuming Anaconda is installed
$ conda install -c conda-forge -y opencv

```

## 설치하기

Anaconda 가상환경이 설치된 상황에서 가상환경에 들어간 상태를 가정합니다.

* 예를 들어, `$`는 `(keras-gpu) aimldl@aimldl-home-desktop:~$`와 동일합니다.

```bash
$ conda install -c conda-forge -y opencv
```

를 실행하면 처음 몇 분간은 좀 헤매네요. 계속 기다리면 `solving environment: done`이라고 나옵니다.

```bash
Collecting package metadata (current_repodata.json): done
Solving environment: failed with initial frozen solve. Retrying with flexible solve.
Solving environment: failed with repodata from current_repodata.json, will retry with next repodata source.
Collecting package metadata (repodata.json): done
Solving environment: done
```

이후로는 설치가 시작되는데 아래처럼 상당히 많은 패키지가 같이 설치됩니다.

```bash
## Package Plan ##

  environment location: /home/aimldl/anaconda3/envs/keras-gpu

  added / updated specs:
    - opencv


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    _libgcc_mutex-0.1          |      conda_forge           3 KB  conda-forge
    _openmp_mutex-4.5          |            1_gnu          22 KB  conda-forge
    ca-certificates-2020.12.5  |       ha878542_0         137 KB  conda-forge
    cairo-1.16.0               |    h7979940_1007         1.5 MB  conda-forge
    certifi-2020.12.5          |   py38h578d9bd_1         143 KB  conda-forge
    curl-7.71.1                |       he644dc0_8         139 KB  conda-forge
    ffmpeg-4.2                 |       h167e202_0        80.2 MB  conda-forge
    fontconfig-2.13.1          |    hba837de_1004         344 KB  conda-forge
    gettext-0.19.8.1           |    h0b5b191_1005         3.6 MB  conda-forge
    glib-2.66.4                |       hc4f0c31_2         442 KB  conda-forge
    glib-tools-2.66.4          |       hc4f0c31_2          85 KB  conda-forge
    gnutls-3.6.13              |       h85f3911_1         2.0 MB  conda-forge
    gst-plugins-base-1.14.5    |       h0935bb2_2         6.8 MB  conda-forge
    gstreamer-1.18.3           |       h3560a44_0         2.0 MB  conda-forge
    h5py-2.10.0                |nompi_py38h7442b35_105         1.1 MB  conda-forge
    harfbuzz-2.7.4             |       h5cf4720_0         1.9 MB  conda-forge
    hdf5-1.10.6                |nompi_h3c11f04_101         3.0 MB  conda-forge
    icu-68.1                   |       h58526e2_0        13.0 MB  conda-forge
    jasper-1.900.1             |    h07fcdf6_1006         286 KB  conda-forge
    jpeg-9d                    |       h36c2ea0_0         264 KB  conda-forge
    krb5-1.17.2                |       h926e7f8_0         1.4 MB  conda-forge
    lame-3.100                 |    h7f98852_1001         496 KB  conda-forge
    libblas-3.8.0              |           14_mkl          10 KB  conda-forge
    libcblas-3.8.0             |           14_mkl          10 KB  conda-forge
    libclang-11.0.1            |default_ha53f305_1        19.2 MB  conda-forge
    libcurl-7.71.1             |       hcdd3856_8         312 KB  conda-forge
    libev-4.33                 |       h516909a_1         104 KB  conda-forge
    libevent-2.1.10            |       hcdb4288_3         1.1 MB  conda-forge
    libgcc-ng-9.3.0            |      h2828fa1_18         7.8 MB  conda-forge
    libglib-2.66.4             |       h748fe8e_2         3.0 MB  conda-forge
    libgomp-9.3.0              |      h2828fa1_18         376 KB  conda-forge
    libiconv-1.16              |       h516909a_0         1.4 MB  conda-forge
    liblapack-3.8.0            |           14_mkl          10 KB  conda-forge
    liblapacke-3.8.0           |           14_mkl          10 KB  conda-forge
    libllvm11-11.0.1           |       hf817b99_0        29.1 MB  conda-forge
    libnghttp2-1.41.0          |       h8cfc5f6_2         774 KB  conda-forge
    libopencv-4.2.0            |           py38_6        55.4 MB  conda-forge
    libpq-12.3                 |       h255efa7_3         2.6 MB  conda-forge
    libstdcxx-ng-9.3.0         |      h6de172a_18         4.0 MB  conda-forge
    libuuid-2.32.1             |    h7f98852_1000          28 KB  conda-forge
    libwebp-1.0.2              |       h576950b_1         920 KB  conda-forge
    libxkbcommon-1.0.3         |       he3ba5ed_0         581 KB  conda-forge
    libxml2-2.9.10             |       h72842e0_3         1.3 MB  conda-forge
    libxslt-1.1.33             |       h15afd5d_2         522 KB  conda-forge
    lxml-4.6.2                 |   py38hf1fe3a4_1         1.5 MB  conda-forge
    mysql-common-8.0.22        |       ha770c72_1         1.5 MB  conda-forge
    mysql-libs-8.0.22          |       h1fd7589_1         1.7 MB  conda-forge
    nettle-3.6                 |       he412f7d_0         6.5 MB  conda-forge
    nspr-4.29                  |       h9c3ff4c_1         232 KB  conda-forge
    nss-3.61                   |       hb5efdd6_0         2.1 MB  conda-forge
    opencv-4.2.0               |           py38_6          19 KB  conda-forge
    openh264-1.8.0             |    hdbcaa40_1000         1.4 MB  conda-forge
    openssl-1.1.1i             |       h7f98852_0         2.1 MB  conda-forge
    py-opencv-4.2.0            |   py38h23f93f0_6          21 KB  conda-forge
    pyqt-5.12.3                |   py38h578d9bd_7          21 KB  conda-forge
    pyqt-impl-5.12.3           |   py38h7400c14_7         5.9 MB  conda-forge
    pyqt5-sip-4.19.18          |   py38h709712a_7         310 KB  conda-forge
    pyqtchart-5.12             |   py38h7400c14_7         257 KB  conda-forge
    pyqtwebengine-5.12.1       |   py38h7400c14_7         175 KB  conda-forge
    pytables-3.6.1             |   py38hf9f05d5_3         1.5 MB  conda-forge
    python_abi-3.8             |           1_cp38           4 KB  conda-forge
    qt-5.12.9                  |       h9d6b050_2        99.5 MB  conda-forge
    sqlite-3.34.0              |       h74cdb3f_0         1.4 MB  conda-forge
    x264-1!152.20180806        |       h14c3975_0         1.4 MB  conda-forge
    xorg-kbproto-1.0.7         |    h7f98852_1002          27 KB  conda-forge
    xorg-libice-1.0.10         |       h516909a_0          57 KB  conda-forge
    xorg-libsm-1.2.3           |    h84519dc_1000          25 KB  conda-forge
    xorg-libx11-1.6.12         |       h516909a_0         917 KB  conda-forge
    xorg-libxext-1.3.4         |       h516909a_0          51 KB  conda-forge
    xorg-libxrender-0.9.10     |    h516909a_1002          31 KB  conda-forge
    xorg-renderproto-0.11.1    |    h14c3975_1002           8 KB  conda-forge
    xorg-xextproto-7.3.0       |    h7f98852_1002          28 KB  conda-forge
    xorg-xproto-7.0.31         |    h7f98852_1007          73 KB  conda-forge
    ------------------------------------------------------------
                                           Total:       376.1 MB

The following NEW packages will be INSTALLED:

  _openmp_mutex      conda-forge/linux-64::_openmp_mutex-4.5-1_gnu
  ffmpeg             conda-forge/linux-64::ffmpeg-4.2-h167e202_0
  gettext            conda-forge/linux-64::gettext-0.19.8.1-h0b5b191_1005
  glib-tools         conda-forge/linux-64::glib-tools-2.66.4-hc4f0c31_2
  gnutls             conda-forge/linux-64::gnutls-3.6.13-h85f3911_1
  jasper             conda-forge/linux-64::jasper-1.900.1-h07fcdf6_1006
  lame               conda-forge/linux-64::lame-3.100-h7f98852_1001
  libblas            conda-forge/linux-64::libblas-3.8.0-14_mkl
  libcblas           conda-forge/linux-64::libcblas-3.8.0-14_mkl
  libclang           conda-forge/linux-64::libclang-11.0.1-default_ha53f305_1
  libev              conda-forge/linux-64::libev-4.33-h516909a_1
  libevent           conda-forge/linux-64::libevent-2.1.10-hcdb4288_3
  libglib            conda-forge/linux-64::libglib-2.66.4-h748fe8e_2
  libgomp            conda-forge/linux-64::libgomp-9.3.0-h2828fa1_18
  libiconv           conda-forge/linux-64::libiconv-1.16-h516909a_0
  liblapack          conda-forge/linux-64::liblapack-3.8.0-14_mkl
  liblapacke         conda-forge/linux-64::liblapacke-3.8.0-14_mkl
  libllvm11          conda-forge/linux-64::libllvm11-11.0.1-hf817b99_0
  libnghttp2         conda-forge/linux-64::libnghttp2-1.41.0-h8cfc5f6_2
  libopencv          conda-forge/linux-64::libopencv-4.2.0-py38_6
  libpq              conda-forge/linux-64::libpq-12.3-h255efa7_3
  libxkbcommon       conda-forge/linux-64::libxkbcommon-1.0.3-he3ba5ed_0
  mysql-common       conda-forge/linux-64::mysql-common-8.0.22-ha770c72_1
  mysql-libs         conda-forge/linux-64::mysql-libs-8.0.22-h1fd7589_1
  nettle             conda-forge/linux-64::nettle-3.6-he412f7d_0
  nspr               conda-forge/linux-64::nspr-4.29-h9c3ff4c_1
  nss                conda-forge/linux-64::nss-3.61-hb5efdd6_0
  opencv             conda-forge/linux-64::opencv-4.2.0-py38_6
  openh264           conda-forge/linux-64::openh264-1.8.0-hdbcaa40_1000
  py-opencv          conda-forge/linux-64::py-opencv-4.2.0-py38h23f93f0_6
  pyqt-impl          conda-forge/linux-64::pyqt-impl-5.12.3-py38h7400c14_7
  pyqt5-sip          conda-forge/linux-64::pyqt5-sip-4.19.18-py38h709712a_7
  pyqtchart          conda-forge/linux-64::pyqtchart-5.12-py38h7400c14_7
  pyqtwebengine      conda-forge/linux-64::pyqtwebengine-5.12.1-py38h7400c14_7
  python_abi         conda-forge/linux-64::python_abi-3.8-1_cp38
  x264               conda-forge/linux-64::x264-1!152.20180806-h14c3975_0
  xorg-kbproto       conda-forge/linux-64::xorg-kbproto-1.0.7-h7f98852_1002
  xorg-libice        conda-forge/linux-64::xorg-libice-1.0.10-h516909a_0
  xorg-libsm         conda-forge/linux-64::xorg-libsm-1.2.3-h84519dc_1000
  xorg-libx11        conda-forge/linux-64::xorg-libx11-1.6.12-h516909a_0
  xorg-libxext       conda-forge/linux-64::xorg-libxext-1.3.4-h516909a_0
  xorg-libxrender    conda-forge/linux-64::xorg-libxrender-0.9.10-h516909a_1002
  xorg-renderproto   conda-forge/linux-64::xorg-renderproto-0.11.1-h14c3975_1002
  xorg-xextproto     conda-forge/linux-64::xorg-xextproto-7.3.0-h7f98852_1002
  xorg-xproto        conda-forge/linux-64::xorg-xproto-7.0.31-h7f98852_1007

The following packages will be UPDATED:

  cairo                 pkgs/main::cairo-1.14.12-h8948797_3 --> conda-forge::cairo-1.16.0-h7979940_1007
  certifi            pkgs/main::certifi-2020.12.5-py38h06a~ --> conda-forge::certifi-2020.12.5-py38h578d9bd_1
  curl                    pkgs/main::curl-7.71.1-hbc83047_1 --> conda-forge::curl-7.71.1-he644dc0_8
  fontconfig         pkgs/main::fontconfig-2.13.0-h9420a91~ --> conda-forge::fontconfig-2.13.1-hba837de_1004
  glib                    pkgs/main::glib-2.66.1-h92f7085_0 --> conda-forge::glib-2.66.4-hc4f0c31_2
  gst-plugins-base   pkgs/main::gst-plugins-base-1.14.0-h8~ --> conda-forge::gst-plugins-base-1.14.5-h0935bb2_2
  gstreamer          pkgs/main::gstreamer-1.14.0-h28cd5cc_2 --> conda-forge::gstreamer-1.18.3-h3560a44_0
  h5py                pkgs/main::h5py-2.10.0-py38h7918eee_0 --> conda-forge::h5py-2.10.0-nompi_py38h7442b35_105
  harfbuzz             pkgs/main::harfbuzz-2.4.0-hca77d97_1 --> conda-forge::harfbuzz-2.7.4-h5cf4720_0
  hdf5                    pkgs/main::hdf5-1.10.4-hb1b8bf9_0 --> conda-forge::hdf5-1.10.6-nompi_h3c11f04_101
  icu                        pkgs/main::icu-58.2-he6710b0_3 --> conda-forge::icu-68.1-h58526e2_0
  jpeg                        pkgs/main::jpeg-9b-h024ee3a_2 --> conda-forge::jpeg-9d-h36c2ea0_0
  libcurl              pkgs/main::libcurl-7.71.1-h20c2e04_1 --> conda-forge::libcurl-7.71.1-hcdd3856_8
  libgcc-ng            anaconda::libgcc-ng-9.1.0-hdf63c60_0 --> conda-forge::libgcc-ng-9.3.0-h2828fa1_18
  libstdcxx-ng       anaconda::libstdcxx-ng-9.1.0-hdf63c60~ --> conda-forge::libstdcxx-ng-9.3.0-h6de172a_18
  libuuid               pkgs/main::libuuid-1.0.3-h1bed415_2 --> conda-forge::libuuid-2.32.1-h7f98852_1000
  libwebp               pkgs/main::libwebp-1.0.1-h8e7db2f_0 --> conda-forge::libwebp-1.0.2-h576950b_1
  lxml                 pkgs/main::lxml-4.6.2-py38h9120a33_0 --> conda-forge::lxml-4.6.2-py38hf1fe3a4_1
  pyqt                 pkgs/main::pyqt-5.9.2-py38h05f1152_4 --> conda-forge::pyqt-5.12.3-py38h578d9bd_7
  pytables           pkgs/main::pytables-3.6.1-py38h9fd0a3~ --> conda-forge::pytables-3.6.1-py38hf9f05d5_3
  qt                         pkgs/main::qt-5.9.7-h5867ecd_1 --> conda-forge::qt-5.12.9-h9d6b050_2
  sqlite                 anaconda::sqlite-3.33.0-h62c20be_0 --> conda-forge::sqlite-3.34.0-h74cdb3f_0

The following packages will be SUPERSEDED by a higher-priority channel:

  _libgcc_mutex           pkgs/main::_libgcc_mutex-0.1-main --> conda-forge::_libgcc_mutex-0.1-conda_forge
  ca-certificates    pkgs/main::ca-certificates-2021.1.19-~ --> conda-forge::ca-certificates-2020.12.5-ha878542_0
  krb5                    pkgs/main::krb5-1.18.2-h173b8e3_0 --> conda-forge::krb5-1.17.2-h926e7f8_0
  libxml2              pkgs/main::libxml2-2.9.10-hb55368b_3 --> conda-forge::libxml2-2.9.10-h72842e0_3
  libxslt              pkgs/main::libxslt-1.1.34-hc22bd24_0 --> conda-forge::libxslt-1.1.33-h15afd5d_2
  openssl              pkgs/main::openssl-1.1.1i-h27cfd23_0 --> conda-forge::openssl-1.1.1i-h7f98852_0
```

다운로드 및 설치가 본격적으로 시작합니다.

```bash
Downloading and Extracting Packages
certifi-2020.12.5    | 143 KB    | ################################################################################### | 100%
ffmpeg-4.2           | 80.2 MB   | ################################################################################### | 100%
pyqt-5.12.3          | 21 KB     | ################################################################################### | 100%
libev-4.33           | 104 KB    | ################################################################################### | 100%
gstreamer-1.18.3     | 2.0 MB    | ################################################################################### | 100%
xorg-xextproto-7.3.0 | 28 KB     | ################################################################################### | 100%
libglib-2.66.4       | 3.0 MB    | ################################################################################### | 100%
py-opencv-4.2.0      | 21 KB     | ################################################################################### | 100%
libiconv-1.16        | 1.4 MB    | ################################################################################### | 100%
xorg-libice-1.0.10   | 57 KB     | ################################################################################### | 100%
hdf5-1.10.6          | 3.0 MB    | ################################################################################### | 100%
libxml2-2.9.10       | 1.3 MB    | ################################################################################### | 100%
nss-3.61             | 2.1 MB    | ################################################################################### | 100%
cairo-1.16.0         | 1.5 MB    | ################################################################################### | 100%
gst-plugins-base-1.1 | 6.8 MB    | ################################################################################### | 100%
pyqt5-sip-4.19.18    | 310 KB    | ################################################################################### | 100%
jasper-1.900.1       | 286 KB    | ################################################################################### | 100%
libpq-12.3           | 2.6 MB    | ################################################################################### | 100%
harfbuzz-2.7.4       | 1.9 MB    | ################################################################################### | 100%
libevent-2.1.10      | 1.1 MB    | ################################################################################### | 100%
libuuid-2.32.1       | 28 KB     | ################################################################################### | 100%
mysql-common-8.0.22  | 1.5 MB    | ################################################################################### | 100%
openssl-1.1.1i       | 2.1 MB    | ################################################################################### | 100%
gettext-0.19.8.1     | 3.6 MB    | ################################################################################### | 100%
xorg-libxrender-0.9. | 31 KB     | ################################################################################### | 100%
libwebp-1.0.2        | 920 KB    | ################################################################################### | 100%
libxslt-1.1.33       | 522 KB    | ################################################################################### | 100%
xorg-libx11-1.6.12   | 917 KB    | ################################################################################### | 100%
krb5-1.17.2          | 1.4 MB    | ################################################################################### | 100%
ca-certificates-2020 | 137 KB    | ################################################################################### | 100%
libclang-11.0.1      | 19.2 MB   | ################################################################################### | 100%
libnghttp2-1.41.0    | 774 KB    | ################################################################################### | 100%
pytables-3.6.1       | 1.5 MB    | ################################################################################### | 100%
lxml-4.6.2           | 1.5 MB    | ################################################################################### | 100%
libcblas-3.8.0       | 10 KB     | ################################################################################### | 100%
icu-68.1             | 13.0 MB   | ################################################################################### | 100%
fontconfig-2.13.1    | 344 KB    | ################################################################################### | 100%
pyqtwebengine-5.12.1 | 175 KB    | ################################################################################### | 100%
libxkbcommon-1.0.3   | 581 KB    | ################################################################################### | 100%
libgomp-9.3.0        | 376 KB    | ################################################################################### | 100%
liblapack-3.8.0      | 10 KB     | ################################################################################### | 100%
lame-3.100           | 496 KB    | ################################################################################### | 100%
nspr-4.29            | 232 KB    | ################################################################################### | 100%
mysql-libs-8.0.22    | 1.7 MB    | ################################################################################### | 100%
gnutls-3.6.13        | 2.0 MB    | ################################################################################### | 100%
glib-tools-2.66.4    | 85 KB     | ################################################################################### | 100%
jpeg-9d              | 264 KB    | ################################################################################### | 100%
xorg-xproto-7.0.31   | 73 KB     | ################################################################################### | 100%
xorg-renderproto-0.1 | 8 KB      | ################################################################################### | 100%
openh264-1.8.0       | 1.4 MB    | ################################################################################### | 100%
glib-2.66.4          | 442 KB    | ################################################################################### | 100%
qt-5.12.9            | 99.5 MB   | ################################################################################### | 100%
libopencv-4.2.0      | 55.4 MB   | ################################################################################### | 100%
_openmp_mutex-4.5    | 22 KB     | ################################################################################### | 100%
_libgcc_mutex-0.1    | 3 KB      | ################################################################################### | 100%
python_abi-3.8       | 4 KB      | ################################################################################### | 100%
pyqt-impl-5.12.3     | 5.9 MB    | ################################################################################### | 100%
libllvm11-11.0.1     | 29.1 MB   | ################################################################################### | 100%
h5py-2.10.0          | 1.1 MB    | ################################################################################### | 100%
xorg-kbproto-1.0.7   | 27 KB     | ################################################################################### | 100%
libgcc-ng-9.3.0      | 7.8 MB    | ################################################################################### | 100%
x264-1!152.20180806  | 1.4 MB    | ################################################################################### | 100%
nettle-3.6           | 6.5 MB    | ################################################################################### | 100%
xorg-libsm-1.2.3     | 25 KB     | ################################################################################### | 100%
liblapacke-3.8.0     | 10 KB     | ################################################################################### | 100%
xorg-libxext-1.3.4   | 51 KB     | ################################################################################### | 100%
pyqtchart-5.12       | 257 KB    | ################################################################################### | 100%
opencv-4.2.0         | 19 KB     | ################################################################################### | 100%
curl-7.71.1          | 139 KB    | ################################################################################### | 100%
libcurl-7.71.1       | 312 KB    | ################################################################################### | 100%
sqlite-3.34.0        | 1.4 MB    | ################################################################################### | 100%
libstdcxx-ng-9.3.0   | 4.0 MB    | ################################################################################### | 100%
libblas-3.8.0        | 10 KB     | ################################################################################### | 100%
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
$
```

## 설치 확인

### 파이썬 환경

파이썬에서 설치가 잘 되었는지 확인해봅니다.

```bash
$ python -c 'import cv2; print(cv2.__version__)'
4.2.0
$
```

파이썬에서 cv2 모듈을 import할 수 있어서 설치가 잘 되었음을 알 수 있습니다.

### `pkg-config` 명령어

`pkg-config` 명령어를 이용했을 땐 `opencv`를 찾을 수 없었습니다.

```bash
$ pkg-config --modversion opencv
Package opencv was not found in the pkg-config search path.
Perhaps you should add the directory containing `opencv.pc'
to the PKG_CONFIG_PATH environment variable
No package 'opencv' found
$
```

