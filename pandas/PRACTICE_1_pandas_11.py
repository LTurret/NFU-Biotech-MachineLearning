import pandas as pd
import numpy as np

# np.reshape() and describe()
df = pd.DataFrame(np.random.randint(0, 100, 5).reshape(3, 4))

print(df)
print(df.describe())

print(df.T)
print((df.T).describe())