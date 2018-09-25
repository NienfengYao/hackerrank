from itertools import permutations

s, k = input().split()
"""
k = int(k)
rel = []
for i in permutations(s, k):
    rel.append("".join(i))

rel.sort()
print("\n".join(rel))
"""

print(*["".join(i) for i in permutations(sorted(s), int(k))], sep='\n')
