import numpy as np
import pandas as pd
import time

# Input
state = np.random.RandomState(100)
ser = pd.Series(state.normal(10,5,25))

#Solution
print(np.percentile(ser, q=[0, 25, 50, 75, 100]))

# repeat for many normal distributions, as many as there are random states
def RandomState_Assesment(e):
	start_time = time.time()
	for n in range(e):
		state_n = np.random.RandomState(100)
		ser = pd.Series(state.normal(10,5,25))
		with open("epoch_%s" % e, "a") as ep:
			line = np.array2string(np.percentile(ser, q=[0, 25, 50, 75, 100]))
			ep.write(line)
	print("----%s seconds ----" % (time.time()-start_time))

epochs = [10, 100, 1000, 10000, 100000, 1000000]
for epoch in epochs:
	RandomState_Assesment(epoch)