import numpy as np
import pandas as pd

# Input
ser = pd.Series(np.arange(20) + np.random.normal(1,10,20))
print(ser)

# Solution
autocorrelations = [ser.autocorr(i).round(2) for i in range(11)]
print(autocorrelations[1:])
print('Lag having highest correlation: ', np.argmax(np.abs(autocorrelations[1:]))+1)