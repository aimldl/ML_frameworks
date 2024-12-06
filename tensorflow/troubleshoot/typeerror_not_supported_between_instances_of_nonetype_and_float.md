



## Problem

```bash
TypeError: '>' not supported between instances of 'NoneType' and 'float'
```



```python
# GRADED FUNCTION: train_mnist
def train_mnist():
    # Please write your code only where you are indicated.
    # please do not remove # model fitting inline comments.
   
    # YOUR CODE SHOULD START HERE
    class myCallback(tf.keras.callbacks.Callback):
        def on_epoch_end(self, epoch, logs={}):
            if (logs.get('accuracy') > 0.99):
                print("\nReached 99% accuracy so cancelling training!")
                self.model.stop_training = True
    # YOUR CODE SHOULD END HERE
```



```bash
Epoch 1/10
59616/60000 [============================>.] - ETA: 0s - loss: 0.1998 - acc: 0.9414
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-16-d3617ae8770d> in <module>
----> 1 train_mnist()

<ipython-input-15-313e4db034b3> in train_mnist()
     39     # model fitting
     40     history = model.fit(# YOUR CODE SHOULD START HERE
---> 41         x_train, y_train, epochs=10, callbacks=[callbacks]
     42               # YOUR CODE SHOULD END HERE
     43     )

/usr/local/lib/python3.6/dist-packages/tensorflow/python/keras/engine/training.py in fit(self, x, y, batch_size, epochs, verbose, callbacks, validation_split, validation_data, shuffle, class_weight, sample_weight, initial_epoch, steps_per_epoch, validation_steps, validation_freq, max_queue_size, workers, use_multiprocessing, **kwargs)
    778           validation_steps=validation_steps,
    779           validation_freq=validation_freq,
--> 780           steps_name='steps_per_epoch')
    781 
    782   def evaluate(self,

/usr/local/lib/python3.6/dist-packages/tensorflow/python/keras/engine/training_arrays.py in model_iteration(model, inputs, targets, sample_weights, batch_size, epochs, verbose, callbacks, val_inputs, val_targets, val_sample_weights, shuffle, initial_epoch, steps_per_epoch, validation_steps, validation_freq, mode, validation_in_fit, prepared_feed_values_from_dataset, steps_name, **kwargs)
    417     if mode == ModeKeys.TRAIN:
    418       # Epochs only apply to `fit`.
--> 419       callbacks.on_epoch_end(epoch, epoch_logs)
    420     progbar.on_epoch_end(epoch, epoch_logs)
    421 

/usr/local/lib/python3.6/dist-packages/tensorflow/python/keras/callbacks.py in on_epoch_end(self, epoch, logs)
    309     logs = logs or {}
    310     for callback in self.callbacks:
--> 311       callback.on_epoch_end(epoch, logs)
    312 
    313   def on_train_batch_begin(self, batch, logs=None):

<ipython-input-15-313e4db034b3> in on_epoch_end(self, epoch, logs)
      8         def on_epoch_end(self, epoch, logs={}):
      9             print( type(logs.get('accuracy')) )
---> 10             if (logs.get('accuracy') > 0.99):
     11                 print("\nReached 99% accuracy so cancelling training!")
     12                 self.model.stop_training = True

```



## Hint

`logs.get('accuracy')` returns nothing.

```python
>>> print( type(logs.get('accuracy')) )
<class 'NoneType'>
```



        def on_epoch_end(self, epoch, logs={}):
            if (logs.get('acc') > 0.99):


And this is what the progress bar shows.

```bash
Epoch 1/10
59616/60000 [============================>.] - ETA: 0s - loss: 0.1998 - acc: 0.9414
```

## Solution

`accuracy` has been changed to `acc` which is the same as the way progress bar displays the accuracy.

From

```python
logs.get('accuracy')
```

to

```python
logs.get('acc')
```

The change in the source code

```python
# GRADED FUNCTION: train_mnist
def train_mnist():
    # Please write your code only where you are indicated.
    # please do not remove # model fitting inline comments.
   
    # YOUR CODE SHOULD START HERE
    class myCallback(tf.keras.callbacks.Callback):
        def on_epoch_end(self, epoch, logs={}):
            if (logs.get('acc') > 0.99):
                print("\nReached 99% accuracy so cancelling training!")
                self.model.stop_training = True
    # YOUR CODE SHOULD END HERE
```



```python
>>> print( type(logs.get('acc')) )
<class 'numpy.float32'>
```

