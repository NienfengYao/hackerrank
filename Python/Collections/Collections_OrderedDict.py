# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict

"""
N = int(input())
items = OrderedDict()
for i in range(N):
    name, value = input().rsplit(maxsplit=1)
    value = int(value)
    if name in items.keys():
        items[name] += value
    else:
        items[name] = value

for i in items.items():
    print(i[0], i[1])
"""

d = OrderedDict()
for _ in range(int(input())):
    item, quantity = input().rsplit(maxsplit=1)
    d[item] = d.get(item, 0) + int(quantity)
for item, quantity in d.items():
    print(item, quantity)
