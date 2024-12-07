



Test Faster R-CNN



```bash
$ python tools/test.py configs/DOTA/faster_rcnn_RoITrans_r50_fpn_1x_dota.py \
 work_dirs/faster_rcnn_RoITrans_r50_fpn_1x_dota/epoch_12.pth \ 
 --out work_dirs/faster_rcnn_RoITrans_r50_fpn_1x_dota/results.pkl
```

Problem1

When I opened a new terminal, `ModuleNotFoundError` has occured.

```bash
sh-4.2$ python tools/test.py configs/DOTA/faster_rcnn_RoITrans_r50_fpn_1x_dota.py work_dirs/faster_rcnn_RoITrans_r50_fpn_1x_dota/epoch_12.pth --out work_dirs/faster_rcnn_RoITrans_r50_fpn_1x_dota/results.pkl
Traceback (most recent call last):
  File "tools/test.py", line 6, in <module>
    import mmcv
ModuleNotFoundError: No module named 'mmcv'
sh-4.2$
```

Solution1

`mmcv` is installed in Conda virtual environment `pytorch_p36`. Activating the environment resolves the problem.

```bash
sh-4.2$ source activate pytorch_p36
(pytorch_p36) sh-4.2$
```

Problem2

```
$ python tools/test.py configs/DOTA/faster_rcnn_RoITrans_r50_fpn_1x_dota.py work_dirs/faster_rcnn_RoITrans_r50_fpn_1x_dota/epoch_12.pth --out work_dirs/faster_rcnn_RoITrans_r50_fpn_1x_dota/results.pkl
Traceback (most recent call last):
  File "tools/test.py", line 12, in <module>
    from mmdet.apis import init_dist
  File "/home/ec2-user/SageMaker/AerialDetection/mmdet/apis/__init__.py", line 2, in <module>
    from .train import train_detector
  File "/home/ec2-user/SageMaker/AerialDetection/mmdet/apis/train.py", line 12, in <module>
    from mmdet import datasets
  File "/home/ec2-user/SageMaker/AerialDetection/mmdet/datasets/__init__.py", line 16
    from .ROKSI2020 import ROKSI2020, ROKSI2020Dataset_v3x`
                                                          ^
SyntaxError: invalid syntax
```

Solution2

```bash
from .ROKSI2020 import ROKSI2020, ROKSI2020Dataset_v3x`
```

The trailing ` has been deleted.

```bash
from .ROKSI2020 import ROKSI2020, ROKSI2020Dataset_v3x
```



Problem 3

```bash
$ python tools/test.py configs/DOTA/faster_rcnn_RoITrans_r50_fpn_1x_dota.py work_dirs/faster_rcnn_RoITrans_r50_fpn_1x_dota/epoch_12.pth --out work_dirs/faster_rcnn_RoITrans_r50_fpn_1x_dota/results.pkl
Traceback (most recent call last):
  File "tools/test.py", line 12, in <module>
    from mmdet.apis import init_dist
  File "/home/ec2-user/SageMaker/AerialDetection/mmdet/apis/__init__.py", line 2, in <module>
    from .train import train_detector
  File "/home/ec2-user/SageMaker/AerialDetection/mmdet/apis/train.py", line 12, in <module>
    from mmdet import datasets
  File "/home/ec2-user/SageMaker/AerialDetection/mmdet/datasets/__init__.py", line 16, in <module>
    from .ROKSI2020 import ROKSI2020, ROKSI2020Dataset_v3x
ImportError: cannot import name 'ROKSI2020Dataset_v3x'
$
```

