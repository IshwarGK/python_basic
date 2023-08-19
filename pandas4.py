import pandas as pd
import numpy as np

arr1 = np.array([[12, 23, 24, 45], [1, 2, 3, 4]])
print(arr1)

df = pd.DataFrame(arr1, columns=['A', 'B', 'C', 'D'])
print(df)

# pandas average
dict1 = {
    "Name": ["Ram", "Krsna", "Ram"],
    "Age": [12, 13, 16]
}

df = pd.DataFrame(dict1)
val = df.groupby("Name")
print(val.mean())