def city_decorator(fun1):
    def wrapper_fun(*args, **kwargs):
        print("Inside wrapper function")
        print(args[0])
        print(kwargs)
        fun1(*args, **kwargs)
        print("Final line from decorators")
    return wrapper_fun  # Return the wrapper function

@city_decorator
def student(name):
    print(f"I am from student {name}")

student("Ishwar")

x = 10
result = lambda x : x * x

print(result(9))

a = [2, 4, 5, 9]

x = map(lambda y: y * 2, a)

print(list(x))