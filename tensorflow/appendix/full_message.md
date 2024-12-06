

`aimldl@aimldl-home-desktop:~`에서 실행한 결과입니다.

```bash
$ pip install --upgrade pip
Collecting pip
  Downloading https://files.pythonhosted.org/packages/54/eb/4a3642e971f404d69d4f6fa3885559d67562801b99d7592487f1ecc4e017/pip-20.3.3-py2.py3-none-any.whl (1.5MB)
    100% |████████████████████████████████| 1.5MB 930kB/s
Installing collected packages: pip
Successfully installed pip-20.3.3
$
```

```bash
$ pip install tensorflow
WARNING: pip is being invoked by an old script wrapper. This will fail in a future version of pip.
Please see https://github.com/pypa/pip/issues/5599 for advice on fixing the underlying issue.
To avoid this problem you can invoke Python with '-m pip' instead of running pip directly.
DEPRECATION: Python 2.7 reached the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 is no longer maintained. pip 21.0 will drop support for Python 2.7 in January 2021. More details about Python 2 support in pip can be found at https://pip.pypa.io/en/latest/development/release-process/#python-2-support pip 21.0 will remove support for this functionality.
Defaulting to user installation because normal site-packages is not writeable
Collecting tensorflow
  Downloading tensorflow-2.1.0-cp27-cp27mu-manylinux2010_x86_64.whl (421.8 MB)
     |████████████████████████████████| 421.8 MB 35 kB/s
Collecting numpy<2.0,>=1.16.0
  Downloading numpy-1.16.6-cp27-cp27mu-manylinux1_x86_64.whl (17.0 MB)
     |████████████████████████████████| 17.0 MB 71.6 MB/s
Collecting opt-einsum>=2.3.2
  Downloading opt_einsum-2.3.2.tar.gz (59 kB)
     |████████████████████████████████| 59 kB 6.1 MB/s
Collecting gast==0.2.2
  Downloading gast-0.2.2.tar.gz (10 kB)
Requirement already satisfied: enum34>=1.1.6; python_version < "3.4" in /usr/lib/python2.7/dist-packages (from tensorflow) (1.1.6)
Collecting keras-applications>=1.0.8
  Downloading Keras_Applications-1.0.8.tar.gz (289 kB)
     |████████████████████████████████| 289 kB 27.4 MB/s
Collecting keras-preprocessing>=1.1.0
  Downloading Keras_Preprocessing-1.1.2-py2.py3-none-any.whl (42 kB)
     |████████████████████████████████| 42 kB 1.3 MB/s
Collecting astor>=0.6.0
  Downloading astor-0.8.1-py2.py3-none-any.whl (27 kB)
Collecting termcolor>=1.1.0
  Downloading termcolor-1.1.0.tar.gz (3.9 kB)
Collecting mock>=2.0.0; python_version < "3"
  Downloading mock-3.0.5-py2.py3-none-any.whl (25 kB)
Collecting backports.weakref>=1.0rc1; python_version < "3.4"
  Downloading backports.weakref-1.0.post1-py2.py3-none-any.whl (5.2 kB)
Collecting protobuf>=3.8.0
  Downloading protobuf-3.14.0-cp27-cp27mu-manylinux1_x86_64.whl (1.0 MB)
     |████████████████████████████████| 1.0 MB 86.8 MB/s
Collecting absl-py>=0.7.0
  Downloading absl-py-0.11.0.tar.gz (110 kB)
     |████████████████████████████████| 110 kB 56.2 MB/s
Collecting scipy==1.2.2; python_version < "3"
  Downloading scipy-1.2.2-cp27-cp27mu-manylinux1_x86_64.whl (24.8 MB)
     |████████████████████████████████| 24.8 MB 51.8 MB/s
Collecting functools32>=3.2.3; python_version < "3"
  Downloading functools32-3.2.3-2.tar.gz (31 kB)
Collecting six>=1.12.0
  Downloading six-1.15.0-py2.py3-none-any.whl (10 kB)
Collecting tensorboard<2.2.0,>=2.1.0
  Downloading tensorboard-2.1.0-py2-none-any.whl (3.8 MB)
     |████████████████████████████████| 3.8 MB 82.3 MB/s
Requirement already satisfied: wheel; python_version < "3" in /usr/lib/python2.7/dist-packages (from tensorflow) (0.30.0)
Collecting wrapt>=1.11.1
  Downloading wrapt-1.12.1.tar.gz (27 kB)
Collecting tensorflow-estimator<2.2.0,>=2.1.0rc0
  Downloading tensorflow_estimator-2.1.0-py2.py3-none-any.whl (448 kB)
     |████████████████████████████████| 448 kB 21.5 MB/s
Collecting google-pasta>=0.1.6
  Downloading google_pasta-0.2.0-py2-none-any.whl (57 kB)
     |████████████████████████████████| 57 kB 6.5 MB/s
Collecting grpcio>=1.8.6
  Downloading grpcio-1.35.0-cp27-cp27mu-manylinux2010_x86_64.whl (3.9 MB)
     |████████████████████████████████| 3.9 MB 106.4 MB/s
Collecting h5py
  Downloading h5py-2.10.0-cp27-cp27mu-manylinux1_x86_64.whl (2.8 MB)
     |████████████████████████████████| 2.8 MB 80.5 MB/s
Collecting funcsigs>=1; python_version < "3.3"
  Downloading funcsigs-1.0.2-py2.py3-none-any.whl (17 kB)
Collecting google-auth<2,>=1.6.3
  Downloading google_auth-1.24.0-py2.py3-none-any.whl (114 kB)
     |████████████████████████████████| 114 kB 79.4 MB/s
Collecting requests<3,>=2.21.0
  Downloading requests-2.25.1-py2.py3-none-any.whl (61 kB)
     |████████████████████████████████| 61 kB 8.5 MB/s
Collecting google-auth-oauthlib<0.5,>=0.4.1
  Downloading google_auth_oauthlib-0.4.1-py2.py3-none-any.whl (18 kB)
Collecting werkzeug>=0.11.15
  Downloading Werkzeug-1.0.1-py2.py3-none-any.whl (298 kB)
     |████████████████████████████████| 298 kB 71.7 MB/s
Collecting futures>=3.1.1; python_version < "3"
  Downloading futures-3.3.0-py2-none-any.whl (16 kB)
Collecting markdown>=2.6.8
  Downloading Markdown-3.1.1-py2.py3-none-any.whl (87 kB)
     |████████████████████████████████| 87 kB 8.4 MB/s
Collecting setuptools>=41.0.0
  Downloading setuptools-44.1.1-py2.py3-none-any.whl (583 kB)
     |████████████████████████████████| 583 kB 79.8 MB/s
Collecting pyasn1-modules>=0.2.1
  Downloading pyasn1_modules-0.2.8-py2.py3-none-any.whl (155 kB)
     |████████████████████████████████| 155 kB 77.9 MB/s
Collecting rsa<4.6; python_version < "3.6"
  Downloading rsa-4.5-py2.py3-none-any.whl (36 kB)
Collecting cachetools<5.0,>=2.0.0
  Downloading cachetools-3.1.1-py2.py3-none-any.whl (11 kB)
Collecting chardet<5,>=3.0.2
  Downloading chardet-4.0.0-py2.py3-none-any.whl (178 kB)
     |████████████████████████████████| 178 kB 61.9 MB/s
Collecting urllib3<1.27,>=1.21.1
  Downloading urllib3-1.26.2-py2.py3-none-any.whl (136 kB)
     |████████████████████████████████| 136 kB 78.5 MB/s
Requirement already satisfied: idna<3,>=2.5 in /usr/lib/python2.7/dist-packages (from requests<3,>=2.21.0->tensorboard<2.2.0,>=2.1.0->tensorflow) (2.6)
Collecting certifi>=2017.4.17
  Downloading certifi-2020.12.5-py2.py3-none-any.whl (147 kB)
     |████████████████████████████████| 147 kB 87.7 MB/s
Collecting requests-oauthlib>=0.7.0
  Downloading requests_oauthlib-1.3.0-py2.py3-none-any.whl (23 kB)
Collecting pyasn1<0.5.0,>=0.4.6
  Downloading pyasn1-0.4.8-py2.py3-none-any.whl (77 kB)
     |████████████████████████████████| 77 kB 7.3 MB/s
Collecting oauthlib>=3.0.0
  Downloading oauthlib-3.1.0-py2.py3-none-any.whl (147 kB)
     |████████████████████████████████| 147 kB 31.6 MB/s
Building wheels for collected packages: opt-einsum, gast, keras-applications, termcolor, absl-py, functools32, wrapt
  Building wheel for opt-einsum (setup.py) ... done
  Created wheel for opt-einsum: filename=opt_einsum-2.3.2-py2-none-any.whl size=52336 sha256=914bae99529d699fd043281eaf53852a03b53f0ee59bac22efa3c6d34cc6016a
  Stored in directory: /home/aimldl/.cache/pip/wheels/ef/c4/c2/d0b07dd2a54f4d583a5de0e6ce5eb7a1832961b9a10d1ec953
  Building wheel for gast (setup.py) ... done
  Created wheel for gast: filename=gast-0.2.2-py2-none-any.whl size=7632 sha256=078480995009a7a2a42f1a92f958a400cd32f6b9a3e4af2c0d075a1e7e7d25d0
  Stored in directory: /home/aimldl/.cache/pip/wheels/0f/10/f7/29260ef8a721b90061c8c70a4f0130a64036e8dafe15acc097
  Building wheel for keras-applications (setup.py) ... done
  Created wheel for keras-applications: filename=Keras_Applications-1.0.8-py2-none-any.whl size=50943 sha256=68ff603a0a9d401f256e8f686425dea8eb2a3e6e0a24de845fe9148acd7c34c9
  Stored in directory: /home/aimldl/.cache/pip/wheels/71/a0/64/e2e0c93740e0460f4b7f036141b7c73b5e44ff38f690ddff9f
  Building wheel for termcolor (setup.py) ... done
  Created wheel for termcolor: filename=termcolor-1.1.0-py2-none-any.whl size=5678 sha256=79c29b783d121f3997e68b561cad2a703b8f92131d438cf29f59c94239cc3cd3
  Stored in directory: /home/aimldl/.cache/pip/wheels/48/54/87/2f4d1a48c87e43906477a3c93d9663c49ca092046d5a4b00b4
  Building wheel for absl-py (setup.py) ... done
  Created wheel for absl-py: filename=absl_py-0.11.0-py2-none-any.whl size=124916 sha256=b11a5d9f8628e606fd57df36eb3b791cc21e7b6d28b0a40ef01b211d2c9dfb7a
  Stored in directory: /home/aimldl/.cache/pip/wheels/be/12/8b/0c41b135a6383624dedb48fa1c3a4c99f7961edafcb42e8189
  Building wheel for functools32 (setup.py) ... done
  Created wheel for functools32: filename=functools32-3.2.3.post2-py2-none-any.whl size=10943 sha256=f33873e30a9071f64f95136c16add6579c1e3a31ea0ee03c6e91863450aa86cb
  Stored in directory: /home/aimldl/.cache/pip/wheels/c2/ea/a3/25af52265fad6418a74df0b8d9ca8b89e0b3735dbd4d0d3794
  Building wheel for wrapt (setup.py) ... done
  Created wheel for wrapt: filename=wrapt-1.12.1-cp27-cp27mu-linux_x86_64.whl size=51195 sha256=3d4879f0aeafb82e9c048a45073a4922473b7cb6d3b59ef6c19a9f5180e4a250
  Stored in directory: /home/aimldl/.cache/pip/wheels/5b/d8/8e/81a83cb5321b940a954996f5b57fddc8976e712b3ac3a1a54b
Successfully built opt-einsum gast keras-applications termcolor absl-py functools32 wrapt
Installing collected packages: numpy, opt-einsum, gast, six, h5py, keras-applications, keras-preprocessing, astor, termcolor, funcsigs, mock, backports.weakref, protobuf, absl-py, scipy, functools32, pyasn1, pyasn1-modules, rsa, cachetools, setuptools, google-auth, chardet, urllib3, certifi, requests, futures, grpcio, oauthlib, requests-oauthlib, google-auth-oauthlib, werkzeug, markdown, tensorboard, wrapt, tensorflow-estimator, google-pasta, tensorflow
  WARNING: The scripts f2py, f2py2 and f2py2.7 are installed in '/home/aimldl/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  NOTE: The current PATH contains path(s) starting with `~`, which may not be expanded by all applications.
  WARNING: The scripts pyrsa-decrypt, pyrsa-encrypt, pyrsa-keygen, pyrsa-priv2pub, pyrsa-sign and pyrsa-verify are installed in '/home/aimldl/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  NOTE: The current PATH contains path(s) starting with `~`, which may not be expanded by all applications.
  WARNING: The scripts easy_install and easy_install-2.7 are installed in '/home/aimldl/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  NOTE: The current PATH contains path(s) starting with `~`, which may not be expanded by all applications.
  WARNING: The script chardetect is installed in '/home/aimldl/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  NOTE: The current PATH contains path(s) starting with `~`, which may not be expanded by all applications.
  WARNING: The script google-oauthlib-tool is installed in '/home/aimldl/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  NOTE: The current PATH contains path(s) starting with `~`, which may not be expanded by all applications.
  WARNING: The script markdown_py is installed in '/home/aimldl/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  NOTE: The current PATH contains path(s) starting with `~`, which may not be expanded by all applications.
  WARNING: The script tensorboard is installed in '/home/aimldl/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  NOTE: The current PATH contains path(s) starting with `~`, which may not be expanded by all applications.
  WARNING: The scripts estimator_ckpt_converter, saved_model_cli, tensorboard, tf_upgrade_v2, tflite_convert, toco and toco_from_protos are installed in '/home/aimldl/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  NOTE: The current PATH contains path(s) starting with `~`, which may not be expanded by all applications.
Successfully installed absl-py-0.11.0 astor-0.8.1 backports.weakref-1.0.post1 cachetools-3.1.1 certifi-2020.12.5 chardet-4.0.0 funcsigs-1.0.2 functools32-3.2.3.post2 futures-3.3.0 gast-0.2.2 google-auth-1.24.0 google-auth-oauthlib-0.4.1 google-pasta-0.2.0 grpcio-1.35.0 h5py-2.10.0 keras-applications-1.0.8 keras-preprocessing-1.1.2 markdown-3.1.1 mock-3.0.5 numpy-1.16.6 oauthlib-3.1.0 opt-einsum-2.3.2 protobuf-3.14.0 pyasn1-0.4.8 pyasn1-modules-0.2.8 requests-2.25.1 requests-oauthlib-1.3.0 rsa-4.5 scipy-1.2.2 setuptools-44.1.1 six-1.15.0 tensorboard-2.1.0 tensorflow-2.1.0 tensorflow-estimator-2.1.0 termcolor-1.1.0 urllib3-1.26.2 werkzeug-1.0.1 wrapt-1.12.1
$
```

