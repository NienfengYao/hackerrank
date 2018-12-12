import sys
from collections import deque

for _ in range(int(input())):
    n, d = int(input()), deque(map(int, input().split()))
    # print(n, d)
    size = sys.maxsize
    ret = True
    for _ in range(n):
        if(d[0] >= d[-1]):
            val = d[0]
            d.pop()
        else:
            val = d[-1]
            d.popleft()
        if val > size:
            ret = False
        else:
            size = val
    print("Yes") if ret else print("No")
