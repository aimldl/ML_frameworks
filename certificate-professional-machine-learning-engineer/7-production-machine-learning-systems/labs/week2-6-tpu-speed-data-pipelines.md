# Lab: TPU-speed data pipelines

1. 2 hours
2. https://www.coursera.org/learn/gcp-production-ml-systems/gradedLti/UdDCM/lab-tpu-speed-data-pipelines

# Purpose

- tf.data.Dataset API
  - Learn how to **load data from GCS with the tf.data.Dataset API to feed your TPU**.
  - TPUs are very fast. 
    - The stream of training data must keep up with their training speed.

## Objectives

- Use the **tf.data.Dataset API** to load training data.
- Use **TFRecord** format to load training data efficiently from Cloud Storage.

## Tasks

1. Prepare the JupyterLab environment with Vertex Workbench
2. Create a Cloud Storage bucket
3. Open the Jupyter notebook
4. Do the hands-on with the notebook

For details about 1~3, refer to [Prepare the JupyterLab environment with Vertex Workbench](https://docs.google.com/document/d/1nibFT4N9wTIjY9ISDZhW1sgrD_o26i_l4Se3SPaOn3M/edit#).

## Related Files 

Google docs > 

```bash
git clone https://github.com/GoogleCloudPlatform/training-data-analyst
```

Soure code > [training-data-analyst](https://github.com/GoogleCloudPlatform/training-data-analyst)/[courses](https://github.com/GoogleCloudPlatform/training-data-analyst/tree/master/courses)/[machine_learning](https://github.com/GoogleCloudPlatform/training-data-analyst/tree/master/courses/machine_learning)/[deepdive2](https://github.com/GoogleCloudPlatform/training-data-analyst/tree/master/courses/machine_learning/deepdive2)/

- [production_ml](https://github.com/GoogleCloudPlatform/training-data-analyst/tree/master/courses/machine_learning/deepdive2/production_ml)/
  - [labs](https://github.com/GoogleCloudPlatform/training-data-analyst/tree/master/courses/machine_learning/deepdive2/production_ml/labs) > [tpu_speed_data_pipelines.ipynb](https://github.com/GoogleCloudPlatform/training-data-analyst/blob/master/courses/machine_learning/deepdive2/production_ml/labs/tpu_speed_data_pipelines.ipynb)
    - Each learning objective will correspond to a #TODO in the student lab notebook
  - [solutions](https://github.com/GoogleCloudPlatform/training-data-analyst/tree/master/courses/machine_learning/deepdive2/production_ml/solutions) > [tpu_speed_data_pipelines.ipynb](https://github.com/GoogleCloudPlatform/training-data-analyst/blob/master/courses/machine_learning/deepdive2/production_ml/solutions/tpu_speed_data_pipelines.ipynb)

My mirror files

- ipynb_files/

- - 

  - - Output all cleaned

  - 
    - TODO: 

## Backgrounds

### Speed test: too slow

Google Cloud  Storage is capable of great throughput but has a per-file access  penalty. Run the cell below and see that throughput is around 8 images  per second. That is too slow. Training on thousands of individual files  will not work. We have to use the **TFRecord** format to group files together.

### Recompress the images

The bandwidth savings outweight the decoding CPU cost

### Write dataset to TFRecord files

**Do not run the below cell, just read through.**

**You do not have write access to the output bucket so you  would get an error. Read through the code to familiarize yourself with  TFRecord encoding.**

```python
# Three types of data can be stored in TFRecords: bytestrings, integers and floats
# They are always stored as lists, a single data element will be a list of size 1

def _bytestring_feature(list_of_bytestrings):
  return tf.train.Feature(bytes_list=tf.train.BytesList(value=list_of_bytestrings))

def _int_feature(list_of_ints): # int64
  return tf.train.Feature(int64_list=tf.train.Int64List(value=list_of_ints))

def _float_feature(list_of_floats): # float32
  return tf.train.Feature(float_list=tf.train.FloatList(value=list_of_floats))
  

def to_tfrecord(tfrec_filewriter, img_bytes, label, height, width):  
  class_num = np.argmax(np.array(CLASSES)==label) # 'roses' => 2 (order defined in CLASSES)
  one_hot_class = np.eye(len(CLASSES))[class_num]     # [0, 0, 1, 0, 0] for class #2, roses

  feature = {
      "image": _bytestring_feature([img_bytes]), # one image in the list
      "class": _int_feature([class_num]),        # one class in the list
      
      # additional (not very useful) fields to demonstrate TFRecord writing/reading of different types of data
      "label":         _bytestring_feature([label]),          # fixed length (1) list of strings, the text label
      "size":          _int_feature([height, width]),         # fixed length (2) list of ints
      "one_hot_class": _float_feature(one_hot_class.tolist()) # variable length  list of floats, n=len(CLASSES)
  }
  return tf.train.Example(features=tf.train.Features(feature=feature))
  
print("Writing TFRecords")
for shard, (image, label, height, width) in enumerate(dataset3):
  # batch size used as shard size here
  shard_size = image.numpy().shape[0]
  # good practice to have the number of records in the filename
  filename = GCS_OUTPUT + "{:02d}-{}.tfrec".format(shard, shard_size)
  
  with tf.io.TFRecordWriter(filename) as out_file:
    for i in range(shard_size):
      example = to_tfrecord(out_file,
                            image.numpy()[i], # re-compressed image: already a byte string
                            label.numpy()[i],
                            height.numpy()[i],
                            width.numpy()[i])
      out_file.write(example.SerializeToString())
    print("Wrote file {} containing {} records".format(filename, shard_size))
```

### Read  from TFRecord Dataset

**Resume running the cells**

```python
def read_tfrecord(example):
    features = {
        "image": tf.io.FixedLenFeature([], tf.string),  # tf.string = bytestring (not text string)
        "class": tf.io.FixedLenFeature([], tf.int64),   # shape [] means scalar
        
        # additional (not very useful) fields to demonstrate TFRecord writing/reading of different types of data
        "label":         tf.io.FixedLenFeature([], tf.string),  # one bytestring
        "size":          tf.io.FixedLenFeature([2], tf.int64),  # two integers
        "one_hot_class": tf.io.VarLenFeature(tf.float32)        # a certain number of floats
    }
    # decode the TFRecord
# TODO
    example = tf.io.parse_single_example(example, features)
    
    # FixedLenFeature fields are now ready to use: exmple['size']
    # VarLenFeature fields require additional sparse_to_dense decoding
    
    image = tf.image.decode_jpeg(example['image'], channels=3)
    image = tf.reshape(image, [*TARGET_SIZE, 3])
    
    class_num = example['class']
    
    label  = example['label']
    height = example['size'][0]
    width  = example['size'][1]
    one_hot_class = tf.sparse.to_dense(example['one_hot_class'])
    return image, class_num, label, height, width, one_hot_class
    
# read from TFRecords. For optimal performance, read from multiple
# TFRecord files at once and set the option experimental_deterministic = False
# to allow order-altering optimizations.

option_no_order = tf.data.Options()
option_no_order.experimental_deterministic = False

filenames = tf.io.gfile.glob(GCS_OUTPUT + "*.tfrec")
dataset4 = tf.data.TFRecordDataset(filenames, num_parallel_reads=AUTO)
dataset4 = dataset4.with_options(option_no_order)
dataset4 = dataset4.map(read_tfrecord, num_parallel_calls=AUTO)
dataset4 = dataset4.shuffle(300)
```

```python
display_dataset = dataset4.map(lambda image, class_num, label, height, width, one_hot_class: (image, label)) display_9_images_from_dataset(display_dat
```

After the changes...

### Speed test: fast

Loading training data is not a bottleneck anymore
