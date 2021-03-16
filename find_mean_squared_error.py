import numpy as np
import pandas as pd

# Input
truth = pd.Series(range(10))
pred = pd.Series(range(10))+np.random.random(10)

# Solution
print(np.mean(truth-pred)**2)