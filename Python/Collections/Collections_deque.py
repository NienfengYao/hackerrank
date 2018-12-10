# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import deque

d = deque()
""" first implement"
for i in range(int(input())):
    cmds = input().split()
    if(len(cmds) > 1):
        eval("d.%s(%s)" % (cmds[0], cmds[1]))
    else:
        eval("d.%s()" % cmds[0])
for i in d:
    print(i, end=" ")
"""

for _ in range(int(input())):
    inp = input().split()
    getattr(d, inp[0])(*[inp[1]] if len(inp) > 1 else [])
    print(*[inp[1]] if len(inp) > 1 else [])
print(*[item for item in d])
