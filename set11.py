#add
#update
#delete
#extend with new same element


set1 = {1, 2, 3, 4, 5, 6}
print(set1)

print(type(set1))

list1 = [1, 2, 3, 2, 3, 4]
set2 = set(list1)
print(set2)
print(type(set2))
set1.update(set2)
print(set1)

set1.add(9)
print(set1)

set1.remove(5)
print(set1)
list1.remove(2)
print(list1)