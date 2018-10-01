"""
A = set(input().split())
n = int(input())

flag = True
for i in range(n):
    N = set(input().split())
    if N < A:
        continue
    else:
        flag = False
        break
        
if (flag):
    print(True)
else:
    print(False)
"""

A = set(input().split())
print(all(A > set(input().split()) for _ in range(int(input()))))
