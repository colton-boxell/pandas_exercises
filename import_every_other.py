import numpy as np
import pandas as pd

# Solution 1
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv', chunksize=50)
df2 = pd.DataFrame()
for chunk in df:
	df2 = df2.append(chunk.iloc[0,:])
print(df2)

# Solution 2
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv', chunksize=50)
df2 = pd.concat([chunk.iloc[0] for chunk in df], axis = 1)
df2 = df2.transpose()
print(df2)

# Solution 3
import csv
with open('BostonHousing.csv', 'r') as f:
	reader = csv.reader(f)
	out = []
	for i,row in enumerate(reader):
		if i%50 == 0:
			out.append(row)

df2 = pd.DataFrame(out[1:], columns=out[0])
print(df2.head())