from collections import deque
from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict


dict1 = defaultdict(int)

dict1['a'] = 1
print(dict1['b'])


dict1 = OrderedDict()
dict1['a'] = 1
dict1['b'] = 2
dict1['c'] = 3

print(type(dict1))
for k, v in dict1.items():
    print(k, v)


Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(type(p.y))
print(type(Point))

list1 = [1, 1, 2, 3, 3, 3, 2, 1]

counter1 = Counter(list1)

print(counter1[2])