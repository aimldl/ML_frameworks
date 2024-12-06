# -*- coding: utf-8 -*-
'''
dlp_3_4-evaluating_predicting_imdb_dataset-binary_classification-sentiment_analysis.py

The IMDB Dataset

Deep Learning with Python
By François Chollet
https://www.manning.com/books/deep-learning-with-python

3.4. Classifying movie reviews: a binary classification example
https://livebook.manning.com/book/deep-learning-with-python/chapter-3/100

pp.115~116
3.4.영화 리뷰 분류: 이진 분류 예
'''

# Stop early when epoch=4
#   because it gives the best result.
# Check below with "This is different".
# Only four lines are different compared to the previous code.

from keras.datasets import imdb
from keras import models
from keras import layers
from keras import optimizers
from keras import losses
from keras import metrics

import numpy as np

def vectorize_sequences( sequences, dimension=10000 ):
    #TypeError: data type not understood
    # <class 'numpy.ndarray'>
    results = np.zeros( (len(sequences), dimension) )
    for i, sequence in enumerate( sequences ):
        results[i, sequence] = 1.
    return results


# Load data
(train_data, train_labels), (test_data, test_labels) = imdb.load_data( num_words=10000 )
print( train_data[0] )
print( train_labels[0] )
print( max( [max(sequence) for sequence in train_data] ) )

# Prepare data
x_train = vectorize_sequences( train_data )
x_test  = vectorize_sequences( test_data )
print( x_train[0] )
print( x_test[0] )

y_train = np.asarray( train_labels ).astype('float32')
y_test  = np.asarray( test_labels ).astype('float32')

# Decode
word_index = imdb.get_word_index()
reverse_word_index = dict( [(value, key) for (key, value) in word_index.items()])
decoded_review = ' '.join( [reverse_word_index.get(i-3, '?') for i in train_data[0] ] )

# Create a model
model = models.Sequential()
model.add( layers.Dense(16, activation='relu', input_shape=(10000,)) )
model.add( layers.Dense(16, activation='relu') )
model.add( layers.Dense(1, activation='sigmoid') )

# Set the loss and optimizer
#model.compile( optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy' ])
#model.compile( optimizer=optimizers.RMSprop( lr=0.001), loss='binary_crossentropy', metrics=['accuracy' ])
#model.compile( optimizer=optimizers.RMSprop( lr=0.001), loss=losses.binary_crossentropy, metrics=[ metrics.binary_accuracy ])
model.compile( optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy' ])

# Validation data
x_train_part = x_train[10000:]
x_val        = x_train[:10000]
y_train_part = y_train[10000:]
y_val        = y_train[:10000]

history = model.fit( x_train_part, y_train_part,
                    epochs=4,  # This is different
                    batch_size=512,
                    validation_data=(x_val, y_val) )

# Plot the history
import matplotlib.pyplot as plt

history_dict = history.history
#history_dict.keys()
loss     = history_dict[ 'loss' ]
val_loss = history_dict[ 'val_loss' ]

epochs = range( 1, len(loss)+1 )

plt.plot( epochs, loss, 'bo', label='Training loss' )
plt.plot( epochs, val_loss, 'b', label='Validation loss' )
plt.title( 'Training & Validation Loss' )
plt.xlabel( 'Epochs' )
plt.ylabel( 'Loss' )
plt.legend()
plt.show()

# Plot accuracy
plt.clf()
acc     = history_dict[ 'acc' ]
val_acc = history_dict[ 'val_acc' ]

plt.plot( epochs, acc, 'bo', label='Training accuracy' )
plt.plot( epochs, val_acc, 'b', label='Validation accuracy' )
plt.title( 'Training & Validation Accuracy' )
plt.xlabel( 'Epochs' )
plt.ylabel( 'accuracy' )
plt.legend()
plt.show()

#%% This part is different

# Evaluate & Predict
results     = model.evaluate( x_test, y_test )
predictions = model.predict( x_test )

print( results )  # [1.0153425671856846, 0.7871772039180766]
print( predictions[0].shape )
print( np.sum( predictions[0] ) )  # Sum is 1.

# The one with the largest prediction value
#   is the class with the highest probability.
print( np.argmax( predictions[0] ) )

# EOF
