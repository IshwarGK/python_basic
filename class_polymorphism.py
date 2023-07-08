class Animal(object):
    def make_sound(self):
        print("pass")

class Cat(Animal):      
    def make_sound(self):
        print("Miau Miau")
        
class Dog(Animal):
    def make_sound(self):
        print("Bhoo Bhoo")
    
    
if __name__ == "__main__":
    obj1 = Cat()
    obj1.make_sound()