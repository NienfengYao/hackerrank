n = int(input())
for i in range(n):
    a = input()
    A = set(input().split())
    b = input()
    B = set(input().split())    
    # print(A, B)
    """
    if ( len(A.union(B)) == len(B)):
        print(True)
    else:
        print(False)
    """
    
    if ( A.issubset(B)):
        print(True)
    else:
        print(False)
