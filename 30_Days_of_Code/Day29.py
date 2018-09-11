#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])
    
        """ Terminated due to timeout in Testcase 2...
        max_and = 0
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                val = i & j
                if(val < k and val > max_and):
                    max_and = val        
        print(max_and)
        """
        
        """
            P.S. 以下的推導不確定是否全面，只是根據討論的內容加以理解
        
            已知 
                K <= N
                A < B 且 A, B 屬於 S
            求 A&B < K，其理論上 A&B 的最大值為 K-1
            
            假設 K is odd (K-1 is even)
                則 (K-1) 與 K 的二進位只有最後一個位元有差別。推得 (K-1) & K = K-1 和 (K-1) | K = K <= N
                A=(K-1), B=K
                ex:
                    K   = 1011
                    K-1 = 1010
                    K-1 = (K-1) & K
                    K   = (K-1) | K <= N
                    
                             
            假設 K is even (K-1 is odd) 則有二個情況，先觀察
                ex: 
                    K        = 10110
                    K-1   = 10101
                    K|K-1 = 10111
                    
                可推得 (K-1) & (K|(K-1)) = (K-1)，所以若 (K|(K-1)) <= N時, 也可得 A&B 的最大值為 (K-1)
                但唯一不確定的是 K|(K-1) 是否 <= N
            
                case A. 若 K|(K-1) <= N
                    則 A&B < K 的最大值為 K-1
                    A=(K-1), B=K
                    
                
                case B. 若 K|(K-1) > N
                    則 A&B < K 的最大值 != K-1，其最大值該為何呢?
                    思考: 因為 K is even，推得 K-1 is odd
                    所以 ((K-1)-1) & (K-1) = (K-1) - 1 = K-2
                    我們至少可以找到 A&B = K-2 if A|B > N
                    A=(K-2), B=(K-1)
        """
        print(k-1 if ((k-1) | k) <= n else k-2)
