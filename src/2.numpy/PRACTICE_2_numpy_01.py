import pandas as pd
import numpy as np

# Create DataFrame
df = pd.DataFrame(np.arange(1, 13).reshape(3, 4))

print(df)

print("\n")

# Create DataFrame with custom index indent.
df = pd.DataFrame(np.arange(1, 13).reshape(4, 3), index=list("瑪格麗特"), columns=list("大披薩"))

print(df)