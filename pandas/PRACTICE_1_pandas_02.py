import pandas as pd

ser = pd.Series(["NTU", "NCKU", "NCU", "NYCU"])

# Indexing with list method.
ser[0]

# Indexing with index argument.
ser = pd.Series(["NTU", "NCKU", "NCU", "NYCU"], index=["Bes", "Dec", "Thr", "Flo"])
print(ser["Flo"])