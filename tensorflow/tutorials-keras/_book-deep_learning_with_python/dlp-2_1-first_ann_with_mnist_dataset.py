# dlp-2_1-first_ann_with_mnist_dataset.py
# Deep Learning with Pytnon
# 케라스 창시자에게 배우는 딥러닝
# 2.1. 신경망과의 첫 만남

>>> from keras.datasets import mnist
Using TensorFlow backend.
>>> (train_images, train_labels), (test_images, test_labels) = mnist.load_data()
Downloading data from https://s3.amazonaws.com/img-datasets/mnist.npz
11493376/11490434 [==============================] - 10s 1us/step
>>> train_images.shape
(60000, 28, 28)
>>> len(train_labels)
60000
>>> train_labels
array([5, 0, 4, ..., 5, 6, 8], dtype=uint8)
>>> test_images.shape
(10000, 28, 28)
>>> len(test_labels)
10000
>>> test_labels
array([7, 2, 1, ..., 4, 5, 6], dtype=uint8)
>>> from keras import models
>>> from keras import layers
>>>
>>> network = models.Sequential()
WARNING: Logging before flag parsing goes to stderr.
W0727 05:32:43.815149 13104 deprecation_wrapper.py:119] From C:\Users\aimldl\Anaconda3\envs\keras\lib\site-packages\keras\backend\tensorflow_backend.py:74: The name tf.get_default_graph is deprecated. Please use tf.compat.v1.get_default_graph instead.

>>> network.add( layers.Dense( 512, activation='relu', input_shape=(28*28,) )  )
W0727 05:33:33.433607 13104 deprecation_wrapper.py:119] From C:\Users\aimldl\Anaconda3\envs\keras\lib\site-packages\keras\backend\tensorflow_backend.py:517: The name tf.placeholder is deprecated. Please use tf.compat.v1.placeholder instead.

W0727 05:33:33.612130 13104 deprecation_wrapper.py:119] From C:\Users\aimldl\Anaconda3\envs\keras\lib\site-packages\keras\backend\tensorflow_backend.py:4138: The name tf.random_uniform is deprecated. Please use tf.random.uniform instead.

>>> network.add( layers.Dense(10, activation='softmax') )
>>> network.compile( optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'] )
W0727 05:34:47.570944 13104 deprecation_wrapper.py:119] From C:\Users\aimldl\Anaconda3\envs\keras\lib\site-packages\keras\optimizers.py:790: The name tf.train.Optimizer is deprecated. Please use tf.compat.v1.train.Optimizer instead.

W0727 05:34:47.627791 13104 deprecation_wrapper.py:119] From C:\Users\aimldl\Anaconda3\envs\keras\lib\site-packages\keras\backend\tensorflow_backend.py:3295: The name tf.log is deprecated. Please use tf.math.log instead.

>>> train_images = train_images.reshape( (60000,28*28) )
>>> train_images = train_images.astype('float32')/255
>>> test_images = test_images.reshape( (10000, 28*28) )
>>> test_images = test_images.astype('float32')/255
>>> from keras.utils import to_categorical
>>>
>>> train_labels = to_categorical( train_labels )
>>> test_labels = to_categorical( test_labels )
>>> network.fit( train_images, train_labels, epochs=5, batch_size=128 )
W0727 05:37:57.691185 13104 deprecation.py:323] From C:\Users\aimldl\Anaconda3\envs\keras\lib\site-packages\tensorflow\python\ops\math_grad.py:1250: add_dispatch_support.<locals>.wrapper (from tensorflow.python.ops.array_ops) is deprecated and will be removed in a future version.
Instructions for updating:
Use tf.where in 2.0, which has the same broadcast rule as np.where
W0727 05:37:57.737062 13104 deprecation_wrapper.py:119] From C:\Users\aimldl\Anaconda3\envs\keras\lib\site-packages\keras\backend\tensorflow_backend.py:986: The name tf.assign_add is deprecated. Please use tf.compat.v1.assign_add instead.

Epoch 1/5
2019-07-27 05:37:57.830333: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2
60000/60000 [==============================] - 4s 73us/step - loss: 0.2553 - acc: 0.9263
Epoch 2/5
60000/60000 [==============================] - 3s 54us/step - loss: 0.1044 - acc: 0.9687
Epoch 3/5
60000/60000 [==============================] - 3s 54us/step - loss: 0.0687 - acc: 0.9796
Epoch 4/5
60000/60000 [==============================] - 3s 52us/step - loss: 0.0505 - acc: 0.9844
Epoch 5/5
60000/60000 [==============================] - 3s 54us/step - loss: 0.0378 - acc: 0.9887
<keras.callbacks.History object at 0x000001B1B1568A58>
>>> test_loss, test_acc = network.evaluate( test_images. test_labels )
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'numpy.ndarray' object has no attribute 'test_labels'
>>> test_loss, test_acc = network.evaluate( test_images, test_labels )
10000/10000 [==============================] - 0s 19us/step
>>> print( 'test_loss, test_acc=', test_loss, test_acc)
test_loss, test_acc= 0.06689464278970846 0.9797
>>>
