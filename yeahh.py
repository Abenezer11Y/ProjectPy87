import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('IMDB Dataset.csv')

print(df.head(3))
print(df.tail(3))

if df.isnull().values.any() == True:
    print("There is a null value")
elif df.isnull().values.any() == False:
    print("There isn't any null values")

print(df.iloc[41:76])
print(f"The movie with the best rating: \n{df.loc[df['No_of_Votes'].idxmax()]}")

sns.boxplot(x=df['IMDB_Rating'], y=df['Runtime'], color="green")
plt.show()

print(df['col1'].corr(df['col2']))

sns.countplot( df['IMDB_Rating'])
plt.show()