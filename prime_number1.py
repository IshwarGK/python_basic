def multi(num1):
    if num1 <= 1:
        return 1
    
    return num1 * multi(num1-1)

print(multi(5))

def fibbo(num1):
    a = 0
    b = 1
    for i in range(num1):
        print(a)
        a, b = b, a+b
fibbo(8)