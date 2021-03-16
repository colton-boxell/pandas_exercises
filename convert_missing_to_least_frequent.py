import numpy as np
import pandas as pd

# Input
my_str = 'dbc deb abed gade'

# Solution
ser = pd.Series(list(my_str))
freq = ser.value_counts()
print(freq)
least_freq = freq.dropna().index[-1]
print("".join(ser.replace(' ', least_freq)))