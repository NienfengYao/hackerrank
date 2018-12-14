import numpy as np

n, m = list(map(int, input().split()))
# print(n, m)
arr = []
for _ in range(n):
    arr.extend(input().split())
# print(arr)
arr = np.array(arr, int).reshape((n, m))
# arr = np.array(arr, int)
# arr = arr.reshape((n, m))
print(arr.transpose())
print(arr.flatten())
