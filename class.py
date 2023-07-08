class add():
    def fun1(self, a, b):
        print(a+b)

obj1 = add()
obj1.fun1(10,12)

class fibbo:
    def __init__(self, count, n):
        a = 0
        b = 1
        for i in range(count):
            print (a)
            a, b = b, a + b

#obj1 = fibbo(10)


class choose_class(add, fibbo):
    def __init__(self, a, b) -> None:
        super().__init__(a, b)

    
obj1 = choose_class(10, 5)

