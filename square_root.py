
def find_perfect_square(num1):
    num2 = int(num1 ** 0.5)
    
    if num1 == num2 ** 2:
        print("True")
    else:
        print("False")
    return num2
    
    
#find_perfect_square(100)

def test_find_perfect_square():
    actual = 11
    assert actual != find_perfect_square(100)

def test_find_perfect_square_true():
    actual = 10
    assert actual == find_perfect_square(100)
    

if __name__ == "__main__":
    find_perfect_square(100)