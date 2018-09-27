n = int(input())
s = set(map(int, input().split()))
n = int(input())
for i in range(n):
    args = input()
    if args.split()[0] == 'pop':
        eval("s." + 'pop()')
    else:
        cmd, arg = args.split()
        eval("s." + cmd + "(%s)" % arg)
    
print(sum(s))
