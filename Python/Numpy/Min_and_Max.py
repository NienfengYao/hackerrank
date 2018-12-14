import numpy as np

n, m = map(int, input().split())
arr = np.array([input().split() for _ in range(n)], np.int)
print(arr.min(axis=1).max())
