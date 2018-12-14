import numpy as np

n, m = map(int, input().split())
# print(n, m)
A = np.array([input().split() for _ in range(n)], np.int)
B = np.array([input().split() for _ in range(n)], np.int)
# print(A, B)
print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)
print(A ** B)
