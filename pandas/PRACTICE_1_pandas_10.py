import pandas as pd

# Create DataFrame with Dictionary
dic = {
    1: list("bird"),
    2: [2,4,6,8],
    3: True,
    4: 3.141
}

df = pd.DataFrame(dic)

print(df)
print(df.T)