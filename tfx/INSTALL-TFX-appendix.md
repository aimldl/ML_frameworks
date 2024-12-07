

* 2021-01-08 (Fri)

# 부록. INSTALL-TFX

## 부록 A. `pip3 install tfx` 실행 결과

* `$ pip3 install tfx` 실행 시 주요 출력 메세지

* 성공적으로 설치된 패키지의 전체 리스트

* `$ pip3 install tfx` 실행 시 전체 출력 메세지

### `$ pip3 install tfx` 실행 시 주요 출력 메세지

* 설치된 시스템은 Alienware-Aurora-R7입니다. 

* 터미널 쉘의 `k3sserver@k3sserver-Alienware-Aurora-R7:~$`를 `$`로 생략했습니다.

```bash
$ pip3 install tfx
Collecting tfx
  Downloading tfx-0.26.0-py3-none-any.whl (2.2 MB)
     |████████████████████████████████| 2.2 MB 1.3 MB/s 
   ...
ERROR: tensorflow 2.3.2 has requirement numpy<1.19.0,>=1.16.0, but you'll have numpy 1.19.5 which is incompatible.
ERROR: apache-beam 2.25.0 has requirement requests<3.0.0,>=2.24.0, but you'll have requests 2.22.0 which is incompatible.
ERROR: google-api-python-client 1.12.8 has requirement httplib2<1dev,>=0.15.0, but you'll have httplib2 0.14.0 which is incompatible.
  ...
Successfully installed Send2Trash-1.5.0  ...
apache-beam-2.25.0  ...
google-api-core-1.24.1  ...
grpc-google-iam-v1-0.12.3  ...
ipython-7.19.0  ...
jupyter-client-6.1.7  ...
keras-preprocessing-1.1.2  ...
kubernetes-11.0.0  ...
numpy-1.19.5  ...
scikit-learn-0.24.0 scipy-1.6.0  ...
tensorboard-2.4.0  ...
tensorflow-2.3.2   ...
  ...
wrapt-1.12.1
$
```

`apache-beam`, `kubernetes`, `scikit-learn`, `tensorflow` 등이 성공적으로 설치되었습니다. 전체 패키지 리스트와 전체 출력 메세지는 아래에서 확인하세요.

버전 이슈로 인해 3개의 에러 메세지가 발생했습니다. 현 단계에서는 일단 진행해 봅니다.

```bash
ERROR: tensorflow 2.3.2 has requirement numpy<1.19.0,>=1.16.0, but you'll have numpy 1.19.5 which is incompatible.
ERROR: apache-beam 2.25.0 has requirement requests<3.0.0,>=2.24.0, but you'll have requests 2.22.0 which is incompatible.
ERROR: google-api-python-client 1.12.8 has requirement httplib2<1dev,>=0.15.0, but you'll have httplib2 0.14.0 which is incompatible.
```

### 성공적으로 설치된 패키지의 전체 리스트

```bash
Send2Trash-1.5.0 absl-py-0.10.0 apache-beam-2.25.0 argon2-cffi-20.1.0 astunparse-1.6.3 async-generator-1.10 attrs-20.3.0 avro-python3-1.9.2.1 backcall-0.2.0 bleach-3.2.1 cachetools-4.2.0 cffi-1.14.4 crcmod-1.7 decorator-4.4.2 defusedxml-0.6.0 dill-0.3.1.1 docker-4.4.1 docopt-0.6.2 fastavro-1.2.3 gast-0.3.3 google-api-core-1.24.1 google-api-python-client-1.12.8 google-apitools-0.5.31 google-auth-1.24.0 google-auth-httplib2-0.0.4 google-auth-oauthlib-0.4.2 google-cloud-bigquery-1.28.0 google-cloud-bigtable-1.6.1 google-cloud-build-2.0.0 google-cloud-core-1.5.0 google-cloud-datastore-1.15.3 google-cloud-dlp-1.0.0 google-cloud-language-1.3.0 google-cloud-pubsub-1.7.0 google-cloud-spanner-1.19.1 google-cloud-storage-1.35.0 google-cloud-videointelligence-1.16.1 google-cloud-vision-1.0.0 google-crc32c-1.1.0 google-pasta-0.2.0 google-resumable-media-1.2.0 googleapis-common-protos-1.52.0 grpc-google-iam-v1-0.12.3 grpcio-1.34.0 grpcio-gcp-0.2.2 h5py-2.10.0 hdfs-2.5.8 ipykernel-5.4.2 ipython-7.19.0 ipython-genutils-0.2.0 ipywidgets-7.6.3 jedi-0.18.0 jinja2-2.11.2 joblib-0.14.1 jsonschema-3.2.0 jupyter-client-6.1.7 jupyter-core-4.7.0 jupyterlab-pygments-0.1.2 jupyterlab-widgets-1.0.0 keras-preprocessing-1.1.2 keras-tuner-1.0.1 kubernetes-11.0.0 libcst-0.3.16 markdown-3.3.3 mistune-0.8.4 ml-metadata-0.26.0 ml-pipelines-sdk-0.26.0 mock-2.0.0 mypy-extensions-0.4.3 nbclient-0.5.1 nbconvert-6.0.7 nbformat-5.0.8 nest-asyncio-1.4.3 notebook-6.1.6 numpy-1.19.5 oauth2client-4.1.3 opt-einsum-3.3.0 packaging-20.8 pandas-1.2.0 pandocfilters-1.4.3 parso-0.8.1 pbr-5.5.1 pickleshare-0.7.5 prometheus-client-0.9.0 promise-2.3 prompt-toolkit-3.0.9 proto-plus-1.13.0 protobuf-3.14.0 ptyprocess-0.7.0 pyarrow-0.17.1 pyasn1-0.4.8 pyasn1-modules-0.2.8 pycparser-2.20 pydot-1.4.1 pygments-2.7.3 pymongo-3.11.2 pyparsing-2.4.7 pyrsistent-0.17.3 python-dateutil-2.8.1 pyzmq-20.0.0 requests-oauthlib-1.3.0 rsa-4.6 scikit-learn-0.24.0 scipy-1.6.0 tabulate-0.8.7 tensorboard-2.4.0 tensorboard-plugin-wit-1.7.0 tensorflow-2.3.2 tensorflow-cloud-0.1.11 tensorflow-data-validation-0.26.0 tensorflow-datasets-3.0.0 tensorflow-estimator-2.3.0 tensorflow-hub-0.9.0 tensorflow-metadata-0.26.0 tensorflow-model-analysis-0.26.0 tensorflow-serving-api-2.3.0 tensorflow-transform-0.26.0 termcolor-1.1.0 terminado-0.9.2 terminaltables-3.1.0 testpath-0.4.4 tfx-0.26.0 tfx-bsl-0.26.1 threadpoolctl-2.1.0 tornado-6.1 tqdm-4.55.1 traitlets-5.0.5 typing-extensions-3.7.4.3 typing-inspect-0.6.0 uritemplate-3.0.1 wcwidth-0.2.5 webencodings-0.5.1 websocket-client-0.57.0 werkzeug-1.0.1 widgetsnbextension-3.5.1 wrapt-1.12.1
```



