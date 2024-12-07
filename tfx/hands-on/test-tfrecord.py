# test-tfrecord.py
import tensorflow as tf

with tf.io.TFRecordWriter('test.tfrecord') as w:
    w.write(b'First record')
    w.write(b'Second record')
    
for record in tf.data.TFRecordDataset('test.tfrecord'):
    print(record)
