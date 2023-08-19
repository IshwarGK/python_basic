def validate_arg(fun2):
    def wrapper(*args, **kwargs):
        print("Before calling function")
        for arg in args:
            print(arg) 
            if arg < 10:
                raise TypeError("Value is Negative")
        return fun2(*args, **kwargs)
        
    return wrapper


@validate_arg
def fun1(x, y):
    return x + y

result = fun1(10, 20)
print(result)