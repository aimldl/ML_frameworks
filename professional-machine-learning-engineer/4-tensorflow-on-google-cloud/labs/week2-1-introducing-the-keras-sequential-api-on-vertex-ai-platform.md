# Lab: Introducing the Keras Sequential API on Vertex AI Platform

## Summary

- [training-data-analyst](https://github.com/GoogleCloudPlatform/training-data-analyst)/[courses](https://github.com/GoogleCloudPlatform/training-data-analyst/tree/master/courses)/[machine_learning](https://github.com/GoogleCloudPlatform/training-data-analyst/tree/master/courses/machine_learning)/[deepdive2](https://github.com/GoogleCloudPlatform/training-data-analyst/tree/master/courses/machine_learning/deepdive2)/[introduction_to_tensorflow](https://github.com/GoogleCloudPlatform/training-data-analyst/tree/master/courses/machine_learning/deepdive2/introduction_to_tensorflow)/[**solutions**](https://github.com/GoogleCloudPlatform/training-data-analyst/tree/master/courses/machine_learning/deepdive2/introduction_to_tensorflow/solutions) / [3_keras_sequential_api.ipynb](https://github.com/GoogleCloudPlatform/training-data-analyst/blob/master/courses/machine_learning/deepdive2/introduction_to_tensorflow/solutions/3_keras_sequential_api.ipynb)
- I've added some additional comments in the following lines.
- Each learning objective will correspond to a #TODO in the student lab notebook

## Introduction

The [Keras sequential API](https://keras.io/models/sequential/) allows you to create Tensorflow models layer-by-layer. This is useful for building most kinds of machine learning models but it does not allow you to create models that share layers, re-use layers or have multiple inputs or outputs.

- Purpose: predict the fare amount for NYC taxi cab rides
- **Build a simple deep neural network model** with 
  - the **Keras sequential api** and 
  - **feature columns**. 

- **Deploy the trained model using Vertex AI** and see how to call our model for online prediciton.

## Learning objectives

1. Build a DNN model using the **Keras Sequential API**
2. Learn how to use **feature columns** in a Keras model
3. Learn how to train a model with Keras
4. Learn how to save/load, and deploy a Keras model on GCP
5. Learn how to deploy the Model to Vertex AI and make predictions with the Keras model

## Excerpts from the solution `.ipynb`

### 2. Learn how to use feature columns in a Keras model

We will use feature columns to connect our raw data to our keras DNN model. Feature columns make it easy to perform common types of feature engineering on your raw data. For example, you can one-hot encode categorical data, create feature crosses, embeddings and more. Refer to [feature columns guide](https://www.tensorflow.org/guide/feature_columns) for more information.

### 3. Learn how to train a model with Keras

To train your model, Keras provides three functions that can be used:

1. `.fit()` for training a model for a fixed number of epochs (iterations on a dataset).
2. `.fit_generator()` for training a model on data yielded batch-by-batch by a generator
3. `.train_on_batch()` runs a single gradient update on a single batch of data.

The `.fit()` function works well for small datasets which can fit entirely in memory. However, for large datasets (or if you need to manipulate the training data on the fly via data augmentation, etc) you will need to use `.fit_generator()` instead. The `.train_on_batch()` method is for more fine-grained control over training and accepts only a single batch of data.

The taxifare dataset we sampled is small enough to fit in memory, so can we could use `.fit` to train our model. Our `create_dataset` function above generates batches of training examples, so we could also use `.fit_generator`. In fact, when calling `.fit` the method inspects the data, and if it's a generator (as our dataset is) it will invoke automatically `.fit_generator` for training.

We start by setting up some parameters for our training job and create the data generators for the training and validation data.

We refer you the the blog post [ML Design Pattern #3: Virtual Epochs](https://medium.com/google-cloud/ml-design-pattern-3-virtual-epochs-f842296de730) for further details on why express the training in terms of `NUM_TRAIN_EXAMPLES` and `NUM_EVALS` and why, in this training code, the number of epochs is really equal to the number of evaluations we perform.

The [.fit method](https://www.tensorflow.org/versions/r2.0/api_docs/python/tf/keras/Model#fit). 

Here `x` specifies the input data which in our case is a `tf.data` dataset returning a tuple of (inputs, targets). The `steps_per_epoch` parameter is used to mark the end of training for a single epoch. Here we are training for NUM_EVALS epochs. Lastly, for the `callback` argument we specify a Tensorboard callback so we can inspect Tensorboard after training.

## Source Code

```
!sudo chown -R jupyter:jupyter /home/jupyter/training-data-analyst
```

```
# Load raw data
!ls -l ../data/*.csv
```

```
-rw-r--r-- 1 jupyter jupyter  123590 Nov 27 06:00 ../data/taxi-test.csv
-rw-r--r-- 1 jupyter jupyter 2186310 Nov 27 06:00 ../data/taxi-traffic-test.csv
-rw-r--r-- 1 jupyter jupyter 9713118 Nov 27 06:00 ../data/taxi-traffic-train.csv
-rw-r--r-- 1 jupyter jupyter 2036826 Nov 27 06:00 ../data/taxi-traffic-valid.csv
-rw-r--r-- 1 jupyter jupyter  579055 Nov 27 06:00 ../data/taxi-train.csv
-rw-r--r-- 1 jupyter jupyter  123114 Nov 27 06:00 ../data/taxi-valid.csv
```

```
#!head ../data/taxi*.csv
!head -n 1 ../data/taxi*.csv
```

```
==> ../data/taxi-test.csv <==
6.0,2013-03-27 03:35:00 UTC,-73.977672,40.784052,-73.965332,40.801025,2,0

==> ../data/taxi-traffic-test.csv <==
15.7,6,12,-73.990072,40.758199,-73.974686,40.742004,2089

==> ../data/taxi-traffic-train.csv <==
6.1,2,0,-73.98689499999999,40.729723,-74.00631,40.739407,1129

==> ../data/taxi-traffic-valid.csv <==
7.7,2,11,-73.97463,40.742118,-73.98544,40.760585999999996,1059

==> ../data/taxi-train.csv <==
11.3,2011-01-28 20:42:59 UTC,-73.999022,40.739146,-73.990369,40.717866,1,0

==> ../data/taxi-valid.csv <==
5.3,2012-01-03 19:21:35 UTC,-73.962627,40.763214,-73.973485,40.753353,1,0
```

### code

```python
import datetime
import os
import shutil

import numpy as np
import pandas as pd
import tensorflow as tf
from google.cloud import aiplatform
from matplotlib import pyplot as plt
from tensorflow import keras
from tensorflow.keras.callbacks import TensorBoard
from tensorflow.keras.layers import Dense, DenseFeatures
from tensorflow.keras.models import Sequential

print(tf.__version__)
%matplotlib inline

# Use tf.data to read the CSV files
CSV_COLUMNS = [
    "fare_amount",
    "pickup_datetime",
    "pickup_longitude",
    "pickup_latitude",
    "dropoff_longitude",
    "dropoff_latitude",
    "passenger_count",
    "key",
]
LABEL_COLUMN = "fare_amount"

# There are 8 columns in CSV_COLUMNS
DEFAULTS = [[0.0], ["na"], [0.0], [0.0], [0.0], [0.0], [0.0], ["na"]]
UNWANTED_COLS = ["pickup_datetime", "key"]

# Prepare the features & label from row_data
def features_and_labels(row_data):
    label = row_data.pop(LABEL_COLUMN)
    features = row_data

    for unwanted_col in UNWANTED_COLS:
        features.pop(unwanted_col)

    return features, label

# Later this function will be called as follows.
#   TRAIN_BATCH_SIZE = 1000
#   NUM_EVAL_EXAMPLES = 10000  # enough to get a reasonable sample
#   trainds = create_dataset(
#       pattern="../data/taxi-train*", batch_size=TRAIN_BATCH_SIZE, mode="train"
#   )
#   evalds = create_dataset(
#       pattern="../data/taxi-valid*", batch_size=1000, mode="eval"
#   ).take(NUM_EVAL_EXAMPLES // 1000)

def create_dataset(pattern, batch_size=1, mode="eval"):
    # https://www.tensorflow.org/api_docs/python/tf/data/experimental/make_csv_dataset
    #   tf.data.experimental.make_csv_dataset
    #     reads CSV files into a dataset
    #       where each element of the dataset is a (features, labels) tuple 
    #       that corresponds to a batch of CSV rows. 
    dataset = tf.data.experimental.make_csv_dataset(
        pattern, batch_size, CSV_COLUMNS, DEFAULTS
    )
    # file_pattern	List of files or patterns of file paths containing CSV records. 
    #               See tf.io.gfile.glob for pattern rules.
    # By default, the first rows of the CSV files are expected to be
    #   headers listing the column names. 
    # If the first rows are not headers, 
    #   set header=False and provide the column names with the column_names argument.

    # https://www.geeksforgeeks.org/python-map-function/
    #   Python map() function
    #     returns a list of the results after applying the given function  
    #       to each item of a given iterable (list, tuple etc.) 
    #     syntax: map(fun, iter)
    dataset = dataset.map(features_and_labels)
    #  returns a (features, label) tuple.
    
    # https://www.tensorflow.org/api_docs/python/tf/data/Dataset
    #   tf.data.Dataset
    #     Note: cache will produce exactly the same elements during each iteration 
    #           through the dataset. If you wish to randomize the iteration order, 
    #           make sure to call shuffle after calling cache.
    
    # https://www.tensorflow.org/api_docs/python/tf/data/Dataset#shuffle
    #   tf.data.Dataset > shuffle
    #     Randomly shuffles the elements of this dataset.
    
    # https://www.tensorflow.org/api_docs/python/tf/data/Dataset#repeat
    #   tf.data.Dataset > repeat
    #     Repeats this dataset so each original value is seen count times.
    #     The default behavior (if count is None or -1) is 
    #       for the dataset be repeated indefinitely.
    if mode == "train":
        dataset = dataset.shuffle(buffer_size=1000).repeat()

    # https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch
    #   tf.data.Dataset > prefetch
    #     creates a Dataset that prefetches elements from this dataset.
    #   - Most dataset input pipelines should end with a call to prefetch. 
    #   - This allows later elements to be prepared 
    #       while the current element is being processed. 
    #   - This often improves latency and throughput 
    #       at the cost of using additional memory to store prefetched elements.

    # take advantage of multi-threading; 1=AUTOTUNE
    dataset = dataset.prefetch(1)
    return dataset

# Build a simple keras DNN model

# Reminder
# CSV_COLUMNS = [
#    "fare_amount",
#    "pickup_datetime", 
#    "pickup_longitude",  *
#    "pickup_latitude",   *
#    "dropoff_longitude", *
#    "dropoff_latitude",  *
#    "passenger_count",   *
#    "key",
#]
INPUT_COLS = [
    "pickup_longitude",
    "pickup_latitude",
    "dropoff_longitude",
    "dropoff_latitude",
    "passenger_count",
]

# Create input layer of feature columns

# tf.feature_column.numeric_column()
#   We won't do any feature engineering. However, we still need to create a list of feature columns to specify the numeric values which will be passed on to our model. To do this, we use tf.feature_column.numeric_column()
# tf.feature_column.numeric_column(INPUT_COLS)
#   ...
# ValueError: key must be a string. Got: type <class 'list'>. Given key: ['pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude', 'passenger_count'].

# tf.feature_column.numeric_column(column_string) for column_string in INPUT_COLS
#  ...
# SyntaxError: invalid syntax

# [tf.feature_column.numeric_column(column_string) for column_string in INPUT_COLS]
# [NumericColumn(key='pickup_longitude', shape=(1,), default_value=None, dtype=tf.float32, normalizer_fn=None),
  ...
# NumericColumn(key='passenger_count', shape=(1,), default_value=None, dtype=tf.float32, normalizer_fn=None)]

# { column_string: tf.feature_column.numeric_column(column_string) for column_string in INPUT_COLS}

# {'pickup_longitude': NumericColumn(key='pickup_longitude', shape=(1,), default_value=None, dtype=tf.float32, normalizer_fn=None),
  ...
# 'passenger_count': NumericColumn(key='passenger_count', shape=(1,), default_value=None, dtype=tf.float32, normalizer_fn=None)}

# TODO 1
feature_columns = {
    colname: tf.feature_column.numeric_column(colname) for colname in INPUT_COLS
}

# Build a keras DNN model using Sequential API
# https://www.tensorflow.org/guide/keras/sequential_model
# TODO 2a
model = Sequential(
    [
        DenseFeatures(feature_columns=feature_columns.values()),
        Dense(units=32, activation="relu", name="h1"),
        Dense(units=8, activation="relu", name="h2"),
        Dense(units=1, activation="linear", name="output"),
    ]
)
# The Sequential model is a linear stack of layers.

# TODO 2b
# Create a custom evalution metric
def rmse(y_true, y_pred):
    return tf.sqrt( tf.reduce_mean(tf.square(y_pred - y_true)) )

# Compile the keras model
#   RMSE (root mean square error)
model.compile(optimizer="adam", loss="mse", metrics=[rmse, "mse"])
# Q: I'm not sure why RMSE is denoted as MSE. RMSE and MSE are different!
#    https://stephenallwright.com/rmse-vs-mse/
# A:  model.compile(optimizer="adam", loss="rmse", metrics=[rmse, "rmse"])
# ValueError: Unknown loss function: rmse. Please ensure this object is passed to the `custom_objects` argument. See https://www.tensorflow.org/guide/keras/save_and_serialize#registering_the_custom_object for details.
#     ValueError: Unknown metric function: rmse. Please ensure this object is passed to the `custom_objects` argument. See https://www.tensorflow.org/guide/keras/save_and_serialize#registering_the_custom_object for details.

# Train the model
# The taxifare dataset we sampled is small enough to fit in memory, so can we could use .fit() to train our model.

TRAIN_BATCH_SIZE = 1000
NUM_TRAIN_EXAMPLES = 10000 * 5  # training dataset will repeat, wrap around
NUM_EVALS = 50  # how many times to evaluate
NUM_EVAL_EXAMPLES = 10000  # enough to get a reasonable sample

# Training Dataset
trainds = create_dataset(
    pattern="../data/taxi-train*", batch_size=TRAIN_BATCH_SIZE, mode="train"
)

# Evaluation Dataset
evalds = create_dataset(
    pattern="../data/taxi-valid*", batch_size=1000, mode="eval"
).take(NUM_EVAL_EXAMPLES // 1000)

# TODO 3
%time
steps_per_epoch = NUM_TRAIN_EXAMPLES // (TRAIN_BATCH_SIZE * NUM_EVALS)
# 1 = (10000 * 5 ) // (1000 * 50)

LOGDIR = "./taxi_trained"
history = model.fit(
    x=trainds,
    validation_data=evalds,
    epochs=NUM_EVALS,
    steps_per_epoch=steps_per_epoch,
    callbacks=[TensorBoard(LOGDIR)]
)
# x specifies the input data or tf.data dataset returning a tuple of (inputs, targets). 
# Tensorboard callback to inspect Tensorboard after training.

# High-level model evaluation
model.summary()

RMSE_COLS = ["rmse", "val_rmse"]
pd.DataFrame(history.history)[RMSE_COLS].plot()

LOSS_COLS = ["loss", "val_loss"]
pd.DataFrame(history.history)[LOSS_COLS].plot()

# Making predictions with our model
# Since we have just one example, we set steps=1 (setting steps=None would also work). 
# If x is a tf.data dataset or a dataset iterator and steps is set to None, 
#   predict will run until the input dataset is exhausted.
model.predict(
    x={
        "pickup_longitude": tf.convert_to_tensor([-73.982683]),
        "pickup_latitude": tf.convert_to_tensor([40.742104]),
        "dropoff_longitude": tf.convert_to_tensor([-73.983766]),
        "dropoff_latitude": tf.convert_to_tensor([40.755174]),
        "passenger_count": tf.convert_to_tensor([3.0]),
    },
    steps=1,
)
# An example of the prediction result is "array([[12.043668]], dtype=float32"
# Making individual predictions like this is not realistic 
#   because we can't expect client code to have a model object in memory.

# Export and deploy our model
#   We'll have to export our model to a file (in a TensorFlow SavedModel format) and 
#     expect client code to instantiate the model from that exported file.
#   We have lots of ways to "serve" the model: 
#     from a web application
#     from JavaScript
#     from mobile applications, etc.

OUTPUT_DIR = "./export/savedmodel"
shutil.rmtree(OUTPUT_DIR, ignore_errors=True)
TIMESTAMP = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
EXPORT_PATH = os.path.join(OUTPUT_DIR, TIMESTAMP)

tf.saved_model.save(model, EXPORT_PATH)  # with default serving function

!saved_model_cli show \
    --tag_set serve \
    --signature_def serving_default \
    --dir {EXPORT_PATH}

!find {EXPORT_PATH}
os.environ['EXPORT_PATH'] = EXPORT_PATH

# Deploy our model to Vertex AI
PROJECT = !gcloud config list --format 'value(core.project)' 2>/dev/null
PROJECT = PROJECT[0]
BUCKET = PROJECT
REGION = "us-central1"  # us-west1-b
MODEL_DISPLAYNAME = f"taxifare-kerase-sequential{TIMESTAMP}"
print(f"MODEL_DISPLAYNAME: {MODEL_DISPLAYNAME}")

# from https://cloud.google.com/vertex-ai/docs/predictions/pre-built-containers
SERVING_CONTAINER_IMAGE_URI = (
    "us-docker.pkg.dev/vertex-ai/prediction/tf2-cpu.2-3:latest"
)
os.environ["BUCKET"] = BUCKET
os.environ["REGION"] = REGION

%%bash
# Create GCS bucket if it doesn't exist already...
exists=$(gsutil ls -d | grep -w gs://${BUCKET}/)

if [ -n "$exists" ]; then
    echo -e "Bucket exists, let's not recreate it."
else
    echo "Creating a new GCS bucket."
    gsutil mb -l ${REGION} gs://${BUCKET}
    echo "Here are your current buckets:"
    gsutil ls
fi
# Bucket exists, let's not recreate it.
!gsutil cp -R $EXPORT_PATH gs://$BUCKET/$MODEL_DISPLAYNAME

uploaded_model = aiplatform.Model.upload(
    display_name=MODEL_DISPLAYNAME,
    artifact_uri=f"gs://{BUCKET}/{MODEL_DISPLAYNAME}",
    serving_container_image_uri=SERVING_CONTAINER_IMAGE_URI,
)

MACHINE_TYPE = "n1-standard-2"
endpoint = uploaded_model.deploy(
    machine_type=MACHINE_TYPE,
    accelerator_type=None,
    accelerator_count=None,
)

instance = {
    "pickup_longitude": -73.982683,
    "pickup_latitude": 40.742104,
    "dropoff_longitude": -73.983766,
    "dropoff_latitude": 40.755174,
    "passenger_count": 3.0,
}
endpoint.predict([instance])

# Cleanup
endpoint.undeploy_all()
endpoint.delete()
```
