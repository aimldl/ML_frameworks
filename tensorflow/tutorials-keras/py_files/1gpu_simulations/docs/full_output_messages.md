* Draft: 2021-05-28 (Fri)

# Full Ouput Messages

## 2_mnist-mlp-keras.py 

```bash
$ python 2_mnist-mlp-keras.py
<class 'numpy.ndarray'> <class 'numpy.ndarray'> <class 'numpy.ndarray'> <class 'numpy.ndarray'>
(60000, 28, 28) (60000,) (10000, 28, 28) (10000,)
60000 10000
Epoch 1/20
192/192 [==============================] - 3s 5ms/step - loss: 9.7234 - accuracy: 0.6130 - val_loss: 0.6511 - val_accuracy: 0.8380
Epoch 2/20
192/192 [==============================] - 1s 3ms/step - loss: 0.5525 - accuracy: 0.8496 - val_loss: 0.4655 - val_accuracy: 0.8772
Epoch 3/20
192/192 [==============================] - 1s 3ms/step - loss: 0.3622 - accuracy: 0.8943 - val_loss: 0.3896 - val_accuracy: 0.9049
Epoch 4/20
192/192 [==============================] - 1s 3ms/step - loss: 0.2774 - accuracy: 0.9207 - val_loss: 0.3637 - val_accuracy: 0.9227
Epoch 5/20
192/192 [==============================] - 1s 3ms/step - loss: 0.2461 - accuracy: 0.9335 - val_loss: 0.3662 - val_accuracy: 0.9269
Epoch 6/20
192/192 [==============================] - 1s 3ms/step - loss: 0.2025 - accuracy: 0.9422 - val_loss: 0.3451 - val_accuracy: 0.9322
Epoch 7/20
192/192 [==============================] - 1s 3ms/step - loss: 0.1868 - accuracy: 0.9484 - val_loss: 0.3145 - val_accuracy: 0.9335
Epoch 8/20
192/192 [==============================] - 1s 3ms/step - loss: 0.1569 - accuracy: 0.9545 - val_loss: 0.3006 - val_accuracy: 0.9463
Epoch 9/20
192/192 [==============================] - 1s 3ms/step - loss: 0.1379 - accuracy: 0.9608 - val_loss: 0.3051 - val_accuracy: 0.9465
Epoch 10/20
192/192 [==============================] - 1s 3ms/step - loss: 0.1324 - accuracy: 0.9638 - val_loss: 0.2809 - val_accuracy: 0.9496
Epoch 11/20
192/192 [==============================] - 1s 3ms/step - loss: 0.1078 - accuracy: 0.9678 - val_loss: 0.3028 - val_accuracy: 0.9481
Epoch 12/20
192/192 [==============================] - 1s 3ms/step - loss: 0.1114 - accuracy: 0.9680 - val_loss: 0.2476 - val_accuracy: 0.9512
Epoch 13/20
192/192 [==============================] - 1s 3ms/step - loss: 0.0904 - accuracy: 0.9732 - val_loss: 0.3008 - val_accuracy: 0.9563
Epoch 14/20
192/192 [==============================] - 1s 3ms/step - loss: 0.0867 - accuracy: 0.9756 - val_loss: 0.2681 - val_accuracy: 0.9499
Epoch 15/20
192/192 [==============================] - 1s 3ms/step - loss: 0.0944 - accuracy: 0.9731 - val_loss: 0.2411 - val_accuracy: 0.9578
Epoch 16/20
192/192 [==============================] - 1s 3ms/step - loss: 0.0803 - accuracy: 0.9771 - val_loss: 0.3033 - val_accuracy: 0.9544
Epoch 17/20
192/192 [==============================] - 1s 3ms/step - loss: 0.0853 - accuracy: 0.9769 - val_loss: 0.2876 - val_accuracy: 0.9557
Epoch 18/20
192/192 [==============================] - 1s 3ms/step - loss: 0.0800 - accuracy: 0.9771 - val_loss: 0.2590 - val_accuracy: 0.9581
Epoch 19/20
192/192 [==============================] - 1s 3ms/step - loss: 0.0658 - accuracy: 0.9805 - val_loss: 0.2990 - val_accuracy: 0.9603
Epoch 20/20
192/192 [==============================] - 1s 3ms/step - loss: 0.0675 - accuracy: 0.9820 - val_loss: 0.2327 - val_accuracy: 0.9582
313/313 [==============================] - 1s 2ms/step - loss: 0.2544 - accuracy: 0.9602
Test results: Loss = 0.2544148564338684, Accuracy = 0.9602000117301941
$
```

