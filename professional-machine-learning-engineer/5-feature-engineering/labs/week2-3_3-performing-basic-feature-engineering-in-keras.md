# Lab: Performing Basic Feature Engineering in Keras

## Summary

- I've added some additional comments in the following lines.

- Each learning objective will correspond to a #TODO in the student lab notebook

## Introduction

- [training-data-analyst > courses > machine_learning > deepdive2 > **feature_engineering**  > labs](https://github.com/GoogleCloudPlatform/training-data-analyst/tree/master/courses/machine_learning/deepdive2/feature_engineering/labs)
- [training-data-analyst > courses > machine_learning > deepdive2 > **feature engineering > solutions**](https://github.com/GoogleCloudPlatform/training-data-analyst/tree/master/courses/machine_learning/deepdive2/feature_engineering/solutions)
  - [3_keras_basic_feat_eng.ipynb](https://github.com/GoogleCloudPlatform/training-data-analyst/blob/master/courses/machine_learning/deepdive2/feature_engineering/solutions/3_keras_basic_feat_eng.ipynb)


### Learning objectives

1. Create an input pipeline using tf.data
2. Engineer features to create categorical, crossed, and numerical feature columns

## Source code/Excerpts from the solution `.ipynb`

### Lab Task 1: Create an input pipeline using tf.data

- Wrap the dataframes with [tf.data](https://www.tensorflow.org/guide/datasets). 
- This will enable us to use feature columns as a bridge to map from the columns in the Pandas dataframe to features used to train the model.

```python
# A utility method to create a tf.data dataset from a Pandas Dataframe
# TODO 1a
def df_to_dataset(dataframe, shuffle=True, batch_size=32):
    dataframe = dataframe.copy()
    labels = dataframe.pop('median_house_value')
    ds = tf.data.Dataset.from_tensor_slices((dict(dataframe), labels))
    if shuffle:
        ds = ds.shuffle(buffer_size=len(dataframe))
    ds = ds.batch(batch_size)
    return ds
```

Shufful the training dataset while the validation dataset should not be shuffled.

```python
train_ds = df_to_dataset(train)
val_ds = df_to_dataset(val, shuffle=False)
```

Equivalently, the verbose version is below.

```python
batch_size = 32
train_ds = df_to_dataset(train, shuffle=True, batch_size=batch_size)
val_ds = df_to_dataset(val, shuffle=False, batch_size=batch_size)
```

Let's check out the first batch of feature and label.

```python
# TODO 1b
for feature_batch, label_batch in train_ds.take(1):
    print('Every feature:', list(feature_batch.keys()))
    print('A batch of households:', feature_batch['households'])
    print('A batch of ocean_proximity:', feature_batch['ocean_proximity'])
    print('A batch of targets:', label_batch)
```

Specify the numeric columns.

```python
# Let's create a variable called `numeric_cols` to hold only the numerical feature columns.
# TODO 1c
numeric_cols = ['longitude', 'latitude', 'housing_median_age', 'total_rooms',
                'total_bedrooms', 'population', 'households', 'median_income']
```

```python
# 'get_scal' function takes a list of numerical features and returns a 'minmax' function
# 'Minmax' function itself takes a 'numerical' number from a particular feature and return scaled value of that number.
# Scalar def get_scal(feature):
# TODO 1d
def get_scal(feature):
    def minmax(x):
        minimum = train[feature].min()
        maximum = train[feature].max()
        return (x - minimum)/(maximum-minimum)
        return(minmax)
```

For each numeric column, we append the result into `feature_columns`.

```python
feature_columns =[]
for header in numeric_cols:
    print(header)
```

```
longitude
latitude
housing_median_age
total_rooms
total_bedrooms
population
households
median_income
```

The numeric columns are normalized with min_max.

```python
# TODO 1e
feature_columns = []
for header in numeric_cols:
    scal_input_fn = get_scal(header)
    feature_columns.append(fc.numeric_column(header,
                                             normalizer_fn=scal_input_fn))
```



In the solution, `dict()` is applied twice to features. Why?

```python
# TODO 1f
def test_input_fn(features, batch_size=256):
    """An input function for prediction."""
    # Convert the inputs to a Dataset without labels.
    return tf.data.Dataset.from_tensor_slices(dict(features)).batch(batch_size)

test_predict = test_input_fn(dict(test_data))
```

So I got rid of the `dict()` function in `test_input_fn`.

```python
# TODO 1f -- Your code here
def test_input_fn(features, batch_size=256):
    return tf.data.Dataset.from_tensor_slices(features).batch(batch_size)

test_predict = test_input_fn(dict(test_data))
```

### Lab Task 2: Engineer features to create categorical and numerical features



<img src='images/xxx'>



<img src='images/xxx'>



<img src='images/xxx'>



