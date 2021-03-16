import numpy as np
import pandas as pd

# Input
ser1 = pd.Series(range(5))
ser2 = pd.Series(list('abcde'))

# Solution
# Vertical
print(ser1.append(ser2))
# Horizontal
df = pd.concat([ser1,ser2], axis=1)
print(df)