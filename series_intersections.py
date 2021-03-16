import numpy as np
import pandas as pd

# Input
ser1 = pd.Series([1,2,3,4,5])
ser2 = pd.Series([4,5,6,7,8])

#Solution
ser_u = pd.Series(np.union1d(ser1, ser2)) # union
print(ser_u)
ser_i = pd.Series(np.intersect1d(ser1, ser2)) # intersect
print(ser_i)
print(ser_u[~ser_u.isin(ser_i)]) # interference nullification