## 2_mnist-simple-cnn-keras.py

```bash
$ python 2_mnist-simple-cnn-keras.py
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d (Conv2D)              (None, 26, 26, 32)        320       
_________________________________________________________________
max_pooling2d (MaxPooling2D) (None, 13, 13, 32)        0         
_________________________________________________________________
conv2d_1 (Conv2D)            (None, 11, 11, 64)        18496     
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 5, 5, 64)          0         
_________________________________________________________________
flatten (Flatten)            (None, 1600)              0         
_________________________________________________________________
dropout (Dropout)            (None, 1600)              0         
_________________________________________________________________
dense (Dense)                (None, 10)                16010     
=================================================================
Total params: 34,826
Trainable params: 34,826
Non-trainable params: 0
_________________________________________________________________
Epoch 1/20
1500/1500 [==============================] - 14s 4ms/step - loss: 0.5026 - accuracy: 0.8442 - val_loss: 0.0715 - val_accuracy: 0.9807
Epoch 2/20
1500/1500 [==============================] - 5s 3ms/step - loss: 0.0925 - accuracy: 0.9711 - val_loss: 0.0529 - val_accuracy: 0.9858
Epoch 3/20
1500/1500 [==============================] - 5s 3ms/step - loss: 0.0700 - accuracy: 0.9773 - val_loss: 0.0457 - val_accuracy: 0.9872
Epoch 4/20
1500/1500 [==============================] - 5s 3ms/step - loss: 0.0604 - accuracy: 0.9824 - val_loss: 0.0423 - val_accuracy: 0.9878
Epoch 5/20
1500/1500 [==============================] - 5s 3ms/step - loss: 0.0526 - accuracy: 0.9825 - val_loss: 0.0460 - val_accuracy: 0.9875
Epoch 6/20
1500/1500 [==============================] - 5s 4ms/step - loss: 0.0430 - accuracy: 0.9860 - val_loss: 0.0372 - val_accuracy: 0.9898
Epoch 7/20
1500/1500 [==============================] - 5s 4ms/step - loss: 0.0378 - accuracy: 0.9871 - val_loss: 0.0375 - val_accuracy: 0.9895
Epoch 8/20
1500/1500 [==============================] - 5s 3ms/step - loss: 0.0383 - accuracy: 0.9873 - val_loss: 0.0344 - val_accuracy: 0.9903
Epoch 9/20
1500/1500 [==============================] - 5s 3ms/step - loss: 0.0393 - accuracy: 0.9875 - val_loss: 0.0337 - val_accuracy: 0.9904
Epoch 10/20
1500/1500 [==============================] - 5s 4ms/step - loss: 0.0309 - accuracy: 0.9897 - val_loss: 0.0319 - val_accuracy: 0.9913
Epoch 11/20
1500/1500 [==============================] - 5s 3ms/step - loss: 0.0325 - accuracy: 0.9894 - val_loss: 0.0328 - val_accuracy: 0.9911
Epoch 12/20
1500/1500 [==============================] - 5s 3ms/step - loss: 0.0289 - accuracy: 0.9906 - val_loss: 0.0314 - val_accuracy: 0.9912
Epoch 13/20
1500/1500 [==============================] - 5s 4ms/step - loss: 0.0295 - accuracy: 0.9903 - val_loss: 0.0322 - val_accuracy: 0.9911
Epoch 14/20
1500/1500 [==============================] - 5s 4ms/step - loss: 0.0270 - accuracy: 0.9913 - val_loss: 0.0323 - val_accuracy: 0.9911
Epoch 15/20
1500/1500 [==============================] - 5s 3ms/step - loss: 0.0267 - accuracy: 0.9914 - val_loss: 0.0340 - val_accuracy: 0.9904
Epoch 16/20
1500/1500 [==============================] - 5s 3ms/step - loss: 0.0259 - accuracy: 0.9917 - val_loss: 0.0319 - val_accuracy: 0.9909
Epoch 17/20
1500/1500 [==============================] - 5s 4ms/step - loss: 0.0231 - accuracy: 0.9923 - val_loss: 0.0306 - val_accuracy: 0.9918
Epoch 18/20
1500/1500 [==============================] - 5s 4ms/step - loss: 0.0227 - accuracy: 0.9925 - val_loss: 0.0326 - val_accuracy: 0.9918
Epoch 19/20
1500/1500 [==============================] - 5s 3ms/step - loss: 0.0210 - accuracy: 0.9929 - val_loss: 0.0306 - val_accuracy: 0.9916
Epoch 20/20
1500/1500 [==============================] - 5s 4ms/step - loss: 0.0213 - accuracy: 0.9932 - val_loss: 0.0306 - val_accuracy: 0.9926
313/313 [==============================] - 1s 3ms/step - loss: 0.0238 - accuracy: 0.9935
$
```

