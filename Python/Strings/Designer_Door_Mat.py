n, m = map(int, input().split())
c1, c2 = ['.|.', '-']
# print(n, m, c1, c2)

for i in range(n):
    if(i < (n-1)/2):
        print((c1*(i*2+1)).center(m, c2))
    elif(i == (n-1)/2):
        print("WELCOME".center(m, c2))
    else:
        print((c1*(((n-1)-i)*2+1)).center(m, c2))
