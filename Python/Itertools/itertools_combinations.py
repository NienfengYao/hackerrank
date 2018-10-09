"""
Elements are treated as unique based on their position, not on their value
"""

from itertools import combinations

S, k = input().split()
k = int(k)
# print(S, k)
for i in range(1, k+1):
    for j in (combinations(sorted(S), i)):
        print("".join(j))
