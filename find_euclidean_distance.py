import numpy as np
import pandas as pd

# Input
p = pd.Series([1,2,3,4,5,6,7,8,9,10])
q = pd.Series([10,9,8,7,6,5,4,3,2,1])

# Solution
print(sum((p-q)**2)**0.5)
print(np.linalg.norm(p-q))
