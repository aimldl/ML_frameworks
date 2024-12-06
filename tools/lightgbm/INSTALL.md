* Draft: 2021-03-10 (Wed)

# Installation Guide



## Python

```bash
$ pip install lightgbm
```

To verify the installation, run the following command.

* In python

```python
import lightgbm as lgb
```

* In terminal

```bash
$ python -c 'import lightgbm as lgb'
```

## Linux

1. Install [CMake](https://cmake.org/).

2. Run the following commands:

   ```
   git clone --recursive https://github.com/microsoft/LightGBM
   cd LightGBM
   mkdir build
   cd build
   cmake ..
   make -j4
   ```

**Note**: glibc >= 2.14 is required.

```bash

```

