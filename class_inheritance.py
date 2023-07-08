class Grandparent(object):
    def __init__(self) -> None:
        print("In Grandparent")
    
    def hi(self):
        print("From Grand Hi")

class Parent(Grandparent):
    def __init__(self):
        super().__init__()
        print("In Parent")

class Child1(Parent):
    def __init__(self):
        super().__init__()
        print("In Child")
        self.hi()


class A:
    def __init__(self) -> None:
        print("In Parent")

class B(A):
    def __init__(self) -> None:
        super().__init__()
        print("In Parent")

class C(A):
    def __init__(self) -> None:
        super().__init__()
        print("In Parent")

class D(B, C):
    def __init__(self) -> None:
        super().__init__()
        print("In Parent")

if __name__ == "__main__":
    c_obj1 = Child1()
    #c_obj2 = D()
    