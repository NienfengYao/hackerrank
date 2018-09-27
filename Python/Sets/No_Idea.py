# Very Important
# Note: Since  and  are sets, they have no repeated elements.
# However, the array might contain duplicate elements.

"""
# Terminated due to timeout
# It has bug here, H is not set. But I assume it's set.
# Even I solve the timeout issue, but it doens't work correctly.

n, m = map(int, input().split())
H, A, B = [list(map(int, input().split())) for _ in range(3)]
# print(n, m)
# print(H, A, B)
happ = 0
for i in H:
    if (i in A):
        happ += 1
    elif (i in B):
        happ -= 1     
print(happ)
"""

"""
# This works
n, m = map(int, input().split())
H = input().split()
A, B = [set(input().split()) for _ in range(2)]
happ = 0
for i in H:
    if (i in A):
        happ += 1
    elif (i in B):
        happ -= 1     
print(happ)
"""

n, m = input().split()
sc_ar = input().split()
A = set(input().split())
B = set(input().split())
# sc_ar, A, B = [set(input().split()) for _ in range(3)]   # doesn't work
print(sum((i in A) - (i in B) for i in sc_ar))
