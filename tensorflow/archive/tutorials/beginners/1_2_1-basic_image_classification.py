#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
##### aimldl >python3 > packages > tensorflow > tutorials > beginners > 1_2_1-basic_image_classification.py

* This notebook is a replica of [Basic classification: Classify images of clothing](https://www.tensorflow.org/tutorials/keras/classification) with some comments.
  * [TensorFlow](https://www.tensorflow.org/) > [Learn](https://www.tensorflow.org/learn) > [TensorFlow Core](https://www.tensorflow.org/overview) > [Tutorials](https://www.tensorflow.org/tutorials) > ML basics with Keras > [Basic image classification](https://www.tensorflow.org/tutorials/keras/classification)
* It is prerequisite to install TensorFlow 2.0.
'''

from __future__ import absolute_import, division, print_function, unicode_literals

#--------------------------------------------------------------------#
def plot_image2(i, predictions_array, true_label, img):
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])

  plt.imshow(img, cmap=plt.cm.binary)

  predicted_label = np.argmax(predictions_array)
  if predicted_label == true_label:
    color = 'blue'
  else:
    color = 'red'

  plt.xlabel("Predicted {:2.0f}% {}".format( 100*np.max(predictions_array),
                                   class_names[predicted_label]),
                                   color=color )
  plt.title( "{}th input: {}".format(i, class_names[true_label]) )
  
def plot_value_array2( predictions_array, true_label, use_class_names=False ):
  plt.grid(False)
  if use_class_names:
    _ = plt.xticks(range(10), class_names, rotation=90)
  else:
    plt.xticks(range(10))
  #plt.yticks([])
  thisplot = plt.bar(range(10), predictions_array, color="#777777")
  plt.ylim([0, 1])
  predicted_label = np.argmax(predictions_array)
  plt.title( "Probability" )

  thisplot[predicted_label].set_color('red')
  thisplot[true_label].set_color('blue')
  
def show_prediction( i ):
  plt.figure(figsize=(6,3))
  plt.subplot(1,2,1)
  plot_image2(i, predictions[i], test_labels[i], test_images[i])
  plt.subplot(1,2,2)
  plot_value_array2(predictions[i], test_labels[i])
  plt.show() 
#--------------------------------------------------------------------#

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.image as img

print(tf.__version__)

# Import the Fashion MNIST dataset
fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

train_images = train_images / 255.0
test_images = test_images / 255.0

# Build the model
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])
    

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])


# Train the model
model.fit(train_images, train_labels, epochs=10)

# Evaluate accuracy
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
print('\nTest accuracy:', test_acc)

#--------------------#
#  Make predictions  #
#--------------------#

# of a single image
i = 1
img = test_images[i]

# Add the image to a batch where it's the only member.
img = (np.expand_dims(img,0))
print(img.shape)

predictions_single = model.predict(img)
print(predictions_single)
np.argmax(predictions_single[0])
plot_value_array2( predictions_single[0], test_labels[i] )
plot_value_array2( predictions_single[0], test_labels[i], use_class_names=True )

# of the entire test images
predictions = model.predict(test_images) 
show_prediction( 0 )
show_prediction( 12 )

# Multiple images
num_rows = 5
num_cols = 3
num_images = num_rows*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
for i in range(num_images):
  plt.subplot(num_rows, 2*num_cols, 2*i+1)
  plot_image2(i, predictions[i], test_labels[i], test_images[i])
  plt.subplot(num_rows, 2*num_cols, 2*i+2)
  plot_value_array2(predictions[i], test_labels[i])
plt.tight_layout()
plt.show()