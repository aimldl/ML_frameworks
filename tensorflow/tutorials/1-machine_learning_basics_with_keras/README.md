* Draft: 2021-05-27 (Thu)
# github.com/aimldl/tensorflow/tutorials/1-beginner/1-machine_learning_basics_with_keras

## 1-basic_image_classification-fashion_mnist_mlp-edited
### Run the code
```bash
$ cd py_files/
$ python 1-basic_image_classification-fashion_mnist_mlp-edited.py 
```
Refer to the full output message at [Appendix. Full Output Messages](APPENDIX.md).

### Check the GPU utilization.
Open another terminal and observe the GPU utilization.
```bash
$ watch -n 1 nvidia-smi
```
#### Before
<img src='images/tensorflow_tutorials-nvidia_-n_1_nvidia-smi_python_1-basic_image_classification-fashion_mnist_mlp-edited_py.png'>

#### After: at 10/10 epoch
<img src='images/tensorflow_tutorials-nvidia_-n_1_nvidia-smi_python_1-basic_image_classification-fashion_mnist_mlp-edited_py-10_10.png'>

### Memo
The maximu GPU utilization is 9% on my Amazon EC2 instance with NVIDIA V100 GPU.

<img src='images/tensorflow_tutorials-nvidia_-n_1_nvidia-smi_python_1-basic_image_classification-fashion_mnist_mlp-edited_py-max_gpu_util.png'>

## 2-basic_text_classification-imdb_embedding_mlp
### Run the code
```bash
$ cd py_files/
$ python 2-basic_text_classification-imdb_embedding_mlp-edited.py
```
Refer to the full output message at [Appendix. Full Output Messages](APPENDIX.md).

### Check the GPU utilization.
Open another terminal and observe the GPU utilization.
```bash
$ watch -n 1 nvidia-smi
```
#### Before
<img src='images/tensorflow_tutorials-nvidia_-n_1_nvidia-smi_python_2-basic_text_classification-imdb_embedding_mlp_py.png'>

#### After: at 10/10 epoch
<img src='images/tensorflow_tutorials-nvidia_-n_1_nvidia-smi_python_2-basic_text_classification-imdb_embedding_mlp_py-10_10.png'>

#### Memo
When GPU is used, the output should look like this. On NVIDIA V-100, the GPU utilization is less than 10%.
<src img='images/python_2-2-basic_text_classification-imdb_embedding_mlp-edited_py-watch_-n_1_nvidia-smi.gif'>


