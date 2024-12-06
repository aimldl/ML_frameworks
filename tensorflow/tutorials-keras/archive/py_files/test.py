'''
data_normalization.py
https://aimldl.blog.me/221627895429

https://livebook.manning.com/book/deep-learning-with-python/chapter-3/190
'''
from keras.datasets import boston_housing
import numpy as np

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

# Option 1
x_train = (train_data - mean) / std
x_test  = (test_data - mean) / std

# Option 2
train_data -= mean
train_data /= std
test_data  -= mean
test_data  /= std

print( 'Compare the normalized values.' )
print( x_train[0] )
print( train_data[0] )
print( x_test[0] )
print( test_data[0] )