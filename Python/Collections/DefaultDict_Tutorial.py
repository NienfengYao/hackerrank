# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import defaultdict
n, m = input().split()
# print(n, m, type(n), type(m))
A = defaultdict(list)

for i in range(int(n)):
    A[input()].append(str(i+1))
print(A)

for i in range(int(m)):
    key = input()
    if (not A[key]):
        print(-1)
    else:
        print(" ".join(A[key]))
