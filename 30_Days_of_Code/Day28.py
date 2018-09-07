#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())

    pattern = re.compile("@gmail.com")
    names = []
    for N_itr in range(N):
        firstNameEmailID = input().split()
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]
        if(pattern.search(emailID)):
            names.append(firstName)
    names.sort()
    print("\n".join(names))
