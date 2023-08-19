import pandas as pd

# Create a DataFrame using pandas with the following data:
# sql
# Copy code
# Name    Age    City
# Alice   28     New York
# Bob     24     Los Angeles
# Charlie 22     Chicago
# Now, write a Python program to add a new row with the data:
# Copy code
# Name    Age    City
# David   30     San Francisco

data = {
    "Name":["Alice", "Bob", "Charlie"],
    "Age": [ 28, 24, 22],
    "City": ['New York', 'Los Angeles', 'Chicago']
}

new_row = {"Name":"Ram", "Age":23, "City":"Vraja"}

df = pd.DataFrame(data=data)

df = df.append(new_row, ignore_index=True)

print(df)