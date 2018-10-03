#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

#define min(a, b) (a<b?a:b)

int main() 
{
    /*
    int n, N;
    int i, j, i_tmp;
    scanf("%d", &n);
    // Complete the code to print the pattern.
    N = 2*n -1;
    for(i=0; i<N; i++){
        for(j=0; j<N; j++){
            if(i<n)
                i_tmp = i;
            else
                i_tmp = N-i-1;

            if(i_tmp<=j && j<=(N-i_tmp-1) )
                printf("%d ", n-i_tmp);
            else if (i_tmp>j)
                printf("%d ", n-j);
            else
                printf("%d ", n - (N-j-1));
        }
        printf("\n");
    }
    */
    
    // Great solution, much simpler
    // Get the min distance to the four sides, 
    // wich is the differ between n and the number we wanted.
    int n, len, i, j, m;
    
    scanf("%d", &n);
    len = 2*n -1;
    for(i=0; i<len; i++){
        for(j=0; j<len; j++){
            // find the min distance to the foru sides
            // i, j, len-1-i, len-1-j
            m = min(i, j);
            m = min(m, len-1-i);
            m = min(m, len-1-j);
            printf("%d ", n-m);   
        }
        printf("\n");
    }
    
    return 0;
}
