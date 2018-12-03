# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

_, stock, N = [input(), Counter(input().split()), int(input())]
# print(stock, N)
value = 0

for i in range(N):
    size, price = (input().split())
    #print(size, price)
    if(stock[size] > 0):
        stock[size] -= 1
        value += int(price) 

print(value)
