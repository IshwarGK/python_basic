dict1 = {
    "a": 1,
    "b": 2,
    "c": 3
}

dict2 = {
    "x": 11,
    "y": 12,
    "z": 13
}

dict3 = {
    "aa":33,
    "bb":44,
    "cc":55
}

dict1["d"] = 4

del dict1["b"]
dict1.pop("c")

#dict1.update(dict2)

dict1 = {**dict1, **dict2, **dict3}

# if 2 in dict1.values():
#     print("2 is present in dict1")
print(dict1)
print("Hi")
print("Bye")

for key, value in dict1.items():
    print(f"key={key}, values={value}")
    
    