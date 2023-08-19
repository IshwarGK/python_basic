class Student(object):
    def __init__(self) -> None:
        pass
        
    def _protected(self):
        print("Protected Method called")
    
    def __private(self):
        print("Private Method called")
        
s1 = Student()

s1._protected()
s1._Student__private()