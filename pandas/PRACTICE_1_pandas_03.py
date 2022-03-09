import pandas as pd

# Create Series object with Dictionary.
dic = {
    1: "A rolling stone gathers no moss.",
    2: [2,4,6,8],
    3: True,
    4: 3.14
}

ser = pd.Series(dic)

print(ser)
print(ser.index)
print(ser.values)