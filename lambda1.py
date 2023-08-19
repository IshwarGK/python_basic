fun1 = lambda x: x * x
print(fun1(10))

list1 = [[1,2,3], [4,5], [6,7]]

list2 = [x for y in list1 for x in y]
print(list2)

fun2 = lambda z: [x for y in z for x in y]

print(fun2(list1))