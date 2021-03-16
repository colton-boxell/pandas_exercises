import numpy as np
import pandas as pd

# Input
emails = pd.Series(['buying books at amazom.com', 'rameses@egypt.com', 'matt@t.co', 'narendra@modi.com'])


# Solution 1
import re
pattern ='[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,4}'
mask = emails.map(lambda x:bool(re.match(pattern,x)))
print(emails[mask])

# Solution 2
print(emails.str.findall(pattern, flags=re.IGNORECASE))

# Solution 3
print([x[0] for x in [re.findall(pattern,email) for email in emails] if len(x)>0])