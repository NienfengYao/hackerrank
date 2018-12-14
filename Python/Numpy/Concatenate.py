import numpy as np

n, m, p = list(map(int, input().split()))
# print(n, m, p)
arr_n = np.array([input().split() for i in range(n)], int)
arr_m = np.array([input().split() for i in range(m)], int)
# print(arr_n, arr_m)
print(np.concatenate((arr_n, arr_m), axis = 0) )
