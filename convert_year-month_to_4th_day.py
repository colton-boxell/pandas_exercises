# import numpy as np
import pandas as pd

# Input
ser = pd.Series(['Jan 2010', 'Feb 2011', 'Mar 2012'])

# Solution 1
from dateutil.parser import parse
ser_ts = ser.map(lambda x:parse(x))
ser_datestr = ser_ts.dt.year.astype('str') + '-' + ser_ts.dt.month.astype('str') + '-' + '04'
print([parse(i).strftime('%Y-%m-%d') for i in ser_datestr])

# Solution 2
print(ser.map(lambda x: parse('04' + x)))