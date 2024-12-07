

# 3 Data Ingestion
## Concepts for Data Ingestion

Convert the datasets into TFRecord files containing the data represented as `tf.Example` data structures.

`tf.Example` is the data structure representing every data row within TFRecord.

### TFRecord

TFRecord is a lightweight format optimized for streaming large datasets.

```python
import tensorflow as tf

with tf.io.TFRecordWriter('text.tfrecord') as w:
    w.write(b'First record')
    w.write(b'Second record')
    
for record in tf.data.TFRecordDataset('test.tfrecord'):
    print(record)
    
tf.Tensor(b'First record', shape=(), dtype=string)
tf.Tensor(b'Second record', shape(), dtype=string)
```

If TFRecord files contain `tf.Example` records, each record contains one or more features that would represent the columns in our data.

### Ingesting Local Data Files

#### Converting comma-separated data to tf.Example

TFX provides functionality to read and convert CSV files to `tf.Example` data structures.

The ingestion of a folder containing the CSV data of our example project

```python
import os
from tfx.components import CsvExampleGen
from tfx.utils.dsl_utils import external_input

base_dir = os.getcwd()
data_dir = os.path.join(os.pardir, 'data')
examples = external_input(os.path.join(base_dir, data_dir))
example_gen = CsvExampleGen(input=examples)

context.run(example_gen)
```

## Folder Structure

### Importing existing TFRecord Files

```python
import os
from tfx.components import ImportExampleGen
from tfx.utils.dsl_utils import external_input

base_dir = os.getcwd()
data_dir = os.path.join(os.pardir, 'tfrecord_data')
examples = external_input(os.path.join(base_dir, data_dir))
example_gen = ImportExampleGen(input=examples)

context.run(example_gen)
```

#### Converting Parquet-serialized data to tf.Example

```python
from tfx.components import FileBasedExampleGen
from tfx.components.example_gen.custom_executors import parquet_executor
from tfx.utils.dsl_utils import external_input

# revisit: parquet_dir_path is not specified?
examples = external_input(parquet_dir_path)
example_gen = FileBasedExampleGen(
    input=examples,
    executor_class=parquet_executor.Executor)  # override the executor
```

#### Converting Avro-serialized data to tf.Example

```python
from tfx.components import FileBasedExampleGen
from tfx.components.example_gen.custom_executors import avro_executor
from tfx.utils.dsl_utils import external_input

examples = external_input(avro_dir_path)
examplg_gen = FileBasedExampleGen(
    input=examples,
    executor_class=avro_executor.Executor)  #override the executor
```

#### Converting your custom data to TFRecord data structures

TODO: 

### Ingesting Remote Data Files
### Ingesting Data Directly from Databases
## Data Preparation
### Splitting Datasets
### Spanning Datasets
### Versioning Datasets
## Ingestion Strategies
### Structured Data
### Text Data for Natural Language Problems
### Image Data for Computer Vision Problems
## Summary

