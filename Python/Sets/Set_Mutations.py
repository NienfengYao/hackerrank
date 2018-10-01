# A.update(B) or A|=B
# A.intersection_update(B) or A&=B
# A.difference_update(B) or A-=B
# A.symmetric_difference_update(B) or A^=B

"""
n = input()
A = set(map(int, input().split()))
n = int(input())

for i in range(n):
    cmd = input().split()[0]
    N = set(map(int, input().split()))
    eval("A.{}(N)".format(cmd))

print(sum(A))
"""

(_, A) = (input(), set(map(int, input().split())))
for i in range(int(input())):
    (cmd, B) = (input().split()[0], set(map(int, input().split())))
    getattr(A, cmd)(B)
    
print(sum(A))
