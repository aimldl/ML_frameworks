* Draft: 2020-10-21 (Wed)

# Install the Baseline Aerial Detection for Ubuntu

## Reference

* 



```bash
$ cd /home/ec2-user/SageMaker/AerialDetection/DOTA_devkit
$ python
Python 3.6.10 |Anaconda, Inc.| (default, Jan  7 2020, 21:14:29) 
[GCC 7.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from DOTA import DOTA
>>> 
```

그러면 traincoco.json, valcoco.json을 얻을 수 있어요

https://dacon.io/competitions/official/235644/codeshare/1710?page=1&dtype=recent&ptype=pub

```bash
$ python my_arirang2coco.py 
/home/ec2-user/SageMaker/AerialDetection
800 800
$
```



```bash
$ ls images/ | wc -l
800
$
```

