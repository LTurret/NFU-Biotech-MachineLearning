import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(1, 13).reshape(3, 4))

# DataFrame manipulations.

print(df)
print(f"DataFrame shapes: {df.shape}")
print(f"df.keys(): {df.keys()}")
print(f"df[0:1], first row's content:\n{df[0:1]}")
print(f"df[1:0], first column's content:\n{df[0]}")
print(f"df's 1st row, 4th column content:\n{df[3][0]}")

# Hint: df[row][column]