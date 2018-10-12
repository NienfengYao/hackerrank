from itertools import combinations

_, N, k = input(), input().split(), int(input())
C = list(combinations(N, k))
# print(C)
# print(len([i for i in C if 'a' in i]), len(C))
print(len([i for i in C if 'a' in i])/len(C))
