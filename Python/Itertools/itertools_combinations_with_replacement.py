from itertools import combinations_with_replacement

S, k = input().split()
k = int(k)
for i in combinations_with_replacement(sorted(S), k):
    print("".join(i))
