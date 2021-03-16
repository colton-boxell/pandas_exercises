import numpy as np
import pandas as pd

# Input
ser = pd.Series(np.random.random(20))
print(ser.head())

# Solution
print(pd.qcut(ser, q=[0, .10, .20, .3, .4, .5, .6, .7, .8, .9, 1],
	labels=['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th']).head())