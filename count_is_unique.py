import numpy as np
import pandas as pd

# Input
ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))

#Solution
print(ser, end="\r", flush=False)
#series looks like dna could be written with it
print(ser.value_counts(), end="\r", flush=False)