def outerfun(param1):
    def innerfun(param2):
        return param1 + param2
    
    return innerfun
    
callingfun = outerfun(10)
result = callingfun(20)

print(result)


def validate_param(fun1):
    def wrapper(*args, **kwargs):
        sum1 = 0
        for arg in args: 
            if isinstance(arg, int):
                sum1 += arg
            else:
                print("Input params are not integers")
                return False
        print("Inputs are integer")
        return sum1
    return wrapper

@validate_param
def add_int(num1, num2):
    return num1 + num2

print(add_int(10, 20))

