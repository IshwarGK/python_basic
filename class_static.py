# Static Methods:
# A static method is a method that belongs to a class rather than an instance of the class. 
# It does not have access to the instance or its attributes. Static methods are defined using the @staticmethod decorator,
# and they do not receive the implicit first argument (self for instance methods) like regular methods. 
# They are typically used for utility functions or operations that are related to the class but
# do not depend on instance-specific data.

# Static Classes:
# Python does not have a specific construct for static classes like some other programming languages. 
# However, you can create a class that only contains static methods and does not have any instance-specific data or behavior.
# This can be considered as a "static class" in a conceptual sense. It is common to use a class with
# only static methods as a way to group related utility functions together.


class Animal(object):
    def __init__(self) -> None:
        print("Animal is called")
        
    @staticmethod
    def add(a, b):
        print(a + b)


if __name__ == "__main__":
    Animal().add(12, 12)