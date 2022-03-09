import pandas as pd
import numpy as np

ser = pd.Series(np.random.randint(0, 100, 5))

# 統計 with functions.
print(ser.min())
print(ser.max())
print(ser.mean())
print(ser.sum())
print(ser.nlargest(3))
print(ser.nsmallest(3))