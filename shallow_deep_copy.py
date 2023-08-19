import copy

a = [1, 2, 3, 4, 5]

b = copy.deepcopy(a)

print(a)
print(b)

b[1] = 44

print(a)
print(b)
print(a is b)


a = [1, 2, 3, 4, 5]

b = copy.copy(a)
print(a)
print(b)

b[1] = 44

print(a)
print(b)
print(a is b)