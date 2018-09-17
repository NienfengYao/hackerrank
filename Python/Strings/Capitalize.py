#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    """
    # issue: doesn't solve if space > 1
    s = [i.capitalize() for i in s.split()]
    return " ".join(s)
    """

    for i in s[:].split():
        s = s.replace(i, i.capitalize())        
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()
