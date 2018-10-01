"""
K = input()
tourists = input().split()
# print(tourists)
tourists_cnt = {i:0 for i in set(tourists)}
# print(tourists_cnt)

for i in tourists:
    tourists_cnt[i] += 1
# print(tourists_cnt)

for i in tourists:
    if tourists_cnt[i] == 1:
        print(i)
        break
"""

k,arr = int(input()),list(map(int, input().split()))
myset = set(arr)
print(((sum(myset)*k)-(sum(arr)))//(k-1))
