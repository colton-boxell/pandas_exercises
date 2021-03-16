#Inputs
import numpy as np
import pandas as pd
mylist = list('abcdefghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))

#Solution
ser1 = pd.Series(mylist)
ser2 = pd.Series(myarr)
ser3 = pd.Series(mydict)

print(ser1.head(), end = "\r", flush=False)
print(ser2.head(), end = "\r", flush=False)
print(ser3.head(), end = "\r", flush=False)