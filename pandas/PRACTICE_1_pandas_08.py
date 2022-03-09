import pandas as pd
import numpy as np

ser = pd.Series(np.random.randint(0, 100, 5))

# 篩選 with Series syntax.
print(ser)
print(ser<60)
print(ser[ser<60])
print(ser[(ser>25) & (ser<60)])