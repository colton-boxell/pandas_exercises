import numpy as np
import pandas as pd

# Input
ser = pd.Series(['Apple', 'Orange', 'Plan', 'Python', 'Money'])

# Solution
from collections import Counter
mask = ser.map(lambda x:sum([Counter(x.lower()).get(i,0) for i in list('aeiou')])>=2)
print(ser[mask])