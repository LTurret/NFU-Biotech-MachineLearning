import pandas as pd

ser1 = pd.Series(["NTU", "NCKU"])
ser2 = pd.Series(["NCU", "NYCU"])

# Connect two different Series using append()
ser = ser1.append(ser2)
print(ser)

# append() argument; ignore_index makes sense.
ser = ser1.append(ser2, ignore_index=True)
print(ser)