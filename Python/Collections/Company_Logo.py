#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


"""
key is the sort funciton.
"""
if __name__ == '__main__':
    s = input()
    c = Counter(s)
    most = c.most_common()  # most is a list
    # we sort the list, and sort order is counter first, then alphabet later
    most.sort(key=lambda tup: (-tup[1], tup[0]))
    for i in most[:3]:
        print(i[0], i[1])

