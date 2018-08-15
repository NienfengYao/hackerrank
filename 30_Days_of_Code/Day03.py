#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    val = meal_cost * (1.0 + (tip_percent/100.0) + (tax_percent/100.0))
    return int(round(val))

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    total = solve(meal_cost, tip_percent, tax_percent)
    print("The total meal cost is %d dollars." % total)

