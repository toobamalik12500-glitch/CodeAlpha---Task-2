import pandas as pd
import plotly.express as px

df = pd.read_csv("books.csv")

print(df.head())
print(df.shape)
print(df.columns)
print(df.isnull().sum())
print(df.duplicated().sum())
df["Price"] = df["Price"].str.replace(r"[^\d.]", "", regex=True)
print(df["Price"].head())
df["Price"] = df["Price"].astype(float)

print(df.info())
print(df.describe())
print(df.loc[df["Price"].idxmax()])
print(df.loc[df["Price"].idxmin()])
print(df["Rating"].value_counts())

print(df["Availability"].value_counts()) 


rating_count = df["Rating"].value_counts()

fig = px.bar(
    x=rating_count.index,
    y=rating_count.values,
    labels={"x": "Rating", "y": "Number of Books"},
    title="Books by Rating"
)

fig.show()


fig = px.histogram(
    df,
    x="Price",
    nbins=5,
    title="Price Distribution of Books"
)

fig.show()