### `$ pip3 install tfx` 실행 시 전체 출력 메세지

```bash
$ pip3 install tfx
Collecting tfx
  Downloading tfx-0.26.0-py3-none-any.whl (2.2 MB)
     |████████████████████████████████| 2.2 MB 1.3 MB/s 
Collecting tensorflow-data-validation<0.27,>=0.26
  Downloading tensorflow_data_validation-0.26.0-cp38-cp38-manylinux2010_x86_64.whl (1.3 MB)
     |████████████████████████████████| 1.3 MB 12.4 MB/s 
Collecting absl-py<0.11,>=0.9
  Downloading absl_py-0.10.0-py3-none-any.whl (127 kB)
     |████████████████████████████████| 127 kB 7.8 MB/s 
Collecting keras-tuner<1.0.2,>=1
  Downloading keras-tuner-1.0.1.tar.gz (54 kB)
     |████████████████████████████████| 54 kB 2.8 MB/s 
Collecting tensorflow-model-analysis<0.27,>=0.26
  Downloading tensorflow_model_analysis-0.26.0-py3-none-any.whl (1.7 MB)
     |████████████████████████████████| 1.7 MB 13.8 MB/s 
Collecting apache-beam[gcp]!=2.26.*,<3,>=2.25
  Downloading apache_beam-2.25.0-cp38-cp38-manylinux2010_x86_64.whl (10.3 MB)
     |████████████████████████████████| 10.3 MB 99 kB/s 
Collecting tfx-bsl<0.27,>=0.26.1
  Downloading tfx_bsl-0.26.1-cp38-cp38-manylinux2010_x86_64.whl (2.2 MB)
     |████████████████████████████████| 2.2 MB 14.1 MB/s 
Collecting tensorflow-serving-api!=2.0.*,!=2.1.*,!=2.2.*,!=2.4.*,<3,>=1.15
  Downloading tensorflow_serving_api-2.3.0-py2.py3-none-any.whl (38 kB)
Collecting docker<5,>=4.1
  Downloading docker-4.4.1-py2.py3-none-any.whl (146 kB)
     |████████████████████████████████| 146 kB 3.9 MB/s 
Collecting tensorflow!=2.0.*,!=2.1.*,!=2.2.*,!=2.4.*,<3,>=1.15.2
  Downloading tensorflow-2.3.2-cp38-cp38-manylinux2010_x86_64.whl (320.5 MB)
     |████████████████████████████████| 320.5 MB 9.0 MB/s 
Requirement already satisfied: six<2,>=1.10 in /usr/lib/python3/dist-packages (from tfx) (1.14.0)
Requirement already satisfied: click<8,>=7 in /usr/lib/python3/dist-packages (from tfx) (7.0)
Collecting grpcio<2,>=1.28.1
  Downloading grpcio-1.34.0-cp38-cp38-manylinux2014_x86_64.whl (4.0 MB)
     |████████████████████████████████| 4.0 MB 8.6 MB/s 
Requirement already satisfied: pyyaml<6,>=3.12 in /usr/lib/python3/dist-packages (from tfx) (5.3.1)
Collecting tensorflow-hub<0.10,>=0.9.0
  Downloading tensorflow_hub-0.9.0-py2.py3-none-any.whl (103 kB)
     |████████████████████████████████| 103 kB 7.7 MB/s 
Collecting attrs<21,>=19.3.0
  Downloading attrs-20.3.0-py2.py3-none-any.whl (49 kB)
     |████████████████████████████████| 49 kB 5.5 MB/s 
Collecting pyarrow<0.18,>=0.17
  Downloading pyarrow-0.17.1-cp38-cp38-manylinux2014_x86_64.whl (63.8 MB)
     |████████████████████████████████| 63.8 MB 1.7 MB/s 
Collecting tensorflow-cloud<0.2,>=0.1
  Downloading tensorflow_cloud-0.1.11-py3-none-any.whl (87 kB)
     |████████████████████████████████| 87 kB 3.2 MB/s 
Collecting kubernetes<12,>=10.0.1
  Downloading kubernetes-11.0.0-py3-none-any.whl (1.5 MB)
     |████████████████████████████████| 1.5 MB 24.1 MB/s 
Collecting tensorflow-transform<0.27,>=0.26
  Downloading tensorflow_transform-0.26.0-py3-none-any.whl (380 kB)
     |████████████████████████████████| 380 kB 5.5 MB/s 
Collecting jinja2<3,>=2.7.3
  Downloading Jinja2-2.11.2-py2.py3-none-any.whl (125 kB)
     |████████████████████████████████| 125 kB 9.7 MB/s 
Collecting ml-pipelines-sdk==0.26.0
  Downloading ml_pipelines_sdk-0.26.0-py3-none-any.whl (1.1 MB)
     |████████████████████████████████| 1.1 MB 6.7 MB/s 
Collecting protobuf<4,>=3.12.2
  Downloading protobuf-3.14.0-cp38-cp38-manylinux1_x86_64.whl (1.0 MB)
     |████████████████████████████████| 1.0 MB 10.0 MB/s 
Collecting ml-metadata<0.27,>=0.26
  Downloading ml_metadata-0.26.0-cp38-cp38-manylinux2010_x86_64.whl (2.8 MB)
     |████████████████████████████████| 2.8 MB 6.7 MB/s 
Collecting google-api-python-client<2,>=1.7.8
  Downloading google_api_python_client-1.12.8-py2.py3-none-any.whl (61 kB)
     |████████████████████████████████| 61 kB 22 kB/s 
Collecting numpy<2,>=1.16
  Downloading numpy-1.19.5-cp38-cp38-manylinux2010_x86_64.whl (14.9 MB)
     |████████████████████████████████| 14.9 MB 2.1 MB/s 
Collecting tensorflow-metadata<0.27,>=0.26
  Downloading tensorflow_metadata-0.26.0-py3-none-any.whl (47 kB)
     |████████████████████████████████| 47 kB 3.2 MB/s 
Collecting pandas<2,>=1.0
  Downloading pandas-1.2.0-cp38-cp38-manylinux1_x86_64.whl (9.7 MB)
     |████████████████████████████████| 9.7 MB 20.5 MB/s 
Collecting joblib<0.15,>=0.12
  Downloading joblib-0.14.1-py2.py3-none-any.whl (294 kB)
     |████████████████████████████████| 294 kB 7.3 MB/s 
Requirement already satisfied: colorama in /usr/lib/python3/dist-packages (from keras-tuner<1.0.2,>=1->tfx) (0.4.3)
Requirement already satisfied: future in /usr/lib/python3/dist-packages (from keras-tuner<1.0.2,>=1->tfx) (0.18.2)
Requirement already satisfied: requests in /usr/lib/python3/dist-packages (from keras-tuner<1.0.2,>=1->tfx) (2.22.0)
Collecting scikit-learn
  Downloading scikit_learn-0.24.0-cp38-cp38-manylinux2010_x86_64.whl (24.9 MB)
     |████████████████████████████████| 24.9 MB 52 kB/s 
Collecting scipy
  Downloading scipy-1.6.0-cp38-cp38-manylinux1_x86_64.whl (27.2 MB)
     |████████████████████████████████| 27.2 MB 1.2 MB/s 
Collecting tabulate
  Downloading tabulate-0.8.7-py3-none-any.whl (24 kB)
Collecting terminaltables
  Downloading terminaltables-3.1.0.tar.gz (12 kB)
Collecting tqdm
  Downloading tqdm-4.55.1-py2.py3-none-any.whl (68 kB)
     |████████████████████████████████| 68 kB 4.6 MB/s 
Collecting ipywidgets<8,>=7
  Downloading ipywidgets-7.6.3-py2.py3-none-any.whl (121 kB)
     |████████████████████████████████| 121 kB 9.7 MB/s 
Collecting ipython<8,>=7
  Downloading ipython-7.19.0-py3-none-any.whl (784 kB)
     |████████████████████████████████| 784 kB 16.3 MB/s 
Collecting pydot<2,>=1.2.0
  Downloading pydot-1.4.1-py2.py3-none-any.whl (19 kB)
Collecting crcmod<2.0,>=1.7
  Downloading crcmod-1.7.tar.gz (89 kB)
     |████████████████████████████████| 89 kB 6.0 MB/s 
Collecting oauth2client<5,>=2.0.1
  Downloading oauth2client-4.1.3-py2.py3-none-any.whl (98 kB)
     |████████████████████████████████| 98 kB 3.5 MB/s 
Collecting fastavro<2,>=0.21.4
  Downloading fastavro-1.2.3-cp38-cp38-manylinux2014_x86_64.whl (2.4 MB)
     |████████████████████████████████| 2.4 MB 18.6 MB/s 
Collecting avro-python3!=1.9.2,<1.10.0,>=1.8.1; python_version >= "3.0"
  Downloading avro-python3-1.9.2.1.tar.gz (37 kB)
Collecting python-dateutil<3,>=2.8.0
  Downloading python_dateutil-2.8.1-py2.py3-none-any.whl (227 kB)
     |████████████████████████████████| 227 kB 14.2 MB/s 
Collecting typing-extensions<3.8.0,>=3.7.0
  Downloading typing_extensions-3.7.4.3-py3-none-any.whl (22 kB)
Collecting pymongo<4.0.0,>=3.8.0
  Downloading pymongo-3.11.2-cp38-cp38-manylinux2014_x86_64.whl (531 kB)
     |████████████████████████████████| 531 kB 6.0 MB/s 
Requirement already satisfied: pytz>=2018.3 in /usr/lib/python3/dist-packages (from apache-beam[gcp]!=2.26.*,<3,>=2.25->tfx) (2019.3)
Collecting hdfs<3.0.0,>=2.1.0
  Downloading hdfs-2.5.8.tar.gz (41 kB)
     |████████████████████████████████| 41 kB 347 kB/s 
Collecting dill<0.3.2,>=0.3.1.1
  Downloading dill-0.3.1.1.tar.gz (151 kB)
     |████████████████████████████████| 151 kB 9.6 MB/s 
Requirement already satisfied: httplib2<0.18.0,>=0.8 in /usr/lib/python3/dist-packages (from apache-beam[gcp]!=2.26.*,<3,>=2.25->tfx) (0.14.0)
Collecting mock<3.0.0,>=1.0.1
  Downloading mock-2.0.0-py2.py3-none-any.whl (56 kB)
     |████████████████████████████████| 56 kB 3.7 MB/s 
Collecting google-auth<2,>=1.18.0; extra == "gcp"
  Downloading google_auth-1.24.0-py2.py3-none-any.whl (114 kB)
     |████████████████████████████████| 114 kB 7.8 MB/s 
Collecting google-cloud-spanner<2,>=1.13.0; extra == "gcp"
  Downloading google_cloud_spanner-1.19.1-py2.py3-none-any.whl (255 kB)
     |████████████████████████████████| 255 kB 13.4 MB/s 
Collecting google-cloud-language<2,>=1.3.0; extra == "gcp"
  Downloading google_cloud_language-1.3.0-py2.py3-none-any.whl (83 kB)
     |████████████████████████████████| 83 kB 2.1 MB/s 
Collecting google-cloud-pubsub<2,>=0.39.0; extra == "gcp"
  Downloading google_cloud_pubsub-1.7.0-py2.py3-none-any.whl (144 kB)
     |████████████████████████████████| 144 kB 4.1 MB/s 
Collecting google-cloud-bigtable<2,>=0.31.1; extra == "gcp"
  Downloading google_cloud_bigtable-1.6.1-py2.py3-none-any.whl (267 kB)
     |████████████████████████████████| 267 kB 15.8 MB/s 
Collecting google-cloud-videointelligence<2,>=1.8.0; extra == "gcp"
  Downloading google_cloud_videointelligence-1.16.1-py2.py3-none-any.whl (183 kB)
     |████████████████████████████████| 183 kB 13.5 MB/s 
Collecting google-cloud-datastore<2,>=1.7.1; extra == "gcp"
  Downloading google_cloud_datastore-1.15.3-py2.py3-none-any.whl (134 kB)
     |████████████████████████████████| 134 kB 5.6 MB/s 
Collecting grpcio-gcp<1,>=0.2.2; extra == "gcp"
  Downloading grpcio_gcp-0.2.2-py2.py3-none-any.whl (9.4 kB)
Collecting google-cloud-dlp<2,>=0.12.0; extra == "gcp"
  Downloading google_cloud_dlp-1.0.0-py2.py3-none-any.whl (169 kB)
     |████████████████████████████████| 169 kB 3.3 MB/s 
Collecting google-cloud-build<3,>=2.0.0; python_version >= "3.6" and extra == "gcp"
  Downloading google_cloud_build-2.0.0-py2.py3-none-any.whl (67 kB)
     |████████████████████████████████| 67 kB 4.7 MB/s 
Collecting google-cloud-bigquery<2,>=1.6.0; extra == "gcp"
  Downloading google_cloud_bigquery-1.28.0-py2.py3-none-any.whl (187 kB)
     |████████████████████████████████| 187 kB 4.4 MB/s 
Collecting google-apitools<0.5.32,>=0.5.31; extra == "gcp"
  Downloading google-apitools-0.5.31.tar.gz (173 kB)
     |████████████████████████████████| 173 kB 12.1 MB/s 
Collecting google-cloud-vision<2,>=0.38.0; extra == "gcp"
  Downloading google_cloud_vision-1.0.0-py2.py3-none-any.whl (435 kB)
     |████████████████████████████████| 435 kB 19.0 MB/s 
Collecting google-cloud-core<2,>=0.28.1; extra == "gcp"
  Downloading google_cloud_core-1.5.0-py2.py3-none-any.whl (27 kB)
Collecting cachetools<5,>=3.1.0; extra == "gcp"
  Downloading cachetools-4.2.0-py3-none-any.whl (12 kB)
Collecting websocket-client>=0.32.0
  Downloading websocket_client-0.57.0-py2.py3-none-any.whl (200 kB)
     |████████████████████████████████| 200 kB 12.7 MB/s 
Requirement already satisfied: wheel>=0.26 in /usr/lib/python3/dist-packages (from tensorflow!=2.0.*,!=2.1.*,!=2.2.*,!=2.4.*,<3,>=1.15.2->tfx) (0.34.2)
Collecting google-pasta>=0.1.8
  Downloading google_pasta-0.2.0-py3-none-any.whl (57 kB)
     |████████████████████████████████| 57 kB 4.6 MB/s 
Collecting h5py<2.11.0,>=2.10.0
  Downloading h5py-2.10.0-cp38-cp38-manylinux1_x86_64.whl (2.9 MB)
     |████████████████████████████████| 2.9 MB 14.2 MB/s 
Collecting tensorflow-estimator<2.4.0,>=2.3.0
  Downloading tensorflow_estimator-2.3.0-py2.py3-none-any.whl (459 kB)
     |████████████████████████████████| 459 kB 20.6 MB/s 
Collecting wrapt>=1.11.1
  Downloading wrapt-1.12.1.tar.gz (27 kB)
Collecting astunparse==1.6.3
  Downloading astunparse-1.6.3-py2.py3-none-any.whl (12 kB)
Collecting termcolor>=1.1.0
  Downloading termcolor-1.1.0.tar.gz (3.9 kB)
Collecting tensorboard<3,>=2.3.0
  Downloading tensorboard-2.4.0-py3-none-any.whl (10.6 MB)
     |████████████████████████████████| 10.6 MB 2.2 MB/s 
Collecting opt-einsum>=2.3.2
  Downloading opt_einsum-3.3.0-py3-none-any.whl (65 kB)
     |████████████████████████████████| 65 kB 2.8 MB/s 
Collecting keras-preprocessing<1.2,>=1.1.1
  Downloading Keras_Preprocessing-1.1.2-py2.py3-none-any.whl (42 kB)
     |████████████████████████████████| 42 kB 1.5 MB/s 
Collecting gast==0.3.3
  Downloading gast-0.3.3-py2.py3-none-any.whl (9.7 kB)
Collecting tensorflow-datasets<3.1.0
  Downloading tensorflow_datasets-3.0.0-py3-none-any.whl (3.3 MB)
     |████████████████████████████████| 3.3 MB 15.4 MB/s 
Collecting google-cloud-storage
  Downloading google_cloud_storage-1.35.0-py2.py3-none-any.whl (96 kB)
     |████████████████████████████████| 96 kB 3.2 MB/s 
Requirement already satisfied: urllib3>=1.24.2 in /usr/lib/python3/dist-packages (from kubernetes<12,>=10.0.1->tfx) (1.25.8)
Collecting requests-oauthlib
  Downloading requests_oauthlib-1.3.0-py2.py3-none-any.whl (23 kB)
Requirement already satisfied: certifi>=14.05.14 in /usr/lib/python3/dist-packages (from kubernetes<12,>=10.0.1->tfx) (2019.11.28)
Requirement already satisfied: setuptools>=21.0.0 in /usr/lib/python3/dist-packages (from kubernetes<12,>=10.0.1->tfx) (45.2.0)
Requirement already satisfied: MarkupSafe>=0.23 in /usr/lib/python3/dist-packages (from jinja2<3,>=2.7.3->tfx) (1.1.0)
Collecting google-api-core<2dev,>=1.21.0
  Downloading google_api_core-1.24.1-py2.py3-none-any.whl (92 kB)
     |████████████████████████████████| 92 kB 6.2 MB/s 
Collecting uritemplate<4dev,>=3.0.0
  Downloading uritemplate-3.0.1-py2.py3-none-any.whl (15 kB)
Collecting google-auth-httplib2>=0.0.3
  Downloading google_auth_httplib2-0.0.4-py2.py3-none-any.whl (9.1 kB)
Collecting googleapis-common-protos<2,>=1.52.0
  Downloading googleapis_common_protos-1.52.0-py2.py3-none-any.whl (100 kB)
     |████████████████████████████████| 100 kB 7.6 MB/s 
Collecting threadpoolctl>=2.0.0
  Downloading threadpoolctl-2.1.0-py3-none-any.whl (12 kB)
Collecting traitlets>=4.3.1
  Downloading traitlets-5.0.5-py3-none-any.whl (100 kB)
     |████████████████████████████████| 100 kB 4.7 MB/s 
Collecting nbformat>=4.2.0
  Downloading nbformat-5.0.8-py3-none-any.whl (172 kB)
     |████████████████████████████████| 172 kB 12.6 MB/s 
Collecting ipykernel>=4.5.1
  Downloading ipykernel-5.4.2-py3-none-any.whl (119 kB)
     |████████████████████████████████| 119 kB 14.6 MB/s 
Collecting jupyterlab-widgets>=1.0.0; python_version >= "3.6"
  Downloading jupyterlab_widgets-1.0.0-py3-none-any.whl (243 kB)
     |████████████████████████████████| 243 kB 10.3 MB/s 
Collecting widgetsnbextension~=3.5.0
  Downloading widgetsnbextension-3.5.1-py2.py3-none-any.whl (2.2 MB)
     |████████████████████████████████| 2.2 MB 4.3 MB/s 
Collecting pickleshare
  Downloading pickleshare-0.7.5-py2.py3-none-any.whl (6.9 kB)
Collecting jedi>=0.10
  Downloading jedi-0.18.0-py2.py3-none-any.whl (1.4 MB)
     |████████████████████████████████| 1.4 MB 14.2 MB/s 
Collecting pygments
  Downloading Pygments-2.7.3-py3-none-any.whl (950 kB)
     |████████████████████████████████| 950 kB 13.9 MB/s 
Collecting prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0
  Downloading prompt_toolkit-3.0.9-py3-none-any.whl (355 kB)
     |████████████████████████████████| 355 kB 11.4 MB/s 
Collecting backcall
  Downloading backcall-0.2.0-py2.py3-none-any.whl (11 kB)
Requirement already satisfied: pexpect>4.3; sys_platform != "win32" in /usr/lib/python3/dist-packages (from ipython<8,>=7->tensorflow-model-analysis<0.27,>=0.26->tfx) (4.6.0)
Collecting decorator
  Downloading decorator-4.4.2-py2.py3-none-any.whl (9.2 kB)
Collecting pyparsing>=2.1.4
  Downloading pyparsing-2.4.7-py2.py3-none-any.whl (67 kB)
     |████████████████████████████████| 67 kB 5.1 MB/s 
Collecting pyasn1-modules>=0.0.5
  Downloading pyasn1_modules-0.2.8-py2.py3-none-any.whl (155 kB)
     |████████████████████████████████| 155 kB 15.2 MB/s 
Collecting pyasn1>=0.1.7
  Downloading pyasn1-0.4.8-py2.py3-none-any.whl (77 kB)
     |████████████████████████████████| 77 kB 4.4 MB/s 
Collecting rsa>=3.1.4
  Downloading rsa-4.6-py3-none-any.whl (47 kB)
     |████████████████████████████████| 47 kB 4.0 MB/s 
Collecting docopt
  Downloading docopt-0.6.2.tar.gz (25 kB)
Collecting pbr>=0.11
  Downloading pbr-5.5.1-py2.py3-none-any.whl (106 kB)
     |████████████████████████████████| 106 kB 9.5 MB/s 
Collecting grpc-google-iam-v1<0.13dev,>=0.12.3
  Downloading grpc-google-iam-v1-0.12.3.tar.gz (13 kB)
Collecting proto-plus>=0.4.0
  Downloading proto-plus-1.13.0.tar.gz (44 kB)
     |████████████████████████████████| 44 kB 2.6 MB/s 
Collecting libcst>=0.2.5
  Downloading libcst-0.3.16-py3-none-any.whl (505 kB)
     |████████████████████████████████| 505 kB 13.2 MB/s 
Collecting google-resumable-media<2.0dev,>=0.6.0
  Downloading google_resumable_media-1.2.0-py2.py3-none-any.whl (75 kB)
     |████████████████████████████████| 75 kB 3.5 MB/s 
Requirement already satisfied: fasteners>=0.14 in /usr/lib/python3/dist-packages (from google-apitools<0.5.32,>=0.5.31; extra == "gcp"->apache-beam[gcp]!=2.26.*,<3,>=2.25->tfx) (0.14.1)
Collecting tensorboard-plugin-wit>=1.6.0
  Downloading tensorboard_plugin_wit-1.7.0-py3-none-any.whl (779 kB)
     |████████████████████████████████| 779 kB 7.0 MB/s 
Collecting google-auth-oauthlib<0.5,>=0.4.1
  Downloading google_auth_oauthlib-0.4.2-py2.py3-none-any.whl (18 kB)
Collecting markdown>=2.6.8
  Downloading Markdown-3.3.3-py3-none-any.whl (96 kB)
     |████████████████████████████████| 96 kB 3.5 MB/s 
Collecting werkzeug>=0.11.15
  Downloading Werkzeug-1.0.1-py2.py3-none-any.whl (298 kB)
     |████████████████████████████████| 298 kB 5.0 MB/s 
Collecting promise
  Downloading promise-2.3.tar.gz (19 kB)
Requirement already satisfied: oauthlib>=3.0.0 in /usr/lib/python3/dist-packages (from requests-oauthlib->kubernetes<12,>=10.0.1->tfx) (3.1.0)
Collecting ipython-genutils
  Downloading ipython_genutils-0.2.0-py2.py3-none-any.whl (26 kB)
Collecting jupyter-core
  Downloading jupyter_core-4.7.0-py3-none-any.whl (82 kB)
     |████████████████████████████████| 82 kB 1.1 MB/s 
Collecting jsonschema!=2.5.0,>=2.4
  Downloading jsonschema-3.2.0-py2.py3-none-any.whl (56 kB)
     |████████████████████████████████| 56 kB 4.4 MB/s 
Collecting jupyter-client
  Downloading jupyter_client-6.1.7-py3-none-any.whl (108 kB)
     |████████████████████████████████| 108 kB 9.5 MB/s 
Collecting tornado>=4.2
  Downloading tornado-6.1-cp38-cp38-manylinux2010_x86_64.whl (427 kB)
     |████████████████████████████████| 427 kB 4.5 MB/s 
Collecting notebook>=4.4.1
  Downloading notebook-6.1.6-py3-none-any.whl (9.5 MB)
     |████████████████████████████████| 9.5 MB 258 kB/s 
Collecting parso<0.9.0,>=0.8.0
  Downloading parso-0.8.1-py2.py3-none-any.whl (93 kB)
     |████████████████████████████████| 93 kB 1.1 MB/s 
Collecting wcwidth
  Downloading wcwidth-0.2.5-py2.py3-none-any.whl (30 kB)
Collecting typing-inspect>=0.4.0
  Downloading typing_inspect-0.6.0-py3-none-any.whl (8.1 kB)
Collecting google-crc32c<2.0dev,>=1.0; python_version >= "3.5"
  Downloading google_crc32c-1.1.0-cp38-cp38-manylinux2010_x86_64.whl (39 kB)
Collecting pyrsistent>=0.14.0
  Downloading pyrsistent-0.17.3.tar.gz (106 kB)
     |████████████████████████████████| 106 kB 10.6 MB/s 
Collecting pyzmq>=13
  Downloading pyzmq-20.0.0-cp38-cp38-manylinux1_x86_64.whl (1.1 MB)
     |████████████████████████████████| 1.1 MB 12.2 MB/s 
Collecting Send2Trash
  Downloading Send2Trash-1.5.0-py3-none-any.whl (12 kB)
Collecting argon2-cffi
  Downloading argon2_cffi-20.1.0-cp35-abi3-manylinux1_x86_64.whl (97 kB)
     |████████████████████████████████| 97 kB 1.7 MB/s 
Collecting nbconvert
  Downloading nbconvert-6.0.7-py3-none-any.whl (552 kB)
     |████████████████████████████████| 552 kB 7.3 MB/s 
Collecting prometheus-client
  Downloading prometheus_client-0.9.0-py2.py3-none-any.whl (53 kB)
     |████████████████████████████████| 53 kB 2.2 MB/s 
Collecting terminado>=0.8.3
  Downloading terminado-0.9.2-py3-none-any.whl (14 kB)
Collecting mypy-extensions>=0.3.0
  Downloading mypy_extensions-0.4.3-py2.py3-none-any.whl (4.5 kB)
Collecting cffi>=1.0.0
  Downloading cffi-1.14.4-cp38-cp38-manylinux1_x86_64.whl (411 kB)
     |████████████████████████████████| 411 kB 8.9 MB/s 
Collecting nbclient<0.6.0,>=0.5.0
  Downloading nbclient-0.5.1-py3-none-any.whl (65 kB)
     |████████████████████████████████| 65 kB 3.9 MB/s 
Requirement already satisfied: entrypoints>=0.2.2 in /usr/lib/python3/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets<8,>=7->tensorflow-model-analysis<0.27,>=0.26->tfx) (0.3)
Collecting defusedxml
  Downloading defusedxml-0.6.0-py2.py3-none-any.whl (23 kB)
Collecting jupyterlab-pygments
  Downloading jupyterlab_pygments-0.1.2-py-2.py3-none-any.whl (4.6 kB)
Collecting mistune<2,>=0.8.1
  Downloading mistune-0.8.4-py2.py3-none-any.whl (16 kB)
Collecting bleach
  Downloading bleach-3.2.1-py2.py3-none-any.whl (145 kB)
     |████████████████████████████████| 145 kB 6.6 MB/s 
Collecting pandocfilters>=1.4.1
  Downloading pandocfilters-1.4.3.tar.gz (16 kB)
Collecting testpath
  Downloading testpath-0.4.4-py2.py3-none-any.whl (163 kB)
     |████████████████████████████████| 163 kB 5.8 MB/s 
Collecting ptyprocess; os_name != "nt"
  Downloading ptyprocess-0.7.0-py2.py3-none-any.whl (13 kB)
Collecting pycparser
  Downloading pycparser-2.20-py2.py3-none-any.whl (112 kB)
     |████████████████████████████████| 112 kB 11.7 MB/s 
Collecting async-generator
  Downloading async_generator-1.10-py3-none-any.whl (18 kB)
Collecting nest-asyncio
  Downloading nest_asyncio-1.4.3-py3-none-any.whl (5.3 kB)
Collecting webencodings
  Downloading webencodings-0.5.1-py2.py3-none-any.whl (11 kB)
Collecting packaging
  Downloading packaging-20.8-py2.py3-none-any.whl (39 kB)
Building wheels for collected packages: keras-tuner, terminaltables, crcmod, avro-python3, hdfs, dill, google-apitools, wrapt, termcolor, docopt, grpc-google-iam-v1, proto-plus, promise, pyrsistent, pandocfilters
  Building wheel for keras-tuner (setup.py) ... done
  Created wheel for keras-tuner: filename=keras_tuner-1.0.1-py3-none-any.whl size=73196 sha256=8430a6a809d68603e97443dc170e5c2f0971c107818ee159ead927f3dfc08c9c
  Stored in directory: /home/k3sserver/.cache/pip/wheels/62/84/96/51c62791835c5185b9f66e915e19ae7c20f3d8c40443b3e9fa
  Building wheel for terminaltables (setup.py) ... done
  Created wheel for terminaltables: filename=terminaltables-3.1.0-py3-none-any.whl size=15354 sha256=efdb165cfe3edb6e78a8f46f83c7d3c79dd4c414a79f9c636f500d5da4a73bfc
  Stored in directory: /home/k3sserver/.cache/pip/wheels/08/8f/5f/253d0105a55bd84ee61ef0d37dbf70421e61e0cd70cef7c5e1
  Building wheel for crcmod (setup.py) ... done
  Created wheel for crcmod: filename=crcmod-1.7-cp38-cp38-linux_x86_64.whl size=35984 sha256=a7d448cafc16348c3219093c41267929f4f34903b263d11102d1fb93921b06a4
  Stored in directory: /home/k3sserver/.cache/pip/wheels/ca/5a/02/f3acf982a026f3319fb3e798a8dca2d48fafee7761788562e9
  Building wheel for avro-python3 (setup.py) ... done
  Created wheel for avro-python3: filename=avro_python3-1.9.2.1-py3-none-any.whl size=43513 sha256=d100323983d7bb28b4e8679292f0637d7ebfeecf9885e9dc0b2d684a8d0e7130
  Stored in directory: /home/k3sserver/.cache/pip/wheels/a5/f2/87/b7c4b9d5915716d94e8bf2e2f3bfbbd73bb5fe2a98677a59cb
  Building wheel for hdfs (setup.py) ... done
  Created wheel for hdfs: filename=hdfs-2.5.8-py3-none-any.whl size=33213 sha256=0653f3db484f6b1b43de876f5856b5035976c4f656d564f31cb66de755aa37a9
  Stored in directory: /home/k3sserver/.cache/pip/wheels/43/cb/59/3fdce328ada746ea437798538a9808e4f730135f5a26f137a4
  Building wheel for dill (setup.py) ... done
  Created wheel for dill: filename=dill-0.3.1.1-py3-none-any.whl size=78530 sha256=8e6c5568db685528b833f19c369afd5c6419b5ca13ba21ce70042b32f862f3c1
  Stored in directory: /home/k3sserver/.cache/pip/wheels/07/35/78/e9004fa30578734db7f10e7a211605f3f0778d2bdde38a239d
  Building wheel for google-apitools (setup.py) ... done
  Created wheel for google-apitools: filename=google_apitools-0.5.31-py3-none-any.whl size=131042 sha256=ce1153cf953746800a5971723efd50bce50600155643bdb5d51d69fbc05fa0b6
  Stored in directory: /home/k3sserver/.cache/pip/wheels/d7/54/79/85de1824f2f4175fb4960c72afb10045d86700c3941dc73685
  Building wheel for wrapt (setup.py) ... done
  Created wheel for wrapt: filename=wrapt-1.12.1-cp38-cp38-linux_x86_64.whl size=78517 sha256=beedf20e8be7ae82b13e2d698187c4c72af6b619a4983b9d4350c8adec709ec3
  Stored in directory: /home/k3sserver/.cache/pip/wheels/5f/fd/9e/b6cf5890494cb8ef0b5eaff72e5d55a70fb56316007d6dfe73
  Building wheel for termcolor (setup.py) ... done
  Created wheel for termcolor: filename=termcolor-1.1.0-py3-none-any.whl size=4830 sha256=0c826808879d3b5818c040b2e33eca2dcb6d7dfb5ba0e5f752430b8e44e2ff93
  Stored in directory: /home/k3sserver/.cache/pip/wheels/a0/16/9c/5473df82468f958445479c59e784896fa24f4a5fc024b0f501
  Building wheel for docopt (setup.py) ... done
  Created wheel for docopt: filename=docopt-0.6.2-py2.py3-none-any.whl size=13704 sha256=4d89db2905a1b6b1f9519091918c837a99ac42915851ad7233ab15bd933ebb5c
  Stored in directory: /home/k3sserver/.cache/pip/wheels/56/ea/58/ead137b087d9e326852a851351d1debf4ada529b6ac0ec4e8c
  Building wheel for grpc-google-iam-v1 (setup.py) ... done
  Created wheel for grpc-google-iam-v1: filename=grpc_google_iam_v1-0.12.3-py3-none-any.whl size=18483 sha256=6b78eccd1c410aad49a4153c1b7e4e4471b2b69fe7935b8e5676c8161a27e9d6
  Stored in directory: /home/k3sserver/.cache/pip/wheels/8f/b9/13/fce3d62261f63c01b28281fe6a9d704a7af65d96ff2c88552e
  Building wheel for proto-plus (setup.py) ... done
  Created wheel for proto-plus: filename=proto_plus-1.13.0-py3-none-any.whl size=41591 sha256=ae4dca927aa99d6911575423bba413a941c64f50aef73ba39fa4c760201cf1b3
  Stored in directory: /home/k3sserver/.cache/pip/wheels/c4/f7/51/d264693ef5a67296bb5601bca5834f5d5b12e325eb4b2d3f7f
  Building wheel for promise (setup.py) ... done
  Created wheel for promise: filename=promise-2.3-py3-none-any.whl size=21493 sha256=09267d8fc54f240c225a837aebc830d2f8e41771826ee937bbf6dc1289adcff9
  Stored in directory: /home/k3sserver/.cache/pip/wheels/54/aa/01/724885182f93150035a2a91bce34a12877e8067a97baaf5dc8
  Building wheel for pyrsistent (setup.py) ... done
  Created wheel for pyrsistent: filename=pyrsistent-0.17.3-cp38-cp38-linux_x86_64.whl size=106642 sha256=7b98d9124e9802b5acab4104f05d2b9d3310ac5e56e622cb2cb7cce2f4ef22fd
  Stored in directory: /home/k3sserver/.cache/pip/wheels/3d/22/08/7042eb6309c650c7b53615d5df5cc61f1ea9680e7edd3a08d2
  Building wheel for pandocfilters (setup.py) ... done
  Created wheel for pandocfilters: filename=pandocfilters-1.4.3-py3-none-any.whl size=7991 sha256=f3c9262bce975711135c7fc37738153be6c980ce4db18c10bf27c107ea0d8131
  Stored in directory: /home/k3sserver/.cache/pip/wheels/fc/39/52/8d6f3cec1cca4ceb44d658427c35711b19d89dbc4914af657f
Successfully built keras-tuner terminaltables crcmod avro-python3 hdfs dill google-apitools wrapt termcolor docopt grpc-google-iam-v1 proto-plus promise pyrsistent pandocfilters
ERROR: tensorflow 2.3.2 has requirement numpy<1.19.0,>=1.16.0, but you'll have numpy 1.19.5 which is incompatible.
ERROR: apache-beam 2.25.0 has requirement requests<3.0.0,>=2.24.0, but you'll have requests 2.22.0 which is incompatible.
ERROR: google-api-python-client 1.12.8 has requirement httplib2<1dev,>=0.15.0, but you'll have httplib2 0.14.0 which is incompatible.
Installing collected packages: protobuf, numpy, pyarrow, googleapis-common-protos, absl-py, tensorflow-metadata, pyparsing, pydot, google-pasta, h5py, tensorflow-estimator, wrapt, grpcio, astunparse, termcolor, tensorboard-plugin-wit, requests-oauthlib, cachetools, pyasn1, pyasn1-modules, rsa, google-auth, google-auth-oauthlib, markdown, werkzeug, tensorboard, opt-einsum, keras-preprocessing, gast, tensorflow, crcmod, oauth2client, fastavro, avro-python3, python-dateutil, typing-extensions, pymongo, docopt, hdfs, dill, pbr, mock, google-api-core, google-cloud-core, grpc-google-iam-v1, google-cloud-spanner, google-cloud-language, google-cloud-pubsub, google-cloud-bigtable, google-cloud-videointelligence, google-cloud-datastore, grpcio-gcp, google-cloud-dlp, proto-plus, mypy-extensions, typing-inspect, libcst, google-cloud-build, pycparser, cffi, google-crc32c, google-resumable-media, google-cloud-bigquery, google-apitools, google-cloud-vision, apache-beam, tensorflow-serving-api, uritemplate, google-auth-httplib2, google-api-python-client, pandas, tfx-bsl, tensorflow-transform, joblib, tensorflow-data-validation, threadpoolctl, scipy, scikit-learn, tabulate, terminaltables, tqdm, keras-tuner, ipython-genutils, traitlets, jupyter-core, pyrsistent, attrs, jsonschema, nbformat, pickleshare, parso, jedi, pygments, wcwidth, prompt-toolkit, backcall, decorator, ipython, tornado, pyzmq, jupyter-client, ipykernel, jupyterlab-widgets, Send2Trash, jinja2, argon2-cffi, async-generator, nest-asyncio, nbclient, defusedxml, jupyterlab-pygments, mistune, webencodings, packaging, bleach, pandocfilters, testpath, nbconvert, prometheus-client, ptyprocess, terminado, notebook, widgetsnbextension, ipywidgets, tensorflow-model-analysis, websocket-client, docker, tensorflow-hub, promise, tensorflow-datasets, google-cloud-storage, tensorflow-cloud, kubernetes, ml-metadata, ml-pipelines-sdk, tfx
  WARNING: The scripts f2py, f2py3 and f2py3.8 are installed in '/home/k3sserver/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script plasma_store is installed in '/home/k3sserver/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The scripts pyrsa-decrypt, pyrsa-encrypt, pyrsa-keygen, pyrsa-priv2pub, pyrsa-sign and pyrsa-verify are installed in '/home/k3sserver/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script google-oauthlib-tool is installed in '/home/k3sserver/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script markdown_py is installed in '/home/k3sserver/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script tensorboard is installed in '/home/k3sserver/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The scripts estimator_ckpt_converter, saved_model_cli, tensorboard, tf_upgrade_v2, tflite_convert, toco and toco_from_protos are installed in '/home/k3sserver/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script fastavro is installed in '/home/k3sserver/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The scripts hdfscli and hdfscli-avro are installed in '/home/k3sserver/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script pbr is installed in '/home/k3sserver/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script gen_client is installed in '/home/k3sserver/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script tabulate is installed in '/home/k3sserver/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script tqdm is installed in '/home/k3sserver/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The scripts jupyter, jupyter-migrate and jupyter-troubleshoot are installed in '/home/k3sserver/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script jsonschema is installed in '/home/k3sserver/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script jupyter-trust is installed in '/home/k3sserver/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script pygmentize is installed in '/home/k3sserver/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The scripts iptest, iptest3, ipython and ipython3 are installed in '/home/k3sserver/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The scripts jupyter-kernel, jupyter-kernelspec and jupyter-run are installed in '/home/k3sserver/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script jupyter-nbconvert is installed in '/home/k3sserver/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The scripts jupyter-bundlerextension, jupyter-nbextension, jupyter-notebook and jupyter-serverextension are installed in '/home/k3sserver/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The scripts make_image_classifier and make_nearest_neighbour_index are installed in '/home/k3sserver/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script tfx is installed in '/home/k3sserver/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed Send2Trash-1.5.0 absl-py-0.10.0 apache-beam-2.25.0 argon2-cffi-20.1.0 astunparse-1.6.3 async-generator-1.10 attrs-20.3.0 avro-python3-1.9.2.1 backcall-0.2.0 bleach-3.2.1 cachetools-4.2.0 cffi-1.14.4 crcmod-1.7 decorator-4.4.2 defusedxml-0.6.0 dill-0.3.1.1 docker-4.4.1 docopt-0.6.2 fastavro-1.2.3 gast-0.3.3 google-api-core-1.24.1 google-api-python-client-1.12.8 google-apitools-0.5.31 google-auth-1.24.0 google-auth-httplib2-0.0.4 google-auth-oauthlib-0.4.2 google-cloud-bigquery-1.28.0 google-cloud-bigtable-1.6.1 google-cloud-build-2.0.0 google-cloud-core-1.5.0 google-cloud-datastore-1.15.3 google-cloud-dlp-1.0.0 google-cloud-language-1.3.0 google-cloud-pubsub-1.7.0 google-cloud-spanner-1.19.1 google-cloud-storage-1.35.0 google-cloud-videointelligence-1.16.1 google-cloud-vision-1.0.0 google-crc32c-1.1.0 google-pasta-0.2.0 google-resumable-media-1.2.0 googleapis-common-protos-1.52.0 grpc-google-iam-v1-0.12.3 grpcio-1.34.0 grpcio-gcp-0.2.2 h5py-2.10.0 hdfs-2.5.8 ipykernel-5.4.2 ipython-7.19.0 ipython-genutils-0.2.0 ipywidgets-7.6.3 jedi-0.18.0 jinja2-2.11.2 joblib-0.14.1 jsonschema-3.2.0 jupyter-client-6.1.7 jupyter-core-4.7.0 jupyterlab-pygments-0.1.2 jupyterlab-widgets-1.0.0 keras-preprocessing-1.1.2 keras-tuner-1.0.1 kubernetes-11.0.0 libcst-0.3.16 markdown-3.3.3 mistune-0.8.4 ml-metadata-0.26.0 ml-pipelines-sdk-0.26.0 mock-2.0.0 mypy-extensions-0.4.3 nbclient-0.5.1 nbconvert-6.0.7 nbformat-5.0.8 nest-asyncio-1.4.3 notebook-6.1.6 numpy-1.19.5 oauth2client-4.1.3 opt-einsum-3.3.0 packaging-20.8 pandas-1.2.0 pandocfilters-1.4.3 parso-0.8.1 pbr-5.5.1 pickleshare-0.7.5 prometheus-client-0.9.0 promise-2.3 prompt-toolkit-3.0.9 proto-plus-1.13.0 protobuf-3.14.0 ptyprocess-0.7.0 pyarrow-0.17.1 pyasn1-0.4.8 pyasn1-modules-0.2.8 pycparser-2.20 pydot-1.4.1 pygments-2.7.3 pymongo-3.11.2 pyparsing-2.4.7 pyrsistent-0.17.3 python-dateutil-2.8.1 pyzmq-20.0.0 requests-oauthlib-1.3.0 rsa-4.6 scikit-learn-0.24.0 scipy-1.6.0 tabulate-0.8.7 tensorboard-2.4.0 tensorboard-plugin-wit-1.7.0 tensorflow-2.3.2 tensorflow-cloud-0.1.11 tensorflow-data-validation-0.26.0 tensorflow-datasets-3.0.0 tensorflow-estimator-2.3.0 tensorflow-hub-0.9.0 tensorflow-metadata-0.26.0 tensorflow-model-analysis-0.26.0 tensorflow-serving-api-2.3.0 tensorflow-transform-0.26.0 termcolor-1.1.0 terminado-0.9.2 terminaltables-3.1.0 testpath-0.4.4 tfx-0.26.0 tfx-bsl-0.26.1 threadpoolctl-2.1.0 tornado-6.1 tqdm-4.55.1 traitlets-5.0.5 typing-extensions-3.7.4.3 typing-inspect-0.6.0 uritemplate-3.0.1 wcwidth-0.2.5 webencodings-0.5.1 websocket-client-0.57.0 werkzeug-1.0.1 widgetsnbextension-3.5.1 wrapt-1.12.1
$ 
```

