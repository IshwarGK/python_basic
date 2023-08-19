def square_num(num):
    return num*num

list1 = [1, 2, 3, 4, 5]

sum1 = sum(list1)

print(sum1)

list2 = map(square_num, list1)

for i in list2:
    print(i)