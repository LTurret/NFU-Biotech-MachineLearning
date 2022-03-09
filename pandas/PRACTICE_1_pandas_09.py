import pandas as pd
import numpy as np

ser = pd.Series(np.random.randint(0, 100, 5))

# Sort with Series functions.
print(ser)
print(ser.sort_values())
print(ser.sort_values(ascending=False))
print(ser.sort_index())
print(ser.sort_index(ascending=False))