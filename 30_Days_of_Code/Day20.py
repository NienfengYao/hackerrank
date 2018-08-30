#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
numSwaps = 0 

for i in range(len(a)):
    numberOfSwaps = 0
    for j in range(len(a)-1):
        if(a[j] > a[j+1]):
            tmp = a[j]
            a[j] = a[j+1]
            a[j+1] = tmp
            numberOfSwaps += 1
    numSwaps += numberOfSwaps
    
    if (numberOfSwaps == 0):
        break
        
print("Array is sorted in %d swaps." % numSwaps)
print("First Element: %d" % a[0])
print("Last Element: %d" % a[-1])
