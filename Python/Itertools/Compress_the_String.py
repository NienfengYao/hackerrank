from itertools import groupby

"""
S = input()
for k, g in groupby(S):
    # print(k, list(g))
    print((len(list(g)), int(k)), end=' ')
"""

print(*[(len(list(g)), int(k)) for k, g in groupby(input())])
