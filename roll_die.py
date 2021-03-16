import numpy as np
import pandas as pd

# Input
np.random.RandomState(100)
ser = pd.Series(np.random.randint(1,7,[100]))

# Solution
# This is rolling 2 dice
print("Top 2 Freq:", ser.value_counts())
ser[~ser.isin(ser.value_counts().index[:2])] = 'Other'
ser