def get_prime_number(num):
    for i in range(2, int(num/2)):
        if num % i == 0:
            
            print(f"Not prime number can be devided {i}")
            return
    print("Prime number")


get_prime_number(91)