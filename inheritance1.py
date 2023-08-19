class A:
    def disp(self):
        print("I am A")
    
class B(A):
    def disp(self):
        print("I am B")
    
class C(B):
    def disp(self):
        print("I am C")
        super()

class X:
    def disp(self):
        print("I am X")
    
class Y:
    def disp(self):
        print("I am Y")
class Z(X, Y):
    def disp(self):
        print("I am Z")
        
if __name__ == "__main__":
    a = A()
    c = C()
    super(B, c).disp()
    super(C, c).disp()
    c.disp()
    
    z = Z()
    z.disp()
    X.disp(z)
    Y.disp(z)
    
    