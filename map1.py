list1 = [1, 2, 3, 4, 5]

def fun1(x):
    return x**3

x = map(fun1, list1)

print(list(x))