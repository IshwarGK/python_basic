def counter():
    count1 = 0
    while count1 <= 10:
        yield count1 + 1
        count1 += 1
    
gen = counter()

print(next(gen))
print(next(gen))