# In Python, a class method is a method that belongs to the class rather than an instance of the class. 
# It is defined using the @classmethod decorator and takes the class itself (cls) as the first parameter instead ofthe instance (self).
# Class methods are used to perform operations or
# access class-level attributes that are shared by all instances of the class.

class Employee(object):
    country = 'India'
    def __init__(self) -> None:
        self.name = 'name'
        self.city = 'city'
    
    @classmethod
    def print_details(cls, name, city):
        name = name
        city = city
        print(name)
        
        
obj1 = Employee.print_details('Ishwar', 'Pune')
#print(obj1.name)