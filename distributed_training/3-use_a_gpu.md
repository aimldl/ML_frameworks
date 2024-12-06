# Use a GPU

https://www.tensorflow.org/guide/gpu#setup

* Single GPU: No code changes required

* Multiple GPUs: the simplest way is using [Distribution Strategies](https://www.tensorflow.org/guide/distributed_training).

## Distributed training with TensorFlow

[`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy) is a TensorFlow API to distribute training across multiple GPUs, multiple machines or TPUs. Using this API, you can distribute your existing models and training code with minimal code changes because we have changed the underlying components of TensorFlow to become strategy-aware. 

This includes variables, layers, models, optimizers, metrics, summaries, and checkpoints.

In TensorFlow 2.x, you can execute your programs eagerly, but the eager mode is only recommended for debugging purpose and not supported for `TPUStrategy`. 

### Types of strategies

#### Synchronous vs. asynchronous training for data parallelism

* Synchronous
  * All workers train over different slices of input data in sync, and aggregating gradients at each step. Typically supported via all-reduce.
* Asynchronous
  * All workers are independently training over the input data & updating variables asynchronously. Typically supported through parameter server architecture

#### Hardware platform

* Scale 
  * onto multiple GPUs on one machine
  * multiple machines in a network (with 0 or more GPUs each), or
  * on Cloud TPUs

## Six strategies

| Training API         | MirroredStrategy | TPUStrategy   | MultiWorkerMirroredStrategy | CentralStorageStrategy | ParameterServerStrategy    | OneDeviceStrategy |
| -------------------- | ---------------- | ------------- | --------------------------- | ---------------------- | -------------------------- | ----------------- |
| Keras API            | Supported        | Supported     | Experimental support        | Experimental support   | Supported planned post 2.3 | Supported         |
| Custom training loop | Supported        | Supported     | Experimental support        | Experimental support   | Supported planned post 2.3 | Supported         |
| Estimator API        | Limited Support  | Not supported | Limited Support             | Limited Support        | Limited Support            | Limited Support   |

### MirroredStrategy

[tf.distribute.MirroredStrategy](https://www.tensorflow.org/api_docs/python/tf/distribute/MirroredStrategy) supports synchronous distributed training on multiple GPUs on one machine. 

* The simplest way to create `MirroredStrategy` is:

  ```python
  mirrored_strategy = tf.distributed.MirroredStrategy()
  ```

  will use all the visible GPUs to TensorFlow and use NCCl as the cross device communication.

* To use only some of the GPUs,

```python
mirrored_strategy = tf.distribute.MirroredStrategy(devices=["/gpu:0", "/gpu:1"])
```

* cross_device_ops

```python
mirrored_strategy = tf.distribute.MirroredStrategy(
    cross_device_ops=tf.distribute.HierarchicalCopyAllReduce())
```

There are three options for the cross device communication

* [tf.distribute.NcclAllReduce](https://www.tensorflow.org/api_docs/python/tf/distribute/NcclAllReduce) (Default)

* [tf.distribute.HierarchicalCopyAllReduce](https://www.tensorflow.org/api_docs/python/tf/distribute/HierarchicalCopyAllReduce)
* [tf.distribute.ReductionToOneDevice](https://www.tensorflow.org/api_docs/python/tf/distribute/ReductionToOneDevice)

* MirroredVariable 
  * Each variable in the model is mirrored across all the replicas where one replica is created per GPU device.
  * These variables are kept in sync with each other by applying identical updates.
* All-reduce algorithms 
  * aggregates tensors across all the devices by adding them up and makes them available on each device.
  * can reduce the overhead of synchronization significantly and efficiently.
  * Many all-reduce algorithms and implementations are available.
    * By default, NVIDIA NCCL is used.

## Setup to use GPU

```tensorflow
import tensorflow as tf
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
```

Expecting

```python
Num GPUs Available:  2
```

If 

```python
Num GPUs Available:  0
```

Your machine is not properly set up to run with GPU(s).

```text
"/device:CPU:0": The CPU of your machine.
"/GPU:0": Short-hand notation for the first GPU of your machine that is visible to TensorFlow.
"/job:localhost/replica:0/task:0/device:GPU:1": Fully qualified name of the second GPU of your machine that is visible to TensorFlow.
```

### Logging device placement

```python
tf.debugging.set_log_device_placement(True)

# Create some tensors
a = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
b = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
c = tf.matmul(a, b)

print(c)
```

Expected output

```python
Executing op MatMul in device /job:localhost/replica:0/task:0/device:GPU:0
tf.Tensor(
[[22. 28.]
 [49. 64.]], shape=(2, 2), dtype=float32)
```

### Manual device placement

```python
tf.debugging.set_log_device_placement(True)

# Place tensors on the CPU
with tf.device('/CPU:0'):
  a = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
  b = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])

