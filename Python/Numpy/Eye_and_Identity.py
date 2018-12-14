import numpy as np

# To fix the ouput format bug
np.set_printoptions(sign=' ')
n, m = map(int, input().split())
# print(n, m)
print(np.eye(n, m))