## 3_mnist-cnn-keras.py

```bash
$ python 3_mnist-cnn-keras.py 
<class 'numpy.ndarray'> <class 'numpy.ndarray'> <class 'numpy.ndarray'> <class 'numpy.ndarray'>
x_train shape: (60000, 28, 28, 1)
60000 train samples
10000 test samples
<class 'numpy.ndarray'> <class 'numpy.ndarray'>
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d (Conv2D)              (None, 26, 26, 32)        320       
_________________________________________________________________
max_pooling2d (MaxPooling2D) (None, 13, 13, 32)        0         
_________________________________________________________________
conv2d_1 (Conv2D)            (None, 11, 11, 64)        18496     
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 5, 5, 64)          0         
_________________________________________________________________
flatten (Flatten)            (None, 1600)              0         
_________________________________________________________________
dropout (Dropout)            (None, 1600)              0         
_________________________________________________________________
dense (Dense)                (None, 10)                16010     
=================================================================
Total params: 34,826
Trainable params: 34,826
Non-trainable params: 0
_________________________________________________________________
Epoch 1/15
422/422 [==============================] - 5s 6ms/step - loss: 0.7644 - accuracy: 0.7642 - val_loss: 0.0810 - val_accuracy: 0.9778
Epoch 2/15
422/422 [==============================] - 2s 4ms/step - loss: 0.1222 - accuracy: 0.9634 - val_loss: 0.0548 - val_accuracy: 0.9862
Epoch 3/15
422/422 [==============================] - 2s 4ms/step - loss: 0.0908 - accuracy: 0.9720 - val_loss: 0.0468 - val_accuracy: 0.9877
Epoch 4/15
422/422 [==============================] - 2s 4ms/step - loss: 0.0700 - accuracy: 0.9785 - val_loss: 0.0405 - val_accuracy: 0.9895
Epoch 5/15
422/422 [==============================] - 2s 4ms/step - loss: 0.0630 - accuracy: 0.9803 - val_loss: 0.0391 - val_accuracy: 0.9893
Epoch 6/15
422/422 [==============================] - 2s 4ms/step - loss: 0.0549 - accuracy: 0.9829 - val_loss: 0.0349 - val_accuracy: 0.9905
Epoch 7/15
422/422 [==============================] - 2s 4ms/step - loss: 0.0514 - accuracy: 0.9843 - val_loss: 0.0345 - val_accuracy: 0.9908
Epoch 8/15
422/422 [==============================] - 2s 4ms/step - loss: 0.0508 - accuracy: 0.9832 - val_loss: 0.0304 - val_accuracy: 0.9913
Epoch 9/15
422/422 [==============================] - 2s 4ms/step - loss: 0.0426 - accuracy: 0.9858 - val_loss: 0.0310 - val_accuracy: 0.9912
Epoch 10/15
422/422 [==============================] - 2s 4ms/step - loss: 0.0439 - accuracy: 0.9871 - val_loss: 0.0291 - val_accuracy: 0.9918
Epoch 11/15
422/422 [==============================] - 2s 4ms/step - loss: 0.0404 - accuracy: 0.9877 - val_loss: 0.0294 - val_accuracy: 0.9912
Epoch 12/15
422/422 [==============================] - 2s 4ms/step - loss: 0.0378 - accuracy: 0.9875 - val_loss: 0.0275 - val_accuracy: 0.9930
Epoch 13/15
422/422 [==============================] - 2s 4ms/step - loss: 0.0373 - accuracy: 0.9879 - val_loss: 0.0288 - val_accuracy: 0.9922
Epoch 14/15
422/422 [==============================] - 2s 4ms/step - loss: 0.0343 - accuracy: 0.9887 - val_loss: 0.0298 - val_accuracy: 0.9913
Epoch 15/15
422/422 [==============================] - 2s 4ms/step - loss: 0.0310 - accuracy: 0.9900 - val_loss: 0.0257 - val_accuracy: 0.9920
Test loss: 0.02494184300303459
Test accuracy: 0.9908999800682068
$
```

