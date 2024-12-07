$ CUDA_VISIBLE_DEVICES=0 python mnist.py
$ CUDA_VISIBLE_DEVICES=0,1 python mnist.py


$ watch -n 1 "ps -ef | grep python | "



import tensorflor as tf
strategy = tensorflow.distribute.MirroredStrategy()


