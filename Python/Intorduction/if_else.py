#!/bin/python3

N = int(input())
if (N%2 == 1):
    print("Weird")
elif (2 <= N and N <= 5):
    print("Not Weird")
elif (6 <= N and N <= 20):
    print("Weird")
elif (N>20):
    print("Not Weird")
