import numpy as np
import pandas as pd

# Input
ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0,4,8,14,20]

# Solution
print(ser.take(pos))