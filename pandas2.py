import pandas as pd



data = pd.read_csv("data.csv")

print(data["Founded"].mean())
print("asdasdasdad")
print(data["Number of employees"].mean())
print(data.describe)


average_salary = data["Number of employees"].mean()
print(average_salary)