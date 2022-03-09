import pandas as pd

ser = pd.Series(["NTU", "NCKU", "NCU", "NYCU"])

# Using drop() function with list method.
ser = ser.drop(3)
print(ser)

# Using drop() with argument index.
ser = pd.Series(["NTU", "NCKU", "NCU", "NYCU"], index=["Bes", "Dec", "Thr", "Flo"])

ser = ser.drop("Thr")
print(ser)