# Keras
#
# keras_getting_started.py
#
#   This example code is in "Getting started: 30 seconds to Keras" 
# in the official Keras homepage. It's like hello-world for Keras.
#
# A command to run this script on Docker is:
#
#  $ docker run -it --name keras_test -v ~/aimldl/keras:/home/user/uploads aimldl/keras_base_image
#  your_docker_container $ python3 keras_hello_world.py
#
# To-do:
#   - There're some errors in the # parts. Correct them.
#   - In the keras base image,
#   - alias python='python3'
#   - mkdir keras
#
#   Last updated on 2018-09-19 (Wed)
#   First written on 2018-09-18 (Tue)
#   Written by Tae-Hyung "T" Kim, Ph.D.

from keras.utils import np_utils
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Activation
import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_test) = mnist.load_data()
# 28*28=784
x_train = x_train.reshape(60000, 784).astype('float32') / 255.0
y_train = np_utils.to_categorical( y_train )

model = Sequential()
model.add( Dense(units=64, activation='relu', input_dim=28*28) )
model.add( Dense(units=10, activation='softmax') )
model.compile( loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

hist = model.fit( x_train, y_train, epochs=1, batch_size=32 )
#hist = model.fit( x_train, y_train, epochs=5, batch_size=32 )
# hist includes only loss and acc.
print('loss : ' + str( hist.history['loss'] ) )
print('acc' + str( hist.history['acc'] ))

fig, loss_ax = plt.subplots()
acc_ax = loss_ax.twinx()
loss_ax.plot( hist.history['loss'],'y', label='train loss' )
loss_ax.plot( hist.history['acc'],'b', label='train acc' )
loss_ax.set_xlabel('epoch')
loss_ax.set_ylabel('loss')
loss_ax.set_ylabel('accuracy')
loss_ax.legend(loc='upper left')
loss_ax.legend(loc='lower left')
plt.show

# To-do
#
# Fix this error
# Traceback (most recent call last):
#   File "keras_getting_started-01.py", line 44, in <module>
#     fig, loss_ax = plt.subplots()
#   File "/usr/local/lib/python3.6/dist-packages/matplotlib/pyplot.py", line 1184, in subplots
#     fig = figure(**fig_kw)
#   File "/usr/local/lib/python3.6/dist-packages/matplotlib/pyplot.py", line 533, in figure
#     **kwargs)
#   File "/usr/local/lib/python3.6/dist-packages/matplotlib/backend_bases.py", line 161, in new_figure_manager
#     return cls.new_figure_manager_given_figure(num, fig)
#   File "/usr/local/lib/python3.6/dist-packages/matplotlib/backends/_backend_tk.py", line 1046, in new_figure_manager_given_figure
#     window = Tk.Tk(className="matplotlib")
#   File "/usr/lib/python3.6/tkinter/__init__.py", line 2020, in __init__
#     self.tk = _tkinter.create(screenName, baseName, className, interactive, wantobjects, useTk, sync, use)
# _tkinter.TclError: no display name and no $DISPLAY environment variable
#
# Note the following line alone is bad.
#   import matplotlib.pyplot as plt
#
# Adding the following two lines stops the error message. 
#   import matplotlib
#   matplotlib.use('Agg')
#   import matplotlib.pyplot as plt
# But this behavior is not what we want.
#
# _tkinter.TclError: couldn't connect to display "localhost:10.0"

