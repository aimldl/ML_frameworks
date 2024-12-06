* Draft: 2021-06-16 (Wed)

# Multi-Worker with Keras







## Troubleshooting

### InternalError ... group_size 6 and group_key 1 but that group has size 4

The same number of GPUs is expected in each node.

```bash
    
(node0) $ CUDA_VISIBLE_DEVICES=0,1,2 python main.py
(node1) CUDA_VISIBLE_DEVICES=0,1 python main.py
```



```bash
...  pywrap_tfe.TFE_ExecutorWaitForAllPendingNodes(self._handle)
tensorflow.python.framework.errors_impl.InternalError: Collective Op CollectiveReduce: Reduce(Add,Id) has group_size 6 and group_key 1 but that group has size 4
	Encountered when executing an operation using EagerExecutor. This error cancels all future operations and poisons their output tensors.
$
```



Change from

```bash
(node1) CUDA_VISIBLE_DEVICES=0,1 python main.py
```

to

```bash
(node1) CUDA_VISIBLE_DEVICES=0,1,2 python main.py
```

