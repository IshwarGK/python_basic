list1 = ["Ishwar", "Ram", "Jayshri"]
list2 = [30, 1, 23]


result = zip(list1, list2)
result_list = list(result)
print(result_list)

names, ages = zip(*result_list)

print(names)
print(ages)