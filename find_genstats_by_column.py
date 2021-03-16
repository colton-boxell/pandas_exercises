import numpy as np
import pandas as pd

# Solution
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

# Number of rows and columns
print(df.shape)

# Datatypes
print(df.dtypes)

# Columns per datatype
#print(df.get_dtype_counts())
print(df.dtypes.value_counts())

# Summary Statistics
df_stats = df.describe()
print(df_stats)

# Numpy array
df_arr = df.values
print(df_arr)

# List
df_list = df.values.tolist()
#print(df_list)