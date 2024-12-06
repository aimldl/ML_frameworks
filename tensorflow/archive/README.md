##### aimldl > python3 > packages > tensorflow > README.md

# TensorFlow
TensorFlow is an open source software that provides libraries for numerical computation used for Machine Learning (ML) research. Google released TensorFlow on Nov. 10, 2015 (Mon) and many people use it along with other frameworks such as Caffe, MxNet, CNTK, Chainer, PyTorch, etc. For details, refer to https://www.tensorflow.org/.

It is designed to be used easily. Python is the scripting language that interfaces the core part of the libraries written in C++. A complex ML code can be used with several lines in Python to run experiments while one can write codes in C++ to extend the existing functionalities of TensorFlow.

## Recommended Articles
* [Getting started with TensorFlow 2.0](#https://medium.com/@himanshurawlani/getting-started-with-tensorflow-2-0-faf5428febae)
  * A practitioner’s guide to building and deploying an image classifier in TensorFlow 2.0

## 1. Installing TensorFlow
```bash
$ pip install --upgrade pip
$ pip install tensorflow
$ pip install tensorflow-datasets
$
```
For details, refer to [Install TensorFlow 2](https://www.tensorflow.org/install).

## 2. TensorFlow Datasets
[TensorFlow Datasets](https://www.tensorflow.org/datasets) have
* audio,
* image,
* text, and
* miscellaneous.

The full list of datasets is available at https://www.tensorflow.org/datasets/catalog/overview.

## 3. Tutorials
### 3.1. Official Tutorials
Tutorials are available at https://www.tensorflow.org/tutorials/.
* For beginners
  * [Beginner quickstart](https://www.tensorflow.org/tutorials/quickstart/beginner)
  * Keras basics
  * Load data
* For experts
  * Advanced quickstart
  * Customization
  * Distributed training

### 3.2. IPython Notebooks
Simple example of image classification with the MNIST dataset
* [1_1-beginner_quickstart.ipynb](#tutorials/beginners/1_1-beginner_quickstart.ipynb)
  * This example uses TensorFlow.
  * mnist = tf.keras.datasets.mnist
  
"ML basics with Keras" has a collection of examples from [ML basics with Keras(https://www.tensorflow.org/tutorials/keras/classification).
* [1_2-keras_basics.ipynb](#tutorials/beginners/1_2-keras_basics.ipynb)
  * [Basic classification: Classify images of clothing](), [official](https://www.tensorflow.org/tutorials/keras/classification)
    * This example uses Keras.
    * fashion_mnist = keras.datasets.fashion_mnist
  * [Text classification with TF Hub]()
  * [Text classification with preprocessed text]()
  * [Regression]()
  * [Overfit and underfit]()
  * [Save and load]()

* Load and preprocess data
  * [CSV]()
  * [Numpy]()
  * [pandas.DataFrame]()
  * [Images]()
  * [Text]()
  * [Unicode]()
  * [TF.Text]()
  * [TFRecord and tf.Example]()
  * [Additional formats with tf.io]()
* Estimator
  * [Premade estimator]()
  * [Linear model]()
  * [Boosted trees]()
  * [Boosted trees model understanding]()
  * [Keras model to Estimator]()
  
  