## 4_fashion_mnist-cnn-keras.py

```bash
$ python 4_fashion_mnist-cnn-keras.py
<class 'numpy.ndarray'> <class 'numpy.ndarray'> <class 'numpy.ndarray'> <class 'numpy.ndarray'>
x_train shape: (60000, 28, 28, 1)
60000 train samples
10000 test samples
<class 'numpy.ndarray'> <class 'numpy.ndarray'>
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d (Conv2D)              (None, 26, 26, 32)        320       
_________________________________________________________________
max_pooling2d (MaxPooling2D) (None, 13, 13, 32)        0         
_________________________________________________________________
conv2d_1 (Conv2D)            (None, 11, 11, 64)        18496     
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 5, 5, 64)          0         
_________________________________________________________________
flatten (Flatten)            (None, 1600)              0         
_________________________________________________________________
dropout (Dropout)            (None, 1600)              0         
_________________________________________________________________
dense (Dense)                (None, 10)                16010     
=================================================================
Total params: 34,826
Trainable params: 34,826
Non-trainable params: 0
_________________________________________________________________
Epoch 1/15
422/422 [==============================] - 5s 6ms/step - loss: 1.0113 - accuracy: 0.6445 - val_loss: 0.4508 - val_accuracy: 0.8335
Epoch 2/15
422/422 [==============================] - 2s 4ms/step - loss: 0.4793 - accuracy: 0.8274 - val_loss: 0.3960 - val_accuracy: 0.8550
Epoch 3/15
422/422 [==============================] - 2s 4ms/step - loss: 0.4170 - accuracy: 0.8508 - val_loss: 0.3627 - val_accuracy: 0.8702
Epoch 4/15
422/422 [==============================] - 2s 4ms/step - loss: 0.3822 - accuracy: 0.8629 - val_loss: 0.3409 - val_accuracy: 0.8772
Epoch 5/15
422/422 [==============================] - 2s 4ms/step - loss: 0.3582 - accuracy: 0.8707 - val_loss: 0.3173 - val_accuracy: 0.8853
Epoch 6/15
422/422 [==============================] - 2s 4ms/step - loss: 0.3359 - accuracy: 0.8783 - val_loss: 0.3152 - val_accuracy: 0.8838
Epoch 7/15
422/422 [==============================] - 2s 4ms/step - loss: 0.3263 - accuracy: 0.8822 - val_loss: 0.2927 - val_accuracy: 0.8940
Epoch 8/15
422/422 [==============================] - 2s 4ms/step - loss: 0.3132 - accuracy: 0.8858 - val_loss: 0.2829 - val_accuracy: 0.8970
Epoch 9/15
422/422 [==============================] - 2s 4ms/step - loss: 0.3059 - accuracy: 0.8889 - val_loss: 0.2770 - val_accuracy: 0.8960
Epoch 10/15
422/422 [==============================] - 2s 4ms/step - loss: 0.3023 - accuracy: 0.8917 - val_loss: 0.2730 - val_accuracy: 0.9012
Epoch 11/15
422/422 [==============================] - 2s 4ms/step - loss: 0.2885 - accuracy: 0.8953 - val_loss: 0.2679 - val_accuracy: 0.9033
Epoch 12/15
422/422 [==============================] - 2s 4ms/step - loss: 0.2830 - accuracy: 0.8962 - val_loss: 0.2654 - val_accuracy: 0.9040
Epoch 13/15
422/422 [==============================] - 2s 4ms/step - loss: 0.2805 - accuracy: 0.8983 - val_loss: 0.2569 - val_accuracy: 0.9062
Epoch 14/15
422/422 [==============================] - 2s 4ms/step - loss: 0.2733 - accuracy: 0.9013 - val_loss: 0.2589 - val_accuracy: 0.9053
Epoch 15/15
422/422 [==============================] - 2s 4ms/step - loss: 0.2681 - accuracy: 0.9021 - val_loss: 0.2548 - val_accuracy: 0.9073
Test loss: 0.2675645053386688
Test accuracy: 0.9018999934196472
$
```

