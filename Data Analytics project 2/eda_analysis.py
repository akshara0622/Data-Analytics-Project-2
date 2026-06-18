import pandas as pd

df = pd.read_excel("Dataset.xlsx", engine="openpyxl")
print(df.head())      
print(df.info())      
print(df.shape)      
print(df.describe())
print(df.isnull().sum())
print("Duplicate Rows:", df.duplicated().sum())
print("Average Total Price:", df["TotalPrice"].mean())
print("Median Total Price:", df["TotalPrice"].median())
Q1 = df["TotalPrice"].quantile(0.25)
Q3 = df["TotalPrice"].quantile(0.75)
IQR = Q3 - Q1

outliers = df[
    (df["TotalPrice"] < Q1 - 1.5 * IQR) |
    (df["TotalPrice"] > Q3 + 1.5 * IQR)
]

print("Number of outliers:", len(outliers))
import matplotlib.pyplot as plt

plt.hist(df["TotalPrice"], bins=20)
plt.title("Distribution of Total Price")
plt.xlabel("Total Price")
plt.ylabel("Frequency")
plt.show()