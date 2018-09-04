"""
Ref: [求質數演算法的N種境界](https://www.getit01.com/p201807213917086/)
"""
import math

def isPrime_n(data):
    if (data == 2):
        print("Prime")
        return
    elif ((data == 1) or (data % 2 == 0)):
        print("Not prime")
        return
    
    squart_root = int(math.sqrt(data))
    # print("squart_root:", squart_root)
    for i in range(3, squart_root+1):
        if data % i == 0:
            print("Not prime")
            return     

    print("Prime")
    return

T = int(input())
for i in range(T):
    data = int(input())
    isPrime_n(data)
