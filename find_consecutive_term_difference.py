import numpy as np
import pandas as pd

# Input
ser = pd.Series([1,3,6,10,15,21,27,35])

# Solution
print(ser.diff().tolist())
print(ser.diff().diff().tolist())