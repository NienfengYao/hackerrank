"""
m = int(input())
M = set(map(int, input().split()))
n = int(input())
N = set(map(int, input().split()))
# print(m, n, M, N)
res = sorted(list(M.difference(N)) + list(N.difference(M)))
res = list(map(str, res))
print("\n".join(res))
"""

"""
m = int(input())
M = set(input().split())
n = int(input())
N = set(input().split())
res = M.difference(N).union(N.difference(M))
print("\n".join(sorted(res, key=int)))
"""

M, N = [set(input().split()) for _ in range(4)][1::2]
# print(M, N)
print("\n".join(sorted(M.difference(N).union(N.difference(M)), key=int)))
