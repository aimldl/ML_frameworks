# Lab: Classifying Structured Data using Keras Preprocessing Layers

## Summary

### Structured data

a simplified version of the PetFinder [dataset](https://www.kaggle.com/c/petfinder-adoption-prediction)

- There are both numeric and categorical columns.

| Column        | Description                        | Feature Type   | Data Type |
| ------------- | ---------------------------------- | -------------- | --------- |
| Type          | Type of animal (Dog, Cat)          | Categorical    | string    |
| Age           | Age of the pet                     | Numerical      | integer   |
| Breed1        | Primary breed of the pet           | Categorical    | string    |
| Color1        | Color 1 of pet                     | Categorical    | string    |
| Color2        | Color 2 of pet                     | Categorical    | string    |
| MaturitySize  | Size at maturity                   | Categorical    | string    |
| FurLength     | Fur length                         | Categorical    | string    |
| Vaccinated    | Pet has been vaccinated            | Categorical    | string    |
| Sterilized    | Pet has been sterilized            | Categorical    | string    |
| Health        | Health Condition                   | Categorical    | string    |
| Fee           | Adoption Fee                       | Numerical      | integer   |
| Description   | Profile write-up for this pet      | Text           | string    |
| PhotoAmt      | Total uploaded photos for this pet | Numerical      | integer   |
| AdoptionSpeed | Speed of adoption                  | Classification | integer   |

## Demonstrate the use of preprocessing layers.

The Keras preprocessing layers API allows you to build Keras-native input processing pipelines. You will use 3 preprocessing layers to demonstrate the feature preprocessing code.

- [`Normalization`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/experimental/preprocessing/Normalization) - Feature-wise normalization of the data.
- [`CategoryEncoding`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/experimental/preprocessing/CategoryEncoding) - Category encoding layer.
- [`StringLookup`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/experimental/preprocessing/StringLookup) - Maps strings from a vocabulary to integer indices.
- [`IntegerLookup`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/experimental/preprocessing/IntegerLookup) - Maps integers from a vocabulary to integer indices.

You can find a list of available preprocessing layers [here](https://www.tensorflow.org/api_docs/python/tf/keras/layers/experimental/preprocessing).

### Review

```py
# Prepare a Dataset that only yields our feature.
  feature_ds = dataset.map(lambda x, y: x[name])
# in

def get_normalization_layer(name, dataset):
  # Create a Normalization layer for our feature.
  normalizer = preprocessing.Normalization(axis=None)

# TODO
# Prepare a Dataset that only yields our feature.
  feature_ds = dataset.map(lambda x, y: x[name])# TODO: Your code goes here(lambda x, y: x[name])

  # Learn the statistics of the data.
  normalizer.adapt(feature_ds)

  return normalizer

photo_count_col = train_features['PhotoAmt']
layer = get_normalization_layer('PhotoAmt', train_ds)
layer(photo_count_col)

# returns
# <tf.Tensor: shape=(5,), dtype=float32, numpy=
#array([-0.8140722 ,  1.0590171 , -0.18970911, -0.50189066, -0.8140722 ],
#      dtype=float32)>
```

```python
type(train_ds)
#tensorflow.python.data.ops.dataset_ops.PrefetchDataset
```

Read more on https://stackoverflow.com/questions/62436302/extract-target-from-tensorflow-prefetchdataset

### Source code

```python
!pip install -q sklearn

# print the tensorflow version
tf.__version__

# import necessary libraries
import numpy as np
import pandas as pd
import tensorflow as tf

from sklearn.model_selection import train_test_split
from tensorflow.keras import layers
from tensorflow.keras.layers.experimental import preprocessing

# Use Pandas to create a dataframe
import pathlib

dataset_url = 'http://storage.googleapis.com/download.tensorflow.org/data/petfinder-mini.zip'
csv_file = 'gs://cloud-training/mlongcp/v3.0_MLonGC/toy_data/petfinder-mini_toy.csv'

tf.keras.utils.get_file('petfinder_mini.zip', dataset_url,
                        extract=True, cache_dir='.')
# TODO
# read a comma-separated values (csv) file into DataFrame
dataframe = pd.read_csv(csv_file)

# get the first n rows
dataframe.head()

# Create target variable
# In the original dataset "4" indicates the pet was not adopted.
dataframe['target'] = np.where(dataframe['AdoptionSpeed']==4, 0, 1)

# Check the output is either 0 or 1
dataframe['target'].head()
dataframe['target'].tail()

# Drop un-used columns.
dataframe = dataframe.drop(columns=['AdoptionSpeed', 'Description'])

# Double-check the output
dataframe.head()

# Split the dataframe into train, validation, and test
train, test = train_test_split(dataframe, test_size=0.2)
train, val = train_test_split(train, test_size=0.2)
print(len(train), 'train examples')
print(len(val), 'validation examples')
print(len(test), 'test examples')

# Create an input pipeline using tf.data
# A utility method to create a tf.data dataset from a Pandas Dataframe
def df_to_dataset(dataframe, shuffle=True, batch_size=32):
  dataframe = dataframe.copy()
  labels = dataframe.pop('target')
  ds = tf.data.Dataset.from_tensor_slices((dict(dataframe), labels))
  if shuffle:
    ds = ds.shuffle(buffer_size=len(dataframe))
  ds = ds.batch(batch_size)
  ds = ds.prefetch(batch_size)
  return ds

batch_size = 5
# TODO
# call the necessary function with required parameters
train_ds = df_to_dataset(train, batch_size=batch_size)

# Note: the following line results in a batch of 32, not 5
# train_ds = df_to_dataset(train, batch_size)
# So the print outputs should look like this.
# Every feature: ['Type', 'Age', 'Breed1', 'Gender', 'Color1', 'Color2', 'MaturitySize', 'FurLength', 'Vaccinated', 'Sterilized', 'Health', 'Fee', 'PhotoAmt']
# A batch of ages: tf.Tensor([60  1 36  7  9], shape=(5,), dtype=int64)
# A batch of targets: tf.Tensor([1 1 1 0 0], shape=(5,), dtype=int64)

[(train_features, label_batch)] = train_ds.take(1)
print('Every feature:', list(train_features.keys()))
print('A batch of ages:', train_features['Age'])
print('A batch of targets:', label_batch )

# Demonstrate the use of preprocessing layers.
# Numeric columns

def get_normalization_layer(name, dataset):
  # Create a Normalization layer for our feature.
  normalizer = preprocessing.Normalization(axis=None)

# TODO
  # Prepare a Dataset that only yields our feature.
  feature_ds = dataset.map(lambda x, y: x[name])

  # Learn the statistics of the data.
  normalizer.adapt(feature_ds)

  return normalizer

photo_count_col = train_features['PhotoAmt']
layer = get_normalization_layer('PhotoAmt', train_ds)
layer(photo_count_col)

# Categorical columns
# In this dataset, Type is represented as a string (e.g. 'Dog', or 'Cat'). 
def get_category_encoding_layer(name, dataset, dtype, max_tokens=None):
  # Create a StringLookup layer which will turn strings into integer indices
  if dtype == 'string':
    index = preprocessing.StringLookup(max_tokens=max_tokens)
  else:
    index = preprocessing.IntegerLookup(max_tokens=max_tokens)

# TODO
  # Prepare a Dataset that only yields our feature
  feature_ds = dataset.map(lambda x, y: x[name])

  # Learn the set of possible values and assign them a fixed integer index.
  index.adapt(feature_ds)

  # Create a Discretization for our integer indices.
  encoder = preprocessing.CategoryEncoding(num_tokens=index.vocabulary_size())

  # Apply one-hot encoding to our indices. The lambda function captures the
  # layer so we can use them, or include them in the functional model later.
  return lambda feature: encoder(index(feature))

type_col = train_features['Type']
layer = get_category_encoding_layer('Type', train_ds, 'string')
layer(type_col)

type_col = train_features['Age']
category_encoding_layer = get_category_encoding_layer('Age', train_ds,
                                                      'int64', 5)
category_encoding_layer(type_col)

# Choose which columns to use
# Earlier, you used a small batch size to demonstrate the input pipeline. Let's now create a new input pipeline with a larger batch size.
batch_size = 256
train_ds = df_to_dataset(train, batch_size=batch_size)
val_ds = df_to_dataset(val, shuffle=False, batch_size=batch_size)
test_ds = df_to_dataset(test, shuffle=False, batch_size=batch_size)

all_inputs = []
encoded_features = []

# Numeric features.
for header in ['PhotoAmt', 'Fee']:
  numeric_col = tf.keras.Input(shape=(1,), name=header)
  normalization_layer = get_normalization_layer(header, train_ds)
  encoded_numeric_col = normalization_layer(numeric_col)
  all_inputs.append(numeric_col)
  encoded_features.append(encoded_numeric_col)

# Categorical features encoded as integers.
age_col = tf.keras.Input(shape=(1,), name='Age', dtype='int64')
encoding_layer = get_category_encoding_layer('Age', train_ds, dtype='int64',
                                             max_tokens=5)
encoded_age_col = encoding_layer(age_col)
all_inputs.append(age_col)
encoded_features.append(encoded_age_col)

# Categorical features encoded as string.
categorical_cols = ['Type', 'Color1', 'Color2', 'Gender', 'MaturitySize',
                    'FurLength', 'Vaccinated', 'Sterilized', 'Health', 'Breed1']
for header in categorical_cols:
  categorical_col = tf.keras.Input(shape=(1,), name=header, dtype='string')
  encoding_layer = get_category_encoding_layer(header, train_ds, dtype='string',
                                               max_tokens=5)
  encoded_categorical_col = encoding_layer(categorical_col)
  all_inputs.append(categorical_col)
  encoded_features.append(encoded_categorical_col)

# Create, compile, and train the model
all_features = tf.keras.layers.concatenate(encoded_features)
x = tf.keras.layers.Dense(32, activation="relu")(all_features)
x = tf.keras.layers.Dropout(0.5)(x)
output = tf.keras.layers.Dense(1)(x)
model = tf.keras.Model(all_inputs, output)
# TODO
# compile the model
model.compile(optimizer='adam',              loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
              metrics=["accuracy"])

# rankdir='LR' is used to make the graph horizontal.
tf.keras.utils.plot_model(model, show_shapes=True, rankdir="LR")

# TODO
# train the model
model.fit(train_ds, epochs=10, validation_data=val_ds)

loss, accuracy = model.evaluate(test_ds)
print("Accuracy", accuracy)

# Inference on new data
model.save('my_pet_classifier')
reloaded_model = tf.keras.models.load_model('my_pet_classifier')

sample = {
    'Type': 'Cat',
    'Age': 3,
    'Breed1': 'Tabby',
    'Gender': 'Male',
    'Color1': 'Black',
    'Color2': 'White',
    'MaturitySize': 'Small',
    'FurLength': 'Short',
    'Vaccinated': 'No',
    'Sterilized': 'No',
    'Health': 'Healthy',
    'Fee': 100,
    'PhotoAmt': 2,
}

input_dict = {name: tf.convert_to_tensor([value]) for name, value in sample.items()}
predictions = reloaded_model.predict(input_dict)
prob = tf.nn.sigmoid(predictions[0])

print(
    "This particular pet had a %.1f percent probability "
    "of getting adopted." % (100 * prob)
)
```

```
This particular pet had a 76.7 percent probability of getting adopted.
```

Key point: You will typically see best results with deep learning with larger and more complex datasets. When working with a small dataset like this one, we recommend using a decision tree or random forest as a strong baseline. The goal of this tutorial is to demonstrate the mechanics of working with structured data, so you have code to use as a starting point when working with your own datasets in the future.

## Next steps

The best way to learn more about classifying structured data is to try it yourself. You may want to find another dataset to work with, and training a model to classify it using code similar to the above. To improve accuracy, think carefully about which features to include in your model, and how they should be represented.



## Overview

In this lab, you learn **how to classify structured data** (e.g. tabular data in a CSV). You use [Keras](https://www.tensorflow.org/guide/keras) to define the model, and [preprocessing layers](https://www.tensorflow.org/guide/keras/preprocessing_layers) as a bridge to map from columns in a CSV to features used to train the model.

### Learning objectives

- Load a CSV file using [Pandas](https://pandas.pydata.org/).
- Build an input pipeline to batch and shuffle the rows using [tf.data](https://www.tensorflow.org/guide/datasets).
- Map from columns in the CSV to features used to train the model using Keras preprocessing layers.
- Build, train, and evaluate a model using Keras.

## Task 1. Set up your environment

1. Enable the Vertex AI API.
2. Navigate to the [Vertex AI section of your Cloud Console](https://console.cloud.google.com/ai/platform?utm_source=codelabs&utm_medium=et&utm_campaign=CDR_sar_aiml_vertexio_&utm_content=-) and click **Enable Vertex AI API**.

## Task 2. Launch a Vertex AI Notebooks instance

1. In the Google Cloud Console, on the **Navigation Menu**, click **Vertex AI > Workbench**. Select **User-Managed Notebooks**.
2. On the Notebook instances page, click **New Notebook > TensorFlow Enterprise > TensorFlow Enterprise 2.6 (with LTS) > Without GPUs**.
3. In the **New notebook** instance dialog, confirm the name of the deep learning VM, if you don’t want to change the region and zone, leave all settings as they are and then click **Create**. The new VM will take 2-3 minutes to start.
4. Click **Open JupyterLab**. A JupyterLab window will open in a new tab.
5. You will see “Build recommended” pop up, click **Build**. If you see the build failed, ignore it.

## Task 3. Clone a course repo within your Vertex AI Notebooks instance

To clone the training-data-analyst notebook in your JupyterLab instance:

1. In JupyterLab, to open a new terminal, click the **Terminal** icon.

2. At the command-line prompt, run the following command:

   ```
   git clone https://github.com/GoogleCloudPlatform/training-data-analyst
   ```

3. To confirm that you have cloned the repository, double-click on the training-data-analyst directory and ensure that you can see its contents. The files for all the Jupyter notebook-based labs throughout this course are available in this directory.

## Task 4. Classify structured data using Keras preprocessing layers

Directory: https://github.com/GoogleCloudPlatform/training-data-analyst/tree/master/courses/machine_learning/deepdive2/introduction_to_tensorflow/labs

File: https://github.com/GoogleCloudPlatform/training-data-analyst/blob/master/courses/machine_learning/deepdive2/introduction_to_tensorflow/labs/preprocessing_layers.ipynb

1. In the notebook interface, navigate to **training-data-analyst > courses > machine_learning > deepdive2 > introduction_to_tensorflow > labs**, and open **preprocessing_layers.ipynb**. 
2. In the notebook interface, click **Edit > Clear All Outputs**.
3. Carefully read through the notebook instructions and fill in lines marked with #TODO where you need to complete the code.

**Tip:** To run the current cell, click the cell and press SHIFT+ENTER. Other cell commands are listed in the notebook UI under **Run**.

- Hints may also be provided for the tasks to guide you along. Highlight the text to read the hints (they are in white text).
- If you need more help, look at the complete solution at **training-data-analyst > courses > machine_learning > deepdive2 > introduction_to_tensorflow > solutions**, and open **preprocessing_layers.ipynb**.