## 5_cifar10-cnn-keras.py

```bash
$ python 5_cifar10-cnn-keras-tf2.py 
/home/ubuntu/anaconda3/envs/tensorflow2_latest_p37/lib/python3.7/site-packages/seaborn/_decorators.py:43: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.
  FutureWarning
x_train shape: (50000, 32, 32, 3)
50000 train samples
10000 test samples
<class 'numpy.ndarray'> <class 'numpy.ndarray'>
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d (Conv2D)              (None, 32, 32, 32)        896       
_________________________________________________________________
max_pooling2d (MaxPooling2D) (None, 16, 16, 32)        0         
_________________________________________________________________
conv2d_1 (Conv2D)            (None, 16, 16, 64)        18496     
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 8, 8, 64)          0         
_________________________________________________________________
flatten (Flatten)            (None, 4096)              0         
_________________________________________________________________
dense (Dense)                (None, 512)               2097664   
_________________________________________________________________
dropout (Dropout)            (None, 512)               0         
_________________________________________________________________
dense_1 (Dense)              (None, 10)                5130      
=================================================================
Total params: 2,122,186
Trainable params: 2,122,186
Non-trainable params: 0
_________________________________________________________________
Epoch 1/15
352/352 [==============================] - 5s 6ms/step - loss: 1.7824 - accuracy: 0.3481 - val_loss: 1.2086 - val_accuracy: 0.5812
Epoch 2/15
352/352 [==============================] - 1s 4ms/step - loss: 1.2261 - accuracy: 0.5674 - val_loss: 1.0241 - val_accuracy: 0.6506
Epoch 3/15
352/352 [==============================] - 1s 4ms/step - loss: 1.0411 - accuracy: 0.6324 - val_loss: 0.9207 - val_accuracy: 0.6796
Epoch 4/15
352/352 [==============================] - 1s 4ms/step - loss: 0.9323 - accuracy: 0.6736 - val_loss: 0.8560 - val_accuracy: 0.7048
Epoch 5/15
352/352 [==============================] - 1s 4ms/step - loss: 0.8423 - accuracy: 0.7060 - val_loss: 0.8104 - val_accuracy: 0.7194
Epoch 6/15
352/352 [==============================] - 1s 4ms/step - loss: 0.7749 - accuracy: 0.7271 - val_loss: 0.7955 - val_accuracy: 0.7242
Epoch 7/15
352/352 [==============================] - 1s 4ms/step - loss: 0.7005 - accuracy: 0.7546 - val_loss: 0.7756 - val_accuracy: 0.7398
Epoch 8/15
352/352 [==============================] - 1s 4ms/step - loss: 0.6589 - accuracy: 0.7695 - val_loss: 0.7829 - val_accuracy: 0.7350
Epoch 9/15
352/352 [==============================] - 1s 4ms/step - loss: 0.5899 - accuracy: 0.7924 - val_loss: 0.7717 - val_accuracy: 0.7438
Epoch 10/15
352/352 [==============================] - 1s 4ms/step - loss: 0.5340 - accuracy: 0.8096 - val_loss: 0.7506 - val_accuracy: 0.7572
Epoch 11/15
352/352 [==============================] - 1s 4ms/step - loss: 0.4777 - accuracy: 0.8309 - val_loss: 0.7787 - val_accuracy: 0.7440
Epoch 12/15
352/352 [==============================] - 1s 4ms/step - loss: 0.4347 - accuracy: 0.8456 - val_loss: 0.7688 - val_accuracy: 0.7538
Epoch 13/15
352/352 [==============================] - 1s 4ms/step - loss: 0.3875 - accuracy: 0.8655 - val_loss: 0.8026 - val_accuracy: 0.7486
Epoch 14/15
352/352 [==============================] - 1s 4ms/step - loss: 0.3556 - accuracy: 0.8755 - val_loss: 0.7966 - val_accuracy: 0.7592
Epoch 15/15
352/352 [==============================] - 1s 4ms/step - loss: 0.3187 - accuracy: 0.8866 - val_loss: 0.8407 - val_accuracy: 0.7482
Test loss: 0.8585140705108643
Test accuracy: 0.7311000227928162
$
```



