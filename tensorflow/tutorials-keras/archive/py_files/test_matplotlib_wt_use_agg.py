# test_matplotlib.py
#
# A command to run this script on Docker is:
#
#  $ python3 test_matplotlib.py
#
#   Last updated on 2018-09-21 (Fri)
#   First written on 2018-09-21 (Fri)
#   Written by Tae-Hyung "T" Kim, Ph.D.

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.plot([1,2,3])
plt.savefig('myfig')
