import numpy as np
import pandas as pd

# Input
ser1 = pd.Series([10, 9, 6, 5, 3, 1, 12, 8, 13])
ser2 = pd.Series([1, 3, 10, 13])

# Solution 1
print([np.where(i==ser1)[0].tolist()[0] for i in ser2])

# Solution 2
print([pd.Index(ser1).get_loc(i) for i in ser2])