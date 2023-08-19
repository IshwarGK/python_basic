list1 = [1, 2, 3, 4, 5]

list2 = filter(lambda x: x % 2 == 0, list1)
list3 = [x for x in list1 if x % 2 == 0]
print(list(list2))
print(list3)