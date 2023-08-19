def fun1(string1, dict1):
    for i in range(1, len(string1)):
        if string1[:i] in dict1:
            string2 = string1[i:]
            if not string2 or string2 in dict1:
                print("True")
            else:
                print("False")
                
s = "datacamp1"
dictionary = ["data", "camp", "cam", "lack"]

fun1(s, dictionary)


