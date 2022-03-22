import numpy as np
import pandas as pd

dic = {
    "A": np.arange(1, 11),
    "B": np.arange(11, 21),
    "C": np.arange(21, 31),
    "D": np.arange(31, 41),
    "E": np.arange(41, 51)
}

df = pd.DataFrame(dic)

print(df)
print(df.head(3)) # Print the first three columns of content
print(df.tail(3)) # Print the end three columns of content