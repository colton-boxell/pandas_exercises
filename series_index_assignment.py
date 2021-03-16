import pandas as pd
import numpy as np

ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
ser.name = 'alphabets'
print(ser.head())