## 6_imdb_movie_review-bidirectional_lstm-keras.py

```bash
$ python 6_imdb_movie_review-bidirectional_lstm-keras.py 
Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/imdb.npz
17465344/17464789 [==============================] - 1s 0us/step
<string>:6: VisibleDeprecationWarning: Creating an ndarray from ragged nested sequences (which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes) is deprecated. If you meant to do this, you must specify 'dtype=object' when creating the ndarray
/home/ubuntu/anaconda3/envs/tensorflow2_latest_p37/gpu_cuda11.0/lib/python3.7/site-packages/tensorflow/python/keras/datasets/imdb.py:159: VisibleDeprecationWarning: Creating an ndarray from ragged nested sequences (which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes) is deprecated. If you meant to do this, you must specify 'dtype=object' when creating the ndarray
  x_train, y_train = np.array(xs[:idx]), np.array(labels[:idx])
/home/ubuntu/anaconda3/envs/tensorflow2_latest_p37/gpu_cuda11.0/lib/python3.7/site-packages/tensorflow/python/keras/datasets/imdb.py:160: VisibleDeprecationWarning: Creating an ndarray from ragged nested sequences (which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes) is deprecated. If you meant to do this, you must specify 'dtype=object' when creating the ndarray
  x_test, y_test = np.array(xs[idx:]), np.array(labels[idx:])
25000 training sequences
25000 validation sequences
Model: "model"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
input_1 (InputLayer)         [(None, None)]            0         
_________________________________________________________________
embedding (Embedding)        (None, None, 128)         2560000   
_________________________________________________________________
bidirectional (Bidirectional (None, None, 128)         98816     
_________________________________________________________________
bidirectional_1 (Bidirection (None, 128)               98816     
_________________________________________________________________
dense (Dense)                (None, 1)                 129       
=================================================================
Total params: 2,757,761
Trainable params: 2,757,761
Non-trainable params: 0
_________________________________________________________________
Epoch 1/5
782/782 [==============================] - 59s 65ms/step - loss: 0.4618 - accuracy: 0.7659 - val_loss: 0.3004 - val_accuracy: 0.8741
Epoch 2/5
782/782 [==============================] - 50s 63ms/step - loss: 0.1952 - accuracy: 0.9285 - val_loss: 0.3439 - val_accuracy: 0.8660
Epoch 3/5
782/782 [==============================] - 49s 63ms/step - loss: 0.1096 - accuracy: 0.9626 - val_loss: 0.3725 - val_accuracy: 0.8557
Epoch 4/5
782/782 [==============================] - 50s 63ms/step - loss: 0.0945 - accuracy: 0.9676 - val_loss: 0.4481 - val_accuracy: 0.8473
Epoch 5/5
782/782 [==============================] - 50s 63ms/step - loss: 0.1025 - accuracy: 0.9644 - val_loss: 0.4230 - val_accuracy: 0.8402
$
```

## 7_reuters_newswire-mlp-keras-tf2.py

