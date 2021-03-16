import numpy as np
import pandas as pd

# Solution
x = input('10 Weekends starting from when? -Must be YYYY-DD-MM format -')
ser = pd.Series(np.random.randint(1,10,10),pd.date_range(x,periods=10,freq='W-SAT'))
print(ser)