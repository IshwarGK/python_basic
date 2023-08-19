def write_file():
    with open("test.txt", "w") as file:
        file.write("Hi there 1 \n")
        file.write("Welcome to file 2 \n")
        
    with open("test.txt", "a") as file:
        file.write("Are you from Pune \n")
        file.write("What about Mumbai \n")

write_file()

def read_file():
    with open("test.txt", 'r') as file:
        conetent = file.read()
        print(conetent)
        
    with open("test.txt", "r") as file:
        line = file.readline()
        while line:
            print(line)
            line = file.readline()
            

read_file()