class A:
    def dis(self):
        return ("I am A")
    
    @classmethod
    def cls_method(cls):
        print("I am from class method")
        
    @staticmethod
    def static_method():
        return ("I am from Static method")
        

if __name__ == "__main__":
    a = A()
    A.cls_method()
    A.static_method()
    A.dis(a)
    