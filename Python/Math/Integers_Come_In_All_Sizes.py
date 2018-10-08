"""
Integers in Python can be as big as the bytes in your machine's memory. 
There is no limit in size as there is:  (c++ int) or  (C++ long long int).
"""
a, b, c, d = [int(input()) for _ in range(4)]
# print(a, b, c, d)
print(pow(a, b) + pow(c, d))