c = tf.matmul(a, b)
print(c)
```

### Limiting GPU memory growth

```python
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
  # Restrict TensorFlow to only use the first GPU
  try:
    tf.config.experimental.set_visible_devices(gpus[0], 'GPU')
    logical_gpus = tf.config.experimental.list_logical_devices('GPU')
    print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPU")
  except RuntimeError as e:
    # Visible devices must be set before GPUs have been initialized
    print(e)
```

Expected result

```python
2 Physical GPUs, 1 Logical GPU
```

There are two options

#### Option 1: use  [tf.config.experimental.set_memory_growth](https://www.tensorflow.org/api_docs/python/tf/config/experimental/set_memory_growth)

```python
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
  try:
    # Currently, memory growth needs to be the same across GPUs
    for gpu in gpus:
      tf.config.experimental.set_memory_growth(gpu, True)
    logical_gpus = tf.config.experimental.list_logical_devices('GPU')
    print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
  except RuntimeError as e:
    # Memory growth must be set before GPUs have been initialized
    print(e)
```

Expected result

```python
2 Physical GPUs, 2 Logical GPUs
```

#### Option 2: set the environmental variable `TF_FORCE_GPU_ALLOW_GROWTH` to `true`

```python
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
  # Restrict TensorFlow to only allocate 1GB of memory on the first GPU
  try:
    tf.config.experimental.set_virtual_device_configuration(
        gpus[0],
        [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=1024)])
    logical_gpus = tf.config.experimental.list_logical_devices('GPU')
    print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
  except RuntimeError as e:
    # Virtual devices must be set before GPUs have been initialized
    print(e)
```

## Using a single GPU on a multi-GPU system

If you have more than one GPU in your system, the GPU with the lowest ID will be selected by default. 

```python
tf.debugging.set_log_device_placement(True)

try:
  # Specify an invalid GPU device
  with tf.device('/device:GPU:2'):
    a = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    b = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
    c = tf.matmul(a, b)
except RuntimeError as e:
  print(e)
```

```python
/job:localhost/replica:0/task:0/device:GPU:2 unknown device.
```

If the device you have specified does not exist, you will get a `RuntimeError`: `.../device:GPU:2 unknown device`.

#### [tf.config.set_soft_device_placement(True)](https://www.tensorflow.org/api_docs/python/tf/config/set_soft_device_placement)

TensorFlow can automatically choose an existing and supported device.

```python
tf.config.set_soft_device_placement(True)
tf.debugging.set_log_device_placement(True)

# Creates some tensors
a = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
b = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
c = tf.matmul(a, b)

print(c)
```

## Using multiple GPUs

```python
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
  # Create 2 virtual GPUs with 1GB memory each
  try:
    tf.config.experimental.set_virtual_device_configuration(
        gpus[0],
        [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=1024),
         tf.config.experimental.VirtualDeviceConfiguration(memory_limit=1024)])
    logical_gpus = tf.config.experimental.list_logical_devices('GPU')
    print(len(gpus), "Physical GPU,", len(logical_gpus), "Logical GPUs")
  except RuntimeError as e:
    # Virtual devices must be set before GPUs have been initialized
    print(e)
```



Once we have multiple logical GPUs available to the runtime, we can utilize the multiple GPUs with [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy) or with manual placement.

#### With [tf.distribute.Strategy](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy)

The best practice for using multiple GPUs is to use [tf.distribute.Strategy](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy).

```python
tf.debugging.set_log_device_placement(True)

strategy = tf.distribute.MirroredStrategy()
with strategy.scope():
  inputs = tf.keras.layers.Input(shape=(1,))
  predictions = tf.keras.layers.Dense(1)(inputs)
  model = tf.keras.models.Model(inputs=inputs, outputs=predictions)
  model.compile(loss='mse',
                optimizer=tf.keras.optimizers.SGD(learning_rate=0.2))
```

This program will run a copy of your model on each GPU, splitting the input data between them, also known as "[data parallelism](https://en.wikipedia.org/wiki/Data_parallelism)".

#### Manual placement

```python
tf.debugging.set_log_device_placement(True)

gpus = tf.config.experimental.list_logical_devices('GPU')
if gpus:
  # Replicate your computation on multiple GPUs
  c = []
  for gpu in gpus:
    with tf.device(gpu.name):
      a = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
      b = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
      c.append(tf.matmul(a, b))

  with tf.device('/CPU:0'):
    matmul_sum = tf.add_n(c)

  print(matmul_sum)
```



## References

* [Distributed training with TensorFlow](https://www.tensorflow.org/guide/distributed_training#types_of_strategies)
* [Use a GPU](https://www.tensorflow.org/guide/gpu#setup)
* [MULTI-GPU AND DISTRIBUTED DEEP LEARNING](https://frankdenneman.nl/2020/02/19/multi-gpu-and-distributed-deep-learning/)