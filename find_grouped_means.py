import numpy as np
import pandas as pd

# Input 
fruit = pd.Series(np.random.choice(['apple', 'banana', 'carrot'],10))
print(fruitsubl)
weights = pd.Series(np.linspace(1,10,10))
print(weights)

# Solution
print(weights.groupby(fruit).mean())