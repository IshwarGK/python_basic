class Student(object):
    def __init__(self):
        self.name = "Ram"
        self.city = "Pune"
        
    def div_method(self):
        try:
            self.result = 100/1
            print(self.result)
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
        except TypeError as e:
            print(f"TypeError rased : {e}")
        except Exception as e:
            print(e)
        else:
            print("There is no any error rasied")
        finally:
            print("Finally we are happy")


sobj = Student()
sobj.div_method()