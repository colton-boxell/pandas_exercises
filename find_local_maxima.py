import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Input
ser = pd.Series([2,10,3,4,9,10,2,7,3])
ser.plot()
plt.show()

# Solution
dd = np.diff(np.sign(np.diff(ser)))
print(dd)
peak_locs = np.where(dd == -2)[0] + 1
print(peak_locs)