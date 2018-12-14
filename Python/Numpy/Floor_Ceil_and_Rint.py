import numpy as np

# for meet output format
np.set_printoptions(sign=' ')
arr = np.array(input().split(), np.float)
# print(arr)
print(np.floor(arr))
print(np.ceil(arr))
print(np.rint(arr))
