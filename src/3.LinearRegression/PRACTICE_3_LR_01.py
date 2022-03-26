import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

df = pd.read_csv("../../data/data.csv")

print(df.isnull().values.sum()) # Check evey key if it has Null, summaries them, calculates as number eventually
print(f"Shape: {df.shape}")
print(f"Variables: {df.keys()}")
print(f"The first data content:\n{df.iloc[0,::]}")
print(f'The first predicted goal: {df["Weight"][0]}') # I am not sure is this operation match the title, I think it's not

# Setup figures
plt.scatter(df.Height, df.Weight, color="b")
plt.title("Original graph")
plt.xlabel("Height")
plt.ylabel("Weight")
plt.savefig(f"./pictures/Original_Data.jpg")
plt.clf()

# Prepare train data and test data for model
x = df.drop("Weight", axis=1)
y = df["Weight"]

train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.2, random_state=42)
print(f"Original data shape: {df.shape}")
print(f"Tranning data shape: {train_x.shape}")
print(f"Testing data shape: {test_x.shape}")

# Trainning
model = LinearRegression()
model.fit(train_x, train_y)
print(f"Coefficients: {model.coef_}")
print(f"Intercept: {model.intercept_}")

# Import test data to model for predictions and calculate MSE
pred = model.predict(test_x)
score = mean_squared_error(pred, test_y)
print(f"MSE: {score}")

# Linear regression
plt.scatter(x, y, color="b")
plt.plot(test_x.values.tolist(), pred, color="r")
plt.title("Regression graph")
plt.xlabel("Height")
plt.ylabel("Weight")
plt.savefig(f"./pictures/Regression_Data.jpg")