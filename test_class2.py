from class2 import A

def test_dis():
    a = A()
    result = a.dis()
    
    assert "I am A" == result
    
def test_static_method():
    result = A.static_method()
    
    assert "I am from Static method" == result
     
    