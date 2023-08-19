list1 = [0, 1, 2, 3, 4, 5]

def even_no(num1):
    if num1%2 == 0:
        return True
    return False

list2 = filter(even_no, list1)

print(list(list2))