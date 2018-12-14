import numpy as np

n, m = map(int, input().split())
# print(n, m)
arr = np.array([input().split() for _ in range(n)], np.int)
# print(arr)
print(arr.sum(axis=0).prod())
