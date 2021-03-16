import numpy as np
import pandas as pd

# Input
ser = pd.Series(np.random.randint(1,10,35))
print(ser)

# Solution
df = pd.DataFrame(ser.values.reshape(7,5))
print(df)