import pandas as pd

ser = pd.Series(["NTU", "NCKU", "NCU", "NYCU"])

# Replace with specific value using list method.
ser[1] = "NFU"
print(f'We got "{ser[1]}" in:\n{ser}')

# Replace with specific value using index argument.
ser = pd.Series(["NTU", "NCKU", "NCU", "NYCU"], index=["Bes", "Dec", "Thr", "Flo"])

ser["Bes"] = "NFU"
print(f'We got "{ser["Bes"]}" in:\n{ser}')