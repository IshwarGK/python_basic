def square_generator(limit):
    print("Inside generator")
    num = 1
    while num <= limit:
        print(f"In while {num}")
        yield num ** 2
        num += 1

# Using the generator to get the squares of numbers up to 5
squares = square_generator(5)
print(next(squares))
print(next(squares))
print(next(squares))

#for square in squares:
#    print(square)

