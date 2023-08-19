import pandas as pd

df = pd.read_csv("data.csv")

#print(df["Organization Id"])

dict1 = {
    "name":["Ram", "Krishana", "Hari"],
    "city":["Pune", None, "Pune"],
    "Age":[11, 12, 13]
}

df = pd.DataFrame(dict1)
selected_row = df[df["Age"] > 11]
print(selected_row)
# print(df)
# print(df.fillna("Mumbai"))
# print(df.dropna())
# print(df.notnull())

data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)

print(df.iloc[:,0])
print(df.iloc[0, 0])
print(df.loc[:,'A'])
