import numpy as np
import pandas as pd

# Input
ser = pd.Series(['How', 'old', 'is', 'my', 'Dad?'])

# Solution
print(ser.map(lambda x:len(x)))