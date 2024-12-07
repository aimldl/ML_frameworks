# Quiz: Designing high-performance ML systems

**80(?)% --> 100%**

Question 1

If each of your examples is large in terms of size and requires parsing, and your model is relatively simple and shallow, your model is likely to be:

```
Hmm... I/O bound vs. CPU-bound?
- I think parsing requires more computations on the CPU side.
- I initially selected I/O bound and meant to give more CPU power along with the input pipeline.
- The problem here is the input pipline itself may not be sufficient. We need more CPU!
- The problem with the 2nd choice (or CPU-bound) is the solution is not to increase the CPU power, but to use accelerators only!

Should I go with CPU-bound? No. the question says a LARGE dataset. The parsing part may not be complex that requires a lot of CPU power. So go with I/O bound.
```



- [x] I/O bound, so you should look for ways to store data more efficiently and ways to parallelize the reads.
- [ ] CPU-bound, so you should use GPUs or TPUs.
- [ ] Latency-bound, so you should use faster hardware

```
Correct! Your ML training will be I/O bound if the number of inputs is large or heterogeneous (requires parsing) or if the model is so small that the compute requirements are trivial. This also tends to be the case if the input data is on a storage system with low throughput. If you are I/O bound, look at storing the data more efficiently, storing the data on a storage system with higher throughput, or parallelizing the reads. Although it is not ideal, you might consider reducing the batch size so that you are reading less data in each step.
```



Question 2

For the fastest I/O performance in TensorFlow… (check all that apply)

- [x] Read TF records into your model.
- [x] Read in parallel threads.
- [ ] Optimize TensorFlow performance using the Profiler.
- [x] Prefetch the data

```
Initially selected all! But unchecked the 3rd one with the following logic. But I was wrong. >.<
- A profiler can help identify the bottole is either I/O bound or CPU bound. It doesn't make the I/O performance fast.
```

```
1. Read TF records
Correct. This is one of the correct answers. dataset = tf.data.TFRecordDataset(...) TF Records are set for fast, efficient, batch reads, without the overhead of having to parse the data in Python.

2. Read in parallel threads
This is one of the correct answers. dataset = tf.data.TFRecordDataset(files, num_parallel_reads=40) When you're dealing with a large dataset sharded across Cloud Storage, you can speed up by reading multiple files in parallel to increase the effective throughput. You can use this feature with a single option to the TFRecordDataset constructor called num_parallel_reads.

4. Prefetch the data
Correct. This is one of the correct answers. dataset.prefetch decouples the time data is produced from the time it is consumed. It prefetches the data into a buffer in parallel with the training step. This means that we have input data for the next training step before the current one is completed.
```



Question 3

What does high-performance machine learning determine?



- [x] Time taken to train a model
- [ ] Reliability of a model
- [ ] Deploying a model
- [ ] Training a model

### 

Question 4

Which of the following indicates that ML training is CPU bound?



- [ ] If I/O is complex, but the model involves lots of complex/expensive computations.
- [ ] If you are running a model on powered hardware.
- [x] If I/O is simple, but the model involves lots of complex/expensive computations.
- [ ] If you are running a model on accelerated hardware.
