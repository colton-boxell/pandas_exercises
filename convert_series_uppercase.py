import numpy as np
import pandas as pd

# Input
ser = pd.Series(['how','to','kick','ass?'])

# Solution 1
print(ser.map(lambda x:x.title()))

# Solution 2
print(ser.map(lambda x:x[0].upper()+x[1:]))

# Solution 3
print(pd.Series([i.title() for i in ser]))