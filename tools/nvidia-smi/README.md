* Draft: 2021-06-03 (Thu)

# How to Save `nvidia-smi` Output

## Reference

Google search: how to save nvidia-smi output

* ### [Capture vGPU performance data in csv format using nvidia-smi](https://forums.developer.nvidia.com/t/capture-vgpu-performance-data-in-csv-format-using-nvidia-smi/161846)

* > #### Intent
  >
  > Capture the GPU utilization, GPU memory utilization, Total GPU memory, GPU memory free, GPU memory used performance statistics to a CSV formatted file.
  >
  > To capture the GPU utilization for all vGPUs enabled virtual machines on PCIe ID "0000:09:00.0" and display to the console:
  >
  > ```bash
  > root@nvgrid:~ # nvidia-smi --query-gpu=utilization.gpu,utilization.memory,memory.total,memory.free,memory.used --format=csv --id=0000:09:00 -l 1
  > ```
  >
  > To redirect the output to a file:
  >
  > ```bash
  > root@nvgrid:~ # nvidia-smi --query-gpu=utilization.gpu,utilization.memory,memory.total,memory.free,memory.used --format=csv --id=0000:09:00 -l 1 -f ./GPU-09-stats.csv
  > ```
  >
  > The data will be captured in one second intervals and written to the file.

## Example

Say a Keras source code is executed.

```bash
$ python 6_imdb_movie_review-bidirectional_lstm-keras.py
```

We can observe the GPU performance such as GPU utilization, used memory and so on.

```bash
$ watch -n 1 nvidia-smi
```

We can save the observation to a file with the `-f` option.

```bash
$ nvidia-smi -f gpu_performance.csv --format=csv -l 1 --query-gpu=utilization.gpu,utilization.memory,memory.total,memory.free,memory.used   
$
```

The saved file looks like

```bash
$ cat gpu_performance.csv
utilization.gpu [%], utilization.memory [%], memory.total [MiB], memory.free [MiB], memory.used [MiB]
54 %, 3 %, 16160 MiB, 604 MiB, 15556 MiB
0 %, 0 %, 16160 MiB, 15666 MiB, 494 MiB
0 %, 0 %, 16160 MiB, 15666 MiB, 494 MiB
0 %, 0 %, 16160 MiB, 15666 MiB, 494 MiB
54 %, 3 %, 16160 MiB, 604 MiB, 15556 MiB
  ..
$
```

The GPU utilization can be extracted with the `awk` command as follows.

```bash
$ awk '{print $1;}' gpu_performance.csv
utilization.gpu
54
0
0
0
54
  ...
$
```

To get rid of `0`,  run:

```bash
$ awk '{print $1;}' gpu_performance.csv | grep -v '0'
utilization.gpu
54
54
54
  ...
$
```

To get rid of `utilization.gpu`,  run:

```bash
$ awk '{print $1;}' gpu_performance.csv | egrep -v "0|utilization"
54
54
54
  ...
$
```

