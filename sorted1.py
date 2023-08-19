people = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

print(people)

sorted_arr = sorted(people, key=lambda x: x['age'], reverse= False)

print(sorted_arr)