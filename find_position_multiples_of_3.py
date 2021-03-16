import numpy as np
import pandas as pd

# Input

ser = pd.Series(np.random.randint(1,10,7))
ser

# Solution
print(ser)
np.argwhere(ser % 3==0)