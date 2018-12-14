import numpy as np

# setting for output format
np.set_printoptions(legacy='1.13')
n, m = map(int, input().split())
arr = np.array([input().split() for _ in range(n)], np.float)
print(arr.mean(axis=1))
print(arr.var(axis=0))
print(arr.std())
