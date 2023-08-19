
def decorator(a_func):
  
    def wrapper():
        print("Before executing function requiring decoration.")
  
        a_func()
  
        print("After executing requiring decoration.")
  
    return wrapper
  
def function():
    print("Function requiring decoration.")
  
function()
  
function = decorator(function)
  
function()
