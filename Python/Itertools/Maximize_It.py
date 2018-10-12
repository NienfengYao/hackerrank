from itertools import product

"""
def f(pro, m):
    return sum(pow(i, 2) for i in pro) % m

k, m = map(int, input().split())
# print(k, m)
N = []
for i in range(k):
    # Note: the first input is the quantity, not the content
    N.append(list(map(int, input().split()[1:])))
# print(N)
# print(list(product(*N)))
print(max([f(pro, m)for pro in product(*N)]))
"""


K,M = map(int,input().split())
N = (list(map(int, input().split()))[1:] for _ in range(K))
print(max(map(lambda x: sum(i**2 for i in x)%M, product(*N))))
