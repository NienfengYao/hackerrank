"""
1. pow(1,2)=1 pow(11,2)=121 pow(111,2)=12321 pow(1111,2)=1234321...
2. In Python 3 the behaviour for / is float division and integer division is //
"""


for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(int(pow((pow(10, i)-1)//9, 2))) 
