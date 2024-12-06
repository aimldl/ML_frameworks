#!/usr/bin/env python
# coding: utf-8

# # Reuters Newswire Dataset Trained with Multi-Layer Percentron (Keras)
# * Draft: 2020-11-25 (Wed)

# ## Summary
# ### Project
# * Text classification
# * Multiclass classification
#   * More specifically, single-label multiclass classification
# * Train a 2-layer Multi-Layer Perceptron (MLP) on the Reuters newswire dataset
# 
# ### Reuters Newswire Dataset
# * 11,228 newswires from [Reuters](https://www.reuters.com/)
# * labeled over 46 topics; 46 classes
#   * The label is an integer ranging from 0 to 45.
# * See [7_reuters_newswire_dataset.ipynb](7_reuters_newswire_dataset.ipynb) for details.

# ## Tutorials
# ### Official tutorial by Keras
# * Not available
# 
# ### Book chapter
# * [Deep Learning with Python](https://www.manning.com/books/deep-learning-with-python), François Chollet, Nov. 2017, Manning Publications
#   * [3.5. Classifying newswires: a multiclass classification example](https://livebook.manning.com/book/deep-learning-with-python/chapter-3/193)
#   
# * 케라스 창시자에게 배우는 딥러닝, 프랑소와 숄레 지음, 박해선 옮김, 길벗, 2018-10-22
#   * 3.5. 뉴스 기사 분류: 다중 분류 문제, pp.117-126
# 
# ### Selected Google search results
# Keywords: keras reuters example
# 
# * [Reuters - Document classification with Keras TF](https://www.kaggle.com/drscarlat/reuters-document-classification-with-keras-tf), Kaggle

# The old code

# Configuration
batch_size = 512
epochs = 10

# Python module imports
from keras 		   import models
from keras 		   import layers
from keras.datasets 	   import reuters
from keras.utils.np_utils import to_categorical
import numpy as np

# Data acquisition
(train_data, train_labels), (test_data, test_labels) = reuters.load_data( num_words=10000 )

# Double-check the dataset size
print( train_data.shape[0], 'training samples' )
print( test_data.shape[0], 'test samples' )

total_sample_size = train_data.shape[0] + test_data.shape[0]
print( total_sample_size, 'total samples' )
print( train_labels.shape[0], 'training labels,', test_labels.shape[0], 'test labels')

# Double-check the content of the dataset by seeing a sample data
sample_data = train_data[10]

# Notice the sample data is not human-readable.
# The first 10 elemetns
sample_data[:10]

word_index = reuters.get_word_index()

# Rename the variable name for convenience
word2index_dict = word_index

# Reverse the key-value to value-key for all items of word2index_dict
index2word_dict = dict( [(value, key) for (key, value) in word2index_dict.items()] )

# Let's see what index2word_dict has got.
index2word_dict[1], index2word_dict[245], index2word_dict[273], index2word_dict[207], index2word_dict[156], index2word_dict[53], index2word_dict[74], index2word_dict[160], index2word_dict[26], index2word_dict[14]

# 0, 1, 2 are padding, start, oov, respectively. So
index2word_dict[245-3], index2word_dict[273-3], index2word_dict[207-3], index2word_dict[156-3], index2word_dict[53-3], index2word_dict[74-3], index2word_dict[160-3], index2word_dict[26-3], index2word_dict[14-3]

# Decode the sample data
# For each word in sample_data, change an index to a word and put a space ' '.
decoded_sample_data = ' '.join( [ index2word_dict.get(word - 3, '?') for word in
sample_data])

print( decoded_sample_data )

# ### Data Preparation

# One-hot encoding, https://en.wikipedia.org/wiki/One-hot
# All columns are 0 except 1 for the index.
def vectorize_sequences( sequences, dimension=10000 ):
    # One-hot encoding with 10k columns
    #import numpy as np

    results = np.zeros((len(sequences), dimension))
    for i, sequence in enumerate(sequences):
        results[i, sequence] = 1.
    return results

# Vectorize the training and test data to tensors with 10k columns
x_train = vectorize_sequences( train_data )
x_test = vectorize_sequences( test_data )

print("x_train", x_train.shape)
print("x_test ", x_test.shape)


