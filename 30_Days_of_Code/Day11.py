#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []
    items = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    for i in range(6):
        if(i > 3):
            break
        for j in range(6):
            if (j > 3):
                continue
            # print(arr[i][j], arr[i][j+1], arr[i][j+2], arr[i+1][j+1], arr[i+2][j], arr[i+2][j+1], arr[i+2][j+2]) 
            value = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2] 
            items.append(value)
    print(max(items))