```bash
$ python 7_reuters_newswire-mlp-keras-tf2.py 
Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/reuters.npz
2113536/2110848 [==============================] - 0s 0us/step
/home/ubuntu/anaconda3/envs/tensorflow2_latest_p37/gpu_cuda11.0/lib/python3.7/site-packages/tensorflow/python/keras/datasets/reuters.py:148: VisibleDeprecationWarning: Creating an ndarray from ragged nested sequences (which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes) is deprecated. If you meant to do this, you must specify 'dtype=object' when creating the ndarray
  x_train, y_train = np.array(xs[:idx]), np.array(labels[:idx])
/home/ubuntu/anaconda3/envs/tensorflow2_latest_p37/gpu_cuda11.0/lib/python3.7/site-packages/tensorflow/python/keras/datasets/reuters.py:149: VisibleDeprecationWarning: Creating an ndarray from ragged nested sequences (which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes) is deprecated. If you meant to do this, you must specify 'dtype=object' when creating the ndarray
  x_test, y_test = np.array(xs[idx:]), np.array(labels[idx:])
8982 training samples
2246 test samples
11228 total samples
8982 training labels, 2246 test labels
Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/reuters_word_index.json
557056/550378 [==============================] - 0s 0us/step
? period ended december 31 shr profit 11 cts vs loss 24 cts net profit 224 271 vs loss 511 349 revs 7 258 688 vs 7 200 349 reuter 3
x_train (8982, 10000)
x_test  (2246, 10000)
y_train_dummy (8982, 46)
y_test_dummy  (2246, 46)
3 [0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
4 [0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
y_train (8982, 46)
y_test  (2246, 46)
3 [0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
4 [0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
x_val  (1000, 10000)
y_val  (1000, 46)
partial_x_train  (7982, 10000)
partial_y_train  (7982, 46)
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense (Dense)                (None, 64)                640064    
_________________________________________________________________
dense_1 (Dense)              (None, 64)                4160      
_________________________________________________________________
dense_2 (Dense)              (None, 46)                2990      
=================================================================
Total params: 647,214
Trainable params: 647,214
Non-trainable params: 0
_________________________________________________________________
Epoch 1/10
16/16 [==============================] - 2s 37ms/step - loss: 3.1934 - accuracy: 0.3493 - val_loss: 1.7706 - val_accuracy: 0.6320
Epoch 2/10
16/16 [==============================] - 0s 9ms/step - loss: 1.5242 - accuracy: 0.6919 - val_loss: 1.3115 - val_accuracy: 0.7170
Epoch 3/10
16/16 [==============================] - 0s 16ms/step - loss: 1.0906 - accuracy: 0.7730 - val_loss: 1.1584 - val_accuracy: 0.7530
Epoch 4/10
16/16 [==============================] - 0s 9ms/step - loss: 0.8628 - accuracy: 0.8149 - val_loss: 1.0400 - val_accuracy: 0.7830
Epoch 5/10
16/16 [==============================] - 0s 9ms/step - loss: 0.6769 - accuracy: 0.8638 - val_loss: 0.9623 - val_accuracy: 0.8010
Epoch 6/10
16/16 [==============================] - 0s 9ms/step - loss: 0.5628 - accuracy: 0.8839 - val_loss: 0.9299 - val_accuracy: 0.8070
Epoch 7/10
16/16 [==============================] - 0s 9ms/step - loss: 0.4458 - accuracy: 0.9077 - val_loss: 0.9085 - val_accuracy: 0.8090
Epoch 8/10
16/16 [==============================] - 0s 9ms/step - loss: 0.3568 - accuracy: 0.9250 - val_loss: 0.9140 - val_accuracy: 0.8180
Epoch 9/10
16/16 [==============================] - 0s 8ms/step - loss: 0.2895 - accuracy: 0.9360 - val_loss: 0.9055 - val_accuracy: 0.8190
Epoch 10/10
16/16 [==============================] - 0s 9ms/step - loss: 0.2477 - accuracy: 0.9447 - val_loss: 0.9418 - val_accuracy: 0.8080
$
```

