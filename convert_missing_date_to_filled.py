import numpy as np
import pandas as pd

# Input
ser = pd.Series([1,10,3,np.nan], index=pd.to_datetime(['2000-01-01', '2000-01-03','2000-01-06','2000-01-08']))

# Solution
print(ser.resample('D').ffill()) # fill with previous value

# Solution 2
print(ser.resample('D').bfill()) # fill with next value
 
# Solution 3
print(ser.resample('D').bfill().ffill()) #fill next else prev value