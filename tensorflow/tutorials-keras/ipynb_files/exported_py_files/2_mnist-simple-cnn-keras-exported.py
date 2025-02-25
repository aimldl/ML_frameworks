#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tensorflow import keras
import numpy as np

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255

# Make sure the shape
x_train = np.expand_dims( x_train, -1 )
x_test = np.expand_dims( x_test, -1 )

number_of_classes = 10  # because 0-9

# One-hot encoding
y_train = keras.utils.to_categorical(y_train, number_of_classes)


# In[ ]:


y_test = keras.utils.to_categorical(y_test, number_of_classes)


# In[ ]:


input_shape = (28, 28, 1)
#input_shape = (784, )
input_shape


# In[ ]:


# Model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import layers

model = keras.Sequential(
    [
     keras.Input(shape=input_shape),
     layers.Conv2D(32, kernel_size=(3,3), activation='relu'),
     layers.MaxPooling2D(pool_size=(2,2)),
     layers.Conv2D(64, kernel_size=(3,3), activation='relu'),
     layers.MaxPooling2D(pool_size=(2,2)),
     layers.Flatten(),
     layers.Dropout(0.5),
     Dense(number_of_classes, activation='softmax')
    ]
)


# In[ ]:


model.summary()


# In[ ]:


model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=20, validation_split=0.2)  #


# In[ ]:


predictions = model.evaluate(x_test, y_test)

