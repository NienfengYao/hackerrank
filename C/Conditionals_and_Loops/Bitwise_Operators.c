#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
//Complete the following function.


void calculate_the_maximum(int n, int k) {
  //Write your code here.
    int and, or, xor;
    int i, j;
    
    and = or = xor = 0;
    for(i=1; i<n; i++){
        for(j=i+1; j<=n; j++){                        
            if(((i&j) < k) && ((i&j) > and)){
                and = i&j;
            }
            if(((i|j) < k) && ((i|j) > or))
                or = i|j;
            if(((i^j) < k) && ((i^j) > xor))
                xor = i^j;    
            // printf("%d, %d, %d, %d, %d, %d, %d, %d\n", i, j, i&j, i|j, i^j, and, or, xor);
        }
    }
    printf("%d\n%d\n%d\n", and, or, xor);
}

int main() {
    int n, k;
  
    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);
 
    return 0;
}
