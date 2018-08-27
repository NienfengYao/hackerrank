#!/bin/python3

import math
import os
import random
import re
import sys
import cProfile

# Complete the bigSorting function below.
def bigSorting(unsorted):
    unsorted.sort(key=int)
    return unsorted

# It got Compiler Message "Terminated due to timeout" on Testcase 3
def bigSorting_timeout(unsorted):
    sorted = list(map(int, unsorted))
    sorted.sort()
    return list(map(str, sorted))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
