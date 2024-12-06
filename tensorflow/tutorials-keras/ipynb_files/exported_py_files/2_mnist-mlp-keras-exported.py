#!/usr/bin/env python
# coding: utf-8

# # Training the MNIST Dataset with MLP on Keras
# * Google search: keras mnist example with mlp
#   * [How to create an MLP classifier with TensorFlow 2.0 and Keras](https://www.machinecurve.com/index.php/2019/07/27/how-to-create-a-basic-mlp-classifier-with-the-keras-sequential-api/)
# 
# * The following Keras code is similar to the above reference, but not equal.
# * Read the reference to understand the details.

# ## Data acquisition

# In[58]:


from tensorflow import keras

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()


# ## Data exploration

# In[59]:


print(type(x_train), type(y_train), type(x_test), type(y_test))


# In[60]:


print( x_train.shape, y_train.shape, x_test.shape, y_test.shape )


# In[61]:


import matplotlib.pyplot as plt
plt.imshow(x_train[0])
plt.show()


# In[62]:


y_train.shape, y_train, 


# In[63]:


plt.imshow(x_train[1])
plt.show()


# In[64]:


plt.imshow(x_train[2])
plt.show()


# ## Data Preparation

# In[65]:


# pixel value ranges from 0 to 255. (256)
# scaling the max value to 1
x_train_normalized = x_train.astype('float32') / 255
x_test_normalized = x_test.astype('float32') / 255


# In[66]:


plt.imshow(x_train_normalized[0], cmap='Greys')


# In[67]:


import numpy as np

# Make sure the shape
x_train_normalized = np.expand_dims( x_train_normalized, -1 )
x_test_normalized = np.expand_dims( x_test_normalized, -1 )
print( x_train_normalized.shape[0], x_test_normalized.shape[0] )


# In[68]:


# Reshape the data
#   by flattening the 2D (28x28) to 1D (784)
# input_shape = (28, 28, 1)
input_shape = (784, )

x_train_prepared = x_train.reshape(x_train_normalized.shape[0], input_shape[0])
x_test_prepared = x_test.reshape(x_test_normalized.shape[0], input_shape[0])


# In[70]:


x_train_normalized.shape[0], input_shape[0]


# In[71]:


# One-hot encoding
number_of_classes = 10  # because 0-9

y_train_prepared = keras.utils.to_categorical(y_train, number_of_classes)
y_test_prepared = keras.utils.to_categorical(y_test, number_of_classes)


# In[72]:


y_train_prepared[0]


# In[73]:


y_train_prepared[1]


# In[74]:


y_train_prepared[2]


# In[75]:


y_test.shape, y_test


# In[76]:


y_test_prepared[0]


# In[77]:


y_test_prepared[1]


# ## Feature Engineering
# is skipped

# ## Model Selection
# MLP with
# * input layer of 350 neurons
# * hidden layer of 50 neurons
# * output layer of 10 neurons

# In[80]:


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import layers

model = keras.Sequential(
    [Dense(350, input_shape=input_shape, activation='relu'),
     Dense(50, activation='relu'),
     Dense(number_of_classes, activation='softmax'),
    ]
)


# ## Model Training & Hyper-parameter Tuning
# Configure the hyper-parameters.
# 
# Recall
# ```text
# (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
# ```

# In[81]:


model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])


# In[87]:


model.fit(x_train_prepared, y_train_prepared, epochs=20, batch_size=250, validation_split=0.2)

# ValueError: Shapes (250, 10) and (250, 28, 28, 10) are incompatible
# ValueError: Shapes (32, 10) and (32, 28, 28, 10) are incompatible
# -> input_shape = (28, 28, 1) => input_shape = (784, )
# ValueError: Input 0 of layer sequential_1 is incompatible with the layer: 
#              expected axis -1 of input shape to have value 784 but received input with shape (32, 28, 28, 1)
# -> x_train = x_train.reshape(x_train.shape[0], input_shape[0])
# -> x_test = x_test.reshape(x_test.shape[0], input_shape[0])


# ## Predictions

# In[85]:


predictions = model.evaluate(x_test_prepared, y_test_prepared)


# MLP can achieve the accuracy of 0.9803

# In[86]:


print(f'Test results: Loss = {predictions[0]}, Accuracy = {predictions[1]}')

