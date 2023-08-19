import pytest
from functools import reduce

def fun3():
    list1 = [1, 2, 3, 4, 5]

    val = sum(list1)
    print(val)

    val = reduce(lambda x, y: x + y, list1)
    print(val)

def fun1(list1):
    val = reduce(lambda x,y: x * y, list1)
    return val

def test_fun1():
    result = 120
    assert result == fun1(list1=[1, 2, 3, 4, 5])
    
def test_fun1_negative_case():
    result = 10
    assert result != fun1(list1=[12, 13, 14])
    
if __name__ == "__main__":
    pytest.main()