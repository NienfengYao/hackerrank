#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    # print("{0:b}".format(n))
    s = "{0:b}".format(n)
    # print(s)
    # print(re.findall(r'1{1,}', s))
    max_cnt = 0
    for i in re.findall(r'1{1,}', s):
        # print(type(i), i, len(i))
        if max_cnt < (len(i)):
            max_cnt = len(i)

    print(max_cnt)
