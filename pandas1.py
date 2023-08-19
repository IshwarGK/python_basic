import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']}

df = pd.DataFrame(data)

print(df)

data = pd.read_csv('data.csv')

print(data.head())

print(data.describe())

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [42, 30, 35],
        'City': ['New York', 'London', 'Paris']}

filter_df = df[df['Age'] > 30]
print(filter_df)

query_result = df.query('Age > 21')
print(query_result)

print("hihihih")

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Age': [25, None, 35, None, 28],
        'City': ['New York', 'London', None, 'Paris', 'Berlin']}
df = pd.DataFrame(data)

print(df.isnull())

df_cleaned = df.dropna()
print(df_cleaned)
print("oaisdjalksjd ")
df_filled = df.fillna(10)
print(df_filled)


# Create two DataFrames
data1 = {'ID': [1, 2, 3],
         'Name': ['Alice', 'Bob', 'Charlie']}
df1 = pd.DataFrame(data1)

data2 = {'ID': [3, 2, 5],
         'Age': [25, 30, 35]}
df2 = pd.DataFrame(data2)

# Merge DataFrames based on the 'ID' column
merged_df = pd.merge(df1, df2, on='ID')
print(merged_df)

dict1 = {"name":["Ram", "Krsna", "Hari"],
         "Age":[1, 77, 1]
         }
df = pd.DataFrame(dict1)
print(df.loc)

