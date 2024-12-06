# -*- coding: utf-8 -*-
'''
dlp_3_6-training_boston_housing_dataset-regression.py

The Boston Housing Price Dataset

Deep Learning with Python
By François Chollet
https://www.manning.com/books/deep-learning-with-python

3.6. Predicting house prices: a regression example
https://livebook.manning.com/book/deep-learning-with-python/chapter-3/192

pp.127~
3.6. 주택 가격 예측: 회귀 문제
'''

from keras.datasets import boston_housing
from keras import models
from keras import layers
from keras import optimizers
from keras import losses
from keras import metrics

import numpy as np

def build_model( input_length ):
    '''
    Usage:
        model = build_model( train_data.shape[1] )
    '''
    
    model = models.Sequential()
    model.add( layers.Dense(64, activation='relu', input_shape=(input_length,)) )
    model.add( layers.Dense(64, activation='relu') )
    model.add( layers.Dense(1) )  # activation function is linear!
    
    # Set the loss and optimizer
    #   MSE (Mean Squared Error) is a popular loss function for regression problems.
    #   MAE (Mean Absolute Error) is the length between the predicted and target values.
    #     e.g. MAE=0.5 means 500 dollars difference in average.
    model.compile( optimizer='rmsprop', loss='mse', metrics=['mae'] )
    
    return model

# Exponential Moving Average ( 지수 이동 평균 )
def smooth_curve( points, factor=0.9 ):
    smoothed_points = []
    for point in points:
        if smoothed_points:
            previous = smoothed_points[-1]
            smoothed_points.append( previous* factor + point * (1-factor) )
        else:
            smoothed_points.append( point )
    return smoothed_points

# Load data
(train_data, train_targets), (test_data, test_targets) = boston_housing.load_data()
print(f'train_data.shape = {train_data.shape}' )  # (404, 13)
print(f'test_data.shape = {test_data.shape}' )    # (102, 13)
print( train_data[0] )
print( train_targets[0] )

# Prepare data
#   Normalize the data with respect to the features
mean = train_data.mean( axis=0 )
std  = train_data.std( axis=0 )

x_train = (train_data - mean) / std
x_test  = (test_data - mean) / std

y_train = train_targets
y_test  = test_targets

# This is in the book, but I like the above two lines better.
#train_data -= mean
#train_data /= std
#test_data  -= mean
#test_data  /= std
#
#print( x_train[0] )
#print( train_data[0] )
#print( x_test[0] )
#print( test_data[0] )

# Use K-fold cross-validation
k = 4

num_val_samples   = len( x_train ) // k
num_epochs        = 100
all_mae_histories = []
#all_scores        = 0

s = num_val_samples
for i in range( k ):
    print( 'Fold', i)

    # Validation data    
    x_val = x_train[ i*s: (i+1)*s ]
    model = build_model( x_train.shape[1] )
    y_val = y_train[ i*s: (i+1)*s ]
    
    x_train_part = np.concatenate( [x_train[:i*s], x_train[ (i+1)*s:] ], axis=0 )
    y_train_part = np.concatenate( [y_train[:i*s], y_train[ (i+1)*s:] ], axis=0 )
    
    # Train the model
    # Fix this error
    history = model.fit( x_train_part, y_train_part,
                         validation_data = (x_val, y_val),
                         epochs=num_epochs, batch_size=1, verbose=0 )
    history_dict = history.history
    mae          = history_dict[ 'val_mean_absolute_error' ]
    all_mae_histories.append( mae )

# Plot the history
import matplotlib.pyplot as plt

average_mae_history = [ np.mean( [ x[i] for x in all_mae_histories ] )
                                   for i in range( num_epochs ) ]
epochs = range(1, len( average_mae_history )+1 )

plt.plot( epochs, average_mae_history )
plt.title( 'Average Mean Absolute Error' )
plt.xlabel( 'Epochs' )
plt.ylabel( 'Validation MAE' )
plt.show()

# Smooth the history and plot it.
smooth_mae_history = smooth_curve( average_mae_history[10:] )
epochs = range(1, len( smooth_mae_history )+1 )

plt.clf()
plt.plot( epochs, smooth_mae_history)
plt.title( 'Moving Averaged Mean Absolute Error' )
plt.xlabel( 'Epochs' )
plt.ylabel( 'Validation MAE' )
plt.show()

# EOF