# Keras's built-in function `keras.utils.to_categorical` will be used to encode the labels. See below just to deepen the understanding of how one-hot encoding of the labels works.
# Example of [One-hot encoding](https://en.wikipedia.org/wiki/One-hot)
# 
# | Binary | Gray code | One-hot  |
# | :----: | :-------: | :------: |
# |  000   |    000    | 00000001 |
# |  001   |    001    | 00000010 |
# |  010   |    011    | 00000100 |
# |  011   |    010    | 00001000 |
# |  100   |    110    | 00010000 |
# |  101   |    111    | 00100000 |
# |  110   |    101    | 01000000 |
# |  111   |    100    | 10000000 |

def encode_to_one_hot( labels, dimension=46 ):
    import numpy as np

    results = np.zeros((len(labels), dimension))
    for i, label in enumerate(labels):
        results[i, label] = 1.
    return results

y_train_dummy = encode_to_one_hot( train_labels )
y_test_dummy = encode_to_one_hot( test_labels )

print("y_train_dummy", y_train_dummy.shape)
print("y_test_dummy ", y_test_dummy.shape)

print( train_labels[0], y_train_dummy[0] )
print( train_labels[1], y_train_dummy[1] )

# Convert class vectors to binary class matrices
num_classes = 46
y_train = to_categorical( train_labels, num_classes )
y_test = to_categorical( test_labels, num_classes )

print("y_train", y_train.shape)
print("y_test ", y_test.shape)

print( train_labels[0], y_train[0] )
print( train_labels[1], y_train[1] )

# Setting aside a VALIDATION set
x_val           = x_train[:1000]
partial_x_train = x_train[1000:]
y_val           = y_train[:1000]
partial_y_train = y_train[1000:]

print("x_val ", x_val.shape)
print("y_val ", y_val.shape)

print("partial_x_train ", partial_x_train.shape)
print("partial_y_train ", partial_y_train.shape)

# ## Model Training

# We will start off with a basic model for simplicity. Note there are 46 output neurons because 46 classes exist. Given 46 output neurons, 64 input neurons are selected. The size of the input layer is a slightly larger than that of the output layer. The hidden layer size is set to be equal to the input layer.
# 
# Say there exists 16 input neurons. The network size is too small.
# 
# > In a stack of Dense layers like that you’ve been using, each layer can only access information present in the output of the previous layer. If one layer drops some information relevant to the classification problem, this information can never be recovered by later layers: each layer can potentially become an information bottleneck. In the previous example, you used 16-dimensional intermediate layers, but a 16-dimensional space may be too limited to learn to separate 46 different classes: such small layers may act as information bottlenecks, permanently dropping relevant information. - Source: [3.5.3. Building your network](https://livebook.manning.com/book/deep-learning-with-python/chapter-3/215)

# MODEL
model = models.Sequential()
model.add( layers.Dense(64, activation='relu', input_shape=(10000,)) )
model.add( layers.Dense(64, activation='relu') )
model.add( layers.Dense(46, activation='softmax') )
model.summary()

# The network size used by Kaggle's [Reuters - Document classification with Keras TF](https://www.kaggle.com/drscarlat/reuters-document-classification-with-keras-tf):
# 
# ```python
# model = models.Sequential()
# model.add( layers.Dense(256, kernel_regularizer=regularizers.l1(0.001), activation='relu', input_shape=(10000,)) )
# model.add( layers.Dropout(0.5) )
# model.add( layers.Dense(256, kernel_regularizer=regularizers.l1(0.001), activation='relu') )
# model.add( layers.Dropout(0.5) )
# model.add( layers.Dense(46, activation='softmax') )
# model.summary()
# ```
# 
# ```python
# # REGULARIZERS L1 L2
# #regularizers.l1(0.001)
# #regularizers.l2(0.001)
# #regularizers.l1_l2(l1=0.001, l2=0.001)
# 
# # Best results I got with HU=128/128/128 or 256/256 and L1=0.001 and Dropout=0.5 = 77.02%
# # Without Regularizer 72.92%
# # Reg L1 = 76.04, L2 = 76.2, L1_L2 = 76.0
# # Only DropOut (0.5) = 76.85%
# ```
# 

model.compile(optimizer='rmsprop',loss='categorical_crossentropy', metrics=['accuracy'])
history = model.fit(partial_x_train, partial_y_train, epochs=epochs, batch_size=batch_size, validation_data=(x_val, y_val))

# TODO: https://www.kaggle.com/drscarlat/reuters-document-classification-with-keras-tf
# 
# Start from 
# 
# decoded_newswire = ' '.join([reverse_word_index.get(i - 3, '?') for i in
# train_data[0]])
