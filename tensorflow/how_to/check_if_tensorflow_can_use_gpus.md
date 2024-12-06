* Draft: 2021-06-10 (Thu)

# How to Check if TensorFlow can Use GPUs



Google search: tensorflow how to check gpu

### [tf.config.list_physical_devices](https://www.tensorflow.org/api_docs/python/tf/config/list_physical_devices)

Use this API for TensorFlow 2.x,

```bash
$ python -c "import tensorflow as tf; tf.config.list_physical_devices('GPU')"
```

### [tf.test.is_gpu_available](https://www.tensorflow.org/api_docs/python/tf/test/is_gpu_available)

* This API is for TensorFlow 1.x.

```bash
$ python -c 'import tensorflow as tf; tf.test.is_gpu_available()'
```

* You can still use it for TensorFlow 2.x
  * This API is deprecated and `tf.config.list_physical_devices` is suggested for TensorFlow 2.x.
  * Running `tf.test.is_gpu_available()` in TensorFlow 2.x gives the following warning:

```bash
$ python -c 'import tensorflow as tf; tf.test.is_gpu_available()'
  ...
WARNING:tensorflow:From <string>:1: is_gpu_available (from tensorflow.python.framework.test_util) is deprecated and will be removed in a future version.
Instructions for updating:
Use `tf.config.list_physical_devices('GPU')` instead.
  ...
$
```
