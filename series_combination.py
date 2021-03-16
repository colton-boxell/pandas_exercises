import pandas as pd
import numpy as np
ser1 = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))

# Solution 1
df = pd.concat([ser1, ser2], axis = 1)
print(df.head(), end = "\r", flush=False)

#Solution 2
df = pd.DataFrame({'col1': ser1, 'col2': ser2})
print(df.head(), end = "\r", flush=False)