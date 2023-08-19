import collections
from collections import OrderedDict
from collections import namedtuple

list1 = [1, 2, 3, 3, 4, 5, 3, 1, 3, 4, 5]

list2 = collections.Counter(list1)
print(list2)
print(list2[7])

list3 = collections.deque(list1)
print(list3)

od = OrderedDict()
od["a"] = 1
od["v"] = 2
od["b"] = 3
od["c"] = 4

for key, val in od.items():
    print(key, val)
     
Student = namedtuple('Student', ['name', 'age', 'city'])
Ram = Student('Ram', '01', 'Pune')
Krsna = Student('Krsna', '01', 'Pune')

print(Ram.city)