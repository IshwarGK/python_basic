class Animal(object):
    def __init__(self) -> None:
        print("Animal is called")
        
    @staticmethod
    def add(a, b):
        print(a + b)


if __name__ == "__main__":
    obj1 = Animal()
    obj1.add(12, 12)